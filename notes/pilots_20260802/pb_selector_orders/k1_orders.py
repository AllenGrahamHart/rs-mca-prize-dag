#!/usr/bin/env python3
"""K1 under every viable resolution of the P-B first-match selector order.

Lane P-B.  Runs the adversarial audit's kill line K1 -- "does the NORMATIVE
selector, run on split-fibre pencils, itself select a super-budget Sidon-type
family?" -- under each concrete total order that the SELECTOR_MANIFEST's
ambiguities A1-A8 generate, at scales where exact exhaustive first-match
selection is computable.

Run under the compute law from the repo root, e.g.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/pb_selector_orders/k1_orders.py select Q3
    tools/ramguard local -- python3 \
        notes/pilots_20260802/pb_selector_orders/k1_orders.py stats Q3

All verdict-path arithmetic is exact (integers mod q, Fractions for ratios).

Construction, parameter checks, candidate-family builder and the family
statistics are IMPORTED from the prior pilot
(notes/pilots_20260802/pb_split_fibre_selector/pb_split_fibre_pilot.py) so
that shared parameter points cross-validate exactly.  Nothing outside this
directory is written.

Enumeration differs from the prior pilot (and is much faster): instead of
looping over slopes, note that for the split-fibre pencil
    U = G X^{m a},  V = -G X^{m(a-1)}
the exact-A membership condition  deg(f_z - prod_{x in S}(X-x)) < K  reads
    e_j(S) = (-1)^j (alpha_j + z beta_j),  j = 1..h,
with alpha_j = U[A-j] = G[g-j] and beta_j = V[A-j] = -G[g-j+m].  beta_j = 0
for j < m, so the first m-1 constraints are SLOPE-FREE (used as the
meet-in-the-middle key), beta_m = -1 always, so j = m DETERMINES z, and
j = m+1..h are verified.  Every exact-A witness at every slope is produced
exactly once.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_PRIOR = os.path.join(os.path.dirname(_HERE), "pb_split_fibre_selector")
sys.dont_write_bytecode = True   # never write into the prior pilot's dir
sys.path.insert(0, _PRIOR)
import pb_split_fibre_pilot as P  # noqa: E402

# ---------------------------------------------------------------------------
# candidate orders: exact comparators + their A1-A8 resolutions
# ---------------------------------------------------------------------------
# A1  object ordered: agreement support / witness polynomial / codeword
# A1' object ordered: agreement support S  vs  its complement (error support)
# A2  lex vs colex on supports
# A3  coordinate order on D: exponent (x_i = omega^i) vs integer value
# A4  polynomial reading: coefficient direction and residue representatives
# A5  strip before/after selection  (moot: pencil is strip-free, see manifest)
# A6  ties  (none: supports distinct inside W_z; every comparator below total)
# A7  affine vs projective slope set (z = infinity dead at all parameters)
# A8  order-minimum vs procedural first match

ORDER_SPEC = {
    "ORD-LEX": dict(
        summary="min agreement support, increasing exponent-index tuple, "
                "lexicographic.  S prec T iff min(S xor T) in S.",
        A1="agreement support (a)", A1p="agreement support",
        A2="lex", A3="exponent order x_i = omega^i", A4="n/a",
        A5="moot (strip-free pencil)", A6="no ties (total on W_z)",
        A7="affine", A8="order-minimum",
        leading=True),
    "ORD-COLEX": dict(
        summary="min support bitmask as an integer.  S prec T iff "
                "max(S xor T) in T.",
        A1="agreement support (a)", A1p="agreement support",
        A2="colex", A3="exponent order", A4="n/a",
        A5="moot", A6="no ties", A7="affine", A8="order-minimum"),
    "ORD-VALEX": dict(
        summary="value-major lexicographic (support reading): coordinates "
                "re-indexed by the integer representative of x in F_q, then "
                "lex on the increasing tuple.",
        A1="agreement support (a)", A1p="agreement support",
        A2="lex", A3="integer-representative order", A4="n/a",
        A5="moot", A6="no ties", A7="affine", A8="order-minimum"),
    "ORD-VALCOLEX": dict(
        summary="value-order coordinates, colex.",
        A1="agreement support (a)", A1p="agreement support",
        A2="colex", A3="integer-representative order", A4="n/a",
        A5="moot", A6="no ties", A7="affine", A8="order-minimum"),
    "ORD-ERRLEX": dict(
        summary="min ERROR support (D minus S) lexicographically in exponent "
                "order -- the decoder reading of 'first match'.  Identically "
                "the REVERSE of ORD-LEX on equal-size supports.",
        A1="agreement support (a)", A1p="error support (complement)",
        A2="lex", A3="exponent order", A4="n/a",
        A5="moot", A6="no ties", A7="affine", A8="order-minimum"),
    "ORD-POLYLEX": dict(
        summary="witness polynomial, coefficients low-to-high, residues "
                "{0..q-1}, lexicographic.",
        A1="witness polynomial (b)", A1p="n/a",
        A2="n/a", A3="n/a (coefficients)",
        A4="low-to-high, representatives 0..q-1",
        A5="moot", A6="no ties", A7="affine", A8="order-minimum"),
    "ORD-POLYHI": dict(
        summary="witness polynomial, coefficients HIGH-to-low, residues "
                "{0..q-1}, lexicographic.",
        A1="witness polynomial (b)", A1p="n/a",
        A2="n/a", A3="n/a",
        A4="high-to-low, representatives 0..q-1",
        A5="moot", A6="no ties", A7="affine", A8="order-minimum"),
    "ORD-POLYCENT": dict(
        summary="witness polynomial, coefficients low-to-high, CENTRED "
                "representatives -(q-1)/2..(q-1)/2, lexicographic.",
        A1="witness polynomial (b)", A1p="n/a",
        A2="n/a", A3="n/a",
        A4="low-to-high, centred representatives",
        A5="moot", A6="no ties", A7="affine", A8="order-minimum"),
    "ORD-CODEWORD": dict(
        summary="value-major lexicographic (codeword reading): the witness "
                "CODEWORD (p(x_0),...,p(x_{n-1})) in exponent coordinate "
                "order, residues {0..q-1}, lexicographic.",
        A1="codeword / evaluation vector (b')", A1p="n/a",
        A2="n/a", A3="exponent order (evaluation coordinates)",
        A4="evaluations, representatives 0..q-1",
        A5="moot", A6="no ties", A7="affine", A8="order-minimum"),
    "ORD-DEGLEX": dict(
        summary="procedural reading: a decoder enumerating codewords by "
                "increasing degree.  key = (deg p, ORD-LEX support key).",
        A1="witness polynomial then support", A1p="agreement support",
        A2="lex (tie-break)", A3="exponent order",
        A4="degree only, no representative choice",
        A5="moot", A6="ties broken by ORD-LEX", A7="affine",
        A8="PROCEDURAL (low-degree-first search)"),
    "ORD-SLOPEMAJOR": dict(
        summary="slope-major lexicographic: order the full witness datum "
                "(z, p, S) with the slope as the leading key, then "
                "ORD-POLYLEX, then ORD-LEX.",
        A1="witness/codeword pair including its slope", A1p="agreement "
           "support",
        A2="lex", A3="exponent order", A4="low-to-high, 0..q-1",
        A5="moot", A6="no ties", A7="affine", A8="order-minimum",
        note="DEGENERATE by the pinned 'one selection per slope' semantics: "
             "z is constant on W_z, so the leading key never separates and "
             "the induced selection equals the tail order's.  Verified "
             "computationally (selected families identical to ORD-POLYLEX)."),
    "ORD-HASH-pb-null-01": dict(
        summary="NULL CONTROL: blake2b(bitmask, key='pb-null-01').",
        A1="n/a", A1p="n/a", A2="n/a", A3="n/a", A4="n/a",
        A5="moot", A6="no ties", A7="affine", A8="order-minimum"),
    "ORD-HASH-pb-null-02": dict(
        summary="NULL CONTROL: blake2b(bitmask, key='pb-null-02').",
        A1="n/a", A1p="n/a", A2="n/a", A3="n/a", A4="n/a",
        A5="moot", A6="no ties", A7="affine", A8="order-minimum"),
}

EXACT_ORDERS = ["ORD-LEX", "ORD-COLEX", "ORD-VALEX", "ORD-VALCOLEX",
                "ORD-ERRLEX", "ORD-HASH-pb-null-01", "ORD-HASH-pb-null-02"]
PREF_ORDERS = ["ORD-POLYLEX", "ORD-POLYHI", "ORD-POLYCENT", "ORD-CODEWORD"]
ALL_ORDERS = (EXACT_ORDERS[:5] + PREF_ORDERS
              + ["ORD-DEGLEX", "ORD-SLOPEMAJOR"] + EXACT_ORDERS[5:])

# ---------------------------------------------------------------------------
# scales
# ---------------------------------------------------------------------------
CASES = {
    # n = 16, rate 1/4 -- small anchor, two field sizes
    "Q1": dict(n=16, q=17, m=2, K=4, h=2, g=2, a=2, b=6),    # prior P2
    "Q2": dict(n=16, q=97, m=2, K=4, h=2, g=2, a=2, b=6),    # new, sparse
    "Q3": dict(n=16, q=17, m=2, K=4, h=3, g=1, a=3, b=7),    # prior P1
    # n = 32, rate 1/4, h = m = 2 -- densest reachable competition
    "Q4": dict(n=32, q=97, m=2, K=8, h=2, g=2, a=4, b=14),   # prior P4
    "Q5": dict(n=32, q=193, m=2, K=8, h=2, g=2, a=4, b=14),  # prior P4b
    "Q6": dict(n=32, q=449, m=2, K=8, h=2, g=2, a=4, b=14),  # prior P4c
    # n = 32, rate 1/4, h = 3 > m -- the OFFICIAL row's core shape (A-m=K+1)
    "Q7": dict(n=32, q=97, m=2, K=8, h=3, g=1, a=5, b=15),   # prior P3
    "Q8": dict(n=32, q=193, m=2, K=8, h=3, g=1, a=5, b=15),  # new
    # n = 32, rate 1/2 -- deepest competition reachable at n = 32
    "Q9": dict(n=32, q=97, m=2, K=16, h=2, g=2, a=8, b=14),   # prior P7
    "Q10": dict(n=32, q=97, m=2, K=16, h=3, g=1, a=9, b=15),  # prior P6
    "Q12": dict(n=32, q=193, m=2, K=16, h=2, g=2, a=8, b=14),  # new
    # n = 32, m = 4 = the OFFICIAL RowC 1/4 fibre width, h = 5 > m.
    # Structurally closest to the F_12289 fixture; no competition (control).
    "Q11": dict(n=32, q=97, m=4, K=8, h=5, g=1, a=3, b=7),    # prior P5
}

PRIOR_OF = {"Q1": "P2", "Q3": "P1", "Q4": "P4", "Q5": "P4b", "Q6": "P4c",
            "Q7": "P3", "Q9": "P7", "Q10": "P6", "Q11": "P5"}

HASH_SEEDS = (b"pb-null-01", b"pb-null-02")


# ---------------------------------------------------------------------------
# half-mask tables
# ---------------------------------------------------------------------------
def build_half(vals, gidx, H, q, n, rank, evalpts, omega):
    """Tables over subsets of one half of D.

    Returns dict of arrays indexed by the local mask.  Every entry is an
    additive/multiplicative statistic of the subset, so the two halves
    combine in O(1).
    """
    L = len(vals)
    N = 1 << L
    size = [0] * N
    sig = [0] * N                      # sum of global exponents mod n
    iso = [0] * N                      # sum of x^-1  (for e_{A-1})
    ps = [[0] * N for _ in range(H + 1)]
    rev = [0] * N                      # bit i -> bit n-1-i
    vperm = [0] * N                    # bit i -> bit rank[i]
    rvperm = [0] * N                   # bit i -> bit n-1-rank[i]
    powv = [[pow(v, j, q) for j in range(H + 1)] for v in vals]
    invv = [pow(v, q - 2, q) for v in vals]
    gg = P.primitive_root(q)
    dlog = {}
    acc = 1
    for e in range(q - 1):
        dlog[acc] = e
        acc = (acc * gg) % q
    # per evaluation point: #zero factors and sum of dlog(pt - x_i)
    zcs, sls, dls, zfs = [], [], [], []
    for pt in evalpts:
        dl, zf = [], []
        for v in vals:
            d = (pt - v) % q
            zf.append(1 if d == 0 else 0)
            dl.append(0 if d == 0 else dlog[d])
        dls.append(dl)
        zfs.append(zf)
        zcs.append([0] * N)
        sls.append([0] * N)
    for mask in range(1, N):
        low = mask & -mask
        i = low.bit_length() - 1
        rest = mask ^ low
        size[mask] = size[rest] + 1
        sig[mask] = (sig[rest] + gidx[i]) % n
        iso[mask] = (iso[rest] + invv[i]) % q
        pv = powv[i]
        for j in range(1, H + 1):
            ps[j][mask] = (ps[j][rest] + pv[j]) % q
        rev[mask] = rev[rest] | (1 << (n - 1 - gidx[i]))
        vperm[mask] = vperm[rest] | (1 << rank[gidx[i]])
        rvperm[mask] = rvperm[rest] | (1 << (n - 1 - rank[gidx[i]]))
        for t in range(len(evalpts)):
            zcs[t][mask] = zcs[t][rest] + zfs[t][i]
            sls[t][mask] = (sls[t][rest] + dls[t][i]) % (q - 1)
    return dict(size=size, sig=sig, iso=iso, ps=ps, rev=rev, vperm=vperm,
                rvperm=rvperm, zc=zcs, sl=sls, gg=gg)


# ---------------------------------------------------------------------------
# exact witness polynomial / codeword
# ---------------------------------------------------------------------------
class PolyCtx:
    def __init__(self, case):
        self.case = case
        self.fz = {}

    def f(self, z):
        v = self.fz.get(z)
        if v is None:
            v = P.padd(self.case.U, P.pscal(self.case.V, z, self.case.q),
                       self.case.q)
            self.fz[z] = v
        return v

    def coeffs(self, z, mask):
        """the K coefficients of the witness polynomial, low-to-high."""
        c = self.case
        loc = P.locator([c.D[i] for i in P.idx_of(mask, c.n)], c.q)
        p = P.padd(self.f(z), P.pneg(loc, c.q), c.q)
        assert P.deg(p) < c.K, (z, mask, P.deg(p))
        return [(p[i] if i < len(p) else 0) for i in range(c.K)]

    def codeword(self, z, mask):
        c = self.case
        p = self.coeffs(z, mask)
        return tuple(P.peval(p, x, c.q) for x in c.D)


def centred(v, q):
    return v if 2 * v <= q - 1 else v - q


# ---------------------------------------------------------------------------
# STAGE 1 : exhaustive first-match selection over a slope range
# ---------------------------------------------------------------------------
def stage_select(name, zlo, zhi, outdir):
    prm = dict(CASES[name])
    case = P.Case(name, dict(prm))
    case.build_family()
    q, n, m, K, h, A = case.q, case.n, case.m, case.K, case.h, case.A
    D, U, V = case.D, case.U, case.V
    ALLN = (1 << n) - 1
    H = h + 2                     # power sums needed: p_1..p_{h+2}

    order_vals = sorted(range(n), key=lambda i: D[i])
    rank = [0] * n
    for r, i in enumerate(order_vals):
        rank[i] = r

    L1 = n // 2
    evalpts = [D[0], D[1]]
    T1 = build_half(D[:L1], list(range(L1)), H, q, n, rank, evalpts,
                    case.omega)
    T2 = build_half(D[L1:], list(range(L1, n)), H, q, n, rank, evalpts,
                    case.omega)

    # --- alpha/beta and slope-free targets -------------------------------
    alpha = [0] * (h + 3)
    beta = [0] * (h + 3)
    for j in range(1, h + 1):
        t = A - j
        alpha[j] = U[t] if 0 <= t < len(U) else 0
        beta[j] = V[t] if 0 <= t < len(V) else 0
    assert all(beta[j] % q == 0 for j in range(1, m)), beta
    assert beta[m] % q != 0, beta
    inv_beta_m = pow(beta[m] % q, q - 2, q)
    sgn_m = 1 if m % 2 == 0 else -1

    e_free = [0] * (m + 1)
    for j in range(1, m):
        e_free[j] = (((-1) ** j) * alpha[j]) % q
    p_free = ([0, 0] if m == 1
              else P.newton_power_sums(e_free, m - 1, q))

    invj = [0] * (H + 1)
    for j in range(1, H + 1):
        invj[j] = pow(j % q, q - 2, q)

    sgnA = 1 if A % 2 == 0 else -1
    sgnA1 = 1 if (A - 1) % 2 == 0 else -1
    sgnH1 = 1 if (h + 1) % 2 == 0 else -1
    sgnH2 = 1 if (h + 2) % 2 == 0 else -1
    powom = [pow(case.omega, t, q) for t in range(n)]
    gg = T1["gg"]
    powg = [1] * (q - 1)
    for t in range(1, q - 1):
        powg[t] = (powg[t - 1] * gg) % q

    def fzc(z, t):
        return ((U[t] if 0 <= t < len(U) else 0)
                + z * (V[t] if 0 <= t < len(V) else 0)) % q

    fz0 = [fzc(z, 0) for z in range(q)]
    fz1 = [fzc(z, 1) for z in range(q)]
    fzKa = [fzc(z, K - 1) for z in range(q)]
    fzKb = [fzc(z, K - 2) for z in range(q)]
    fzx0 = [(P.peval(U, D[0], q) + z * P.peval(V, D[0], q)) % q
            for z in range(q)]
    fzx1 = [(P.peval(U, D[1], q) + z * P.peval(V, D[1], q)) % q
            for z in range(q)]

    s1, ps1, sig1, iso1 = T1["size"], T1["ps"], T1["sig"], T1["iso"]
    s2, ps2, sig2, iso2 = T2["size"], T2["ps"], T2["sig"], T2["iso"]
    rev1, rev2 = T1["rev"], T2["rev"]
    vp1, vp2 = T1["vperm"], T2["vperm"]
    rvp1, rvp2 = T1["rvperm"], T2["rvperm"]
    zcA1, zcA2 = T1["zc"][0], T2["zc"][0]
    slA1, slA2 = T1["sl"][0], T2["sl"][0]
    zcB1, zcB2 = T1["zc"][1], T2["zc"][1]
    slB1, slB2 = T1["sl"][1], T2["sl"][1]

    table = {}
    for mask in range(1 << L1):
        sz = s1[mask]
        if sz > A:
            continue
        k = sz
        for j in range(1, m):
            k = k * q + ps1[j][mask]
        table.setdefault(k, []).append(mask)

    # ---------------------------------------------------------------
    # generator of every exact-A witness, exactly once
    # ---------------------------------------------------------------
    def pairs():
        rng = range(1, h + 1)
        rng2 = range(m + 1, h + 1)
        for m2 in range(1 << (n - L1)):
            sz2 = s2[m2]
            need = A - sz2
            if need < 0 or need > L1:
                continue
            k = need
            for j in range(1, m):
                k = k * q + (p_free[j] - ps2[j][m2]) % q
            bucket = table.get(k)
            if not bucket:
                continue
            r2 = [ps2[j][m2] for j in range(H + 1)]
            for m1 in bucket:
                r1 = ps1
                pw = [0] * (H + 1)
                for j in rng:
                    pw[j] = (r2[j] + r1[j][m1]) % q
                e = [0] * (H + 1)
                e[0] = 1
                for j in rng:
                    s = 0
                    for i in range(1, j + 1):
                        t = e[j - i] * pw[i]
                        s = s + t if (i & 1) else s - t
                    e[j] = (s * invj[j]) % q
                z = ((sgn_m * e[m] - alpha[m]) * inv_beta_m) % q
                ok = True
                for j in rng2:
                    if e[j] != (((-1) ** j) * (alpha[j] + z * beta[j])) % q:
                        ok = False
                        break
                if not ok:
                    continue
                for j in (h + 1, h + 2):
                    pw[j] = (r2[j] + r1[j][m1]) % q
                    s = 0
                    for i in range(1, j + 1):
                        t = e[j - i] * pw[i]
                        s = s + t if (i & 1) else s - t
                    e[j] = (s * invj[j]) % q
                yield z, m1, m2, e[h + 1], e[h + 2]

    # --- accumulators -----------------------------------------------------
    bk = {o: [None] * q for o in EXACT_ORDERS}
    bm = {o: [0] * q for o in EXACT_ORDERS}
    ck = {o: [None] * q for o in PREF_ORDERS}
    sv = {o: [None] * q for o in PREF_ORDERS}
    deg2 = [None] * q      # (lexkey, mask) best among deg p == K-2
    deeper = [None] * q    # masks with p[K-1] == p[K-2] == 0
    count = [0] * q
    total = 0

    intended = {c["z"]: c["mask"] for c in case.cand}
    seen_intended = set()
    qm1 = q - 1
    bl2 = hashlib.blake2b
    seed1, seed2 = HASH_SEEDS
    svP, svC, svH, svW = (sv["ORD-POLYLEX"], sv["ORD-POLYCENT"],
                          sv["ORD-POLYHI"], sv["ORD-CODEWORD"])
    ckP, ckC, ckH, ckW = (ck["ORD-POLYLEX"], ck["ORD-POLYCENT"],
                          ck["ORD-POLYHI"], ck["ORD-CODEWORD"])
    bkL, bmL = bk["ORD-LEX"], bm["ORD-LEX"]
    bkE, bmE = bk["ORD-ERRLEX"], bm["ORD-ERRLEX"]
    bkC, bmC = bk["ORD-COLEX"], bm["ORD-COLEX"]
    bkV, bmV = bk["ORD-VALEX"], bm["ORD-VALEX"]
    bkX, bmX = bk["ORD-VALCOLEX"], bm["ORD-VALCOLEX"]
    bkH1, bmH1 = bk["ORD-HASH-pb-null-01"], bm["ORD-HASH-pb-null-01"]
    bkH2, bmH2 = bk["ORD-HASH-pb-null-02"], bm["ORD-HASH-pb-null-02"]

    for z, m1, m2, ehi1, ehi2 in pairs():
        count[z] += 1
        total += 1
        if z < zlo or z >= zhi:
            continue
        mask = m1 | (m2 << L1)
        if intended.get(z) == mask:
            seen_intended.add(z)

        # ---- exact-key support orders ----
        rb = rev1[m1] | rev2[m2]
        key = ALLN ^ rb
        cur = bkL[z]
        if cur is None or key < cur:
            bkL[z] = key
            bmL[z] = mask
        cur = bkE[z]
        if cur is None or rb < cur:
            bkE[z] = rb
            bmE[z] = mask
        cur = bkC[z]
        if cur is None or mask < cur:
            bkC[z] = mask
            bmC[z] = mask
        vpm = vp1[m1] | vp2[m2]
        cur = bkX[z]
        if cur is None or vpm < cur:
            bkX[z] = vpm
            bmX[z] = mask
        key2 = ALLN ^ (rvp1[m1] | rvp2[m2])
        cur = bkV[z]
        if cur is None or key2 < cur:
            bkV[z] = key2
            bmV[z] = mask
        mb = mask.to_bytes(8, "little")
        hk = bl2(mb, digest_size=16, key=seed1).digest()
        cur = bkH1[z]
        if cur is None or hk < cur:
            bkH1[z] = hk
            bmH1[z] = mask
        hk = bl2(mb, digest_size=16, key=seed2).digest()
        cur = bkH2[z]
        if cur is None or hk < cur:
            bkH2[z] = hk
            bmH2[z] = mask

        # ---- polynomial-keyed orders: exact 2-coefficient cheap prefix ----
        eA = powom[(sig1[m1] + sig2[m2]) % n]
        eA1 = (eA * (iso1[m1] + iso2[m2])) % q
        p0 = (fz0[z] - sgnA * eA) % q
        p1 = (fz1[z] - sgnA1 * eA1) % q
        kk = (p0, p1)
        cur = ckP[z]
        if cur is None or kk < cur:
            ckP[z] = kk
            svP[z] = [mask]
        elif kk == cur:
            svP[z].append(mask)
        kk = (p0 if 2 * p0 <= qm1 else p0 - q,
              p1 if 2 * p1 <= qm1 else p1 - q)
        cur = ckC[z]
        if cur is None or kk < cur:
            ckC[z] = kk
            svC[z] = [mask]
        elif kk == cur:
            svC[z].append(mask)
        pa = (fzKa[z] - sgnH1 * ehi1) % q
        pb = (fzKb[z] - sgnH2 * ehi2) % q
        kk = (pa, pb)
        cur = ckH[z]
        if cur is None or kk < cur:
            ckH[z] = kk
            svH[z] = [mask]
        elif kk == cur:
            svH[z].append(mask)
        # ---- ORD-DEGLEX bookkeeping (deg p = K-1 unless pa == 0) ----
        if pa == 0:
            if pb == 0:
                if deeper[z] is None:
                    deeper[z] = [mask]
                else:
                    deeper[z].append(mask)
            else:
                cur = deg2[z]
                if cur is None or key < cur[0]:
                    deg2[z] = (key, mask)
        # ---- codeword order: exact 2-coordinate cheap prefix ----
        if zcA1[m1] + zcA2[m2]:
            v0 = fzx0[z]
        else:
            v0 = (fzx0[z] - powg[(slA1[m1] + slA2[m2]) % qm1]) % q
        if zcB1[m1] + zcB2[m2]:
            v1 = fzx1[z]
        else:
            v1 = (fzx1[z] - powg[(slB1[m1] + slB2[m2]) % qm1]) % q
        kk = (v0, v1)
        cur = ckW[z]
        if cur is None or kk < cur:
            ckW[z] = kk
            svW[z] = [mask]
        elif kk == cur:
            svW[z].append(mask)

    # --- resolve prefilter orders exactly on their survivor sets ----------
    ctx = PolyCtx(case)
    selected = {o: {} for o in ALL_ORDERS}
    survivor_sizes = {o: [] for o in PREF_ORDERS}
    for o in EXACT_ORDERS:
        for z in range(zlo, zhi):
            if bk[o][z] is not None:
                selected[o][z] = bm[o][z]
    for z in range(zlo, zhi):
        if count[z] == 0:
            continue
        for o in PREF_ORDERS:
            cand = sv[o][z]
            survivor_sizes[o].append(len(cand))
            if len(cand) == 1:
                selected[o][z] = cand[0]
                continue
            best = None
            bestm = None
            for msk in cand:
                if o == "ORD-CODEWORD":
                    key = ctx.codeword(z, msk)
                else:
                    c = ctx.coeffs(z, msk)
                    if o == "ORD-POLYLEX":
                        key = tuple(c)
                    elif o == "ORD-POLYHI":
                        key = tuple(reversed(c))
                    else:
                        key = tuple(centred(v, q) for v in c)
                if best is None or key < best:
                    best = key
                    bestm = msk
            selected[o][z] = bestm
        # ---- ORD-DEGLEX ----
        if deeper[z]:
            best = None
            bestm = None
            for msk in deeper[z]:
                c = ctx.coeffs(z, msk)
                d = P.deg(c) if any(c) else -1
                kk = (d, ALLN ^ (T1["rev"][msk & ((1 << L1) - 1)]
                                 | T2["rev"][msk >> L1]))
                if best is None or kk < best:
                    best = kk
                    bestm = msk
            selected["ORD-DEGLEX"][z] = bestm
        elif deg2[z] is not None:
            selected["ORD-DEGLEX"][z] = deg2[z][1]
        else:
            selected["ORD-DEGLEX"][z] = selected["ORD-LEX"][z]
        # ---- ORD-SLOPEMAJOR (degenerate: leading key constant on W_z) ----
        selected["ORD-SLOPEMAJOR"][z] = selected["ORD-POLYLEX"][z]

    out = dict(
        case=name, zlo=zlo, zhi=zhi,
        parameters=dict(n=n, q=q, m=m, K=K, h=h, A=A, g=case.g, a=case.a,
                        b=case.b, rate=f"{K}/{n}", omega=case.omega,
                        core_indices=case.core_idx),
        checks=[dict(tag=t, ok=o, detail=d) for t, o, d in case.checks],
        total_witnesses_all_slopes=total,
        per_slope_counts={str(z): count[z] for z in range(q) if count[z]},
        intended_found_in_range=sorted(seen_intended),
        survivor_max={o: (max(survivor_sizes[o]) if survivor_sizes[o] else 0)
                      for o in PREF_ORDERS},
        survivor_total={o: sum(survivor_sizes[o]) for o in PREF_ORDERS},
        selected={o: {str(z): msk for z, msk in selected[o].items()}
                  for o in ALL_ORDERS},
    )
    path = os.path.join(outdir, f"sel_{name}_{zlo}_{zhi}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, sort_keys=True)
    live = sum(1 for z in range(q) if count[z])
    print(f"[select {name}] z in [{zlo},{zhi}) witnesses(all slopes)={total} "
          f"live(all)={live} survmax={out['survivor_max']} -> {path}")
    return out


# ---------------------------------------------------------------------------
# STAGE 2 : family statistics, budget, classification, K1 verdict
# ---------------------------------------------------------------------------
def classify(retention, sidon):
    if retention >= Fraction(9, 10):
        return ("SIDON-SUPER" if sidon else "HIGH-RETENTION"), "RED"
    if retention <= Fraction(1, 10):
        return "SUPPORT-COLLAPSED", "GREEN"
    return "MIXED", "AMBER"


def stage_stats(name, outdir):
    prm = dict(CASES[name])
    case = P.Case(name, dict(prm))
    case.build_family()
    q, n, K, A = case.q, case.n, case.K, case.A
    parts = []
    for fn in sorted(os.listdir(outdir)):
        if fn.startswith(f"sel_{name}_") and fn.endswith(".json"):
            with open(os.path.join(outdir, fn)) as fh:
                parts.append(json.load(fh))
    if not parts:
        raise SystemExit(f"no sel_{name}_*.json in {outdir}")
    counts = {}
    for p in parts:
        for zs, c in p["per_slope_counts"].items():
            counts[int(zs)] = c
    live = sorted(counts)
    total = parts[0]["total_witnesses_all_slopes"]
    covered = set()
    for p in parts:
        covered |= set(range(p["zlo"], p["zhi"]))
    missing = [z for z in live if z not in covered]
    if missing:
        raise SystemExit(f"slopes not covered by any chunk: {missing[:10]}")

    sel = {o: {} for o in ALL_ORDERS}
    for p in parts:
        for o, d in p["selected"].items():
            for zs, msk in d.items():
                sel[o][int(zs)] = msk
    for o in ALL_ORDERS:
        assert sorted(sel[o]) == live, (o, len(sel[o]), len(live))

    intended = {c["z"]: c["mask"] for c in case.cand}
    budget = 8 * n ** 3
    cand_masks = [c["mask"] for c in case.cand]
    cand_stats = dict(size=len(cand_masks), slopes=[c["z"] for c in case.cand],
                      supports=[c["support"] for c in case.cand],
                      **P.diff_stats(cand_masks),
                      **P.intersection_stats(cand_masks, K),
                      **P.prefix_stats(cand_masks, n, A - case.h))
    cand_stats["budget_ratio"] = f"{cand_stats['gamma_lo_size']}/{budget}"

    orders = {}
    for o in ALL_ORDERS:
        masks = [sel[o][z] for z in live]
        ds = P.diff_stats(masks)
        iss = P.intersection_stats(masks, K)
        ps_ = P.prefix_stats(masks, n, A - case.h)
        glo = iss["gamma_lo_size"]
        retention = Fraction(glo, len(live))
        cls, verdict = classify(retention, ds["sidon"])
        cf_masks = [intended[z] if z in intended else sel[o][z] for z in live]
        cf_is = P.intersection_stats(cf_masks, K)
        cf_lo_cand = 0
        for z in sorted(intended):
            msk = intended[z]
            worst = max((P.popcount(msk & other)
                         for w, other in zip(live, cf_masks) if w != z),
                        default=0)
            if worst <= K - 1:
                cf_lo_cand += 1
        restricted = [sel[o][z] for z in sorted(intended)]
        orders[o] = dict(
            spec=ORDER_SPEC[o],
            live_slopes=len(live),
            distinct_selected_supports=len(set(masks)),
            gamma_lo_size=glo,
            gamma_hi_size=iss["gamma_hi_size"],
            retention=f"{glo}/{len(live)}",
            retention_float=float(retention),
            budget_8n3=budget,
            budget_ratio=f"{glo}/{budget}",
            budget_ratio_float=float(Fraction(glo, budget)),
            budget_violated=glo > budget,
            selected_class=cls,
            k1_verdict=verdict,
            sidon=ds["sidon"],
            max_multiplicity=ds["max_multiplicity"],
            distinct_differences=ds["distinct_differences"],
            additive_energy=ds["additive_energy"],
            max_pairwise_intersection=iss["max_pairwise_intersection"],
            greedy_lowcore_subfamily=iss["greedy_lowcore_subfamily"],
            unallocated_slopes_bridge_gap=iss["unallocated_slopes_bridge_gap"],
            pairs_core_eq_K=iss["pairs_core_eq_K"],
            pairs_core_above_K=iss["pairs_core_above_K"],
            common_prefix_len=ps_["common_prefix_len"],
            common_coordinates=ps_["common_coordinates"],
            window_width=ps_["window_width"],
            intended_is_first_match=sum(1 for z in intended
                                        if sel[o].get(z) == intended[z]),
            candidate_family_size=len(intended),
            restricted_to_candidate_slopes=dict(
                **P.diff_stats(restricted),
                **P.intersection_stats(restricted, K)),
            counterfactual_intended_normative=dict(
                **P.diff_stats(cf_masks), **cf_is,
                candidate_slopes_in_gamma_lo=cf_lo_cand),
            selected_masks={str(z): sel[o][z] for z in live},
            example_selected_supports=[P.idx_of(sel[o][z], n)
                                       for z in live[:6]],
        )

    # slope-major degeneracy check
    degen = all(sel["ORD-SLOPEMAJOR"][z] == sel["ORD-POLYLEX"][z]
                for z in live)
    # errlex == reverse of lex check (selected mask must be the lex-MAX)
    checks_extra = dict(slopemajor_equals_polylex=degen)

    # cross-check against the prior pilot
    cross = None
    pn = PRIOR_OF.get(name)
    if pn:
        ppath = os.path.join(_PRIOR, f"results_{pn}.json")
        if os.path.exists(ppath):
            with open(ppath) as fh:
                prior = json.load(fh)
            wc = prior["witness_census"]
            cross = dict(prior_case=pn,
                         total_match=(wc["total_exact_A_witnesses"] == total),
                         prior_total=wc["total_exact_A_witnesses"],
                         our_total=total,
                         live_match=(wc["live_slopes"] == len(live)),
                         per_slope_match=(
                             {int(k): v for k, v
                              in wc["per_slope_counts"].items()} == counts),
                         orders={})
            for o, st in prior["selected_family"].items():
                if o not in orders:
                    continue
                ours = orders[o]
                cross["orders"][o] = dict(
                    gamma_lo=(st["gamma_lo_size"], ours["gamma_lo_size"],
                              st["gamma_lo_size"] == ours["gamma_lo_size"]),
                    sidon=(st["sidon"], ours["sidon"],
                           st["sidon"] == ours["sidon"]),
                    maxmult=(st["max_multiplicity"], ours["max_multiplicity"],
                             st["max_multiplicity"]
                             == ours["max_multiplicity"]),
                    prefix=(st["common_prefix_len"], ours["common_prefix_len"],
                            st["common_prefix_len"]
                            == ours["common_prefix_len"]),
                    examples=(st["example_selected_supports"]
                              == ours["example_selected_supports"]),
                )

    out = dict(
        case=name,
        parameters=parts[0]["parameters"],
        checks_total=len(parts[0]["checks"]),
        checks_all_pass=all(c["ok"] for c in parts[0]["checks"]),
        witness_census=dict(
            total_exact_A_witnesses=total,
            live_slopes=len(live),
            dead_slopes=q - len(live),
            min_witnesses_per_live_slope=min(counts.values()),
            max_witnesses_per_live_slope=max(counts.values()),
            mean_per_live_slope=f"{total}/{len(live)}",
            per_slope_counts={str(z): counts[z] for z in live},
        ),
        budget=dict(budget_8n3=budget, n_squared=n * n,
                    max_possible_gamma_lo=len(live),
                    budget_testable=len(live) > budget),
        candidate_family=cand_stats,
        extra_checks=checks_extra,
        orders=orders,
        prior_crosscheck=cross,
    )
    path = os.path.join(outdir, f"k1_{name}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(f"[stats {name}] live={len(live)} total={total} budget={budget}")
    for o in ALL_ORDERS:
        s = orders[o]
        print(f"   {o:22s} Glo={s['gamma_lo_size']:4d}/{s['live_slopes']:<4d}"
              f" ({s['retention_float']:.3f})  {s['selected_class']:18s}"
              f" K1={s['k1_verdict']:5s} sidon={str(s['sidon']):5s}"
              f" maxmult={s['max_multiplicity']:3d}"
              f" maxcore={s['max_pairwise_intersection']:3d}"
              f" prefix={s['common_prefix_len']}")
    if cross:
        bad = [k for k, v in cross["orders"].items()
               if not all(x[-1] for x in v.values() if isinstance(x, tuple))
               or not v["examples"]]
        print(f"   prior {cross['prior_case']}: total={cross['total_match']} "
              f"live={cross['live_match']} perslope="
              f"{cross['per_slope_match']} order-mismatches={bad}")
    print(f"   -> {path}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["select", "stats"])
    ap.add_argument("case")
    ap.add_argument("--zlo", type=int, default=0)
    ap.add_argument("--zhi", type=int, default=-1)
    ap.add_argument("--outdir", default=_HERE)
    args = ap.parse_args()
    if args.stage == "select":
        zhi = args.zhi if args.zhi >= 0 else CASES[args.case]["q"]
        stage_select(args.case, args.zlo, zhi, args.outdir)
    else:
        stage_stats(args.case, args.outdir)


if __name__ == "__main__":
    main()
