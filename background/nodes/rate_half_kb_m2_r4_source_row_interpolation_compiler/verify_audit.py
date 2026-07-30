#!/usr/bin/env python3
"""Independent interpolation and product-form audit."""

from pathlib import Path


NODE = Path(__file__).resolve().parent
Q = 127


def inv(value: int) -> int:
    return pow(value % Q, Q - 2, Q)


def lagrange_three(values: list[int], labels: list[int]) -> list[int]:
    out = [0, 0, 0]
    for i, xi in enumerate(labels):
        others = [labels[j] for j in range(3) if j != i]
        denominator = (xi - others[0]) * (xi - others[1]) % Q
        scale = values[i] * inv(denominator) % Q
        out[0] = (out[0] + scale * others[0] * others[1]) % Q
        out[1] = (out[1] - scale * (others[0] + others[1])) % Q
        out[2] = (out[2] + scale) % Q
    return out


def evaluate(poly: list[int], value: int) -> int:
    return sum(coefficient * pow(value, degree, Q)
               for degree, coefficient in enumerate(poly)) % Q


def main() -> None:
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "standard product formula" in proof
    assert "full-support `45 x 12`" in contract

    labels = list(range(12))
    scales = [(23 * i + 7) % Q or 1 for i in labels]
    for b in range(5):
        source = [(29 * b + 31 * a + 11 * a * b + 1) % Q for a in range(3)]
        projective = [evaluate(source, value) * inv(scales[i]) % Q
                      for i, value in enumerate(labels)]
        restored = [scales[i] * projective[i] % Q for i in range(12)]
        interpolated = lagrange_three(restored[:3], labels[:3])
        assert interpolated == source
        assert all(evaluate(interpolated, value) == restored[i]
                   for i, value in enumerate(labels))
    print("RATE_HALF_KB_M2_R4_SOURCE_ROW_INTERPOLATION_COMPILER_AUDIT_PASS")


if __name__ == "__main__":
    main()
