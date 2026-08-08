#!/usr/bin/env python3
"""Audit the pairing-8 eliminant identity and terminal scope."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
RESULT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell4_de_pairing8_"
    "nested_quadratic_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    A, B, C, a, M, D, u, f = sp.symbols("A B C a M D u f")
    polynomial = a*u**4 + M*f**2*u**2 + D*f**4
    remainder = sp.rem(polynomial, A*u**2 + B*u + C, u)
    linear = a*(-B**3 + 2*A*B*C) - M*f**2*B*A**2
    constant = (
        a*(-B**2*C + A*C**2) - M*f**2*C*A**2 + D*f**4*A**3
    )
    require(sp.simplify(remainder - (linear*u + constant)/A**3) == 0,
            "cleared remainder identity")
    eliminant = sp.expand(A*constant**2 - B*linear*constant + C*linear**2)
    require(sp.Poly(eliminant, f).degree() == 8 and
            sp.expand(eliminant.subs(A, 0)) == 0,
            "degree-eight and leading-drop identity")

    payload = json.loads(RESULT.read_text())
    rows = payload["rows"]
    require(len(rows) == 32 and all(
        row["status"] == "COMPLETE" and row["excluded"] and
        not row["witnesses"] and not row["unresolved"]
        for row in rows
    ), "complete exact rows")
    require(sum(row["candidate_root_count"] for row in rows) == 320 and
            sum(row["source_point_count"] for row in rows) == 288 and
            sum(row["uf_candidate_count"] for row in rows) == 80 and
            sum(len(row["target_boundary_rows"]) for row in rows) == 16,
            "printed terminal ledger")
    proof = (NODE / "proof.md").read_text()
    statement = (NODE / "statement.md").read_text()
    require("Positive `DE` at matching 13 is not claimed" in
            (NODE / "audit.md").read_text(), "matching-13 fence")
    require("A missing sign/lane row" in statement and
            "degree-drop specializations" in proof,
            "falsifier and degree-drop disclosure")
    print("audit=ok degree=8 rows=32 candidates=320 witnesses=0")


if __name__ == "__main__":
    main()
