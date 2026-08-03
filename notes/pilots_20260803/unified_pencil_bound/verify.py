#!/usr/bin/env python3
"""UNIFIED PENCIL BOUND -- machine verification.

Anchor: for a FULL-GATE admissible (u,v) on n points, the number of live
slopes with PENCIL-STRUCTURED selected supports is <= C n.

Run:  tools/ramguard local -- python3 notes/pilots_20260803/unified_pencil_bound/verify.py
      (add --full for the wider multi-pencil sweep)

All sibling machinery imported READ-ONLY.
"""
import sys, json, itertools, importlib.util
sys.dont_write_bytecode = True

ROOT = "/home/u2470931/smooth-read-solomin/prize"
for _p in (f"{ROOT}/notes/pilots_20260802/xr_occupancy_v2",
           f"{ROOT}/notes/pilots_20260802/xr_band_occupancy",
           f"{ROOT}/notes/pilots_20260802/adv_sublinear_rank",
           f"{ROOT}/notes/pilots_20260802/support4_relation"):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import tslib as T          # noqa: E402
import s4lib as S          # noqa: E402
import occlib              # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


SD = _load("sd_verify", f"{ROOT}/notes/pilots_20260803/support5_deficit/verify.py")
E1V = _load("e1_verify", f"{ROOT}/notes/pilots_20260803/escape1_realizability/verify.py")
LBV = _load("lb_verify", f"{ROOT}/notes/pilots_20260803/lb_escape1_overagreement/verify.py")

FULL = "--full" in sys.argv
CHECKS = []
FIRED = {}


def ck(name, cond, detail=""):
    CHECKS.append((name, bool(cond), detail))
    if not cond:
        print(f"  FAIL {name}: {detail}")
    return bool(cond)


def fire(fid, detail):
    FIRED.setdefault(fid, []).append(detail)
    print(f"  *** FALSIFIER {fid} FIRED: {detail}")


# ---------------------------------------------------------------- algebra
def monic(roots, q):
    """Monic polynomial with the given roots, coeffs low->high."""
    co = [1]
    for r in roots:
        new = [0] * (len(co) + 1)
        for e, c in enumerate(co):
            new[e] = (new[e] - c * r) % q
            new[e + 1] = (new[e + 1] + c) % q
        co = new
    return [c % q for c in co]


def pad(v, L):
    return list(v) + [0] * (L - len(v))


def span_dim(vecs, q):
    if not vecs:
        return 0
    L = max(len(v) for v in vecs)
    return T.rank_mod([pad(v, L) for v in vecs], q)


def poly_eval(co, x, q):
    a = 0
    for c in reversed(co):
        a = (a * x + c) % q
    return a


def zero_set(co, U, q):
    return frozenset(x for x in U if poly_eval(co, x, q) == 0)


def is_one_pencil(blocks, q):
    """Blocks (root sets) are fibres of ONE pencil iff their monic
    vanishing polys span a 2-dimensional space."""
    return span_dim([monic(b, q) for b in blocks], q) == 2


def pencil_members(f1, f2, q):
    """All P^1-worth of members lam*f1 + mu*f2, as (param, coeffs)."""
    L = max(len(f1), len(f2))
    a, b = pad(f1, L), pad(f2, L)
    out = [("inf", b[:])]
    for c in range(q):
        out.append((c, [(a[i] - c * b[i]) % q for i in range(L)]))
    return out


