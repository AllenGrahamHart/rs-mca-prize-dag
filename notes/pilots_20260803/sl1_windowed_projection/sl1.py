#!/usr/bin/env python3
"""SL-1 WINDOWED PROJECTION — exhaustive toy verifier (pilot 2026-08-03).

PROFILE: local.   Run:  tools/ramguard local -- python3 <this>

Decides, exhaustively on toy rows, whether a BAND-PROPER joint-explanation
pair P (depth d in [ceil(h/2), h-2]) projects to agreement <= A-2 with
w_z -- at some member / at every member -- and whether the WINDOWED
upgrade of THEOREM 2 survives.

Quantities (PREREG.md section 0):
    a_P(z)    = agr(pi_z(P), w_z),  z in P^1(F_q)
    mult_P(z) = a_P(z) - |Z_P|
    LIVE_P    = {z : a_P(z) = A}        (live slopes, definitions item 7)
    OA_P      = {z : a_P(z) >= A-1}     (over-agreement members)
    cap_d     = (n-k-d)//(h-d)          (BANKED: bandlib `cap`)
    beta_d    = (n-k-d)//(h-d-1)
    W_d(z)    = #{c in C : k+d <= agr(c,w_z) <= A-2}
    b_d(z)    = #{depth-d pairs P : z in OA_P}

Checks P1-P9 and falsifiers F1-F8 of PREREG.md.

Banked machinery consumed READ-ONLY, never re-derived (hard law 5):
  bandlib.Row/plant/scan  (xr_graded_band_ledger)
  census.lagrange         (listsize_program; top-coefficient algebra of the
                           KEY LEMMA, background/nodes/
                           xr_band_key_lemma_pencil_mass)
The member-list enumeration is written here (not imported) because
census.profile() thresholds at a single tau, while this pilot needs the
per-member agreement-set census graded by SIZE across the whole window
[k+d, A-2] and the top tier {A-1, A}.
"""
import itertools
import json
import sys
from collections import defaultdict

sys.dont_write_bytecode = True
BASE = "/home/u2470931/smooth-read-solomin/prize/notes/"
sys.path.insert(0, BASE + "pilots_20260802/xr_graded_band_ledger")
sys.path.insert(0, BASE + "pilots_20260803/listsize_program")
from bandlib import Row, plant, scan            # noqa: E402  read-only
from census import lagrange                     # noqa: E402  read-only


# --------------------------------------------------------------- profiles
def pair_profile(row, u, v, Z):
    """(f, g, mult, slope_of) for the joint-explanation pair with core Z.

    slope_of[i] = the UNIQUE member of P^1(F_q) at which the non-core
    coordinate i joins the projection's agreement set (PREREG P1).
    """
    q, k, n = row.q, row.k, row.n
    Zl = sorted(Z)
    base = tuple(Zl[:k])
    f = row.interp(base, [u[i] for i in base])
    g = row.interp(base, [v[i] for i in base])
    mult = defaultdict(int)
    slope_of = {}
    bad = []
    for i in range(n):
        e = (u[i] - row.ev(f, row.xs[i])) % q
        ep = (v[i] - row.ev(g, row.xs[i])) % q
        if i in Z:
            if (e, ep) != (0, 0):
                bad.append(("core point not explained", i))
            continue
        if (e, ep) == (0, 0):
            bad.append(("core not maximal", i))
            continue
        z = 'inf' if ep == 0 else (-e) * pow(ep, q - 2, q) % q
        mult[z] += 1
        slope_of[i] = z
    return f, g, dict(mult), slope_of, bad


