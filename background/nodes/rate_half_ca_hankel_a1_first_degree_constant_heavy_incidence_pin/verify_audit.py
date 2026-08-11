#!/usr/bin/env python3
"""Independent incidence-saturation gap audit."""


def main():
    m = 1 << 37
    rho = 4 * m
    e = (rho + 1) // 3

    rows = []
    for s, a in ((0, 2), (1, 1)):
        d = rho - s
        delta = d - (s + 1) * e
        light_rows = 3 * rho + 3 + a
        heavy_plus_omission = (rho + 4) * d - light_rows * e
        residual_gap = 2 * delta - heavy_plus_omission
        rows.append((s, a, heavy_plus_omission, residual_gap))

    assert rows[0][-1] == 1
    assert rows[1][-1] == 2

    print(
        "RATE_HALF_CA_HANKEL_A1_FIRST_DEGREE_CONSTANT_HEAVY_PIN_AUDIT_PASS "
        f"rows={rows}"
    )


if __name__ == "__main__":
    main()
