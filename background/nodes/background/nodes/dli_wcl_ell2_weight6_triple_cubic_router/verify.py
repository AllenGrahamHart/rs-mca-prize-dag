#!/usr/bin/env python3
"""Verify the weight-six triple-cubic router on an exact finite fixture."""

from __future__ import annotations

import itertools


def antipodal_free(values: tuple[int, ...] | list[int], prime: int) -> bool:
    support = set(values)
    return len(support) == len(values) and all(
        (-value) % prime not in support for value in support
    )


def router_data(
    prime: int, order: int, x: int, y: int, d_value: int
) -> tuple[int, int, int, list[int]]:
    u = (1 + x + y) % prime
    if not u:
        raise ZeroDivisionError("selected triple has sum zero")
    a_value = (x + y + x * y) % prime
    b_value = x * y % prime
    w_value = (u * a_value - b_value - d_value) % prime
    c_value = w_value * pow(u, -1, prime) % prime

    sigma = -u * u % prime
    theta = u * w_value % prime
    product = pow(u, 3, prime) * d_value % prime
    power = 1
    while power < order:
        old_sigma, old_theta, old_product = sigma, theta, product
        sigma = (old_sigma * old_sigma - 2 * old_theta) % prime
        theta = (old_theta * old_theta - 2 * old_product * old_sigma) % prime
        product = old_product * old_product % prime
        power *= 2

    roots = [
        value
        for value in range(1, prime)
        if (
            value**3
            + u * value**2
            + c_value * value
            - d_value
        )
        % prime
        == 0
    ]
    return c_value, sigma, theta, roots


def check_doubling_identities() -> None:
    prime = 97
    roots = (2, 3, 5)
    u = -sum(roots) % prime
    c_value = sum(left * right for left, right in itertools.combinations(roots, 2)) % prime
    d_value = roots[0] * roots[1] * roots[2] % prime
    scaled = tuple(u * root % prime for root in roots)

    sigma = sum(scaled) % prime
    theta = sum(left * right for left, right in itertools.combinations(scaled, 2)) % prime
    product = scaled[0] * scaled[1] * scaled[2] % prime
    for power in (1, 2, 4, 8, 16):
        expected_sigma = sum(pow(root, power, prime) for root in scaled) % prime
        expected_theta = sum(
            pow(left * right, power, prime)
            for left, right in itertools.combinations(scaled, 2)
        ) % prime
        expected_product = pow(scaled[0] * scaled[1] * scaled[2], power, prime)
        if (sigma, theta, product) != (
            expected_sigma,
            expected_theta,
            expected_product,
        ):
            raise AssertionError((power, sigma, theta, product))
        old_sigma, old_theta, old_product = sigma, theta, product
        sigma = (old_sigma * old_sigma - 2 * old_theta) % prime
        theta = (old_theta * old_theta - 2 * old_product * old_sigma) % prime
        product = old_product * old_product % prime

    # The cubic coefficients used by the router agree with these roots.
    if ((-u) % prime, c_value, d_value) != (
        sum(roots) % prime,
        sum(left * right for left, right in itertools.combinations(roots, 2))
        % prime,
        roots[0] * roots[1] * roots[2] % prime,
    ):
        raise AssertionError("cubic coefficient identity")


def main() -> None:
    check_doubling_identities()

    prime, order = 17, 16
    group = tuple(range(1, prime))
    direct_relations = {
        relation
        for relation in itertools.combinations(group, 6)
        if 1 in relation
        and antipodal_free(relation, prime)
        and sum(relation) % prime == 0
        and sum(pow(value, 3, prime) for value in relation) % prime == 0
    }

    router_relations: set[tuple[int, ...]] = set()
    equation_candidates = 0
    guarded_routes = 0
    missing_sigma_witness = None
    missing_theta_witness = None

    selectable = tuple(value for value in group if value not in (1, prime - 1))
    for x, y in itertools.combinations(selectable, 2):
        if not antipodal_free((1, x, y), prime):
            continue
        for d_value in group:
            u = (1 + x + y) % prime
            if not u:
                continue
            c_value, sigma, theta, roots = router_data(
                prime, order, x, y, d_value
            )
            sigma_ok = sigma == 3 * pow(u, order, prime) % prime
            theta_ok = theta == 3 * pow(u, 2 * order, prime) % prime
            if sigma_ok and not theta_ok and missing_theta_witness is None:
                missing_theta_witness = (x, y, d_value, c_value)
            if theta_ok and not sigma_ok and missing_sigma_witness is None:
                missing_sigma_witness = (x, y, d_value, c_value)
            if not (sigma_ok and theta_ok):
                continue
            equation_candidates += 1
            union = (1, x, y, *roots)
            if len(roots) != 3 or not antipodal_free(union, prime):
                continue
            guarded_routes += 1
            router_relations.add(tuple(sorted(union)))

    if direct_relations != router_relations:
        raise AssertionError((direct_relations, router_relations))
    if (len(direct_relations), equation_candidates, guarded_routes) != (6, 216, 60):
        raise AssertionError(
            (len(direct_relations), equation_candidates, guarded_routes)
        )

    # Both recurrence equations are load-bearing.
    if missing_sigma_witness is None or missing_theta_witness is None:
        raise AssertionError((missing_sigma_witness, missing_theta_witness))

    # A known relation exercises the product-to-coefficient sign.
    x, y, d_value = 14, 8, 4
    c_value, sigma, theta, roots = router_data(prime, order, x, y, d_value)
    if (c_value, tuple(sorted(roots))) != (7, (5, 10, 13)):
        raise AssertionError((c_value, roots))
    u = (1 + x + y) % prime
    if sigma != 3 * pow(u, order, prime) % prime:
        raise AssertionError("known sigma fixture")
    if theta != 3 * pow(u, 2 * order, prime) % prime:
        raise AssertionError("known theta fixture")

    # Changing -d to +d in W destroys the known reconstruction.
    a_value = (x + y + x * y) % prime
    b_value = x * y % prime
    mutated_c = (u * a_value - b_value + d_value) * pow(u, -1, prime) % prime
    if mutated_c == c_value:
        raise AssertionError("coefficient-sign mutation survived")
    if all(
        (root**3 + u * root**2 + mutated_c * root - d_value) % prime == 0
        for root in roots
    ):
        raise AssertionError("mutated cubic still reconstructs the fixture")

    print(
        "DLI_WCL_ELL2_WEIGHT6_TRIPLE_CUBIC_ROUTER_PASS "
        f"direct_relations={len(direct_relations)} "
        f"equation_candidates={equation_candidates} "
        f"guarded_routes={guarded_routes} negative_controls=3/3"
    )


if __name__ == "__main__":
    main()