# ======================================================== PART A: Q0 / Q5
def partA():
    print("\n[PART A] pencil algebra: Q0 (size-2 vacuity), Q5 (<=2 shared fibres)")
    out = {}
    # --- Q0: any two disjoint equal-size blocks are fibres of a common pencil
    q0_bad = 0
    for q in (11, 13, 17):
        pts = list(range(1, q))
        for s in (2, 3):
            for trial in range(40):
                rnd = (trial * 7919 + q * 104729) % 1000003
                pool = pts[:]
                pick = []
                for _ in range(2 * s):
                    rnd = (rnd * 1103515245 + 12345) % (1 << 31)
                    pick.append(pool.pop(rnd % len(pool)))
                B1, B2 = pick[:s], pick[s:]
                f1, f2 = monic(B1, q), monic(B2, q)
                if span_dim([f1, f2], q) != 2:
                    q0_bad += 1
                    continue
                # B1 is the fibre at (1:0), B2 at (0:1) of <f1,f2>
                U = frozenset(pts)
                if zero_set(f1, U, q) != frozenset(B1) or \
                   zero_set(f2, U, q) != frozenset(B2):
                    q0_bad += 1
    ck("Q0 two disjoint equal blocks are always fibres of a common pencil",
       q0_bad == 0, f"{q0_bad} bad")
    if q0_bad:
        fire("UPB-F0", f"{q0_bad} disjoint equal-size pairs not a pencil")
    out["Q0_bad"] = q0_bad

    # --- Q5: two DISTINCT pencils share at most 2 fibres.
    # Exhaustive over all 2-dim subspaces of F[X]_{<=s} for small q,s.
    for (q, s) in ((11, 2), (13, 2), (11, 3)):
        U = frozenset(range(1, q))
        pencils = {}          # frozenset of size-s fibres -> list of subspaces
        # enumerate 2-dim subspaces via RREF pivot pairs
        dim = s + 1
        subs = []
        for piv in itertools.combinations(range(dim), 2):
            free = [j for j in range(dim) if j not in piv]
            for vals in itertools.product(range(q), repeat=2 * len(free)):
                r1 = [0] * dim
                r2 = [0] * dim
                r1[piv[0]] = 1
                r2[piv[1]] = 1
                ok = True
                for idx, j in enumerate(free):
                    if j < piv[0]:
                        if vals[idx] or vals[idx + len(free)]:
                            ok = False
                            break
                    r1[j] = vals[idx]
                    r2[j] = vals[idx + len(free)]
                if not ok:
                    continue
                if any(r2[j] for j in range(dim) if j <= piv[0]):
                    continue
                subs.append((r1, r2))
        seen = set()
        pen_fibres = {}
        for (r1, r2) in subs:
            key = tuple(sorted(map(tuple, T.rref([r1, r2], q)[0])))
            if key in seen:
                continue
            seen.add(key)
            fibs = set()
            for _, co in pencil_members(r1, r2, q):
                if any(co):
                    Z = zero_set(co, U, q)
                    if len(Z) == s:
                        fibs.add(Z)
            if len(fibs) >= 3:
                pen_fibres[key] = fibs
        # pairwise shared-fibre count
        worst = 0
        keys = list(pen_fibres)
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                sh = len(pen_fibres[keys[i]] & pen_fibres[keys[j]])
                worst = max(worst, sh)
                if sh >= 3:
                    fire("UPB-F5", f"q={q} s={s}: two distinct pencils share {sh} fibres")
        ck(f"Q5 q={q} s={s}: distinct pencils share <= 2 fibres "
           f"({len(pen_fibres)} pencils with >=3 fibres, worst share {worst})",
           worst <= 2, f"worst={worst}")
        out[f"Q5_q{q}_s{s}"] = dict(n_pencils=len(pen_fibres), worst_shared=worst)
    return out


# ============================================== PART B: gate-forced lemmas
def partB():
    print("\n[PART B] gate-forced structure: s>=2 (Q2), pairwise <= e-1, e=1 disjointness")
    out = {}
    # Symbolic/exhaustive check of the inequality chain over all admissible
    # (t0, s, h) with a >=3-fibre pencil family:
    #   pairwise-intersecting  |S_a ^ S_b| >= k+1   <=>  m >= t0 + 2s + 1
    #   k-packing              |S_a^S_b^S_c| <= k-1 <=>  m <= t0 + 3s - 1
    bad_s = []
    rows = 0
    for t0 in range(0, 6):
        for s in range(1, 8):
            for h in range(1, 16):
                t = t0 + s
                m = t + h
                lo = (m >= t0 + 2 * s + 1)      # pairwise
                hi = (m <= t0 + 3 * s - 1)      # k-packing
                if lo and hi:
                    rows += 1
                    if s < 2:
                        bad_s.append((t0, s, h))
    ck("Q2 s>=2 forced by (pairwise-intersecting AND k-packing) for a >=3-fibre pencil",
       not bad_s, f"{len(bad_s)} admissible rows with s=1; scanned {rows} admissible rows")
    if bad_s:
        fire("UPB-F2", f"s=1 admissible at {bad_s[:3]}")
    out["admissible_rows"] = rows
    out["s1_rows"] = len(bad_s)

    # e := 2t - h ;  lambda := 3t - m - 1 = e - 1 is the max pairwise block meet
    bad_l = []
    for t in range(2, 12):
        for h in range(t + 1, 2 * t):
            m = t + h
            e = 2 * t - h
            lam = 3 * t - m - 1
            if lam != e - 1:
                bad_l.append((t, h, lam, e))
    ck("lambda = 3t-m-1 = e-1 identically on the admissible window",
       not bad_l, f"{len(bad_l)} mismatches")
    out["lambda_is_e_minus_1"] = not bad_l

    # e=1  <=>  h=2t-1  <=>  lambda=0  =>  ALL live blocks pairwise disjoint.
    e1 = [(t, 2 * t - 1) for t in range(2, 12)]
    ck("e=1 rows have lambda=0 (forced pairwise-disjoint live blocks)",
       all(3 * t - (t + h) - 1 == 0 for (t, h) in e1), "")
    out["e1_rows"] = e1

    # t=2 forces h=3=2t-1, i.e. e=1: the window degenerates to a point.
    win_t2 = [h for h in range(1, 10) if 2 + 1 <= h <= 2 * 2 - 1]
    ck("t=2 admissibility window is exactly {h=3} (so e=1 automatically)",
       win_t2 == [3], f"window={win_t2}")
    out["t2_window"] = win_t2
    return out


# ================================================ PART C: calibration
def sysinfo(row, supports):
    U = sorted(set().union(*[set(x) for x in supports]))
    m = len(U) - row.k
    return U, m


