#!/usr/bin/env python3
"""F2 opening pilot (round 14, mystery 2): the K1 MASS obligations (O1)-(O3).

Verifies the pre-registered predictions P1-P10 of PREREG.json.  Everything is
exact: pure python integers and exact Z[zeta_p] arithmetic (vector of p ints
modulo sum_i zeta^i = 0).  Floats appear only in printed diagnostics.

Self-contained: the window model is re-implemented from scratch; nothing is
imported from, or written to, any other directory.

--------------------------------------------------------------------- MODEL --
p odd, e = v_2(p-1) >= 2.  F_{p^2} = F_p(w), w^2 = N (least non-residue),
Tr(a + bw) = 2a.  G = mu_{n_ord} <= F_{p^2}^*.  A window W <= G is any subset
closed under x -> -x;  m := |W|/2 antipodal pairs with reps y_1..y_m.

A frequency is f(x) = sum_{l in Lambda} C_l x^l with C_l in F_{p^2}; the
character is chi_c(x) = Tr(f(x)) in F_p; psi(s) = zeta_p^s.  The census term is

    T_W(c) = prod_{x in W} (1 + psi(chi_c(x)))          (= 'exp S_c')

and its b-resolved refinement is  V_b(c) = [z^b] prod_{x in W} (1 + z psi(...)).

CLASS K1 (the parity-pure class of f2_deployed_windows/REPORT.md:41 -- NOT the
k=1 of critical/nodes/f2_k1_contraction_theorem): Lambda consists of ODD
exponents only, so f(-x) = -f(x), chi_c(-x) = -chi_c(x), and pairing x with -x

    (1 + zeta^s)(1 + zeta^{-s}) = 2 + zeta^s + zeta^{-s} = |1 + zeta^s|^2 >= 0

so T_W(c) = prod_{i=1..m} (2 + zeta^{s_i} + zeta^{-s_i}) with s_i = chi_c(y_i).
(Total positivity is already proved upstream: f2_fixed_sector/REPORT.md:19.)

------------------------------------------------------------------ THE POINT --
s = (s_i)_i is an F_p-LINEAR image of c, so it ranges over a subspace
L <= F_p^m.  Expanding the product ternary-wise and using orthogonality:

    E_{c in K1(Lambda)} [ T_W(c) ]  =  sum_{eps in L^perp cap {-1,0,1}^m}
                                            2^{m - wt(eps)}                (P1)

and eps in L^perp cap {-1,0,1}^m is exactly a VANISHING POWER SUM condition
sum_i eps_i y_i^l = 0 (l in Lambda), i.e. a subset of W with one element per
antipodal pair whose l-th power sums all vanish.
"""
from __future__ import annotations

import json
import os
import sys

sys.dont_write_bytecode = True

_HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(_HERE, "results")

FAILURES: list[str] = []
LOG: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    tag = "PASS" if ok else "FAIL"
    line = f"[{tag}] {name}" + (f"  --  {detail}" if detail else "")
    print(line)
    LOG.append(line)
    if not ok:
        FAILURES.append(name)
    return ok


def note(msg: str) -> None:
    print(msg)
    LOG.append(msg)


# ------------------------------------------------------------------ arith ----


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % q == 0:
            return m == q
    d, r = m - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


def official_shaped_prime(e: int) -> int:
    """Smallest prime p with v_2(p-1) == e exactly."""
    k = 1
    while True:
        p = (1 << e) * k + 1
        if is_prime(p) and v2(p - 1) == e:
            return p
        k += 2


