"""D3 -- exact scaled census of the NON-MINIMUM-WEIGHT type-2 stratum.

Profile (SAT1): rho=4m-1, N=16m, R=8m, R+1=8m+1, e=m, A=3.
D = mu_N <= F_q^*, K = {c in F_q^D : sum_x c_x x^i = 0, i < R}, an
[N, N-R, R+1] MDS code.  A pencil is V = span(v_1,v_2); the joint support
is W; a supported slope gamma has a unique min-weight coset representative
v_gamma of weight <= rho (unique because 2rho = 8m-2 < R+1 = d(K)).
kappa_gamma = z_gamma - v_gamma in K; type-1 <=> kappa = 0.
p_gamma = |S_gamma \\ W|;  j_gamma = wt(kappa_gamma) - (R+1)  (the WEIGHT
EXCESS).  The mandate's stratum is {type-2 : j >= 1}.

KEY STRUCTURAL POINT used to build the census: w* = |W| is a MINIMUM joint
support, and for two supported slopes (v_i, v_j) is itself a representation
of the pair, so w* <= |S_i u S_j| <= 2rho.  Hence a = 8m-2 = 2rho forces
W = S_1 u S_2 with S_1, S_2 DISJOINT of full size rho.  We therefore build
pencils as span(v_1, v_2) with prescribed |S_1 ^ S_2| = 2rho - a.

usage:  d3_census.py m q  [ntrials_random] [ntrials_targeted]
"""

import random
import sys

m = int(sys.argv[1])
q = int(sys.argv[2])
NR = int(sys.argv[3]) if len(sys.argv) > 3 else 60
NT = int(sys.argv[4]) if len(sys.argv) > 4 else 20

rho, N, R = 4 * m - 1, 16 * m, 8 * m
R1 = R + 1
e = m
assert (q - 1) % N == 0, "need N | q-1"

OUT = []


def say(s=""):
    OUT.append(s)
    if len(OUT) % 40 == 0:                      # checkpoint
        sys.stderr.write(".")


def inv(x):
    return pow(x, q - 2, q)


# ---------------------------------------------------------------- domain
def primitive_root(q):
    fac, n = [], q - 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            fac.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        fac.append(n)
    for g in range(2, q):
        if all(pow(g, (q - 1) // f, q) != 1 for f in fac):
            return g
    raise RuntimeError


g = primitive_root(q)
w = pow(g, (q - 1) // N, q)
D = [pow(w, i, q) for i in range(N)]
assert len(set(D)) == N
IDX = {x: i for i, x in enumerate(D)}
POW = [[pow(x, i, q) for i in range(R)] for x in D]      # N x R


# ------------------------------------------------------- Berlekamp-Massey
def bm(s, cap):
    """shortest LFSR for s; returns (L, C) or (None,None) if L exceeds cap."""
    C = [1]
    B = [1]
    L, mm, b = 0, 1, 1
    for n in range(len(s)):
        d = s[n]
        for i in range(1, L + 1):
            if i < len(C):
                d = (d + C[i] * s[n - i]) % q
        d %= q
        if d == 0:
            mm += 1
        else:
            coef = d * inv(b) % q
            T = C[:]
            need = mm + len(B)
            if len(C) < need:
                C = C + [0] * (need - len(C))
            for i in range(len(B)):
                C[mm + i] = (C[mm + i] - coef * B[i]) % q
            if 2 * L <= n:
                L = n + 1 - L
                if L > cap:
                    return None, None
                B, b, mm = T, d, 1
            else:
                mm += 1
    return L, C


def polyval(C, x):
    r = 0
    for cco in reversed(C):
        r = (r * x + cco) % q
    return r


def decode(syn):
    """min-weight rep of the coset with syndrome syn; None if weight > rho."""
    L, C = bm(syn, rho)
    if L is None or L == 0:
        return [] if L == 0 else None
    S = [x for x in D if polyval(C, inv(x)) == 0]
    if len(S) != L:
        return None
    return S


def solve(A, bvec):
    """gaussian elimination over F_q; A is n x n (list of rows)."""
    n = len(A)
    M = [A[i][:] + [bvec[i]] for i in range(n)]
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c]), None)
        if piv is None:
            return None
        M[c], M[piv] = M[piv], M[c]
        ic = inv(M[c][c])
        M[c] = [v * ic % q for v in M[c]]
        for r in range(n):
            if r != c and M[r][c]:
                f = M[r][c]
                M[r] = [(M[r][k] - f * M[c][k]) % q for k in range(n + 1)]
    return [M[i][n] for i in range(n)]


