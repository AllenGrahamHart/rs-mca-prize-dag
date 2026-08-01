#!/usr/bin/env python3
"""Audit scope for the cell-5 ratio exceptional branch exclusion."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    combined = "\n".join(path.read_text() for path in NODE.glob("*.md"))
    for marker in (
        "22 atomic guards",
        "basis `{1}`",
        "algebraic closure",
        "does not make the generic common curve",
        "No cell, route, K3 row, or Prize result is closed",
    ):
        require(marker in combined, f"missing scope marker: {marker}")
    print("positive 433-1a cell-5 exceptional-branch audit verified")


if __name__ == "__main__":
    main()
