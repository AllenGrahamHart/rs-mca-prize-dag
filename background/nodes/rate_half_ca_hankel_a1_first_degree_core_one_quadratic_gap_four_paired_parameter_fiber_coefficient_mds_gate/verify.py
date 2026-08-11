#!/usr/bin/env python3
"""Exact checks for the parameter-fiber coefficient-MDS gate."""

E = 183251937963
P = 274877906944
Q = 101


def inv(x: int) -> int:
    return pow(x % Q, Q - 2, Q)


def parity_replay() -> None:
    zset = list(range(1, 8))
    c = len(zset)
    m = 3

    def coeffs(t: int) -> tuple[int, int, int]:
        return (t * (t + 1) % Q, -(2 * t + 1) % Q, 1)

    zeta = {t: (t + 3) % Q for t in zset}
    checks = []
    for i in range(3):
        for ell in range(c - m - 1):
            total = 0
            for t in zset:
                deriv = 1
                for u in zset:
                    if u != t:
                        deriv = deriv * (t - u) % Q
                total += zeta[t] * coeffs(t)[i] * pow(t, ell, Q) * inv(deriv)
            checks.append(total % Q)
    assert checks == [0] * len(checks)

    zeta[zset[0]] += 1
    tampered = 0
    for i in range(3):
        for ell in range(c - m - 1):
            total = 0
            for t in zset:
                deriv = 1
                for u in zset:
                    if u != t:
                        deriv = deriv * (t - u) % Q
                total += zeta[t] * coeffs(t)[i] * pow(t, ell, Q) * inv(deriv)
            tampered |= total % Q
    assert tampered != 0


def main() -> None:
    p = (3 * E - 1) // 2
    assert p == P

    ext_rows = (p - 2) * (E + 1)
    strict_rows = (p - 1) * (p + 2 - E)
    assert ext_rows == 50371909150609548946088
    assert strict_rows == 25185954575671278348969
    assert 2 * E == 366503875926
    assert p + 2 == 274877906946
    parity_replay()
    print("PASS parameter-fiber coefficient-MDS gate tamper=1/1")


if __name__ == "__main__":
    main()
