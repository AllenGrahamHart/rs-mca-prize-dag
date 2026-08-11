"""D2/D3 -- THE STRUCTURED SLOPE-MERGE (round 37).

Registered structure (PREREG R2.1-R2.4), verified in block V below.

  R(gamma,t) = U~(t)gamma^3 - E~_1(t)gamma^2 + E~_2(t)gamma - E~_3(t)
  is a bidegree-(3,3) form.  The monic slope cubic of fibre i is
  f_i(Z) = R(Z,t_i)/U~(t_i).  With A = {t_0..t_3}, B = {t_4..t_7} and
  L_i = the Lagrange basis on the four A-nodes,

      f_j = sum_{i in A} lambda_ji f_i ,
      lambda_ji = L_i(t_j) * U~(t_i)/U~(t_j) ,   sum_i lambda_ji = 1.

  Hence a merge on edge (i,j) -- a common root r of f_i and f_j -- is
  equivalent to (sum_{k != i} lambda_jk f_k)(r) = 0, a cubic that does
  NOT involve f_i.  So each A-block is DETERMINED by the other three,
  and the search is a block coordinate descent on (T_0,T_1,T_2,T_3).

  |slopes| = 24 - (#merges).  Target 13 slopes = 11 merges.  The merge
  graph is forced to be K_{4,4} minus a perfect matching minus one edge,
  degrees (3,3,3,2 | 3,3,3,2), realised here as
      adjA[0]=[1,2,3] adjA[1]=[0,2,3] adjA[2]=[0,1,3] adjA[3]=[1,2]

Writes d2_merge_results_<TAG>.txt (versioned) and appends d2_merge_ckpt.txt.
Stdlib only.  NO import of any banked script (r36's share3_pencil.py
flushes to r36's own results path AT MODULE LEVEL in "w" mode -- audited
and deliberately not imported).
"""
import random
import sys
import time

DIR = "notes/pilots_20260811/r37_share3_gap/"
TAG = sys.argv[1] if len(sys.argv) > 1 else "a"
FIELDS = [int(x) for x in (sys.argv[2].split(",") if len(sys.argv) > 2
                           else ["193", "257"])]
RESTARTS = int(sys.argv[3]) if len(sys.argv) > 3 else 400
DEADLINE = float(sys.argv[4]) if len(sys.argv) > 4 else 240.0

OUT = []
T0 = time.time()
adjA = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [1, 2]]
adjB = [[1, 2], [0, 2, 3], [0, 1, 3], [0, 1, 2]]


def p(s=""):
    OUT.append(str(s))


def flush():
    with open(DIR + "d2_merge_results_%s.txt" % TAG, "w") as f:
        f.write("\n".join(OUT) + "\n")