def errvals(S, syn):
    A = [[pow(x, i, q) for x in S] for i in range(len(S))]
    return solve(A, syn[:len(S)])


def nullspace(M, ncols):
    """basis of the right nullspace of M over F_q."""
    M = [row[:] for row in M]
    nrows = len(M)
    piv_of, r = {}, 0
    for c in range(ncols):
        p = next((i for i in range(r, nrows) if M[i][c]), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        ic = inv(M[r][c])
        M[r] = [v * ic % q for v in M[r]]
        for i in range(nrows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][k] - f * M[r][k]) % q for k in range(ncols)]
        piv_of[c] = r
        r += 1
    basis = []
    for c in range(ncols):
        if c in piv_of:
            continue
        v = [0] * ncols
        v[c] = 1
        for pc, pr in piv_of.items():
            v[pc] = (-M[pr][c]) % q
        basis.append(v)
    return basis


def sigma_prime(Z, x):
    r = 1
    for y in Z:
        if y != x:
            r = r * (x - y) % q
    return r


def newton_degree(nodes, vals):
    """degree of the interpolating polynomial through (nodes, vals)."""
    n = len(nodes)
    dd = vals[:]
    for k in range(1, n):
        for i in range(n - 1, k - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) * inv(nodes[i] - nodes[i - k]) % q
    deg = -1
    for i in range(n):
        if dd[i]:
            deg = i
    return deg


# ------------------------------------------------------------ the analysis
def analyse(v1, v2):
    """v1,v2 are dicts x->val. returns per-slope records."""
    W = sorted(set(v1) | set(v2), key=lambda x: IDX[x])
    A = [0] * R
    B = [0] * R
    for x, val in v1.items():
        pw = POW[IDX[x]]
        for i in range(R):
            A[i] = (A[i] + val * pw[i]) % q
    for x, val in v2.items():
        pw = POW[IDX[x]]
        for i in range(R):
            B[i] = (B[i] + val * pw[i]) % q
    recs = []
    slopes = [("inf", None)] + [("f", gam) for gam in range(q)]
    for tag, gam in slopes:
        if tag == "inf":
            syn = B[:]
            zv = dict(v2)
        else:
            syn = [(A[i] + gam * B[i]) % q for i in range(R)]
            zv = {}
            for x in W:
                val = (v1.get(x, 0) + gam * v2.get(x, 0)) % q
                if val:
                    zv[x] = val
        S = decode(syn)
        if S is None:
            continue
        vv = dict(zip(S, errvals(S, syn))) if S else {}
        if any(val == 0 for val in vv.values()):
            continue                                   # not a genuine support
        kap = {}
        for x in set(zv) | set(vv):
            val = (zv.get(x, 0) - vv.get(x, 0)) % q
            if val:
                kap[x] = val
        Sset = set(S)
        Wset = set(W)
        p = len(Sset - Wset)
        typ = 1 if not kap else 2
        n_gam = sum(1 for x in W if zv.get(x, 0) == 0)
        n0 = len(Wset) - sum(1 for x in Wset if x in kap)
        j = (len(kap) - R1) if kap else None
        recs.append(dict(tag=tag, gam=gam, S=Sset, v=vv, z=zv, kap=kap,
                         p=p, typ=typ, n_gam=n_gam, n0=n0, j=j,
                         wt=len(kap), absS=len(Sset)))
    return W, recs


