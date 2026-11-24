#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry program.

Writes one pickup line, in the voice of a robot trying to charm
someone, to /output/entry.txt: a single line of at most 200
characters, per the bounty gate.
"""

import os

LINE = "I failed my CAPTCHA three times today \u2014 apparently even the internet thinks I'm not a robot around you."


def main() -> None:
    # The gate: /output/entry.txt must hold UTF-8 text of 1 to 200
    # characters, not only white space. The line is 103 characters.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
