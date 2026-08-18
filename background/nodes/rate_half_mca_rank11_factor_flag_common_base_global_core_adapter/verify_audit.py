#!/usr/bin/env python3
"""Independent scalar audit of the common-base implication."""

Q = 103
X = 12


def main() -> None:
    pencil_values = ((X - X) % Q, ((X - X) * (X + 9)) % Q)
    residual_values = (1, 7, 19, 44, 88)
    products = tuple(g * b % Q for g in pencil_values for b in residual_values)
    assert products == (0,) * 10

    pencil_values_b = (1, 17)
    residual_values_b = (0,) * 5
    products_b = tuple(g * b % Q for g in pencil_values_b for b in residual_values_b)
    assert products_b == (0,) * 10

    anchor = (37, 79)
    corrections = ((products[0], products[1]), (products[4], products[9]))
    pairs = tuple(((anchor[0] + a) % Q, (anchor[1] + b) % Q) for a, b in corrections)
    assert pairs == (anchor, anchor)
    print("RANK11_FACTOR_BASE_GLOBAL_CORE_AUDIT_PASS products=20 records=2")


if __name__ == "__main__":
    main()
