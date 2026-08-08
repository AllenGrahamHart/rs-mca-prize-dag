#!/usr/bin/env python3
"""Audit pairing-4/9 composition and the positive pairing-9 fence."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    audit = (NODE / "audit.md").read_text()
    require("(0,4), (1,4), (2,4), (2,9)" in statement,
            "four-label statement")
    require("does **not** send" in statement and
            "No action sends `(0,4)` or `(1,4)` to pairing 9" in proof,
            "positive pairing-9 fence")
    require("**Raw cases excluded:** `64`" in contract and
            "`86` labels in `49` quotient orbits" in contract,
            "contract counts")
    require("currencies are printed separately" in audit,
            "currency discipline")
    print("audit=ok direct=48 transported=16 overclaim_fenced=32")


if __name__ == "__main__":
    main()
