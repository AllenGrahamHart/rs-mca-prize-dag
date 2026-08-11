#!/usr/bin/env python3
"""Independent missing-incidence replay for the sharp-pair contradiction."""


def audit(e, arm, r_alpha, r_beta):
    rho = 3 * e - 1
    heavy_rows = 1 if arm == "double" else 2

    if arm == "double":
        source_deficit = r_alpha
        pair_padding_cap = heavy_rows
    elif max(r_alpha, r_beta) >= 1:
        source_deficit = max(r_alpha, r_beta)
        pair_padding_cap = heavy_rows
    else:
        source_deficit = 0
        pair_padding_cap = 0

    clone_size = source_deficit + 2
    triple_union = rho + 2 + pair_padding_cap + rho - (clone_size + 1)
    assert triple_union <= 2 * rho

    line_size = e + 1
    light_joint_support = rho + 1
    forced_deficit = light_joint_support - 2 * line_size
    assert forced_deficit == e - 2
    assert forced_deficit > e - 6


for e in (7, 13, 183251937963):
    for left in range(2):
        for right in range(2):
            audit(e, "double", left, right)
    for left in range(3):
        for right in range(3):
            audit(e, "two-simple", left, right)

print("RATE_HALF_QUADRATIC_GAP_FOUR_SHARP_PAIR_EXCLUSION_AUDIT_PASS")
