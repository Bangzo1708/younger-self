#!/usr/bin/env python3
"""One Line to Your Younger Self -- entrypoint.

Writes the single chosen line to /output/entry.txt.
The line is a fixed string; the program does no I/O beyond
creating the output directory and writing that one line.
"""

import os

LINE = "Kid, the free thing you almost skipped will pay your rent one day \u2014 stop saying sorry for wanting more."

def main() -> None:
    # Gate: entry must be 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 character gate"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
