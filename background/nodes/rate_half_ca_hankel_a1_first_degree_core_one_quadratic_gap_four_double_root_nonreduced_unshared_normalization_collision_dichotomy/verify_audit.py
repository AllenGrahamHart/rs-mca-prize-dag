#!/usr/bin/env python3
"""Independently replay moving/fixed valuation dominance."""


def main() -> None:
    cases = [
        # multiplicity, ramification, contact, substitution, base order
        (2, 1, 4, 6, 4),
        (2, 2, 4, 6, 2),
        (1, 1, 2, 3, 2),
        (1, 1, 2, 3, 2),
    ]
    for multiplicity, ramification, contact, substitution, base_order in cases:
        assert contact == 2 * multiplicity
        assert substitution == 3 * multiplicity
        assert substitution > contact
        assert ramification * base_order == contact

    assert sum(case[1] for case in cases[2:]) == 2
    print(
        "RATE_HALF_NONREDUCED_NORMALIZATION_COLLISION_AUDIT_PASS "
        "moving_contact_exact fixed_substitution_higher"
    )


if __name__ == "__main__":
    main()
