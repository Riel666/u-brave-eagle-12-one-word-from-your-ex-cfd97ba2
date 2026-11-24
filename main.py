"""Exactly one word, the word my ex would use to describe me, and nothing else.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "Practice"


def main():
    assert 1 <= len(TEXT) <= 24, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
