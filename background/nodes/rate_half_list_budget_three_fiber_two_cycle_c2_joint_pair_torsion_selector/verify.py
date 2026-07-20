#!/usr/bin/env python3
"""Exact finite-field checks for the c=2 joint pair-torsion selector."""

from __future__ import annotations

import importlib.util
import json
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_joint_pair_torsion_selector"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_mismatch_trace_resolvent_elimination",
    "rate_half_list_budget_three_fiber_two_cycle_c2_outer_torsion_trace_gate",
}
CONSUMER = "rate_half_list_adjacent_crossing"
DEPENDENCY = (
    HERE.parent
    / "rate_half_list_budget_three_fiber_two_cycle_mismatch_trace_resolvent_elimination"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("mismatch_trace_algebra", DEPENDENCY)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load mismatch trace algebra")
algebra = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(algebra)

PRIME = algebra.PRIME


def primitive_root() -> int:
    factors = (2, 3, 7)
    for candidate in range(2, PRIME):
        if all(
            pow(candidate, (PRIME - 1) // factor, PRIME) != 1
            for factor in factors
        ):
            return candidate
    raise AssertionError("primitive root not found")


def terminal_polynomial(
    cubic: list[int],
    levels: int,
    recurrence_constant: int = 2,
    trace_shift: int = 2,
    terminal_value: int = 2,
) -> list[int]:
    value = [-trace_shift % PRIME, 1]
    for _ in range(levels):
        square = algebra.poly_mul(value, value)
        _, value = algebra.poly_divmod(square, cubic)
        value[0] = (value[0] - recurrence_constant) % PRIME
        value = algebra.trim(value)
        assert len(value) <= 3
    value[0] = (value[0] - terminal_value) % PRIME
    return algebra.trim(value)


def pair_trace(a: int, b: int) -> int:
    return (a + b) ** 2 * pow(a * b % PRIME, -1, PRIME) % PRIME


def joint_selector(
    roots: tuple[int, int, int, int],
    cubic: list[int],
    levels: int,
    recurrence_constant: int = 2,
    trace_shift: int = 2,
    terminal_value: int = 2,
) -> list[int]:
    resolvent = algebra.resolvent_formula(roots)
    _, reduced_resolvent = algebra.poly_divmod(resolvent, cubic)
    first = algebra.poly_gcd(cubic, reduced_resolvent)
    terminal = terminal_polynomial(
        cubic,
        levels,
        recurrence_constant=recurrence_constant,
        trace_shift=trace_shift,
        terminal_value=terminal_value,
    )
    return algebra.poly_gcd(first, terminal)


def expected_traces(
    roots: tuple[int, int, int, int], cubic: list[int], levels: int
) -> set[int]:
    expected: set[int] = set()
    for a, b in combinations(roots, 2):
        z = pair_trace(a, b)
        ratio = a * pow(b, -1, PRIME) % PRIME
        if (
            algebra.eval_poly(cubic, z) == 0
            and pow(ratio, 1 << levels, PRIME) == 1
        ):
            expected.add(z)
    return expected


def field_roots(poly: list[int]) -> set[int]:
    return {
        value
        for value in range(PRIME)
        if algebra.eval_poly(poly, value) == 0
    }


def source_cubic(t: int) -> list[int]:
    root = algebra.square_root(t)
    source = (1, -1 % PRIME, root, -root % PRIME)
    invariant_i, invariant_j = algebra.invariants_from_roots(source)
    cubic = algebra.outer_cubic(invariant_i, invariant_j)
    assert len(algebra.trim(cubic)) == 4
    return cubic


def check_wiring() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge.get("kind") == "req"
    }
    outgoing = {
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "ev"
    }
    assert nodes[NODE_ID]["status"] == "PROVED"
    assert incoming == DEPENDENCIES
    assert CONSUMER in outgoing


def completion_roots(t: int) -> tuple[int, int, int, int]:
    roots = [1, t]
    for candidate in range(2, PRIME):
        square = candidate * candidate % PRIME
        if square not in roots:
            roots.append(square)
        if len(roots) == 4:
            break
    assert len(set(roots)) == 4
    return tuple(roots)  # type: ignore[return-value]


def find_outer_only_false_positive(
    cubic: list[int], levels: int
) -> tuple[int, int, int, int]:
    squares = sorted({value * value % PRIME for value in range(1, 24)})
    for roots in combinations(squares, 4):
        if not expected_traces(roots, cubic, levels):
            selector = joint_selector(roots, cubic, levels)
            if len(selector) == 1:
                return roots
    raise AssertionError("outer-only false-positive denominator not found")


def main() -> None:
    check_wiring()
    generator = primitive_root()
    levels = 3
    exact_packets = 0

    for exponent in range(1, 8):
        t = pow(generator, (PRIME - 1) // 8 * exponent, PRIME)
        roots = completion_roots(t)
        cubic = source_cubic(t)
        selector = joint_selector(roots, cubic, levels)
        expected = expected_traces(roots, cubic, levels)
        assert pair_trace(1, t) in expected
        assert field_roots(selector) == expected
        assert 1 <= len(selector) - 1 <= 3
        exact_packets += 1

    t = pow(generator, (PRIME - 1) // 8, PRIME)
    cubic = source_cubic(t)
    terminal = terminal_polynomial(cubic, levels)
    assert len(algebra.poly_gcd(cubic, terminal)) > 1
    false_positive_roots = find_outer_only_false_positive(cubic, levels)
    assert not expected_traces(false_positive_roots, cubic, levels)
    assert joint_selector(false_positive_roots, cubic, levels) == [1]

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_JOINT_PAIR_TORSION_PASS "
        f"exact_packets={exact_packets} outer_only_false_positives=1 "
        f"levels={levels} official_levels=40 wiring=3"
    )


if __name__ == "__main__":
    main()
