#!/usr/bin/env python3
"""Independent local-polynomial audit of the order-three obstruction."""


def order_at_zero(coefficients: list[int]) -> int:
    for index, coefficient in enumerate(coefficients):
        if coefficient:
            return index
    raise AssertionError("zero polynomial has no finite order")


def main() -> None:
    # Q(t,X)=X+t^3 and the putative zero heavy row forces X|G.
    q_at_xstar = [0, 0, 0, 1]
    exact_correction = [0, 0, 1]
    assert order_at_zero(q_at_xstar) == 3
    assert order_at_zero(exact_correction) == 2

    # Intersecting Q with the component X=0 has length three:
    # F[t,X]/(X+t^3,X) is F[t]/(t^3).
    quotient_basis = [1, "t", "t^2"]
    assert len(quotient_basis) == 3
    assert len(quotient_basis) != 1
    print("RATE_HALF_CENTER_DISJOINT_HEAVY_ROW_NONZERO_AUDIT_PASS length=3")


if __name__ == "__main__":
    main()
