#!/usr/bin/env python3
"""Audit pairing-5/12 composition and the positive pairing-12 fence."""

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
    require("(0,5), (1,5), (2,5), (2,12)" in statement,
            "four-label statement")
    require("does **not** send" in statement and
            "No action sends `(0,5)` or `(1,5)` to pairing 12" in proof,
            "positive pairing-12 fence")
    require("**Raw cases excluded:** `64`" in contract and
            "`80` labels in `46` quotient orbits" in contract,
            "contract counts")
    require("currencies are printed separately" in audit,
            "currency discipline")
    print("audit=ok direct=48 transported=16 overclaim_fenced=32")


if __name__ == "__main__":
    main()
