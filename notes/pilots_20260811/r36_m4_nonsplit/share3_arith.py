"""D2: the ARITHMETIC layer of the 3-sharing (SHARE3-4) ansatz, plus an
EXHAUSTIVE census of the constant-(e1,e3) multiplicative sub-family.

Part A (exhaustive, not a ceiling): bucket all C(64,3) = 41664 mu_64
triples by (e1,e3) = (sum, product).  A bucket of size f IS a degree-3
pencil with f complete fibres (Delta proportional to X).  This is a
COMPLETE enumeration of that named sub-family.

Part B: given such a pencil with >= 9 fibres, the arithmetic layer.
Psi~ = (U~,E~1,E~2,E~3), each deg_w <= 3: 16 coefficients.  The tuple at
fibre j is the root set of  U~(t_j)Z^3 - E~1(t_j)Z^2 + E~2(t_j)Z - E~3(t_j).
"slope gamma occurs at fibre j" is ONE homogeneous linear condition on
the 16 coefficients (R1.14).  Feasibility of the full 26-incidence
system is exactly  rank(M) <= 15.

Writes share3_arith_results.txt in this directory only.  Stdlib only.
"""
import random
import sys
import time

DIR = "notes/pilots_20260811/r36_m4_nonsplit/"
OUT = []
T0 = time.time()
DEADLINE = 255.0


def p(s=""):
    OUT.append(str(s))


def flush():
    with open(DIR + "share3_arith_results.txt", "w") as f:
        f.write("\n".join(OUT) + "\n")