def member_census(row, u, v, dmin):
    """member -> {size: #distinct agreement sets}, EXHAUSTIVE.

    Every codeword c with agr(c, w_z) >= k arises as I_W(w_z) for any
    k-subset W of its agreement set; distinct agreement sets <-> distinct
    codewords (a codeword of degree < k is determined by any k points of
    its agreement set).  Only sizes >= k+dmin are retained.
    """
    n, k, q = row.n, row.k, row.q
    thr = k + dmin
    sets = defaultdict(set)
    for W in itertools.combinations(range(n), k):
        f = row.interp(W, [u[i] for i in W])
        g = row.interp(W, [v[i] for i in W])
        Z = []
        buck = defaultdict(list)
        zb = []
        for i in range(n):
            a = (row.ev(f, row.xs[i]) - u[i]) % q
            b = (row.ev(g, row.xs[i]) - v[i]) % q
            if a == 0 and b == 0:
                Z.append(i)
            elif b == 0:
                zb.append(i)
            else:
                buck[(-a) * pow(b, q - 2, q) % q].append(i)
        Zf = frozenset(Z)
        for z, extra in buck.items():
            S = Zf | frozenset(extra)
            if len(S) >= thr:
                sets[z].add(S)
        S = Zf | frozenset(zb)
        if len(S) >= thr:
            sets['inf'].add(S)
        if len(Zf) >= thr:                     # joint event: ALL members
            for z in range(q):
                if z not in buck:
                    sets[z].add(Zf)
            if not zb:
                sets['inf'].add(Zf)
    out = {}
    for m, ss in sets.items():
        c = defaultdict(int)
        for S in ss:
            c[len(S)] += 1
        out[m] = dict(c)
    return out


# -------------------------------------------------------------- fixtures
def plant_free(row, specs, seed, extra_random=True):
    """bandlib.plant generalised to blocks of ARBITRARY size.

    specs: [dict(Z=[...], blocks=[(slope z, [idx...]), ...]), ...]
    A block of size m on slope z gives mult_P(z) = m exactly, hence
    a_P(z) = |Z| + m.  bandlib.plant is the special case m = A - |Z|
    (live slope); this pilot needs m = A - 1 - |Z| as well.
    """
    import random
    rnd = random.Random(seed)
    n, k, q = row.n, row.k, row.q
    u = [None] * n
    v = [None] * n
    built = []
    for spec in specs:
        Z = list(spec["Z"])
        base = Z[:k]
        for i in base:
            if u[i] is None:
                u[i] = rnd.randrange(q)
                v[i] = rnd.randrange(1, q)
        f = row.interp(tuple(base), [u[i] for i in base])
        g = row.interp(tuple(base), [v[i] for i in base])
        for i in Z:
            if u[i] is None:
                u[i] = row.ev(f, row.xs[i])
                v[i] = row.ev(g, row.xs[i])
        built.append((f, g, frozenset(Z)))
    for spec, (f, g, Zf) in zip(specs, built):
        for z, blk in spec.get("blocks", []):
            for i in blk:
                assert u[i] is None, "block point already used"
                gi = row.ev(g, row.xs[i])
                vi = rnd.randrange(1, q)
                while vi == gi:
                    vi = rnd.randrange(1, q)
                v[i] = vi
                u[i] = (row.ev(f, row.xs[i]) + z * (gi - vi)) % q
    if extra_random:
        for i in range(n):
            if u[i] is None:
                u[i] = rnd.randrange(q)
                v[i] = rnd.randrange(1, q)
    return u, v


