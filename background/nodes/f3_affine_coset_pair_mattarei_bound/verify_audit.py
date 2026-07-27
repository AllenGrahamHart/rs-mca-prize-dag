#!/usr/bin/env python3
"""Independent small-field scope and mutation audit for the Mattarei transport."""

from __future__ import annotations


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for q in range(2, int(n**0.5) + 1):
        if n % q == 0:
            return False
    return True


def factors(n: int) -> set[int]:
    ans: set[int] = set()
    q = 2
    while q * q <= n:
        if n % q == 0:
            ans.add(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        ans.add(n)
    return ans


def primitive_root(p: int) -> int:
    fac = factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g
    raise AssertionError(p)


def main() -> None:
    fixtures = 0
    outside_slopes = 0
    for p in range(5, 128):
        if not is_prime(p):
            continue
        g = primitive_root(p)
        for d in range(4, p):
            if (p - 1) % d:
                continue
            m = (p - 1) // d
            if d**3 < 4 * m:
                continue
            subgroup = {pow(g, d * j, p) for j in range(m)}
            for alpha in range(1, p):
                for beta in range(1, p):
                    count = sum((alpha * u + beta) % p in subgroup for u in subgroup)
                    # count < 3*2^(-2/3)m^(2/3), cubed without radicals.
                    assert 4 * count**3 < 27 * m**2, (p, d, m, alpha, beta, count)
                    fixtures += 1
                    if alpha not in subgroup and count:
                        outside_slopes += 1

    assert fixtures > 100_000
    assert outside_slopes > 0

    # The forbidden beta=0 (proportional forms) extension is false.
    p, d = 113, 8
    m = (p - 1) // d
    assert d**3 >= 4 * m
    proportional_count = m
    assert 4 * proportional_count**3 >= 27 * m**2

    print(
        "F3_AFFINE_COSET_PAIR_MATTAREI_BOUND_AUDIT_PASS "
        f"fixtures={fixtures} outside_slopes={outside_slopes} "
        f"proportional_falsifier=F_{p}/m{m}"
    )


if __name__ == "__main__":
    main()
