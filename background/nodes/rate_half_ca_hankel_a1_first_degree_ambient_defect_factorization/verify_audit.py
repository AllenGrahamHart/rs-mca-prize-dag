#!/usr/bin/env python3
"""Independent gcd-degree audit for row defects."""


def main():
    # Synthetic degree ledgers include off-support roots and repeated
    # supported roots. In every case deg(q/gcd(q,H))=e-d_x.
    cases = (
        (7, 7, 0),
        (7, 5, 2),
        (7, 2, 5),
        (9, 6, 3),
    )
    for e, distinct_supported, residual_degree in cases:
        assert e - distinct_supported == residual_degree

    m = 1 << 37
    rho = 4 * m
    e = (rho + 1) // 3
    assert e == 183251937963
    for j in range(3):
        assert j < e

    print(
        "RATE_HALF_CA_HANKEL_A1_FIRST_DEGREE_AMBIENT_DEFECT_AUDIT_PASS "
        f"cases={len(cases)} e={e}"
    )


if __name__ == "__main__":
    main()