def fixtures():
    """(name, row, u, v, note).  Banked fixtures first, then new rows."""
    out = []

    # ---- BANKED calibration row: k=5, h=4, A=9; band proper = {2} = {h-2}
    r = Row(14, 5, 4, 101)
    spec = [dict(Z=list(range(7)), slopes=[1, 2], blocks=[[7, 8], [9, 10]])]
    for s in (11, 12):
        u, v, _ = plant(r, spec, seed=s)
        out.append((f"BANKED k5h4_core7_2slopes_s{s}", r, u, v,
                    "listsize census fixture; two planted live slopes"))
    spec1 = [dict(Z=list(range(7)), slopes=[3], blocks=[[7, 8]])]
    u, v, _ = plant(r, spec1, seed=13)
    out.append(("BANKED k5h4_core7_1slope", r, u, v,
                "L_P = 1: N_d = 0 but the pair still over-agrees"))
    spec2 = [dict(Z=list(range(7)), slopes=[1], blocks=[[7, 8]]),
             dict(Z=[0, 1, 2, 3, 9, 10, 11], slopes=[4], blocks=[[12, 13]])]
    u, v, _ = plant(r, spec2, seed=14)
    out.append(("BANKED k5h4_two_cores", r, u, v, "two disjoint-block cores"))
    import random
    for s in (21, 22):
        rnd = random.Random(s)
        u = [rnd.randrange(r.q) for _ in range(r.n)]
        v = [rnd.randrange(1, r.q) for _ in range(r.n)]
        out.append((f"BANKED k5h4_random_{s}", r, u, v, "random control"))
    r2 = Row(13, 4, 5, 61)
    spec3 = [dict(Z=list(range(7)), slopes=[2, 5], blocks=[[7, 8], [9, 10]])]
    u, v, _ = plant(r2, spec3, seed=31)
    out.append(("BANKED k4h5_core7_2slopes", r2, u, v, "second banked row"))
    rnd = random.Random(41)
    u = [rnd.randrange(r2.q) for _ in range(r2.n)]
    v = [rnd.randrange(1, r2.q) for _ in range(r2.n)]
    out.append(("BANKED k4h5_random", r2, u, v, "random control"))

    # ---- NEW: bare core, no planted block (PREREG P9 genericity)
    r3 = Row(14, 5, 4, 101)
    for s in (51, 52):
        u, v = plant_free(r3, [dict(Z=list(range(7)))], seed=s)
        out.append((f"NEW k5h4_bare_core_s{s}", r3, u, v,
                    "core only, no planted slope: P9 sharpness at d=h-2"))

    # ---- NEW: h = 6 row.  band proper = [3, 4]; d = 3 is INTERIOR
    #      core size k+3 = 6, block of size h-d-1 = 2 -> a_P(z) = 8 = A-1
    r4 = Row(14, 3, 6, 101)
    for s in (61, 62, 63):
        u, v = plant_free(r4, [dict(Z=list(range(6)),
                                    blocks=[(7, [6, 7]), (9, [8, 9])])],
                          seed=s)
        out.append((f"NEW k3h6_d3_A1blocks_s{s}", r4, u, v,
                    "F3 target: interior depth d=3<h-2, two A-1 members"))
    for s in (64, 65):
        u, v = plant_free(r4, [dict(Z=list(range(6)))], seed=s)
        out.append((f"NEW k3h6_d3_bare_s{s}", r4, u, v,
                    "interior depth, no planted block"))

    # ---- NEW: h = 7 row.  band proper = [4, 5]; d = 4 is INTERIOR
    r5 = Row(16, 3, 7, 101)
    for s in (71, 72):
        u, v = plant_free(r5, [dict(Z=list(range(7)),
                                    blocks=[(5, [7, 8]), (11, [9, 10])])],
                          seed=s)
        out.append((f"NEW k3h7_d4_A1blocks_s{s}", r5, u, v,
                    "F3 target: interior depth d=4<h-2, two A-1 members"))

    # ---- NEW: h = 6 row, block of size h-d = 3 at the INTERIOR depth
    #      -> a_P(z) = 9 = A exactly: a LIVE slope at an interior depth
    for s in (81, 82):
        u, v = plant_free(r4, [dict(Z=list(range(6)),
                                    blocks=[(7, [6, 7, 8]),
                                            (9, [9, 10, 11])])],
                          seed=s)
        out.append((f"NEW k3h6_d3_Ablocks_s{s}", r4, u, v,
                    "interior depth with two EXACT-A live slopes"))

    # ---- NEW: MULTI-CORE rows, so N_d^raw >= 2 and b_d(z) >= 2.
    #      h = 6, k = 3: three depth-3 cores, all over-agreeing at the
    #      SAME member z0 = 7 -> b_3(7) = 3 with W_3(7) small: the
    #      sharpest stress of the windowed inequality P8.
    C3 = [list(range(0, 6)), list(range(6, 12)), list(range(12, 18))]
    for q_ in (101, 1009):
        r6 = Row(24, 3, 6, q_)
        for s in (91, 92):
            u, v = plant_free(r6, [dict(Z=Z) for Z in C3], seed=s)
            out.append((f"NEW k3h6_3cores_bare_q{q_}_s{s}", r6, u, v,
                        "three depth-3 cores, no planted block"))
        for s in (93, 94):
            u, v = plant_free(
                r6, [dict(Z=C3[0], blocks=[(7, [18, 19])]),
                     dict(Z=C3[1], blocks=[(7, [20, 21])]),
                     dict(Z=C3[2], blocks=[(7, [22, 23])])], seed=s)
            out.append((f"NEW k3h6_3cores_sharedA1_q{q_}_s{s}", r6, u, v,
                        "three depth-3 cores ALL over-agreeing at z=7"))
    # ---- NEW: h = 6 row at d = h-2 = 4 (core k+4 = 7), the UPPER end of
    #      band proper: reaching A-1 costs a SINGLE extra point (P10).
    for s in (101, 102, 103):
        u, v = plant_free(r4, [dict(Z=list(range(7)))], seed=s)
        out.append((f"NEW k3h6_d4_bare_s{s}", r4, u, v,
                    "d = h-2 upper end, no planted block: P10"))
    r6b = Row(24, 3, 6, 1009)
    for s in (104, 105):
        u, v = plant_free(r6b, [dict(Z=list(range(7)))], seed=s)
        out.append((f"NEW k3h6_d4_bare_q1009_s{s}", r6b, u, v,
                    "d = h-2 at large q: over-agreement still forced"))
    # two depth-3 cores with EXACT-A blocks on a shared slope
    r7 = Row(20, 3, 6, 101)
    for s in (95, 96):
        u, v = plant_free(
            r7, [dict(Z=C3[0], blocks=[(7, [12, 13, 14])]),
                 dict(Z=C3[1], blocks=[(7, [15, 16, 17])])], seed=s)
        out.append((f"NEW k3h6_2cores_sharedA_s{s}", r7, u, v,
                    "two depth-3 cores, both LIVE at the same z=7"))
    return out


