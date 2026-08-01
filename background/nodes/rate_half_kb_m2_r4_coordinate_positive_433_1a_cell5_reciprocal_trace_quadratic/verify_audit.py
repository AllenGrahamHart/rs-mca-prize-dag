#!/usr/bin/env python3
"""Audit scope fences for the reciprocal trace quadratic node."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    statement = (NODE / "statement.md").read_text().lower()
    claim = (NODE / "claim_contract.md").read_text().lower()
    audit = (NODE / "audit.md").read_text().lower()
    require("b!=0" in statement, "trace guard")
    require("quadratic is not asserted" in audit, "residual scope")
    for token in ("signed-pair", "colored-edge", "prize closure"):
        require(token in claim, token)
    require("does not reconstruct" in statement, "nonclaim")
    print("positive 433-1a cell-5 reciprocal trace scope audit verified")


if __name__ == "__main__":
    main()
