#!/usr/bin/env python3
"""Exact checks for the degree-four irreducible support router."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def admissible_boundary(
    low: tuple[int, int, int, int],
    high: tuple[int, int, int, int],
) -> bool:
    for boundary in (low, high):
        for endpoint in (0, 3):
            if boundary[endpoint] and any(
                boundary[index] for index in range(4) if index != endpoint
            ):
                return True
    return False


def check_boundary_classification() -> tuple[int, int, int]:
    prime = 7
    ordinary = cyclotomic = monomial = 0
    for s1 in range(prime):
        for s2 in range(prime):
            for s3 in range(prime):
                s0 = 1
                for r0 in range(prime):
                    for r1 in range(prime):
                        for r2 in range(prime):
                            for r3 in range(prime):
                                if r0 == r1 == r2 == r3 == 0:
                                    continue
                                low = (
                                    (s1 * r0 - s0 * r1) % prime,
                                    (s2 * r0 - s0 * r2) % prime,
                                    (s3 * r0 - s0 * r3) % prime,
                                    r0,
                                )
                                high = (r0, r1, r2, r3)
                                if admissible_boundary(low, high):
                                    ordinary += 1
                                elif r0:
                                    need(
                                        r1 == r2 == r3 == s1 == s2 == s3 == 0,
                                        "unclassified nonzero-r0 failure",
                                    )
                                    cyclotomic += 1
                                else:
                                    need(
                                        sum(value != 0 for value in (r1, r2, r3)) == 1,
                                        "unclassified zero-r0 failure",
                                    )
                                    monomial += 1
    return ordinary, cyclotomic, monomial


def evaluate_middle_original(
    x: int,
    y: int,
    s0: int,
    s1: int,
    s3: int,
    prime: int,
) -> int:
    return (
        x**3 * y**2
        + x**2 * y**3
        + s3 * x**2 * y**2
        - s1 * x * y
        - s0 * (x + y)
    ) % prime


def evaluate_middle_transformed(
    u: int,
    v: int,
    s0: int,
    s1: int,
    s3: int,
    prime: int,
) -> int:
    return (
        1
        - s0 * u**2
        - s1 * u**2 * v
        + s3 * u * v
        + u * v**2
        - s0 * u**3 * v**2
    ) % prime


def check_middle_transform() -> int:
    prime = 101
    checks = 0
    for s0, s1, s3 in ((3, 5, 7), (11, 13, 17), (19, 23, 29)):
        for u, v in ((2, 3), (5, 9), (17, 41)):
            x = pow(u * v % prime, -1, prime)
            y = v
            left = evaluate_middle_original(x, y, s0, s1, s3, prime)
            right = evaluate_middle_transformed(u, v, s0, s1, s3, prime)
            need(
                right == left * pow(u, 3, prime) * v % prime,
                "middle monomial torus transform failed",
            )
            checks += 1
    return checks


def check_laurent_identity() -> int:
    prime = 101
    checks = 0
    for a, b, d in ((3, 5, 7), (11, 13, 17)):
        for x, y in ((2, 3), (5, 9), (17, 41)):
            psi_x = (
                x**3 + a * x**2 + b * x + d * pow(x, -1, prime)
            ) % prime
            psi_y = (
                y**3 + a * y**2 + b * y + d * pow(y, -1, prime)
            ) % prime
            curve = (
                x
                * y
                * (x**2 + x * y + y**2 + a * (x + y) + b)
                - d
            ) % prime
            need(
                (x - y) * curve % prime == x * y * (psi_x - psi_y) % prime,
                "Laurent-end coincidence identity failed",
            )
            checks += 1
    return checks


def main() -> None:
    n_value = 1 << 41
    e_value = (1 << 38) - 1
    ordered = 2 * (e_value - 148)
    need(2592**3 * n_value**2 < ordered**3, "(3,3) margin failed")
    need(960**3 * n_value**2 < ordered**3, "(3,2) margin failed")
    need(5376**3 * n_value**2 >= ordered**3, "Laurent route unexpectedly paid")

    boundary_counts = check_boundary_classification()
    middle_checks = check_middle_transform()
    laurent_checks = check_laurent_identity()
    print(
        "RATE_HALF_DISTANCE_THREE_QUARTIC_SUPPORT_DEGREE_FOUR_ROUTER_PASS "
        f"boundary={boundary_counts} middle_checks={middle_checks} "
        f"laurent_checks={laurent_checks} paid_constants=2592/960 "
        "unpaid_laurent_constant=5376"
    )


if __name__ == "__main__":
    main()
