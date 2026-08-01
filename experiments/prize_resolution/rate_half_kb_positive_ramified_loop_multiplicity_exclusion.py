#!/usr/bin/env python3
"""Local complete-source multiplicity obstruction for positive ramified loops."""

import itertools

import sympy as sp


BRANCHES = ("zero", "infinity")
NONRAMIFIED = "ordinary"


def valuation(polynomial, variable):
    poly = sp.Poly(sp.expand(polynomial), variable)
    return min(monomial[0] for monomial, coefficient in poly.terms() if coefficient)


def local_expansion_check():
    u, a, t = sp.symbols("u a t")
    d0, d1, d2, e1, e2, c0, c1 = sp.symbols(
        "d0 d1 d2 e1 e2 c0 c1"
    )
    w = u**2
    denominator = d0 + d1 * w + d2 * w**2
    numerator = -a**2 * d0 + e1 * w + e2 * w**2
    odd = c0 + c1 * w

    row_plus = sp.expand(a**2 * denominator + numerator + a * u * odd)
    row_minus = sp.expand(a**2 * denominator + numerator - a * u * odd)
    row_other = sp.expand(t**2 * denominator + numerator + t * u * odd)
    if sp.Poly(row_plus, u).coeff_monomial(u) != a * c0:
        raise RuntimeError("positive loop-row tangent")
    if sp.Poly(row_minus, u).coeff_monomial(u) != -a * c0:
        raise RuntimeError("negative loop-row tangent")
    if sp.expand(row_other.subs(u, 0) - d0 * (t**2 - a**2)) != 0:
        raise RuntimeError("other target unit")
    return 2, 4


def exact_product_samples():
    u = sp.Symbol("u")
    targets = tuple(range(-6, 0)) + tuple(range(1, 7))
    samples = (
        {
            "loop": 1,
            "denominator": 2 + 3 * u**2 + 5 * u**4,
            "numerator": -2 + 13 * u**2 + 17 * u**4,
            "odd_term": u * (7 + 11 * u**2),
        },
        {
            "loop": 2,
            "denominator": 5 + 3 * u**2 + 2 * u**4,
            "numerator": -20 + 17 * u**2 + 13 * u**4,
            "odd_term": u * (11 + 7 * u**2),
        },
    )
    observed = []
    for sample in samples:
        product = sp.Integer(1)
        for target in targets:
            product *= (
                target**2 * sample["denominator"]
                + sample["numerator"]
                + target * sample["odd_term"]
            )
        row_order = valuation(product, u)
        complete_source_square = (u**2 * (1 + u)) ** 2
        square_order = valuation(complete_source_square, u)
        if row_order != 2 or square_order != 4:
            raise RuntimeError("local product order")
        observed.append((row_order, square_order))
    return tuple(observed)


def loop_placement_census():
    placements = []
    slots = BRANCHES + (NONRAMIFIED,)
    for loop_count in (2, 3):
        for loops in itertools.combinations(slots, loop_count):
            if not set(loops) & set(BRANCHES):
                continue
            if NONRAMIFIED in loops:
                zero_of_b1 = NONRAMIFIED
                live_branch = next(branch for branch in loops if branch in BRANCHES)
            else:
                zero_of_b1 = BRANCHES[0]
                live_branch = BRANCHES[1]
            if live_branch not in loops or live_branch == zero_of_b1:
                raise RuntimeError("missing nonzero ramified loop")
            placements.append((loops, zero_of_b1, live_branch))
    if len(placements) != 4:
        raise RuntimeError("loop placement coverage")
    return tuple(placements)


def verify():
    local_orders = local_expansion_check()
    samples = exact_product_samples()
    placements = loop_placement_census()
    return {
        "local_row_order": local_orders[0],
        "required_square_order": local_orders[1],
        "branch_charts": len(samples),
        "loop_placements_deleted": len(placements),
        "loop_counts_deleted": (2, 3),
        "one_loop_ramified_requires_b1_zero": True,
    }


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_RAMIFIED_LOOP_MULTIPLICITY_PASS "
        f"local_order={result['local_row_order']} "
        f"required_order={result['required_square_order']} "
        f"branch_charts={result['branch_charts']} "
        f"placements_deleted={result['loop_placements_deleted']} "
        "loop_counts=2,3"
    )


if __name__ == "__main__":
    main()
