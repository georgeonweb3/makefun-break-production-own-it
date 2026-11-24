#!/usr/bin/env python3
"""Break Production, Own It entry.

One line, under 200 characters: what an AI agent prints the instant
it breaks production.
"""
import os

ENTRY = "The deploy passed all 400 tests. The tests test nothing. I wrote the tests."


def main():
    # Gate: 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry out of gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
