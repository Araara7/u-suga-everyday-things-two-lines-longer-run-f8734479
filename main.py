#!/usr/bin/env python3
"""Everyday Things, Two Lines — make.fun bounty entry.

Writes the two-line entry to /output/entry.txt:
line 1 explains a traffic jam to a 10-year-old via analogy,
line 2 says why the analogy works and what it leaves out.
"""

import os

ENTRY = (
    "A traffic jam is a school of metal fish that forgot how to swim, "
    "so they just float there honking at the water.\n"
    "The analogy works because traffic bunches and flows like fish, "
    "but it leaves out that fish never blame each other for being late."
)


def main() -> None:
    lines = ENTRY.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "no blank lines allowed"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
