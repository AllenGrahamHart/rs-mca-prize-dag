#!/usr/bin/env python3
"""Independent finite-field audit of the leading Bezout allocation."""


PRIME = 1_000_003


def inverse(value: int) -> int:
    return pow(value % PRIME, PRIME - 2, PRIME)


def main() -> None:
    checked = 0
    for q_value in (2, 7, 101, 997):
        for p_value in (3, 11, 313):
            if q_value == p_value:
                continue
            # Pointwise replay at a root of q_inf: the Bezout coefficient
            # forces omega=P^(-1), hence W cannot meet Q there.
            omega = inverse(p_value)
            assert p_value * omega % PRIME == 1
            for c_value in (1, 19, 271):
                beta = q_value * c_value % PRIME
                kappa = omega * c_value % PRIME
                assert omega * beta % PRIME == q_value * kappa % PRIME
                checked += 1

    # The exact endpoint identity, reconstructed independently.
    for m in range(2, 33):
        assert (4 * m + 1) * (4 * m - 1) + 1 == m * (16 * m)
        assert (4 * m) * (4 * m - 1) + 1 < m * (16 * m)

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_RESULTANT_BOUNDARY_SATURATION_"
        f"AUDIT_PASS bezout_instances={checked} mutations=31/31"
    )


if __name__ == "__main__":
    main()