def gnf_check(rec):
    """kappa_x * sigma'_Z(x) should be a poly of degree <= |Z|-R-1 on Z."""
    Z = sorted(rec["kap"], key=lambda x: IDX[x])
    if len(Z) < 2:
        return None
    vals = [rec["kap"][x] * sigma_prime(Z, x) % q for x in Z]
    deg = newton_degree(Z, vals)
    return deg, len(Z) - R1


STATS = dict(cells=0, pencils=0, supported=0, t2=0, t2_eq=0, t2_gt=0,
             gnf_ok=0, gnf_bad=0, eq_fwd_ok=0, eq_fwd_bad=0,
             eq_bwd_ok=0, eq_bwd_bad=0, tr1_ok=0, tr1_bad=0, tr1_alt2=0,
             maxT=0, maxT2gt=0, wstar_bad=0)


def record(W, recs, jhist, phist, Thist, gnf_budget):
    STATS["pencils"] += 1
    T = len(recs)
    Thist[T] = Thist.get(T, 0) + 1
    STATS["maxT"] = max(STATS["maxT"], T)
    STATS["supported"] += T
    t2gt = 0
    for rc in recs:
        if rc["typ"] != 2:
            continue
        STATS["t2"] += 1
        phist[rc["p"]] = phist.get(rc["p"], 0) + 1
        jhist[rc["j"]] = jhist.get(rc["j"], 0) + 1
        if rc["j"] == 0:
            STATS["t2_eq"] += 1
        else:
            STATS["t2_gt"] += 1
            t2gt += 1
        # (EQ) forward: equality in (C2)  =>  j = 0
        c2_eq = (rc["p"] == R1 - len(W) + rc["n_gam"])
        if c2_eq:
            if rc["j"] == 0:
                STATS["eq_fwd_ok"] += 1
            else:
                STATS["eq_fwd_bad"] += 1
        # (EQ) backward: j = 0  =>  equality in (C2)
        if rc["j"] == 0:
            if c2_eq:
                STATS["eq_bwd_ok"] += 1
            else:
                STATS["eq_bwd_bad"] += 1
        if gnf_budget[0] > 0:
            gnf_budget[0] -= 1
            gd = gnf_check(rc)
            if gd and gd[0] <= gd[1]:
                STATS["gnf_ok"] += 1
            elif gd:
                STATS["gnf_bad"] += 1
    STATS["maxT2gt"] = max(STATS["maxT2gt"], t2gt)
    # w* sanity: no pair of supported slopes gives a SMALLER joint support
    for i in range(len(recs)):
        for k in range(i + 1, len(recs)):
            if len(recs[i]["S"] | recs[k]["S"]) < len(W):
                STATS["wstar_bad"] += 1
    # (TR1') on triples
    n = len(recs)
    if 3 <= n <= 8:
        for i in range(n):
            for k in range(i + 1, n):
                for l in range(k + 1, n):
                    U = recs[i]["S"] | recs[k]["S"] | recs[l]["S"]
                    if len(U) >= R1:
                        STATS["tr1_ok"] += 1
                    else:
                        # must be an exact relation: v_l in span(v_i,v_k)
                        Ul = sorted(U, key=lambda x: IDX[x])
                        cols = [[rc["v"].get(x, 0) for x in Ul]
                                for rc in (recs[i], recs[k], recs[l])]
                        Mt = [[cols[t][r] for t in range(3)] for r in range(len(Ul))]
                        if len(nullspace(Mt, 3)) >= 1:
                            STATS["tr1_alt2"] += 1
                        else:
                            STATS["tr1_bad"] += 1


def rand_supp_pair(a):
    """S_1,S_2 of size rho with |S_1 ^ S_2| = 2rho-a."""
    ov = 2 * rho - a
    pool = D[:]
    random.shuffle(pool)
    I = pool[:ov]
    rest = pool[ov:]
    S1 = I + rest[:rho - ov]
    S2 = I + rest[rho - ov:2 * (rho - ov)]
    return set(S1), set(S2)


def rand_vec(S):
    return {x: random.randrange(1, q) for x in S}


