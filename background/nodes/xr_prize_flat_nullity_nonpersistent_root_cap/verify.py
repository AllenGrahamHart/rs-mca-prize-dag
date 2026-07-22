#!/usr/bin/env python3
"""Verify the XR prize nonpersistent-root cap."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_flat_nullity_nonpersistent_root_cap"
PARENTS = {
    "xr_rs_flat_nullity_basis_charge",
    "xr_prize_flat_nullity_effective_core_floor",
    "xr_target_budget_audit",
}
CONSUMER = "xr_highcore_collision_count"
ROWS = (
    ("prize-1/4", 4, 256, 16, 11_243_370, 1_526_176_111),
    ("prize-1/8", 8, 256, 16, 9_629_972, 2_902_067_940),
    ("prize-1/16", 16, 512, 14, 2_241_633, 1_962_285_107),
)


def endpoint_conditions(
    n: int, rate_denominator: int, scale: int, a: int, v: int
) -> tuple[bool, bool]:
    k = n // rate_denominator
    h = n // scale + 1
    r = n - k
    ell = r // h
    budget = 8 * n**3
    c = a + h
    cv = comb(c + v - 1, a - 1)
    left = a * ell
    zero = left * comb(r + a, a) <= (budget - k) * (c + v) * cv
    full = left * comb(n - v, a) <= (budget - k) * (k + h) * cv
    return zero, full


def official_check() -> int:
    n = 1 << 41
    checks = 0
    for _name, rate, scale, a, _effective, expected_v in ROWS:
        k = n // rate
        lo, hi = 0, k - a
        while lo < hi:
            middle = (lo + hi) // 2
            if all(endpoint_conditions(n, rate, scale, a, middle)):
                hi = middle
            else:
                lo = middle + 1
        assert lo == expected_v
        assert all(endpoint_conditions(n, rate, scale, a, expected_v))
        assert not all(endpoint_conditions(n, rate, scale, a, expected_v - 1))
        checks += 3
    return checks


def convexity_check() -> int:
    checks = 0
    # Exact rational replay on small parameters satisfying the proof's
    # positivity condition. This guards the algebraic rewrite and endpoints.
    for a in range(2, 7):
        for h in range(2, 6):
            r = 40 + a + h
            ell = 3
            k = 12
            c = a + h
            for v in range(0, 5):
                cv = comb(c + v - 1, a - 1)
                c0 = comb(c - 1, a - 1)
                values = []
                for u in range(0, k - a - v + 1):
                    value = Fraction(v * (cv - c0), cv) + Fraction(
                        a * ell * comb(r + a + u, a) + v * v * c0,
                        (c + u + v) * cv,
                    )
                    values.append(value)
                for left, middle, right in zip(
                    values, values[1:], values[2:], strict=False
                ):
                    assert left - 2 * middle + right >= 0
                    checks += 1
                assert max(values) == max(values[0], values[-1])
                checks += 1
    return checks


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "isconvex",
        "1,526,176,110",
        "2,902,067,939",
        "1,962,285,106",
        "parameter-spacereduction",
    ):
        assert marker in statement


def main() -> None:
    official = official_check()
    convexity = convexity_check()
    packet_check()
    print(
        "XR_PRIZE_FLAT_NULLITY_NONPERSISTENT_ROOT_CAP_PASS "
        f"official_checks={official} convexity_checks={convexity}"
    )


if __name__ == "__main__":
    main()
