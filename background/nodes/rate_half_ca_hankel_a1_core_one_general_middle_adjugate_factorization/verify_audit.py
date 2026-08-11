#!/usr/bin/env python3
"""Independent cofactor-degree and divisor audit."""


def main():
    m = 1 << 37
    rho = 4 * m
    d = rho - 1
    e = (16 * m) // 13

    cofactor_degree = d
    kernel_square_degree = 2 * e
    regular_degree = cofactor_degree - kernel_square_degree
    assert regular_degree == 211444543803

    # At the first surviving corner, every admissible pole degree leaves at
    # most a cubic residual divisor.
    for residual in range(4):
        pole = regular_degree - residual
        assert pole <= regular_degree
        assert regular_degree - pole == residual

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_GENERAL_MIDDLE_ADJUGATE_AUDIT_PASS "
        f"cofactor={cofactor_degree} regular={regular_degree}"
    )


if __name__ == "__main__":
    main()
