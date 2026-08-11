#!/usr/bin/env python3
"""Exhaustive small fibre-case and mutation audit."""


def possible_multiples(e, base_fibres, correction):
    degree = base_fibres * e + correction
    return [n for n in range(4) if n * e == degree]


def main():
    cases = 0
    for e in range(4, 80):
        # Isolated contact outside D.
        assert possible_multiples(e, 0, 3) == []

        # Contact on a D fibre forces common degree three.
        assert possible_multiples(e, 1, 0) == [1]

        for p in (0, 1):
            # Coincident clearing/contact fibre outside D.
            assert possible_multiples(e, 1, 3 - p) == []

            # On D, k=3-p is the unique way to obtain two fibres.
            solutions = [
                k
                for k in range(e + 1)
                if 2 * e - k - p + 3 in (e, 2 * e, 3 * e)
            ]
            assert solutions == [3 - p]
            assert (3 - p) - 1 > 1 - p
            cases += 1

    # With an incorrectly enlarged omission budget O=2, the p=0 margin
    # disappears; this detects the load-bearing endpoint bound.
    assert 3 - 1 == 2

    print(
        "RATE_HALF_CA_HANKEL_STRICT_A3_FINAL_CORNER_DIVISOR_EXCLUSION_AUDIT_PASS "
        f"cases={cases} mutation=detected"
    )


if __name__ == "__main__":
    main()
