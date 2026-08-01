#!/usr/bin/env python3
"""Audit scope fences for the positive 433-1a cell-5 ratio compiler."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    combined = "\n".join(path.read_text() for path in NODE.glob("*.md"))
    for marker in (
        "exact deployed-field",
        "factor `t-r`",
        "x=c/b",
        "a0=a1=0",
        "not outside-system equations",
        "No cell, route, K3 row, or Prize result is closed",
    ):
        require(marker in combined, f"missing audit marker: {marker}")
    print("positive 433-1a cell-5 ratio audit verified")


if __name__ == "__main__":
    main()