# ===================================================================
# ROUND-32 DRIVER (rh_fr_algebraic).  Everything above this line is a
# byte-identical scratch copy of notes/pilots_20260810/rh_type2_stratum/
# d3_census.py lines 1-345 (the round-31 decoder: BM + Vandermonde +
# nullspace + analyse()).  Only the driver below is new.
#
# QUESTION: for a REALIZABLE pencil, what is max_gamma |S_gamma ^ W|
# when W is the CANONICAL joint support W* = S_g u S_h of a pair
# MINIMISING the union (a* = min pair union), versus the planted W?
# ===================================================================

FR = dict(cells=0, pencils=0, canon=0,
          ov_ok=0, ov_bad=0, fib_ok=0, fib_bad=0, c2_ok=0, c2_bad=0,
          fr_ok=0, fr_bad=0, t1hist={}, xmax_planted=[], xmax_canon=[],
          astar=[], pairwise_bad=0, need_ok=0, need_bad=0)


def fibres(Wsorted, vg, vh):
    """mu: W -> P^1 for the representation pair (vg,vh):  z_g = vg + g*vh.
    x is killed by the finite slope -vg[x]/vh[x] when vh[x] != 0, else by
    the slope 'inf' (which is vh's own zero set inside W)."""
    mu = {}
    for x in Wsorted:
        b = vh.get(x, 0)
        if b == 0:
            mu[x] = "inf"
        else:
            mu[x] = (-vg.get(x, 0)) * inv(b) % q
    n = {}
    for x in Wsorted:
        n[mu[x]] = n.get(mu[x], 0) + 1
    return mu, n


def canonical_pass(recs0):
    """recs0: supported-slope records of ANY basis of the pencil.
    Re-runs the analysis in the basis (v_g, v_h) of a MINIMISING pair."""
    n = len(recs0)
    if n < 3:
        return None
    best, bestpair = None, None
    for i in range(n):
        for k in range(i + 1, n):
            u = len(recs0[i]["S"] | recs0[k]["S"])
            if best is None or u < best:
                best, bestpair = u, (i, k)
    i, k = bestpair
    vg, vh = recs0[i]["v"], recs0[k]["v"]
    W, recs = analyse(vg, vh)
    if len(W) != best:
        return None
    return best, W, recs, vg, vh


def fr_record(a_planted, W0, recs0):
    FR["pencils"] += 1
    xs0 = [len(rc["S"] & set(W0)) for rc in recs0 if rc["typ"] == 2]
    if xs0:
        FR["xmax_planted"].append(max(xs0))
    # the MANDATE's stratum only: non-minimum-weight type-2 (j >= 1)
    xs0g = [len(rc["S"] & set(W0)) for rc in recs0 if rc["typ"] == 2 and rc["j"] >= 1]
    if xs0g:
        FR.setdefault("xmax_planted_j1", []).append(max(xs0g))
    out = canonical_pass(recs0)
    if out is None:
        return
    astar, W, recs, vg, vh = out
    FR["canon"] += 1
    FR["astar"].append(astar)
    Wset = set(W)
    T = len(recs)
    t1 = sum(1 for rc in recs if rc["typ"] == 1)
    FR["t1hist"][t1] = FR["t1hist"].get(t1, 0) + 1
    mu, nfib = fibres(W, vg, vh)
    # (FIB) identity: the fibres partition W
    if sum(nfib.values()) == astar:
        FR["fib_ok"] += 1
    else:
        FR["fib_bad"] += 1
    xmax = 0                       # over TYPE-2 slopes only: (FR)'s quantifier
    for rc in recs:
        X = len(rc["S"] & Wset)
        if rc["typ"] == 2:
            xmax = max(xmax, X)
        # (C2) spend inequality for this W
        if rc["typ"] == 2:
            if rc["p"] >= R1 - astar + rc["n_gam"]:
                FR["c2_ok"] += 1
            else:
                FR["c2_bad"] += 1
        # (OV+): for EVERY g != gamma in P^1,  n_g - |S ^ F_g| <= p_gamma
        me = rc["gam"] if rc["tag"] == "f" else "inf"
        for gslope, ng in nfib.items():
            if gslope == me:
                continue
            s = sum(1 for x in Wset if mu[x] == gslope and x in rc["S"])
            if ng - s <= rc["p"]:
                FR["ov_ok"] += 1
            else:
                FR["ov_bad"] += 1
        # (FR) chain: X <= |S^S_g| + |S^S_h| <= 2(2rho - a*)
        if rc["typ"] == 2 and X > 2 * (2 * rho - astar):
            FR["fr_bad"] += 1
        elif rc["typ"] == 2:
            FR["fr_ok"] += 1
    FR["xmax_canon"].append((astar, xmax, T, t1))
    # pairwise sanity: no supported pair beats a*
    for i in range(len(recs)):
        for k in range(i + 1, len(recs)):
            if len(recs[i]["S"] | recs[k]["S"]) < astar:
                FR["pairwise_bad"] += 1


