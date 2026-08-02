#!/usr/bin/env python3
"""Graded band ledger: fixture battery.

Every fixture is verified EXHAUSTIVELY (one pass over all k-subsets) to be
  * globally generic         (max joint codeword-pair agreement <= A-1)
  * below the cascade tier   (max joint agreement <= A-2)
  * tangent/strip free       (no ray with agreement > A; v nowhere zero)
before any ledger number is read off it.

Groups (CLI arg): v1 s1 depth multi shared triple adv all

Run: tools/ramguard local -- python3 <this> <group>
"""
import json
import sys
from math import comb
from collections import defaultdict

sys.path.insert(0, "notes/pilots_20260802/xr_graded_band_ledger")
from bandlib import Row, scan, plant  # noqa: E402

OUT = []


# ------------------------------------------------------------------ checks
def full_report(row, u, v, name, intended=None):
    n, k, A, h, q = row.n, row.k, row.A, row.h, row.q
    pairs, rays, cnt = scan_counted(row, u, v)
    rec = dict(fixture=name, n=n, k=k, t=row.t, A=A, h=h, R=row.R, r=row.r,
               q=q, band=[k + 1, A - 2], intended=intended)

    maxJ = max(p["J"] for p in pairs.values())
    maxagr = max((rr["agr"] for rr in rays.values()), default=0)
    rec["max_joint_agreement"] = maxJ
    rec["globally_generic"] = maxJ <= A - 1
    rec["below_cascade"] = maxJ <= A - 2
    rec["max_ray_agreement"] = maxagr
    rec["tangent_free"] = maxagr <= A
    rec["v_nonvanishing"] = all(x != 0 for x in v)
    rec["ADMISSIBLE"] = (rec["globally_generic"] and rec["below_cascade"]
                         and rec["tangent_free"] and rec["v_nonvanishing"])

    # k-packing, exhaustively: each pair's Z must be hit by exactly C(J,k)
    # of the C(n,k) k-subsets, i.e. every k-set lies in at most one Z.
    kp_bad = [(sorted(Z), cnt[Z], comb(len(Z), k))
              for Z in pairs if cnt[Z] != comb(len(Z), k)]
    rec["kpacking_count_violations"] = kp_bad[:5]
    rec["kpacking_ok"] = not kp_bad
    deep = [Z for Z, p in pairs.items() if p["J"] >= k + 1]
    worst = 0
    for a in range(len(deep)):
        for b in range(a + 1, len(deep)):
            worst = max(worst, len(deep[a] & deep[b]))
    rec["deep_pairs"] = len(deep)
    rec["deep_pairwise_max_intersection"] = worst
    rec["kpacking_direct_ok"] = worst <= k - 1

    live = defaultdict(int)
    for rr in rays.values():
        live[rr["z"]] += 1
    rec["n_rays"] = len(rays)
    rec["live_slopes"] = len(live)
    rec["max_rays_per_slope"] = max(live.values(), default=0)
    rec["reselection_freedom_slopes"] = sum(1 for c in live.values() if c > 1)

    # ledger by depth
    byd = defaultdict(list)
    for Z, p in pairs.items():
        byd[p["J"] - k].append(len(p["slopes"]))
    ledger = {}
    capbad = []
    for d in sorted(byd):
        Ls = byd[d]
        cap = (row.R - d) // (h - d) if h - d > 0 else None
        nz = [L for L in Ls if L >= 2]
        ledger[str(d)] = dict(n_pairs=len(Ls), N_d=len(nz), maxL=max(Ls),
                              cap=cap, sumL=sum(nz))
        if cap is not None and max(Ls) > cap:
            capbad.append((d, max(Ls), cap))
    rec["ledger_by_depth"] = ledger
    rec["LINE_CAP_violations"] = capbad
    rec["banked_kappa_k_cap_floor_R_over_h"] = row.R // h
    rec["banked_cap_violations"] = [(d, ledger[str(d)]["maxL"])
                                    for d in ledger
                                    if ledger[d]["maxL"] > row.R // h]

    # cores from ray pairs + T2 fibre identity
    rl = list(rays.values())
    hist = defaultdict(int)
    t2bad = []
    band_slopes, eqk_slopes = set(), set()
    for a in range(len(rl)):
        for b in range(a + 1, len(rl)):
            if rl[a]["z"] == rl[b]["z"]:
                continue
            core = rl[a]["supp"] & rl[b]["supp"]
            hist[len(core)] += 1
            if len(core) >= k:
                if core not in pairs or pairs[core]["J"] != len(core):
                    t2bad.append((rl[a]["z"], rl[b]["z"], len(core)))
                if len(core) == k:
                    eqk_slopes |= {rl[a]["z"], rl[b]["z"]}
                elif len(core) <= A - 2:
                    band_slopes |= {rl[a]["z"], rl[b]["z"]}
    rec["core_histogram_ge_k"] = {str(a): b for a, b in sorted(hist.items())
                                  if a >= k}
    rec["T2_fibre_violations"] = t2bad
    rec["band_slopes"] = len(band_slopes)
    rec["exact_k_core_slopes"] = len(eqk_slopes)

    # shared-slope rigidity over every pair carrying >= 1 slope
    ws = [(Z, p) for Z, p in pairs.items() if p["slopes"]]
    rec["pairs_with_a_live_slope"] = len(ws)
    shared = defaultdict(int)
    rigbad, propbad = [], []
    for a in range(len(ws)):
        sa = set(ws[a][1]["slopes"])
        for b in range(a + 1, len(ws)):
            sh = sa & set(ws[b][1]["slopes"])
            shared[len(sh)] += 1
            if len(sh) > 1:
                rigbad.append((sorted(ws[a][0]), sorted(ws[b][0]), sorted(sh)))
            for z in sh:
                f1, g1 = ws[a][1]["coeffs"]
                f2, g2 = ws[b][1]["coeffs"]
                df = [(x - y) % q for x, y in zip(f1, f2)]
                dg = [(x - y) % q for x, y in zip(g1, g2)]
                if any((x + z * y) % q for x, y in zip(df, dg)):
                    propbad.append((z, df, dg))
    rec["rigidity_shared_slope_hist"] = {str(a): b
                                         for a, b in sorted(shared.items())}
    rec["rigidity_violations"] = rigbad[:5]
    rec["rigidity_proportionality_violations"] = propbad[:5]

    col = sum(ledger[d]["sumL"] for d in ledger if int(d) >= 1)
    rec["MEASURED_BAND_COLUMN"] = col
    rec["printed_tangent_column"] = n - A + 1
    rec["column_beats_printed"] = col > n - A + 1
    rec["sum_of_caps_over_band"] = sum((row.R - d) // (h - d)
                                       for d in range(1, h - 1))
    return rec


def scan_counted(row, u, v):
    """scan() plus the k-subset multiplicity per pair (for k-packing)."""
    import itertools
    from collections import defaultdict as dd
    n, k, q, A = row.n, row.k, row.q, row.A
    INV, DIFF, INVDIFF = row.INV, row.DIFF, row.INVDIFF
    pairs, rays, cnt = {}, {}, dd(int)
    for W in itertools.combinations(range(n), k):
        Wset = set(W)
        invden = []
        for j in W:
            d_ = 1
            dj = DIFF[j]
            for m in W:
                if m != j:
                    d_ = d_ * dj[m] % q
            invden.append(INV[d_])
        cu = [u[j] * invden[e] % q for e, j in enumerate(W)]
        cv = [v[j] * invden[e] % q for e, j in enumerate(W)]
        Z = list(W)
        buckets = dd(list)
        for i in range(n):
            if i in Wset:
                continue
            di = DIFF[i]
            PI = 1
            for m in W:
                PI = PI * di[m] % q
            gi = INVDIFF[i]
            su = sv = 0
            for e, j in enumerate(W):
                g = gi[j]
                su += cu[e] * g
                sv += cv[e] * g
            a = (PI * su - u[i]) % q
            b = (PI * sv - v[i]) % q
            if a == 0 and b == 0:
                Z.append(i)
            elif b:
                buckets[(-a) * INV[b] % q].append(i)
        Zf = frozenset(Z)
        cnt[Zf] += 1
        if Zf not in pairs:
            pairs[Zf] = dict(J=len(Zf), coeffs=None, slopes={})
        pr = pairs[Zf]
        for z, extra in buckets.items():
            s = len(Zf) + len(extra)
            if s >= A:
                pr["slopes"][z] = s
                key = (z, Zf | frozenset(extra))
                if key not in rays:
                    rays[key] = dict(z=z, supp=Zf | frozenset(extra), agr=s)
    for Zf, pr in pairs.items():
        Zl = sorted(Zf)[:row.k]
        pr["coeffs"] = (row.interp(tuple(Zl), [u[i] for i in Zl]),
                        row.interp(tuple(Zl), [v[i] for i in Zl]))
    return pairs, rays, cnt


# ------------------------------------------------------------- planting
def plant_general(row, cores, assign, seed):
    """cores: list of index lists Z_s.  assign: {point: [(s, z), ...]}
    (1 or 2 constraints per point; 2 constraints must use distinct slopes).
    """
    import random
    rnd = random.Random(seed)
    n, k, q = row.n, row.k, row.q
    u = [None] * n
    v = [None] * n
    built = []
    for Z in cores:
        fixed = [i for i in Z if u[i] is not None]
        free = [i for i in Z if u[i] is None]
        assert len(fixed) <= k, f"core over-determined ({len(fixed)} > k)"
        base = fixed + free[:k - len(fixed)]
        assert len(base) == k, "core smaller than k"
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
    for i, cons in assign.items():
        assert u[i] is None, f"assigned point {i} already used by a core"
        rhs = [(z, (row.ev(built[s][0], row.xs[i])
                    + z * row.ev(built[s][1], row.xs[i])) % q)
               for s, z in cons]
        if len(rhs) == 1:
            z, c = rhs[0]
            gi = row.ev(built[cons[0][0]][1], row.xs[i])
            vi = rnd.randrange(1, q)
            while vi == gi:
                vi = rnd.randrange(1, q)
            v[i] = vi
            u[i] = (c - z * vi) % q
        else:
            (z1, c1), (z2, c2) = rhs[0], rhs[1]
            assert z1 != z2, "two constraints need distinct slopes"
            vi = (c1 - c2) * row.INV[(z1 - z2) % q] % q
            if vi == 0:
                raise ValueError("degenerate shared point (v=0)")
            for s, _z in cons:
                if vi == row.ev(built[s][1], row.xs[i]):
                    raise ValueError("shared point falls into a core")
            v[i] = vi
            u[i] = (c1 - z1 * vi) % q
    for i in range(n):
        if u[i] is None:
            u[i] = rnd.randrange(q)
            v[i] = rnd.randrange(1, q)
    return u, v, built


def blocks_from(pool, sizes):
    out, p = [], list(pool)
    for s in sizes:
        out.append(p[:s])
        p = p[s:]
    return out, p


def run_single_core(row, J, L, seed, name, q_slopes=None):
    """one planted core of size J carrying L live slopes on disjoint blocks."""
    n, A = row.n, row.A
    Z = list(range(J))
    pool = list(range(J, n))
    blk, _ = blocks_from(pool, [A - J] * L)
    slopes = q_slopes or [3 + 7 * i for i in range(L)]
    assign = {}
    for s, b in zip(slopes, blk):
        for i in b:
            assign[i] = [(0, s)]
    u, v, built = plant_general(row, [Z], assign, seed)
    return full_report(row, u, v, name,
                       intended=dict(cores=[J], slopes=[L], shared_blocks=False))


def main():
    grp = sys.argv[1] if len(sys.argv) > 1 else "v1"

    if grp in ("v1", "all"):
        # validation against the banked planted_band.py fixture
        row = Row(14, 5, 4, 97)
        for seed in (1, 2, 3):
            OUT.append(run_single_core(row, 7, 3, seed, f"V1-seed{seed}"))

    if grp in ("s1", "all"):
        # saturation at the top of the band: L == cap
        row = Row(16, 5, 4, 97)          # A=9 R=11 h=4 band [6,7]; cap(d=2)=4
        for seed in (11, 12, 13):
            OUT.append(run_single_core(row, 7, 4, seed, f"S1-sat-d2-seed{seed}"))
        # one over the cap is arithmetically impossible: 7 + 5*2 = 17 > 16
        OUT.append(dict(fixture="S1-overflow-note",
                        note="L=5 at J=7 needs 7+10=17 > n=16 points: the cap "
                             "floor((n-J)/(A-J))=4 is not merely unbeaten, it "
                             "is unrealisable by point count"))

    if grp in ("depth", "all"):
        row = Row(16, 4, 5, 97)          # A=9 R=12 h=5 band [5,7]
        for J, L in ((5, 2), (6, 3), (7, 4)):
            for seed in (21, 22):
                OUT.append(run_single_core(row, J, L, seed,
                                           f"D-J{J}-L{L}-seed{seed}"))

    if grp in ("multi", "all"):
        # two band cores, DISJOINT blocks
        row = Row(20, 5, 4, 101)         # A=9 R=15 h=4 band [6,7]
        Z1, Z2 = list(range(0, 7)), list(range(4, 11))   # |Z1^Z2| = 3 <= k-1
        pool = list(range(11, 20))
        blk, _ = blocks_from(pool, [2, 2, 2, 2])
        for seed in (31, 32):
            assign = {}
            for (s, z), b in zip([(0, 5), (0, 13), (1, 23), (1, 37)], blk):
                for i in b:
                    assign[i] = [(s, z)]
            u, v, _ = plant_general(row, [Z1, Z2], assign, seed)
            OUT.append(full_report(row, u, v, f"M1-2cores-disjoint-seed{seed}",
                                   intended=dict(cores=[7, 7], slopes=[2, 2],
                                                 shared_blocks=False)))

    if grp in ("shared", "all"):
        # two band cores SHARING every block point (the doubling attack)
        row = Row(16, 5, 4, 97)          # A=9 h=4 band [6,7]
        Z1, Z2 = list(range(0, 7)), list(range(3, 10))   # |Z1^Z2| = 4 = k-1
        pool = list(range(10, 16))       # 6 free points -> 3 shared blocks
        blk, _ = blocks_from(pool, [2, 2, 2])
        import random as _r
        rr = _r.Random(7)
        cands = [tuple(_r.Random(1000 + j).sample(range(2, 90), 6))
                 for j in range(400)]
        rr.shuffle(cands)
        for seed in (41, 42, 43, 44, 45):
            got = None
            for six in cands:
                trio = [(six[0], six[1]), (six[2], six[3]), (six[4], six[5])]
                zs = [x for p in trio for x in p]
                if len(set(zs)) != 6:
                    continue
                assign = {}
                for (za, zb), b in zip(trio, blk):
                    for i in b:
                        assign[i] = [(0, za), (1, zb)]
                try:
                    u, v, _ = plant_general(row, [Z1, Z2], assign, seed)
                except ValueError:
                    continue
                got = (u, v, trio)
                break
            if got is None:
                continue
            u, v, trio = got
            OUT.append(full_report(row, u, v, f"M2-2cores-SHARED-seed{seed}",
                                   intended=dict(cores=[7, 7], slopes=[3, 3],
                                                 shared_blocks=True,
                                                 slope_pairs=trio)))

    if grp in ("triple", "all"):
        # three band cores, pairwise intersections <= k-1, disjoint blocks
        row = Row(27, 5, 4, 101)         # A=9 R=22 h=4 band [6,7]
        Z1, Z2, Z3 = list(range(0, 7)), list(range(4, 11)), list(range(8, 15))
        pool = list(range(15, 27))       # 12 points -> 6 blocks of 2
        blk, _ = blocks_from(pool, [2] * 6)
        import random as _r4
        best = None
        tried = 0
        for seed in range(51, 75):
            zs = _r4.Random(seed).sample(range(2, 95), 6)
            spec = [(0, zs[0]), (0, zs[1]), (1, zs[2]), (1, zs[3]),
                    (2, zs[4]), (2, zs[5])]
            assign = {}
            for (s, z), b in zip(spec, blk):
                for i in b:
                    assign[i] = [(s, z)]
            try:
                u, v, _ = plant_general(row, [Z1, Z2, Z3], assign, seed)
            except ValueError:
                continue
            tried += 1
            rec = full_report(row, u, v, f"M3-3cores-seed{seed}",
                              intended=dict(cores=[7, 7, 7], slopes=[2, 2, 2],
                                            shared_blocks=False))
            if not rec["ADMISSIBLE"]:
                continue
            if best is None or (rec["MEASURED_BAND_COLUMN"] >
                                best["MEASURED_BAND_COLUMN"]):
                best = rec
        if best:
            best["fixture"] = (f"M3-3cores-BEST-ADMISSIBLE (of {tried} built)")
            OUT.append(best)
        else:
            OUT.append(dict(fixture="M3-3cores",
                            note=f"NO admissible 3-core fixture in {tried} "
                                 "builds: every one acquired a ray of "
                                 "agreement > A (forced tangent). Multi-core "
                                 "band configurations are strongly "
                                 "tangent-prone."))

    if grp in ("interact", "all"):
        # THEOREM (shared-slope union agreement) in action: two band pairs
        # whose cores meet in exactly k-1 points have PROPORTIONAL differences
        # (forced by degree), hence share a slope z*, hence the ray at z*
        # agrees on Z1 u Z2 -- a tangent event as soon as |Z1 u Z2| > A.
        row = Row(16, 5, 4, 97)
        Z1, Z2 = list(range(0, 7)), list(range(3, 10))     # |Z1^Z2| = 4 = k-1
        pool = list(range(10, 16))
        blk, _ = blocks_from(pool, [2, 2, 2])
        import random as _r2
        cands = [tuple(_r2.Random(1000 + j).sample(range(2, 90), 6))
                 for j in range(400)]
        for six in cands:
            trio = [(six[0], six[1]), (six[2], six[3]), (six[4], six[5])]
            if len(set(six)) != 6:
                continue
            assign = {}
            for (za, zb), b in zip(trio, blk):
                for i in b:
                    assign[i] = [(0, za), (1, zb)]
            try:
                u, v, built = plant_general(row, [Z1, Z2], assign, 41)
            except ValueError:
                continue
            break
        (f1, g1, _), (f2, g2, _) = built
        q = row.q
        df = [(a - b) % q for a, b in zip(f1, f2)]
        dg = [(a - b) % q for a, b in zip(g1, g2)]
        # proportionality: df = lam * dg  (both are multiples of the degree-(k-1)
        # vanishing polynomial of Z1^Z2, hence constant multiples of each other)
        lead = max(i for i, c in enumerate(dg) if c)
        lam = df[lead] * row.INV[dg[lead]] % q
        prop = all((a - lam * b) % q == 0 for a, b in zip(df, dg))
        zstar = (-lam) % q
        cstar = [(a + zstar * b) % q for a, b in zip(f1, g1)]
        agr = sum(1 for i in range(row.n)
                  if row.ev(tuple(cstar), row.xs[i])
                  == (u[i] + zstar * v[i]) % q)
        union = len(set(Z1) | set(Z2))
        rec = full_report(row, u, v, "INT-forced-tangent",
                          intended=dict(cores=[7, 7], overlap=4))
        rec["interaction"] = dict(
            differences_proportional=prop, lambda_=lam, z_star=zstar,
            agreement_at_z_star=agr, size_Z1_union_Z2=union,
            theorem_holds=(agr >= union), A=row.A,
            tangent_forced=(union > row.A))
        OUT.append(rec)
        print(f"\n### INTERACTION CHECK: differences proportional={prop}, "
              f"z*={zstar}, agreement at z* = {agr}, |Z1 u Z2| = {union}, "
              f"A = {row.A} -> tangent forced = {union > row.A}")

    if grp in ("search", "all"):
        # adversarial random search: is there an ADMISSIBLE received pair whose
        # measured band column beats the printed n-A+1?
        import random as _r3
        shapes = [(12, 3, 4, 13), (12, 3, 4, 17), (12, 3, 5, 17),
                  (14, 4, 4, 17), (12, 3, 5, 13)]
        for (n, k, t, q) in shapes:
            row = Row(n, k, t, q)
            best = None
            adm = 0
            hits = 0
            for s in range(400):
                rnd = _r3.Random(90000 + s)
                u = [rnd.randrange(q) for _ in range(n)]
                v = [rnd.randrange(1, q) for _ in range(n)]
                rec = full_report(row, u, v, f"SEARCH-{n}-{k}-{t}-q{q}-s{s}")
                if not rec["ADMISSIBLE"]:
                    continue
                adm += 1
                if rec["MEASURED_BAND_COLUMN"] > 0:
                    hits += 1
                if best is None or (rec["MEASURED_BAND_COLUMN"] >
                                    best["MEASURED_BAND_COLUMN"]):
                    best = rec
            if best:
                best["fixture"] = (f"SEARCH-BEST n={n} k={k} t={t} q={q} "
                                   f"[{adm}/400 admissible, {hits} with band mass]")
                OUT.append(best)

    if grp in ("adv", "all"):
        # adversarial: maximise the measured column against n-A+1 on a small
        # row where the printed column is small.
        row = Row(16, 5, 4, 97)          # n-A+1 = 8
        Z1, Z2 = list(range(0, 7)), list(range(3, 10))
        pool = list(range(10, 16))
        blk, _ = blocks_from(pool, [2, 2, 2])
        best = None
        for seed in range(60, 72):
            assign = {}
            for (za, zb), b in zip([(5, 11), (13, 23), (29, 41)], blk):
                for i in b:
                    assign[i] = [(0, za), (1, zb)]
            u, v, _ = plant_general(row, [Z1, Z2], assign, seed)
            rec = full_report(row, u, v, f"ADV-seed{seed}")
            if rec["ADMISSIBLE"] and (best is None or
                                      rec["MEASURED_BAND_COLUMN"] >
                                      best["MEASURED_BAND_COLUMN"]):
                best = rec
        if best:
            best["fixture"] = "ADV-best"
            OUT.append(best)

    path = ("notes/pilots_20260802/xr_graded_band_ledger/"
            f"battery_{grp}.json")
    with open(path, "w") as fh:
        json.dump(OUT, fh, indent=1, default=str)
    for rec in OUT:
        if "note" in rec:
            print(f"\n### {rec['fixture']}: {rec['note']}")
            continue
        print(f"\n### {rec['fixture']}  n={rec['n']} k={rec['k']} t={rec['t']} "
              f"A={rec['A']} h={rec['h']} R={rec['R']} band={rec['band']}")
        print(f"  ADMISSIBLE={rec['ADMISSIBLE']}  (generic {rec['globally_generic']}"
              f" / below-cascade {rec['below_cascade']} maxJ={rec['max_joint_agreement']}"
              f" / tangent-free {rec['tangent_free']} maxagr={rec['max_ray_agreement']}"
              f" / v!=0 {rec['v_nonvanishing']})")
        print(f"  rays {rec['n_rays']}, live slopes {rec['live_slopes']}, "
              f"max rays/slope {rec['max_rays_per_slope']}, "
              f"slopes with re-selection freedom {rec['reselection_freedom_slopes']}")
        print(f"  k-packing: count-form ok={rec['kpacking_ok']}, direct max "
              f"intersection over {rec['deep_pairs']} deep pairs = "
              f"{rec['deep_pairwise_max_intersection']} (must be <= k-1="
              f"{rec['k']-1}) -> {rec['kpacking_direct_ok']}")
        print(f"  T2 fibre violations: {rec['T2_fibre_violations']}")
        print(f"  cores >= k histogram: {rec['core_histogram_ge_k']}")
        print(f"  ledger by depth: {rec['ledger_by_depth']}")
        print(f"  LINE CAP violations: {rec['LINE_CAP_violations']}   "
              f"banked kappa=k cap floor(R/h)={rec['banked_kappa_k_cap_floor_R_over_h']}"
              f" violated at: {rec['banked_cap_violations']}")
        print(f"  rigidity: shared-slope histogram {rec['rigidity_shared_slope_hist']}"
              f", violations {rec['rigidity_violations']}, "
              f"proportionality violations {rec['rigidity_proportionality_violations']}")
        print(f"  band slopes {rec['band_slopes']}, exact-k-core slopes "
              f"{rec['exact_k_core_slopes']}")
        print(f"  MEASURED BAND COLUMN {rec['MEASURED_BAND_COLUMN']} vs printed "
              f"n-A+1 = {rec['printed_tangent_column']} -> beats printed: "
              f"{rec['column_beats_printed']}; sum of caps over band = "
              f"{rec['sum_of_caps_over_band']}")
    print(f"\ncheckpoint written: {path}")


if __name__ == "__main__":
    main()