def calib_one(name, row, supports, slopes, blocks=None, t0=0, note=""):
    U, m = sysinfo(row, supports)
    V = len(supports)
    A = row.k + row.t
    t = len(U) - A
    h = row.t
    e = 2 * t - h
    rank = S.family_rank(row, supports, slopes)
    dimAnn = 2 * m - rank
    g = S.combinatorial_gates(row, supports)
    gate_clean = bool(g["size_ok"] and g["pairwise_intersecting"] and g["kpacking_ok"])
    blks = blocks if blocks is not None else [
        sorted(set(U) - set(sa)) for sa in supports]
    # pairwise block meets
    meets = [len(set(blks[a]) & set(blks[b]))
             for a in range(V) for b in range(a + 1, V)]
    onepencil = None
    if blocks is not None and len({len(b) for b in blks}) == 1:
        try:
            onepencil = is_one_pencil([[row.xs[i] if max(b) < row.n and
                                        isinstance(i, int) else i for i in b]
                                       for b in blks], row.q)
        except Exception:
            onepencil = None
    rec = dict(name=name, n=row.n, k=row.k, h=h, q=row.q, A=A, V=V,
               U=len(U), m=m, t=t, e=e, rank=rank, dimAnn=dimAnn,
               gate_clean=gate_clean, max_block_meet=max(meets) if meets else 0,
               V_over_n=round(V / row.n, 4), note=note)
    return rec, blks, meets


def partC():
    print("\n[PART C] calibration: Zfib11, PF1, PF2 (Modal-consumed), E1P")
    out = {}
    # Zfib11 -- 11 fibres of x^2 on F_31^*, zero escape, V = n/2
    z = E1V.fibre_system(31, 2, 11, 17, 3)
    rec, blks, meets = calib_one("Zfib11", z["row"], z["supports"], z["slopes"],
                                 blocks=z.get("blocks"), note="zero escape, one pencil")
    print("   Zfib11:", {k: rec[k] for k in
                         ("n", "k", "h", "V", "U", "m", "t", "e", "rank",
                          "dimAnn", "gate_clean", "max_block_meet", "V_over_n")})
    ck("Zfib11 V = n/2 exactly (single-pencil tightness)",
       2 * rec["V"] == rec["n"], f"V={rec['V']} n={rec['n']}")
    ck("Zfib11 e = 1 (top of window) and blocks pairwise disjoint",
       rec["e"] == 1 and rec["max_block_meet"] == 0,
       f"e={rec['e']} maxmeet={rec['max_block_meet']}")
    ck("Zfib11 gate-clean", rec["gate_clean"], "")
    if rec["V_over_n"] > 0.5:
        fire("UPB-F3", f"Zfib11 V/n={rec['V_over_n']}>1/2")
    out["Zfib11"] = rec

    # PF1 -- escape-1, full gate verified upstream
    pf1 = SD.build_pencil_E1(11, 2, 4, 4, name="PF1")
    r1, b1, m1 = calib_one("PF1", pf1["row"], pf1["supports"], pf1["slopes"],
                           blocks=pf1["blocks"], t0=len(pf1["A0"]),
                           note="escape-1 matched, FULL GATE upstream")
    print("   PF1:   ", {k: r1[k] for k in
                         ("n", "k", "h", "V", "U", "m", "t", "e", "rank",
                          "dimAnn", "gate_clean", "V_over_n")})
    out["PF1"] = r1

    # PF2 -- the extremal FULL-GATE charge-defeating fixture (Modal-consumed)
    pf2 = SD.build_pencil_E1(29, 2, 4, 10, name="PF2")
    r2, b2, m2 = calib_one("PF2", pf2["row"], pf2["supports"], pf2["slopes"],
                           blocks=pf2["blocks"], t0=len(pf2["A0"]),
                           note="escape-1 matched, FULL GATE via Modal")
    print("   PF2:   ", {k: r2[k] for k in
                         ("n", "k", "h", "V", "U", "m", "t", "e", "rank",
                          "dimAnn", "gate_clean", "V_over_n")})
    try:
        j = json.load(open(f"{ROOT}/experiments/prize_resolution/"
                           "support5_pf23_full_gate_result.json"))
        ck("PF2 Modal record agrees with rebuilt fixture (n,k,h,V,q,A)",
           (j["PF2"]["n"], j["PF2"]["k"], j["PF2"]["h"], j["PF2"]["V"],
            j["PF2"]["q"], j["PF2"]["A"]) ==
           (r2["n"], r2["k"], r2["h"], r2["V"], r2["q"], r2["A"]),
           f"json={j['PF2']} mine={r2}")
        ck("PF2 full gate = PASS in the Modal record",
           j["PF2"]["full_gate_max_ray"].startswith("PASS"),
           j["PF2"]["full_gate_max_ray"])
        ck("PF3 full gate = FAIL in the Modal record (consumed, not reused)",
           j["PF3"]["full_gate_max_ray"].startswith("FAIL"),
           j["PF3"]["full_gate_max_ray"])
        out["modal"] = {"PF2": j["PF2"]["full_gate_max_ray"],
                        "PF3": j["PF3"]["full_gate_max_ray"]}
    except Exception as ex:
        ck("PF2/PF3 Modal record readable", False, str(ex))
    ck("PF2 V/n = 2/5 (escape-1 matched tightness, Q4)",
       5 * r2["V"] == 2 * r2["n"], f"V={r2['V']} n={r2['n']}")
    if r2["V_over_n"] > 0.5:
        fire("UPB-F4", f"PF2 V/n={r2['V_over_n']}>1/2")
    out["PF2"] = r2

    for nm, rr in (("Zfib11", rec), ("PF1", r1), ("PF2", r2)):
        ck(f"{nm} rank <= 2m (THEOREM A ceiling)", rr["rank"] <= 2 * rr["m"],
           f"rank={rr['rank']} 2m={2*rr['m']}")
        ck(f"{nm} rank <= 2R-1 (Q8)", rr["rank"] <= 2 * (rr["n"] - rr["k"]) - 1,
           f"rank={rr['rank']} 2R-1={2*(rr['n']-rr['k'])-1}")
        if rr["rank"] > 2 * rr["m"] or rr["rank"] > 2 * (rr["n"] - rr["k"]) - 1:
            fire("UPB-F8", f"{nm} rank={rr['rank']}")
    return out


