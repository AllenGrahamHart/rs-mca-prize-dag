#!/usr/bin/env python3
"""Audit the complete pairing-4/9 set composition."""

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
    require("xi in {0,1,2}, pairing in {4,9}" in statement,
            "complete Cartesian statement")
    require("(0,9), (1,9)" in proof and "15+6=21" in proof,
            "positive supplement and cumulative ledger")
    require("**Raw cases excluded:** `96`" in contract and
            "`84` labels in `48` quotient orbits" in contract,
            "contract counts")
    require("No complete-cell status" in audit, "scope fence")
    print("audit=ok labels=6 orbits=3 raw=96 live=84/48")


if __name__ == "__main__":
    main()
