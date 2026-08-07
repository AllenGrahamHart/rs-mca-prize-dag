#!/usr/bin/env python3
"""Independent modular audit of the parity-adapted quadratic norm."""

from __future__ import annotations

import random


def h(u, v, w, p):
    return (u*u + v*v + w*w - 2*(u*v + u*w + v*w)) % p


def main():
    rng = random.Random(0x1A6)
    checks = 0
    mutations = 0
    for p in (97, 193, 257, 769, 12289):
        for _ in range(200):
            t = rng.randrange(p)
            d = t*t % p
            s = rng.randrange(p)
            v = rng.randrange(p)
            w = rng.randrange(p)
            c = (s*s + 4*d - 2*s*(v+w) + (v-w)*(v-w)) % p
            coefficient = 4*(s-v-w) % p
            left = h(s+2*t, v, w, p) * h(s-2*t, v, w, p) % p
            right = (c*c - d*coefficient*coefficient) % p
            if left != right:
                raise AssertionError((p, s, d, v, w, left, right))
            checks += 1
            wrong = (c*c + d*coefficient*coefficient) % p
            mutations += wrong != left
    if checks != 1000 or mutations < 900:
        raise AssertionError((checks, mutations))
    print(
        "DLI_WCL_ELL1_WEIGHT6_PARITY_HERON_DESCENT_AUDIT_PASS "
        f"modular_checks={checks} mutations_caught={mutations}"
    )


if __name__ == "__main__":
    main()
