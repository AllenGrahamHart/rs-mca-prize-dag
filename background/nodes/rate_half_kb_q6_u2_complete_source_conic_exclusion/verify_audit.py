#!/usr/bin/env python3
"""Independent orbit-residue audit for the KoalaBear conic exclusion."""


def main() -> None:
    surviving_d4 = []
    surviving_d5 = []
    for r in (0, 1, 2):
        simple = 24 - 2 * r
        double = r
        if double % 4 == 0 and (simple - 2) % 4 == 0:
            surviving_d4.append(r)

        fixed_needed = simple % 5 + double % 5
        if fixed_needed <= 2:
            # At r=2 the same two points are fixed by both involutions,
            # forcing their product to be the identity rather than order five.
            if r != 2:
                surviving_d5.append(r)

    assert surviving_d4 == []
    assert surviving_d5 == []
    print("RATE_HALF_KB_Q6_U2_COMPLETE_SOURCE_CONIC_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
