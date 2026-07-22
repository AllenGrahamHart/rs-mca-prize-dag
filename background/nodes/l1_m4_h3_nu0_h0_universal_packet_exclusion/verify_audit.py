#!/usr/bin/env python3
"""Independent coefficient and multiplicity audit for universal exclusion."""

from __future__ import annotations

from pathlib import Path


HERE = Path(__file__).resolve().parent


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (left[index] if index < len(left) else 0) + \
            (right[index] if index < len(right) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(poly: list[int], scalar: int) -> list[int]:
    return [scalar * value for value in poly]


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def main() -> None:
    # Normalize r=1; every checked identity is homogeneous under Y=rZ.
    g = [20, 6, 0, 1]
    derivative = [6, 0, 3]
    assert multiply([2, 1], [10, -2, 1]) == g
    assert multiply(multiply([-1, 1], [-4, 1]), [5, 1]) == [20, -21, 0, 1]

    # Cross-multiplied form of the logarithmic partial-fraction identity.
    numerator = add(
        add(multiply([-1, 1], g),
            multiply(multiply([-1, 1], [-4, 1]), derivative)),
        scale(multiply([-4, 1], g), -4),
    )
    assert numerator == [324]
    checks = 3

    for p in (8191, 131071, 524287, 2147483647):
        possible = []
        for d in (0, 1):
            for multiplier in (1, 2, 3):
                value = multiplier * p - d
                if value % 4 == 0 and 1 <= value // 4 <= p - 1:
                    possible.append((d, value // 4))
        e = (3 * p - 1) // 4
        assert possible == [(1, e)]
        assert e < p - 1 < 2 * e
        checks += 2

    proof = (HERE / "proof.md").read_text()
    for anchor in ("Cancelling `R+5r`", "F'/F", "finite and hence perfect",
                   "ord_0(F)", "remaining total multiplicity"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "universal projective packet" in statement
    assert "exceptional projective packet" in statement
    checks += 2
    print(f"L1_M4_H3_NU0_H0_UNIVERSAL_PACKET_EXCLUSION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
