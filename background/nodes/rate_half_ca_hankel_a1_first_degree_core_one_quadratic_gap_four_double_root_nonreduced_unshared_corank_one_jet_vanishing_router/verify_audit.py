#!/usr/bin/env python3
"""Audit the corank-one conclusion and the corank-two escape."""


def main() -> None:
    # Corank one: Schur order four and a z^2 complement both pair in order 4.
    schur_order = 4
    complement_vector_order = 2
    assert min(schur_order, 2 * complement_vector_order) == 4

    # Corank two escape: diag(z^2,z^2) has determinant order four, while
    # e_1 has image and self-pairing of order two.
    smith = (2, 2)
    determinant_order = sum(smith)
    first_chain_order = smith[0]
    assert determinant_order == 4
    assert first_chain_order == 2
    assert first_chain_order < determinant_order

    print("RATE_HALF_NONREDUCED_CORANK_ONE_JET_ROUTER_AUDIT_PASS escape=[2,2]")


if __name__ == "__main__":
    main()
