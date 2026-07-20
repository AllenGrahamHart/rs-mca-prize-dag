#!/usr/bin/env python3
"""Exact checks for the c=2 outer dyadic torsion-trace gate."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
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


def trace_remainder(
    cubic: list[int],
    levels: int = 40,
    recurrence_constant: int = 2,
    trace_shift: int = 2,
) -> list[int]:
    value = [-trace_shift % PRIME, 1]
    for _ in range(levels):
        square = algebra.poly_mul(value, value)
        _, value = algebra.poly_divmod(square, cubic)
        value[0] = (value[0] - recurrence_constant) % PRIME
        value = algebra.trim(value)
        assert len(value) <= 3
    return value


def terminal_polynomial(
    cubic: list[int],
    levels: int = 40,
    recurrence_constant: int = 2,
    trace_shift: int = 2,
    terminal_value: int = 2,
) -> list[int]:
    value = trace_remainder(
        cubic,
        levels=levels,
        recurrence_constant=recurrence_constant,
        trace_shift=trace_shift,
    )
    value[0] = (value[0] - terminal_value) % PRIME
    return algebra.trim(value)


def gcd_degree(cubic: list[int], terminal: list[int]) -> int:
    return len(algebra.poly_gcd(cubic, terminal)) - 1


def primitive_root() -> int:
    factors = (2, 3, 7)
    for candidate in range(2, PRIME):
        if all(
            pow(candidate, (PRIME - 1) // factor, PRIME) != 1
            for factor in factors
        ):
            return candidate
    raise AssertionError("primitive root not found")


def positive_packet(t: int) -> tuple[list[int], int]:
    b = algebra.square_root(t)
    source = (1, -1 % PRIME, b, -b % PRIME)
    invariant_i, invariant_j = algebra.invariants_from_roots(source)
    cubic = algebra.outer_cubic(invariant_i, invariant_j)
    z = (t + pow(t, -1, PRIME) + 2) % PRIME
    assert algebra.eval_poly(cubic, z) == 0
    assert len(algebra.trim(cubic)) == 4
    return cubic, z


def main() -> None:
    generator = primitive_root()
    positive = 0
    trace_checks = 0

    # The order-eight subgroup lies in the square subgroup of F_1009.
    # Every nonidentity element therefore gives a split c=2 source packet,
    # and its order divides the official 2^40 order.
    for exponent in range(1, 8):
        t = pow(generator, (PRIME - 1) // 8 * exponent, PRIME)
        assert t != 1
        assert pow(t, 1 << 40, PRIME) == 1
        cubic, z = positive_packet(t)

        value = [-2 % PRIME, 1]
        for level in range(41):
            expected = (
                pow(t, 1 << level, PRIME)
                + pow(t, -(1 << level), PRIME)
            ) % PRIME
            assert algebra.eval_poly(value, z) == expected
            trace_checks += 1
            if level < 40:
                square = algebra.poly_mul(value, value)
                _, value = algebra.poly_divmod(square, cubic)
                value[0] = (value[0] - 2) % PRIME
                value = algebra.trim(value)

        terminal = value[:]
        terminal[0] = (terminal[0] - 2) % PRIME
        assert gcd_degree(cubic, algebra.trim(terminal)) >= 1
        assert gcd_degree(cubic, terminal_polynomial(cubic)) >= 1
        positive += 1

    negative = 0
    for roots in ((3, 5, 7, 29), (2, 10, 31, 44), (1, 2, 4, 8)):
        outer = algebra.centered(roots)
        invariant_i, invariant_j = algebra.invariants_from_roots(outer)
        cubic = algebra.outer_cubic(invariant_i, invariant_j)
        assert len(algebra.trim(cubic)) == 4
        assert gcd_degree(cubic, terminal_polynomial(cubic)) == 0
        negative += 1

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_OUTER_TORSION_TRACE_PASS "
        f"positive={positive} negative={negative} "
        f"trace_checks={trace_checks} reductions={positive * 40}"
    )


if __name__ == "__main__":
    main()

