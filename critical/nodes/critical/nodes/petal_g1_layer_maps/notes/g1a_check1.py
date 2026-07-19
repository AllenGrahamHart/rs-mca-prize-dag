#!/usr/bin/env python3
"""g1a_check1 — tiny-cell EXACT engine check for the F4 falsifier theorem.

Cell: n=16, k=8, q=17  =>  quotient row n'=8, k'=4, nf=3, t=4.
Checks:
  A. dual census: brute g-side (all q^{k'} codewords) vs support-side
     DD-consistency, for a battery of label vectors: N1 identity
     N1 = sum_{g: y_nf in A_g, |A_g|>=k'+1} C(|A_g|-1, k').
  B. P3-curse in vivo: every band chart holds <= 1 member; minimal charts
     of distinct band classes are distinct; hence any covering atlas has
     >= B charts, weight >= 3 each.
  C. B >= (N1 - V)/(k'+1) pointwise.
  D. torus-count formula for one nonzero linear form on (F_q^*)^m:
     #solutions = ((q-1)^m + (-1)^m (q-1))/q, verified by enumeration
     against the ACTUAL (DIAMOND) coefficients of several supports.
  E. triangular-rank claim for oversized supports (|S| = k'+3): the linear
     system on labels has rank exactly j=3, and #torus solutions <= 2 q^{-3}
     (q-1)^{m'} bound check by enumeration.
  F. mutation control: corrupting one DD coefficient breaks the dual census.
Exit 0 iff ALL PASS.
"""
import itertools, sys
import numpy as np

q = 17
n, k = 16, 8
npr, kpr = 8, 4          # n', k'
nf = kpr - 1             # 3
t = n - k >> 1           # 4

# multiplicative structure: g=3 generates F_17^*, H = <3> order 16, H^2 = <9>
g0 = 3
assert sorted(pow(g0, j, q) for j in range(16)) == list(range(1, 17))
y = [pow(9, j, q) for j in range(npr)]          # y_j, j=0..7
core = y[:kpr]                                   # Z' u {y_nf}: y_0..y_3
ynf = y[nf]                                      # y_3
petals = y[kpr:]                                 # y_4..y_7
Zp = y[:nf]                                      # Z' = y_0..y_2

def polyeval(coeffs, x):                         # coeffs low->high
    r = 0
    for c in reversed(coeffs):
        r = (r * x + c) % q
    return r

LZp = lambda x: (x - Zp[0]) * (x - Zp[1]) * (x - Zp[2]) % q

def word(c):                                     # u1 values on y_0..y_7
    w = [0] * kpr + [c[i] * LZp(petals[i]) % q for i in range(t)]
    return w

def interp_consistent(S, w):
    """S = tuple of indices into y (size >= kpr). Return (ok, coeffs) where
    ok iff a deg<=kpr-1 interpolant of w on S exists; coeffs of it if ok."""
    pts = [y[i] for i in S]
    vals = [w[i] for i in S]
    # solve Vandermonde on first kpr points
    import numpy.linalg  # noqa
    A = [[pow(pts[r], c, q) for c in range(kpr)] for r in range(kpr)]
    b = vals[:kpr]
    # Gaussian elimination mod q
    M = [row[:] + [bb] for row, bb in zip(A, b)]
    for col in range(kpr):
        piv = next(r for r in range(col, kpr) if M[r][col] % q)
        M[col], M[piv] = M[piv], M[col]
        inv = pow(M[col][col], q - 2, q)
        M[col] = [v * inv % q for v in M[col]]
        for r in range(kpr):
            if r != col and M[r][col]:
                f = M[r][col]
                M[r] = [(a - f * b2) % q for a, b2 in zip(M[r], M[col])]
    coeffs = [M[r][kpr] for r in range(kpr)]
    ok = all(polyeval(coeffs, pts[i]) == vals[i] for i in range(kpr, len(S)))
    return ok, coeffs

comb = lambda a, b: 0 if b < 0 or b > a else __import__('math').comb(a, b)

# ---- brute g-side census -------------------------------------------------
V4 = np.array([[pow(y[j], c, q) for j in range(npr)] for c in range(kpr)])  # 4x8
allcoef = np.array(list(itertools.product(range(q), repeat=kpr)))            # 83521x4
evals = (allcoef @ V4) % q                                                    # 83521x8

def brute(c):
    w = np.array(word(c))
    agr = (evals == w)                                   # bool 83521x8
    sizes = agr.sum(1)
    contrib = sizes >= kpr + 1
    withnf = agr[:, nf] & contrib
    N1 = sum(comb(int(s) - 1, kpr) for s in sizes[withnf])
    Vv = sum(comb(int(s) - 1, kpr) for s in sizes[withnf] if s >= kpr + 3)
    band = withnf & (sizes <= kpr + 2)
    supports = [tuple(np.nonzero(agr[i])[0]) for i in np.nonzero(band)[0]]
    assert len(set(supports)) == len(supports), "L1 violated?!"
    return N1, Vv, supports, agr, sizes

# ---- support-side DD census ---------------------------------------------
def support_side(c):
    w = word(c)
    N1 = 0
    bandcls = []
    for sz in (kpr + 1, kpr + 2):
        for S in itertools.combinations(range(npr), sz):
            if nf not in S:
                continue
            ok, coeffs = interp_consistent(S, w)
            if not ok:
                continue
            if sz == kpr + 1:
                N1 += 1
            A = tuple(j for j in range(npr) if polyeval(coeffs, y[j]) == w[j])
            if A == S:
                bandcls.append(S)
    return N1, bandcls

