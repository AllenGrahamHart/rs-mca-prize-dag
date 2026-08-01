#!/usr/bin/env python3
"""Target-neighbor norm compiler for positive three-loop packets."""

import sympy as sp


PLACEMENT_COMMON = {
    "442_root_low": (("one", "b", 1), ("one", "b", -1)),
    "442_root_high": (("one", "c", 1), ("one", "c", -1)),
    "433_root_low": (("one", "b", 1), ("one", "c", 1)),
    "433_root_high": (("one", "c", 1), ("b", "c", 1)),
}

PLACEMENT_COLORED = {
    "442_root_low": ("c", "c"),
    "442_root_high": ("b", "b"),
    "433_root_low": ("b", "c"),
    "433_root_high": ("one", "b"),
}


def add_edge_orbit(edges, left, right, edge_sign):
    edges.append(((left, 1), (right, edge_sign)))
    edges.append(((left, -1), (right, -edge_sign)))


def full_lane_edges(placement, cycle_sign):
    edges = []
    for target in ("one", "b", "c"):
        edges.extend([((target, 1), (target, -1))] * 2)
    for left, right, edge_sign in PLACEMENT_COMMON[placement]:
        add_edge_orbit(edges, left, right, edge_sign)
    colored_left, colored_right = PLACEMENT_COLORED[placement]
    add_edge_orbit(edges, colored_left, "e", 1)
    add_edge_orbit(edges, colored_right, "f", 1)
    add_edge_orbit(edges, "d", "e", 1)
    add_edge_orbit(edges, "d", "e", -1)
    add_edge_orbit(edges, "d", "f", 1)
    add_edge_orbit(edges, "d", "f", -1)
    add_edge_orbit(edges, "e", "f", cycle_sign)
    return tuple(edges)


def neighbor_products(placement, cycle_sign):
    symbols = {
        "one": sp.Integer(1),
        **{name: sp.Symbol(name) for name in ("b", "c", "d", "e", "f")},
    }
    edges = full_lane_edges(placement, cycle_sign)
    if len(edges) != 24:
        raise RuntimeError("edge count")
    products = {}
    for name in symbols:
        vertex = (name, 1)
        neighbors = []
        for left, right in edges:
            if left == vertex:
                neighbors.append(right)
            if right == vertex:
                neighbors.append(left)
        if len(neighbors) != 4:
            raise RuntimeError(f"{placement} {cycle_sign} degree {name}")
        product = sp.Integer(1)
        for neighbor_name, neighbor_sign in neighbors:
            product *= neighbor_sign * symbols[neighbor_name]
        products[name] = sp.expand(product)
    return products


def expected_product_table(placement, cycle_sign):
    b, c, d, e, f = sp.symbols("b c d e f")
    table = {
        "442_root_low": {
            "one": -b**2,
            "b": -b**2,
            "c": c**2 * e * f,
            "d": e**2 * f**2,
            "e": -cycle_sign * c * d**2 * f,
            "f": -cycle_sign * c * d**2 * e,
        },
        "442_root_high": {
            "one": -c**2,
            "b": b**2 * e * f,
            "c": -c**2,
            "d": e**2 * f**2,
            "e": -cycle_sign * b * d**2 * f,
            "f": -cycle_sign * b * d**2 * e,
        },
        "433_root_low": {
            "one": b * c,
            "b": b**2 * e,
            "c": c**2 * f,
            "d": e**2 * f**2,
            "e": -cycle_sign * b * d**2 * f,
            "f": -cycle_sign * c * d**2 * e,
        },
        "433_root_high": {
            "one": c * e,
            "b": b**2 * c * f,
            "c": b * c**2,
            "d": e**2 * f**2,
            "e": -cycle_sign * d**2 * f,
            "f": -cycle_sign * b * d**2 * e,
        },
    }
    return table[placement]


def verify_resultant_norm():
    W, X, r, U = sp.symbols("W X r U")
    d0, d1, d2, e0, e1, e2, beta = sp.symbols(
        "d0 d1 d2 e0 e1 e2 beta"
    )
    D = d0 + d1 * W + d2 * W**2
    E = e0 + e1 * W + e2 * W**2
    B = beta * (W - 1)
    source_row = sp.expand(
        r**2 * D.subs(W, X**2)
        + E.subs(W, X**2)
        + r * X * B.subs(W, X**2)
    )
    numerator = sp.resultant(E, U * D**2 - W * B**2, W)
    denominator = sp.resultant(D, E**2 - U * W * B**2, W)
    source_E = sp.resultant(source_row, E.subs(W, X**2), X)
    source_D = sp.resultant(source_row, D.subs(W, X**2), X)
    if sp.expand(source_E - r**4 * numerator.subs(U, r**2)) != 0:
        raise RuntimeError("E norm identity")
    if sp.expand(source_D - denominator.subs(U, r**2)) != 0:
        raise RuntimeError("D norm identity")
    if sp.degree(numerator, U) != 2 or sp.degree(denominator, U) != 2:
        raise RuntimeError("neighbor norm degree")
    return numerator, denominator


