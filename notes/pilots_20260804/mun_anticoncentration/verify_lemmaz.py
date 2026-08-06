#!/usr/bin/env python3
"""Round 15 -- LEMMA Z: the characteristic-ZERO structure of the window.

Claim (pre-registered, section (Z) of PREREG.md).  Let n = 2^m, S <= Z/n,
chi_S(X) = sum_{i in S} X^i.  If chi_S(zeta^s) = 0 in C for s = 1..w-1
(zeta a primitive n-th root of unity, 2 <= w <= n) then, with

    A = floor(log2(w-1)),  M = 2^{A+1} = least power of two >= w,  L = n/M,

chi_S is divisible by (X^n - 1)/(X^L - 1), hence S is L-periodic, hence
T = zeta^S is a union of cosets of mu_M.  Conversely every such union
satisfies the conditions.  Therefore

    W_w^struct nonempty <=> M | r',  and then |W_w^struct| = C(n/M, r'/M).

Exact oracle used throughout: chi_S(zeta^s) = 0 depends only on
a = v_2(s) (Galois), and with xi = zeta^{2^a} of order N_a = n/2^a and
xi^{N_a/2} = -1, the value is the integer vector
c_j = #{i in S : i = j mod N_a} - #{i in S : i = j + N_a/2 mod N_a},
j = 0..N_a/2-1, in the power basis.  Vanishing is c = 0.  No floats.

Checks: (Z1) cyclotomic identity, (Z2) solution space = L-periodic vectors,
(Z3) exhaustive 0/1 census, (Z4) count formula, (Z5) exact scope in n.
tiny.
"""

import itertools
import math

FAILURES = []
CHECKS = [0]


def check(name, cond, detail=""):
    CHECKS[0] += 1
    if not cond:
        FAILURES.append((name, detail))
    return cond


# ------------------------------------------------------- integer polynomials
def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return r


def pdivexact(a, b):
    a = a[:]
    db = len(b) - 1
    q = [0] * (len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i] // b[db]
        q[i - db] = c
        if c:
            for j in range(db + 1):
                a[i - db + j] -= c * b[j]
    assert all(x == 0 for x in a[:db]), "not exact"
    return q


_PHI = {}


def phi(n):
    if n in _PHI:
        return _PHI[n]
    num = [0] * (n + 1)
    num[0], num[n] = -1, 1
    for d in range(1, n):
        if n % d == 0:
            num = pdivexact(num, phi(d))
    _PHI[n] = num
    return num


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def vanishes(S, n, a):
    """exact test chi_S(zeta^{2^a}) == 0 in Z[zeta_n], n a power of two."""
    Na = n >> a
    half = Na >> 1
    c = [0] * half
    for i in S:
        j = i % Na
        if j < half:
            c[j] += 1
        else:
            c[j - half] -= 1
    return not any(c)


def sec(t):
    print("\n" + "-" * 78)
    print(t)
    print("-" * 78)


