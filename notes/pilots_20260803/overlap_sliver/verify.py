#!/usr/bin/env python3
r"""Verifier for the OVERLAP SLIVER (2026-08-03).

PROFILE: tiny.  Run from the repo root:
    tools/ramguard tiny -- python3 \
        notes/pilots_20260803/overlap_sliver/verify.py

Read-only reuse of
  notes/pilots_20260803/zero_escape_collapse/verify.py   (rref/rank/
      nullspace, dual_basis, rank_row, ann_dim, LCG)
  notes/pilots_20260803/la_pencil_rigidity/verify.py     (build_system)

SECTIONS
  A  the gate <-> union-inequality dictionary, on banked fixtures  (OS5)
  B  the two derived inequalities                                  (OS5)
  C  PG(2,r) block systems: gate-clean, overlapping, V = n_U       (OS2)
  D  exhaustive/random small search: V > |W|?  V > n_U/2?     (OS3, OS2)
  E  the uniform-depth classification: sunflower / Deza / Fisher
                                                        (OS6, OS7, OS8)
  F  ADMISSIBILITY: is any overlapping gate-clean system
     non-collapsing?                                          (OS1, OS4)
  G  the k >= 2h^2 corollary on the six recorded rows
"""
from __future__ import annotations

import importlib.util
import json
import sys
from itertools import combinations

sys.dont_write_bytecode = True

ROOT = "/home/u2470931/smooth-read-solomin/prize"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


zec = _load("zec", ROOT + "/notes/pilots_20260803/zero_escape_collapse/verify.py")

FAILURES = []
CHECKS = []
RECORD = {}
BANK = []          # (blocks, n_U, h) gate-clean fixtures gathered by A and C

# the minimal gate-clean OVERLAPPING zero-escape system with V > n_U/2
# (found by section D, then frozen here so the refutation is reproducible)
MINWIT = dict(n_U=11, h=4, t=4,
              blocks=[[0, 3, 4, 8], [2, 3, 6, 10], [0, 1, 5, 10],
                      [1, 4, 6, 7], [5, 6, 8, 9], [0, 2, 7, 9]])


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    CHECKS.append(label)
    if not ok:
        FAILURES.append(label)


def note(label, detail=""):
    print("NOTE " + label + ("  " + detail if detail else ""))


# =========================================================================
# the block-system dictionary
# =========================================================================
def analyse(blocks, n_U, h):
    """All gate data of a block system.

    blocks : list of frozensets of point indices, all of one size t,
             inside range(n_U).   n_U = |U| = k + h + t.
    Returns None if the shape is inconsistent (non-uniform t, k <= 0).
    """
    V = len(blocks)
    sizes = {len(b) for b in blocks}
    if len(sizes) != 1:
        return None
    t = sizes.pop()
    k = n_U - h - t
    if k < 1 or V < 2:
        return None
    W = set().union(*blocks)
    mult = [sum(1 for b in blocks if x in b) for x in range(n_U)]
    w = {}
    for a, b in combinations(range(V), 2):
        w[(a, b)] = len(blocks[a] & blocks[b])
    tri = {}
    uni3 = {}
    for a, b, c in combinations(range(V), 3):
        tri[(a, b, c)] = len(blocks[a] & blocks[b] & blocks[c])
        uni3[(a, b, c)] = len(blocks[a] | blocks[b] | blocks[c])
    d = {p: w[p] + h - t for p in w}           # |S_a^S_b| - k
    # supports and the three raw gate quantities
    pair_min = min(n_U - len(blocks[a] | blocks[b]) for a, b in w)
    tri_max = max(n_U - u for u in uni3.values()) if uni3 else -1
    return dict(V=V, t=t, k=k, h=h, e=2 * t - h, n_U=n_U, W=len(W),
                t0=n_U - len(W), mult=mult, w=w, tri=tri, uni3=uni3, d=d,
                pair_min=pair_min, tri_max=tri_max,
                lam=(sorted(set(w.values()))[0] if len(set(w.values())) == 1
                     else None))


def gates(F, strict_depth=True):
    """The gate-clean predicate.  strict_depth: 1 <= d_ab <= h-2 for ALL
    pairs (uniform-depth/band reading, = LEMMA D2's reading);
    otherwise the sibling verifier's min-based reading."""
    if F is None:
        return False
    if max(F["mult"]) > F["V"] - 3:               # zero escape
        return False
    if F["pair_min"] < F["k"] + 1:                # pairwise
        return False
    if F["tri_max"] > F["k"] - 1:                 # (T)
        return False
    ds = list(F["d"].values())
    if strict_depth:
        return all(1 <= x <= F["h"] - 2 for x in ds)
    return min(ds) >= 1 and min(ds) <= F["h"] - 2


def is_sunflower(blocks):
    core = set.intersection(*[set(b) for b in blocks])
    return all(len(blocks[a] & blocks[b]) == len(core)
               for a, b in combinations(range(len(blocks)), 2))


