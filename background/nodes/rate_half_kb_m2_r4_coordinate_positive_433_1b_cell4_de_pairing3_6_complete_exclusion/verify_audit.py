#!/usr/bin/env python3
"""Audit the complete pairing-3/6 composition currencies."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("(0,3), (1,3), (2,3), (0,6), (1,6), (2,6)" in statement,
            "six labels")
    require("partitions these six labels" in proof and
            "leaves 90 labels in 51 orbits" in proof,
            "orbit subtraction")
    require("**Raw cases excluded:** `96`" in contract and
            "`90` labels in `51` orbits" in contract,
            "currency contract")
    print("audit=ok labels=6 orbits=3 raw=96 live=90/51")


if __name__ == "__main__":
    main()