def main():
    print("=" * 78)
    print("ROUND 15 -- LEMMA Z (characteristic-zero window structure)")
    print("=" * 78)

    # ------------------------------------------------------------------ (Z1)
    sec("[Z1] cyclotomic identity  prod_{a=0}^{A} Phi_{2^{m-a}} "
        "= (X^n-1)/(X^L-1)")
    bad = []
    npairs = 0
    for m in range(2, 10):
        n = 2 ** m
        for w in range(2, n + 1):
            A = (w - 1).bit_length() - 1
            M = 2 ** (A + 1)
            if M > n:
                continue
            L = n // M
            D = sorted({n // math.gcd(n, s) for s in range(1, w)})
            prod = [1]
            for e in D:
                prod = pmul(prod, phi(e))
            num = [0] * (n + 1)
            num[0], num[n] = -1, 1
            den = [0] * (L + 1)
            den[0], den[L] = -1, 1
            npairs += 1
            if prod != pdivexact(num, den):
                bad.append((m, w, D, L))
    check("Z1 identity for all n = 2^m, all w", not bad, str(bad[:3]))
    print("  verified on %d (n, w) pairs, m = 2..9: %s"
          % (npairs, "OK" if not bad else "BROKEN"))
    print("  D(n,w) = {n/gcd(n,s)} is exactly the TOP A+1 divisors of n, so")
    print("  the whole condition set collapses to ONE divisibility by")
    print("  (X^n-1)/(X^L-1) = 1 + X^L + ... + X^{n-L}.")

    # ------------------------------------------------------------------ (Z2)
    sec("[Z2] Q-solution space = the L-periodic vectors (dimension L)")
    bad = []
    for m in range(2, 9):
        n = 2 ** m
        for A in range(0, m):
            M, L = 2 ** (A + 1), n // 2 ** (A + 1)
            g = pdivexact([-1] + [0] * (n - 1) + [1],
                          [-1] + [0] * (L - 1) + [1])
            if n - (len(g) - 1) != L:
                bad.append(("dim", m, A))
            for j0 in range(L):
                S = [j0 + t * L for t in range(M)]
                for a in range(0, A + 1):
                    if not vanishes(S, n, a):
                        bad.append(("per", m, A, j0, a))
    check("Z2 dim = L and every mu_M-coset is a solution", not bad,
          str(bad[:3]))
    print("  m = 2..8, every A: dim{chi : g | chi} = L = n/M, and the L")
    print("  coset indicators are solutions -> they are a BASIS.  Since")
    print("  deg h < L in chi = g*h, the coefficient of X^j in chi is")
    print("  h_{j mod L}: a 0/1 solution is L-PERIODIC, i.e. a union of")
    print("  mu_M-cosets.  (This is the whole proof of the hard direction.)")

    # ------------------------------------------------------------------ (Z3)
    sec("[Z3] exhaustive 0/1 census -- the falsifier hunt")
    tot = 0
    for m in (2, 3, 4):
        n = 2 ** m
        for mask in range(1 << n):
            S = [i for i in range(n) if (mask >> i) & 1]
            for A in range(0, m):
                L = n // 2 ** (A + 1)
                sol = all(vanishes(S, n, a) for a in range(A + 1))
                per = all(((mask >> i) & 1) == ((mask >> ((i + L) % n)) & 1)
                          for i in range(n))
                tot += 1
                if sol != per:
                    FAILURES.append(("Z3", (m, A, mask)))
                    break
    check("Z3 exhaustive: solution <=> L-periodic", not FAILURES, "")
    print("  n = 4, 8, 16 : %d (subset, A) pairs, ZERO misclassifications"
          % tot)

    n, bad32, tested32 = 32, 0, 0
    for A in range(0, 5):
        L = n // 2 ** (A + 1)
        for rp in (2, 4, 6):
            for comb in itertools.combinations(range(n), rp):
                sol = all(vanishes(comb, n, a) for a in range(A + 1))
                st = set(comb)
                per = all(((i in st) == (((i + L) % n) in st))
                          for i in range(n))
                tested32 += 1
                if sol != per:
                    bad32 += 1
    check("Z3b n = 32 exhaustive at r' = 2,4,6", bad32 == 0, str(bad32))
    print("  n = 32, A = 0..4, r' in {2,4,6}: %d subsets, %d misclassified"
          % (tested32, bad32))

    # ------------------------------------------------------------------ (Z4)
    sec("[Z4] the count formula |W_w^struct| = C(n/M, r'/M)")
    bad = []
    for m in (3, 4, 5):
        n = 2 ** m
        for A in range(0, m):
            M, L = 2 ** (A + 1), n // 2 ** (A + 1)
            by_size = [0] * (n + 1)
            for sub in range(1 << L):
                by_size[bin(sub).count("1") * M] += 1
            for rp in range(0, n + 1):
                pred = math.comb(L, rp // M) if rp % M == 0 else 0
                if by_size[rp] != pred:
                    bad.append((m, A, rp, by_size[rp], pred))
    check("Z4 count formula", not bad, str(bad[:3]))
    print("  |W_w^struct| = C(n/M, r'/M) verified at n = 8,16,32, all A, "
          "all r'")
    print("  crossing prize row (n=2^41, k=2^40, w=2^v): C(2^{41-v},"
          " 2^{40-v}-1)")
    for v in (34, 39):
        print("    v = %d :  C(%d, %d) = %s"
              % (v, 2 ** (41 - v), 2 ** (40 - v) - 1,
                 math.comb(2 ** (41 - v), 2 ** (40 - v) - 1)))

    # ------------------------------------------------------------------ (Z5)
    sec("[Z5] EXACT SCOPE: for which n does the periodicity conclusion hold?")
    print("  Needs D(n,w) = {n/gcd(n,s) : 1<=s<=w-1} to be COMPLEMENTARY,")
    print("  i.e. D = {e | n : e does not divide L} for some L | n.")
    print()
    print("  %-6s %-30s %-14s" % ("n", "w with NON-complementary D", "verdict"))
    for n in (4, 8, 16, 32, 9, 27, 25, 6, 12, 10, 15, 20, 24, 30, 36):
        divs = divisors(n)
        badw = []
        for w in range(2, n + 1):
            D = {n // math.gcd(n, s) for s in range(1, w)}
            if not any(D == {e for e in divs if L % e != 0} for L in divs):
                badw.append(w)
        primes = [f for f in divs if f > 1 and
                  all(f % t for t in range(2, int(f ** 0.5) + 1))]
        pp = len(primes) == 1
        print("  %-6d %-30s %-14s"
              % (n, (str(badw[:6]) + ("..." if len(badw) > 6 else ""))
                 if badw else "(none)",
                 "PRIME POWER" if pp else ("ok" if not badw else "FAILS")))
        if pp:
            check("Z5 prime power n=%d complementary for all w" % n,
                  not badw, str(badw[:3]))
        else:
            check("Z5 composite n=%d has a failing w" % n, bool(badw),
                  "no failure found")
    print()
    print("  => LEMMA Z is a PRIME-POWER theorem.  n = 2^41 is exactly the")
    print("     good case (rules freeze: 'smooth domain = coset of a")
    print("     power-of-2-order subgroup'), so the prize rows are inside")
    print("     the scope and no Lam-Leung machinery is needed.")

    print("\n" + "=" * 78)
    print("checks run: %d   failures: %d" % (CHECKS[0], len(FAILURES)))
    for nm, d in FAILURES:
        print("  FAILED: %s | %s" % (nm, d))
    print("=" * 78)


if __name__ == "__main__":
    main()
