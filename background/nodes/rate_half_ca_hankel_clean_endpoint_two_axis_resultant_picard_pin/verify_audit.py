#!/usr/bin/env python3
"""Independent divisor-class audit for the degree-one Picard pin."""


def main() -> None:
    checked = 0
    for m in range(2, 65):
        rho = 4 * m - 1
        n_value = 16 * m
        t_value = 4 * m + 1
        for b_degree in range(1, m):
            ambient_degree = n_value * m + b_degree * rho
            infinity_degree = (t_value + b_degree) * rho
            affine_degree = ambient_degree - infinity_degree
            assert affine_degree == 1

            # Off-by-one multiplicity destroys the point divisor.
            bad_affine = ambient_degree - (t_value + b_degree - 1) * rho
            assert bad_affine == rho + 1 != 1
            checked += 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_TWO_AXIS_RESULTANT_PICARD_PIN_"
        f"AUDIT_PASS divisor_profiles={checked}"
    )


if __name__ == "__main__":
    main()
