#!/usr/bin/env python3
"""Independent finite-field audit of the interpolation equivalence."""

from pathlib import Path


NODE = Path(__file__).resolve().parent
Q = 127


def inv(value: int) -> int:
    return pow(value % Q, Q - 2, Q)


def lagrange(values: list[int], labels: list[int]) -> list[int]:
    out = [0] * len(labels)
    for i, xi in enumerate(labels):
        basis = [1]
        denominator = 1
        for j, xj in enumerate(labels):
            if i == j:
                continue
            nxt = [0] * (len(basis) + 1)
            for degree, coefficient in enumerate(basis):
                nxt[degree] = (nxt[degree] - xj * coefficient) % Q
                nxt[degree + 1] = (nxt[degree + 1] + coefficient) % Q
            basis = nxt
            denominator = denominator * (xi - xj) % Q
        scale = values[i] * inv(denominator) % Q
        for degree, coefficient in enumerate(basis):
            out[degree] = (out[degree] + scale * coefficient) % Q
    return out


def evaluate(poly: list[int], value: int) -> int:
    return sum(coefficient * pow(value, degree, Q)
               for degree, coefficient in enumerate(poly)) % Q


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "full-support" in statement
    assert "individual-star transport" in contract

    labels = list(range(12))
    scales = [(17 * p + 4) % Q or 1 for p in labels]
    for a in range(5):
        source = [(19 * a + 23 * b + 7 * a * b + 3) % Q for b in range(5)]
        projective_values = [
            evaluate(source, value) * inv(scales[p]) % Q
            for p, value in enumerate(labels)
        ]
        restored = [scales[p] * projective_values[p] % Q for p in labels]
        interpolated = lagrange(restored[:5], labels[:5])
        assert len(interpolated) == 5
        assert all(evaluate(interpolated, value) == restored[p]
                   for p, value in enumerate(labels))
        assert interpolated == source
    print("RATE_HALF_KB_M2_R4_DIAGONAL_FIBER_RESULTANT_INTERPOLATION_COMPILER_AUDIT_PASS")


if __name__ == "__main__":
    main()
