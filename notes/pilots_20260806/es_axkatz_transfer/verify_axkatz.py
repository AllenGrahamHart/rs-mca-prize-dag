#!/usr/bin/env python3
"""Round 16 -- THE AX-KATZ / CHEVALLEY-WARNING TRANSFER ON (ES).

Pre-registered in PREREG.md (pilot section P0-P5) BEFORE any computation.

Sections:
  [K0] validate the Ax-Katz exponent formula and Warning's second theorem
       by brute force on small systems (including systems with mu >= 1).
  [K1] the two algebraizations (ALG-I indicator, ALG-L locator): verify at
       small fixtures that their F_q-point counts equal |W_w| exactly, and
       exhibit the ALG-I weight-aliasing failure when p <= n.
  [K2] the Ax-Katz exponent mu computed EXACTLY at the four rows of record,
       in both readings, with the Chevalley-Warning deficit in bits.
  [K3] the p-adic unit obstruction (P2b) and the Warning obstruction (P2c).
  [K4] insensitivity on the round-15 identical-enumerator witness (P2d),
       plus the McEliece exponent (P2e).
  [K5] toy calibration: exact |W_w| vs p-divisibility; the adversarial
       "periodic + one accident" check.
  [K6] the one LIVE shape: divisibility + a priori upper bound => vanishing.

Exact integer / finite-field arithmetic throughout; floats only for log2 of
astronomically large binomials (absolute error << 1 bit, stated inline).
Fail-closed: exits nonzero if any check fails.  ramguard local.
"""

import itertools
import math
import random
import sys

FAILURES = []
CHECKS = [0]


def check(name, cond, detail=""):
    CHECKS[0] += 1
    if not cond:
        FAILURES.append((name, detail))
    return bool(cond)


def sec(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78)


def sub(t):
    print("\n" + "-" * 78)
    print(t)
    print("-" * 78)


# ===========================================================================
# the pre-registered exponents (P0), implemented once, validated in [K0]
# ===========================================================================
def ak_mu(nvars, sum_degs, max_deg):
    """mu = ceil((N - sum d_j)/max d_j).  Ax-Katz: q^mu divides |V|.
    Taken on (N, sum d, max d) so that rows with n = 2^41 equations never
    materialise a list."""
    return -((-(nvars - sum_degs)) // max_deg)


def ax_katz_mu(nvars, degs):
    if not degs:
        return nvars
    return ak_mu(nvars, sum(degs), max(degs))


# ===========================================================================
# small finite fields
# ===========================================================================
def primitive_root(p):
    fac, m, d = set(), p - 1, 2
    while d * d <= m:
        while m % d == 0:
            fac.add(d)
            m //= d
        d += 1
    if m > 1:
        fac.add(m)
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in fac):
            return g
    raise RuntimeError("no primitive root")


