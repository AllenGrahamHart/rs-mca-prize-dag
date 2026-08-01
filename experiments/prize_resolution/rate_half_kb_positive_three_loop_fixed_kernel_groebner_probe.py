#!/usr/bin/env python3
"""Algebraic-closure probes for four admissible F_17 common kernels."""

import importlib.util
from pathlib import Path

import sympy as sp


PRIME = 17
ROOT = Path(__file__).resolve().parents[2]
PLACEMENT_SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_three_loop_common_placement_atlas.py"
)

FIXTURES = {
    "442_root_low": {
        "b": 2, "c": 3, "x": 2, "y": 5,
        "kernel": (14, 0, 16, 1), "colored": (3, 3),
        "six_unit": False, "raw_cycle_units": {-1: False, 1: True},
    },
    "442_root_high": {
        "b": 2, "c": 3, "x": 3, "y": 6,
        "kernel": (15, 14, 7, 1), "colored": (2, 2),
        "six_unit": True, "raw_cycle_units": {-1: True, 1: True},
    },
    "433_root_low": {
        "b": 4, "c": 7, "x": 8, "y": 15,
        "kernel": (12, 6, 14, 1), "colored": (4, 7),
        "six_unit": True, "raw_cycle_units": {-1: True, 1: True},
    },
    "433_root_high": {
        "b": 2, "c": 7, "x": 8, "y": 11,
        "kernel": (5, 8, 2, 1), "colored": (1, 2),
        "six_unit": True, "raw_cycle_units": {-1: True, 1: True},
    },
}


def load_placements():
    specification = importlib.util.spec_from_file_location("placements", PLACEMENT_SCRIPT)
    placements = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(placements)
    return placements


def is_unit(polynomials, variables):
    basis = sp.groebner(
        polynomials, *variables, modulus=PRIME, order="grevlex"
    )
    return len(basis.polys) == 1 and basis.polys[0].total_degree() == 0


def edge_polynomial(b, c, kernel):
    w, product, squared_sum = sp.symbols("w product squared_sum")
    d0, d1, d2, beta = kernel
    denominator = d0 + d1 * w + d2 * w**2
    middle = ((1 - c**2) * d0 - c**2 * d1 + (b**2 - c**2) * d2)
    numerator = -d0 + middle * w - b**2 * d2 * w**2
    resultant = sp.resultant(
        numerator - product * denominator,
        beta**2 * w * (w - 1)**2 - squared_sum * denominator**2,
        w,
    )
    return sp.Poly(resultant, product, squared_sum, modulus=PRIME).as_expr()


def verify_common_kernel(name, fixture, matrix):
    b, c, x, y = (fixture[key] for key in ("b", "c", "x", "y"))
    specialization = {sp.Symbol("b"): b, sp.Symbol("c"): c,
                      sp.Symbol("x"): x, sp.Symbol("y"): y}
    specialized = matrix.subs(specialization)
    kernel = sp.Matrix(fixture["kernel"])
    if any(int(value) % PRIME for value in specialized * kernel):
        raise RuntimeError(f"{name} common kernel")


def fixture_probe(name, fixture):
    d, e, f, inverse_guard = sp.symbols("d e f inverse_guard")
    variables = (d, e, f)
    product, squared_sum = sp.symbols("product squared_sum")
    curve = edge_polynomial(fixture["b"], fixture["c"], fixture["kernel"])

    def edge(left, right, edge_sign):
        return sp.Poly(
            curve.subs({
                product: edge_sign * left * right,
                squared_sum: left**2 + right**2 + 2 * edge_sign * left * right,
            }),
            *variables,
            modulus=PRIME,
        ).as_expr()

    left, right = fixture["colored"]
    six = (
        edge(left, e, 1),
        edge(right, f, 1),
        edge(d, e, 1),
        edge(d, e, -1),
        edge(d, f, 1),
        edge(d, f, -1),
    )
    six_unit = is_unit(six, variables)
    if six_unit != fixture["six_unit"]:
        raise RuntimeError(f"{name} six-edge status")
    cycle = {}
    saturated_cycle = {}
    target_values = (1, fixture["b"], fixture["c"], d, e, f)
    target_guard = d * e * f
    for left_index, left_value in enumerate(target_values):
        for right_value in target_values[left_index + 1:]:
            target_guard *= left_value**2 - right_value**2
    for cycle_sign in (-1, 1):
        cycle[cycle_sign] = is_unit(six + (edge(e, f, cycle_sign),), variables)
        if cycle[cycle_sign] != fixture["raw_cycle_units"][cycle_sign]:
            raise RuntimeError(f"{name} raw cycle {cycle_sign}")
        if cycle[cycle_sign]:
            saturated_cycle[cycle_sign] = True
        else:
            saturated_cycle[cycle_sign] = is_unit(
                six + (
                    edge(e, f, cycle_sign),
                    inverse_guard * target_guard - 1,
                ),
                variables + (inverse_guard,),
            )
        if not saturated_cycle[cycle_sign]:
            raise RuntimeError(f"{name} saturated cycle {cycle_sign}")
    return six_unit, cycle, saturated_cycle


def verify():
    placements = load_placements().placement_cases()
    results = {}
    for name, fixture in FIXTURES.items():
        verify_common_kernel(name, fixture, placements[name][0])
        results[name] = fixture_probe(name, fixture)
    return results


def main():
    results = verify()
    six_units = sum(six_unit for six_unit, _, _ in results.values())
    raw_cycle_units = sum(
        sum(cycle.values()) for _, cycle, _ in results.values()
    )
    saturated_cycle_units = sum(
        sum(cycle.values()) for _, _, cycle in results.values()
    )
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_FIXED_GROEBNER_PASS "
        f"prime={PRIME} fixtures={len(results)} six_edge_units={six_units} "
        f"raw_full_units={raw_cycle_units}/{2 * len(results)} "
        f"saturated_full_units={saturated_cycle_units}/{2 * len(results)}"
    )


if __name__ == "__main__":
    main()
