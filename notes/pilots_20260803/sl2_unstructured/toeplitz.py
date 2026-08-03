#!/usr/bin/env python3
"""SL-2 pilot: THEOREM R -- the syndrome Toeplitz system has FULL RANK d
on the tangent-gated class.   (2026-08-03)

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 <this>

LEMMA W writes the depth-d window system for a word u as
    sum_{i=0}^{r'} u_{(j-i) mod n} E_i = 0,   j = n-d, ..., n-1,
a d x (r'+1) Toeplitz matrix R(u,d) in the syndrome window
(u_k, ..., u_{n-1}).  A linear dependency among its rows, with
coefficients (lambda_j), is exactly the statement that the syndrome
sequence obeys the linear recurrence with characteristic polynomial
Lambda(X) = sum_j lambda_j X^{j-(n-d)}, deg Lambda <= d-1, across all
n-k syndromes.  Since n-k >= 2d, Berlekamp-Massey turns Lambda into an
error locator of degree <= d-1, i.e. a codeword agreeing with u on
>= n-d+1 points.  The TANGENT GATE (agreement <= A = k+h, and
d <= h-2 << n-k-h) forbids that.  Hence

   THEOREM R.  On the tangent-gated class, rank R(u,d) = d exactly.

Consequence: an adversary CANNOT buy a large family by degenerating the
LINEAR part of the window system -- any blow-up must come from the
arithmetic of the divisors of X^n - 1, not from rank collapse.  (The MC
word is the illustration: its system has FULL rank w, yet its solution
set is the whole coset lattice.)

Checks:
  T1  rank R(u,d) = d for random gated words, all fixtures.
  T2  planting a codeword at distance L < d (gate violated) drops the
      rank to EXACTLY L -- the converse, so the criterion is sharp.
  T3  the MC word has FULL rank d = w yet |solutions| >> 1 (rank is not
      what the adversary degenerates).
"""
import json
import random
from itertools import combinations

from algebra import (evalpoly, locator, lemmaW, rank, root_of_unity)

random.seed(20260803)
checks = []


def ck(name, tag, ok, extra=None):
    checks.append(dict(check=name, fixture=tag, ok=bool(ok), extra=extra))


def toeplitz(u, n, d, rp):
    return [[u[(j - i) % n] for i in range(rp + 1)]
            for j in range(n - d, n)]


def main():
    res = []
    FIX = [dict(n=16, k=4, q=97, d=3), dict(n=16, k=4, q=97, d=5),
           dict(n=12, k=4, q=13, d=3), dict(n=20, k=6, q=41, d=4),
           dict(n=16, k=8, q=17, d=4)]
    for f in FIX:
        n, k, q, d = f["n"], f["k"], f["q"], f["d"]
        rp = n - k - d
        g = root_of_unity(n, q)
        H = [pow(g, i, q) for i in range(n)]
        tag = f"n{n}k{k}d{d}q{q}"
        # ---- T1: random word (generic: max agreement is small, so the
        #      tangent gate holds with room)
        for t in range(5):
            u = [0] * n
            for p in range(k, n):
                u[p] = random.randrange(q)
            r = rank(toeplitz(u, n, d, rp), q)
            ck("T1: rank = d for a generic (gated) word", f"{tag}#{t}",
               r == d, dict(rank=r, d=d))
        # ---- T2: plant an error of weight L < d on a codeword
        for L in range(1, d):
            c = [random.randrange(q) for _ in range(k)] + [0] * (n - k)
            supp = random.sample(range(n), L)
            vals = {i: random.randrange(1, q) for i in supp}
            # u = c + e  with e supported on supp: build by interpolation
            # in the evaluation domain, then take its polynomial form
            uv = [(evalpoly(c, H[i], q) + vals.get(i, 0)) % q
                  for i in range(n)]
            # inverse DFT to coefficients: u_p = (1/n) sum_i uv_i x_i^{-p}
            ninv = pow(n % q, q - 2, q)
            u = [ninv * sum(uv[i] * pow(H[i], -p % (q - 1), q)
                            for i in range(n)) % q for p in range(n)]
            # sanity: u evaluates back
            okv = all(evalpoly(u, H[i], q) == uv[i] for i in range(n))
            r = rank(toeplitz(u, n, d, rp), q)
            ck("T2: rank = L exactly when u is at distance L < d "
               "(gate violated)", f"{tag}L{L}", okv and r == L,
               dict(rank=r, L=L, d=d, dft_ok=okv))
        # ---- T3: the MC word -- full rank, many solutions
        if (n - k - d) % 2 == 0 and d <= 2:
            pass
        res.append(dict(tag=tag, n=n, k=k, d=d, q=q))

    # T3 on the banked MC fixture (16,4,w=2,q=97)
    n, k, w, q, M = 16, 4, 2, 97, 2
    rp = n - k - w
    g = root_of_unity(n, q)
    H = [pow(g, i, q) for i in range(n)]
    N0, m0 = n // M, rp // M
    T0 = [i + j * N0 for i in range(m0) for j in range(M)]
    prod0 = 1
    for i in T0:
        prod0 = prod0 * H[i] % q
    c = ((-1) ** (rp + 1) * prod0) % q
    u = [0] * n
    u[n - 1] = 1
    u[k + w - 1] = c
    r = rank(toeplitz(u, n, w, rp), q)
    nsol = sum(1 for T in combinations(range(n), rp)
               if lemmaW(u, [H[i] for i in T], n, k, w, q)[0])
    ck("T3: the MC word has FULL rank w yet many solutions "
       "(rank is not the degeneracy the adversary buys)",
       f"MC n{n}k{k}w{w}", r == w and nsol > 1,
       dict(rank=r, w=w, solutions=nsol))

    bad = [x for x in checks if not x["ok"]]
    print(f"checks: {len(checks)}   failures: {len(bad)}")
    for b in bad[:10]:
        print("  FAIL", b)
    print(f"\nMC word (16,4,w=2,q=97): rank = {r} = w, solutions = {nsol}")
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(dict(checks=checks, n_checks=len(checks),
                       n_fail=len(bad), mc=dict(rank=r, solutions=nsol),
                       verdict="PASS" if not bad else "FAIL"), fh,
                  indent=1)


if __name__ == "__main__":
    main()