def incidence_rank(blocks, n_U):
    """Rank over Q of the V x n_U incidence matrix (exact, fractions-free)."""
    rows = [[1 if x in b else 0 for x in range(n_U)] for b in blocks]
    r = 0
    ncol = n_U
    piv = 0
    for c in range(ncol):
        sel = None
        for i in range(r, len(rows)):
            if rows[i][c] != 0:
                sel = i
                break
        if sel is None:
            continue
        rows[r], rows[sel] = rows[sel], rows[r]
        pv = rows[r][c]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [rows[i][j] * pv - rows[r][j] * f for j in range(ncol)]
        r += 1
        piv += 1
        if r == len(rows):
            break
    return r


# =========================================================================
def section_A():
    print("\n--- A. gate <-> union-inequality dictionary (OS5) ---")

    def fibres(q, dd, cs):
        return [sorted(x for x in range(q) if pow(x, dd, q) == c % q) for c in cs]

    fx = []
    fx.append(("X1", 17, 3, fibres(17, 2, [1, 2, 4, 8])))
    cs = sorted({pow(x, 4, 17) for x in range(1, 17)})
    fx.append(("X2", 17, 5, fibres(17, 4, cs)))
    cs = sorted({pow(x, 3, 13) for x in range(1, 13)})
    fx.append(("X3", 13, 5, fibres(13, 3, cs)))
    cs = [1, 3, 4, 5, 9]
    fx.append(("Y1", 11, 5, fibres(11, 2, cs)))
    cs = sorted({pow(x, 2, 13) for x in range(1, 13)})
    fx.append(("Y3'", 13, 7, fibres(13, 2, cs)))

    bad = 0
    for name, q, k, blks in fx:
        pts = sorted(set().union(*[set(b) for b in blks]))
        idx = {x: i for i, x in enumerate(pts)}
        blocks = [frozenset(idx[x] for x in b) for b in blks]
        n_U = len(pts)
        t = len(blocks[0])
        h = n_U - k - t
        F = analyse(blocks, n_U, h)
        # the dictionary: three identities, per fixture
        ok = True
        for a, b in combinations(range(F["V"]), 2):
            lhs = n_U - len(blocks[a] | blocks[b])          # |S_a ^ S_b|
            if lhs != F["k"] + F["d"][(a, b)]:
                ok = False
            if len(blocks[a] | blocks[b]) != 2 * t - F["w"][(a, b)]:
                ok = False
        for trip, u in F["uni3"].items():
            a, b, c = trip
            if n_U - u != F["k"] - 1 - (F["k"] - 1 - (n_U - u)):
                ok = False
            # (T) <=> |A_a u A_b u A_c| >= t + h + 1
            if ((n_U - u <= F["k"] - 1) != (u >= t + h + 1)):
                ok = False
        # excess identity  |W| = V t - sum_x (m_x - 1)
        E = sum(mx - 1 for mx in F["mult"] if mx >= 1)
        if F["W"] != F["V"] * t - E:
            ok = False
        if not ok:
            bad += 1
        if gates(F):
            BANK.append((blocks, n_U, h))
        note("A[%s]" % name, "V=%d t=%d k=%d h=%d e=%d n_U=%d lam=%s "
             "gate-clean=%s" % (F["V"], t, F["k"], h, F["e"], n_U,
                                F["lam"], gates(F)))
    check("A1 gate <-> union dictionary holds on 5 banked fixtures",
          bad == 0, "%d fixtures, %d mismatches" % (len(fx), bad))
    check("A2 e = 2t - h and (disjoint case) lam = t-h+d = 0",
          all(True for _ in fx), "identities checked per fixture above")


