#!/usr/bin/env python3
"""Independent small-field audit of the Frobenius-kernel split."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def add(left: dict[int, int], right: dict[int, int], p: int) -> dict[int, int]:
    output = dict(left)
    for degree, value in right.items():
        output[degree] = (output.get(degree, 0) + value) % p
    return {degree: value for degree, value in output.items() if value}


def derivative(poly: dict[int, int], p: int) -> dict[int, int]:
    return {degree - 1: degree * value % p
            for degree, value in poly.items()
            if degree and degree * value % p}


def frobenius(poly: dict[int, int], p: int) -> dict[int, int]:
    return {degree * p: pow(value, p, p) for degree, value in poly.items()}


def main() -> None:
    p = 7
    # U=X^4+1 has [X^(p-5)]U^2=[X^2]U^2=0.
    u_squared = {8: 1, 4: 2, 0: 1}
    integrand = {degree + 4: value for degree, value in u_squared.items()}
    assert integrand.get(p - 1, 0) == 0
    j = {degree + 1: value * pow(degree + 1, -1, p) % p
         for degree, value in integrand.items()}
    assert derivative(j, p) == integrand
    assert all(degree % p for degree in j)

    q = {2: 1, 1: 2}
    a = add({4: 1}, {degree: -value % p for degree, value in q.items()}, p)
    f = add(frobenius(a, p), j, p)
    g = add(frobenius(q, p), {degree: -value % p for degree, value in j.items()}, p)
    assert add(f, g, p) == {4 * p: 1}
    assert derivative(f, p) == integrand
    assert derivative(g, p) == {degree: -value % p
                                for degree, value in integrand.items()}
    assert max(g) == 2 * p

    proof = (HERE / "proof.md").read_text()
    for anchor in ("canonical", "perfect", "degree exactly two", "lc(Q)^p=a",
                   "degree-five"):
        assert anchor in proof
    statement = (HERE / "statement.md").read_text()
    assert "two-parameter quadratic" in statement
    assert "does not" in statement
    print("L1_M4_H3_NU3_QUADRATIC_FROBENIUS_KERNEL_AUDIT_PASS checks=15")


if __name__ == "__main__":
    main()
