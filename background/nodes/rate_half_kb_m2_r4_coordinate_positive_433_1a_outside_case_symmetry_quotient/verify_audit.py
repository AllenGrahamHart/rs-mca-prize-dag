#!/usr/bin/env python3
"""Audit documentation fences for the outside-case symmetry quotient."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    combined = "\n".join(path.read_text() for path in NODE.glob("*.md"))
    for marker in (
        "per fixed common row and fixed cycle sign",
        "75+450=525",
        "global-sign kernel",
        "not algebraic survivors",
        "five of 39",
        "algebraic case or route is deleted",
    ):
        require(marker in combined, f"missing audit marker: {marker}")
    print("positive 433-1a outside-case symmetry audit verified")


if __name__ == "__main__":
    main()
