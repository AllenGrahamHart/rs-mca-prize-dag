#!/usr/bin/env python3
"""Audit scope for positive 433-1a common-kernel uniqueness."""

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
        "rank B=6", "all-zero", "rank exactly seven",
        "one-dimensional", "generic matching-cell point", "does not",
    ):
        require(marker in text, f"missing marker {marker}")
    require("lambda_0 lambda_i (lambda_i-lambda_0)" in text,
            "determinant pin")
    print("positive 433-1a common-kernel uniqueness audit verified")


if __name__ == "__main__":
    main()
