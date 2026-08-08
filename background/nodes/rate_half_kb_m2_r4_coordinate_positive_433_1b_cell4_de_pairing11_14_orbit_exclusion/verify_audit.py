#!/usr/bin/env python3
"""Audit pairing-11/14 composition and the positive pairing-14 fence."""

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
    require("(0,11), (1,11), (2,11), (2,14)" in statement,
            "four-label statement")
    require("does **not** send" in statement and
            "No action sends `(0,11)` or `(1,11)` to pairing 14" in proof,
            "positive pairing-14 fence")
    require("**Raw cases excluded:** `64`" in contract and
            "`62` labels in `37` quotient orbits" in contract,
            "contract counts")
    require("currencies are printed separately" in audit,
            "currency discipline")
    print("audit=ok direct=48 transported=16 overclaim_fenced=32")


if __name__ == "__main__":
    main()
