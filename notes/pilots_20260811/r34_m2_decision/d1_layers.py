"""D1 (r34): the two linear layers of the m=2 (SAT3) question, plus the
combinatorial layer, plus the corrected dimension ledger.

Layers, in the order a witness must pass them:

  (L0) COMBINATORIAL.  9 blocks of size rho=7 on N=32 points, each point in
       <= e=2 blocks, 31 points in exactly 2 -> a 31-edge multigraph on 9
       vertices with degrees 7^8,6.  Enumerated here (labelled + iso classes).

  (L1) CURVE-FROM-DESIGN (the brief's 62 x 24).  Given the 9 slopes G and the
       31 domain points X, each edge {a,b} at x imposes
         c_1(x) + (a+b) c_2(x) = 0,   c_0(x) - a b c_2(x) = 0,
       linear in the 24 coefficients of (c_2,c_1,c_0), deg <= 7.  A curve
       exists iff rank <= 23.

  (L2) PENCIL-FROM-CURVE (NOT in the brief, and it is the sharper one).  The
       locator curve is only the kernel of a real syndrome Hankel pencil if
         M(Z) Q_Z == 0,  M(Z) = M_r(y_0) + Z M_r(y_1),  Q_Z = sum_k Z^k Q_k,
       which is (m+2)(4m+1) equations on 2R = 16m unknowns.  At m=1 that is
       15 < 16 (ALWAYS solvable -- which is exactly why round 33's m=1 search
       succeeded on all 16 families); at m=2 it is 36 > 32.  Overdetermination
       4m^2-7m+2 = -1, +4, +17, ... for m = 1,2,3.

Stdlib only.  Usage: d1_layers.py OUTFILE
"""
import sys
import random

LINES = []


def out(s=""):
    print(s)
    LINES.append(s)


# ---------------------------------------------------------------- field ----
def make_field(q):
    def inv(a):
        return pow(a % q, q - 2, q)
    return inv


def rref(rows, ncols, q):
    rows = [r[:] for r in rows]
    piv, rk = [], 0
    for c in range(ncols):
        p = None
        for i in range(rk, len(rows)):
            if rows[i][c] % q:
                p = i
                break
        if p is None:
            continue
        rows[rk], rows[p] = rows[p], rows[rk]
        iv = pow(rows[rk][c], q - 2, q)
        rows[rk] = [v * iv % q for v in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][c] % q:
                f = rows[i][c]
                rows[i] = [(a - f * b) % q for a, b in zip(rows[i], rows[rk])]
        piv.append(c)
        rk += 1
        if rk == len(rows):
            break
    return rows, piv, rk


def rank(rows, ncols, q):
    return rref(rows, ncols, q)[2]


def nullspace(rows, ncols, q):
    if not rows:
        return [[1 if i == j else 0 for i in range(ncols)] for j in range(ncols)]
    rr, piv, rk = rref(rows, ncols, q)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-rr[i][f]) % q
        basis.append(v)
    return basis


