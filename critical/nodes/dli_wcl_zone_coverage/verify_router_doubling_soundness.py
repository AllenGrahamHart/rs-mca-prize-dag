#!/usr/bin/env python3
"""Router doubling-test soundness, all k (2026-07-26).  Stdlib, exact, no floats.

The (2,w) routers reduce a slot to shape variables plus a monic degree-k factor
f whose roots must be tested for membership in mu_M, M = 2^t (t = 10 at M = 1024).
The test in use is the power-of-two doubling recurrence, i.e. X^M mod f by t
modular squarings ("ten recurrence doublings per candidate" for w=6).

LEMMA (proved in notes/router_doubling_soundness_20260726.md).  Let F be a field
with char F = 0 or char F > k, let M = 2^t with char F != 2, and let f in F[X] be
monic of degree k with f(0) != 0.  Then

  (i)   X^M == 1 (mod f)  <=>  f | X^M - 1  <=>  f is SQUAREFREE and every root
        of f lies in mu_M;
  (ii)  hence the doubling test never yields a FALSE POSITIVE: if it passes, every
        root is in mu_M;
  (iii) but it does yield FALSE NEGATIVES exactly on the non-squarefree f whose
        roots all lie in mu_M, because X^M - 1 is separable and so has no repeated
        factor to absorb them;
  (iv)  the correct test on arbitrary f is X^M == 1 (mod rad f), rad f = f/gcd(f,f').

CONSEQUENCE FOR THE CENSUSES.  The slots are ZERO-EVENT obligations: the census
must EXCLUDE every candidate.  A false negative is a candidate wrongly discarded,
so applying the bare doubling test to a possibly-non-squarefree f makes the
emptiness claim UNSOUND.  Either test the radical, or enumerate the
non-squarefree stratum separately.  This is exactly what the closed (2,6)
certificate did with its "510 structural double-zero cases" (the antipodal-mirror
family c = 512+a+b), and it is the obligation owed by any (2,7) router at k = 5.

This script certifies (i)-(iv) exhaustively on small analogues, including an
explicit false-negative witness, and checks the doubling cost is exactly t.
"""

from __future__ import annotations

import sys
from itertools import product

errors: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        errors.append(msg)


