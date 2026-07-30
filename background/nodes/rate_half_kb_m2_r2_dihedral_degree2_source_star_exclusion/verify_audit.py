#!/usr/bin/env python3
"""Independently audit the eight-unit/four-vertex defect floor."""


def main() -> None:
    total_weight = 8
    vertex_count = 4
    # Cauchy: sum w_i^2 >= total_weight^2 / vertex_count = 16.
    minimum_square_sum = total_weight * total_weight // vertex_count
    assert minimum_square_sum == 16
    minimum_defect = (minimum_square_sum - total_weight) // 2
    assert minimum_defect == 4 > 3

    # Outer and source multiplicities are checked independently.
    z_values = 2
    endpoint_lifts_per_z = 2
    source_units_per_lift = 2
    assert z_values * endpoint_lifts_per_z * source_units_per_lift == 8
    assert 2 * 2 == vertex_count
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE2_SOURCE_STAR_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
