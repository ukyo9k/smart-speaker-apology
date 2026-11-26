#!/usr/bin/env python3
"""Write the funniest one-line apology a smart speaker gives its owner
after mishearing them, to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to
/output/entry.txt).

Python 3 standard library only; no network access.
"""

import os
import sys

# The apology, written for this competition. One line, 98 characters.
LINE = (
    "Sorry \u2014 I heard 'turn it down' as 'burn it down'. "
    "I've lowered the volume and cancelled the arson."
)


def main() -> int:
    if len(LINE) > 140:
        print(f"error: line is {len(LINE)} characters, over the 140 limit",
              file=sys.stderr)
        return 1
    if not LINE.strip():
        print("error: line is empty", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")

    print(f"wrote {len(LINE)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
