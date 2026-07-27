#!/usr/bin/env python3
"""Verify the RS tangent unsafe floor and its strict budget conversion."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rs_tangent_flexible_budget_unsafe_floor"
CLASSIFIER = "tangent_clean_anchor_route_classification"
TARGET = "unsafe_crossing_family_instantiation"

EXPECTED_PIN = {
    "upstream_commit": "b13de8113a03f06b6fc22bbd2f289a8abcdf7e95",
    "file": "tex/slackMCA_v4.tex",
    "file_sha256": "810ac469b8a8a8ba4638d882ec8426be95ffddf0f8888b83315afb4d60e990b4",
    "label": "prop:floor",
}


def evaluate(coefficients: tuple[int, ...], x: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % prime
    return value


def check_toy_instance(prime: int, n: int, k: int, agreement: int) -> int:
    assert n < prime
    assert k < agreement < n
    error_count = n - agreement
    assert error_count <= prime

    domain = tuple(range(n))
    errors = set(domain[:error_count])
    f = {x: index + 1 if x in errors else 0 for index, x in enumerate(domain)}
    g = {x: int(x in errors) for x in domain}
    slopes = set()

    codewords = tuple(itertools.product(range(prime), repeat=k))
    for x in errors:
        slope = (-f[x]) % prime
        slopes.add(slope)
        support = tuple(y for y in domain if y not in errors) + (x,)

        assert len(support) == agreement + 1
        assert all((f[y] + slope * g[y]) % prime == 0 for y in support)
        assert not any(
            all(evaluate(coefficients, y, prime) == g[y] for y in support)
            for coefficients in codewords
        )

    assert len(slopes) == error_count
    return len(slopes)


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN

    toy_slopes = 0
    toy_slopes += check_toy_instance(11, 8, 3, 4)
    toy_slopes += check_toy_instance(13, 10, 4, 6)

    budget_checks = 0
    for bits in range(1, 9):
        scale = 1 << bits
        for error_count in range(1, 25):
            cutoff = error_count * scale - 1
            for q in range(1, error_count * scale + scale + 1):
                direct = error_count > q // scale
                routed = q <= cutoff
                assert direct == routed
                budget_checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[CLASSIFIER] == "PROVED"
    assert statuses[TARGET] == "TARGET"
    assert (NODE, CLASSIFIER, "req") in edges
    assert (NODE, TARGET, "ev") in edges
    assert "n-a>floor(q/2^t)" in statements[NODE]
    assert "q<=e*2^t-1" in statements[NODE]

    print(
        "RS_TANGENT_FLEXIBLE_BUDGET_UNSAFE_FLOOR_PASS "
        f"toy_slopes={toy_slopes} budget_checks={budget_checks}"
    )


if __name__ == "__main__":
    main()
