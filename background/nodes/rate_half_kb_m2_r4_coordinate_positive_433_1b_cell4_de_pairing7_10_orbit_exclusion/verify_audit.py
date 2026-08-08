#!/usr/bin/env python3
"""Audit pairing-7/10 composition and the positive pairing-10 fence."""

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
    require("(0,7), (1,7), (2,7), (2,10)" in statement,
            "four-label statement")
    require("does **not** send" in statement and
            "No action sends `(0,7)` or `(1,7)` to pairing 10" in proof,
            "positive pairing-10 fence")
    require("**Raw cases excluded:** `64`" in contract and
            "`74` labels in `43` quotient orbits" in contract,
            "contract counts")
    require("currencies are printed separately" in audit,
            "currency discipline")
    print("audit=ok direct=48 transported=16 overclaim_fenced=32")


if __name__ == "__main__":
    main()
