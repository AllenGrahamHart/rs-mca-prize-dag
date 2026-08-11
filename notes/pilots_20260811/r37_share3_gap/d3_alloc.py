"""D1(c)/D2/D3 -- THE INCIDENCE-RANK INSTRUMENT (round 37).

Derived form (PREREG R2.1).  An incidence "gamma is a type-2 slope at the
fibre over t" is the single LINEAR condition

    w(t)^T Psi v(gamma) = 0 ,   w(t) = (1,t,t^2,t^3),
                                v(g) = (g^3, -g^2, g, -1),

on the 4x4 matrix Psi = Psi~ (16 coefficients, P^15).  Each condition is
a RANK-ONE tensor w(t) (x) v(gamma) in F_q^16, so the whole search is
linear algebra on a 16-dimensional space, and:

  * ALLOC  (anchor 1's instrument, replicated here): prescribe 15
    incidences, solve the 1-dimensional null space, count the merges that
    actually occur.  15 conditions buy at most floor(15/2) = 7 designed
    merges; the rest are free coincidences.
  * RANK-GREEDY (new here): process the 11 design edges in order and, for
    each, SCAN gamma over F_q choosing the value whose 2 new rows raise
    the rank LEAST.  A merge that costs 1 instead of 2 is exactly the
    degeneracy the 13-slope variety is made of (R2.2: the variety has
    dimension 15 - 11 = 4, so on it the average cost per edge is 1).

|slopes| = 24 - #merges ; the target is 11 merges = 13 slopes.
Writes d3_alloc_results_<TAG>.txt (versioned); appends d3_alloc_ckpt.txt.
Stdlib only; no banked-script import.
"""
import random
import sys
import time

DIR = "notes/pilots_20260811/r37_share3_gap/"
TAG = sys.argv[1] if len(sys.argv) > 1 else "a"
FIELDS = [int(x) for x in (sys.argv[2].split(",") if len(sys.argv) > 2
                           else ["193"])]
NDRAW = int(sys.argv[3]) if len(sys.argv) > 3 else 300
DEADLINE = float(sys.argv[4]) if len(sys.argv) > 4 else 250.0

OUT = []
T0 = time.time()
EDGES = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 2), (1, 3),
         (2, 0), (2, 1), (2, 3), (3, 1), (3, 2)]      # (A-index, B-index)


def p(s=""):
    OUT.append(str(s))


def flush():
    with open(DIR + "d3_alloc_results_%s.txt" % TAG, "w") as f:
        f.write("\n".join(OUT) + "\n")


