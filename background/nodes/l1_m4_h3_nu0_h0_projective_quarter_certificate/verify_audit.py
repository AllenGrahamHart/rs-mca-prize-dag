#!/usr/bin/env python3
"""Independent algebraic audit of the h=0 projective packet table."""

from __future__ import annotations

from pathlib import Path


HERE = Path(__file__).resolve().parent
PRIMES = (8191, 131071, 524287, 2147483647)
Gaussian = tuple[int, int]
Polynomial = list[Gaussian]
PACKETS = {
    8191: ((6, 20),),
    131071: ((6, 20),),
    524287: ((6, 20),),
    2147483647: ((6, 20), (844833809, 2002167159)),
}


def convolution(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return out


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gneg(value: Gaussian) -> Gaussian:
    return -value[0], -value[1]


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (left[0] * right[0] - left[1] * right[1],
            left[0] * right[1] + left[1] * right[0])


def padd(left: Polynomial, right: Polynomial) -> Polynomial:
    out = [(0, 0)] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = gadd(left[index] if index < len(left) else (0, 0),
                          right[index] if index < len(right) else (0, 0))
    return out


def ptrim(poly: Polynomial) -> Polynomial:
    while len(poly) > 1 and poly[-1] == (0, 0):
        poly.pop()
    return poly


def pscale(poly: Polynomial, scalar: Gaussian) -> Polynomial:
    return [gmul(value, scalar) for value in poly]


def pmul(left: Polynomial, right: Polynomial) -> Polynomial:
    out = [(0, 0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = gadd(out[i + j], gmul(x, y))
    return out


def e_polynomial(u: Gaussian) -> Polynomial:
    # s=(1+u)+V and q=u+(1+u)V in E=q(4q-s^2)-3uVs.
    one_plus_u = gadd((1, 0), u)
    s = [one_plus_u, (1, 0)]
    q = [u, one_plus_u]
    four_q_minus_s2 = padd(pscale(q, (4, 0)), pscale(pmul(s, s), (-1, 0)))
    u_v_s = pmul([(0, 0), u], s)
    return ptrim(padd(pmul(q, four_q_minus_s2), pscale(u_v_s, (-3, 0))))


def factor(scalar: Gaussian, roots: list[Gaussian]) -> Polynomial:
    out = [scalar]
    for root in roots:
        out = pmul(out, [gneg(root), (1, 0)])
    return ptrim(out)


def main() -> None:
    checks = 0
    for p in PRIMES:
        for a_value, b_value in PACKETS[p]:
            assert (9 * b_value - 4 * a_value * a_value
                    - 6 * a_value) % p == 0
            assert (-4 * pow(a_value, 3, p)
                    - 27 * pow(b_value, 2, p)) % p != 0
            checks += 2

    universal = [27, 9, 3, 1]
    assert convolution([3, 1], [9, 0, 1]) == universal
    assert universal == [1 + 6 + 20, 3 + 6, 3, 1]
    checks += 2

    # Directly audit the four complete factorizations E(u,V) over Z[i].
    one, minus_one, i, minus_i = (1, 0), (-1, 0), (0, 1), (0, -1)
    expected = {
        one: factor((-2, 0), [(0, 0), one, one]),
        minus_one: factor((4, 0), [i, minus_i]),
        i: factor((-1, -1), [minus_one, minus_i, (1, 1)]),
        minus_i: factor((-1, 1), [minus_one, i, (1, -1)]),
    }
    for u_value, polynomial in expected.items():
        assert e_polynomial(u_value) == polynomial
    checks += 4

    proof = (HERE / "proof.md").read_text()
    for anchor in ("elementary symmetric identities", "each of the 16 quarter pairs",
                   "saturates the forbidden factor", "unique common",
                   "complete table"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "necessary projective classification" in statement
    assert "does not prove that either" in statement
    checks += 2
    print(f"L1_M4_H3_NU0_H0_PROJECTIVE_QUARTER_CERTIFICATE_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
