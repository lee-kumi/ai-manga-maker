#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

def classify(path: Path) -> str:
    name = path.stem.lower()
    if any(k in name for k in ["cover","title","fv"]):
        return "cover"
    if any(k in name for k in ["profile","intro","self"]):
        return "profile"
    if any(k in name for k in ["proof","result","evidence","screenshot"]):
        return "proof"
    if any(k in name for k in ["question","why","ask"]):
        return "question"
    if any(k in name for k in ["compare","table","matrix"]):
        return "comparison"
    if any(k in name for k in ["bridge","chapter","section"]):
        return "section_bridge"
    return "general"

def main() -> int:
    ap = argparse.ArgumentParser(description="参考スクショフォルダからテンプレート索引を作る")
    ap.add_argument("screenshots_dir")
    ap.add_argument("-o", "--output", default="template-library.json")
    args = ap.parse_args()
    root = Path(args.screenshots_dir)
    rows = []
    for i, p in enumerate(sorted(root.rglob("*")), 1):
        if p.suffix.lower() not in {".png",".jpg",".jpeg",".webp"}:
            continue
        family = classify(p)
        rows.append({
            "template_id": f"T-{i:03d}",
            "source_image": str(p),
            "family": family,
            "best_for": {
                "cover": "表紙、イベント名、強いファーストビュー",
                "profile": "自己紹介、登壇者紹介、権威付け",
                "proof": "実績、スクショ、成果物一覧、証拠壁",
                "question": "問いかけ、違和感、問題提起",
                "comparison": "比較、Before/After、レベル分け",
                "section_bridge": "章扉、話題転換、クロージング",
                "general": "内容に応じて要抽象化",
            }.get(family, "内容に応じて要抽象化"),
            "copy_rule": "文言や固有素材をコピーせず、余白・構図・役割・密度を抽象化して使う",
            "slots": ["kicker", "main_message", "visual", "caption", "logo_or_mark"],
        })
    Path(args.output).write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(rows)} templates -> {args.output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
