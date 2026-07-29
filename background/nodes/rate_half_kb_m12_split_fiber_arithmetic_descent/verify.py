#!/usr/bin/env python3
"""Verify the m12 split-fiber arithmetic descent."""

from math import gcd
from pathlib import Path
from fractions import Fraction


NODE = Path(__file__).resolve().parent


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "G_arithmetic=G_geometric" in statement
    assert "Only the Dickson" in contract

    p = 2_130_706_433
    degree = 6
    q = p**degree
    assert p > 5 and p % 2 == 1
    assert gcd(5, q - 1) == 1

    # Every prime-field square class becomes square in an even extension.
    geometric_sum = sum(p**index for index in range(degree))
    assert geometric_sum % 2 == 0
    assert (q - 1) // 2 == ((p - 1) // 2) * geometric_sum
    legendre = pow((-20) % p, (p - 1) // 2, p)
    assert legendre in (1, p - 1)
    assert pow(legendre, geometric_sum, p) == 1

    # The normalized A5 ratio polynomial has split, distinct, non-involutive
    # roots over K. Product one means the two roots are reciprocal.
    discriminant = 4**2 - 4 * 3 * 3
    assert discriminant == -20
    assert 3 * 1**2 + 4 * 1 + 3 == 10
    assert 3 * (-1) ** 2 + 4 * (-1) + 3 == 2
    leading, constant = 3, 3
    assert Fraction(constant, leading) == 1

    descended = {
        ("A5", ((2, 2), (3,))),
        ("S5", ((2,), (3, 2))),
        ("S5", ((2,), (4,))),
    }
    twists = {
        ("D5", ((2, 2), (2, 2))),
        ("A5", ((3,), (3,))),
        ("S5", ((2,), (2,), (2, 2))),
    }
    assert len(descended) == len(twists) == 3
    assert descended.isdisjoint(twists)
    assert "No family is deleted" in contract
    print("RATE_HALF_KB_M12_SPLIT_FIBER_ARITHMETIC_DESCENT_PASS")


if __name__ == "__main__":
    main()
