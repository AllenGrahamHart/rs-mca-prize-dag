#!/usr/bin/env python3
"""Audit scope fences for the positive quadratic paired-product node."""

from pathlib import Path


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    directory = Path(__file__).resolve().parent
    statement = (directory / "statement.md").read_text()
    audit = (directory / "audit.md").read_text()
    contract = (directory / "claim_contract.md").read_text()
    proof = (directory / "proof.md").read_text()
    combined = "\n".join((statement, audit, contract, proof))

    for marker in (
        "xi=eta", "xi in L^c", "necessary", "not asserted sufficient",
        "outside sum", "525", "degree-drop", "KBPQI-7", "KBPQI-8",
        "does not close",
    ):
        require(marker in combined, f"missing scope marker: {marker}")
    require("five internal" in combined, "eta location fence")
    require("seven possible" in combined, "xi range fence")
    require("timed out" in audit and "prove no" in audit,
            "timeout inference fence")
    print("positive 433-1a paired-product audit verified")


if __name__ == "__main__":
    main()
