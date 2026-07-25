#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


CSS = """
*{box-sizing:border-box}
html,body{margin:0;background:#050608;color:#fff;font-family:-apple-system,BlinkMacSystemFont,'Hiragino Kaku Gothic ProN','Yu Gothic',Meiryo,sans-serif}
.slide{width:1280px;height:720px;position:relative;overflow:hidden;page-break-after:always;padding:58px 78px;background:radial-gradient(circle at 78% 22%,rgba(255,255,255,.13),transparent 24%),linear-gradient(135deg,#07080a,#222933 62%,#111)}
.slide.light{background:#f7f7f4;color:#111}
.slide.gold{background:linear-gradient(135deg,#090909,#2a261c 58%,#111)}
.num{position:absolute;right:54px;top:34px;font-size:88px;font-weight:950;opacity:.16}
.wm{position:absolute;right:-18px;bottom:-96px;font-size:285px;font-weight:1000;opacity:.07;letter-spacing:-.08em}
.kicker{font-size:21px;letter-spacing:.14em;color:#f2d65c;font-weight:950;margin-bottom:18px}
h1{font-size:68px;line-height:1.08;margin:0;font-weight:950;letter-spacing:0}
h2{font-size:42px;line-height:1.2;margin:0 0 18px;font-weight:950}
p{font-size:27px;line-height:1.58;margin:24px 0 0;max-width:930px}
.small{font-size:19px;opacity:.75}
.cover-layout{display:grid;grid-template-columns:minmax(0,1fr) 430px;gap:58px;align-items:center;height:100%}
.visual{height:420px;border:1px solid rgba(255,255,255,.18);border-radius:24px;background:linear-gradient(135deg,rgba(255,255,255,.16),rgba(255,255,255,.045));display:grid;place-items:center;text-align:center;font-size:33px;font-weight:950;padding:28px}
.light .visual{background:#fff;border-color:#d7d7d7;color:#111}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:32px}
.cards.two{grid-template-columns:repeat(2,1fr)}
.cards.four{grid-template-columns:repeat(4,1fr)}
.card{border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.08);border-radius:17px;padding:23px;min-height:134px}
.light .card{background:#fff;border-color:#d6d6d6}
.card b{display:block;font-size:31px;line-height:1.18;margin-bottom:10px}
.card span{font-size:19px;line-height:1.52;opacity:.82}
.quote{display:grid;place-items:center;text-align:center;height:100%;padding:0 90px}.quote h1{font-size:76px}.quote p{margin-left:auto;margin-right:auto}
.split-layout{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center;height:100%}
.steps{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:42px}
.step{border-top:5px solid #f2d65c;background:rgba(255,255,255,.08);padding:18px;border-radius:12px;min-height:190px}
.light .step{background:#fff;border:1px solid #ddd;border-top:5px solid #111}
.step b{font-size:24px}.step span{display:block;margin-top:10px;font-size:17px;line-height:1.55}
.evidence{display:grid;grid-template-columns:1.2fr .8fr;gap:28px;align-items:stretch;margin-top:30px}
.panel{border:1px solid rgba(255,255,255,.2);border-radius:18px;padding:26px;background:rgba(255,255,255,.08)}
.light .panel{background:#fff;border-color:#ddd}
.panel ul{margin:12px 0 0;padding-left:1.2em}.panel li{font-size:22px;line-height:1.62;margin:6px 0}
.note{position:absolute;left:78px;bottom:28px;font-size:15px;opacity:.58}
"""


def esc(v) -> str:
    return html.escape(str(v or ""))


def card_html(cards, cls="cards"):
    return "<div class='%s'>%s</div>" % (cls, "".join(f"<div class='card'><b>{esc(c.get('title'))}</b><span>{esc(c.get('body'))}</span></div>" for c in cards))


def render(s: dict, idx: int) -> str:
    layout = s.get("layout", "message")
    theme = " " + s.get("theme", "") if s.get("theme") else ""
    base = [f"<section class='slide layout-{layout}{theme}'>", f"<div class='num'>{idx:02d}</div><div class='wm'>A</div>"]
    kicker = f"<div class='kicker'>{esc(s.get('kicker'))}</div>" if s.get("kicker") else ""
    if layout == "cover":
        base.append("<div class='cover-layout'><div>")
        base.append(kicker + f"<h1>{esc(s.get('title'))}</h1><p>{esc(s.get('body'))}</p></div><div class='visual'>{esc(s.get('visual','Main visual'))}</div></div>")
    elif layout == "proof":
        base.append(kicker + f"<h1>{esc(s.get('title'))}</h1>" + card_html(s.get("cards", []), "cards"))
    elif layout == "four":
        base.append(kicker + f"<h1>{esc(s.get('title'))}</h1>" + card_html(s.get("cards", []), "cards four"))
    elif layout == "quote":
        base.append(f"<div class='quote'><div>{kicker}<h1>{esc(s.get('title'))}</h1><p>{esc(s.get('body'))}</p></div></div>")
    elif layout == "split":
        base.append("<div class='split-layout'><div>" + kicker + f"<h1>{esc(s.get('title'))}</h1><p>{esc(s.get('body'))}</p></div><div class='visual'>{esc(s.get('visual','Visual'))}</div></div>")
    elif layout == "steps":
        steps = "".join(f"<div class='step'><b>{esc(x.get('title'))}</b><span>{esc(x.get('body'))}</span></div>" for x in s.get("steps", []))
        base.append(kicker + f"<h1>{esc(s.get('title'))}</h1><div class='steps'>{steps}</div>")
    elif layout == "evidence":
        items = "".join(f"<li>{esc(x)}</li>" for x in s.get("items", []))
        base.append(kicker + f"<h1>{esc(s.get('title'))}</h1><div class='evidence'><div class='panel'><h2>{esc(s.get('left_title','証拠'))}</h2><ul>{items}</ul></div><div class='visual'>{esc(s.get('visual','Evidence'))}</div></div>")
    else:
        base.append(kicker + f"<h1>{esc(s.get('title'))}</h1><p>{esc(s.get('body'))}</p>")
    if s.get("note"):
        base.append(f"<div class='note'>{esc(s.get('note'))}</div>")
    base.append("</section>")
    return "".join(base)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("json_path")
    ap.add_argument("-o", "--output", default="slides/index.html")
    args = ap.parse_args()
    slides = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    doc = "<!doctype html><html lang='ja'><meta charset='utf-8'><meta name='viewport' content='width=1280'><style>" + CSS + "</style><body>" + "".join(render(s, i) for i, s in enumerate(slides, 1)) + "</body></html>"
    out.write_text(doc, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
