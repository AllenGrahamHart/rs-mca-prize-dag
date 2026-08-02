#!/usr/bin/env python3
"""FM1 + FM2 — split-fibre first-match selector pilot for P-B
(critical/nodes/xr_lowcore_spread_heart).

Run under the compute law, e.g.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/pb_split_fibre_selector/pb_split_fibre_pilot.py P3

All verdict-path arithmetic is exact (integers mod q). Floats appear only in
printed summaries.

WHAT THIS DOES
--------------
1. Builds a scaled analogue of the adversarial audit's split-fibre pencil
       U = G * X^(m a),   V = -G * X^(m (a-1)),   p_J = -G * R_J(X^m)
   over D = mu_n < F_q^*, and verifies every degree / support / strip /
   genericity identity exactly.
2. FM1: compiles the COMPLETE set W_z of exact-A witnesses at EVERY slope
   z in F_q (not only the pencil slopes), using the exact characterisation

       W_z  <->  { A-subsets S of D : deg( (U+zV) - prod_{x in S}(X-x) ) < K }

   which is valid because U+zV is monic of degree exactly A (so agreement can
   never exceed A, and every witness is f_z minus the monic locator of its own
   agreement support). Enumeration is meet-in-the-middle on power sums
   p_1..p_h, which are additive; the target power sums come from the target
   elementary symmetric functions by Newton's identities.
3. FM2: compares the CANDIDATE family {S_J} against the SELECTED family
   {first-match at each live slope} under four orders (see SELECTOR_MANIFEST).

Nothing here writes outside this directory.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from collections import Counter, defaultdict
from itertools import combinations

# --------------------------------------------------------------------------
# case table
# --------------------------------------------------------------------------
# constraints enforced by check_parameters():
#   n | q-1 ; m | n ; K = rate*n ; m <= h < 2m ; A = K + h = g + m*a ;
#   deg V = A - m >= K ; deg p <= A - 2m < K ; g >= 1 and core not a
#   union of complete fibres (else the pencil is T3 quotient-stripped) ;
#   g <= n/m - b (core drawn from distinct unused fibres).

CASES: dict[str, dict] = {
    # n=16, q=17 (D = mu_16 = F_17^*), rate 1/4, m=2, h=3.
    # A=7=g+m*a=1+2*3. Label pool = 7 of the 8 fibres; core = 1 point of the
    # 8th fibre. 2 z-independent constraints => ~C(16,7)/17^2 = 39.6 witnesses
    # spread over 17 slopes.
    "P1": dict(n=16, q=17, m=2, K=4, h=3, g=1, a=3, b=7, poly_order=True),
    # n=16, q=17, rate 1/4, m=2, h=2. A=6=2+2*2. Richest competition at n=16
    # (~C(16,6)/17 = 471 witnesses over 17 slopes) but the candidate family is
    # forced tiny (a=2 => pairwise-disjoint pairs).
    "P2": dict(n=16, q=17, m=2, K=4, h=2, g=2, a=2, b=6, poly_order=True),
    # FLAGSHIP. n=32, q=97, rate 1/4, m=2, h=3. A=11=1+2*5.
    # ~C(32,11)/97^2 = 13713 witnesses over 97 slopes (~141 per slope).
    "P3": dict(n=32, q=97, m=2, K=8, h=3, g=1, a=5, b=15, poly_order=True),
    # FLAGSHIP (deep competition). n=32, q=97, rate 1/4, m=2, h=2. A=10=2+2*4.
    # ~C(32,10)/97 = 665074 witnesses over 97 slopes (~6857 per slope).
    "P4": dict(n=32, q=97, m=2, K=8, h=2, g=2, a=4, b=14, poly_order=True),
    # CONTROL: m=4 at n=32 (the audit's own fibre width) but q^h swamps
    # C(n,A), so almost every slope has at most one witness. Included to show
    # what "no competition" looks like.
    "P5": dict(n=32, q=97, m=4, K=8, h=5, g=1, a=3, b=7, poly_order=True),
    # RATE CONTROL: n=32, q=97, rate 1/2 (not a clean-rate row; a scaling
    # probe only). A=19=1+2*9, ~C(32,19)/97^2 = 36919 witnesses.
    "P6": dict(n=32, q=97, m=2, K=16, h=3, g=1, a=9, b=15, poly_order=True),
    # DEEPEST competition reachable at n=32: rate 1/2, h=m=2, A=18=2+2*8,
    # ~C(32,18)/97^2 = 50105 witnesses per slope.
    "P7": dict(n=32, q=97, m=2, K=16, h=2, g=2, a=8, b=14, poly_order=False),
    # COMPETITION-DEPTH SWEEP at fixed (n,m,K,h,g,a,b), varying only q.
    # per-slope witness count ~ C(32,10)/q^2: 6857 / 1732 / 320 / 109.
    "P4b": dict(n=32, q=193, m=2, K=8, h=2, g=2, a=4, b=14, poly_order=False),
    "P4c": dict(n=32, q=449, m=2, K=8, h=2, g=2, a=4, b=14, poly_order=False),
    "P4d": dict(n=32, q=769, m=2, K=8, h=2, g=2, a=4, b=14, poly_order=False),
}

HASH_SEEDS = (b"pb-null-01", b"pb-null-02")


# --------------------------------------------------------------------------
# exact field / polynomial helpers  (all ints mod q)
# --------------------------------------------------------------------------
def prime_factors(x: int) -> list[int]:
    out, d = [], 2
    while d * d <= x:
        if x % d == 0:
            out.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        out.append(x)
    return out


def is_prime(x: int) -> bool:
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def primitive_root(q: int) -> int:
    fs = prime_factors(q - 1)
    for cand in range(2, q):
        if all(pow(cand, (q - 1) // f, q) != 1 for f in fs):
            return cand
    raise AssertionError("no primitive root")


def root_of_unity(q: int, n: int) -> int:
    assert (q - 1) % n == 0, "mu_n does not exist in F_q"
    w = pow(primitive_root(q), (q - 1) // n, q)
    assert pow(w, n, q) == 1
    for d in range(1, n):
        if n % d == 0 and pow(w, d, q) == 1:
            raise AssertionError("omega has order < n")
    return w


def ptrim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a: list[int], b: list[int], q: int) -> list[int]:
    r = [0] * max(len(a), len(b))
    for i in range(len(r)):
        r[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % q
    return ptrim(r)


def pneg(a: list[int], q: int) -> list[int]:
    return ptrim([(-c) % q for c in a])


def pscal(a: list[int], s: int, q: int) -> list[int]:
    return ptrim([(c * s) % q for c in a])


def pmul(a: list[int], b: list[int], q: int) -> list[int]:
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    r[i + j] = (r[i + j] + x * y) % q
    return ptrim(r)


def pshift(a: list[int], d: int) -> list[int]:
    return [0] * d + list(a)


def pcompose_xm(a: list[int], m: int) -> list[int]:
    r = [0] * (m * (len(a) - 1) + 1)
    for i, x in enumerate(a):
        r[m * i] = x
    return ptrim(r)


def peval(a: list[int], x: int, q: int) -> int:
    acc = 0
    for c in reversed(a):
        acc = (acc * x + c) % q
    return acc


def locator(roots: list[int], q: int) -> list[int]:
    p = [1]
    for r in roots:
        p = pmul(p, [(-r) % q, 1], q)
    return p


def deg(a: list[int]) -> int:
    return len(ptrim(list(a))) - 1


def newton_power_sums(e: list[int], h: int, q: int) -> list[int]:
    """e[1..h] elementary symmetric -> p[1..h] power sums (needs q > h)."""
    assert q > h, "Newton's identities need char > h"
    p = [0] * (h + 1)
    for j in range(1, h + 1):
        s = 0
        for i in range(1, j):
            s += ((-1) ** (i - 1)) * e[i] * p[j - i]
        s += ((-1) ** (j - 1)) * j * e[j]
        p[j] = s % q
    return p


# --------------------------------------------------------------------------
# construction
# --------------------------------------------------------------------------
class Case:
    def __init__(self, name: str, prm: dict):
        self.name = name
        self.__dict__.update(prm)
        self.A = self.K + self.h
        self.nf = self.n // self.m          # number of fibres / labels
        self.checks: list[tuple[str, bool, str]] = []
        self.build()

    def req(self, tag: str, cond: bool, detail: str = "") -> None:
        self.checks.append((tag, bool(cond), detail))
        if not cond:
            raise AssertionError(f"{self.name}: CHECK FAILED {tag} {detail}")

    # ---------------- parameters + field ----------------
    def build(self) -> None:
        q, n, m, K, h, g, a, b = (
            self.q, self.n, self.m, self.K, self.h, self.g, self.a, self.b)
        A = self.A
        self.req("prime_q", is_prime(q), f"q={q}")
        self.req("mu_n_exists", (q - 1) % n == 0, f"q-1={q-1} n={n}")
        self.req("m_divides_n", n % m == 0, f"m={m} n={n}")
        self.req("split_fibre_range", m <= h < 2 * m, f"m={m} h={h}")
        self.req("support_size", g + m * a == A, f"{g}+{m}*{a} vs A={A}")
        self.req("gap", A - K == h)
        self.req("degV_ge_K", A - m >= K, f"degV={A-m} K={K}")
        self.req("degp_lt_K", A - 2 * m < K, f"degp<={A-2*m} K={K}")
        self.req("intersection_cap", g + m * (a - 2) <= K - 1,
                 f"cap={g+m*(a-2)} K-1={K-1}")
        self.req("core_positive", g >= 1, "g=0 would fold through x->x^m (T3)")
        self.req("core_fits_unused_fibres", g <= self.nf - b,
                 f"g={g} unused_fibres={self.nf-b}")
        self.req("labels_fit", b >= a, f"b={b} a={a}")
        self.req("newton_ok", q > h)

        self.omega = root_of_unity(q, n)
        self.D = [pow(self.omega, i, q) for i in range(n)]
        self.req("domain_distinct", len(set(self.D)) == n)

        # fibre j (label omega^(m j)) = { i : i = j mod nf }
        self.fibre_idx = [[j + t * self.nf for t in range(m)]
                          for j in range(self.nf)]
        for j, fib in enumerate(self.fibre_idx):
            lab = pow(self.omega, m * j, q)
            self.req(f"fibre_eq_{j}",
                     all(pow(self.D[i], m, q) == lab for i in fib))
        self.labels = [pow(self.omega, m * j, q) for j in range(self.nf)]
        self.req("labels_distinct", len(set(self.labels)) == self.nf)

        # label pool = first b fibres; core = one point from each of the next g
        self.pool = list(range(b))
        self.core_idx = [self.nf * 0 + j for j in range(b, b + g)]
        self.req("core_disjoint_from_pool",
                 all(i % self.nf >= b for i in self.core_idx))
        self.req("core_not_fibre_union",
                 not any(set(fib) <= set(self.core_idx)
                         for fib in self.fibre_idx),
                 "core must not be a union of complete fibres (T3)")

        self.G = locator([self.D[i] for i in self.core_idx], q)
        self.req("degG", deg(self.G) == g)
        self.U = pshift(self.G, m * a)
        self.V = pneg(pshift(self.G, m * (a - 1)), q)
        self.req("degU", deg(self.U) == A, f"{deg(self.U)} vs {A}")
        self.req("degV", deg(self.V) == A - m)
        self.req("U_monic", self.U[A] == 1)

        self.strip_checks()

    # ---------------- strips + genericity ----------------
    def strip_checks(self) -> None:
        q, n, m, K = self.q, self.n, self.m, self.K
        u = [peval(self.U, x, q) for x in self.D]
        v = [peval(self.V, x, q) for x in self.D]
        self.req("T1_u_nonzero", any(u))
        self.req("T1_v_nonzero", any(v))
        prop = False
        for lam in range(q):
            if all((v[i] - lam * u[i]) % q == 0 for i in range(n)):
                prop = True
        self.req("T1_not_proportional", not prop)

        # T2: deg(u+zv) = A for every z, so agreement can never exceed A.
        for z in range(q):
            fz = padd(self.U, pscal(self.V, z, q), q)
            if deg(fz) != self.A or fz[self.A] != 1:
                self.req("T2_monic_degA", False, f"z={z}")
        self.req("T2_monic_degA", True, "deg(u+zv)=A monic for all z")

        # T3: no rate-preserving fold x -> x^M, M | gcd(n,K), M>1
        gc = self._gcd(n, K)
        folds = []
        for M in range(2, gc + 1):
            if gc % M:
                continue
            zeta = pow(self.omega, n // M, q)
            fold_u = all(peval(self.U, (zeta * x) % q, q) == peval(self.U, x, q)
                         for x in self.D)
            fold_v = all(peval(self.V, (zeta * x) % q, q) == peval(self.V, x, q)
                         for x in self.D)
            if fold_u and fold_v:
                folds.append(M)
        self.req("T3_no_quotient_fold", not folds, f"folds={folds}")

        # T4 direction rank 2 (u, v linearly independent as words)
        indep = any((u[i] * v[j] - u[j] * v[i]) % q
                    for i in range(n) for j in range(n))
        self.req("T4_rank_two", indep)

        # global genericity: joint agreement <= deg(V - c_1) = A - m < A
        self.req("globally_generic_by_degree", self.A - m < self.A and
                 deg(self.V) >= K,
                 f"joint support <= {self.A-m} < A={self.A}")

    @staticmethod
    def _gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x

    # ---------------- candidate family ----------------
    def build_family(self) -> None:
        q, m, a, b = self.q, self.m, self.a, self.b
        fam: list[tuple[int, ...]] = []
        sums: set[int] = set()
        diffs: set[tuple[frozenset, frozenset]] = set()
        for J in combinations(range(b), a):
            Js = set(J)
            if any(len(Js & set(J2)) > a - 2 for J2 in fam):
                continue
            zJ = sum(self.labels[i] for i in J) % q
            if zJ in sums:
                continue
            new: set[tuple[frozenset, frozenset]] = set()
            ok = True
            for J2 in fam:
                S2 = set(J2)
                d = (frozenset(Js - S2), frozenset(S2 - Js))
                dr = (d[1], d[0])
                if d in diffs or dr in diffs or d in new or dr in new:
                    ok = False
                    break
                new.add(d)
                new.add(dr)
            if not ok:
                continue
            fam.append(J)
            sums.add(zJ)
            diffs |= new
        self.family = fam

        # realize each J: witness polynomial, slope, support
        self.cand: list[dict] = []
        for J in fam:
            QJ = [1]
            for i in J:
                QJ = pmul(QJ, [(-self.labels[i]) % q, 1], q)
            zJ = sum(self.labels[i] for i in J) % q
            self.req("QJ_deg", deg(QJ) == a)
            self.req("QJ_e1", (-QJ[a - 1]) % q == zJ)
            RJ = ptrim(QJ[: a - 1] + [0])
            self.req("RJ_deg", deg(RJ) <= a - 2 or RJ == [0])
            pJ = pneg(pmul(self.G, pcompose_xm(RJ, m), q), q)
            self.req("degpJ_lt_K", deg(pJ) < self.K, f"{deg(pJ)}")
            lhs = padd(padd(self.U, pscal(self.V, zJ, q), q), pneg(pJ, q), q)
            rhs = pmul(self.G, pcompose_xm(QJ, m), q)
            self.req("split_fibre_identity", lhs == rhs, str(J))
            sup = sorted(set(self.core_idx) |
                         {i for j in J for i in self.fibre_idx[j]})
            self.req("support_size_A", len(sup) == self.A, str(J))
            roots = [i for i in range(self.n)
                     if peval(rhs, self.D[i], q) == 0]
            self.req("exact_agreement_support", roots == sup, str(J))
            self.cand.append(dict(J=list(J), z=zJ, support=sup,
                                  mask=mask_of(sup), degp=deg(pJ)))
        # candidate slopes distinct
        self.req("candidate_slopes_distinct",
                 len({c["z"] for c in self.cand}) == len(self.cand))

    # ---------------- target symmetric functions per slope ----------------
    def targets(self, z: int) -> list[int]:
        """power sums p_1..p_h that any S in W_z must have."""
        q, A, h = self.q, self.A, self.h
        fz = padd(self.U, pscal(self.V, z, q), q)
        assert deg(fz) == A and fz[A] == 1
        e = [0] * (h + 1)
        for j in range(1, h + 1):
            e[j] = (((-1) ** j) * fz[A - j]) % q
        return newton_power_sums(e, h, q)


def mask_of(idx) -> int:
    r = 0
    for i in idx:
        r |= 1 << i
    return r


def idx_of(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def popcount(x: int) -> int:
    return bin(x).count("1")


# --------------------------------------------------------------------------
# FM1 : complete witness compiler (meet in the middle on power sums)
# --------------------------------------------------------------------------
def half_tables(vals: list[int], h: int, q: int):
    L = len(vals)
    size = [0] * (1 << L)
    ps = [[0] * (1 << L) for _ in range(h + 1)]
    powv = [[pow(v, j, q) for j in range(h + 1)] for v in vals]
    for mask in range(1, 1 << L):
        low = mask & -mask
        i = low.bit_length() - 1
        rest = mask ^ low
        size[mask] = size[rest] + 1
        pv = powv[i]
        for j in range(1, h + 1):
            ps[j][mask] = (ps[j][rest] + pv[j]) % q
    return size, ps


def enumerate_all_witnesses(case: Case, on_solution):
    """Call on_solution(z, mask) for every (slope, exact-A support) pair."""
    q, n, h, A = case.q, case.n, case.h, case.A
    L1 = n // 2
    v1 = case.D[:L1]
    v2 = case.D[L1:]
    s1, p1 = half_tables(v1, h, q)
    s2, p2 = half_tables(v2, h, q)

    def enc(sz, pv):
        k = sz
        for j in range(1, h + 1):
            k = k * q + pv[j]
        return k

    table: dict[int, list[int]] = defaultdict(list)
    for mask in range(1 << L1):
        if s1[mask] > A:
            continue
        table[enc(s1[mask], [0] + [p1[j][mask] for j in range(1, h + 1)])
              ].append(mask)

    half2 = [m2 for m2 in range(1 << (n - L1)) if s2[m2] <= A]
    for z in range(q):
        t = case.targets(z)
        for m2 in half2:
            need_sz = A - s2[m2]
            k = need_sz
            for j in range(1, h + 1):
                k = k * q + (t[j] - p2[j][m2]) % q
            lst = table.get(k)
            if not lst:
                continue
            shifted = m2 << L1
            for m1 in lst:
                on_solution(z, m1 | shifted)


# --------------------------------------------------------------------------
# orders
# --------------------------------------------------------------------------
def key_lex(mask: int, n: int, *_):
    return tuple(idx_of(mask, n))


def key_colex(mask: int, n: int, *_):
    return mask


def key_polylex(mask: int, n: int, case: Case, z: int, fz_cache: dict):
    q, A, K = case.q, case.A, case.K
    fz = fz_cache.get(z)
    if fz is None:
        fz = padd(case.U, pscal(case.V, z, q), q)
        fz_cache[z] = fz
    loc = locator([case.D[i] for i in idx_of(mask, n)], q)
    p = padd(fz, pneg(loc, q), q)
    assert deg(p) < K
    return tuple((p[i] if i < len(p) else 0) for i in range(K))


def key_hash_factory(seed: bytes):
    def key(mask: int, n: int, *_):
        return hashlib.blake2b(mask.to_bytes(8, "little"),
                               digest_size=16, key=seed).digest()
    return key


# --------------------------------------------------------------------------
# FM2 : family statistics
# --------------------------------------------------------------------------
def diff_stats(masks: list[int]) -> dict:
    c: Counter = Counter()
    M = len(masks)
    for i in range(M):
        Si = masks[i]
        for j in range(M):
            if i == j:
                continue
            Sj = masks[j]
            c[(Si & ~Sj, Sj & ~Si)] += 1
    if not c:
        return dict(M=M, ordered_pairs=0, distinct_differences=0,
                    max_multiplicity=0, additive_energy=M * M,
                    repeated_difference_pairs=0, sidon=True)
    mult = list(c.values())
    return dict(
        M=M,
        ordered_pairs=M * (M - 1),
        distinct_differences=len(c),
        max_multiplicity=max(mult),
        additive_energy=M * M + sum(x * x for x in mult),
        repeated_difference_pairs=sum(x for x in mult if x > 1),
        sidon=all(x == 1 for x in mult),
    )


def intersection_stats(masks: list[int], K: int) -> dict:
    M = len(masks)
    mx, hist = 0, Counter()
    lo = []
    eq_K = 0            # unordered pairs meeting in exactly K
    above_K = 0         # unordered pairs meeting in >= K+1
    touch_above = set()
    unallocated = []    # max core >= K+1 but never exactly K  (bridge gap)
    adj = [set() for _ in range(M)]
    for i in range(M):
        worst = 0
        has_eqK = False
        has_above = False
        for j in range(M):
            if i == j:
                continue
            t = popcount(masks[i] & masks[j])
            hist[t] += 1
            worst = max(worst, t)
            if t == K:
                has_eqK = True
                eq_K += 1
            if t >= K + 1:
                has_above = True
                above_K += 1
                touch_above.add(i)
            if t >= K:
                adj[i].add(j)
        mx = max(mx, worst)
        if M == 1 or worst <= K - 1:
            lo.append(i)
        if has_above and not has_eqK:
            unallocated.append(i)
    # greedy maximal subfamily that is pairwise <= K-1 (a LOWER bound on the
    # largest low-core subfamily the selector still retains)
    order = sorted(range(M), key=lambda i: len(adj[i]))
    chosen: list[int] = []
    for i in order:
        if all(j not in adj[i] for j in chosen):
            chosen.append(i)
    return dict(max_pairwise_intersection=mx,
                gamma_lo_size=len(lo),
                gamma_hi_size=M - len(lo),
                pairs_core_eq_K=eq_K // 2,
                pairs_core_above_K=above_K // 2,
                slopes_touching_core_above_K=len(touch_above),
                unallocated_slopes_bridge_gap=len(unallocated),
                greedy_lowcore_subfamily=len(chosen),
                intersection_histogram={str(k): v
                                        for k, v in sorted(hist.items())})


def prefix_stats(masks: list[int], n: int, block: int = 0) -> dict:
    if not masks:
        return dict(common_prefix_len=0, common_coordinates=0,
                    full_initial_block_slopes=0, max_index_used=0,
                    window_width=0)
    common = masks[0]
    for m in masks[1:]:
        common &= m
    idx_sets = [idx_of(m, n) for m in masks]
    L = 0
    while True:
        if any(len(s) <= L for s in idx_sets):
            break
        if len({s[L] for s in idx_sets}) != 1:
            break
        L += 1
    blockmask = (1 << block) - 1
    full_block = sum(1 for m in masks if (m & blockmask) == blockmask)
    top = max(s[-1] for s in idx_sets)
    return dict(common_prefix_len=L, common_coordinates=popcount(common),
                full_initial_block_slopes=full_block,
                initial_block_size=block,
                max_index_used=top, window_width=top + 1)


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------
def run_case(name: str) -> dict:
    case = Case(name, CASES[name])
    case.build_family()
    n, q, A, K = case.n, case.q, case.A, case.K

    orders = [("ORD-LEX", key_lex), ("ORD-COLEX", key_colex)]
    if case.poly_order:
        orders.append(("ORD-POLYLEX", key_polylex))
    for s in HASH_SEEDS:
        orders.append((f"ORD-HASH-{s.decode()}", key_hash_factory(s)))

    intended = {c["z"]: c["mask"] for c in case.cand}
    fz_cache: dict = {}

    # intended keys per order
    intended_key = {}
    for oname, kf in orders:
        for z, msk in intended.items():
            intended_key[(oname, z)] = kf(msk, n, case, z, fz_cache)

    per_slope_count: Counter = Counter()
    best: dict[tuple[str, int], tuple] = {}
    best_mask: dict[tuple[str, int], int] = {}
    n_less: Counter = Counter()
    intended_seen: set[int] = set()
    total = 0

    def on_solution(z: int, mask: int):
        nonlocal total
        total += 1
        per_slope_count[z] += 1
        if z in intended and mask == intended[z]:
            intended_seen.add(z)
        for oname, kf in orders:
            k = kf(mask, n, case, z, fz_cache)
            cur = best.get((oname, z))
            if cur is None or k < cur:
                best[(oname, z)] = k
                best_mask[(oname, z)] = mask
            ik = intended_key.get((oname, z))
            if ik is not None and k < ik:
                n_less[(oname, z)] += 1

    enumerate_all_witnesses(case, on_solution)

    case.req("all_intended_witnesses_found",
             intended_seen == set(intended.keys()),
             f"missing={sorted(set(intended)-intended_seen)}")

    live = sorted(per_slope_count)
    counts = [per_slope_count[z] for z in live]

    cand_masks = [c["mask"] for c in case.cand]
    cand_report = dict(
        size=len(cand_masks),
        slopes=[c["z"] for c in case.cand],
        supports=[c["support"] for c in case.cand],
        J=[c["J"] for c in case.cand],
        **diff_stats(cand_masks),
        **intersection_stats(cand_masks, K),
        **prefix_stats(cand_masks, n, A - case.h),
    )

    per_order = {}
    for oname, _kf in orders:
        sel = [best_mask[(oname, z)] for z in live]
        matches = [z for z in intended
                   if best_mask.get((oname, z)) == intended[z]]
        ranks = {str(z): n_less[(oname, z)] + 1 for z in intended}
        st = dict(
            live_slopes=len(live),
            distinct_selected_supports=len(set(sel)),
            intended_is_first_match=len(matches),
            intended_first_match_slopes=sorted(matches),
            intended_rank=ranks,
            intended_rank_max=max(ranks.values()) if ranks else 0,
            intended_rank_median=sorted(ranks.values())[len(ranks) // 2]
            if ranks else 0,
            **diff_stats(sel),
            **intersection_stats(sel, K),
            **prefix_stats(sel, n, A - case.h),
        )
        # candidate-slope-restricted selected family
        selc = [best_mask[(oname, z)] for z in sorted(intended)]
        st["restricted_to_candidate_slopes"] = dict(
            **diff_stats(selc), **intersection_stats(selc, K),
            **prefix_stats(selc, n, A - case.h))
        # COUNTERFACTUAL: intended witness at every pencil slope, first-match
        # elsewhere.  This is the family P-B would have to count if the
        # exhibited witnesses WERE the normative selections.
        cf_masks = [intended[z] if z in intended else best_mask[(oname, z)]
                    for z in live]
        cf_is = intersection_stats(cf_masks, K)
        cf_lo_cand = 0
        for z in sorted(intended):
            msk = intended[z]
            worst = max((popcount(msk & o) for w, o in zip(live, cf_masks)
                         if w != z), default=0)
            if worst <= K - 1:
                cf_lo_cand += 1
        st["counterfactual_intended_normative"] = dict(
            **diff_stats(cf_masks), **cf_is,
            candidate_slopes_in_gamma_lo=cf_lo_cand,
            candidate_slopes=len(intended))
        st["example_selected_supports"] = [
            idx_of(best_mask[(oname, z)], n) for z in live[:6]]
        per_order[oname] = st

    out = dict(
        case=name,
        parameters=dict(n=n, q=q, m=case.m, K=K, h=case.h, A=A,
                        g=case.g, a=case.a, b=case.b, rate=f"{K}/{n}",
                        omega=case.omega,
                        core_indices=case.core_idx,
                        label_pool=case.pool),
        checks=[dict(tag=t, ok=o, detail=d) for t, o, d in case.checks],
        witness_census=dict(
            total_exact_A_witnesses=total,
            live_slopes=len(live),
            dead_slopes=q - len(live),
            slope_infinity_live=False,
            min_witnesses_per_live_slope=min(counts) if counts else 0,
            max_witnesses_per_live_slope=max(counts) if counts else 0,
            mean_witnesses_per_live_slope_num=total,
            mean_witnesses_per_live_slope_den=len(live) if live else 1,
            per_slope_counts={str(z): per_slope_count[z] for z in live},
        ),
        budget=dict(budget_8n3=8 * n ** 3, candidate_family_size=len(cand_masks),
                    n_squared=n ** 2,
                    budget_test_vacuous=len(cand_masks) <= 8 * n ** 3),
        candidate_family=cand_report,
        selected_family=per_order,
    )
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cases", nargs="*", default=list(CASES))
    ap.add_argument("--outdir", default=os.path.dirname(os.path.abspath(__file__)))
    args = ap.parse_args()
    for name in args.cases:
        res = run_case(name)
        path = os.path.join(args.outdir, f"results_{name}.json")
        with open(path, "w") as fh:
            json.dump(res, fh, indent=1, sort_keys=True)
        wc = res["witness_census"]
        cf = res["candidate_family"]
        print(f"[{name}] n={res['parameters']['n']} q={res['parameters']['q']} "
              f"m={res['parameters']['m']} K={res['parameters']['K']} "
              f"h={res['parameters']['h']} A={res['parameters']['A']} "
              f"| candidates M={cf['size']} sidon={cf['sidon']} "
              f"| witnesses={wc['total_exact_A_witnesses']} "
              f"live={wc['live_slopes']} "
              f"per-slope[{wc['min_witnesses_per_live_slope']}"
              f"..{wc['max_witnesses_per_live_slope']}]")
        for oname, st in res["selected_family"].items():
            print(f"    {oname:22s} intended-first-match "
                  f"{st['intended_is_first_match']}/{cf['size']} "
                  f"| sel Gamma_lo={st['gamma_lo_size']}/{st['live_slopes']} "
                  f"maxcap={st['max_pairwise_intersection']} (K-1="
                  f"{res['parameters']['K']-1}) "
                  f"sidon={st['sidon']} maxmult={st['max_multiplicity']} "
                  f"commonprefix={st['common_prefix_len']}")
        print(f"    -> {path}")


if __name__ == "__main__":
    main()