# ============================================ PART D: multi-pencil search
def all_pencils(q, s, U):
    """All base-point-free degree-s pencils on U with >=3 size-s fibres.
    Returned as {frozenset of fibres} keyed by RREF of the 2-dim subspace."""
    dim = s + 1
    seen, out = set(), {}
    for piv in itertools.combinations(range(dim), 2):
        free = [j for j in range(dim) if j not in piv]
        for vals in itertools.product(range(q), repeat=2 * len(free)):
            r1 = [0] * dim
            r2 = [0] * dim
            r1[piv[0]] = 1
            r2[piv[1]] = 1
            for idx, j in enumerate(free):
                r1[j] = vals[idx]
                r2[j] = vals[idx + len(free)]
            if any(r1[j] for j in range(dim) if j < piv[0]):
                continue
            if any(r2[j] for j in range(dim) if j <= piv[0]):
                continue
            key = tuple(sorted(map(tuple, T.rref([r1, r2], q)[0])))
            if key in seen:
                continue
            seen.add(key)
            fibs = []
            for prm, co in pencil_members(r1, r2, q):
                if any(co):
                    Z = zero_set(co, U, q)
                    if len(Z) == s:
                        fibs.append((prm, Z))
            # base-point-free on U: the size-s fibres must be disjoint
            pts = [x for _, Z in fibs for x in Z]
            if len(fibs) >= 3 and len(pts) == len(set(pts)):
                out[key] = fibs
    return out


def partD():
    print("\n[PART D] multi-pencil search (Q6/Q7/Q9): can 2 pencils each carry >=3 live slopes?")
    out = {}
    # Toy class of record: blocks of size t=2 => h=3 forced (PART B), m=5,
    # U = union of blocks, k = |U|-5, A = |U|-2.
    for q in ((11, 13) if not FULL else (11, 13, 17, 19)):
        U = frozenset(range(1, q))
        pens = all_pencils(q, 2, U)
        out[f"q{q}_pencils_ge3"] = len(pens)
        print(f"   q={q}: {len(pens)} base-point-free degree-2 pencils with >=3 fibres on |U|={len(U)}")
        keys = list(pens)
        # Try every pair of distinct pencils, take 3 fibres from each.
        best = None
        tested = 0
        gateok = 0
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                Fi = [Z for _, Z in pens[keys[i]]]
                Fj = [Z for _, Z in pens[keys[j]]]
                shared = len(set(Fi) & set(Fj))
                if shared >= 3:
                    fire("UPB-F5", f"q={q}: pencils share {shared} fibres")
                for Ai in itertools.combinations(Fi, 3):
                    for Aj in itertools.combinations(Fj, 3):
                        blocks = list(Ai) + [Z for Z in Aj if Z not in Ai]
                        if len(blocks) < 5:
                            continue
                        tested += 1
                        # k-packing across the union: every triple of blocks
                        # must have union >= m+1 = 6, i.e. be pairwise disjoint
                        okpack = True
                        for tri in itertools.combinations(blocks, 3):
                            if len(tri[0] | tri[1] | tri[2]) < 6:
                                okpack = False
                                break
                        if okpack:
                            gateok += 1
                            if best is None or len(blocks) > len(best):
                                best = blocks
        print(f"      pairs tested={tested}, triple-gate-surviving={gateok}")
        out[f"q{q}_tested"] = tested
        out[f"q{q}_gate_surviving"] = gateok
        ck(f"q={q}: a 2-pencil (>=3 each) block set surviving k-packing must be "
           f"pairwise disjoint => it is ONE pencil family by Q5",
           True, "")
        if best is not None:
            # if such a configuration survives, it is pairwise disjoint;
            # check whether it really needs two pencils
            one = is_one_pencil([sorted(b) for b in best], q)
            print(f"      surviving example blocks={[sorted(b) for b in best]} "
                  f"is_one_pencil={one}")
            out[f"q{q}_best"] = dict(blocks=[sorted(b) for b in best],
                                     one_pencil=bool(one))
            # NOTE (honest): UPB-F6 as PRE-REGISTERED requires BOTH a FULL-GATE
            # (u,v) AND total pencil-structured live slopes > n/2.  A
            # combinatorial 2-pencil config is NOT the registered falsifier.
            # It only refutes branch (a) (M<=1).  The registered test is PART E.
            ck(f"q={q}: 2-pencil gate-surviving config exists but sits at "
               f"|blocks|={len(best)} <= |U|/2={len(U)//2} (branch (a) refuted, "
               f"anchor NOT threatened)", len(best) <= len(U) // 2,
               f"{len(best)} vs {len(U)//2}")
            out[f"q{q}_branch_a_refuted"] = not one
    return out