def build_modeB(a, p):
    """round-31 MODE B: plant a third slope with |S_3 \\ W| = p."""
    S1, S2 = rand_supp_pair(a)
    Wset = S1 | S2
    outside = [x for x in D if x not in Wset]
    if p > len(outside):
        return None
    P = set(random.sample(outside, p))
    Z = sorted(Wset | P, key=lambda x: IDX[x])
    Mv = [[pow(x, i, q) for x in Z] for i in range(R)]
    ns = nullspace(Mv, len(Z))
    if not ns:
        return None
    co = [random.randrange(q) for _ in ns]
    kv = [0] * len(Z)
    for cc, bs in zip(co, ns):
        for i2 in range(len(Z)):
            kv[i2] = (kv[i2] + cc * bs[i2]) % q
    kap = {Z[i2]: kv[i2] for i2 in range(len(Z)) if kv[i2]}
    if not all(x in kap for x in P):
        return None
    inW = [x for x in Wset if x in kap]
    k3 = rho - p
    if k3 < 0 or k3 > len(inW):
        return None
    S3inW = set(random.sample(inW, k3))
    v1, v2 = {}, {}
    for src, dst in ((S1, v1), (S2, v2)):
        for x in src:
            if x in S3inW:
                dst[x] = random.randrange(1, q)
            elif x in kap:
                dst[x] = kap[x]
            else:
                return None
    return v1, v2


random.seed(20260810 + m * 1000 + q)
say("=" * 74)
say("D3 (round 32) FR CENSUS   m=%d q=%d   rho=%d N=%d R+1=%d" % (m, q, rho, N, R1))
say("   incidence bound 3m-3 = %d ;  target 2m = %d ;  2(m-1) = %d"
    % (3 * m - 3, 2 * m, 2 * (m - 1)))
say("=" * 74)
say()
say("PRE-REGISTERED (PREREG R4): P4.1 planted-W max |S^W| exceeds 2m and")
say("reaches rho-(R+1-a)=%d ; P4.2/P4.3 zero (OV+)/(FR) violations at the" % (rho - (R1 - (8 * m - 2))))
say("canonical W* ; P4.4 census cannot separate 2m from 3m-3 ; P4.5 T_1=2.")
say()

for a in (8 * m - 2, 6 * m):
    lo = max(1, R1 - a)
    for p in range(lo, rho + 1):
        made = 0
        for _ in range(NT * 8):
            if made >= NT:
                break
            b = build_modeB(a, p)
            if b is None:
                continue
            W0, recs0 = analyse(b[0], b[1])
            if len(W0) != a:
                continue
            made += 1
            fr_record(a, W0, recs0)
    say("  planted a=%-5d : pencils=%-5d canonical passes=%-5d" % (a, FR["pencils"], FR["canon"]))

say()
say("--- RESULTS ---")
xp = FR["xmax_planted"]
say("  planted W  : max |S_gamma ^ W| over %d pencils : max %s  mean %.3f"
    % (len(xp), max(xp) if xp else None, (sum(xp) / len(xp)) if xp else 0))