def mu_group(n, p):
    """the n-th roots of unity in F_p, as [zeta^0, ..., zeta^{n-1}]."""
    assert (p - 1) % n == 0
    z = pow(primitive_root(p), (p - 1) // n, p)
    out, cur = [], 1
    for _ in range(n):
        out.append(cur)
        cur = cur * z % p
    return out


class F2Field(object):
    """F_{p^2} = F_p[t]/(t^2 - nr), minimal, for the p <= n aliasing witness."""

    def __init__(self, p):
        self.p = p
        self.nr = next(a for a in range(2, p)
                       if pow(a, (p - 1) // 2, p) == p - 1)

    def mul(self, x, y):
        p, nr = self.p, self.nr
        return ((x[0] * y[0] + nr * x[1] * y[1]) % p,
                (x[0] * y[1] + x[1] * y[0]) % p)

    def add(self, x, y):
        p = self.p
        return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

    def pw(self, x, e):
        r = (1, 0)
        while e:
            if e & 1:
                r = self.mul(r, x)
            x = self.mul(x, x)
            e >>= 1
        return r

    def order(self, x):
        o, y = 1, x
        while y != (1, 0):
            y = self.mul(y, x)
            o += 1
            if o > self.p * self.p:
                raise RuntimeError
        return o

    def elt_of_order(self, m):
        q = self.p * self.p
        assert (q - 1) % m == 0
        for a in range(1, self.p):
            for b in range(0, self.p):
                if self.order((a, b)) == q - 1:
                    return self.pw((a, b), (q - 1) // m)
        raise RuntimeError("no generator")


# ===========================================================================
# banked exact-count machinery (round-15 verify_transfercut.py:104-125),
# plus a full-weight-profile version cross-checked against it
# ===========================================================================
def zero01(n, p, elts, zeros, rp):
    """# of 0/1 weight-rp vectors x with sum_i x_i elts[i]^s = 0, s in zeros."""
    coef = [dict() for _ in range(rp + 1)]
    coef[0][0] = 1
    for i in range(n):
        syn = 0
        for t, s in enumerate(zeros):
            syn += pow(elts[i], s, p) * (p ** t)
        for r in range(min(i, rp - 1), -1, -1):
            for key, v in list(coef[r].items()):
                nk, base = 0, key
                for t in range(len(zeros)):
                    a = base % p
                    b = (syn // (p ** t)) % p
                    nk += ((a + b) % p) * (p ** t)
                    base //= p
                coef[r + 1][nk] = coef[r + 1].get(nk, 0) + v
    return coef[rp].get(0, 0)


def profile01_clean(n, p, elts, zeros):
    """one DP, all weights: profile[r] = # of 0/1 weight-r window solutions."""
    z0 = tuple([0] * len(zeros))
    coef = [dict() for _ in range(n + 1)]
    coef[0][z0] = 1
    for i in range(n):
        syn = tuple(pow(elts[i], s, p) for s in zeros)
        for r in range(min(i, n - 1), -1, -1):
            src = coef[r]
            if not src:
                continue
            dst = coef[r + 1]
            for key, v in src.items():
                nk = tuple((key[t] + syn[t]) % p for t in range(len(zeros)))
                dst[nk] = dst.get(nk, 0) + v
    return [coef[r].get(z0, 0) for r in range(n + 1)]


def brute_profile(n, p, elts, zeros):
    """brute force over the whole 0/1 cube (n <= 16), all weights at once."""
    out = [0] * (n + 1)
    pw = [[pow(elts[i], s, p) for s in zeros] for i in range(n)]
    for mask in range(1 << n):
        acc = [0] * len(zeros)
        m, i = mask, 0
        while m:
            if m & 1:
                for t in range(len(zeros)):
                    acc[t] += pw[i][t]
            m >>= 1
            i += 1
        if all(a % p == 0 for a in acc):
            out[bin(mask).count("1")] += 1
    return out


# ===========================================================================
# polynomials over F_p (for ALG-L)
# ===========================================================================
def poly_divmod(a, b, p):
    a = a[:]
    db = len(b) - 1
    inv = pow(b[db], p - 2, p)
    q = [0] * max(0, len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i] * inv % p
        q[i - db] = c
        if c:
            for j in range(db + 1):
                a[i - db + j] = (a[i - db + j] - c * b[j]) % p
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return q, a


# ===========================================================================
# [K0]  validate Ax-Katz and Warning-2 by brute force
# ===========================================================================
def k0():
    sec("[K0] VALIDATION of the Ax-Katz exponent and Warning's 2nd theorem")
    print("Ax-Katz (Katz 1971):  q^mu | |V|,  mu = ceil((N - sum d_j)/max d_j)")
    print("Warning-2:            sum d_j < N and V != {}  =>  |V| >= q^{N-sum d}")
    print()
    rng = random.Random(20260806)
    bad_ak, bad_w2, tested, nontriv = [], [], 0, 0
    plans = [(3, 5, [2]), (3, 6, [2]), (3, 4, [1, 1]), (5, 4, [1, 1]),
             (2, 6, [2, 1]), (3, 5, [2, 2]), (5, 3, [1]), (7, 3, [1]),
             (3, 4, [3]), (2, 5, [2]), (5, 4, [2]), (3, 6, [2, 2])]
    for p, N, degs in plans:
        for _trial in range(12):
            polys = []
            for d in degs:
                mons = {}
                e = [0] * N
                for _ in range(d):
                    e[rng.randrange(N)] += 1
                mons[tuple(e)] = rng.randrange(1, p)
                for _ in range(rng.randrange(0, 5)):
                    ee = [0] * N
                    for _ in range(rng.randrange(0, d + 1)):
                        ee[rng.randrange(N)] += 1
                    t = tuple(ee)
                    mons[t] = (mons.get(t, 0) + rng.randrange(0, p)) % p
                polys.append(mons)
            cnt = 0
            for pt in itertools.product(range(p), repeat=N):
                good = True
                for mons in polys:
                    acc = 0
                    for e, c in mons.items():
                        term = c
                        for i, ei in enumerate(e):
                            if ei:
                                term = term * pow(pt[i], ei, p) % p
                        acc += term
                    if acc % p:
                        good = False
                        break
                if good:
                    cnt += 1
            mu = ax_katz_mu(N, degs)
            tested += 1
            if mu >= 1:
                nontriv += 1
                if cnt % (p ** mu) != 0:
                    bad_ak.append((p, N, degs, mu, cnt))
            if sum(degs) < N and cnt > 0:
                if cnt < p ** (N - sum(degs)):
                    bad_w2.append((p, N, degs, cnt, p ** (N - sum(degs))))
    check("K0 Ax-Katz divisibility holds on every brute-forced system",
          not bad_ak, str(bad_ak[:3]))
    check("K0 Warning-2 lower bound holds on every brute-forced system",
          not bad_w2, str(bad_w2[:3]))
    check("K0 the validation set contains systems with mu >= 1",
          nontriv >= 20, "only %d" % nontriv)
    print("  %d random systems brute-forced, %d of them with mu >= 1."
          % (tested, nontriv))
    print("  Ax-Katz violations: %d.   Warning-2 violations: %d."
          % (len(bad_ak), len(bad_w2)))
    print("  => the exponent formula and the Warning bound are implemented")
    print("     correctly and are used unchanged in [K2]-[K6].")


# ===========================================================================
# [K1]  the algebraizations
# ===========================================================================
def k1():
    sec("[K1] THE ALGEBRAIZATION (A1): ALG-I indicator and ALG-L locator")

    sub("[K1a] the banked DP == the weight-profile DP == full brute force")
    bad = []
    cells = 0
    for n, p in ((8, 17), (8, 41), (16, 17), (4, 13)):
        elts = mu_group(n, p)
        for w in (2, 3):
            zeros = list(range(1, w))
            prof = profile01_clean(n, p, elts, zeros)
            bru = brute_profile(n, p, elts, zeros)
            if prof != bru:
                bad.append(("profile", n, p, w, prof, bru))
            for rp in range(1, n):
                cells += 1
                if zero01(n, p, elts, zeros, rp) != prof[rp]:
                    bad.append(("banked", n, p, w, rp))
    check("K1a banked DP == profile DP == cube brute force", not bad,
          str(bad[:3]))
    print("  (n,p) = (8,17),(8,41),(16,17),(4,13); w = 2,3; every r':")
    print("  %d cells, all three counters agree.  The round-15 syndrome DP" % cells)
    print("  is the ground truth used below.")

    sub("[K1b] ALG-L: the locator system E*F = X^n - 1 counts |W_w| EXACTLY")
    print("  variables: the r' non-leading coefficients of monic E (deg r')")
    print("  and the n-r' non-leading coefficients of monic F (deg n-r');")
    print("  equations: the n coefficient identities of E*F = X^n - 1, each")
    print("  of degree 2 (bilinear), plus the window forms (degree 1) on E.")
    print("  A monic E of degree r' extends to a solution iff E | X^n - 1,")
    print("  and then F is unique -- so the point count is the number of")
    print("  size-r' subsets of mu_n meeting the window.")
    bad, rows = [], []
    for n, p in ((8, 17), (8, 41), (4, 13)):
        elts = mu_group(n, p)
        xn1 = [p - 1] + [0] * (n - 1) + [1]
        for rp in range(1, n):
            if p ** rp > 300000:
                continue
            for w in (2, 3):
                zeros = list(range(1, w))
                cnt = 0
                for coeffs in itertools.product(range(p), repeat=rp):
                    E = list(coeffs) + [1]
                    _, r = poly_divmod(xn1, E, p)
                    if len(r) == 1 and r[0] == 0:
                        if all(E[rp - j] % p == 0 for j in range(1, w)):
                            cnt += 1
                truth = zero01(n, p, elts, zeros, rp)
                rows.append((n, p, w, rp, cnt, truth))
                if cnt != truth:
                    bad.append((n, p, w, rp, cnt, truth))
    check("K1b ALG-L point count == |W_w| at every fixture", not bad,
          str(bad[:3]))
    print()
    print("  %-4s %-4s %-3s %-4s %-14s %-14s" %
          ("n", "p", "w", "r'", "ALG-L count", "|W_w| (DP)"))
    for r in rows:
        print("  %-4d %-4d %-3d %-4d %-14d %-14d" % r)
    print("  %d fixtures, %d mismatches." % (len(rows), len(bad)))
    print("  ALG-L IS AN EXACT ALGEBRAIZATION.  (It also re-verifies Newton")
    print("  invertibility: the ELEMENTARY-symmetric prefix e_1..e_{w-1} = 0")
    print("  and the POWER-SUM prefix agree at every fixture, since p > w.)")
    print("  ALG-L has NO weight equation: deg E = r' is built into the")
    print("  variable set, so it is exact at every row, with or without p > n.")

    sub("[K1c] ALG-I: exact iff p > n -- the weight-aliasing failure")
    print("  ALG-I's weight form sum_i x_i - r' pins wt(x) only MOD p, so its")
    print("  F_q-point count is sum over j = r' (mod p) of |W_w^{(j)}|.")
    ok_pgn, cells = [], 0
    for n, p in ((8, 17), (16, 17), (16, 97), (4, 13)):
        elts = mu_group(n, p)
        for w in (2, 3):
            prof = profile01_clean(n, p, elts, list(range(1, w)))
            for rp in range(0, n + 1):
                alias = sum(prof[j] for j in range(n + 1) if (j - rp) % p == 0)
                ok_pgn.append(alias == prof[rp])
                cells += 1
    check("K1c ALG-I exact whenever p > n", all(ok_pgn), "")
    print("  p > n is FORCED when delta = 1 (n | p-1 => p >= n+1): no")
    print("  aliasing, verified in %d cells." % cells)
    F = F2Field(7)
    zeta = F.elt_of_order(8)
    check("K1c zeta has order 8 in F_49", F.order(zeta) == 8, str(zeta))
    byw = [0] * 9
    for mask in range(1 << 8):
        acc = (0, 0)
        for i in range(8):
            if (mask >> i) & 1:
                acc = F.add(acc, F.pw(zeta, i))
        if acc == (0, 0):
            byw[bin(mask).count("1")] += 1
    print("  witness n = 8, p = 7 (delta = ord_8(7) = 2, so p < n), w = 2:")
    print("  weight profile of {x in {0,1}^8 : sum x_i zeta^i = 0 in F_49}")
    print("    = %s" % byw)
    found = None
    for rp in range(9):
        alias = sum(byw[j] for j in range(9) if (j - rp) % 7 == 0)
        if alias != byw[rp]:
            found = (rp, byw[rp], alias)
            break
    check("K1c ALG-I OVERCOUNTS when p <= n", found is not None, str(byw))
    if found:
        print("  r' = %d: |W_w| = %d but the ALG-I system has %d F_q-points."
              % found)
    print("  CATCH: at the prize rows delta in {2,4} admits p < n = 2^41")
    print("  (p ~ 2^40 for delta = 2), so ALG-I is NOT an exact algebraization")
    print("  there; ALG-L is.  Row numbers below are reported for BOTH, with")
    print("  ALG-L load-bearing.")


# ===========================================================================
# [K2]  the exponent at the four rows of record
# ===========================================================================
N_LEN = 2 ** 41
LOG2Q_LO = 255.900  # log2 q in (255.900, 256), banked razor row


def row_table():
    """(label, n, nforms, r', M, wpar); nforms = # of F_q-linear window forms."""
    rows, n = [], N_LEN
    for v in range(34, 40):
        w = 2 ** v
        rows.append(("crossing w=2^%d" % v, n, w - 1, 2 ** 40 - w, w, w))
    for lbl, k, dlo, dhi in (("band 1/4", 2 ** 39, 2 ** 32 + 1, 2 ** 33 - 1),
                             ("band 1/8", 2 ** 38, 2 ** 32 + 1, 2 ** 33 - 1),
                             ("band 1/16", 2 ** 37, 2 ** 31 + 1, 2 ** 32 - 1)):
        for d in (dlo, dhi):
            M = 1 << (d - 1).bit_length()   # least power of two >= d
            rows.append(("%s d=%d" % (lbl, d), n, 2 * d, n - k - d, M, d))
    return rows


def k2():
    sec("[K2] THE AX-KATZ EXPONENT mu, EXACT, AT THE FOUR ROWS OF RECORD")
    print("formula (pre-registered, P0): mu = ceil((N - sum_j d_j)/max_j d_j),")
    print("and q^mu | |V|.  Chevalley-Warning bites iff sum_j d_j < N.")
    print()
    print("ALG-I extension (over F_q):  N = n; degrees = n copies of 2 (the")
    print("   0/1 quadrics) + nforms copies of 1 (window) + 1 (weight).")
    print("ALG-I base-field (over F_p): same with nforms -> |Z_w|,")
    print("   |Z_w| in [w-1, delta(w-1)].")
    print("ALG-L extension (over F_q):  N = n; degrees = n copies of 2 +")
    print("   nforms copies of 1.")
    print("ALG-L prefix (over F_q):  for a PREFIX window the nforms forced-")
    print("   zero coefficients are eliminated outright: N = n - nforms and")
    print("   NO linear equations -- the best reading available anywhere.")
    print()
    print("%-24s %-17s %-17s %-17s" %
          ("row", "mu (ALG-I ext)", "mu (ALG-L ext)", "mu (ALG-L pfx)"))
    print("-" * 78)
    recs = []
    for lbl, n, nf, rp, M, wp in row_table():
        mu_I = ak_mu(n, 2 * n + nf + 1, 2)
        mu_L = ak_mu(n, 2 * n + nf, 2)
        mu_P = ak_mu(n - nf, 2 * n, 2)
        recs.append((lbl, n, nf, rp, M, wp, mu_I, mu_L, mu_P))
        print("%-24s %-17d %-17d %-17d" % (lbl, mu_I, mu_L, mu_P))
    print()
    print("EVERY exponent is negative.  Closed forms:")
    print("  ALG-I ext:  mu = -floor((n + nforms + 1)/2)")
    print("  ALG-L ext:  mu = -floor((n + nforms)/2)")
    print("  ALG-L pfx:  mu = -floor((n + nforms)/2)   [N = n - nforms]")
    bad = []
    for lbl, n, nf, rp, M, wp, mI, mL, mP in recs:
        if mI != -((n + nf + 1) // 2):
            bad.append(("I", lbl, mI))
        if mL != -((n + nf) // 2):
            bad.append(("L", lbl, mL))
        if mP != -((n + nf) // 2):
            bad.append(("P", lbl, mP))
    check("K2 closed forms match the computed exponents", not bad,
          str(bad[:3]))
    check("K2 mu < 0 at every row in every reading",
          all(m < 0 for r in recs for m in r[6:9]), "")
    check("K2 the crossing exponent is exactly -(n+w)/2 in ALG-I ext",
          all(r[6] == -(r[1] + r[5]) // 2 for r in recs
              if r[0].startswith("crossing")), "")

    sub("[K2b] the Chevalley-Warning deficit, exactly and in bits")
    print("  CW needs sum_j d_j < N.  DEFICIT := sum d_j - N + 1 = the total")
    print("  degree that must be REMOVED for CW to bite at all.")
    print("  GAP1 := sum d_j - N + max d_j = removal needed for mu >= 1.")
    print("  (Both quoted for the BEST reading, ALG-L prefix.)")
    print()
    print("  %-24s %-22s %-10s %-22s" %
          ("row", "CW deficit", "log2", "GAP1 (mu >= 1)"))
    for lbl, n, nf, rp, M, wp, mI, mL, mP in recs:
        Sd, Nv = 2 * n, n - nf
        print("  %-24s %-22d %-10.5f %-22d"
              % (lbl, Sd - Nv + 1, math.log2(Sd - Nv + 1), Sd - Nv + 2))
    print()
    print("  Every row is short by 2^41.0 -- 2^41.3 degree-units: the system")
    print("  is over-determined by a factor sum d / N > 2 where Ax-Katz needs")
    print("  < 1.  Compare the round-15 Weil/C-U vacuity at the same rows,")
    print("  13.5 - 107 bits.  AX-KATZ IS VACUOUS BY ~41 BITS OF DEFICIT --")
    print("  and the deficit is MULTIPLICATIVE in the wrong direction, not a")
    print("  near miss.")

    sub("[K2c] base-field reading: the |Z_w| dependence")
    print("  |Z_w| in [w-1, delta(w-1)], delta in {1,2,4}.  The base-field")
    print("  exponent mu_p = -floor((n + |Z_w| + 1)/2) DOES depend on the")
    print("  defining set -- but only through |Z_w|, and MONOTONICALLY")
    print("  DOWNWARD: a larger p-cyclotomic closure makes it strictly WORSE.")
    print()
    print("  %-24s %-24s %-24s" % ("row", "mu_p at |Z| = w-1",
                                   "mu_p at |Z| = 4(w-1)"))
    for lbl, n, nf, rp, M, wp, mI, mL, mP in recs[:6]:
        print("  %-24s %-24d %-24d"
              % (lbl, -((n + nf + 1) // 2), -((n + 4 * nf + 1) // 2)))
    print("  Both ends negative: the whole interval is vacuous, and the only")
    print("  defining-set sensitivity that exists points the wrong way.")
    return recs


# ===========================================================================
# [K3]  the p-adic unit obstruction and the Warning obstruction
# ===========================================================================
def factor_below(x, bound):
    """divide out all primes <= bound; return (largest such prime, residue)."""
    largest, res = 1, x
    d = 2
    while d <= bound:
        if res % d == 0:
            while res % d == 0:
                res //= d
            largest = d
        d += 1
    return largest, res


def k3(recs):
    sec("[K3] THE TWO STRUCTURAL OBSTRUCTIONS (P2b, P2c)")

    sub("[K3a] the (ES) target at each row -- LEMMA Z's |W^struct|")
    print("  LEMMA Z (round-15, banked): W^struct is nonempty iff M | r', and")
    print("  then |W^struct| = C(n/M, r'/M), M = least power of two >= w.")
    print()
    print("  %-24s %-9s %-9s %-28s" % ("row", "L = n/M", "M | r' ?",
                                       "|W^struct| = C(L, r'/M)"))
    crossing_vals, band_zero = [], []
    for lbl, n, nf, rp, M, wp, mI, mL, mP in recs:
        L = n // M
        val = math.comb(L, rp // M) if rp % M == 0 else 0
        print("  %-24s %-9d %-9s %-28s"
              % (lbl, L, "yes" if val else "NO",
                 val if val else "0  (FAMILY EMPTY)"))
        (crossing_vals if lbl.startswith("crossing") else band_zero).append(
            (lbl, L, val))
    check("K3a every crossing row has a NONZERO structural count",
          all(v > 0 for _, _, v in crossing_vals), str(crossing_vals))
    check("K3a every band row has an EMPTY structural family",
          all(v == 0 for _, _, v in band_zero), str(band_zero))
    print()
    print("  CONSEQUENCE: the CROSSING target is a positive integer; the")
    print("  three BAND targets are genuine VANISHING statements.  The two")
    print("  obstructions below apply to the crossing rows; the band rows go")
    print("  to [K6].")

    sub("[K3b] P2b -- the p-adic UNIT obstruction at the crossing rows")
    print("  Every prime factor of C(L, j) is <= L (a prime > L divides no")
    print("  factor of L!).  Here L = n/M <= 2^7 = 128, while p >= 2^39 + 1.")
    print()
    print("  %-24s %-40s %-9s %-10s" %
          ("row", "|W^struct|", "max prime", "log2"))
    bad = []
    for lbl, L, val in crossing_vals:
        lp, res = factor_below(val, L)
        print("  %-24s %-40d %-9d %-10.4f" % (lbl, val, lp, math.log2(val)))
        if res != 1 or lp > L:
            bad.append((lbl, lp, res, L))
    check("K3b every crossing target factors completely over primes <= L",
          not bad, str(bad[:3]))
    check("K3b every crossing target is coprime to every admissible p "
          "(p >= 2^39+1 > 128 >= L)",
          all(factor_below(v, L)[0] < 2 ** 39 + 1
              for _, L, v in crossing_vals), "")
    print()
    print("  => p does NOT divide the (ES) target, at ANY crossing row, for")
    print("     ANY admissible p, with no case split on delta.  Therefore a")
    print("     true statement 'p | |W_w|' is LOGICALLY EQUIVALENT to")
    print("     '|W_w| != |W^struct|', i.e. to the EXISTENCE of accidents.")
    print("     p-divisibility here is an ACCIDENT-EXISTENCE theorem.  It can")
    print("     only REFUTE (ES); it can never prove it.")

    sub("[K3c] P2c -- the WARNING obstruction (kills ALL exact encodings)")
    print("  Warning-2 (validated in [K0]): sum d < N and V != {} =>")
    print("  |V| >= q^{N - sum d}.  Hence for ANY polynomial system over F_q")
    print("  whose F_q-point count equals |W_w| EXACTLY: if 0 < |W_w| < q")
    print("  then N - sum d <= 0, so mu = ceil((N - sum d)/max d) <= 0.")
    print()
    mx = max(v for _, _, v in crossing_vals)
    print("  max over crossing rows of |W^struct| = C(128,63)")
    print("    = %d" % mx)
    print("    log2 = %.4f   vs   log2 q > %.3f" % (math.log2(mx), LOG2Q_LO))
    check("K3c the largest crossing target is < q",
          math.log2(mx) < LOG2Q_LO, "%.4f" % math.log2(mx))
    print()
    print("  => UNDER (ES), NO EXACT ALGEBRAIZATION OF THE CROSSING COUNT --")
    print("     not ALG-I, not ALG-L, not any system anyone will ever write")
    print("     down -- CAN HAVE A POSITIVE AX-KATZ EXPONENT.  The vacuity is")
    print("     not an artefact of our encoding; it is FORCED.")
    print()
    print("  NAMED ESCAPE HATCH (registered, and closed here): a FIBERED")
    print("  encoding with point count c*|W_w|.  Then q^mu | c*|W_w| is")
    print("  consistent -- but by [K3b] gcd(|W_w|, p) = 1 under (ES), so")
    print("  q^mu | c.  ALL the divisibility sits in the fibre, where it says")
    print("  nothing about |W_w|.  The hatch is information-free.")

    sub("[K3d] the same obstruction run against the SHARPEST refinements")
    print("  Moreno-Moreno replaces each d_j by its p-weight degree (sum of")
    print("  p-adic digit sums of the exponents).  Every degree in play is 1")
    print("  or 2 and p >= 2^39 + 1, so every p-adic digit sum equals the")
    print("  degree itself: MM gives EXACTLY the same mu.")
    bad = []
    for d in (1, 2):
        for p in (2 ** 39 + 1, 2 ** 61 - 1, 2 ** 127 - 1):
            digits, x = 0, d
            while x:
                digits += x % p
                x //= p
            if digits != d:
                bad.append((d, p, digits))
    check("K3d p-weight degree == degree for every degree in play",
          not bad, str(bad[:3]))
    print("  Adolphson-Sperber and Wan sharpen the EXPONENT via the Newton")
    print("  polyhedron, but their conclusion has the same SHAPE, 'p^mu |")
    print("  count'.  By [K3b] the target is a p-adic UNIT, so no sharpening")
    print("  of mu can rescue the family.  The whole p-divisibility toolkit")
    print("  -- Chevalley-Warning, Ax, Katz, Ax-Katz, Moreno-Moreno,")
    print("  Adolphson-Sperber, Wan, McEliece -- is cut in ONE stroke.")
    return crossing_vals


# ===========================================================================
# [K4]  insensitivity on the round-15 witness + McEliece
# ===========================================================================
def cyclotomic_closure(S, n, p):
    Z = set()
    for s in S:
        t = s % n
        while t not in Z:
            Z.add(t)
            t = t * p % n
    return Z


def k4():
    sec("[K4] P2d/P2e -- INSENSITIVITY ON THE ROUND-15 SEPARATING WITNESS")
    n, p, w = 16, 17, 3
    elts = mu_group(n, p)
    print("  round-15 route cut: same (n, k, p) = (%d, %d, %d), hence"
          % (n, n - w + 1, p))
    print("  IDENTICAL MDS weight enumerator / MacWilliams dual / Krawtchouk-")
    print("  Delsarte data, but DIFFERENT 0/1 counts.  Does Ax-Katz see it?")
    print("  r' = 7 is the pair the round-15 audit cites (32 vs 0); r' = 8 is")
    print("  verify_transfercut.py's [T4] row, replayed here (54/98/22/276).")
    print()
    print("  %-4s %-14s %-9s %-6s %-16s %-16s %-8s"
          % ("r'", "defining set", "|W_w|", "|Z|", "mu (ALG-I ext)",
             "mu (ALG-L pfx)", "McE ell"))
    counts, mus_I, mus_L, zs, ells, nonzero = [], [], [], [], [], []
    for rp in (7, 8):
        for a in range(1, 8):
            zeros = list(range(a, a + w - 1))
            c = zero01(n, p, elts, zeros, rp)
            Z = cyclotomic_closure(zeros, n, p)
            muI = ak_mu(n, 2 * n + (w - 1) + 1, 2)
            muL = ak_mu(n - (w - 1), 2 * n, 2)
            ell = 1 if 0 not in Z else 0
            counts.append(c)
            mus_I.append(muI)
            mus_L.append(muL)
            zs.append(len(Z))
            ells.append(ell)
            if c:
                nonzero.append(c)
            print("  %-4d %-14s %-9d %-6d %-16d %-16d %-8d"
                  % (rp, str(zeros), c, len(Z), muI, muL, ell))
    check("K4 the 0/1 counts SEPARATE across the shifts",
          len(set(counts)) > 1, str(counts))
    check("K4 the Ax-Katz exponent is IDENTICAL across the shifts (ALG-I)",
          len(set(mus_I)) == 1, str(mus_I))
    check("K4 the Ax-Katz exponent is IDENTICAL across the shifts (ALG-L)",
          len(set(mus_L)) == 1, str(mus_L))
    check("K4 even |Z_w| is identical across the shifts (delta = "
          "ord_16(17) = 1)", len(set(zs)) == 1, str(zs))
    check("K4 McEliece exponent ell-1 = 0 for every shift",
          all(e == 1 for e in ells), str(ells))
    check("K4 EVERY NONZERO count on the separating family is COPRIME to p "
          "(direct refutation of any nontrivial p-divisibility)",
          all(c % p != 0 for c in nonzero), str(nonzero))
    check("K4 the r'=8 row replays the banked verify_transfercut.py [T4]",
          counts[7:] == [54, 54, 98, 98, 22, 54, 276], str(counts[7:]))
    check("K4 the r'=7 row reproduces the banked audit witness (32 vs 0)",
          {32, 0} <= set(counts[:7]) and counts[:4] == [32, 32, 0, 0],
          str(counts[:7]))
    print()
    print("  counts   %s   <- SEPARATE" % sorted(set(counts)))
    print("  mu       %s   <- CONSTANT" % sorted(set(mus_I)))
    print("  |Z|      %s   <- CONSTANT" % sorted(set(zs)))
    print("  every NONZERO count %s is coprime to p = 17."
          % sorted(set(nonzero)))
    print("  VERDICT COMPONENT (iii): the Ax-Katz exponent is a function of")
    print("  (n, #forms, degrees) ONLY.  It is CONSTANT on precisely the")
    print("  family that separates the terminal.  The hoped-for 'p-divisi-")
    print("  bility is sensitive to defining sets' is NOT realised here.")

    sub("[K4b] McEliece at the four rows of record")
    print("  McEliece: p^{ell-1} divides every weight, ell = least number of")
    print("  NONZEROS (repetitions allowed) whose product is 1.")
    print("  Our defining set is Z_w = the p-closure of {1,...,w-1}.  0 is")
    print("  never in it (0*p^j = 0, and 0 is not in {1,...,w-1}), so")
    print("  zeta^0 = 1 IS a nonzero of the code, ell = 1, and McEliece gives")
    print("  p^0 = 1.")
    bad = []
    for n_, p_, w_ in ((16, 17, 3), (16, 17, 5), (8, 17, 2), (32, 97, 4),
                       (16, 97, 3), (64, 193, 6)):
        if 0 in cyclotomic_closure(range(1, w_), n_, p_):
            bad.append((n_, p_, w_))
    check("K4b 0 is never in the cyclotomic closure of {1,...,w-1}",
          not bad, str(bad[:3]))
    print("  verified on 6 fixtures; the argument is uniform in (n, p, w) and")
    print("  applies verbatim at n = 2^41.  McEliece: VACUOUS AT EVERY ROW,")
    print("  and vacuous for every SHIFTED defining set too (any a >= 1 keeps")
    print("  0 out of the closure).  The ONE classical p-divisibility theorem")
    print("  that IS defining-set-sensitive is sensitive through a quantity")
    print("  (ell) pinned at its trivial value on this whole family.")
    return counts


# ===========================================================================
# [K5]  toy calibration + the adversarial check
# ===========================================================================
def k5():
    sec("[K5] CALIBRATION (A4) + THE ADVERSARIAL CHECK (PREREG 3, clause 2)")
    print("  For each fixture: the exact |W_w| (banked machinery), the")
    print("  Ax-Katz prediction, and whether p ACTUALLY divides the count.")
    print()
    print("  %-5s %-6s %-4s %-4s %-13s %-9s %-11s %-11s"
          % ("n", "p", "w", "r'", "|W_w|", "mu", "q^mu | ?", "p | |W_w| ?"))
    ndiv, ntot, nz_div, nz_tot, bad = 0, 0, 0, 0, []
    for n, p in ((8, 17), (8, 41), (16, 17), (16, 97), (4, 13), (16, 113)):
        elts = mu_group(n, p)
        for w in (2, 3):
            prof = profile01_clean(n, p, elts, list(range(1, w)))
            for rp in sorted({n // 2, n // 2 - 1, n // 4}):
                if rp < 1:
                    continue
                c = prof[rp]
                mu = ak_mu(n - (w - 1), 2 * n, 2)
                pred_ok = (mu <= 0) or (c % (p ** mu) == 0)
                pdiv = (c % p == 0)
                ntot += 1
                ndiv += 1 if pdiv else 0
                if c:
                    nz_tot += 1
                    nz_div += 1 if pdiv else 0
                if not pred_ok:
                    bad.append((n, p, w, rp, c, mu))
                print("  %-5d %-6d %-4d %-4d %-13d %-9d %-11s %-11s"
                      % (n, p, w, rp, c, mu,
                         "TRIVIAL" if mu <= 0 else "ok",
                         "YES" if pdiv else ("no" if c else "YES (c=0)")))
    check("K5 the Ax-Katz prediction is never violated at a fixture",
          not bad, str(bad[:3]))
    print()
    print("  %d of %d fixtures have p | |W_w| -- but %d of those %d are the"
          % (ndiv, ntot, ndiv - nz_div, ndiv))
    print("  TRIVIAL case |W_w| = 0.  Among the %d fixtures with a NONZERO"
          % nz_tot)
    print("  count, p divides it in %d." % nz_div)
    check("K5 p fails to divide |W_w| at a clear majority of fixtures (P5a)",
          ndiv * 2 < ntot, "%d/%d" % (ndiv, ntot))
    check("K5 p divides NO nonzero |W_w| in the whole fixture sweep "
          "(sharpened P5a)", nz_div == 0, "%d/%d" % (nz_div, nz_tot))
    print("  The Ax-Katz prediction is TRUE at every fixture -- because at")
    print("  every fixture mu <= 0, and 'q^0 divides N' is true of EVERY")
    print("  integer.  It is true and EMPTY.  Meanwhile p divides NO nonzero")
    print("  count anywhere in the sweep: there is no p-divisibility here to")
    print("  be found, at any row, vacuous exponent or not.")

    sub("[K5b] the adversarial check required by PREREG section 3 clause 2")
    n, p, w, rp = 16, 17, 3, 8
    elts = mu_group(n, p)
    true_c = zero01(n, p, elts, [1, 2], rp)
    M = 4
    struct = math.comb(n // M, rp // M) if rp % M == 0 else 0
    mu = ak_mu(n - (w - 1), 2 * n, 2)
    print("  n=16, p=17, w=3, r'=8:  |W_w| = %d, |W^struct| = C(4,2) = %d,"
          % (true_c, struct))
    print("  so |W^acc| = %d accidental members.  Ax-Katz mu = %d."
          % (true_c - struct, mu))
    trip = []
    for label, val in (("|W^struct|", struct),
                       ("|W^struct| + 1 accident", struct + 1),
                       ("the TRUE count", true_c)):
        sat = True if mu <= 0 else (val % (p ** mu) == 0)
        trip.append(sat)
        print("    divisibility satisfied by %-26s : %s" % (label, sat))
    check("K5b the divisibility statement CANNOT separate periodic from "
          "periodic+accident => verdict component (iii)",
          len(set(trip)) == 1, str(trip))
    print("  All three satisfy it identically.  By the pre-registered rule")
    print("  (PREREG 3, clause 2) this alone forces verdict (iii) over (i).")
    print()
    print("  Honest scope split: this toy sits far BELOW balance")
    print("  (C(16,8)/p^{|Z|} = %.1f), so accidents abound here, unlike the"
          % (math.comb(16, 8) / 17.0 ** 2))
    print("  prize rows.  The toy kills the ROW-LEVEL divisibility claim, not")
    print("  the method; the METHOD is killed by [K3b]/[K3c].")


# ===========================================================================
# [K6]  the one LIVE shape: divisibility + upper bound => vanishing
# ===========================================================================
def log2_binom(n, k):
    if k < 0 or k > n:
        return float("-inf")
    return (math.lgamma(n + 1) - math.lgamma(k + 1)
            - math.lgamma(n - k + 1)) / math.log(2.0)


def k6(recs):
    sec("[K6] THE ONE LIVE SHAPE (P3): divisibility + upper bound => 0")
    print("  If q^mu | |W| with mu >= 1 AND independently |W| < q^mu, then")
    print("  |W| = 0.  This is the ONLY shape in which a p-divisibility")
    print("  theorem can PROVE a suppression statement, and it is the")
    print("  relevant one at the three BAND rows, where [K3a] showed the")
    print("  structural family is EMPTY -- i.e. the target IS a vanishing.")
    print()
    print("  Ingredient 1: mu >= 1.  Ingredient 2: an UNCONDITIONAL upper")
    print("  bound U on |W| with U < q^mu.  The only unconditional bound is")
    print("  U = C(n, r').  Needed exponent: mu > log2(U)/log2(q).")
    print()
    print("  %-24s %-18s %-16s %-18s"
          % ("row", "log2 C(n,r')", "mu needed", "mu available"))
    bad = []
    for lbl, n, nf, rp, M, wp, mI, mL, mP in recs:
        lu = log2_binom(n, rp)
        need = math.ceil(lu / LOG2Q_LO)
        print("  %-24s %-18.7g %-16d %-18d" % (lbl, lu, need, mP))
        if mP >= need:
            bad.append((lbl, mP, need))
    check("K6 the available exponent never reaches the needed exponent",
          not bad, str(bad[:3]))
    print()
    print("  (log2 C(n,r') via lgamma; absolute error << 1 bit on a 2.2e12-bit")
    print("   quantity, immaterial.)")
    print()
    print("  BOTH ingredients fail, by enormous margins:")
    print("   - ingredient 1 fails by ~2^41 degree-units ([K2b]);")
    print("   - ingredient 2 needs mu ~ 8.6e9 while mu available is ~ -1.1e12.")
    print()
    print("  WORTH BANKING: with ONLY mu >= 1 plus the band's OWN budget")
    print("  0.68 n^2 = 2^81.442 as an a priori bound, the route WOULD close,")
    print("  because 2^81.442 < q^1 (q > 2^255.900).  So the entire gap is in")
    print("  INGREDIENT 1.  The band rows are the only place in the terminal")
    print("  where a p-divisibility theorem could ever have been decisive,")
    print("  and there it needs only mu >= 1 -- short by 2^41.")
    check("K6 the band budget would fit under q^1", 81.442 < LOG2Q_LO, "")


def main():
    print("=" * 78)
    print("ROUND 16 -- THE AX-KATZ / CHEVALLEY-WARNING TRANSFER ON (ES)")
    print("=" * 78)
    k0()
    k1()
    recs = k2()
    k3(recs)
    k4()
    k5()
    k6(recs)
    print("\n" + "=" * 78)
    print("checks run: %d   failures: %d" % (CHECKS[0], len(FAILURES)))
    for nm, d in FAILURES:
        print("  FAILED: %s | %s" % (nm, d))
    print("=" * 78)
    sys.exit(1 if FAILURES else 0)


if __name__ == "__main__":
    main()