# ------------------------------------------------------------------ main
def main():
    results = []
    fails = []
    fired = defaultdict(list)

    def note(fid, name, detail):
        fired[fid].append((name, detail))

    for name, r, u, v, desc in fixtures():
        n, k, q, A, h = r.n, r.k, r.q, r.A, r.h
        dlo, dhi = (h + 1) // 2, h - 2
        rec = dict(name=name, desc=desc, n=n, k=k, h=h, A=A, q=q,
                   band_proper=[dlo, dhi])
        if dlo > dhi:
            results.append(rec)
            continue

        # ---------- exhaustive joint-explanation census -----------------
        cores = {}
        for W in itertools.combinations(range(n), k):
            f = r.interp(W, [u[i] for i in W])
            g = r.interp(W, [v[i] for i in W])
            Z = [i for i in range(n)
                 if (r.ev(f, r.xs[i]) - u[i]) % q == 0
                 and (r.ev(g, r.xs[i]) - v[i]) % q == 0]
            cores[frozenset(Z)] = len(Z)
        maxJ = max(cores.values())

        # ---------- per-pair projection profiles ------------------------
        prof = {}
        for Z in cores:
            f, g, mult, slope_of, bad = pair_profile(r, u, v, Z)
            if bad:
                fails.append((name, "profile", bad[:3]))
            d = len(Z) - k
            aP = {z: len(Z) + m for z, m in mult.items()}
            live = {z for z, a in aP.items() if a == A}
            oa = {z for z, a in aP.items() if a >= A - 1}
            prof[Z] = dict(d=d, mult=mult, slope_of=slope_of, aP=aP,
                           live=live, oa=oa,
                           maxa=max(aP.values()) if aP else len(Z))

        # ---------- admissibility gates ---------------------------------
        max_a = max((p["maxa"] for p in prof.values()), default=0)
        gates = dict(v_nonvanishing=all(x != 0 for x in v),
                     tangent_gate=max_a <= A,
                     below_cascade=maxJ <= A - 2,
                     kpacking=True)
        big = [Z for Z in cores if len(Z) >= k]
        for a_ in range(len(big)):
            for b_ in range(a_ + 1, len(big)):
                if len(big[a_] & big[b_]) > k - 1:
                    gates["kpacking"] = False
        admissible = all(gates.values())
        # A fixture failing the TANGENT GATE is outside every hypothesis
        # list in the lane (H3); the listsize pilot already excludes the
        # two banked ones as a planting artifact.  Their violations are
        # RECORDED but are not hard failures: P2 *is* the gate.
        excluded = not gates["tangent_gate"]
        rec.update(gates=gates, admissible=admissible, max_joint=maxJ,
                   max_projection_agreement=max_a, gate_excluded=excluded)

        # ---------- P1 / P2 / P5 / P6 / P7 ------------------------------
        p1 = p2 = p6 = 0
        for Z, p in prof.items():
            d = p["d"]
            if sum(p["mult"].values()) != n - k - d:          # P1 / F7
                p1 += 1
                fails.append((name, "P1 identity", (sorted(Z), d)))
                note("F7", name, sorted(Z))
            if p["maxa"] > A:                                  # P2
                p2 += 1
                if not excluded:
                    fails.append((name, "P2 gate", (sorted(Z), p["maxa"])))
            if 0 <= d <= h - 1 and h - d > 0:
                cap = (n - k - d) // (h - d)
                if len(p["live"]) > cap:                       # P6 / F5
                    p6 += 1
                    fails.append((name, "P6 line cap",
                                  (sorted(Z), len(p["live"]), cap)))
                    note("F5", name, ("cap", sorted(Z)))
            if h - d - 1 >= 1:
                beta = (n - k - d) // (h - d - 1)
                if len(p["oa"]) > beta:                        # P6 / F5
                    p6 += 1
                    fails.append((name, "P6 beta", (sorted(Z),
                                                    len(p["oa"]), beta)))
                    note("F5", name, ("beta", sorted(Z)))
        rec.update(P1_violations=p1, P2_violations=p2, P6_violations=p6)

        # P5: LIVE_P (finite part) must equal bandlib's live-slope count.
        # bandlib.scan omits the (0:1) direction (occupancy caveat 6), so
        # the comparison is on z in F_q only, with the inf part reported.
        bpairs, _ = scan(r, u, v)
        p5 = 0
        inf_live = 0
        n_live_ge2 = 0
        for Z, p in prof.items():
            mine = {z for z in p["live"] if z != 'inf'}
            if 'inf' in p["live"]:
                inf_live += 1
            if len(p["live"]) >= 2 and dlo <= p["d"] <= dhi:
                n_live_ge2 += 1
            sl = bpairs.get(Z, dict(slopes={}))["slopes"]
            theirs = {z for z, s_ in sl.items() if s_ == A}
            if mine != theirs:
                p5 += 1
                if not excluded:
                    fails.append((name, "P5 live-slope mismatch",
                                  (sorted(Z), sorted(mine), sorted(theirs))))
        rec.update(P5_violations=p5, pairs_with_live_inf=inf_live,
                   band_proper_pairs_with_L_ge_2=n_live_ge2)

        # P7 / F4: over-agreement sets are NOT joint-explanation sets.
        p7 = 0
        checked7 = 0
        for Z, p in prof.items():
            for z in p["oa"]:
                S = sorted(set(Z) | {i for i, zz in p["slope_of"].items()
                                     if zz == z})
                checked7 += 1
                Acf = lagrange(r, S, [u[i] for i in S])[k:]
                Bcf = lagrange(r, S, [v[i] for i in S])[k:]
                if not any(Acf) and not any(Bcf):
                    p7 += 1
                    note("F4", name, (sorted(Z), z, len(S)))
                    if gates["below_cascade"]:
                        fails.append((name, "P7 member-privacy",
                                      (sorted(Z), z, len(S))))
        rec.update(P7_violations=p7, P7_checked=checked7)

        # ---------- SL-1 proper, on BAND-PROPER pairs -------------------
        bp = {Z: p for Z, p in prof.items() if dlo <= p["d"] <= dhi}
        sl1 = []
        for Z, p in bp.items():
            d = p["d"]
            clean = (q + 1) - len(p["aP"])        # members with mult = 0
            ev = dict(d=d, core=len(Z), maxa=p["maxa"],
                      mina=k + d,                  # every unlisted member
                      n_over=len(p["oa"]), n_live=len(p["live"]),
                      clean_members=clean,
                      sl1_every_member=(p["maxa"] <= A - 2),
                      sl1_some_member=(clean > 0))
            # P10: at d = h-2 the extra point needed to reach A-1 is a
            # SINGLE non-core point, so over-agreement is unavoidable.
            ev["P10_forced_over_agreement"] = (
                d == h - 2 and n > k + d and p["maxa"] >= A - 1)
            sl1.append(ev)
            if not ev["sl1_some_member"]:                       # F1
                note("F1", name, ev)
                fails.append((name, "F1 SL-1 fails at EVERY member", ev))
            if d == h - 2 and n > k + d and p["maxa"] < A - 1 and admissible:
                fails.append((name, "P10 d=h-2 not forced", ev))
            if not ev["sl1_every_member"] and admissible:       # F2
                note("F2", name, ev)
                if d < dhi:                                     # F3
                    note("F3", name, ev)
        rec["band_proper_pairs"] = sl1

        # ---------- windowed reduction (P8 / F6) ------------------------
        cens = member_census(r, u, v, dlo)
        members = list(range(q)) + ['inf']
        wind = []
        for d in range(dlo, dhi + 1):
            Nraw = sum(1 for Z in cores if len(Z) == k + d)
            if Nraw == 0:
                continue
            beta = (n - k - d) // (h - d - 1)
            bz = defaultdict(int)
            for Z, p in prof.items():
                if p["d"] != d:
                    continue
                for z in p["oa"]:
                    bz[z] += 1
            sumW = 0
            worst = None
            inj_bad = 0
            for m in members:
                c = cens.get(m, {})
                W = sum(v_ for s_, v_ in c.items() if k + d <= s_ <= A - 2)
                T = sum(v_ for s_, v_ in c.items() if s_ >= A - 1)
                sumW += W
                if Nraw > W + bz.get(m, 0):                     # P8 / F6
                    fails.append((name, f"P8 window d={d}",
                                  (m, Nraw, W, bz.get(m, 0))))
                    note("F6", name, (d, m, Nraw, W, bz.get(m, 0)))
                if worst is None or W + bz.get(m, 0) < worst[1]:
                    worst = (m, W + bz.get(m, 0), W, bz.get(m, 0), T)
                # THEOREM 2 injectivity, checked directly at this member
            for m in members:
                seen = {}
                for Z, p in prof.items():
                    if p["d"] != d:
                        continue
                    S = frozenset(set(Z) | {i for i, zz
                                            in p["slope_of"].items()
                                            if zz == m})
                    if S in seen:
                        inj_bad += 1
                    seen[S] = Z
            if inj_bad and not excluded:
                fails.append((name, f"T2 injectivity d={d}", inj_bad))
            good = [m for m in members if bz.get(m, 0) == 0]
            minWgood = min((sum(v_ for s_, v_ in cens.get(m, {}).items()
                                if k + d <= s_ <= A - 2) for m in good),
                           default=None)
            agg_ok = (q + 1) * Nraw <= sumW + beta * Nraw
            if not agg_ok:
                fails.append((name, f"P8 aggregate d={d}",
                              (Nraw, sumW, beta)))
                note("F6", name, ("aggregate", d))
            if beta * Nraw < q + 1 and not good:                # F8
                note("F8", name, (d, Nraw, beta))
                fails.append((name, f"F8 no clean member d={d}", (Nraw, beta)))
            wind.append(dict(d=d, N_raw=Nraw, beta=beta,
                             sum_W=sumW, avg_W=sumW / (q + 1),
                             aggregate_ok=agg_ok,
                             injectivity_violations=inj_bad,
                             best_member=worst, n_good_members=len(good),
                             min_W_over_good=minWgood,
                             n_members_with_OA=len(bz)))
        rec["windowed"] = wind
        results.append(rec)

        sl1e = sum(1 for e in sl1 if e["sl1_every_member"])
        sl1s = sum(1 for e in sl1 if e["sl1_some_member"])
        print(f"{name:34s} adm={str(admissible):5s} bp_pairs={len(sl1):3d} "
              f"SL1@every={sl1e:3d}/{len(sl1):<3d} "
              f"SL1@some={sl1s:3d}/{len(sl1):<3d} "
              f"maxJ={maxJ} maxproj={max_a} (A={A}) "
              f"P1={p1} P5={p5} P6={p6} P7={p7}")

    out = dict(results=results,
               falsifiers={f: dict(n=len(v_), sample=v_[:3])
                           for f, v_ in fired.items()},
               fails=fails, verdict="PASS" if not fails else "FAIL")
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("\nVERDICT:", out["verdict"], " hard failures:", len(fails))
    for f in fails[:12]:
        print("  FAIL", f)
    print("\nFALSIFIERS FIRED:")
    for f in sorted(fired):
        print(f"  {f}: {len(fired[f])} occurrences, e.g. {fired[f][0]}")
    for f in ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"]:
        if f not in fired:
            print(f"  {f}: NOT FIRED")


if __name__ == "__main__":
    main()
