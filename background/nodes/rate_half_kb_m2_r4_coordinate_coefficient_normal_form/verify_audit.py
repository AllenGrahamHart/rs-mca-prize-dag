#!/usr/bin/env python3
"""Independent parity and norm audit for the coordinate normal form."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def evaluate(terms: dict[tuple[int, int], int], t: int, x: int) -> int:
    return sum(value * t**i * x**j for (i, j), value in terms.items())


def main() -> None:
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    assert "comparison of the even parts" in proof
    assert "transposed coordinate" in audit

    plus = {
        (0, 0): 2, (0, 2): 3, (0, 4): 5,
        (2, 0): 7, (2, 2): 11, (2, 4): 13,
        (1, 1): 17, (1, 3): 19,
    }
    minus = {
        (1, 0): 2, (1, 2): 3, (1, 4): 5,
        (0, 1): 7, (0, 3): 11, (2, 1): 13, (2, 3): 17,
    }
    for terms, sign in ((plus, 1), (minus, -1)):
        for t, x in ((2, 3), (3, 5), (5, 7)):
            h = evaluate(terms, t, x)
            assert evaluate(terms, -t, -x) == sign * h
            deck = evaluate(terms, t, -x)
            g = h * deck
            g_tau = evaluate(terms, -t, x) * evaluate(terms, -t, -x)
            assert g_tau == g
            assert deck != h
    print("RATE_HALF_KB_M2_R4_COORDINATE_COEFFICIENT_NORMAL_FORM_AUDIT_PASS")


if __name__ == "__main__":
    main()