def mu(q, n=64):
    for g in range(2, q):
        h = pow(g, (q - 1) // n, q)
        s = set()
        x = 1
        for _ in range(n):
            s.add(x)
            x = x * h % q
        if len(s) == n:
            return sorted(s)
    raise RuntimeError


def rank_mod(rows, ncol, q):
    rows = [r[:] for r in rows]
    r = 0
    for c in range(ncol):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][c]:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        iv = pow(rows[r][c], q - 2, q)
        rows[r] = [v * iv % q for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]
                rows[i] = [(a - f * b) % q for a, b in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r, rows


def nullvec(rows, ncol, q):
    r, red = rank_mod(rows, ncol, q)
    if r >= ncol:
        return None
    pivcol = []
    for row in red[:r]:
        for c in range(ncol):
            if row[c]:
                pivcol.append(c)
                break
    free = [c for c in range(ncol) if c not in pivcol]
    v = [0] * ncol
    v[free[0]] = 1
    for i, c in enumerate(pivcol):
        v[c] = (-red[i][free[0]]) % q
    return v


def cond_row(t, gam, q):
    """the linear condition 'gam is a root of the cubic at fibre value t'
    on the 16 coefficients ordered U~[0..3], E~1[0..3], E~2[0..3], E~3[0..3]."""
    tp = [1, t % q, t * t % q, t * t % q * t % q]
    g3 = gam * gam % q * gam % q
    g2 = gam * gam % q
    row = []
    for a in tp:
        row.append(a * g3 % q)
    for a in tp:
        row.append((-a * g2) % q)
    for a in tp:
        row.append(a * gam % q)
    for a in tp:
        row.append((-a) % q)
    return row


def verify_struct(triples):
    """MISS-2 GUARD.  |slopes| alone is NOT the constrained quantity.
    A legal k=3 configuration must ALSO satisfy, per R1.10/R1.11:
      (a) three DISTINCT slopes per fibre;
      (b) hypergraph degree <= 2   (per-side cap 3 with X' = 3d);
      (c) pair multiplicity 1      ((OV) cap met with equality at k=3);
      (d) the slope graph on the 8 triples 2-colourable with a 4/4 split
          (the (2,1)/(1,2) per-side balance, sum_T a_T = 12)."""
    slopes = sorted(set(s for t in triples for s in t))
    deg = dict((s, 0) for s in slopes)
    for t in triples:
        if len(set(t)) != 3:
            return False, "repeated root inside a fibre", None
        for s in t:
            deg[s] += 1
    if max(deg.values()) > 2:
        return False, "hypergraph degree %d > 2" % max(deg.values()), None
    pm = {}
    for t in triples:
        for a in range(3):
            for b in range(a + 1, 3):
                key = (min(t[a], t[b]), max(t[a], t[b]))
                pm[key] = pm.get(key, 0) + 1
    if max(pm.values()) > 1:
        return False, "pair multiplicity %d > 1" % max(pm.values()), None
    adj = dict((i, []) for i in range(len(triples)))
    for s, d in deg.items():
        if d == 2:
            vs = [i for i, t in enumerate(triples) if s in t]
            adj[vs[0]].append(vs[1])
            adj[vs[1]].append(vs[0])
    col = {}
    comps = []
    for start in range(len(triples)):
        if start in col:
            continue
        col[start] = 0
        stack = [start]
        comp = [start]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in col:
                    col[v] = 1 - col[u]
                    stack.append(v)
                    comp.append(v)
                elif col[v] == col[u]:
                    return False, "slope graph not bipartite", None
        c0 = sum(1 for v in comp if col[v] == 0)
        comps.append((c0, len(comp) - c0))
    reach = set([0])
    for c0, c1 in comps:
        reach = set([r + c0 for r in reach]) | set([r + c1 for r in reach])
    if 4 not in reach:
        return False, "no 4/4 per-side balance (reachable %s)" % sorted(reach), None
    return True, ("PASS: %d slopes, degseq %s, pair mult 1, bipartite 4/4"
                  % (len(slopes), sorted(deg.values()))), (slopes, deg)


def cubic_roots(c3, c2, c1, c0, q):
    rs = [z for z in range(q)
          if (((c3 * z + c2) * z + c1) * z + c0) % q == 0]
    return rs


# ---------------- the design (R1.11 certificate C2) ----------------
A, B = [0, 1, 2, 3], [4, 5, 6, 7]
K = [(a, b) for a in A for b in B if b - 4 != a]        # 12 edges
E11 = K[:-1]                                            # 11 edges
drop = K[-1]
DESIGN = {v: [] for v in A + B}
for si, (a, b) in enumerate(E11):
    DESIGN[a].append(si)
    DESIGN[b].append(si)
DESIGN[drop[0]].append(11)                              # pendant slopes
DESIGN[drop[1]].append(12)
NSLOPE = 13                                             # + 2 middle slopes

FIELDS = [193, 257]
if len(sys.argv) > 1:
    FIELDS = [int(x) for x in sys.argv[1].split(",")]

p("=== D2  (SHARE3-4) ARITHMETIC LAYER + EXHAUSTIVE MULTIPLICATIVE CENSUS ===")
p("design (R1.11 cert C2): 8 triples, 11 edge-slopes + 2 pendants = 13,")
p("  plus 2 middle slopes = T_2 = rho = 15 exactly.")
p("  slot sum = %d ; degree sequence = %s"
  % (sum(len(v) for v in DESIGN.values()),
     sorted([sum(1 for v in DESIGN.values() if s in v)
             for s in range(NSLOPE)])))
p()

for q in FIELDS:
    if time.time() - T0 > DEADLINE:
        p("!! DEADLINE before q=%d -- ZERO DRAWS, NOT a measurement" % q)
        break
    D = mu(q)
    # ---- Part A: exhaustive (e1,e3) census ----
    buck = {}
    for i in range(64):
        a = D[i]
        for j in range(i + 1, 64):
            b = D[j]
            ab = a * b % q
            apb = (a + b) % q
            for k in range(j + 1, 64):
                c = D[k]
                key = ((apb + c) % q, ab * c % q)
                e2 = (ab + c * apb) % q
                buck.setdefault(key, []).append((e2, (a, b, c)))
    sizes = {}
    for v in buck.values():
        sizes[len(v)] = sizes.get(len(v), 0) + 1
    best = max(buck.items(), key=lambda kv: len(kv[1]))
    p("--- q = %d  PART A1: EXHAUSTIVE constant-(e1,e3) census (Delta ~ X)"
      % q)
    p("    buckets = %d ; size histogram (size:count) = %s"
      % (len(buck), dict(sorted(sizes.items()))))
    p("    MAX complete fibres in one such pencil = %d   (need 9)"
      % len(best[1]))
    p("    pencils with >= 9 fibres = %d ; with >= 8 = %d"
      % (sum(1 for v in buck.values() if len(v) >= 9),
         sum(1 for v in buck.values() if len(v) >= 8)))
    p("    EXHAUSTIVE over that sub-family -- not a ceiling.")

    # ---- Part A2: constant-e3 family (Delta = X(cX+d)); lines in (e1,e2) ----
    by3 = {}
    for (a1, a3), v in buck.items():
        for e2, tri in v:
            by3.setdefault(a3, []).append((a1, e2, tri))
    POOLP = []
    bestn = 0
    NB = 200
    for a3, pts3 in by3.items():
        if time.time() - T0 > DEADLINE:
            break
        n = len(pts3)
        bases = range(n) if n <= NB else random.sample(range(n), NB)
        for bi in bases:
            b1, b2, btri = pts3[bi]
            bset = set(btri)
            lines = {}
            for t in range(n):
                if t == bi:
                    continue
                a1, e2, tri = pts3[t]
                if bset & set(tri):
                    continue
                u = (a1 - b1) % q
                v2 = (e2 - b2) % q
                key = (0, v2 * pow(u, q - 2, q) % q) if u else (1, 0)
                lines.setdefault(key, []).append(t)
            for key, mem in lines.items():
                if len(mem) + 1 >= 9:
                    fibs = [(0, btri)]
                    for t in mem:
                        a1, e2, tri = pts3[t]
                        s = (a1 - b1) % q if key[0] == 0 else (e2 - b2) % q
                        fibs.append((s, tri))
                    okd = True
                    seen = set()
                    for _, tri in fibs:
                        if seen & set(tri):
                            okd = False
                        seen.update(tri)
                    if okd and len(set(f[0] for f in fibs)) == len(fibs):
                        POOLP.append(fibs)
                        bestn = max(bestn, len(fibs))
    p("    PART A2: constant-e3 family (Delta = X(cX+d)), %d bases per e3"
      % NB)
    p("       exhaustive over every line through each sampled base triple")
    p("       pencils found with >= 9 disjoint complete fibres : %d"
      % len(POOLP))
    p("       MAX complete fibres over the family = %d" % bestn)
    if not POOLP:
        POOLP = [sorted(v) for v in buck.values() if len(v) >= 9]
    if not POOLP:
        p("    !! no pencil with >= 9 fibres at q = %d -- Part B SKIPPED"
          " (zero draws, NOT a measurement)" % q)
        p()
        flush()
        continue
    fib = sorted(max(POOLP, key=len))[:9]
    p("    chosen pencil has %d fibres ; using 9" % len(max(POOLP, key=len)))
    p("    fibre parameters t_j = %s" % [f[0] for f in fib])
    pts = sorted(x for f in fib for x in f[1])
    p("    27 W-points, all distinct : %s ; |W| = %d = a = 7m-1 : %s"
      % (len(set(pts)) == 27, len(set(pts)), len(set(pts)) == 27))
    T = [f[0] for f in fib]

    # ---- Part B: the arithmetic layer ----
    random.seed(7 * q)
    p("    PART B: arithmetic layer, 16 coefficients of Psi~")

    # B0: the full 26-incidence rank test with random slope values
    minrank = 99
    NR = 400
    for _ in range(NR):
        gam = random.sample(range(1, q), NSLOPE + 2)
        rows = []
        for vi, v in enumerate(A + B):
            for s in DESIGN[v]:
                rows.append(cond_row(T[vi], gam[s], q))
        for s in (NSLOPE, NSLOPE + 1):                  # the middle tuple
            rows.append(cond_row(T[8], gam[s], q))
        r, _ = rank_mod(rows, 16, q)
        minrank = min(minrank, r)
    p("      B0 RANK TEST (feasible iff rank <= 15): %d random slope draws"
      % NR)
    p("         min rank over draws = %d   (16 = infeasible, <=15 = WITNESS)"
      % minrank)

    # B1: RANDOM Psi~
    bestk = 0
    bestrec = None
    NDR = 3000
    for _ in range(NDR):
        co = [random.randrange(q) for _ in range(16)]
        slopes = set()
        k = 0
        trip = []
        for j in range(8):
            t = T[j]
            tp = [1, t % q, t * t % q, t * t % q * t % q]
            c3 = sum(co[i] * tp[i] for i in range(4)) % q
            c2 = (-sum(co[4 + i] * tp[i] for i in range(4))) % q
            c1 = sum(co[8 + i] * tp[i] for i in range(4)) % q
            c0 = (-sum(co[12 + i] * tp[i] for i in range(4))) % q
            if c3 == 0:
                continue
            rs = cubic_roots(c3, c2, c1, c0, q)
            if len(rs) == 3:
                k += 1
                trip.append(rs)
                slopes.update(rs)
        if k > bestk or (k == bestk and bestrec and len(slopes) < bestrec[1]):
            bestk, bestrec = k, (k, len(slopes), 3 * k - len(slopes))
    p("      B1 RANDOM Psi~ (%d draws): best k = %d of 8 fully-split fibres;"
      % (NDR, bestk))
    p("         best (k, |slopes|, coincidences C = 3k-|slopes|) = %s"
      % (bestrec,))

    # B2: ALLOC -- prescribe 15 incidences by nullspace, measure the rest
    #     widened: random pencil among all with >=9 fibres, random 8-subset
    #     of its fibres, random rotation of the design.
    bestalloc = None
    hits = []
    slopehist = {}
    legalhist = {}
    struct = {}
    WIT = [None]
    NA = 40000
    for _ in range(NA):
        if time.time() - T0 > DEADLINE:
            break
        fb = sorted(random.choice(POOLP))
        T = [f[0] for f in random.sample(fb, 9)]
        gam = random.sample(range(1, q), NSLOPE + 2)
        order = list(range(8))
        random.shuffle(order)
        rows = []
        used = []
        for n, vi in enumerate(order):           # 2 slopes at each of 7 + 1
            v = (A + B)[vi]
            take = DESIGN[v][:2] if n < 7 else DESIGN[v][:1]
            for s in take:
                rows.append(cond_row(T[vi], gam[s], q))
                used.append((vi, s))
        co = nullvec(rows, 16, q)
        if co is None:
            continue
        pool = set(gam)
        k = 0
        allsl = set()
        extra = 0
        trips8 = []
        for j in range(8):
            t = T[j]
            tp = [1, t % q, t * t % q, t * t % q * t % q]
            c3 = sum(co[i] * tp[i] for i in range(4)) % q
            c2 = (-sum(co[4 + i] * tp[i] for i in range(4))) % q
            c1 = sum(co[8 + i] * tp[i] for i in range(4)) % q
            c0 = (-sum(co[12 + i] * tp[i] for i in range(4))) % q
            if c3 == 0:
                continue
            rs = cubic_roots(c3, c2, c1, c0, q)
            if len(rs) == 3:
                k += 1
                allsl.update(rs)
                trips8.append(sorted(rs))
                for r_ in rs:
                    if r_ in pool:
                        extra += 1
        hits.append((k, len(allsl)))
        if k == 8:
            slopehist[len(allsl)] = slopehist.get(len(allsl), 0) + 1
            ok, why, det = verify_struct(trips8)
            tag = why.split(":")[0].split("(")[0].strip()
            struct[tag] = struct.get(tag, 0) + 1
            if ok:
                legalhist[len(allsl)] = legalhist.get(len(allsl), 0) + 1
                if len(allsl) <= 13 and WIT[0] is None:
                    WIT[0] = (q, T[:], trips8, sorted(allsl), why)
        cand = (k, len(allsl), 3 * k - len(allsl), extra)
        if bestalloc is None or cand[0] > bestalloc[0] or \
           (cand[0] == bestalloc[0] and cand[1] < bestalloc[1]):
            bestalloc = cand
    ks = [h[0] for h in hits]
    p("      B2 ALLOC (15 prescribed incidences, %d draws, %d solved):"
      % (NA, len(hits)))
    p("         pencils sampled from %d with >=9 fibres; random 8-subsets"
      % len(POOLP))
    p("         mean fully-split fibres = %.3f of 8 ; max = %d"
      % (sum(ks) / float(len(ks)) if ks else 0, max(ks) if ks else 0))
    p("         best (k, |slopes|, C=3k-|slopes|, prescribed-slope hits) = %s"
      % (bestalloc,))
    p("         |slopes| histogram AT k = 8 (need <= 13): %s"
      % dict(sorted(slopehist.items())))
    p("         CEILING: min |slopes| at k=8 = %s ; DEMAND <= 13 ; SHORT BY %s"
      % (min(slopehist, default="n/a"),
         (min(slopehist) - 13) if slopehist else "n/a"))
    p("         coincidence currency: achieved C = %s vs demand C >= 11"
      % ((24 - min(slopehist)) if slopehist else "n/a"))
    p("      B2V STRUCTURAL VERIFICATION of every k=8, |slopes|<=13 draw")
    p("         (MISS-2 guard: |slopes| is NOT the constrained quantity)")
    p("         outcome tally over ALL k=8 draws = %s"
      % dict(sorted(struct.items())))
    p("         |slopes| histogram among STRUCTURALLY LEGAL k=8 draws: %s"
      % dict(sorted(legalhist.items())))
    p("         STRUCTURAL CEILING: min |slopes| over legal k=8 = %s"
      % min(legalhist, default="n/a"))
    p("         => legal coincidence supply C = %s ; DEMAND C >= 11"
      % ((24 - min(legalhist)) if legalhist else "n/a"))
    if WIT[0]:
        wq, wT, wtr, wsl, wwhy = WIT[0]
        p("         *** FULL STRUCTURAL WITNESS at q = %d ***" % wq)
        p("             fibre params t_j = %s" % wT[:8])
        p("             slope triples    = %s" % wtr)
        p("             slopes (%d)      = %s" % (len(wsl), wsl))
        p("             %s" % wwhy)
    else:
        p("         NO draw passed the structural verification.")
    p()
    flush()

p("=== SUMMARY ===")
p("total wall %.1f s" % (time.time() - T0))
flush()
print("\n".join(OUT))