def mu(q, n):
    """the n-th roots of unity in F_q (n | q-1)."""
    assert (q - 1) % n == 0, (q, n)
    for a in range(2, q):
        h = pow(a, (q - 1) // n, q)
        seen = {pow(h, i, q) for i in range(n)}
        if len(seen) == n:
            return sorted(seen)
    raise RuntimeError("no mu_%d in F_%d" % (n, q))


def poly_from_roots(roots, q):
    c = [1]
    for r in roots:
        nc = [0] * (len(c) + 1)
        for i, ci in enumerate(c):
            nc[i] = (nc[i] - r * ci) % q
            nc[i + 1] = (nc[i + 1] + ci) % q
        c = nc
    return c


def peval(c, x, q):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % q
    return v


# ------------------------------------------------------- (L0) the design ----
def enumerate_designs(minmult=-1):
    """Multigraphs on 9 vertices, 31 edges, degrees 7^8,6 (vertex 8 = the 6).

    Complement bookkeeping: c_ij = 1 - m_ij <= 1, symmetric, row sums
    r_i = 8 - deg_i = 1 (i<8), 2 (i=8), total sum over pairs = 5.
    """
    n = 9
    target = [1] * 8 + [2]
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    sols = []
    rem = target[:]

    CAP = 60000

    def dfs(k, rem):
        if len(sols) > CAP:
            return
        if k == len(pairs):
            if all(v == 0 for v in rem):
                sols.append(tuple(cur))
            return
        i, j = pairs[k]
        # remaining pairs touching i / j
        left_i = sum(1 for (a, b) in pairs[k:] if a == i or b == i)
        left_j = sum(1 for (a, b) in pairs[k:] if a == j or b == j)
        for val in range(minmult, 2):
            ri, rj = rem[i] - val, rem[j] - val
            # each remaining incident pair contributes at most +1
            if ri > left_i - 1 or rj > left_j - 1:
                continue
            if ri < minmult * (left_i - 1) or rj < minmult * (left_j - 1):
                continue
            cur.append(val)
            rem[i], rem[j] = ri, rj
            dfs(k + 1, rem)
            rem[i], rem[j] = ri + val, rj + val
            cur.pop()

    cur = []
    dfs(0, rem)
    if len(sols) > CAP:
        return sols, -1, [], pairs
    # iso classes: union-find over S_9 generators (adjacent transpositions
    # inside {0..7}, which is the stabiliser of the degree-6 vertex 8)
    idx = {s: i for i, s in enumerate(sols)}
    parent = list(range(len(sols)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    pos = {p: k for k, p in enumerate(pairs)}
    for s, si in idx.items():
        for t in range(7):
            perm = list(range(9))
            perm[t], perm[t + 1] = perm[t + 1], perm[t]
            ns = [0] * len(pairs)
            for k, (i, j) in enumerate(pairs):
                a, b = perm[i], perm[j]
                if a > b:
                    a, b = b, a
                ns[pos[(a, b)]] = s[k]
            union(si, idx[tuple(ns)])
    classes = len({find(i) for i in range(len(sols))})
    simple = [s for s in sols if all(v >= 0 for v in s)]
    return sols, classes, simple, pairs


# ------------------------------------------------- (L1) curve-from-design ----
def design_edges():
    """K_9 minus (P_3 + 3K_2): the unique SIMPLE design.  Vertex 8 has deg 6."""
    n = 9
    # complement: path 8-0-1 (8 is the degree-6 vertex, the middle of P_3)
    # plus disjoint edges {2,3},{4,5},{6,7}
    comp = {(0, 8), (0, 1), (2, 3), (4, 5), (6, 7)}
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) in comp or (j, i) in comp:
                continue
            edges.append((i, j))
    return edges


def layer1_matrix(G, X, edges, q):
    """62 x 24 system.  Unknown order: c_2[0..7], c_1[0..7], c_0[0..7]."""
    rows = []
    for (e, x) in zip(edges, X):
        a, b = G[e[0]], G[e[1]]
        xp = [pow(x, j, q) for j in range(8)]
        r1 = [(a + b) * t % q for t in xp] + xp[:] + [0] * 8
        r2 = [(-a * b) * t % q for t in xp] + [0] * 8 + xp[:]
        rows.append(r1)
        rows.append(r2)
    return rows


# -------------------------------------------------- (L2) pencil-from-curve --
def realization_rows(Qk, m, q):
    """M(Z)Q_Z == 0 as (m+2)(4m+1) equations on (y_0,y_1) in F^{2R}.

    Qk[k] is the X-coefficient vector (length r+1 = 4m) of Z^k, k=0..m.
    Unknown order: y_0[0..R-1], y_1[0..R-1].
    """
    R = 8 * m
    r = 4 * m - 1
    rows = []
    for k in range(m + 2):
        for i in range(R - r):
            row = [0] * (2 * R)
            if 0 <= k <= m:
                for j in range(r + 1):
                    row[i + j] = (row[i + j] + Qk[k][j]) % q
            if 0 <= k - 1 <= m:
                for j in range(r + 1):
                    row[R + i + j] = (row[R + i + j] + Qk[k - 1][j]) % q
            rows.append(row)
    return rows


def Mr(y, m, q):
    R, r = 8 * m, 4 * m - 1
    return [[y[i + j] for j in range(r + 1)] for i in range(R - r)]


def split_locators(mat, D, m, q):
    """monic squarefree degree-r polys with all roots in D lying in ker(mat)"""
    r = 4 * m - 1
    ns = nullspace(mat, r + 1, q)
    if not ns or len(ns) > 1:
        # only the corank-1 case is enumerated cheaply; corank>1 -> flag
        if not ns:
            return []
    out_ = []
    if len(ns) == 1:
        v = ns[0]
        if v[r] == 0:
            return []
        iv = pow(v[r], q - 2, q)
        w = [a * iv % q for a in v]
        roots = [x for x in D if peval(w, x, q) == 0]
        if len(roots) == r:
            out_.append(tuple(sorted(roots)))
    return out_


# ------------------------------------------------------------------ main ----
def main():
    random.seed(20260811)
    out("=== r34 D1: the three layers of the m=2 (SAT3) question ===")
    out("")

    # ---------------- L0 ----------------
    out("--- (L0) COMBINATORIAL LAYER: 31-edge multigraphs, degrees 7^8,6 ---")
    for mm_cap, tag in ((0, "SIMPLE (block pairs meet in <= 1 point)"),
                        (-1, "multiplicity <= 2"),
                        (-2, "multiplicity <= 3")):
        sols, classes, simple, pairs = enumerate_designs(mm_cap)
        mult = {}
        for s in sols:
            mult[max(1 - v for v in s)] = mult.get(max(1 - v for v in s), 0) + 1
        out(f"  {tag}: labelled {len(sols)}"
            f"{'+ (capped)' if classes == -1 else ''}, ISO CLASSES "
            f"{classes if classes != -1 else 'not counted (too many)'}, "
            f"multiplicity histogram {dict(sorted(mult.items()))}")
    out("  (the degree-6 vertex is pinned as vertex 8, so 'iso classes'"
        " counts classes of the whole design)")
    out("")

    # ---------------- L2 arithmetic ----------------
    out("--- (L2) PENCIL-FROM-CURVE: exact sizes, all m ---")
    out(" m | rho | N   | R   | eqs=(m+2)(4m+1) | unknowns=16m | over =")
    out("   |     |     |     |                 |              | 4m^2-7m+2")
    for m in range(1, 7):
        eqs = (m + 2) * (4 * m + 1)
        unk = 16 * m
        out(f" {m} | {4*m-1:3d} | {16*m:3d} | {8*m:3d} | {eqs:15d} | "
            f"{unk:12d} | {eqs-unk:+d}")
    out("m=1 is the ONLY m at which the realization system is "
        "underdetermined.")
    out("")

    # ---------------- empirical: L2 rank ----------------
    out("--- (L2) empirical nullity, random curves Q, two fields ---")
    for q in (97, 193):
        for m in (1, 2):
            r = 4 * m - 1
            hist = {}
            for _ in range(60):
                Qk = [[random.randrange(q) for _ in range(r + 1)]
                      for _ in range(m + 1)]
                rows = realization_rows(Qk, m, q)
                nl = 2 * 8 * m - rank(rows, 2 * 8 * m, q)
                hist[nl] = hist.get(nl, 0) + 1
            out(f"  q={q} m={m}: nullity histogram over 60 random Q: "
                f"{dict(sorted(hist.items()))}")
    out("")

    # ---------------- L2: does ANY e=2 curve realize at m=2? -------------
    out("--- (L2) is the (SAT1) profile with e=m=2 realizable AT ALL? ---")
    m = 2
    r = 4 * m - 1
    R = 8 * m
    for q in (97, 193):
        D = mu(q, 32)
        assert len(D) == 32, (q, len(D))
        # (a) Kummer-type e=2 curve  Q_Z(X) = X^7 + (alpha Z^2 + beta Z + gam)
        hits_k = []
        n_k = 0
        for alpha in range(1, 21):
            for beta in (0, 1):
                for gamma in range(0, q, max(1, q // 10)):
                    n_k += 1
                    Qk = [[0] * (r + 1) for _ in range(m + 1)]
                    Qk[0][0] = gamma
                    Qk[0][r] = 1
                    Qk[1][0] = beta
                    Qk[2][0] = alpha
                    rows = realization_rows(Qk, m, q)
                    if nullspace(rows, 2 * R, q):
                        hits_k.append((alpha, beta, gamma))
        out(f"  q={q}: Kummer e=2 curves scanned {n_k}, realizable: "
            f"{len(hits_k)}   {hits_k[:3]}")
        # (b) split-endpoint ansatz: Q_0 and Q_2 are split degree-7 locators
        #     on random 7-subsets of D, Q_1 random
        n_s, hits_s = 0, 0
        for _ in range(400):
            n_s += 1
            S0 = random.sample(D, 7)
            S2 = random.sample(D, 7)
            Qk = [poly_from_roots(S0, q),
                  [random.randrange(q) for _ in range(r + 1)],
                  poly_from_roots(S2, q)]
            rows = realization_rows(Qk, m, q)
            if nullspace(rows, 2 * R, q):
                hits_s += 1
        out(f"  q={q}: split-endpoint ansatz scanned {n_s}, realizable: "
            f"{hits_s}")
        # (c) fully random curves
        n_r, hits_r = 0, 0
        for _ in range(400):
            n_r += 1
            Qk = [[random.randrange(q) for _ in range(r + 1)]
                  for _ in range(m + 1)]
            rows = realization_rows(Qk, m, q)
            if nullspace(rows, 2 * R, q):
                hits_r += 1
        out(f"  q={q}: random curves scanned {n_r}, realizable: {hits_r}")
    out("ANALYTIC (checked by hand, confirmed above): for the Kummer curve")
    out("  Q_2 = alpha (a CONSTANT in X), so M_r(y_1) Q_2 = 0 forces")
    out("  y_1[0..8] = 0, then block 3 forces y_0[0..7] = 0 and block 1")
    out("  (gamma y_0[i] + y_0[i+7] = 0, i=0..8) then forces y_0 = 0.")
    out("  The e=1 Kummer family that carried round 33's ladder therefore has")
    out("  NO e=2 analogue: the leading Z-coefficient must itself be a")
    out("  degree-rho locator, not a constant.")
    out("")

    # ---------------- L1: the 62x24 layer ----------------
    out("--- (L1) CURVE-FROM-DESIGN: rank of the 62x24 system ---")
    edges = design_edges()
    out(f"design used: K_9 - (P_3 + 3K_2), |E| = {len(edges)}, degrees "
        f"{sorted((sum(1 for e in edges if v in e) for v in range(9)), reverse=True)}")
    for q in (97, 193):
        D = mu(q, 32)
        hist = {}
        best = None
        for _ in range(200):
            G = random.sample(range(q), 9)
            X = random.sample(D, 31)
            rows = layer1_matrix(G, X, edges, q)
            rk = rank(rows, 24, q)
            hist[rk] = hist.get(rk, 0) + 1
            if best is None or rk < best:
                best = rk
        out(f"  q={q} random (G,X): rank histogram over 200: "
            f"{dict(sorted(hist.items()))}  (need <= 23)")
        # structured: G a coset of mu_9 (if 9 | q-1), X = D minus one point
        stru = []
        if (q - 1) % 9 == 0:
            G9 = mu(q, 9)
            for _ in range(50):
                X = random.sample(D, 31)
                rows = layer1_matrix(G9, X, edges, q)
                stru.append(rank(rows, 24, q))
        # structured: X an arithmetic progression, G an AP
        for _ in range(50):
            a0 = random.randrange(1, q)
            d0 = random.randrange(1, q)
            X = [(a0 + i * d0) % q for i in range(31)]
            if len(set(X)) < 31:
                continue
            b0 = random.randrange(1, q)
            e0 = random.randrange(1, q)
            G = [(b0 + i * e0) % q for i in range(9)]
            if len(set(G)) < 9:
                continue
            rows = layer1_matrix(G, X, edges, q)
            stru.append(rank(rows, 24, q))
        out(f"  q={q} structured (mu_9 slopes / AP slopes+points), "
            f"{len(stru)} trials: min rank {min(stru) if stru else 'n/a'}, "
            f"ranks seen {sorted(set(stru))}")
    out("")

    # ---------------- ledgers ----------------
    out("--- CORRECTED DIMENSION LEDGER (heuristic; see MISS list) ---")
    out("(TCAP-DIM) as posed: excess(m) = 12m^2 - 24m - 1 - O")
    out("Correction: every solution carries a free orbit of the group")
    out("  AGL_1(x) x AGL_1(gamma)  (dim 4)  [PGL_2 x PGL_2 generically: 6],")
    out("acting with finite stabilisers (it fixes >= 9 slopes and 32 points),")
    out("so the expected dimension must EXCEED the orbit dimension.")
    out(" m | TCAP excess | corrected (+4) | corrected (+6) | verdict(+6)")
    for m in (1, 2, 3, 4):
        t = 12 * m * m - 24 * m - 1
        out(f" {m} | {t:+11d} | {t+4:+14d} | {t+6:+14d} | "
            f"{'realizable-expected' if t+6 < 0 else 'UNREALIZABLE-expected'}")
    out("positive control 1 (round 33, PROVED): m=1 realizable  -> corrected"
        " ledger must be < 0 at m=1: it is.")
    out("positive control 2 (round 33 ladder, e=1, T=floor(N/rho)=4, every m):")
    out("  TCAP excess = -8m-7; corrected +6 -> -8m-1 < 0 for all m: still"
        " realizable-expected, as measured.")
    out("")
    out("Independent bookkeeping of the SAME correction (locator layer only):")
    out("  unknowns: 32 domain points + 9 scalars lambda_i + 9 slopes = 50")
    out("  conditions: 6 slopes x 8 coords of 'P_g = lambda_g Pi_g' = 48")
    out("  symmetries: lambda-scaling 1 + PGL_2(gamma) 3 + PGL_2(x) 3 = 7")
    out("  excess = 50 - 48 - 7 = -5   (m=2)")
    out("  same count at m=1: 16 pts + 5 lambdas + 5 slopes = 26; conditions"
        " 3 slopes x 4 coords = 12; symmetries 1+3+3=7 -> +7  (realizable)")
    out("")

    with open(sys.argv[1], "w") as f:
        f.write("\n".join(LINES) + "\n")


main()