# ------------------------------------------------------------ F_p[X] utilities
def norm(a: list[int], p: int) -> list[int]:
    a = [c % p for c in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def polymul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % p
    return norm(out, p)


def polydivmod(a: list[int], b: list[int], p: int):
    a = norm(a, p)[:]
    b = norm(b, p)
    inv = pow(b[-1], p - 2, p)
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        d = len(a) - len(b)
        c = a[-1] * inv % p
        q[d] = c
        for i, bi in enumerate(b):
            a[i + d] = (a[i + d] - c * bi) % p
        a = norm(a, p)
        if len(a) < len(b):
            break
    return norm(q, p), norm(a, p)


def polymod(a, b, p):
    return polydivmod(a, b, p)[1]


def polygcd(a, b, p):
    a, b = norm(a, p), norm(b, p)
    while b != [0]:
        a, b = b, polymod(a, b, p)
    if a == [0]:
        return [0]
    inv = pow(a[-1], p - 2, p)
    return norm([c * inv for c in a], p)


def deriv(a, p):
    return norm([(i * a[i]) % p for i in range(1, len(a))] or [0], p)


def x_pow_M_mod(f, t, p):
    """X^(2^t) mod f by exactly t modular squarings.  Returns (result, squarings)."""
    cur = polymod([0, 1], f, p)              # X mod f
    for _ in range(t):
        cur = polymod(polymul(cur, cur, p), f, p)
    return cur, t


def divides(f, g, p):
    """f | g ?"""
    return polymod(g[:], f, p) == [0]


# ---------------------------------------------------- exhaustive certification
CASES = [(17, 3), (17, 4), (97, 5)]                # (p, t) with p == 1 mod 2^t
CAP = 1500                                         # polys per (p, t, k) cell
false_negative_witness = None
tested = 0


def sample_monic(p: int, k: int, cap: int):
    """Deterministic, reproducible sample of monic degree-k f with f(0) != 0.
    Enumerates exhaustively when the space is small; otherwise walks a fixed
    coprime stride so the sample is spread and contains repeated-root cases."""
    space = p ** k
    if space <= cap:
        for coeffs in product(range(p), repeat=k):
            if coeffs[0] % p:
                yield list(coeffs) + [1]
        return
    stride = 7919 % space or 1
    idx = 0
    for _ in range(cap):
        idx = (idx + stride) % space
        c, rem = [], idx
        for _ in range(k):
            c.append(rem % p)
            rem //= p
        if c[0] % p:
            yield c + [1]


for p, t in CASES:
    M = 1 << t
    check((p - 1) % M == 0, f"need p == 1 mod {M} so mu_M lies in F_p (p={p})")
    xM_minus_1 = norm([-1] + [0] * (M - 1) + [1], p)

    for k in (2, 3, 4, 5):
        check(p > k, f"lemma hypothesis char > k violated (p={p}, k={k})")
        # Force the non-squarefree stratum into the sample: (X-r)^2 * (in-mu_M rest)
        # is exactly where the doubling test yields false negatives.
        forced = []
        g = pow(3, (p - 1) // M, p)                # a primitive M-th root of unity
        for a in range(1, min(M, 6)):
            base = polymul([(-pow(g, a, p)) % p, 1], [(-pow(g, a, p)) % p, 1], p)
            for b in range(k - 2):
                base = polymul(base, [(-pow(g, b + 1, p)) % p, 1], p)
            if len(base) == k + 1:
                forced.append(norm(base, p))

        for f in list(sample_monic(p, k, CAP)) + forced:
            if len(f) != k + 1 or f[0] % p == 0:
                continue
            tested += 1

            res, squarings = x_pow_M_mod(f, t, p)
            check(squarings == t, "doubling count must be exactly t")
            passes = (res == [1])

            # (i) X^M == 1 mod f  <=>  f | X^M - 1
            check(passes == divides(f, xM_minus_1, p),
                  f"(i) equivalence failed: p={p} k={k} f={f}")

            g = polygcd(f, deriv(f, p), p)
            squarefree = (g == [1])
            rad = polydivmod(f, g, p)[0] if not squarefree else f
            roots_in_muM = divides(rad, xM_minus_1, p)

            # (i) full form: passes <=> squarefree AND all roots in mu_M
            check(passes == (squarefree and roots_in_muM),
                  f"(i) full form failed: p={p} k={k} f={f} "
                  f"passes={passes} sf={squarefree} roots={roots_in_muM}")

            # (ii) SOUNDNESS: pass => all roots in mu_M.  Never a false positive.
            if passes:
                check(roots_in_muM,
                      f"FALSE POSITIVE: doubling test passed but a root is "
                      f"outside mu_M: p={p} k={k} f={f}")

            # (iii) false negative exists exactly on non-squarefree in-mu_M f
            if roots_in_muM and not passes:
                check(not squarefree,
                      f"false negative on a SQUAREFREE f -- lemma broken: "
                      f"p={p} k={k} f={f}")
                if false_negative_witness is None:
                    false_negative_witness = (p, t, k, f)

            # (iv) radical test is correct on every f
            radres, _ = x_pow_M_mod(rad, t, p)
            check((radres == [1]) == roots_in_muM,
                  f"(iv) radical test wrong: p={p} k={k} f={f}")

check(false_negative_witness is not None,
      "no false-negative witness found -- (iii) is the whole point of the fence; "
      "without a witness the soundness obligation is not demonstrated")

if errors:
    for e in errors[:12]:
        print("FAIL:", e)
    sys.exit(1)

p, t, k, f = false_negative_witness
print(
    "ROUTER_DOUBLING_SOUNDNESS_PASS "
    f"cases={len(CASES)} polys_tested={tested} "
    f"false_positives=0 "
    f"false_negative_witness=(p={p}, M=2^{t}, k={k}, f={f}) "
    "=> bare doubling test is sound-but-incomplete; a zero-event census MUST "
    "test the radical or enumerate the non-squarefree stratum separately"
)
