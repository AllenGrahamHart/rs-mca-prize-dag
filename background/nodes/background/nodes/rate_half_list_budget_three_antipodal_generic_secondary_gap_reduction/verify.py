#!/usr/bin/env python3
"""Verify the generic secondary square-root gap and DAG wiring."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_secondary_gap_reduction"
DEPENDENCY = "rate_half_list_budget_three_antipodal_fourth_root_gap_reduction"
CONSUMER = "rate_half_list_adjacent_crossing"


def pad(poly: list[Fraction], limit: int) -> list[Fraction]:
    return (poly + [Fraction(0)] * limit)[:limit]


def add(left: list[Fraction], right: list[Fraction], limit: int) -> list[Fraction]:
    left = pad(left, limit)
    right = pad(right, limit)
    return [left[index] + right[index] for index in range(limit)]


def scale(poly: list[Fraction], scalar: Fraction, limit: int) -> list[Fraction]:
    return [scalar * coefficient for coefficient in pad(poly, limit)]


def multiply(left: list[Fraction], right: list[Fraction], limit: int) -> list[Fraction]:
    answer = [Fraction(0)] * limit
    for i, a in enumerate(left[:limit]):
        for j, b in enumerate(right[:limit - i]):
            answer[i + j] += a * b
    return answer


def shift(poly: list[Fraction], amount: int, limit: int) -> list[Fraction]:
    return pad([Fraction(0)] * amount + poly, limit)


def inverse(poly: list[Fraction], limit: int) -> list[Fraction]:
    assert poly[0] != 0
    answer = [1 / poly[0]]
    for m in range(1, limit):
        answer.append(
            -sum(poly[j] * answer[m - j] for j in range(1, min(m, len(poly) - 1) + 1))
            / poly[0]
        )
    return answer


def square_root_one(poly: list[Fraction], limit: int) -> list[Fraction]:
    assert poly[0] == 1
    answer = [Fraction(1)]
    for m in range(1, limit):
        cross = sum(answer[j] * answer[m - j] for j in range(1, m))
        answer.append((poly[m] - cross) / 2)
    return answer


def algebra_check() -> None:
    for h in (4, 5, 8, 11):
        limit = 6 * h
        b_poly = [Fraction(1), Fraction(2), Fraction(-1), Fraction(3)]
        c_poly = [Fraction(2)] + [Fraction((m % 5) - 2) for m in range(1, h - 2)]
        e2, e3, e4 = Fraction(3), Fraction(-5), Fraction(7)

        b2 = multiply(b_poly, b_poly, limit)
        c2 = multiply(c_poly, c_poly, limit)
        c3 = multiply(c2, c_poly, limit)
        c4 = multiply(c2, c2, limit)
        inv_b = inverse(b_poly, limit)
        inv_b2 = multiply(inv_b, inv_b, limit)

        j_series = add(
            scale(c2, e2, limit),
            shift(scale(multiply(c3, inv_b, limit), e3, limit), h, limit),
            limit,
        )
        j_series = add(
            j_series,
            shift(scale(multiply(c4, inv_b2, limit), e4, limit), 2 * h, limit),
            limit,
        )

        r_from_j = shift(multiply(b2, j_series, limit), 2 * h, limit)
        r_direct = add(
            shift(scale(multiply(b2, c2, limit), e2, limit), 2 * h, limit),
            shift(scale(multiply(b_poly, c3, limit), e3, limit), 3 * h, limit),
            limit,
        )
        r_direct = add(r_direct, shift(scale(c4, e4, limit), 4 * h, limit), limit)
        assert r_from_j == r_direct

        j0 = j_series[0]
        normalized = scale(j_series, 1 / j0, h)
        p_series = square_root_one(normalized, h)
        expected = scale(c_poly, 1 / c_poly[0], h)
        assert p_series == expected
        assert p_series[h - 2] == p_series[h - 1] == 0


def official_arithmetic_check() -> None:
    s = 1 << 37
    r = s - 1
    v = (s // 2) - 2
    h = r - v
    assert h == (s // 2) + 1
    assert v == h - 3
    assert h - 2 == (1 << 36) - 1
    assert h - 1 == 1 << 36


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "P=C/C(0) mod z^h",
        "[z^(h-2)]P=[z^(h-1)]P=0",
        "h-2=2^36-1",
        "both the primary",
        "do not prove nonexistence",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    official_arithmetic_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_GENERIC_SECONDARY_GAP_PASS "
        "secondary_indices=2^36-1,2^36 normalized_square_root=1"
    )


if __name__ == "__main__":
    main()
