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

    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")

    # Verify the file round-trips: exactly the line plus one trailing newline.
    with open(out_path, "r", encoding="utf-8", newline="") as fh:
        if fh.read() != LINE + "\n":
            print("error: written entry does not match the line", file=sys.stderr)
            return 1

    print(f"wrote {len(LINE)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
