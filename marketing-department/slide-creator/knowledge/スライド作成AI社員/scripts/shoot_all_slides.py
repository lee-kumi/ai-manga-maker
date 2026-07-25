#!/usr/bin/env python3
"""全ページスクショの自動撮影 — 俯瞰QA（同型連続・余白崩れ・文字はみ出し）の目を機械で用意する

07-seminar-style のデッキ（#1, #2, … のハッシュでページ送りするHTML）を、
headless Chrome でページごとに撮影して `screenshots/final/slide_001.png…` に並べる。
手動で「#2に変えて撮る」を繰り返す作業の置き換え。

使い方:
  python3 scripts/shoot_all_slides.py slides/index.html
  python3 scripts/shoot_all_slides.py slides/index.html --count 26 --out screenshots/final
  python3 scripts/shoot_all_slides.py slides/index.html --mode single   # 縦長デッキは1枚の全景で撮る

前提: Google Chrome（パスが違う場合は --chrome で指定）
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

DEFAULT_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def count_slides(html: Path) -> int:
    text = html.read_text(encoding="utf-8", errors="replace")
    n = len(re.findall(r"<section\b", text))
    return n or 1


def main() -> int:
    ap = argparse.ArgumentParser(description="デッキ全ページをheadless Chromeで撮影する")
    ap.add_argument("html_file")
    ap.add_argument("--count", type=int, default=0, help="ページ数（省略時は<section>を数える）")
    ap.add_argument("--out", default="screenshots/final")
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=720)
    ap.add_argument("--chrome", default=DEFAULT_CHROME)
    ap.add_argument("--mode", choices=["hash", "single"], default="hash",
                    help="hash=#1,#2…でページ送りするデッキ / single=縦長デッキを1枚で")
    args = ap.parse_args()

    html = Path(args.html_file).resolve()
    if not html.exists():
        print(f"FAIL: {html} が無い")
        return 1
    chrome = args.chrome
    if not Path(chrome).exists():
        print(f"FAIL: Chromeが見つからない: {chrome}（--chrome で指定）")
        return 1
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    url = html.as_uri()
    # 普段使いのChromeとプロファイルを分ける（分けないと起動競合で1枚数十秒かかることがある）
    profile = tempfile.mkdtemp(prefix="deck_shot_profile_")
    base_cmd = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                "--no-first-run", "--disable-extensions",
                f"--user-data-dir={profile}",
                "--virtual-time-budget=8000",
                f"--window-size={args.width},{args.height}"]

    if args.mode == "single":
        # 縦長デッキ: ページ全体の高さを推定できないため十分な高さで1枚
        shot = out / "full_page.png"
        subprocess.run(base_cmd[:-1] + [f"--window-size={args.width},20000",
                                        f"--screenshot={shot}", url],
                       check=True, capture_output=True)
        print(f"OK: {shot}")
        return 0

    n = args.count or count_slides(html)
    ok = 0
    for i in range(1, n + 1):
        shot = out / f"slide_{i:03d}.png"
        subprocess.run(base_cmd + [f"--screenshot={shot}", f"{url}#{i}"],
                       capture_output=True)
        # Chromeは成功時も非0を返すことがあるため、成功判定はファイル実在で行う
        if shot.exists() and shot.stat().st_size > 1000:
            ok += 1
        else:
            print(f"WARN: {i}ページ目の撮影に失敗", file=sys.stderr)
    print(f"OK: {ok}/{n} 枚を {out}/ に保存した。並べて俯瞰し、同型連続・余白崩れ・はみ出しを潰す。")
    return 0 if ok == n else 1


if __name__ == "__main__":
    raise SystemExit(main())