class Fp2:
    """F_{p^2} = F_p(w), w^2 = N (least non-residue).  Elements are (a, b)."""

    __slots__ = ("p", "N")

    def __init__(self, p: int):
        self.p = p
        n = 2
        while pow(n, (p - 1) // 2, p) != p - 1:
            n += 1
        self.N = n

    def mul(self, u, v):
        p, N = self.p, self.N
        a, b = u
        c, d = v
        return ((a * c + N * b * d) % p, (a * d + b * c) % p)

    def add(self, u, v):
        p = self.p
        return ((u[0] + v[0]) % p, (u[1] + v[1]) % p)

    def smul(self, k: int, u):
        p = self.p
        return ((k * u[0]) % p, (k * u[1]) % p)

    def pw(self, u, k: int):
        r = (1, 0)
        b = u
        while k:
            if k & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            k >>= 1
        return r

    def trace(self, u) -> int:
        return (2 * u[0]) % self.p

    def neg(self, u):
        return ((-u[0]) % self.p, (-u[1]) % self.p)

    def order(self, u) -> int:
        n = self.p * self.p - 1
        o = n
        m = n
        d = 2
        fac = {}
        while d * d <= m:
            while m % d == 0:
                fac[d] = fac.get(d, 0) + 1
                m //= d
            d += 1
        if m > 1:
            fac[m] = fac.get(m, 0) + 1
        for q in fac:
            while o % q == 0 and self.pw(u, o // q) == (1, 0):
                o //= q
        return o

    def subgroup(self, n: int):
        """mu_n as [g^0, g^1, ...] for a generator g of mu_n."""
        assert (self.p * self.p - 1) % n == 0
        cand = (2, 1)
        while True:
            h = self.pw(cand, (self.p * self.p - 1) // n)
            if self.order(h) == n:
                break
            cand = (cand[0] + 1, cand[1] + 1)
            cand = (cand[0] % self.p, cand[1] % self.p)
        out, cur = [], (1, 0)
        for _ in range(n):
            out.append(cur)
            cur = self.mul(cur, h)
        return out


def pair_reps(F: Fp2, elems):
    """One representative per antipodal pair {y, -y}."""
    reps, seen = [], set()
    for y in elems:
        if y in seen:
            continue
        reps.append(y)
        seen.add(y)
        seen.add(F.neg(y))
    assert 2 * len(reps) == len(elems), (len(reps), len(elems))
    return reps


# ---------------------------------------------------------------- Z[zeta_p] --
# vector of p ints modulo sum_{i<p} zeta^i = 0;  canonical form: a_{p-1} = 0.


def canon(u):
    t = u[-1]
    if t:
        return [x - t for x in u]
    return list(u)


def cyc_one(p):
    v = [0] * p
    v[0] = 1
    return v


def cyc_shift(u, s):
    p = len(u)
    s %= p
    if s == 0:
        return list(u)
    return canon(u[-s:] + u[:-s])


def cyc_add(u, v):
    return canon([a + b for a, b in zip(u, v)])


def cyc_mul_pairfactor(u, s):
    """u * (2 + zeta^s + zeta^{-s}) -- O(p), exact."""
    a = cyc_shift(u, s)
    b = cyc_shift(u, -s)
    return canon([2 * x + y + z for x, y, z in zip(u, a, b)])


def cyc_mul_cos(u, s):
    """u * (zeta^s + zeta^{-s}) -- O(p), exact."""
    a = cyc_shift(u, s)
    b = cyc_shift(u, -s)
    return canon([y + z for y, z in zip(a, b)])


def cyc_as_int(u):
    """(is_rational_integer, value)."""
    c = canon(list(u))
    return (all(x == 0 for x in c[1:]), c[0])


# ------------------------------------------------------- window / frequency --


def window_full(F: Fp2, n_ord: int):
    """W = mu_{n_ord} (the whole rung group)."""
    return F.subgroup(n_ord)


def window_moving(F: Fp2, n_ord: int):
    """W = the genuine elements (order exactly n_ord) -- the deployed window."""
    mu = F.subgroup(n_ord)
    return [x for x in mu if F.order(x) == n_ord]


def chi_at(F: Fp2, coeffs: dict, y, n_ord: int) -> int:
    """chi_c(y) = Tr(sum_l C_l y^l) in F_p."""
    acc = (0, 0)
    for l, cl in coeffs.items():
        acc = F.add(acc, F.mul(cl, F.pw(y, l % n_ord)))
    return F.trace(acc)


def enumerate_K1(F: Fp2, Lambda):
    """All frequencies of K1(Lambda): C_l in F_{p^2} for each l in Lambda.

    Yields dicts.  Size p^{2|Lambda|} -- callers keep |Lambda| tiny.
    """
    p = F.p
    ls = sorted(Lambda)
    idx = [0] * len(ls)
    total = (p * p) ** len(ls)
    for t in range(total):
        u = t
        for j in range(len(ls)):
            idx[j] = u % (p * p)
            u //= (p * p)
        yield {l: (idx[j] % p, idx[j] // p) for j, l in enumerate(ls)}


# ------------------------------------------------- the two exact evaluators --


def mass_direct(F: Fp2, W, Lambda, n_ord: int):
    """sum over ALL c in K1(Lambda) of T_W(c), EXACT in Z[zeta_p].

    Returns (total_as_cyclotomic, class_size).  O(p^{2|Lambda|} * m * p).
    """
    p = F.p
    reps = pair_reps(F, W)
    total = [0] * p
    size = 0
    for coeffs in enumerate_K1(F, Lambda):
        acc = cyc_one(p)
        for y in reps:
            s = chi_at(F, coeffs, y, n_ord)
            acc = cyc_mul_pairfactor(acc, s)
        total = cyc_add(total, acc)
        size += 1
    return total, size


def _syndrome_states(F: Fp2, reps, Lambda, n_ord: int):
    """Per pair i, the tuple (y_i^l)_{l in Lambda} in (F_{p^2})^{|Lambda|}."""
    ls = sorted(Lambda)
    return [tuple(F.pw(y, l % n_ord) for l in ls) for y in reps]


def mass_dual(F: Fp2, W, Lambda, n_ord: int) -> int:
    """E_c[T_W(c)] = sum_{eps in L^perp cap ternary} 2^{m-wt(eps)}, EXACT.

    DP over pairs with state = (sum_i eps_i y_i^l)_{l in Lambda}.
    """
    reps = pair_reps(F, W)
    cols = _syndrome_states(F, reps, Lambda, n_ord)
    k = len(sorted(Lambda))
    zero = tuple((0, 0) for _ in range(k))
    dp = {zero: 1}
    for col in cols:
        nd: dict = {}
        for st, val in dp.items():
            # eps_i = 0 : weight 2 (the two ways a zero coordinate appears in
            # the 2^{m-wt} bookkeeping)
            nd[st] = nd.get(st, 0) + 2 * val
            for sgn in (1, -1):
                ns = tuple(F.add(st[j], F.smul(sgn % F.p, col[j]))
                           for j in range(k))
                nd[ns] = nd.get(ns, 0) + val
        dp = nd
    return dp.get(zero, 0)


def mass_dual_bresolved(F: Fp2, W, Lambda, n_ord: int):
    """E_c[V_b] for b = 0..|W|, EXACT.

    Per pair the z-factor is (1 + z zeta^s)(1 + z zeta^{-s})
                            = 1 + z(zeta^s + zeta^{-s}) + z^2.
    Averaging over c, the ternary bookkeeping gives per pair the transitions
        eps=0, b += 0   (the '1')
        eps=+1, b += 1  (zeta^{+s})
        eps=-1, b += 1  (zeta^{-s})
        eps=0, b += 2   (the 'z^2' = zeta^s zeta^{-s})
    """
    reps = pair_reps(F, W)
    cols = _syndrome_states(F, reps, Lambda, n_ord)
    k = len(sorted(Lambda))
    m = len(reps)
    zero = tuple((0, 0) for _ in range(k))
    dp = {(zero, 0): 1}
    for col in cols:
        nd: dict = {}
        for (st, b), val in dp.items():
            nd[(st, b)] = nd.get((st, b), 0) + val
            nd[(st, b + 2)] = nd.get((st, b + 2), 0) + val
            for sgn in (1, -1):
                ns = tuple(F.add(st[j], F.smul(sgn % F.p, col[j]))
                           for j in range(k))
                nd[(ns, b + 1)] = nd.get((ns, b + 1), 0) + val
        dp = nd
    out = [0] * (2 * m + 1)
    for (st, b), val in dp.items():
        if st == zero:
            out[b] = val
    return out


def mass_direct_bresolved(F: Fp2, W, Lambda, n_ord: int):
    """sum over ALL c of V_b(c), EXACT in Z[zeta_p].  Returns (list, size)."""
    p = F.p
    reps = pair_reps(F, W)
    m = len(reps)
    tot = [[0] * p for _ in range(2 * m + 1)]
    size = 0
    for coeffs in enumerate_K1(F, Lambda):
        poly = [cyc_one(p)]
        for y in reps:
            s = chi_at(F, coeffs, y, n_ord)
            new = [None] * (len(poly) + 2)
            for j in range(len(poly) + 2):
                new[j] = [0] * p
            for j, cf in enumerate(poly):
                new[j] = cyc_add(new[j], cf)
                new[j + 1] = cyc_add(new[j + 1], cyc_mul_cos(cf, s))
                new[j + 2] = cyc_add(new[j + 2], cf)
            poly = new
        for j, cf in enumerate(poly):
            tot[j] = cyc_add(tot[j], cf)
        size += 1
    return tot, size


def rank_L(F: Fp2, W, Lambda, n_ord: int) -> int:
    """dim_{F_p} of L = image of K1(Lambda) -> F_p^m, c |-> (chi_c(y_i))_i.

    The map is F_p-linear in the 2|Lambda| coordinates (Re, w-part of each C_l).
    Row r of the matrix is the image of a basis frequency.
    """
    p = F.p
    reps = pair_reps(F, W)
    rows = []
    for l in sorted(Lambda):
        for base in ((1, 0), (0, 1)):
            rows.append([chi_at(F, {l: base}, y, n_ord) for y in reps])
    # gaussian elimination over F_p
    m = len(reps)
    rank = 0
    piv_col = 0
    rows = [r[:] for r in rows]
    while rank < len(rows) and piv_col < m:
        sel = None
        for r in range(rank, len(rows)):
            if rows[r][piv_col] % p:
                sel = r
                break
        if sel is None:
            piv_col += 1
            continue
        rows[rank], rows[sel] = rows[sel], rows[rank]
        inv = pow(rows[rank][piv_col], p - 2, p)
        rows[rank] = [(x * inv) % p for x in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][piv_col] % p:
                f = rows[r][piv_col]
                rows[r] = [(a - f * b) % p for a, b in zip(rows[r], rows[rank])]
        rank += 1
        piv_col += 1
    return rank


# ------------------------------------------------------- carry-window data ---


def sigma_of(p: int, s: int) -> int:
    s %= p
    return s + p * (1 if 2 * s > p else 0)


def deltas_of(F: Fp2, coeffs: dict, reps, n_ord: int):
    p = F.p
    two_p = 2 * p
    out = []
    for y in reps:
        sp = chi_at(F, coeffs, y, n_ord)
        sm = chi_at(F, coeffs, F.neg(y), n_ord)
        out.append((sigma_of(p, sp) - sigma_of(p, sm)) % two_p)
    return out


def defect_D(p: int, deltas) -> int:
    """The parity-defect certificate's D = sum_d |#even - #odd| per class."""
    cnt: dict = {}
    for d in deltas:
        r = d % p
        cnt[r] = cnt.get(r, 0) + (1 if d % 2 == 0 else -1)
    return sum(abs(v) for v in cnt.values())


def R_p_exact(p: int, deltas):
    """m * R_p, EXACTLY, as an integer.

    omega = zeta_{2p} and omega^p = -1, so omega^{p Delta_i} = (-1)^{Delta_i}.
    Hence m*R_p = sum_i (-1)^{Delta_i} -- a plain integer, and it equals m
    exactly iff every Delta_i is even (antipodal descent lemma, Corollary C).
    """
    return sum(1 if d % 2 == 0 else -1 for d in deltas)


def maxR_odd_float(p: int, deltas):
    """(max over odd k of |R_k|, argmax k) -- FLOAT diagnostic only."""
    import cmath
    import math
    two_p = 2 * p
    m = len(deltas)
    best, best_k = -1.0, None
    for k in range(1, two_p, 2):
        s = 0j
        for d in deltas:
            ang = math.pi * ((k * d) % two_p) / p
            s += cmath.exp(1j * ang)
        v = abs(s) / m
        if v > best:
            best, best_k = v, k
    return best, best_k


# =============================================================== V1: model ====


def V1_model():
    note("\n=== V1  model sanity: antipodal closure, K1 positivity ===")
    ok_all = True
    for e in (2, 3, 4):
        p = official_shaped_prime(e)
        F = Fp2(p)
        n_ord = 1 << (e + 1)
        for wname, W in (("full", window_full(F, n_ord)),
                         ("moving", window_moving(F, n_ord))):
            Wset = set(W)
            closed = all(F.neg(x) in Wset for x in W)
            reps = pair_reps(F, W)
            # K1 antipodal law: chi_c(-y) = -chi_c(y) for odd Lambda
            coeffs = {1: (2, 1), 3: (1, 3)}
            antip = all(
                chi_at(F, coeffs, F.neg(y), n_ord)
                == (-chi_at(F, coeffs, y, n_ord)) % p for y in reps)
            # and every Delta even (the antipodal descent lemma's Corollary B)
            dl = deltas_of(F, coeffs, reps, n_ord)
            alleven = all(d % 2 == 0 for d in dl)
            ok = closed and antip and alleven
            ok_all &= ok
            check(f"V1 p={p} e={e} W={wname} |W|={len(W)} m={len(reps)}",
                  ok, f"closed={closed} antipodal={antip} allDeltaEven={alleven}")
    return ok_all


# ======================================= V2: P1, the exact ternary identity ====


def V2_identity():
    note("\n=== V2  P1: E_c[T_W] = sum_{eps in Lperp, ternary} 2^{m-wt}  (exact) ===")
    rows = []
    ok_all = True
    cases = [
        (2, "full", {1}), (2, "moving", {1}),
        (3, "full", {1}), (3, "moving", {1}),
        (4, "moving", {1}),
        (2, "moving", {1, 3}),
        (3, "moving", {1, 3}),
    ]
    for e, wname, Lam in cases:
        p = official_shaped_prime(e)
        F = Fp2(p)
        n_ord = 1 << (e + 1)
        W = window_full(F, n_ord) if wname == "full" else window_moving(F, n_ord)
        m = len(W) // 2
        total, size = mass_direct(F, W, Lam, n_ord)
        isint, tv = cyc_as_int(total)
        dual = mass_dual(F, W, Lam, n_ord)
        ok = isint and (tv == size * dual)
        ok_all &= ok
        check(f"V2 p={p} W={wname} m={m} Lambda={sorted(Lam)}", ok,
              f"direct/|K1| = {tv}/{size}, dual = {dual}, "
              f"rational_integer={isint}")
        rows.append(dict(p=p, e=e, window=wname, m=m, Lambda=sorted(Lam),
                         class_size=size, direct_total=tv, dual_E=dual,
                         floor_2m=2 ** m, Z=dual / 2 ** m))
    return ok_all, rows


# ============================ V3: P2, surjectivity at the full condition set ===


def V3_surjectivity():
    note("\n=== V3  P2: Lambda = ALL odd residues  =>  rank(L) = m, Z = 1, "
         "E_c[T_W] = 2^{n/2} EXACTLY ===")
    rows = []
    ok_all = True
    for e in (2, 3, 4, 5):
        p = official_shaped_prime(e)
        F = Fp2(p)
        n_ord = 1 << (e + 1)
        Lam = set(range(1, n_ord, 2))          # every odd residue mod n_ord
        for wname, W in (("full", window_full(F, n_ord)),
                         ("moving", window_moving(F, n_ord))):
            m = len(W) // 2
            r = rank_L(F, W, Lam, n_ord)
            ok = (r == m)
            ok_all &= ok
            check(f"V3 p={p} e={e} W={wname} m={m} |Lambda|={len(Lam)}", ok,
                  f"rank(L) = {r} (need {m})  => L = F_p^m, Lperp = 0, Z = 1, "
                  f"E_c[T] = 2^{m}")
            rows.append(dict(p=p, e=e, window=wname, m=m, n_window=len(W),
                             rank=r, surjective=ok, E_T=2 ** m))
    # FULL brute force of the theorem: enumerate every c in K1(all odd l)
    note("  -- FULL brute force: every c in K1(Lambda = all odd residues) --")
    for e, wname in ((2, "moving"), (2, "full")):
        p = official_shaped_prime(e)
        F = Fp2(p)
        n_ord = 1 << (e + 1)
        W = window_moving(F, n_ord) if wname == "moving" else window_full(F, n_ord)
        reps = pair_reps(F, W)
        m = len(reps)
        ls = list(range(1, n_ord, 2))
        # precompute y_i^l
        tab = [[F.pw(y, l % n_ord) for l in ls] for y in reps]
        total = [0] * p
        size = 0
        p2 = p * p
        nfreq = p2 ** len(ls)
        for tcode in range(nfreq):
            u = tcode
            C = []
            for _ in ls:
                d = u % p2
                u //= p2
                C.append((d % p, d // p))
            acc = cyc_one(p)
            for i in range(m):
                a = b = 0
                row = tab[i]
                for j in range(len(ls)):
                    cj = C[j]
                    yj = row[j]
                    a += cj[0] * yj[0] + F.N * cj[1] * yj[1]
                    b += cj[0] * yj[1] + cj[1] * yj[0]
                s = (2 * a) % p
                acc = cyc_mul_pairfactor(acc, s)
            total = cyc_add(total, acc)
            size += 1
        isint, tv = cyc_as_int(total)
        ok = isint and (size == nfreq) and (tv == size * 2 ** m)
        ok_all &= ok
        check(f"V3b BRUTE FORCE p={p} W={wname} m={m} "
              f"Lambda=all {len(ls)} odd residues, |K1|={size}", ok,
              f"sum_c T_W(c) = {tv} = |K1| * 2^m = {size} * {2**m} "
              f"= {size * 2**m}  -> E_c[T_W] = 2^m EXACTLY")
    return ok_all, rows


# =========================== V4/V5: P3+P4, the b-resolved law and (O2) <= (O1) ==


def V4_bresolved():
    note("\n=== V4  P3+P4: E_c[V_b] exact; nonnegative; sums to E_c[T] ===")
    rows = []
    ok_all = True
    cases = [(2, "full", {1}), (2, "moving", {1}), (3, "moving", {1}),
             (3, "full", {1}), (2, "moving", {1, 3})]
    for e, wname, Lam in cases:
        p = official_shaped_prime(e)
        F = Fp2(p)
        n_ord = 1 << (e + 1)
        W = window_full(F, n_ord) if wname == "full" else window_moving(F, n_ord)
        m = len(W) // 2
        dual_b = mass_dual_bresolved(F, W, Lam, n_ord)
        tot_b, size = mass_direct_bresolved(F, W, Lam, n_ord)
        direct_b = []
        allint = True
        for cf in tot_b:
            isint, v = cyc_as_int(cf)
            allint &= isint
            direct_b.append(v)
        match = all(d == size * e2 for d, e2 in zip(direct_b, dual_b))
        nonneg = all(v >= 0 for v in dual_b)
        summ = sum(dual_b)
        E_T = mass_dual(F, W, Lam, n_ord)
        sums_ok = (summ == E_T)
        le = all(v <= E_T for v in dual_b)
        ok = allint and match and nonneg and sums_ok and le
        ok_all &= ok
        check(f"V4 p={p} W={wname} m={m} Lambda={sorted(Lam)}", ok,
              f"direct==dual:{match} nonneg:{nonneg} sum==E_T:{sums_ok} "
              f"max_b E[V_b]={max(dual_b)} <= E_T={E_T}:{le}")
        # the surjective case must give exactly C(m, b/2) at even b, 0 at odd b
        r = rank_L(F, W, Lam, n_ord)
        if r == m:
            binom = [0] * (2 * m + 1)
            for j in range(m + 1):
                c = 1
                for i in range(j):
                    c = c * (m - i) // (i + 1)
                binom[2 * j] = c
            ok2 = (dual_b == binom)
            ok_all &= ok2
            check(f"V4b surjective row p={p} W={wname}: E[V_b] == C(m,b/2)",
                  ok2, f"{dual_b[:8]}... vs {binom[:8]}...")
        rows.append(dict(p=p, window=wname, m=m, Lambda=sorted(Lam),
                         rank=r, E_Vb=dual_b, E_T=E_T))
    return ok_all, rows


# ================================= V6: P5, the rigorous necessary condition ====


def V6_necessary():
    note("\n=== V6  P5: E_c[T_W] >= 4^m / |L| = 2^n / p^{dim L}  (total positivity) ===")
    rows = []
    ok_all = True
    for e, wname, Lam in [(2, "full", {1}), (3, "full", {1}), (4, "full", {1}),
                          (3, "moving", {1}), (4, "moving", {1})]:
        p = official_shaped_prime(e)
        F = Fp2(p)
        n_ord = 1 << (e + 1)
        W = window_full(F, n_ord) if wname == "full" else window_moving(F, n_ord)
        m = len(W) // 2
        r = rank_L(F, W, Lam, n_ord)
        E_T = mass_dual(F, W, Lam, n_ord)
        lower = (4 ** m) // (p ** r) if p ** r <= 4 ** m else 0
        ok = (E_T * (p ** r) >= 4 ** m)
        ok_all &= ok
        check(f"V6 p={p} W={wname} m={m} rank={r}", ok,
              f"E_T = {E_T} >= 4^m/p^r = {4**m}/{p**r} = {lower}")
        rows.append(dict(p=p, window=wname, m=m, rank=r, E_T=E_T,
                         floor_2m=2 ** m, lower_4m_over_L=lower))
    return ok_all, rows


# ========================= V7: P6, reconciliation with the banked C3b numbers ==


def V7_reconcile():
    note("\n=== V7  P6: reproduce f2_fixed_sector/results/C3b_annealed_exact.json ===")
    note("  banked: per-pair mean 1.7433843858482772 (p=17), "
         "1.9790806830379395 (p=97), 2.216211414430072 (p=193, 20k sample)")
    rows = []
    ok_all = True
    banked = {17: 1.7433843858482772, 97: 1.9790806830379395,
              193: 2.216211414430072}
    for e, p_expect in ((4, 17), (5, 97), (6, 193)):
        p = official_shaped_prime(e)
        if p != p_expect:
            note(f"  (note: official_shaped_prime({e}) = {p}, banked row {p_expect})")
        F = Fp2(p)
        n_ord = 1 << (e + 1)
        W = window_full(F, n_ord)            # banked n = 2^{e+1}, npairs = 2^e
        m = len(W) // 2
        E_full = mass_dual(F, W, {1}, n_ord)          # includes c = 0
        size = p * p                                   # |K1({1})| = |F_{p^2}|
        T0 = 4 ** m                                    # T at c = 0
        punct = (size * E_full - T0)
        punct_mean = punct / (size - 1)
        per_pair_punct = punct_mean ** (1.0 / m)
        per_pair_full = E_full ** (1.0 / m)
        r = rank_L(F, W, {1}, n_ord)
        Z = E_full / 2 ** m
        target = banked.get(p)
        rel = abs(per_pair_punct - target) / target if target else None
        ok = (target is None) or (rel < 1e-12) or (p == 193 and rel < 5e-2)
        ok_all &= ok
        check(f"V7 p={p} m={m} rank(L)={r}", ok,
              f"per-pair (punctured) = {per_pair_punct!r} vs banked {target}"
              + (f"  rel={rel:.3e}" if rel is not None else ""))
        note(f"     E_full = 2^m * Z with Z = {Z!r} (2^m = {2**m}); "
             f"per-pair FULL = {per_pair_full:.6f} >= 2 exactly as P2's floor "
             f"requires")
        rows.append(dict(p=p, e=e, m=m, rank=r, E_full=E_full, Z=Z,
                         class_size=size, punctured_mean=punct_mean,
                         per_pair_punctured=per_pair_punct,
                         per_pair_full=per_pair_full, banked=target))
    return ok_all, rows


# ================================ V8: P7, the (O3) pullback ramification lemma ==


def V8_pullback():
    note("\n=== V8  P7: pullback f(x) = g(x^{2^d})  =>  P_j(f;z) = (P_{j-d}(g;z))^{2^d} ===")
    rows = []
    ok_all = True
    for e in (3, 4):
        p = official_shaped_prime(e)
        F = Fp2(p)
        for d in (1, 2):
            n = 1 << (e + 1)
            n_red = n >> d
            if n_red < 2:
                continue
            mu = F.subgroup(n)
            mu_red = F.subgroup(n_red)
            for g_coeffs in ({1: (3, 1)}, {1: (1, 0), 2: (2, 5)},
                             {3: (4, 2), 1: (0, 1)}):
                # f(x) = g(x^{2^d})
                f_coeffs = {(l * (1 << d)): c for l, c in g_coeffs.items()}
                pf = _zpoly(F, mu, f_coeffs, n)
                pg = _zpoly(F, mu_red, g_coeffs, n_red)
                pg_pow = _poly_pow(F.p, pg, 1 << d)
                ok = (len(pf) == len(pg_pow)) and all(
                    canon(a) == canon(b) for a, b in zip(pf, pg_pow))
                ok_all &= ok
                check(f"V8 p={p} n={n} d={d} g={sorted(g_coeffs)}", ok,
                      f"deg {len(pf)-1} vs {len(pg_pow)-1}")
                rows.append(dict(p=p, n=n, d=d, g=sorted(g_coeffs), ok=ok))
    return ok_all, rows


def _zpoly(F: Fp2, elems, coeffs: dict, n_ord: int):
    """prod_{x in elems} (1 + z zeta^{chi(x)}) as a list of Z[zeta_p] coeffs."""
    p = F.p
    poly = [cyc_one(p)]
    for x in elems:
        s = chi_at(F, coeffs, x, n_ord)
        new = [[0] * p for _ in range(len(poly) + 1)]
        for j, cf in enumerate(poly):
            new[j] = cyc_add(new[j], cf)
            new[j + 1] = cyc_add(new[j + 1], cyc_shift(cf, s))
        poly = new
    return poly


def _poly_mul(p: int, A, B):
    out = [[0] * p for _ in range(len(A) + len(B) - 1)]
    for i, a in enumerate(A):
        if all(x == 0 for x in a):
            continue
        for j, b in enumerate(B):
            if all(x == 0 for x in b):
                continue
            prod = [0] * p
            for u, av in enumerate(a):
                if av:
                    for v, bv in enumerate(b):
                        if bv:
                            prod[(u + v) % p] += av * bv
            out[i + j] = cyc_add(out[i + j], prod)
    return out


def _poly_pow(p: int, A, k: int):
    res = [cyc_one(p)]
    base = A
    while k:
        if k & 1:
            res = _poly_mul(p, res, base)
        k >>= 1
        if k:
            base = _poly_mul(p, base, base)
    return res


# ============================ V9: P8, T3-uniform refuted by completeness =======


def V9_t3_refutation():
    note("\n=== V9  P8: a GENERIC-class frequency with flat = 0 EXACTLY "
         "(T3-uniform refuted) ===")
    rows = []
    ok_all = True
    for e in (3, 4, 5):
        p = official_shaped_prime(e)
        F = Fp2(p)
        n_ord = 1 << (e + 1)
        W = window_moving(F, n_ord)          # the DEPLOYED window
        reps = pair_reps(F, W)
        mu = F.subgroup(n_ord)
        # ADVERSARIAL CONSTRUCTION.  Assign the character values freely (legal
        # exactly when the condition set covers every residue mod n_ord, so the
        # folded frequency is an ARBITRARY function -- Vandermonde/DFT).
        # Choose every value EVEN and < p/2:
        #   * < p/2  => every carry flag is 0  => Delta_i = s_i^+ - s_i^-,
        #   * all even => every Delta_i is EVEN => |R_p| = 1 => flat = 0.
        # Break the antipodal symmetry so BOTH parity parts are nonzero (G).
        Kc = max(2, (p - 1) // 8)
        vals = {}
        for i, y in enumerate(pair_reps(F, mu)):
            a = 2 * (i % Kc)
            b = 2 * ((i + 3) % Kc) + 2
            while 2 * a > p:
                a -= 2
            while 2 * b > p:
                b -= 2
            vals[y] = a
            vals[F.neg(y)] = b
        # F(x) = v(x)/2 in F_p has Tr(F(x)) = v(x)
        inv2 = pow(2, p - 2, p)
        fun = {x: ((vals[x] * inv2) % p, 0) for x in mu}
        coeffs = _interpolate(F, mu, fun, n_ord)
        # parity class of the interpolated frequency
        odd_sup = [l for l, c in coeffs.items() if l % 2 == 1 and c != (0, 0)]
        even_sup = [l for l, c in coeffs.items() if l % 2 == 0 and c != (0, 0)]
        # verify interpolation reproduces the values
        interp_ok = all(chi_at(F, coeffs, x, n_ord) == vals[x] % p for x in mu)
        dl = deltas_of(F, coeffs, reps, n_ord)
        m = len(dl)
        alleven = all(d % 2 == 0 for d in dl)
        mRp = R_p_exact(p, dl)               # EXACT integer: m*R_p
        flat_zero = (mRp == m)               # |R_p| = 1 exactly -> flat = 0
        maxR, kk = maxR_odd_float(p, dl)     # float diagnostic
        is_G = bool(odd_sup) and bool(even_sup)
        D = defect_D(p, dl)
        ok = interp_ok and is_G and alleven and flat_zero and (D == m)
        ok_all &= ok
        check(f"V9 p={p} n_ord={n_ord} m={m} deployed window", ok,
              f"interp={interp_ok} class=G({len(odd_sup)} odd,"
              f"{len(even_sup)} even) allDeltaEven={alleven} "
              f"m*R_p = {mRp} = m = {m} -> flat = 0 EXACTLY; "
              f"D = {D} (= m); float max_k|R_k| = {maxR:.6f} at k={kk}")
        rows.append(dict(p=p, n_ord=n_ord, m=m, n_odd_support=len(odd_sup),
                         n_even_support=len(even_sup), all_delta_even=alleven,
                         m_times_R_p=mRp, flat_is_zero=flat_zero,
                         float_maxR=maxR, argmax_k=kk, D=D))
    return ok_all, rows


def _interpolate(F: Fp2, mu, fun: dict, n_ord: int):
    """C_l = (1/n) sum_x F(x) x^{-l} -- the inverse DFT over mu_{n_ord}."""
    p = F.p
    n = len(mu)
    ninv = pow(n % p, p - 2, p)
    out = {}
    for l in range(n_ord):
        acc = (0, 0)
        for x in mu:
            acc = F.add(acc, F.mul(fun[x], F.pw(x, (-l) % n_ord)))
        out[l] = F.smul(ninv, acc)
    return out


# ================== V10: P10, the certificate is the WRONG FUNCTIONAL for (O1) ==


def V10_orthogonality():
    note("\n=== V10  P10: same window, same Delta multiset / same D / same flat, "
         "DIFFERENT mass ===")
    rows = []
    ok_all = True
    for e in (4, 5):
        p = official_shaped_prime(e)
        F = Fp2(p)
        n_ord = 1 << (e + 1)
        W = window_moving(F, n_ord)
        reps = pair_reps(F, W)
        m = len(reps)
        Lam_small = {1}
        Lam_full = set(range(1, n_ord, 2))
        E_small = mass_dual(F, W, Lam_small, n_ord)
        r_full = rank_L(F, W, Lam_full, n_ord)
        E_full = 2 ** m if r_full == m else mass_dual(F, W, Lam_full, n_ord)
        # certificate output is IDENTICAL on both: every K1 frequency of either
        # condition set gives all-Delta-even, hence D = m and flat = 0.
        cert_same = True
        for Lam in (Lam_small, Lam_full):
            for trial in range(6):
                coeffs = {l: (((trial + 1) * (l + 2)) % p, (trial * 3 + 1) % p)
                          for l in sorted(Lam)}
                dl = deltas_of(F, coeffs, reps, n_ord)
                if not all(d % 2 == 0 for d in dl):
                    cert_same = False
                if defect_D(p, dl) != m:
                    cert_same = False
        differ = (E_small != E_full)
        ok = cert_same and differ
        ok_all &= ok
        check(f"V10 p={p} W=moving m={m}", ok,
              f"certificate identical (all Delta even, D = m = {m}, flat = 0) "
              f"on BOTH condition sets, but E_c[T] = {E_small} (Lambda={{1}}) "
              f"vs {E_full} (Lambda=all odd) -- ratio {E_small/E_full:.4f}")
        rows.append(dict(p=p, m=m, E_small=E_small, E_full=E_full,
                         cert_identical=cert_same, D=m, flat=0))
    return ok_all, rows


# ================================== V11: P9, the T3 scoping arithmetic ========


def V11_scoping():
    note("\n=== V11  P9: official-row scoping arithmetic for T3 ===")
    P = 2 ** 31 - 2 ** 24 + 1                  # KoalaBear
    t = 7e10
    rows = []
    ok_all = True
    note(f"  p = 2^31 - 2^24 + 1 = {P}, v_2(p-1) = {v2(P-1)}, "
         f"log2 p = {P.bit_length()-1}.xx, sqrt(p) ~ 2^15.5, t ~ {t:.1e}")
    complete_upto = None
    for j in range(1, 17):
        n_j = 1 << (24 + j)
        m_j = 1 << (22 + j)
        complete = (t >= n_j)
        if complete:
            complete_upto = j
        # the window sits in F_{q_j}, q_j = p^{2^j}; |mu_{n_j}| = q_j^{delta}
        log2_q = 31.0 * (2 ** j)
        delta = (24 + j) / log2_q
        rows.append(dict(rung=j, n_j=n_j, m_j=m_j, t_ge_n=complete,
                         log2_q=log2_q, delta_subgroup_exponent=delta,
                         sqrt_q_exceeds_H=(log2_q / 2 > 24 + j)))
    ok = (complete_upto == 12)
    ok_all &= ok
    check("V11 t >= n_j exactly for rungs 1..12", ok,
          f"largest complete rung = {complete_upto} "
          f"(n_12 = {1<<36} <= {t:.1e} < n_13 = {1<<37})")
    dmax = max(r["delta_subgroup_exponent"] for r in rows if r["rung"] >= 13)
    ok2 = (dmax < 2e-4)
    ok_all &= ok2
    check("V11 rungs 13..16 have |H| = q^delta with delta < 2e-4", ok2,
          f"max delta over rungs 13..16 = {dmax:.3e}")
    ok3 = all(r["sqrt_q_exceeds_H"] for r in rows)
    ok_all &= ok3
    check("V11 |H| < sqrt(q_j) at EVERY rung (classical Gauss-sum bound vacuous)",
          ok3, f"rung 1: |H| = 2^25 vs sqrt(q_1) = 2^31")
    # the (O1) necessary condition of P5 at the official row
    note("\n  -- P5's necessary condition at the official row --")
    for j in (1, 8, 13, 16):
        m_j = 1 << (22 + j)
        need = m_j / 31.0
        note(f"     rung {j:2d}: m_j = 2^{22+j} = {m_j:.4e}, need dim L >= "
             f"m_j/log2 p = {need:.4e}; available <= t ~ {t:.1e} -> "
             f"{'OK' if t >= need else 'VIOLATED'} "
             f"(margin {t/need:.2f}x)")
    return ok_all, rows


# ============ V12: the SHARP hypothesis -- only m odd exponents are needed ====


def V12_vandermonde():
    note("\n=== V12  SHARP FORM of P2: Lambda = {1,3,...,2m-1} ALREADY gives "
         "rank m ===")
    note("  reason: (y_i^{2r-1})_{i,r} = diag(y_i) * Vandermonde(y_i^2), and the")
    note("  squares y_i^2 are DISTINCT because y -> y^2 is exactly 2-to-1 on")
    note("  mu_n with fibres the antipodal pairs.  So the matrix is invertible")
    note("  over F_{p^2}, and Tr is surjective coordinatewise.")
    rows = []
    ok_all = True
    for e in (2, 3, 4, 5):
        p = official_shaped_prime(e)
        F = Fp2(p)
        n_ord = 1 << (e + 1)
        for wname, W in (("full", window_full(F, n_ord)),
                         ("moving", window_moving(F, n_ord))):
            m = len(W) // 2
            Lam = set(range(1, 2 * m, 2))
            distinct = (len(Lam) == m) and (2 * m - 1 < n_ord)
            r = rank_L(F, W, Lam, n_ord)
            # squares of the pair reps really are distinct
            reps = pair_reps(F, W)
            sq = [F.mul(y, y) for y in reps]
            sq_distinct = (len(set(sq)) == m)
            ok = (r == m) and sq_distinct and distinct
            ok_all &= ok
            check(f"V12 p={p} e={e} W={wname} m={m} Lambda={{1,3,..,{2*m-1}}}",
                  ok, f"rank(L) = {r} (need {m}); squares distinct="
                      f"{sq_distinct}; exponents distinct mod n={distinct}")
            rows.append(dict(p=p, e=e, window=wname, m=m, n_ord=n_ord,
                             n_conditions_needed=2 * m - 1, rank=r,
                             squares_distinct=sq_distinct))
    # official-row consequence
    note("\n  -- official-row consequence: t >= 2 m_j - 1 = n_j/2 - 1 --")
    t = 7e10
    last = None
    for j in range(1, 17):
        need = (1 << (23 + j)) - 1
        if t >= need:
            last = j
    note(f"     the sharp hypothesis holds for rungs 1..{last} "
         f"(need t >= n_j/2 - 1; n_13/2 - 1 = {(1<<36)-1} <= {t:.1e} "
         f"< n_14/2 - 1 = {(1<<37)-1})")
    ok2 = (last == 13)
    ok_all &= ok2
    check("V12 official rungs covered by the sharp hypothesis = 1..13", ok2,
          f"last = {last}")
    return ok_all, rows


# ===================================================================== main ===


def main():
    os.makedirs(RESULTS, exist_ok=True)
    out: dict = {}
    ok1 = V1_model()
    ok2, r2 = V2_identity()
    ok3, r3 = V3_surjectivity()
    ok4, r4 = V4_bresolved()
    ok6, r6 = V6_necessary()
    ok7, r7 = V7_reconcile()
    ok8, r8 = V8_pullback()
    ok9, r9 = V9_t3_refutation()
    ok10, r10 = V10_orthogonality()
    ok11, r11 = V11_scoping()
    ok12, r12 = V12_vandermonde()
    out["V12_vandermonde"] = r12

    out["V2_identity"] = r2
    out["V3_surjectivity"] = r3
    out["V4_bresolved"] = r4
    out["V6_necessary"] = r6
    out["V7_reconcile"] = r7
    out["V8_pullback"] = r8
    out["V9_t3_refutation"] = r9
    out["V10_orthogonality"] = r10
    out["V11_scoping"] = r11

    with open(os.path.join(RESULTS, "verify_results.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)

    allok = all([ok1, ok2, ok3, ok4, ok6, ok7, ok8, ok9, ok10, ok11, ok12])
    note("\n" + "=" * 70)
    if allok:
        note("DIGEST: F2_OPENING_K1_MASS_ALL_PASS  (V1-V12)")
    else:
        note(f"DIGEST: F2_OPENING_FAILURES: {FAILURES}")
    note("=" * 70)
    with open(os.path.join(RESULTS, "VERIFY_LOG.txt"), "w") as f:
        f.write("\n".join(LOG) + "\n")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