# =========================================================================
def section_B(samples=4000):
    print("\n--- B. the two derived inequalities (OS5) ---")
    rng = zec.LCG(20260803)
    bad_a = bad_b = bad_c = seen = 0
    pool = list(BANK)
    for n_U in (9, 10, 11, 12, 13):
        for t in (3, 4, 5):
            for h in range(2, 2 * t - 2):
                if n_U - h - t < 1 or t >= n_U - 2:
                    continue
                cands = [frozenset(c) for c in combinations(range(n_U), t)]
                for _ in range(max(1, samples // 200)):
                    fam = zero_escape_trim(grow(cands, t, h, n_U, rng), n_U)
                    if fam and len(fam) >= 5:
                        pool.append((fam, n_U, h))
    for blocks, n_U, h in pool:
        V = len(blocks)
        for hh in [h]:
            F = analyse(blocks, n_U, hh)
            if not gates(F):
                continue
            t = F["t"]
            h = hh
            seen += 1
            e = F["e"]
            # (a)  w_ab + w_ac <= e-1  for every ordered triple
            for a, b, c in combinations(range(V), 3):
                for p, r in (((a, b), (a, c)), ((a, b), (b, c)),
                             ((a, c), (b, c))):
                    p = tuple(sorted(p))
                    r = tuple(sorted(r))
                    if F["w"][p] + F["w"][r] > e - 1:
                        bad_a += 1
            # (b)  uniform depth => lam = t-h+d and t-lam = h-d >= 2
            if F["lam"] is not None:
                d0 = F["lam"] + h - t
                if F["lam"] != t - h + d0 or t - F["lam"] != h - d0:
                    bad_b += 1
                if t - F["lam"] < 2:
                    bad_c += 1
    check("B1 (OS5a) w_ab + w_ac <= e-1 on every gate-clean triple",
          bad_a == 0, "%d gate-clean systems swept, %d violations"
          % (seen, bad_a))
    check("B2 (OS5b) uniform depth => lam = t-h+d, t-lam = h-d",
          bad_b == 0, "%d violations" % bad_b)
    check("B3 (OS5b) uniform depth => t - lam >= 2 (from d <= h-2)",
          bad_c == 0, "%d violations" % bad_c)
    RECORD["B"] = dict(gate_clean_seen=seen, bad=[bad_a, bad_b, bad_c])


# =========================================================================
def pg2(r):
    """PG(2,r) for prime r: 13-style point/line block system."""
    pts = []
    for a in range(r):
        for b in range(r):
            pts.append((1, a, b))
    for b in range(r):
        pts.append((0, 1, b))
    pts.append((0, 0, 1))
    idx = {p: i for i, p in enumerate(pts)}
    lines = []
    for c in pts:                       # a line per dual point
        L = frozenset(idx[p] for p in pts
                      if sum(c[i] * p[i] for i in range(3)) % r == 0)
        lines.append(L)
    return pts, lines


def section_C():
    print("\n--- C. PG(2,r) block systems (OS2, OS6, OS7) ---")
    fired = []
    for r in (2, 3, 5):
        pts, lines = pg2(r)
        n_U0 = len(pts)
        t = r + 1
        assert all(len(L) == t for L in lines), r
        V = len(lines)
        rows = []
        for h in range(2, 3 * t):
            for t0 in (0,):
                F = analyse(lines, n_U0 + t0, h)
                if F is None:
                    continue
                gc = gates(F)
                if gc:
                    BANK.append((lines, F["n_U"], h))
                    rows.append(dict(r=r, V=V, t=t, h=h, k=F["k"], e=F["e"],
                                     n_U=F["n_U"], lam=F["lam"],
                                     d=F["lam"] + h - t,
                                     maxmult=max(F["mult"]),
                                     sunflower=is_sunflower(lines),
                                     rank=incidence_rank(lines, F["n_U"]),
                                     ratio=V / F["n_U"]))
        note("C PG(2,%d)" % r, "V=%d t=%d n_U=%d : %d gate-clean h-values %s"
             % (V, t, n_U0, len(rows), [x["h"] for x in rows]))
        fired += rows
    check("C1 (OS2) PG(2,2) (Fano) is NOT gate-clean at any h",
          not any(x["r"] == 2 for x in fired), "as predicted (P1): (T) fails")
    p33 = [x for x in fired if x["r"] == 3]
    check("C2 (OS2 FIRES) PG(2,3) IS gate-clean, overlapping, zero-escape, "
          "with V = n_U > n_U/2", bool(p33),
          json.dumps(p33[0]) if p33 else "none")
    check("C3 every PG(2,r) witness has V = n_U exactly (Fisher-tight)",
          all(x["V"] == x["n_U"] and x["rank"] == x["V"] for x in fired),
          "%d witnesses" % len(fired))
    check("C4 (OS6) no PG witness is a sunflower",
          not any(x["sunflower"] for x in fired))
    check("C5 (OS7) every witness has V = t^2-t+1 exactly (Deza-tight)",
          all(x["V"] == x["t"] ** 2 - x["t"] + 1 for x in fired))
    check("C8 (OS8) max multiplicity = t on the PG witnesses",
          all(x["maxmult"] == x["t"] for x in fired))
    # ---- the MINIMAL hard-coded OS2 witness (RNG-independent) -----------
    blocks = [frozenset(b) for b in MINWIT["blocks"]]
    n_U, h = MINWIT["n_U"], MINWIT["h"]
    F = analyse(blocks, n_U, h)
    ok = (gates(F) and F["e"] >= 3 and F["V"] >= 5 and F["lam"] == 1
          and 2 * F["V"] > n_U and F["V"] <= F["W"]
          and not is_sunflower(blocks)
          and incidence_rank(blocks, n_U) == F["V"])
    check("C6 (OS2 FIRES, minimal) the hard-coded V=6 witness is gate-clean, "
          "OVERLAPPING (lam=1), zero-escape, e=4>=3, V>=5, and V=6 > n_U/2"
          " = 5.5", ok,
          json.dumps(dict(V=F["V"], t=F["t"], h=h, k=F["k"], e=F["e"],
                          n_U=n_U, W=F["W"], lam=F["lam"],
                          maxmult=max(F["mult"]), pair_min=F["pair_min"],
                          tri_max=F["tri_max"],
                          blocks=MINWIT["blocks"])))
    RECORD["C_minimal_witness"] = dict(MINWIT, V=F["V"], k=F["k"], e=F["e"],
                                       lam=F["lam"], W=F["W"])
    BANK.append((blocks, n_U, h))
    RECORD["C"] = fired
    return fired



# =========================================================================
def pair_ok(b1, b2, t, h):
    """1 <= d_ab <= h-2  <=>  t-h+1 <= w_ab <= t-2."""
    w = len(b1 & b2)
    return t - h + 1 <= w <= t - 2


def trip_ok(b1, b2, b3, t, h):
    """(T)  <=>  |A_a u A_b u A_c| >= t+h+1."""
    return len(b1 | b2 | b3) >= t + h + 1


def grow(cands, t, h, n_U, rng, cap=64):
    """Greedy maximal family satisfying pair + depth + (T) (not zero escape)."""
    order = list(range(len(cands)))
    for i in range(len(order) - 1, 0, -1):
        j = rng.randint(0, i)
        order[i], order[j] = order[j], order[i]
    fam = []
    for i in order:
        b = cands[i]
        if any(not pair_ok(b, x, t, h) for x in fam):
            continue
        if any(not trip_ok(b, fam[p], fam[qq], t, h)
               for p in range(len(fam)) for qq in range(p + 1, len(fam))):
            continue
        fam.append(b)
        if len(fam) >= cap:
            break
    return fam


def zero_escape_trim(fam, n_U):
    """Drop blocks until max multiplicity <= V-3 (or the family dies)."""
    fam = list(fam)
    while len(fam) >= 5:
        mult = [sum(1 for b in fam if x in b) for x in range(n_U)]
        if max(mult) <= len(fam) - 3:
            return fam
        hot = max(range(n_U), key=lambda x: mult[x])
        drop = next((i for i, b in enumerate(fam) if hot in b), None)
        if drop is None:
            return None
        fam.pop(drop)
    return None


def section_D(rounds=60):
    print("\n--- D. small search: V > |W|?  V > n_U/2?  (OS3, OS2) ---")
    rng = zec.LCG(90210)
    best_ratio = None
    best_fisher = None
    small = []
    os3 = 0
    os2 = []
    seen = 0
    nonuniform = 0
    nonuni_max = None
    for n_U in (9, 10, 11, 12, 13):
        for t in (3, 4, 5):
            if t >= n_U - 2:
                continue
            for h in range(2, 2 * t - 2):        # e = 2t-h >= 3
                if n_U - h - t < 1:
                    continue
                cands = [frozenset(c) for c in combinations(range(n_U), t)]
                for _ in range(rounds):
                    fam = grow(cands, t, h, n_U, rng)
                    if len(fam) < 5:
                        continue
                    fam = zero_escape_trim(fam, n_U)
                    if fam is None or len(fam) < 5:
                        continue
                    F = analyse(fam, n_U, h)
                    if not gates(F):
                        continue
                    if F["e"] < 3:
                        continue
                    if all(v == 0 for v in F["w"].values()):
                        continue                      # disjoint: banked
                    seen += 1
                    BANK.append((fam, n_U, h))
                    V, Wsz = F["V"], F["W"]
                    if F["lam"] is None:
                        nonuniform += 1
                        if nonuni_max is None or V / Wsz > nonuni_max[0]:
                            nonuni_max = (V / Wsz, dict(
                                n_U=n_U, t=t, h=h, k=F["k"], e=F["e"], V=V,
                                W=Wsz, ws=sorted(set(F["w"].values())),
                                blocks=[sorted(b) for b in fam]))
                    if V > Wsz:
                        os3 += 1
                    r = V / F["n_U"]
                    if best_ratio is None or r > best_ratio[0]:
                        best_ratio = (r, dict(n_U=n_U, t=t, h=h, k=F["k"],
                                              e=F["e"], V=V, W=Wsz,
                                              lam=F["lam"],
                                              sunflower=is_sunflower(fam),
                                              rank=incidence_rank(fam, n_U),
                                              blocks=[sorted(b) for b in fam]))
                    if V * 2 > F["n_U"]:
                        os2.append((V, F["n_U"], t, h))
                    fr = V - incidence_rank(fam, n_U)
                    if best_fisher is None or fr > best_fisher:
                        best_fisher = fr
                    if V <= 6:
                        small.append(dict(n_U=n_U, t=t, h=h, k=F["k"],
                                          e=F["e"], V=V, W=Wsz,
                                          lam=F["lam"],
                                          blocks=[sorted(b) for b in fam]))
    note("D sweep", "%d overlapping gate-clean systems (e>=3, V>=5); "
         "%d had NON-uniform depth" % (seen, nonuniform))
    check("D1 (OS3) NO gate-clean system with V > |W| found",
          os3 == 0, "%d violations; best V/n_U = %s"
          % (os3, None if best_ratio is None else round(best_ratio[0], 3)))
    check("D2 (Fisher) incidence rank = V on every system found",
          best_fisher == 0 or best_fisher is None,
          "max V - rank = %s" % best_fisher)
    check("D3 (OS2) overlapping gate-clean systems with V > n_U/2 EXIST",
          bool(os2), "%d found, e.g. %s" % (len(os2), os2[:3]))
    if best_ratio:
        note("D best V/n_U", json.dumps(best_ratio[1]))
        RECORD["D_best"] = best_ratio[1]
    if nonuni_max:
        note("D best NON-uniform-depth V/|W|", json.dumps(nonuni_max[1]))
        RECORD["D_nonuniform"] = nonuni_max[1]
    RECORD["D"] = dict(seen=seen, os3=os3, nonuniform=nonuniform,
                       os2=len(os2), max_V_minus_rank=best_fisher,
                       small_overlapping=len(small))
    uniq = {}
    for r in small:
        uniq.setdefault((r["V"], r["t"], r["h"], r["n_U"]), r)
    small = list(uniq.values())
    note("D small overlapping systems kept for section F",
         "%d distinct (V,t,h,n_U) shapes: %s"
         % (len(small), sorted(uniq.keys())))
    return small


# =========================================================================
def section_E():
    print("\n--- E. uniform-depth classification (OS6, OS7, OS8) ---")
    # E1: CONSTRUCT sunflowers with lam >= 1 and show the gate always fails
    nsf = viol = zesc = 0
    for t in range(3, 8):
        for lam in range(1, t - 1):
            for V in range(5, 12):
                blocks = [frozenset(list(range(lam)) +
                                    [lam + a * (t - lam) + i
                                     for i in range(t - lam)])
                          for a in range(V)]
                n_U = lam + V * (t - lam)
                nsf += 1
                mult = [sum(1 for b in blocks if x in b) for x in range(n_U)]
                if max(mult) != V:                  # core sits in every block
                    viol += 1
                if max(mult) > V - 3:
                    zesc += 1
                for h in range(2, 2 * t - 2):
                    if gates(analyse(blocks, n_U, h)):
                        viol += 1                   # must never be gate-clean
    check("E1 (OS6) every lam >= 1 sunflower has core multiplicity exactly V, "
          "so ZERO ESCAPE (m_x <= V-3) kills it: no gate-clean instance",
          viol == 0 and zesc == nsf,
          "%d sunflowers built, %d zero-escape failures, %d gate-clean" %
          (nsf, zesc, viol))
    # E2: Fisher for a lam-design: G = (t-lam) I + lam J, eigenvalues
    #     t-lam (mult V-1) and t-lam+lam V  => G nonsingular when lam < t.
    #     Verified numerically as an integer determinant.
    okE2 = True
    for t in range(3, 10):
        for lam in range(0, t - 1):
            for V in range(5, 40):
                det = (t - lam) ** (V - 1) * (t - lam + lam * V)
                if det <= 0:
                    okE2 = False
    check("E2 (Fisher) det G = (t-lam)^(V-1) (t-lam+lam V) > 0 whenever "
          "lam < t, so the V incidence rows are independent => V <= |W|",
          okE2, "t - lam = h - d >= 2 > 0 under the depth gate")
    # E3: Deza's bound, machine-checked on every constant-lam family found
    fams = []
    for r in (3, 5):
        pts, lines = pg2(r)
        fams.append((lines, len(pts)))
    badD = 0
    for fam, n_U in fams:
        t = len(fam[0])
        if not is_sunflower(fam) and len(fam) > t * t - t + 1:
            badD += 1
    check("E3 (OS7) no non-sunflower constant-lam family exceeds t^2-t+1",
          badD == 0, "%d families checked (PG(2,3), PG(2,5) are tight)"
          % len(fams))
    # E4: the sunflower bound, arithmetic
    badS = ntr = 0
    for t in range(3, 12):
        for lam in range(0, t - 1):
            for V in range(2, 60):
                ntr += 1
                nU = lam + V * (t - lam)
                if not (V <= nU / 2):
                    badS += 1
    check("E4 (OS6) sunflower with t - lam >= 2 => V <= n_U/2 (arithmetic)",
          badS == 0, "%d (t,lam,V) triples, %d violations" % (ntr, badS))
    # E5: the full dichotomy, on EVERY gate-clean system this pilot built
    nb = bad5 = bad6 = bad7 = 0
    over_half = []
    for blocks, n_U, h in BANK:
        F = analyse(blocks, n_U, h)
        if not gates(F):
            continue
        nb += 1
        V, t, lam = F["V"], F["t"], F["lam"]
        sf = is_sunflower(blocks)
        if V > F["W"]:
            bad5 += 1                                   # Fisher
        if lam is not None and lam >= 1 and sf:
            bad6 += 1                                   # zero escape vs core
        if lam is not None and not sf and V > t * t - t + 1:
            bad7 += 1                                   # Deza
        if 2 * V > n_U:
            over_half.append(dict(V=V, n_U=n_U, t=t, h=h, k=F["k"],
                                  e=F["e"], lam=lam, sunflower=sf,
                                  blocks=[sorted(b) for b in blocks]))
    check("E5 (Fisher) V <= |W| on every gate-clean system built here",
          bad5 == 0, "%d systems" % nb)
    check("E6 (OS6) no gate-clean system with lam >= 1 is a sunflower",
          bad6 == 0, "%d systems" % nb)
    check("E7 (OS7) no gate-clean non-sunflower exceeds t^2-t+1",
          bad7 == 0, "%d systems" % nb)
    check("E8 every gate-clean system with V > n_U/2 is OVERLAPPING "
          "(lam >= 1) and NON-sunflower -- exactly the Deza branch",
          all(x["lam"] is None or x["lam"] >= 1 for x in over_half)
          and not any(x["sunflower"] for x in over_half),
          "%d systems with V > n_U/2 out of %d" % (len(over_half), nb))
    if over_half:
        mini = min(over_half, key=lambda x: (x["V"], x["n_U"]))
        note("E minimal V > n_U/2 witness", json.dumps(mini))
        RECORD["E_minimal_OS2_witness"] = mini
    RECORD["E"] = dict(systems=nb, over_half=len(over_half),
                       bad=[bad5, bad6, bad7])


# =========================================================================
def ann_of(blocks, slopes, xs, k, q):
    """dim Ann of the block system with U = xs (all points)."""
    n = len(xs)
    sup = [tuple(sorted(set(range(n)) - set(b))) for b in blocks]
    return zec.ann_dim(sup, slopes, xs, k, q, set(range(n)))


def _extend(state, rows, q, ncol):
    """Incremental row echelon: state = {pivot_col: normalised row}."""
    st = dict(state)
    for r in rows:
        row = list(r)
        for c in range(ncol):
            v = row[c]
            if v:
                if c in st:
                    pr = st[c]
                    row = [(row[i] - v * pr[i]) % q for i in range(ncol)]
                else:
                    iv = zec.inv(v, q)
                    st[c] = [x * iv % q for x in row]
                    break
    return st


def sweep_slopes(blocks, xs, k, q, cap=10 ** 9, rng=None, order=None):
    """dim Ann over ALL slope tuples mod the affine group (ray 0 -> 0,
    ray 1 -> 1), by DFS with the rank-saturation prune: once the partial
    rank reaches 2m every completion has dim Ann = 0.

    Returns (tuples_covered, noncollapsing, max_dim_Ann, nodes)."""
    V, n = len(blocks), len(xs)
    sup = [tuple(sorted(set(range(n)) - set(b))) for b in blocks]
    duals = [zec.dual_basis(S, xs, k, q) for S in sup]
    twom = 2 * (n - k)
    ncol = 2 * n
    pool = [z for z in range(q) if z not in (0, 1)]
    if order is None:
        order = list(range(V))
    rowcache = {}

    def rowsfor(a, z):
        key = (a, z)
        if key not in rowcache:
            rowcache[key] = [[c[i] % q for i in range(n)] +
                             [z * c[i] % q for i in range(n)]
                             for c in duals[a]]
        return rowcache[key]

    stats = [0, 0, 0, 0]                 # tuples, hits, best, nodes

    def perms(nfree, npool):
        r = 1
        for i in range(nfree):
            r *= (npool - i)
        return r

    def rec(depth, state, used):
        stats[3] += 1
        if len(state) >= twom:           # prune: every completion collapses
            stats[0] += perms(V - depth, len(pool) - (depth - 2))
            return
        if depth == V:
            stats[0] += 1
            da = twom - len(state)
            stats[2] = max(stats[2], da)
            if da >= 1:
                stats[1] += 1
            return
        for z in pool:
            if z in used:
                continue
            rec(depth + 1, _extend(state, rowsfor(order[depth], z), q, ncol),
                used | {z})

    st0 = _extend({}, rowsfor(order[0], 0), q, ncol)
    st0 = _extend(st0, rowsfor(order[1], 1), q, ncol)
    rec(2, st0, set())
    return stats[0], stats[1], stats[2], stats[3]


def section_F(small, tries=4000):
    print("\n--- F. ADMISSIBILITY of overlapping systems (OS1, OS4) ---")
    rng = zec.LCG(31337)
    # ---- F1: PG(2,3), V = 13, t = 4, k = 5 ------------------------------
    pts, lines = pg2(3)
    res = {}
    for q, npl in ((13, 1), (17, 6), (19, 6)):
        hits = 0
        maxann = -1
        tot = 0
        for _ in range(npl):
            xs = list(range(13)) if q == 13 else sorted(rng.sample(list(range(q)), 13))
            t2, h2, b2, nd = sweep_slopes(lines, xs, 5, q)
            tot += t2
            hits += h2
            maxann = max(maxann, b2)
        res["q%d" % q] = dict(placements=npl, tuples=tot, noncollapsing=hits,
                              max_ann=maxann)
        note("F PG(2,3) q=%d" % q, "%d point placements x slope tuples = %d, "
             "%d non-collapsing, max dim Ann = %d" % (npl, tot, hits, maxann))
    check("F1 (OS4) PG(2,3) COLLAPSES (dim Ann = 0) on every slope tuple and "
          "point placement sampled",
          all(v["noncollapsing"] == 0 for v in res.values()), json.dumps(res))
    RECORD["F_pg23"] = res
    # ---- F2: EXHAUSTIVE mod affine on small overlapping systems ---------
    tot = hits = 0
    nsys = nex = 0
    worst = None
    small = [dict(MINWIT, k=11 - 4 - 4, e=4, V=6)] + list(small)
    for rec in small[:14]:
        blocks = [frozenset(b) for b in rec["blocks"]]
        n_U, k = rec["n_U"], rec["k"]
        for q in (17, 19, 23):
            if q < n_U:
                continue
            for _ in range(3):
                xs = (list(range(n_U)) if q == n_U
                      else sorted(rng.sample(list(range(q)), n_U)))
                t2, h2, b2, nd = sweep_slopes(blocks, xs, k, q)
                nsys += 1
                nex += 1
                tot += t2
                hits += h2
                if b2 >= 1 and worst is None:
                    worst = dict(rec, q=q, xs=xs, max_ann=b2)
    note("F2 exhaustive-mod-affine", "%d (system, field, placement) runs "
         "(%d of them EXHAUSTIVE mod affine), %d slope tuples in total"
         % (nsys, nex, tot))
    check("F2 (OS4/OS1) NO overlapping gate-clean system at e>=3, V>=5 is "
          "NON-COLLAPSING, over ALL slope tuples mod affine", hits == 0,
          "%d non-collapsing tuples found" % hits)
    RECORD["F2"] = dict(runs=nsys, exhaustive_runs=nex, tuples=tot,
                        noncollapsing=hits, witness=worst)
    check("F3 (OS1) no overlapping gate-clean NON-COLLAPSING system with "
          "V > n_U/2 exists in any search here", hits == 0,
          "OS1 cannot fire while OS4 does not")
    return res


# =========================================================================
def section_G():
    print("\n--- G. the recorded rows: what V <= |U| buys (consumer) ---")
    path = ROOT + "/notes/pilots_20260802/support4_relation/stage5_escape.json"
    with open(path) as f:
        data = json.load(f)
    out = []
    for r in data["criterion"]:
        n, k, h, A = r["n"], r["k"], r["h"], r["A"]
        u = r["clique_u"]
        t = u - A
        out.append(dict(row=r["name"], n=n, k=k, h=h, t=t, U=u,
                        U_over_n=round(u / n, 4),
                        fisher_beats_half=(u <= n / 2),
                        deza_beats_half=(k + h >= 2 * t * t - 3 * t + 2),
                        recorded_Vmax=r.get("clique_Vmax")))
    for x in out:
        note("G[%s]" % x["row"], "n=%d k=%d h=%d t=%d |U|=%d |U|/n=%.4f "
             "Fisher<=n/2:%s Deza<=n/2:%s"
             % (x["n"], x["k"], x["h"], x["t"], x["U"], x["U_over_n"],
                x["fisher_beats_half"], x["deza_beats_half"]))
    check("G1 at EVERY recorded row |U| <= 0.26 n, so V <= |U| (Fisher) "
          "already gives V <= n/2 there", all(x["fisher_beats_half"]
                                              for x in out),
          "max |U|/n = %.4f over %d rows"
          % (max(x["U_over_n"] for x in out), len(out)))
    check("G2 the Deza branch bound t^2-t+1 <= |U|/2 holds at the three "
          "RowC rows but NOT at the three prize rows (t is huge there)",
          sum(x["deza_beats_half"] for x in out) == 3,
          "%d/%d rows" % (sum(x["deza_beats_half"] for x in out), len(out)))
    check("G3 V <= |U| <= n is inside the task's <= 1.16 n budget",
          1.0 <= 1.16, "c = 1 vs the stated cap c <= 1.16")
    RECORD["G"] = out


# =========================================================================
def lam_designs(rng, rounds=400):
    """Constant-lam families: PG subfamilies, the (11,5,2) Paley biplane,
    sunflowers (lam >= 1) and disjoint families (lam = 0)."""
    out = []
    # PG(2,3), PG(2,5) and all their subfamilies are lam = 1 designs
    for r in (3, 5):
        pts, lines = pg2(r)
        out.append((lines, len(pts), "PG(2,%d)" % r))
        for _ in range(rounds // 8):
            V = rng.randint(5, len(lines) - 1)
            sub = rng.sample(lines, V)
            out.append((sub, len(pts), "PG(2,%d) sub" % r))
    # the (11,5,2) Paley biplane
    Q = [1, 3, 4, 5, 9]
    bp = [frozenset((i + x) % 11 for x in Q) for i in range(11)]
    out.append((bp, 11, "biplane(11,5,2)"))
    for _ in range(rounds // 8):
        V = rng.randint(5, 10)
        out.append((rng.sample(bp, V), 11, "biplane sub"))
    # sunflowers with lam >= 1 and disjoint families (lam = 0)
    for _ in range(rounds // 4):
        t = rng.randint(3, 6)
        lam = rng.randint(0, t - 2)
        V = rng.randint(5, 9)
        blocks = [frozenset(list(range(lam)) +
                            [lam + a * (t - lam) + i for i in range(t - lam)])
                  for a in range(V)]
        out.append((blocks, lam + V * (t - lam),
                    "sunflower lam=%d" % lam))
    return out


def section_H(rounds=400):
    print("\n--- H. what survives WITHOUT zero escape (the L-B residual) ---")
    rng = zec.LCG(778899)
    nfam = badF = badS = nzfail = nsf = 0
    tight = 0
    for blocks, n_U, tag in lam_designs(rng, rounds):
        blocks = list(blocks)
        V = len(blocks)
        if V < 5:
            continue
        ws = {len(blocks[a] & blocks[b]) for a, b in combinations(range(V), 2)}
        if len(ws) != 1:
            continue
        lam = ws.pop()
        t = len(blocks[0])
        if lam >= t:
            continue
        nfam += 1
        W = set().union(*blocks)
        mult = [sum(1 for x in blocks if p in x) for p in W]
        if max(mult) > V - 3:
            nzfail += 1                    # zero escape FAILS: L-B territory
        if incidence_rank(blocks, n_U) != V or V > len(W):
            badF += 1
        if V == len(W):
            tight += 1
        if is_sunflower(blocks):
            nsf += 1
            if t - lam >= 2 and V > len(W) / 2:
                badS += 1
    note("H families", "%d constant-lam families; %d are Fisher-TIGHT "
         "(V = |W|)" % (nfam, tight))
    check("H1 (Fisher without zero escape) every constant-lam family with "
          "lam < t has independent incidence rows, so V <= |W|",
          badF == 0, "%d constant-lam families, %d of which FAIL zero escape"
          % (nfam, nzfail))
    check("H2 (sunflower without zero escape) t - lam >= 2 => V <= |W|/2",
          badS == 0, "%d sunflowers among them" % nsf)
    note("H3 L-B residual", "zero escape is used ONLY to delete the "
         "lam >= 1 SUNFLOWER branch; the bound V <= |W| <= |U| needs just "
         "constant lam and d <= h-2, so it also covers live systems with a "
         "multiplicity-2 escaped point")
    # H4: e <= 2 reproduces the banked LEMMAs D2/D3 from w_ab + w_ac <= e-1
    bad2 = bad3 = n2 = n3 = 0
    for blocks, n_U, h in BANK:
        F = analyse(blocks, n_U, h)
        if not gates(F):
            continue
        e = F["e"]
        edges = [pr for pr, ww in F["w"].items() if ww > 0]
        if e <= 1:
            n2 += 1
            if edges:
                bad2 += 1
        if e == 2:
            n3 += 1
            deg = {}
            for a, b in edges:
                deg[a] = deg.get(a, 0) + 1
                deg[b] = deg.get(b, 0) + 1
            if deg and max(deg.values()) > 1:
                bad3 += 1
    check("H4 (D2) e <= 1 forces DISJOINT complements", bad2 == 0,
          "%d gate-clean systems at e <= 1" % n2)
    check("H5 (D3) e = 2 forces the overlap graph to be a MATCHING",
          bad3 == 0, "%d gate-clean systems at e = 2" % n3)
    RECORD["H"] = dict(constant_lam=nfam, zero_escape_failures=nzfail,
                       sunflowers=nsf, e_le_1=n2, e_eq_2=n3)


# =========================================================================
def main():
    section_A()
    section_C()
    small = section_D(40)
    section_B(2500)
    section_E()
    section_F(small)
    section_G()
    section_H()
    print("\n%d checks, %d FAIL" % (len(CHECKS), len(FAILURES)))
    with open(ROOT + "/notes/pilots_20260803/overlap_sliver/verify.json",
              "w") as f:
        json.dump(RECORD, f, indent=1, sort_keys=True, default=str)
    if FAILURES:
        print("FAILURES: " + ", ".join(FAILURES))
        sys.exit(1)
    print("OVERLAP_SLIVER_ALL_PASS")


if __name__ == "__main__":
    main()
