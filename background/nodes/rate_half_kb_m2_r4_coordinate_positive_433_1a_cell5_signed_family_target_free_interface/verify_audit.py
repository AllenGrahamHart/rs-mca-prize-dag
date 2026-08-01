#!/usr/bin/env python3
"""Audit scope for the cell-5 signed-family target-free interface."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    combined = "\n".join(path.read_text() for path in NODE.glob("*.md"))
    for marker in (
        "unsquared",
        "necessary and sufficient",
        "Delta D_0D_1D_2",
        "evidence only",
        "Neither is claimed empty",
        "No source system",
    ):
        require(marker in combined, f"missing audit marker: {marker}")
    print("positive 433-1a cell-5 signed-family scope audit verified")


if __name__ == "__main__":
    main()
