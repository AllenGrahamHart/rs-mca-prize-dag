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


say("=" * 74)
say("D3 CENSUS   m=%d  q=%d   rho=%d N=%d R+1=%d  window w* in [%d,%d]"
    % (m, q, rho, N, R1, 4 * m + 2, 8 * m - 2))
say("=" * 74)

# ------------------------------------------------------------- mode A
say()
say("--- MODE A: random pencils at three w* values (a = |S_1 u S_2|) ---")
for a in sorted({4 * m + 2, 6 * m, 8 * m - 2}):
    jh, ph, Th = {}, {}, {}
    before = dict(STATS)
    budget = [12]
    for _ in range(NR):
        S1, S2 = rand_supp_pair(a)
        W, recs = analyse(rand_vec(S1), rand_vec(S2))
        if len(W) != a:
            continue
        record(W, recs, jh, ph, Th, budget)
    say("  a=%-6d cap CAP(m,a)=%-8d   pencils=%d  T histogram %s"
        % (a, (N - a) * e // (R1 - a), NR, sorted(Th.items())))
    say("       type-2 seen=%d   j=0: %d   j>=1: %d   p hist %s   j hist %s"
        % (STATS["t2"] - before["t2"], STATS["t2_eq"] - before["t2_eq"],
           STATS["t2_gt"] - before["t2_gt"], sorted(ph.items()),
           sorted(jh.items())))

# ------------------------------------------------------------- mode B
say()
say("--- MODE B: TARGETED pencils, a = 2rho = 8m-2, third slope planted ---")
say("    Construction: W = S_1 u S_2 disjoint; pick P of size p outside W,")
say("    S_3 = P u (subset of W); kappa in K supported on Z = W u P built by")
say("    NULLSPACE (not by the GNF, so the GNF check stays independent);")
say("    v_1 := kappa on S_1\\S_3 (free on S_1 ^ S_3), same for v_2; then")
say("    v_3 = v_1 + v_2 - kappa is automatically supported in S_3.")
a = 8 * m - 2
say("    a = %d, CAP(m,a) = %d, target rho+1 = %d"
    % (a, (N - a) * e // (R1 - a), rho + 1))
jh, ph, Th = {}, {}, {}
budget = [40]
by_p = {}
for p in range(R1 - a, rho + 1):
    made = 0
    b4 = dict(STATS)
    for _ in range(NT * 6):
        if made >= NT:
            break
        S1, S2 = rand_supp_pair(a)
        Wset = S1 | S2
        outside = [x for x in D if x not in Wset]
        P = set(random.sample(outside, p))
        Z = sorted(Wset | P, key=lambda x: IDX[x])
        Mv = [[pow(x, i, q) for x in Z] for i in range(R)]
        ns = nullspace(Mv, len(Z))
        if not ns:
            continue
        co = [random.randrange(q) for _ in ns]
        kv = [0] * len(Z)
        for cc, bs in zip(co, ns):
            for i2 in range(len(Z)):
                kv[i2] = (kv[i2] + cc * bs[i2]) % q
        kap = {Z[i2]: kv[i2] for i2 in range(len(Z)) if kv[i2]}
        if not all(x in kap for x in P):
            continue
        inW = [x for x in Wset if x in kap]
        k3 = rho - p
        if k3 < 0 or k3 > len(inW):
            continue
        S3inW = set(random.sample(inW, k3))
        v1, v2 = {}, {}
        okc = True
        for x in S1:
            if x in S3inW:
                v1[x] = random.randrange(1, q)
            elif x in kap:
                v1[x] = kap[x]
            else:
                okc = False
                break
        if not okc:
            continue
        for x in S2:
            if x in S3inW:
                v2[x] = random.randrange(1, q)
            elif x in kap:
                v2[x] = kap[x]
            else:
                okc = False
                break
        if not okc:
            continue
        W, recs = analyse(v1, v2)
        if len(W) != a:
            continue
        made += 1
        record(W, recs, jh, ph, Th, budget)
    d = dict(t2=STATS["t2"] - b4["t2"], eq=STATS["t2_eq"] - b4["t2_eq"],
             gt=STATS["t2_gt"] - b4["t2_gt"])
    by_p[p] = (made, d)
    say("    p=%-4d built=%-5d type-2 found=%-6d  j=0: %-6d  j>=1: %-6d"
        % (p, made, d["t2"], d["eq"], d["gt"]))
say("    overall p histogram: %s" % sorted(ph.items()))
say("    overall j histogram: %s" % sorted(jh.items()))
say("    T histogram        : %s" % sorted(Th.items()))

say()
say("--- CHECKS ---")
say("  (GNF)  kappa_x = f(x)/sigma'_Z(x), deg f <= |Z|-(R+1):  OK %d  BAD %d"
    % (STATS["gnf_ok"], STATS["gnf_bad"]))
say("  (EQ->) equality in (C2)  =>  j=0            :  OK %d  BAD %d"
    % (STATS["eq_fwd_ok"], STATS["eq_fwd_bad"]))
say("  (EQ<-) j=0  =>  equality in (C2)            :  OK %d  BAD %d"
    % (STATS["eq_bwd_ok"], STATS["eq_bwd_bad"]))
say("  (TR1') triples: |u S| >= R+1 : %d    exact relation : %d    VIOLATIONS: %d"
    % (STATS["tr1_ok"], STATS["tr1_alt2"], STATS["tr1_bad"]))
say("  w* minimality violations (a supported pair with smaller union): %d"
    % STATS["wstar_bad"])
say()
say("--- SUMMARY (m=%d, q=%d) ---" % (m, q))
say("  pencils analysed        : %d" % STATS["pencils"])
say("  supported slopes seen   : %d" % STATS["supported"])
say("  max T over all pencils  : %d      (rho+2 = %d)" % (STATS["maxT"], rho + 2))
say("  type-2 slopes seen      : %d" % STATS["t2"])
say("    of which j = 0        : %d" % STATS["t2_eq"])
say("    of which j >= 1       : %d   <-- THE MANDATE'S STRATUM" % STATS["t2_gt"])
say("  max T_2^{>} in ONE pencil: %d    CAP(m,8m-2) = %d"
    % (STATS["maxT2gt"], (N - (8 * m - 2)) * e // 3))
say("=== END d3_census m=%d q=%d ===" % (m, q))

sys.stdout.write("\n".join(OUT) + "\n")
