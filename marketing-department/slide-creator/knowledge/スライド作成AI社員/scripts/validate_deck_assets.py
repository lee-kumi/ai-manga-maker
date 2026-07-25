#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

SRC_RE = re.compile(r"(?:src|href)=[\"']([^\"']+)[\"']")

def main() -> int:
    ap = argparse.ArgumentParser(description="HTMLデッキ内の相対素材欠落を検査する")
    ap.add_argument("html_file")
    args = ap.parse_args()
    html_file = Path(args.html_file)
    text = html_file.read_text(encoding="utf-8")
    missing = []
    for ref in SRC_RE.findall(text):
        if ref.startswith(("http://","https://","data:","#","mailto:","tel:")):
            continue
        target = (html_file.parent / ref.split("?")[0].split("#")[0]).resolve()
        if not target.exists():
            missing.append(ref)
    if missing:
        print("missing assets")
        for m in missing:
            print(m)
        return 1
    print("OK: all local assets exist")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
