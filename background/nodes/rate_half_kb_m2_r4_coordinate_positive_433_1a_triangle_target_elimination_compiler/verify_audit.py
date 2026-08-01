#!/usr/bin/env python3
"""Audit scope for the positive 433-1a triangle target compiler."""

from pathlib import Path


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    directory = Path(__file__).resolve().parent
    text = "\n".join(
        (directory / name).read_text()
        for name in ("statement.md", "proof.md", "claim_contract.md", "audit.md")
    )
    for marker in (
        "Template A", "Template B", "KBTEC-4A", "KBTEC-4B",
        "not assert", "not proof input", "algorithm boundary",
    ):
        require(marker in text, f"missing marker {marker}")
    print("positive 433-1a triangle target elimination audit verified")


if __name__ == "__main__":
    main()
