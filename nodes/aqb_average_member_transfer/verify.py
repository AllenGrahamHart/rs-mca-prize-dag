#!/usr/bin/env python3
"""Light verifier for the average-to-member transfer."""

from fractions import Fraction
from itertools import product


def main() -> None:
    for length in range(1, 7):
        for values in product(range(5), repeat=length):
            for threshold_num in range(0, 9):
                threshold = Fraction(threshold_num, 2)
                avg = sum(Fraction(v, 1) for v in values) / length
                if avg > threshold:
                    assert any(Fraction(v, 1) > threshold for v in values), (values, threshold)

    print("PASS: finite average above threshold forces one member above threshold")


if __name__ == "__main__":
    main()