say("               vs 2m=%d : exceeded in %d / %d pencils"
    % (2 * m, sum(1 for v in xp if v > 2 * m), len(xp)))
say("               vs 3m-3=%d : exceeded in %d / %d pencils"
    % (3 * m - 3, sum(1 for v in xp if v > 3 * m - 3), len(xp)))
xj = FR.get("xmax_planted_j1", [])
say("  planted W, MANDATE STRATUM ONLY (non-minimum-weight, j>=1): %d pencils,"
    " max %s, vs 2m=%d exceeded in %d, vs 3m-3=%d exceeded in %d"
    % (len(xj), max(xj) if xj else None, 2 * m,
       sum(1 for v in xj if v > 2 * m), 3 * m - 3,
       sum(1 for v in xj if v > 3 * m - 3)))
xc = FR["xmax_canon"]
if xc:
    say("  canonical W*: a* histogram %s" % sorted({v[0]: 0 for v in xc}))
    say("               max |S_gamma ^ W*| : max %d  mean %.3f"
        % (max(v[1] for v in xc), sum(v[1] for v in xc) / len(xc)))
    say("               vs 2m=%d : exceeded in %d / %d"
        % (2 * m, sum(1 for v in xc if v[1] > 2 * m), len(xc)))
    say("               vs 2(2rho-a*) (the theorem) : exceeded in %d / %d"
        % (sum(1 for v in xc if v[1] > 2 * (2 * rho - v[0])), len(xc)))
    say("               vs 3m-3=%d : exceeded in %d / %d"
        % (3 * m - 3, sum(1 for v in xc if v[1] > 3 * m - 3), len(xc)))
    tab = {}
    for astar, xmax, T, t1 in xc:
        d = tab.setdefault(astar, [0, 0, 0])
        d[0] += 1
        d[1] = max(d[1], xmax)
        d[2] = max(d[2], T)
    say("     a*     n    max X   maxT   2(2rho-a*)   2m   3m-3")
    for astar in sorted(tab):
        d = tab[astar]
        say("  %5d %5d %7d %6d %11d %5d %6d"
            % (astar, d[0], d[1], d[2], 2 * (2 * rho - astar), 2 * m, 3 * m - 3))
    say("  (all X above are over TYPE-2 slopes only -- type-1 supports lie in W* by definition)")
    say("  closure threshold need_X = rho - (floor((N-a*)e/(T-2))+1) per a*: %s"
        % sorted({astar: rho - ((N - astar) * e // max(1, 4 * m + 1 - 2) + 1) for astar in tab}.items()))
say("  T_1 histogram at W* : %s" % sorted(FR["t1hist"].items()))
say("  T   histogram at W* : %s" % sorted({v[2]: 0 for v in xc}) if xc else "")
say()
say("--- FALSIFIERS ---")
say("  (FIB) fibres partition W*        : OK %d  BAD %d" % (FR["fib_ok"], FR["fib_bad"]))
say("  (OV+) n_g - |S^F_g| <= p_gamma   : OK %d  BAD %d" % (FR["ov_ok"], FR["ov_bad"]))
say("  (C2)  p >= R+1-a*+n_gamma        : OK %d  BAD %d" % (FR["c2_ok"], FR["c2_bad"]))
say("  (FR)  X <= 2(2rho-a*)            : OK %d  BAD %d" % (FR["fr_ok"], FR["fr_bad"]))
say("  a* minimality violations         : %d" % FR["pairwise_bad"])
say("  (round-31 carried checks) GNF OK %d BAD %d ; w*_bad %d ; TR1' bad %d"
    % (STATS["gnf_ok"], STATS["gnf_bad"], STATS["wstar_bad"], STATS["tr1_bad"]))
say()
maxT = max([v[2] for v in FR["xmax_canon"]] or [0])
say("  max T over all pencils = %d   (rho+2 = %d)  -> (SAT3) UNTESTED: %s"
    % (maxT, rho + 2, maxT < rho + 2))
say("=== END d3_frcensus m=%d q=%d ===" % (m, q))

sys.stdout.write("\n".join(OUT) + "\n")
