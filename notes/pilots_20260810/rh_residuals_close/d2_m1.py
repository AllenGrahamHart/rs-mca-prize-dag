#!/usr/bin/env python3
"""d2_m1.py -- rh_residuals_close (round 32), DELIVERABLE D2.

EXHAUSTIVE census of the m = 1 failure configurations (T = rho+2 = 5), by a
route INDEPENDENT of the banked node
  background/nodes/rate_half_ca_hankel_strict_m1_corefree_five_slope_route_fence
(which censuses monic split cubic LOCATORS on core-free affine coefficient
lines; this script censuses SUPPORT CONFIGURATIONS directly).

Profile: m=1 => N=16, R=8, R+1=9, rho=3, e=1, A=3.  D = mu_16 <= F_q^*.
Code K = ker H, H_{t,x} = x^t (t=0..7): [16,8,9] MDS, so the shortened code
on any 9-set Z is 1-dimensional and spanned by (1/sigma'_Z(x))_{x in Z}.

Search.  d_x <= e = 1 (SAT2, banked) forces the five locator sets to be
PAIRWISE DISJOINT triples.  Fix S_1, S_2; put W = S_1 u S_2 (|W| = 6).  For
any further triple S disjoint from W, kappa_S := alpha v_1 + beta v_2 - v_S
is a nonzero codeword supported on Z = W u S (|Z| = 9), hence
kappa_S = lambda/sigma'_Z, hence
   v_1 prop (1/(sigma'_W(x) sigma_S(x)))_{x in S_1},
   v_2 prop (1/(sigma'_W(x) sigma_S(x)))_{x in S_2}.
So five slopes are simultaneously supported IFF three pairwise-disjoint
candidates S share the SAME pair of normalized restrictions -- a key match.
sigma'_W is a common factor, so the key uses sigma_S alone.

Symmetry: x -> zeta*x preserves D and the code up to a diagonal syndrome
change, so S_1 may be restricted to orbit representatives (35 of the 560).

usage:  python3 d2_m1.py Q
stdlib only.
"""
import sys
from itertools import combinations

q = int(sys.argv[1]) if len(sys.argv) > 1 else 17
assert (q - 1) % 16 == 0, q
N, RHO, RR = 16, 3, 8            # |D|, locator size, number of syndromes
out = []
P = out.append


def gen(q):
    for c in range(2, q):
        x, k = c, 1
        while x != 1:
            x = x * c % q
            k += 1
        if k == q - 1:
            return c
    raise RuntimeError