def compressed_gates():
    return {
        "442_root_low": {
            "colored_product": "e*f=N(c^2)/c^2",
            "remaining": [
                "N(d^2)=(e*f)^2",
                "N(e^2)=-sigma*c*d^2*f",
                "N(f^2)=-sigma*c*d^2*e",
            ],
        },
        "442_root_high": {
            "colored_product": "e*f=N(b^2)/b^2",
            "remaining": [
                "N(d^2)=(e*f)^2",
                "N(e^2)=-sigma*b*d^2*f",
                "N(f^2)=-sigma*b*d^2*e",
            ],
        },
        "433_root_low": {
            "colored_values": ["e=N(b^2)/b^2", "f=N(c^2)/c^2"],
            "remaining": [
                "N(d^2)=e^2*f^2",
                "N(e^2)=-sigma*b*d^2*f",
                "N(f^2)=-sigma*c*d^2*e",
            ],
        },
        "433_root_high": {
            "colored_values": ["e=N(1)/c", "f=N(b^2)/(b^2*c)"],
            "remaining": [
                "N(d^2)=e^2*f^2",
                "N(e^2)=-sigma*d^2*f",
                "N(f^2)=-sigma*b*d^2*e",
            ],
        },
    }


def weld_counterexample(numerator, denominator):
    """Admissible common-kernel fixture where the graph/resultant weld fails."""
    prime = 13
    b, c, x, y = 2, 3, 2, 3
    d_values = (4, 7, 6)
    beta_value = 1
    d0_value, d1_value, d2_value = d_values
    e_values = (
        -d0_value,
        (1 - c**2) * d0_value - c**2 * d1_value + (b**2 - c**2) * d2_value,
        -b**2 * d2_value,
    )

    def evaluate(coefficients, value):
        return sum(coefficient * value**index for index, coefficient in enumerate(coefficients)) % prime

    for source, product, target_sum in ((x, b, 1 + b), (y, c, 1 + c)):
        w = source**2
        d_at_w = evaluate(d_values, w)
        e_at_w = evaluate(e_values, w)
        b_at_w = beta_value * (w - 1) % prime
        if (e_at_w - product * d_at_w) % prime:
            raise RuntimeError("counterexample product row")
        if (source * b_at_w + target_sum * d_at_w) % prime:
            raise RuntimeError("counterexample sum row")
    if any(evaluate(d_values, value) == 0 for value in (0, 1, x**2, y**2)):
        raise RuntimeError("counterexample leading support")

    symbols = {
        sp.Symbol("d0"): d0_value,
        sp.Symbol("d1"): d1_value,
        sp.Symbol("d2"): d2_value,
        sp.Symbol("e0"): e_values[0],
        sp.Symbol("e1"): e_values[1],
        sp.Symbol("e2"): e_values[2],
        sp.Symbol("beta"): beta_value,
    }
    U = sp.Symbol("U")
    p_coefficients = [
        int(sp.Poly(numerator, U).coeff_monomial(U**index).subs(symbols)) % prime
        for index in range(3)
    ]
    q_coefficients = [
        int(sp.Poly(denominator, U).coeff_monomial(U**index).subs(symbols)) % prime
        for index in range(3)
    ]
    q_at_one = evaluate(q_coefficients, 1)
    if q_at_one == 0:
        raise RuntimeError("counterexample norm denominator")
    observed = evaluate(p_coefficients, 1) * pow(q_at_one, prime - 2, prime) % prime
    expected = b * c % prime
    if observed == expected or (observed, expected) != (8, 6):
        raise RuntimeError("counterexample weld")
    return {
        "prime": prime,
        "placement": "433_root_low",
        "kernel": (4, 7, 6, 1),
        "observed_norm_at_one": observed,
        "claimed_neighbor_product": expected,
    }


def verify():
    numerator, denominator = verify_resultant_norm()
    lanes = {}
    for placement in PLACEMENT_COMMON:
        for cycle_sign in (-1, 1):
            observed = neighbor_products(placement, cycle_sign)
            expected = expected_product_table(placement, cycle_sign)
            if any(sp.expand(observed[name] - expected[name]) != 0 for name in expected):
                raise RuntimeError(f"neighbor table {placement} {cycle_sign}")
            lanes[(placement, cycle_sign)] = observed
    gates = compressed_gates()
    if len(lanes) != 8 or len(gates) != 4:
        raise RuntimeError("lane coverage")
    counterexample = weld_counterexample(numerator, denominator)
    return {
        "numerator_u_degree": sp.degree(numerator, sp.Symbol("U")),
        "denominator_u_degree": sp.degree(denominator, sp.Symbol("U")),
        "placements": len(gates),
        "lanes": len(lanes),
        "target_degree": 4,
        "resultant_identities_valid": True,
        "graph_tables_valid": True,
        "resultant_graph_weld_valid": False,
        "counterexample": counterexample,
    }


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_NEIGHBOR_NORM_REFUTED "
        f"norm_degree={result['numerator_u_degree']}/"
        f"{result['denominator_u_degree']} placements={result['placements']} "
        f"lanes={result['lanes']} counterexample_prime="
        f"{result['counterexample']['prime']} observed="
        f"{result['counterexample']['observed_norm_at_one']} claimed="
        f"{result['counterexample']['claimed_neighbor_product']}"
    )


if __name__ == "__main__":
    main()
