#!/usr/bin/env python3
"""Audit scope for the universal target elimination compiler."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    combined = "\n".join(path.read_text() for path in NODE.glob("*.md"))
    for marker in (
        "necessary and sufficient",
        "Explicit reconstruction",
        "fourth product binomial",
        "seven squared equations remain squared",
        "not source-system elimination",
        "No compiled source system",
    ):
        require(marker in combined, f"missing audit marker: {marker}")
    print("positive 433-1a universal target elimination audit verified")


if __name__ == "__main__":
    main()
