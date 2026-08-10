#!/usr/bin/env python3
"""Arithmetic and cohomology replay for the Picard--Forney exclusion."""


def check(m):
    rho = 4 * m - 1
    n_domain = 16 * m
    n_slopes = 4 * m + 1

    residual = (-rho - 3, m + 1)
    residual_degree = residual[0] * m + residual[1] * rho
    assert residual_degree == m - 1

    tensor = (
        4 * residual[0] + n_domain,
        4 * residual[1] - n_slopes,
    )
    assert tensor == (-8, 3)
    tensor_degree = tensor[0] * m + tensor[1] * rho
    assert tensor_degree == 4 * (m - 1) + 1 == 4 * m - 3

    kernel_surface = (-rho - 8, 3 - m)
    assert kernel_surface[0] < 0
    assert kernel_surface[1] < 0
    return rho


def main():
    profiles = 0
    for m in range(4, 80):
        check(m)
        profiles += 1

    official_m = 1 << 37
    official_rho = check(official_m)
    profiles += 1

    # Mutation controls: one less contact or the inverse Picard sign misses
    # the forbidden (-8,3) bundle.
    rho = 4 * 11 - 1
    weakened = (rho - 1 - (2 * rho + 1), 12)
    assert (4 * weakened[0] + 16 * 11, 4 * weakened[1] - 45) != (-8, 3)
    inverse_pin = (4 * (-rho - 3) - 16 * 11, 4 * 12 + 45)
    assert inverse_pin != (-8, 3)

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_PICARD_FORNEY_CONTACT_EXCLUSION_PASS "
        f"profiles={profiles} official_m={official_m} official_rho={official_rho}"
    )


if __name__ == "__main__":
    main()
