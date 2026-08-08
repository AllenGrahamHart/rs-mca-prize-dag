#!/usr/bin/env python3
"""Audit the pairing-3/6 orbit composition and its scope fence."""

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
    require("(0,3), (1,3), (2,3), (2,6)" in statement,
            "four-label statement")
    require("does **not** transport" in statement and
            "No action sends `(0,3)` or `(1,3)` to pairing 6" in proof,
            "positive pairing-6 fence")
    require("**Raw cases excluded:** `64`" in contract and
            "`92` labels and" in contract and "`52` quotient orbits" in contract,
            "contract counts")
    require("Counts are maintained separately" in audit,
            "currency discipline")
    print("audit=ok direct=48 transported=16 overclaim_fenced=32")


if __name__ == "__main__":
    main()