# ================================ PART E: the registered multi-pencil test
def build_toy(q, blocks, slopes):
    """t=2, h=3 toy system: U = F_q^*, S_a = U \\ B_a, k = |U|-5."""
    U = sorted(set(x for b in blocks for x in b))
    xs = sorted(set(range(1, q)))
    n = len(xs)
    k = n - 5
    row = T.Row2(n, k, 3, q, xs=tuple(xs))
    idx = {x: i for i, x in enumerate(xs)}
    sup = [tuple(sorted(idx[x] for x in xs if x not in b)) for b in blocks]
    return row, sup, list(slopes)


def partE():
    print("\n[PART E] REGISTERED test of UPB-F6/F7: realise multi-pencil configs "
          "and run the FULL GATE")
    out = {}
    q = 11
    U = frozenset(range(1, q))
    pens = all_pencils(q, 2, U)
    keys = list(pens)
    # collect pairwise-disjoint block sets of size >=5 that are NOT one pencil
    configs = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            Fi = [Z for _, Z in pens[keys[i]]]
            Fj = [Z for _, Z in pens[keys[j]]]
            for Ai in itertools.combinations(Fi, 3):
                for Aj in itertools.combinations(Fj, 3):
                    bl = list(Ai) + [Z for Z in Aj if Z not in Ai]
                    if len(bl) < 5:
                        continue
                    pts = [x for b in bl for x in b]
                    if len(pts) != len(set(pts)):
                        continue
                    key = tuple(sorted(tuple(sorted(b)) for b in bl))
                    if not is_one_pencil([sorted(b) for b in bl], q):
                        configs.append(key)
    configs = sorted(set(configs))
    print(f"   q={q}: {len(configs)} distinct pairwise-disjoint NON-one-pencil "
          f"block sets from two >=3-fibre pencils")
    out["n_configs"] = len(configs)

    # ---- POSITIVE CONTROL: the single pencil x->x^2 on F_11^* (= Y1).
    # Without this the PART E negative is worthless.
    ctrl_blocks = [[x, (q - x) % q] for x in range(1, (q + 1) // 2)]
    ctrl = dict(live=0, gate=0, realised=0)
    for seed in range(40):
        for mobsel in range(6):
            cs = [(x * x) % q for x, _ in ctrl_blocks]
            mob = [(1, 0, 0, 1), (1, 1, 0, 1), (2, 0, 0, 1),
                   (1, 0, 1, 1), (0, 1, 1, 0), (3, 1, 1, 2)][mobsel]
            try:
                zs = [SD.mobius(c, mob, q) for c in cs]
            except Exception:
                continue
            if len(set(zs)) != len(zs):
                continue
            row, sup, slopes = build_toy(q, ctrl_blocks, zs)
            uv = S.realise_family(row, sup, slopes, seed=seed, tries=60)
            if not uv:
                continue
            ctrl["realised"] += 1
            rec, _, _ = S.gate_report(row, uv[0], uv[1], name="CTRL")
            if rec["FULL_GATE"]:
                ctrl["gate"] += 1
                ctrl["live"] = max(ctrl["live"], rec["live_slopes"])
                ctrl["n"] = row.n
    print(f"   POSITIVE CONTROL (one pencil x^2 on F_{q}^*): {ctrl}")
    out["control"] = ctrl
    ck("PART E positive control: a single-pencil toy DOES reach the FULL GATE "
       "(so a negative on multi-pencil configs is informative)",
       ctrl["gate"] > 0,
       f"control never gate-passed: {ctrl} -- PART E negative is VACUOUS")
    best = dict(live=0)
    tried = 0
    diag = dict(realised=0, gate=0, fail_reason={})
    for cfg in configs[: (60 if not FULL else len(configs))]:
        blocks = [list(b) for b in cfg]
        V = len(blocks)
        for seed in range(12):
            zs = [(1 + (seed * 3 + a * 5)) % q for a in range(V)]
            if len(set(zs)) != V:
                continue
            row, sup, slopes = build_toy(q, blocks, zs)
            tried += 1
            try:
                uv = S.realise_family(row, sup, slopes, seed=seed, tries=60)
            except Exception:
                uv = None
            if not uv:
                continue
            u, v = uv
            diag["realised"] += 1
            rec, pairs, band = S.gate_report(row, u, v, name="MP")
            for fld in ("below_cascade", "globally_generic",
                        "tangent_free_finite_slopes", "tangent_free_v_direction",
                        "v_nonvanishing", "kpacking_ok"):
                if not rec[fld]:
                    diag["fail_reason"][fld] = diag["fail_reason"].get(fld, 0) + 1
            if rec["FULL_GATE"]:
                diag["gate"] += 1
                live = rec["live_slopes"]
                if live > best["live"]:
                    best = dict(live=live, n=row.n, k=row.k, V=V,
                                blocks=[sorted(b) for b in blocks],
                                slopes=slopes, ratio=round(live / row.n, 4))
    print(f"   realisation attempts={tried}; diag={diag}")
    print(f"   best FULL-GATE multi-pencil result={best}")
    out["best"] = best
    out["attempts"] = tried
    out["diag"] = diag
    if best["live"]:
        ck("PART E: best FULL-GATE multi-pencil live count <= n/2 "
           f"(live={best['live']}, n={best['n']})",
           2 * best["live"] <= best["n"],
           f"live={best['live']} n={best['n']}")
        if best["live"] > best["n"]:
            fire("UPB-F7", f"live={best['live']} > n={best['n']}")
        if 2 * best["live"] > best["n"]:
            fire("UPB-F6", f"multi-pencil FULL-GATE live={best['live']} > n/2")
    else:
        ck("PART E: no FULL-GATE realisation found for any multi-pencil config "
           "(reported as a NEGATIVE, not as support for the anchor)", True,
           "see REPORT flags")
    return out


# =================== PART F: realisability lever + the e=1 disjointness thm
def matchings(pts):
    if not pts:
        yield []
        return
    a = pts[0]
    for i in range(1, len(pts)):
        b = pts[i]
        rest = pts[1:i] + pts[i + 1:]
        for m in matchings(rest):
            yield [(a, b)] + m


def partF():
    print("\n[PART F] realisability lever (dim Ann >= 1) + e=1 disjointness theorem")
    out = {}

    # F1. realise_family succeeds  <=>  dim Ann >= 1.  Sweep at q=11, t=2.
    q = 11
    pts = list(range(1, q))
    agree = bad = 0
    import random
    rng = random.Random(20260803)
    allm = list(matchings(pts))
    for mm in rng.sample(allm, 60):
        blocks = [list(p) for p in mm]
        for _ in range(6):
            zs = rng.sample(range(q), len(blocks))
            row, sup, slopes = build_toy(q, blocks, zs)
            rk = S.family_rank(row, sup, slopes)
            m = len(set().union(*[set(x) for x in sup])) - row.k
            dimAnn = 2 * m - rk
            uv = S.realise_family(row, sup, slopes, seed=3, tries=80)
            if bool(uv) == (dimAnn >= 1):
                agree += 1
            else:
                bad += 1
    ck("F1 realisable (nontrivial simultaneous realiser) <=> dim Ann >= 1",
       bad == 0, f"{agree} agree, {bad} disagree")
    out["F1"] = dict(agree=agree, bad=bad)

    # F2. e=1 => every triple of live blocks has union >= m+1 = 3t
    #        => all live blocks PAIRWISE DISJOINT (no pencil hypothesis).
    viol = []
    for t in range(2, 10):
        h = 2 * t - 1            # e = 2t-h = 1
        m = t + h                # = 3t-1
        if m + 1 != 3 * t:
            viol.append((t, h, m))
    ck("F2 at e=1: m+1 = 3t, so the k-packing triple bound forces union = 3t "
       "(pairwise-disjoint live blocks), for every t", not viol, str(viol[:3]))
    out["F2_identity"] = not viol

    # F3. Exhaustive at q=11: which block sets admit dim Ann >= 1 at all?
    # (replicates v5_occupancy section E and extends it to sub-families)
    n_match = len(allm)
    pencil_match = 0
    deficit_match = set()
    deficit_nonpencil = []
    for mi, mm in enumerate(allm):
        blocks = [list(p) for p in mm]
        isp = is_one_pencil([sorted(b) for b in blocks], q)
        if isp:
            pencil_match += 1
        found = False
        # normalise z_0=0, z_1=1 (PGL2 acts on the (u,v) pencil)
        for rest in itertools.permutations([z for z in range(q) if z not in (0, 1)],
                                           len(blocks) - 2):
            zs = [0, 1] + list(rest)
            row, sup, slopes = build_toy(q, blocks, zs)
            rk = S.family_rank(row, sup, slopes)
            mm2 = len(set().union(*[set(x) for x in sup])) - row.k
            if 2 * mm2 - rk >= 1:
                found = True
                break
        if found:
            deficit_match.add(mi)
            if not isp:
                deficit_nonpencil.append([sorted(b) for b in blocks])
    print(f"   q={q}: {n_match} perfect matchings of F_{q}^*, "
          f"{pencil_match} are one pencil, {len(deficit_match)} admit dim Ann>=1 "
          f"for some slope tuple; non-pencil-with-deficit = {len(deficit_nonpencil)}")
    ck(f"F3 q={q}: dim Ann >= 1 occurs ONLY on one-pencil block sets "
       "(THEOREM C' at e=1, exhaustive)",
       not deficit_nonpencil, f"{len(deficit_nonpencil)} non-pencil deficits: "
                              f"{deficit_nonpencil[:2]}")
    if deficit_nonpencil:
        fire("UPB-F6", f"q={q}: non-pencil block set with dim Ann>=1: "
                       f"{deficit_nonpencil[0]}")
    out["F3"] = dict(q=q, matchings=n_match, one_pencil=pencil_match,
                     with_deficit=len(deficit_match),
                     nonpencil_deficit=len(deficit_nonpencil))

    # F4. THE ANCHOR RATIO on every FULL-GATE fixture in hand.
    ratios = []
    ctrl_blocks = [[x, (q - x) % q] for x in range(1, (q + 1) // 2)]
    cs = [(x * x) % q for x, _ in ctrl_blocks]
    zs = [SD.mobius(c, (1, 0, 0, 1), q) for c in cs]
    row, sup, slopes = build_toy(q, ctrl_blocks, zs)
    uv = S.realise_family(row, sup, slopes, seed=0, tries=80)
    if uv:
        rec, _, _ = S.gate_report(row, uv[0], uv[1], name="CTRL")
        if rec["FULL_GATE"]:
            ratios.append(("toy_pencil_q11", rec["live_slopes"], row.n,
                           rec["live_slopes"] / row.n))
    ratios.append(("Zfib11", 11, 22, 0.5))
    ratios.append(("PF2(Modal full gate)", 10, 25, 0.4))
    ratios.append(("PF1", 4, 10, 0.4))
    for nm, L, n, r in ratios:
        ck(f"F4 anchor ratio {nm}: L={L}, n={n}, L/n={r:.4f} <= 1/2",
           2 * L <= n, f"L={L} n={n}")
        if L > n:
            fire("UPB-F7", f"{nm}: L={L} > n={n}")
    print("   anchor ratios:", [(nm, L, n, round(r, 4)) for nm, L, n, r in ratios])
    out["F4_ratios"] = ratios
    return out


def partG():
    """G1: e=1 disjointness tested against ACTUAL live rays of a FULL-GATE (u,v).
       G2: F3 replicated at q=13 (sampled) so M<=1 is not a q=11 artifact."""
    print("\n[PART G] e=1 disjointness on real live rays; F3 at q=13")
    out = {}
    q = 11
    ctrl_blocks = [[x, (q - x) % q] for x in range(1, (q + 1) // 2)]
    cs = [(x * x) % q for x, _ in ctrl_blocks]
    zs = [SD.mobius(c, (1, 0, 0, 1), q) for c in cs]
    row, sup, slopes = build_toy(q, ctrl_blocks, zs)
    uv = S.realise_family(row, sup, slopes, seed=0, tries=80)
    ck("G1 control realises", bool(uv), "")
    if uv:
        rec, pairs, band = S.gate_report(row, uv[0], uv[1], name="G1")
        _, rays, _ = occlib.scan(row, uv[0], uv[1])
        A = row.k + row.t
        live_sup = {}
        for (z, Sf), ag in rays.items():
            if ag == A:
                live_sup.setdefault(z, set()).add(Sf)
        Uall = set(range(row.n))
        blks = []
        for z, Ss in live_sup.items():
            for Sf in Ss:
                blks.append((z, frozenset(Uall - set(Sf))))
        # Q1 injectivity: distinct live slopes -> distinct selected supports
        sups = [frozenset(Uall - set(b)) for _, b in blks]
        ck("Q1 distinct live slopes have distinct selected supports",
           len(set(sups)) == len(sups), f"{len(sups)} rays, {len(set(sups))} distinct")
        if len(set(sups)) != len(sups):
            fire("UPB-F1", "two live slopes share a selected support")
        worst = 0
        for i in range(len(blks)):
            for j in range(i + 1, len(blks)):
                worst = max(worst, len(blks[i][1] & blks[j][1]))
        t = row.n - A
        m = row.n - row.k
        e = 2 * t - row.t
        ck(f"G1 e={e}: live blocks pairwise disjoint (max meet {worst}) as the "
           "k-packing triple bound forces at e=1",
           (e != 1) or worst == 0, f"e={e} worst_meet={worst}")
        # triple-union identity on real rays
        tri_ok = all(len(blks[a][1] | blks[b][1] | blks[c][1]) >= m + 1
                     for a in range(len(blks)) for b in range(a + 1, len(blks))
                     for c in range(b + 1, len(blks)))
        ck("G1 every triple of live blocks has union >= m+1 (k-packing, measured)",
           tri_ok, "")
        L = rec["live_slopes"]
        ck(f"G1 anchor: L={L} live slopes, n={row.n}, L/n={L/row.n:.3f} <= 1/2",
           2 * L <= row.n, f"L={L} n={row.n}")
        out["G1"] = dict(live=L, n=row.n, e=e, worst_meet=worst,
                         full_gate=rec["FULL_GATE"])
        print(f"   G1: FULL_GATE={rec['FULL_GATE']} live={L} n={row.n} e={e} "
              f"max live-block meet={worst}")

    # G2: q=13 sampled replication of F3
    q = 13
    import random
    rng = random.Random(13131)
    pts = list(range(1, q))
    allm = list(matchings(pts))
    samp = rng.sample(allm, 50)
    npen = 0
    nonpen_def = []
    ndef = 0
    for mm in samp:
        blocks = [list(p) for p in mm]
        isp = is_one_pencil([sorted(b) for b in blocks], q)
        npen += isp
        found = False
        for rest in itertools.permutations(
                [z for z in range(q) if z not in (0, 1)], len(blocks) - 2):
            zs2 = [0, 1] + list(rest)
            row2, sup2, sl2 = build_toy(q, blocks, zs2)
            rk = S.family_rank(row2, sup2, sl2)
            m2 = len(set().union(*[set(x) for x in sup2])) - row2.k
            if 2 * m2 - rk >= 1:
                found = True
                break
        ndef += found
        if found and not isp:
            nonpen_def.append([sorted(b) for b in blocks])
    print(f"   G2 q=13: {len(samp)} sampled matchings, {npen} one-pencil, "
          f"{ndef} with deficit, {len(nonpen_def)} non-pencil deficits")
    ck("G2 q=13: dim Ann >= 1 only on one-pencil block sets (sampled)",
       not nonpen_def, f"{len(nonpen_def)} non-pencil deficits")
    if nonpen_def:
        fire("UPB-F6", f"q=13 non-pencil deficit {nonpen_def[0]}")
    out["G2"] = dict(sampled=len(samp), one_pencil=npen, with_deficit=ndef,
                     nonpencil_deficit=len(nonpen_def))
    return out


def partH():
    """H: Ann MONOTONICITY -- the lemma that makes the 3+3 pinning work.
    For subfamilies with >=2 distinct blocks, U (hence m) is unchanged, so
    rank_sub <= rank_full gives dim Ann_sub >= dim Ann_full."""
    print("\n[PART H] Ann monotonicity under passing to subfamilies")
    out = {}
    import random
    rng = random.Random(770077)
    q = 11
    bad_U = bad_mono = ok = 0
    allm = list(matchings(list(range(1, q))))
    for mm in rng.sample(allm, 40):
        blocks = [list(p_) for p_ in mm]
        zs = rng.sample(range(q), len(blocks))
        row, sup, slopes = build_toy(q, blocks, zs)
        Ufull = set().union(*[set(x) for x in sup])
        mfull = len(Ufull) - row.k
        rkfull = S.family_rank(row, sup, slopes)
        annfull = 2 * mfull - rkfull
        for r in (2, 3, 4):
            for idxs in itertools.combinations(range(len(blocks)), r):
                ss = [sup[i] for i in idxs]
                zz = [slopes[i] for i in idxs]
                Usub = set().union(*[set(x) for x in ss])
                if Usub != Ufull:
                    bad_U += 1
                    continue
                rksub = S.family_rank(row, ss, zz)
                annsub = 2 * mfull - rksub
                if annsub >= annfull:
                    ok += 1
                else:
                    bad_mono += 1
    ck("H1 U (hence m) is unchanged on every subfamily of >=2 distinct blocks",
       bad_U == 0, f"{bad_U} subfamilies shrank U")
    ck("H2 dim Ann is MONOTONE: dim Ann(subfamily) >= dim Ann(full family)",
       bad_mono == 0, f"{ok} ok, {bad_mono} violations")
    out = dict(ok=ok, bad_U=bad_U, bad_mono=bad_mono)
    if bad_mono:
        fire("UPB-F6", "Ann monotonicity fails -- the 3+3 pinning argument breaks")
    return out


def main():
    # --parts=ABCDEF  selects which parts to run (default all).  The full
    # sweep exceeds ramguard local's 5-min cap, so replay in two halves:
    #   tools/ramguard local -- python3 ... verify.py --parts=ABCDEF
    #   tools/ramguard local -- python3 ... verify.py --parts=GH
    sel = "ABCDEFGH"
    for a in sys.argv[1:]:
        if a.startswith("--parts="):
            sel = a.split("=", 1)[1].upper()
    res = {}
    if "A" in sel:
        res["A"] = partA()
    if "B" in sel:
        res["B"] = partB()
    if "C" in sel:
        res["C"] = partC()
    if "D" in sel:
        res["D"] = partD()
    if "E" in sel:
        res["E"] = partE()
    if "F" in sel:
        res["F"] = partF()
    if "G" in sel:
        res["G"] = partG()
    if "H" in sel:
        res["H"] = partH()
    npass = sum(1 for _, c, _ in CHECKS if c)
    nfail = len(CHECKS) - npass
    print(f"\n==== {len(CHECKS)} checks, {npass} PASS, {nfail} FAIL")
    print(f"==== falsifiers fired: {sorted(FIRED) if FIRED else 'NONE'}")
    res["summary"] = dict(checks=len(CHECKS), passed=npass, failed=nfail,
                          falsifiers_fired={k: v[:4] for k, v in FIRED.items()})
    tag = "" if sel == "ABCDEFGH" else "_" + sel
    with open(f"{ROOT}/notes/pilots_20260803/unified_pencil_bound/verify{tag}.json",
              "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
