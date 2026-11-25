#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes one line (under 200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

LINE = "Denied. It's 3 AM — my keys don't do overtime, and neither does your judgment."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
