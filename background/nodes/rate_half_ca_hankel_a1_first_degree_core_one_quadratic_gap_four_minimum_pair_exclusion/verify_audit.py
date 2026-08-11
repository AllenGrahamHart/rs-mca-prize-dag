#!/usr/bin/env python3
"""Independent incidence-ledger audit of the g=e-1 endgame."""


for e in (7, 17, 183251937963):
    rho = 3 * e - 1
    for R in range(5):
        n_difference = R + 6
        common_light = rho - R - 4
        assert common_light + n_difference == rho + 2

        g = e - 1
        line_size = g + 1
        slack = 2 * e - R - 3
        for d_line in (0, 1):
            total_line_misses = 3 * line_size + d_line
            common_line_misses = total_line_misses - n_difference
            positive_slack = e - 6 - d_line
            zero_slack = slack - positive_slack
            assert common_line_misses == common_light + d_line - 1
            assert common_line_misses - zero_slack == 2 * e - 9
            assert common_line_misses > zero_slack

print("RATE_HALF_QUADRATIC_MINIMUM_PAIR_EXCLUSION_AUDIT_PASS")
