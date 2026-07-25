#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
from datetime import date
from pathlib import Path

BASE_CSS = """
:root{
  --bg:#101318;
  --panel:#171b22;
  --text:#f7f7f2;
  --muted:#b7bcc7;
  --accent:#f2d45c;
  --line:rgba(255,255,255,.15);
}
*{box-sizing:border-box}
body{margin:0;background:#090b0f;color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Noto Sans JP','Hiragino Sans',sans-serif}
.deck{width:100vw;min-height:100vh}
.slide{width:1280px;height:720px;position:relative;overflow:hidden;padding:64px 78px;display:flex;flex-direction:column;justify-content:center;background:linear-gradient(135deg,#11151c 0%,#2b313b 72%,#151920 100%);page-break-after:always}
.slide.light{background:#fbfbf7;color:#111}
.slide.cover{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center}
.slide.question{background:#fbfbf7;color:#111}
.slide.bridge{background:radial-gradient(circle at 74% 50%,rgba(255,255,255,.1),transparent 28%),linear-gradient(135deg,#151920,#3a414c)}
.brand-mark{position:absolute;right:70px;bottom:42px;font-size:92px;font-weight:900;opacity:.075}
.no{position:absolute;right:64px;top:40px;font-size:90px;line-height:1;font-weight:900;opacity:.16}
.kicker{font-size:21px;letter-spacing:.14em;color:var(--accent);font-weight:900;text-transform:uppercase;margin-bottom:20px}
h1{font-size:72px;line-height:1.08;letter-spacing:0;margin:0 0 24px;font-weight:900}
h2{font-size:54px;line-height:1.12;margin:0 0 18px;font-weight:900}
p,.body{font-size:30px;line-height:1.58;margin:0;max-width:1000px}
.lead{font-size:34px;line-height:1.5;color:var(--muted)}
.light .lead,.light p{color:#222}
.yellow{color:var(--accent)}
.blackbar{display:inline-block;background:#050505;color:var(--accent);padding:.08em .18em}
.grid{display:grid;gap:24px}
.cols-2{grid-template-columns:1fr 1fr}
.cols-3{grid-template-columns:repeat(3,1fr)}
.card{border:1px solid var(--line);background:rgba(255,255,255,.06);padding:28px;min-height:150px}
.light .card{background:#fff;border-color:#d8d8d2}
.card h3{font-size:34px;margin:0 0 12px}
.card p{font-size:22px;line-height:1.55}
.proof-wall{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;align-items:center}
.proof-wall img{width:100%;height:116px;object-fit:contain;background:#fff;border:1px solid #ddd}
.media{width:100%;height:auto;max-height:540px;object-fit:contain}
.cover-img{width:100%;max-height:540px;object-fit:contain;background:#fff}
.caption{position:absolute;left:78px;bottom:38px;color:var(--muted);font-size:17px}
.center{text-align:center;align-items:center}
.center h1,.center p{margin-left:auto;margin-right:auto}
"""

def esc(value: object) -> str:
    return html.escape(str(value or ""))

def image_tag(src: str, cls: str = "media") -> str:
    if not src:
        return ""
    return f"<img class='{cls}' src='{esc(src)}' alt=''>"