def mu(q, n):
    assert (q - 1) % n == 0
    for g in range(2, q):
        h = pow(g, (q - 1) // n, q)
        seen = set()
        x = 1
        for _ in range(n):
            seen.add(x)
            x = x * h % q
        if len(seen) == n:
            return sorted(seen)
    raise RuntimeError("no generator")


def pencils(q, need=8):
    """EXHAUSTIVE full-constant-norm pencils in the e3=1 slice (D1)."""
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
            A = (y1 - y2) % q
            B = (x2 - x1) % q
            if A:
                v = inv[A]
                A2, B2 = 1, B * v % q
            else:
                A2, B2 = 0, 1
            C2 = (-(A2 * x1 + B2 * y1)) % q
            lines.setdefault((A2, B2, C2), set()).update((s, t))
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
        A2, B2, C2 = key
        de1, de2 = (-B2) % q, A2 % q
        x1, y1, _ = pts[keep[0]]
        ts = []
        for s in keep:
            x, y, _ = pts[s]
            ts.append((x - x1) * inv[de1] % q if de1
                      else (y - y1) * inv[de2] % q)
        out.append((key, ts, [pts[s][2] for s in keep]))
    return D, inv, out


# ---------------- tiny polynomial layer (descending coeffs) ------------
def pev(f, x, q):
    r = 0
    for c in f:
        r = (r * x + c) % q
    return r


def proots(f, q):
    """all F_q roots of a poly of degree <= 3 (brute force, q <= 641)."""
    return [x for x in range(q) if pev(f, x, q) == 0]


def monic_from_roots(rs, q):
    f = [1]
    for r in rs:
        f = [(f[i] if i < len(f) else 0) * 1 for i in range(len(f))] + [0]
        pass
    # explicit expansion (3 roots)
    a, b, c = rs
    return [1, (-(a + b + c)) % q, (a * b + b * c + c * a) % q,
            (-(a * b * c)) % q]


def lincomb(fs, cs, q):
    out = [0, 0, 0, 0]
    for f, c in zip(fs, cs):
        for i in range(4):
            out[i] = (out[i] + c * f[i]) % q
    return out


def lam_matrix(q, ts, U, inv):
    """lambda[j][i] = L_i(t_{4+j}) U(t_i)/U(t_{4+j}) ; rows must sum to 1."""
    tA = ts[:4]
    Uv = [pev(U, t, q) for t in ts]
    if any(u == 0 for u in Uv):
        return None
    lam = []
    for j in range(4):
        tj = ts[4 + j]
        row = []
        for i in range(4):
            num, den = 1, 1
            for k in range(4):
                if k == i:
                    continue
                num = num * (tj - tA[k]) % q
                den = den * (tA[i] - tA[k]) % q
            row.append(num * inv[den] % q * Uv[i] % q * inv[Uv[4 + j]] % q)
        if sum(row) % q != 1:
            return None
        lam.append(row)
    return lam


# ---------------- V: verify the registered relation R2.3 --------------
def verify_R23(q, ts, inv, rng):
    """random Psi~ ; check f_j == sum_i lambda_ji f_i for all j in B."""
    for _ in range(60):
        U = [rng.randrange(q) for _ in range(4)]
        Es = [[rng.randrange(q) for _ in range(4)] for _ in range(3)]
        Uv = [pev(U, t, q) for t in ts]
        if any(u == 0 for u in Uv):
            continue
        f = []
        for a in range(8):
            iu = inv[Uv[a]]
            f.append([1] + [(-1) ** 0 * 0] * 3)
            f[a] = [1,
                    (-pev(Es[0], ts[a], q) * iu) % q,
                    (pev(Es[1], ts[a], q) * iu) % q,
                    (-pev(Es[2], ts[a], q) * iu) % q]
        lam = lam_matrix(q, ts, U, inv)
        if lam is None:
            continue
        ok = True
        for j in range(4):
            pred = lincomb(f[:4], lam[j], q)
            if pred != f[4 + j]:
                ok = False
        return ok
    return None


# ---------------- the block coordinate descent ------------------------
def slopes_of(Ts, lam, q):
    """all 8 triples' slope multisets ; returns (distinct, merges, fB) or None."""
    fA = [monic_from_roots(T, q) for T in Ts]
    allr = [list(T) for T in Ts]
    for j in range(4):
        fj = lincomb(fA, lam[j], q)
        if fj[0] != 1:
            return None
        rs = proots(fj, q)
        # need it to split with 3 roots (with multiplicity)
        full = []
        for r in rs:
            m = 0
            g = fj[:]
            while len(g) > 1 and pev(g, r, q) == 0:
                # synthetic division
                nq = [g[0]]
                for c in g[1:-1]:
                    nq.append((c + nq[-1] * r) % q)
                if (g[-1] + nq[-1] * r) % q != 0:
                    break
                g = nq
                m += 1
            full += [r] * m
        if len(full) != 3:
            return None
        allr.append(full)
    flat = [r for T in allr for r in T]
    return len(set(flat)), 24 - len(set(flat)), allr


def edge_count(Ts, lam, q):
    """#satisfied design edges (i,j): some root of f_i is a root of f_j.
    Pair multiplicity > 1 is PENALISED, never rewarded (R6 clause 2)."""
    fA = [monic_from_roots(T, q) for T in Ts]
    fB = [lincomb(fA, lam[j], q) for j in range(4)]
    tot = 0
    ed = []
    for j in range(4):
        for i in adjB[j]:
            hit = [r for r in set(Ts[i]) if pev(fB[j], r, q) == 0]
            if len(hit) == 1:
                tot += 1
                ed.append((i, j, hit[0]))
            elif len(hit) > 1:
                tot -= 1                      # pair multiplicity > 1: illegal
    # a slope may serve at most one B-partner (d_gamma <= 2)
    seen = {}
    for (i, j, r) in ed:
        seen[(i, r)] = seen.get((i, r), 0) + 1
    tot -= sum(v - 1 for v in seen.values())
    return tot, ed, fB


def descent(q, ts, inv, rng, sweeps=25):
    U = [rng.randrange(q) for _ in range(4)]
    lam = lam_matrix(q, ts, U, inv)
    if lam is None:
        return None
    Ts = [sorted(rng.sample(range(1, q), 3)) for _ in range(4)]
    best = (-1, None)
    cur = edge_count(Ts, lam, q)[0]
    for _ in range(sweeps):
        for i in range(4):
            others = [k for k in range(4) if k != i]
            fO = [monic_from_roots(Ts[k], q) for k in others]
            opts = []
            for j in adjA[i]:
                h = lincomb(fO, [lam[j][k] for k in others], q)
                rs = proots(h, q)
                if not rs:
                    opts = None
                    break
                opts.append(rs)
            if opts is None:
                continue
            cands = []
            if len(opts) == 3:
                for a in opts[0]:
                    for b in opts[1]:
                        for c in opts[2]:
                            if len({a, b, c}) == 3:
                                cands.append(sorted((a, b, c)))
            else:                                    # A3: degree 2 + private
                for a in opts[0]:
                    for b in opts[1]:
                        if a == b:
                            continue
                        for _ in range(3):
                            c = rng.randrange(1, q)
                            if c not in (a, b):
                                cands.append(sorted((a, b, c)))
            other_sl = set()
            for k in range(4):
                if k != i:
                    other_sl |= set(Ts[k])
            cands = [c for c in cands if not (set(c) & other_sl)]
            if not cands:
                continue
            old = Ts[i]
            bestc, bestv = None, -99
            for c in cands:
                Ts[i] = c
                v = edge_count(Ts, lam, q)[0]
                if v > bestv:
                    bestc, bestv = c, v
            Ts[i] = bestc if bestc is not None else old
            cur = bestv
            v, ed, fB = edge_count(Ts, lam, q)
            if v > best[0]:
                best = (v, ([list(T) for T in Ts], ed, U, lam, fB))
        if rng.random() < 0.25:                      # anneal: kick one block
            k = rng.randrange(4)
            Ts[k] = sorted(rng.sample(range(1, q), 3))
    return best


def structural_verify(q, ns, merges, allr):
    """R6 clause 2 -- the MISS-2 guard, on the actual object."""
    msg = []
    deg = {}
    for T in allr:
        for r in set(T):
            deg[r] = deg.get(r, 0) + 1
    if any(len(set(T)) != 3 for T in allr):
        msg.append("FAIL(e-distinct): a fibre has a repeated slope")
    if max(deg.values()) > 2:
        msg.append("FAIL(a-degree): max d_gamma = %d > 2" % max(deg.values()))
    pairs = {}
    for a in range(8):
        for b in range(a + 1, 8):
            c = len(set(allr[a]) & set(allr[b]))
            if c:
                pairs[(a, b)] = c
    if pairs and max(pairs.values()) > 1:
        msg.append("FAIL(b-pairmult): %d > 1" % max(pairs.values()))
    sides = {}
    for (a, b) in pairs:
        sides.setdefault(a, set()).add(b)
    bip = all((a < 4) != (b < 4) for (a, b) in pairs)
    if not bip:
        msg.append("FAIL(c-bipartite): a merge inside one side")
    if len(pairs) != merges:
        msg.append("FAIL(edge-count): %d edges vs %d merges"
                   % (len(pairs), merges))
    return msg


p("=== D2  STRUCTURED SLOPE-MERGE, round 37  (tag %s) ===" % TAG)
p("instrument: block coordinate descent on the registered relation R2.3")
p("|slopes| = 24 - #merges ; TARGET 13 slopes = 11 merges")
p()
flush()

for q in FIELDS:
    if time.time() - T0 > DEADLINE:
        p("!! DEADLINE before q=%d -- ZERO DRAWS, NOT a measurement" % q)
        break
    t1 = time.time()
    D, inv, pens = pencils(q)
    rng = random.Random(9000 + q)
    p("--- q = %d : constant-norm pencils with >= 8 disjoint fibres = %d"
      % (q, len(pens)))
    if not pens:
        p("    NO PENCIL AT THIS FIELD -- the class is EMPTY here"
          " (exhaustive, D1).")
        p()
        flush()
        continue
    key, tsall, trips = max(pens, key=lambda z: len(z[1]))
    p("    best pencil %s with %d complete disjoint fibres" % (key, len(tsall)))

    # ---- V : verify R2.3 on this field ----
    ts8 = tsall[:8]
    v = verify_R23(q, ts8, inv, rng)
    p("    V  REGISTERED RELATION R2.3  f_j = sum_i lambda_ji f_i : %s" % v)

    # ---- the descent ----
    hist = {}
    best = None
    nrun = 0
    while nrun < RESTARTS and time.time() - T0 < DEADLINE:
        key2, tsall2, _ = pens[rng.randrange(len(pens))]
        if len(tsall2) < 8:
            continue
        ts = rng.sample(tsall2, 8)
        r = descent(q, ts, inv, rng)
        nrun += 1
        if r is None or r[1] is None:
            continue
        hist[r[0]] = hist.get(r[0], 0) + 1
        if best is None or r[0] > best[0]:
            best = (r[0], r[1], ts)
    dt = time.time() - t1
    p("    descent restarts completed = %d ; wall %.1f s" % (nrun, dt))
    p("    MERGE-COUNT HISTOGRAM over restarts (|slopes| = 24 - merges):")
    p("      merges %s" % {k: hist[k] for k in sorted(hist)})
    p("      |slopes| %s" % {24 - k: hist[k] for k in sorted(hist, reverse=1)})
    if best:
        mg, (Ts, ed, U, lam, fB) , ts = best
        p("    BEST merges = %d  => |slopes| = %d   (need 11 => 13)"
          % (mg, 24 - mg))
        p("      U~ = %s ; t = %s" % (U, ts))
        p("      A-triples = %s" % (Ts,))
        p("      satisfied edges (i,j,slope) = %s" % (ed,))
        r2 = slopes_of(Ts, lam, q)
        if r2 is None:
            p("      (a B-cubic does not split: |slopes| not yet defined --"
              " R8.3 arithmetic tax)")
        else:
            p("      all 8 slope triples = %s" % (r2[2],))
            msgs = structural_verify(q, r2[0], r2[1], r2[2])
            p("      |slopes| (full check) = %d ; STRUCTURAL VERIFICATION: %s"
              % (r2[0], "PASS" if not msgs else "; ".join(msgs)))
    p()
    flush()
    with open(DIR + "d2_merge_ckpt.txt", "a") as f:
        f.write("tag=%s q=%d pens=%d restarts=%d best=%s hist=%s wall=%.1f\n"
                % (TAG, q, len(pens), nrun, best[0] if best else None,
                   {k: hist[k] for k in sorted(hist)}, dt))

p("total wall %.1f s" % (time.time() - T0))
flush()
print("\n".join(OUT))