g = gen(q)
zeta = pow(g, (q - 1) // 16, q)
D = []
x = 1
for _ in range(16):
    D.append(x)
    x = x * zeta % q
assert len(set(D)) == 16
inv = [0] * q
for i in range(1, q):
    inv[i] = pow(i, q - 2, q)

TRIPLES = list(combinations(range(16), 3))          # indices into D


def orbit_reps():
    seen, reps = set(), []
    for T in TRIPLES:
        if T in seen:
            continue
        reps.append(T)
        for k in range(16):
            seen.add(tuple(sorted((i + k) % 16 for i in T)))
    return reps


REPS = orbit_reps()


def sig(S, i):
    """sigma_S(D[i]) = prod_{j in S} (D[i]-D[j])"""
    r = 1
    xi = D[i]
    for j in S:
        r = r * (xi - D[j]) % q
    return r


def key_on(S, T):
    """normalized (sigma_S(x))_{x in T}, T a triple"""
    a, b, c = (sig(S, i) for i in T)
    if a == 0:
        return None
    ia = inv[a]
    return (1, b * ia % q, c * ia % q)


# ---------------- exhaustive search ----------------
configs = set()
pairs_scanned = 0
for S1 in REPS:
    rest1 = [i for i in range(16) if i not in S1]
    for S2 in combinations(rest1, 3):
        pairs_scanned += 1
        free = [i for i in rest1 if i not in S2]          # 10 points
        buckets = {}
        for S in combinations(free, 3):
            k1 = key_on(S, S1)
            k2 = key_on(S, S2)
            if k1 is None or k2 is None:
                continue
            buckets.setdefault((k1, k2), []).append(S)
        for k, lst in buckets.items():
            if len(lst) < 3:
                continue
            for tri in combinations(lst, 3):
                a, b, c = (set(t) for t in tri)
                if a & b or a & c or b & c:
                    continue
                configs.add(frozenset([S1, S2] + [tuple(t) for t in tri]))

P("=" * 74)
P("D2  m = 1 EXHAUSTIVE support-configuration census   q = %d" % q)
P("=" * 74)
P("  D = mu_16 = %s" % D)
P("  S_1 orbit representatives: %d (of %d triples)" % (len(REPS), len(TRIPLES)))
P("  (S_1,S_2) pairs scanned  : %d" % pairs_scanned)
P("  candidate triples per pair: %d" % len(list(combinations(range(10), 3))))
P("  RAW configurations found (up to the zeta-shift symmetry): %d" % len(configs))

# ---------------- verification of each configuration ----------------


def syndrome(v):
    return tuple(sum(v[i] * pow(D[i], t, q) for i in range(16)) % q
                 for t in range(RR))


def solve_support(S, syn):
    """is there v supported on S with Hv = syn?  returns v or None."""
    rows = [[pow(D[i], t, q) for i in S] + [syn[t]] for t in range(RR)]
    n = len(S)
    piv = []
    r = 0
    for c in range(n):
        pr = None
        for rr in range(r, RR):
            if rows[rr][c]:
                pr = rr
                break
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        iv = inv[rows[r][c]]
        rows[r] = [z * iv % q for z in rows[r]]
        for rr in range(RR):
            if rr != r and rows[rr][c]:
                f = rows[rr][c]
                rows[rr] = [(rows[rr][t] - f * rows[r][t]) % q for t in range(n + 1)]
        piv.append(c)
        r += 1
    for rr in range(r, RR):
        if rows[rr][n]:
            return None
    v = [0] * n
    for idx, c in enumerate(piv):
        v[c] = rows[idx][n]
    return v


ALLSUB = [S for k in range(1, RHO + 1) for S in combinations(range(16), k)]


def full_slope_census(A, B):
    """all supported slopes of the pencil A + gamma B over P^1(F_q)."""
    sup = {}
    pts = [(1, gm) for gm in range(q)] + [(0, 1)]      # (1:gamma) and infinity
    for (u, w) in pts:
        syn = tuple((u * A[t] + w * B[t]) % q for t in range(RR))
        if not any(syn):
            sup[(u, w)] = ()
            continue
        for S in ALLSUB:
            v = solve_support(S, syn)
            if v is not None and all(v):
                sup[(u, w)] = S
                break
    return sup


P("")
P("  --- verification of every configuration found ---")
recs = []
for cfg in sorted(configs, key=lambda c: sorted(c)):
    tris = sorted(cfg)
    used = set()
    for t in tris:
        used |= set(t)
    omitted = sorted(set(range(16)) - used)
    # build v_1, v_2 from one of the codewords, then all five and check rank 2
    S1, S2 = tris[0], tris[1]
    W = tuple(sorted(set(S1) | set(S2)))
    S = tris[2]
    Z = tuple(sorted(set(W) | set(S)))
    kap = {}
    for i in Z:
        d = 1
        for j in Z:
            if j != i:
                d = d * (D[i] - D[j]) % q
        kap[i] = inv[d]
    v1 = [0] * 16
    for i in S1:
        v1[i] = kap[i]
    v2 = [0] * 16
    for i in S2:
        v2[i] = kap[i]
    A, B = syndrome(v1), syndrome(v2)
    sup = full_slope_census(A, B)
    supports = sorted(set(v for v in sup.values() if v))
    T = len(sup)
    ok_partition = (len(omitted) == 1)
    recs.append((tris, omitted, T, supports, ok_partition))

P("  configurations verified: %d" % len(recs))
Ts = {}
for r in recs:
    Ts[r[2]] = Ts.get(r[2], 0) + 1
P("  T histogram over configurations: %s" % dict(sorted(Ts.items())))
P("  every configuration omits exactly ONE domain point: %s"
  % all(r[4] for r in recs))
P("  omitted points (as field elements): %s"
  % sorted(D[r[1][0]] for r in recs if len(r[1]) == 1))
P("")
for tris, omitted, T, supports, okp in recs[:6]:
    P("  cfg omit=%s  T=%d" % ([D[i] for i in omitted], T))
    P("     supports (field elements): %s"
      % sorted(sorted(D[i] for i in t) for t in tris))
    P("     supported-slope supports found by full P^1 scan: %s"
      % sorted(sorted(D[i] for i in t) for t in supports))
P("")
P("  BANKED comparison (q=17 only), (M1F3) triples")
P("    {1,2,5} {3,7,11} {9,12,13} {4,6,16} {8,10,15}, omitting 14")
tgt = set(map(frozenset, [{1, 2, 5}, {3, 7, 11}, {9, 12, 13}, {4, 6, 16}, {8, 10, 15}]))
hit = False
for tris, omitted, T, supports, okp in recs:
    fs = set(frozenset(D[i] for i in t) for t in tris)
    if fs == tgt:
        hit = True
P("    (M1F3) found verbatim among my configurations: %s" % hit)
if not hit and q == 17:
    P("    NOTE: my census is up to the zeta-shift symmetry (S_1 restricted to")
    P("    35 orbit reps), so (M1F3) appears as a SHIFT of one of my configs.")
    orb = False
    for tris, omitted, T, supports, okp in recs:
        for k in range(16):
            fs = set(frozenset(D[(i + k) % 16] for i in t) for t in tris)
            if fs == tgt:
                orb = True
    P("    (M1F3) found as a zeta-shift of one of my configurations: %s" % orb)
P("")
P("  FULL ORBIT COUNT (configurations before quotienting by the 16 shifts):")
allcfg = set()
for cfg in configs:
    for k in range(16):
        allcfg.add(frozenset(tuple(sorted((i + k) % 16 for i in t)) for t in cfg))
P("    %d  (banked node claims exactly 16 five-lines at q=17, one per omitted point)"
  % len(allcfg))
oms = {}
for cfg in allcfg:
    used = set()
    for t in cfg:
        used |= set(t)
    o = tuple(sorted(set(range(16)) - used))
    oms[o] = oms.get(o, 0) + 1
P("    distinct omitted-point patterns: %d ; counts %s"
  % (len(oms), sorted(oms.values())))
P("    omitted points covered: %s" % sorted(D[o[0]] for o in oms if len(o) == 1))

print("\n".join(out))