def mu(q, n):
    assert (q - 1) % n == 0
    for g in range(2, q):
        h = pow(g, (q - 1) // n, q)
        seen, x = set(), 1
        for _ in range(n):
            seen.add(x)
            x = x * h % q
        if len(seen) == n:
            return sorted(seen)
    raise RuntimeError("no generator")


def pencils(q, need=8):
    D = mu(q, 64)
    pos = {x: i for i, x in enumerate(D)}
    inv = [0] * q
    for a in range(1, q):
        inv[a] = pow(a, q - 2, q)
    pts = []
    for ii in range(64):
        a = D[ii]
        for jj in range(ii + 1, 64):
            b = D[jj]
            ab = a * b % q
            kk = pos[inv[ab]]
            if kk <= jj:
                continue
            c = D[kk]
            pts.append(((a + b + c) % q, (ab + c * (a + b)) % q, (ii, jj, kk)))
    lines = {}
    n = len(pts)
    for s in range(n):
        x1, y1, _ = pts[s]
        for t in range(s + 1, n):
            x2, y2, _ = pts[t]
            A, B = (y1 - y2) % q, (x2 - x1) % q
            if A:
                A2, B2 = 1, B * inv[A] % q
            else:
                A2, B2 = 0, 1
            lines.setdefault((A2, B2, (-(A2 * x1 + B2 * y1)) % q),
                             set()).update((s, t))
    out = []
    for key, mem in lines.items():
        if len(mem) < need:
            continue
        mem = sorted(mem)
        cnt = {}
        for s in mem:
            for r in pts[s][2]:
                cnt[r] = cnt.get(r, 0) + 1
        rep = [r for r, c in cnt.items() if c > 1]
        keep = [s for s in mem if not rep or rep[0] not in pts[s][2]]
        if len(keep) < need:
            continue
        A2, B2, _ = key
        de1 = (-B2) % q
        x1, y1, _ = pts[keep[0]]
        ts = [((pts[s][0] - x1) * inv[de1] % q) if de1
              else ((pts[s][1] - y1) * inv[A2] % q) for s in keep]
        out.append((key, ts))
    return D, inv, out


# ---------------- F_q linear algebra on 16-vectors ----------------
def reduce_row(basis, row, q):
    """row-reduce `row` against the reduced `basis` (list of (piv,vec))."""
    row = row[:]
    for piv, vec in basis:
        if row[piv]:
            c = row[piv]
            for k in range(piv, 16):
                row[k] = (row[k] - c * vec[k]) % q
    for k in range(16):
        if row[k]:
            return k, row
    return None, row


def add_row(basis, row, q, inv):
    piv, row = reduce_row(basis, row, q)
    if piv is None:
        return False
    c = inv[row[piv]]
    for k in range(piv, 16):
        row[k] = row[k] * c % q
    basis.append((piv, row))
    basis.sort()
    return True


def inc_row(t, g, q):
    """the rank-one tensor w(t) (x) v(gamma) as a length-16 row."""
    w = [1, t % q, t * t % q, t * t % q * t % q]
    g2 = g * g % q
    v = [g2 * g % q, (-g2) % q, g % q, q - 1]
    return [w[a] * v[b] % q for a in range(4) for b in range(4)]


def nullvec(basis, q, inv, rng):
    """one nonzero vector killed by every basis row (dim >= 1 assumed)."""
    piv = [b[0] for b in basis]
    free = [k for k in range(16) if k not in piv]
    if not free:
        return None
    x = [0] * 16
    for k in free:
        x[k] = rng.randrange(q)
    if not any(x):
        x[free[0]] = 1
    for pv, vec in reversed(basis):
        s = 0
        for k in range(pv + 1, 16):
            s = (s + vec[k] * x[k]) % q
        x[pv] = (-s) % q
    return x if any(x) else None


def triples(Psi, ts, q):
    """the 8 slope triples ; None if a fibre is degenerate or non-split."""
    out = []
    for t in ts:
        w = [1, t % q, t * t % q, t * t % q * t % q]
        c = [sum(w[a] * Psi[4 * a + b] for a in range(4)) % q
             for b in range(4)]
        if c[0] == 0:
            return None                       # U~(t_i) = 0 : c_x = 0, illegal
        f = [c[0], (-c[1]) % q, c[2], (-c[3]) % q]
        rs = []
        for x in range(q):
            v = 0
            for co in f:
                v = (v * x + co) % q
            if v == 0:
                rs.append(x)
        if len(rs) != 3:
            return None                       # not split into 3 DISTINCT roots
        out.append(rs)
    return out


def verify(tr):
    """R6 clause 2 on the actual object.  Returns (nslopes, merges, msgs)."""
    msgs = []
    deg = {}
    for T in tr:
        for r in T:
            deg[r] = deg.get(r, 0) + 1
    ns = len(deg)
    mg = 24 - ns
    if max(deg.values()) > 2:
        msgs.append("d_gamma=%d>2" % max(deg.values()))
    pm = 0
    for a in range(8):
        for b in range(a + 1, 8):
            pm = max(pm, len(set(tr[a]) & set(tr[b])))
    if pm > 1:
        msgs.append("pairmult=%d>1" % pm)
    return ns, mg, msgs


p("=== D3  INCIDENCE-RANK INSTRUMENT (ALLOC replication + RANK-GREEDY) ===")
p("each incidence = ONE linear condition w(t) (x) v(gamma) on Psi in P^15")
p("|slopes| = 24 - merges ; TARGET 11 merges = 13 slopes")
p()
flush()

for q in FIELDS:
    if time.time() - T0 > DEADLINE:
        p("!! DEADLINE before q=%d -- ZERO DRAWS, NOT a measurement" % q)
        break
    t1 = time.time()
    D, inv, pens = pencils(q)
    rng = random.Random(37000 + q)
    p("--- q = %d : constant-norm pencils with >= 8 disjoint fibres = %d"
      % (q, len(pens)))
    if not pens:
        p("    class EMPTY at this field (exhaustive, D1) -- no draws.")
        p()
        flush()
        continue
    for MODE in ("ALLOC", "RANK-GREEDY"):
        hist = {}
        bestrec = None
        nd = 0
        costs = {}
        ranks = {}
        pres = {}
        lastp = 0
        freeh = {}
        while nd < NDRAW and time.time() - T0 < DEADLINE:
            _, tsall = pens[rng.randrange(len(pens))]
            if len(tsall) < 8:
                continue
            ts = rng.sample(tsall, 8)
            basis = []
            nd += 1
            if MODE == "ALLOC":
                # 7 designed merges (14 rows) + 1 spare = 15 conditions
                used = set()
                for (i, j) in EDGES[:7]:
                    g = rng.randrange(q)
                    while g in used:
                        g = rng.randrange(q)
                    used.add(g)
                    add_row(basis, inc_row(ts[i], g, q), q, inv)
                    add_row(basis, inc_row(ts[4 + j], g, q), q, inv)
                g = rng.randrange(q)
                add_row(basis, inc_row(ts[0], g, q), q, inv)
            else:
                order = EDGES[:]
                rng.shuffle(order)
                used = set()
                npres = 0
                # ALL 11 edges, greedily minimising the FINAL rank.
                # A 13-slope configuration exists iff that rank is <= 15.
                for (i, j) in order:
                    cheap = []
                    fb = []
                    for g in range(1, q):
                        if g in used:
                            continue
                        b2 = [(pv, v[:]) for (pv, v) in basis]
                        c = 0
                        c += 1 if add_row(b2, inc_row(ts[i], g, q), q,
                                          inv) else 0
                        c += 1 if add_row(b2, inc_row(ts[4 + j], g, q), q,
                                          inv) else 0
                        if c <= 1:
                            cheap.append((c, g))
                        elif len(fb) < 40:
                            fb.append((c, g))
                    if cheap:
                        bestc, bestg = rng.choice(cheap)
                    elif fb and len(basis) + 2 <= 15:
                        bestc, bestg = rng.choice(fb)
                    else:
                        continue                # would break the rank budget
                    if len(basis) + bestc > 15:
                        continue
                    npres += 1
                    costs.setdefault(len(basis), {})
                    costs[len(basis)][bestc] = \
                        costs[len(basis)].get(bestc, 0) + 1
                    used.add(bestg)
                    add_row(basis, inc_row(ts[i], bestg, q), q, inv)
                    add_row(basis, inc_row(ts[4 + j], bestg, q), q, inv)
                ranks[len(basis)] = ranks.get(len(basis), 0) + 1
                pres[npres] = pres.get(npres, 0) + 1
                lastp = npres
            if len(basis) > 15:
                continue
            x = nullvec(basis, q, inv, rng)
            if x is None:
                continue
            tr = triples(x, ts, q)
            if tr is None:
                continue
            ns, mg, msgs = verify(tr)
            key = ns if not msgs else "ILLEGAL"
            hist[key] = hist.get(key, 0) + 1
            if MODE == "RANK-GREEDY" and not msgs:
                freeh[mg - lastp] = freeh.get(mg - lastp, 0) + 1
            if not msgs and (bestrec is None or ns < bestrec[0]):
                bestrec = (ns, mg, tr, ts, x)
        dt = time.time() - t1
        p("    [%s] draws = %d ; wall %.1f s" % (MODE, nd, dt))
        p("      LEGAL |slopes| HISTOGRAM (ILLEGAL = guard R6.2 killed it):")
        p("        %s" % {k: hist[k] for k in sorted(
            hist, key=lambda z: (isinstance(z, str), z))})
        if MODE == "RANK-GREEDY":
            p("      FINAL RANK under the 15-budget: %s"
              % {k: ranks[k] for k in sorted(ranks)})
            p("      PRESCRIBED design edges per draw (of 11 needed): %s"
              % {k: pres[k] for k in sorted(pres)})
            p("      FREE merges on top of the prescribed ones: %s"
              % {k: freeh[k] for k in sorted(freeh)})
            p("      per-edge cost by CURRENT DIM (cost 1 = the degeneracy):")
            for d0 in sorted(costs):
                p("        dim %2d -> %s" % (d0, costs[d0]))
        if bestrec:
            ns, mg, tr, ts, x = bestrec
            p("      BEST LEGAL |slopes| = %d  (merges %d ; need 13 / 11)"
              % (ns, mg))
            p("        t = %s" % (ts,))
            p("        triples = %s" % (tr,))
            if ns <= 13:
                p("        *** 13-SLOPE CONFIGURATION -- Psi = %s" % (x,))
        else:
            p("      NO legal configuration in this cell")
        p()
        flush()
        with open(DIR + "d3_alloc_ckpt.txt", "a") as f:
            f.write("tag=%s q=%d mode=%s draws=%d best=%s hist=%s wall=%.1f\n"
                    % (TAG, q, MODE, nd, bestrec[0] if bestrec else None,
                       {str(k): v for k, v in hist.items()}, dt))

p("total wall %.1f s" % (time.time() - T0))
flush()
print("\n".join(OUT))