def render_slide(slide: dict, index: int) -> str:
    t = slide.get("type", "message")
    theme = slide.get("theme", "dark")
    classes = ["slide", theme]
    if t in {"cover", "question", "bridge"}:
        classes.append(t)
    if slide.get("align") == "center":
        classes.append("center")
    parts = [f"<section class='{' '.join(classes)}'>", f"<div class='no'>{index}</div>"]
    if t == "cover":
        parts.append("<div>")
        if slide.get("kicker"):
            parts.append(f"<div class='kicker'>{esc(slide['kicker'])}</div>")
        parts.append(f"<h1>{esc(slide.get('title'))}</h1>")
        if slide.get("body"):
            parts.append(f"<p class='lead'>{esc(slide['body']).replace(chr(10), '<br>')}</p>")
        parts.append("</div>")
        parts.append(f"<div>{image_tag(slide.get('image',''), 'cover-img')}</div>")
    elif t == "cards":
        if slide.get("kicker"):
            parts.append(f"<div class='kicker'>{esc(slide['kicker'])}</div>")
        parts.append(f"<h1>{esc(slide.get('title'))}</h1>")
        cards = slide.get("cards", [])
        col_class = "cols-3" if len(cards) >= 3 else "cols-2"
        parts.append(f"<div class='grid {col_class}'>")
        for c in cards:
            parts.append(f"<div class='card'><h3>{esc(c.get('title'))}</h3><p>{esc(c.get('body')).replace(chr(10), '<br>')}</p></div>")
        parts.append("</div>")
    elif t == "proof_wall":
        if slide.get("kicker"):
            parts.append(f"<div class='kicker'>{esc(slide['kicker'])}</div>")
        parts.append(f"<h1>{esc(slide.get('title'))}</h1>")
        parts.append("<div class='proof-wall'>")
        for img in slide.get("images", []):
            parts.append(image_tag(img, ""))
        parts.append("</div>")
    elif t == "media_left":
        parts.append("<div class='grid cols-2' style='align-items:center'>")
        parts.append(f"<div>{image_tag(slide.get('image',''))}</div><div>")
        if slide.get("kicker"):
            parts.append(f"<div class='kicker'>{esc(slide['kicker'])}</div>")
        parts.append(f"<h1>{esc(slide.get('title'))}</h1>")
        if slide.get("body"):
            parts.append(f"<p>{esc(slide['body']).replace(chr(10), '<br>')}</p>")
        parts.append("</div></div>")
    else:
        if slide.get("kicker"):
            parts.append(f"<div class='kicker'>{esc(slide['kicker'])}</div>")
        parts.append(f"<h1>{esc(slide.get('title'))}</h1>")
        if slide.get("body"):
            parts.append(f"<p>{esc(slide['body']).replace(chr(10), '<br>')}</p>")
        parts.append("<div class='brand-mark'>A</div>")
    if slide.get("caption"):
        parts.append(f"<div class='caption'>{esc(slide['caption'])}</div>")
    parts.append("</section>")
    return "\n".join(parts)

def write_project(plan: dict, out_dir: Path) -> None:
    (out_dir / "assets").mkdir(parents=True, exist_ok=True)
    (out_dir / "screenshots" / "final").mkdir(parents=True, exist_ok=True)
    (out_dir / "slides").mkdir(parents=True, exist_ok=True)
    slides = plan.get("slides", [])
    html_doc = "<!doctype html><meta charset='utf-8'><meta name='viewport' content='width=1280'><title>" + esc(plan.get("title", "deck")) + "</title><style>" + BASE_CSS + "</style><main class='deck'>" + "\n".join(render_slide(s, i) for i, s in enumerate(slides, 1)) + "</main>"
    (out_dir / "slides" / "index.html").write_text(html_doc, encoding="utf-8")
    for name, body in {
        "brief.md": plan.get("brief", "# Brief\n\n"),
        "questions.md": plan.get("questions", "# Questions\n\n"),
        "story-plan.md": plan.get("story_plan", "# Story Plan\n\n"),
        "source-map.md": plan.get("source_map", "# Source Map\n\n"),
        "review-notes.md": "# Review Notes\n\n- [ ] full screenshot QA\n- [ ] ratios preserved\n- [ ] no text-only cheap slides\n- [ ] evidence and CTA verified\n",
    }.items():
        (out_dir / name).write_text(body, encoding="utf-8")

def main() -> int:
    ap = argparse.ArgumentParser(description="07標準のHTMLスライド案件フォルダを作る")
    ap.add_argument("plan_json", help="deck-plan.json")
    ap.add_argument("-o", "--output-dir", default=None)
    args = ap.parse_args()
    plan = json.loads(Path(args.plan_json).read_text(encoding="utf-8"))
    slug = plan.get("slug", "seminar-deck")
    out_dir = Path(args.output_dir or f"output/archive/{date.today().isoformat()}_{slug}")
    write_project(plan, out_dir)
    print(out_dir)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