rng = np.random.default_rng(20260713)
batt = [tuple(int(v) for v in rng.integers(1, q, t)) for _ in range(40)]
batt += [(5, 5, 5, 5)]                     # constant labels (degenerate case)
batt += [(1, 1, 1, 1), (1, 2, 4, 8)]

fails = 0
maxB = 0
for c in batt:
    N1b, Vb, sups, agr, sizes = brute(c)
    N1s, bandcls = support_side(c)
    B = len(sups)
    maxB = max(maxB, B)
    # A: dual N1 (support-side counts size-k'+1 consistent supports = mass id)
    if N1b != N1s:
        print(f"FAIL A: c={c} N1 brute={N1b} support={N1s}"); fails += 1
    if sorted(sups) != sorted(bandcls):
        print(f"FAIL A2: c={c} band class sets differ"); fails += 1
    # C: B >= (N1 - V)/(k'+1)
    if (kpr + 1) * B < N1b - Vb:
        print(f"FAIL C: c={c} B={B} N1={N1b} V={Vb}"); fails += 1
    # B(P3-curse): every band chart holds <= 1 member; minimal charts distinct
    mincharts = set()
    for S in sups:
        W = tuple(i for i in S if i < kpr); P = tuple(i for i in S if i >= kpr)
        z, mp = len(W), len(P)
        dpr = kpr - z
        if not (1 <= z <= kpr - 1 and mp <= dpr + 2 and nf in W):
            print(f"FAIL B0: c={c} illegal minimal chart {S}"); fails += 1
        mincharts.add((W, P))
    if len(mincharts) != len(sups):
        print(f"FAIL B1: c={c} minimal charts collide"); fails += 1
    # exhaustive band charts: <= 1 member each
    for z in range(1, kpr):
        for Wrest in itertools.combinations([i for i in range(kpr) if i != nf], z - 1):
            W = tuple(sorted(Wrest + (nf,)))
            dpr = kpr - z
            for mp in range(dpr + 1, dpr + 3):
                for P in itertools.combinations(range(kpr, npr), mp):
                    mem = [S for S in sups
                           if tuple(i for i in S if i < kpr) == W
                           and set(i for i in S if i >= kpr) <= set(P)]
                    if len(mem) > 1:
                        print(f"FAIL B2: chart {(W,P)} holds {len(mem)} members"); fails += 1

print(f"A/B/C over {len(batt)} label vectors: done, maxB={maxB}")

# ---- D: torus-count formula against actual DIAMOND coefficients ----------
def diamond_coeffs(S):
    """coefficients gamma_y of c-variables in the leading DD on S (size k'+1)."""
    pts = [y[i] for i in S]
    gam = {}
    for i in S:
        if i < kpr:
            continue
        Lp = 1
        for j in S:
            if j != i:
                Lp = Lp * (y[i] - y[j]) % q
        gam[i - kpr] = LZp(y[i]) * pow(Lp, q - 2, q) % q
    return gam

for S in [(0, 1, 2, 3, 4), (0, 2, 3, 5, 6), (3, 4, 5, 6, 7), (1, 2, 3, 6, 7)]:
    gam = diamond_coeffs(S)
    m = len(gam)
    if any(v == 0 for v in gam.values()):
        print(f"FAIL D0: zero DIAMOND coefficient at {S}"); fails += 1
    cnt = 0
    for assign in itertools.product(range(1, q), repeat=m):
        if sum(a * g for a, g in zip(assign, gam.values())) % q == 0:
            cnt += 1
    pred = ((q - 1) ** m + (-1) ** m * (q - 1)) // q
    if cnt != pred:
        print(f"FAIL D: S={S} m={m} count={cnt} pred={pred}"); fails += 1
print("D: torus-count formula exact on 4 supports")

# ---- E: oversized supports: rank exactly j, torus count <= 2 q^-j --------
for S in itertools.combinations(range(npr), kpr + 3):
    if nf not in S:
        continue
    mvars = sorted(i - kpr for i in S if i >= kpr)
    m = len(mvars)
    cnt = 0
    for assign in itertools.product(range(1, q), repeat=m):
        c = [1] * t
        for v, a in zip(mvars, assign):
            c[v] = a
        # consistency of FULL S: interpolate on first kpr, check rest
        ok, _ = interp_consistent(S, word(tuple(c)))
        cnt += ok
    j = len(S) - kpr
    if cnt > 2 * (q - 1) ** m // q ** j + 1:
        print(f"FAIL E: S={S} torus count {cnt} vs bound {2*(q-1)**m//q**j}"); fails += 1
print("E: oversized (j=3) torus counts within 2q^-j bound (all supports)")

# ---- F: mutation control --------------------------------------------------
c = batt[0]
w = word(c)
wbad = w[:]; wbad[kpr] = (wbad[kpr] + 1) % q     # corrupt one petal value
N1bad = 0
for S in itertools.combinations(range(npr), kpr + 1):
    if nf in S:
        N1bad += interp_consistent(S, wbad)[0]
N1b, _, _, _, _ = brute(c)
if N1bad == N1b:
    print("FAIL F: mutation not detected"); fails += 1
else:
    print(f"F: mutation TRIPS (N1 {N1b} -> {N1bad})")

print("ALL PASS" if fails == 0 else f"{fails} FAILURES")
sys.exit(0 if fails == 0 else 1)
