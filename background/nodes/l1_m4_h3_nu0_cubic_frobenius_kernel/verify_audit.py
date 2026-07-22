#!/usr/bin/env python3
"""Independent sparse-polynomial audit of the nu=0 kernel split."""

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
    # This source models R^2 H. Its two Cartier slots 4 and p+4 vanish.
    source = {0: 3, 1: 2, 3: 4, 5: 1, 8: 6}
    assert source.get(4, 0) == source.get(p + 4, 0) == 0
    integrand = {degree + p - 5: value for degree, value in source.items()}
    assert integrand.get(p - 1, 0) == integrand.get(2 * p - 1, 0) == 0
    j = {degree + 1: value * pow(degree + 1, -1, p) % p
         for degree, value in integrand.items()}
    assert derivative(j, p) == integrand
    assert all(degree % p for degree in j)
    assert min(j) == p - 4

    q = {3: 2, 2: 1, 1: 4}
    a = add({5: 1}, {degree: -value % p for degree, value in q.items()}, p)
    f = add(frobenius(a, p), j, p)
    g = add(frobenius(q, p), {degree: -value % p for degree, value in j.items()}, p)
    assert add(f, g, p) == {5 * p: 1}
    assert derivative(f, p) == integrand
    assert derivative(g, p) == {degree: -value % p
                                for degree, value in integrand.items()}
    assert max(g) == 3 * p

    proof = (HERE / "proof.md").read_text()
    for anchor in ("canonical", "perfect", "degree exactly three",
                   "lc(Q)^p=a", "degree `p-4`"):
        assert anchor in proof
    statement = (HERE / "statement.md").read_text()
    assert "three-scalar cubic" in statement
    assert "does not" in statement
    print("L1_M4_H3_NU0_CUBIC_FROBENIUS_KERNEL_AUDIT_PASS checks=18")


if __name__ == "__main__":
    main()
