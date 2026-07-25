#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser(description="動画から一定間隔でスライド候補画像を抽出する")
    ap.add_argument("video")
    ap.add_argument("-o", "--out-dir", default="assets/video-frames")
    ap.add_argument("--fps", default="1/5", help="5秒に1枚なら 1/5")
    ap.add_argument("--ffmpeg", default="ffmpeg")
    args = ap.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    pattern = str(out / "frame_%04d.jpg")
    cmd = [args.ffmpeg, "-y", "-i", args.video, "-vf", f"fps={args.fps}", "-q:v", "2", pattern]
    subprocess.run(cmd, check=True)
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
