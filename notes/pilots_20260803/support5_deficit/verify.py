#!/usr/bin/env python3
"""support5_deficit -- the E1-family deficit question.

COMMISSIONED QUESTION
    Does a gate-clean ALL-ESCAPE-1 ray system with dim Ann >= 1 exist?

Banked setting (read-only reuse):
    Row = sum_a G_{z_a}(C_{S_a}),  U = union S_a,  m = |U| - k,
    rank(Row) = 2m - dim Ann = Vh - dim Rel.

Run:
    tools/ramguard tiny  -- python3 notes/pilots_20260803/support5_deficit/verify.py
    tools/ramguard local -- python3 notes/pilots_20260803/support5_deficit/verify.py --full

--full adds PART 5, the exhaustive decisive sweep at the smallest shape.
"""
from __future__ import annotations

import importlib.util
import json
import os
import random
import sys

sys.dont_write_bytecode = True

ROOT = "/home/u2470931/smooth-read-solomin/prize"
for _p in (f"{ROOT}/notes/pilots_20260802/xr_occupancy_v2",
           f"{ROOT}/notes/pilots_20260802/xr_band_occupancy",
           f"{ROOT}/notes/pilots_20260802/adv_sublinear_rank",
           f"{ROOT}/notes/pilots_20260802/support4_relation"):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import tslib as T                                              # noqa: E402
import s4lib as S                                              # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


UNI = _load("uni_verify",
            f"{ROOT}/notes/pilots_20260803/k_escape_unification/verify.py")
E1V = _load("e1_verify",
            f"{ROOT}/notes/pilots_20260803/escape1_realizability/verify.py")
LBV = _load("lb_verify",
            f"{ROOT}/notes/pilots_20260803/lb_escape1_overagreement/verify.py")

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKS = [0]
FAILS = []
HITS = []
LOG = {"checks": [], "fixtures": [], "sweep": {}, "exhaustive": {}}


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    if not ok:
        FAILS.append(f"{label} :: {detail}")
    LOG["checks"].append(dict(label=label, ok=bool(ok), detail=str(detail)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}"
          + (f"   ({detail})" if detail != "" and not ok else ""))
    return bool(ok)


def falsifier(tag, fired, detail=""):
    if fired:
        HITS.append(tag)
        print(f"  [FALSIFIER {tag} FIRED] {detail}")
    LOG["checks"].append(dict(label=f"falsifier {tag}", fired=bool(fired),
                             detail=str(detail)))


def inv(a, q):
    return pow(a % q, q - 2, q)


# ---------------------------------------------------------------- P^1 utils
def norm_p1(a, b, q):
    a, b = a % q, b % q
    if a == 0 and b == 0:
        return None
    if b:
        return (a * inv(b, q) % q, 1)
    return (1, 0)


def cr_proj(P, q):
    """cross-ratio of four P^1 points given as (num, den) pairs."""
    def det(A, B):
        return (A[0] * B[1] - A[1] * B[0]) % q
    num = det(P[0], P[2]) * det(P[1], P[3]) % q
    den = det(P[0], P[3]) * det(P[1], P[2]) % q
    return norm_p1(num, den, q)


# ------------------------------------------------------- dim Ann computations
def ann_dim_dual(row, supports, slopes):
    """dim Ann from THEOREM 1's definition, built from the dual weights.

    {(lam,mu) : sum_{x in S_a} (lam+z_a mu)(x) w^{S_a}_x x^i = 0, i<h}
    modulo (RS_k|_U)^2 (dim 2k).  Assumes U = the whole domain.
    """
    q, n, k, h = row.q, row.n, row.k, row.h
    rows = []
    for a, Sa in enumerate(supports):
        Ss = tuple(sorted(Sa))
        L = T.lam(Ss, row.xs, q)
        z = slopes[a]
        for i in range(h):
            r = [0] * (2 * n)
            for e, j in enumerate(Ss):
                c = L[e] * pow(row.xs[j], i, q) % q
                r[j] = c
                r[n + j] = z * c % q
            rows.append(r)
    ns = T.nullspace_mod(rows, 2 * n, q)
    return len(ns) - 2 * k


def reduced_ann(q, A0, blocks, slopes, h, pair):
    """The structural reduction (this pilot's THEOREM E1-RED).

    Normalising p_{a1} = p_{a2} = 0 leaves the single unknown
    g = mu|_{B_{a1} u B_{a2}} in F^{2s}; ray j (j not in pair) contributes
    exactly h-1 linear conditions.  Returns the nullity.
    """
    E = list(A0) + [x for b in blocks for x in b]
    a1, a2 = pair
    vE = {}
    for x in E:
        p = 1
        for y in E:
            if y != x:
                p = p * (x - y) % q
        vE[x] = inv(p, q)
    unk = list(blocks[a1]) + list(blocks[a2])
    rows = []
    for j in range(len(blocks)):
        if j == a1 or j == a2:
            continue
        bj = blocks[j]
        f1 = (slopes[j] - slopes[a2]) % q
        f2 = (slopes[j] - slopes[a1]) % q
        beta = {}
        for x in unk:
            p = 1
            for y in bj:
                p = p * (x - y) % q
            beta[x] = p
        for i in range(h - 1):
            r = []
            for x in blocks[a1]:
                r.append(f1 * vE[x] % q * beta[x] % q * pow(x, i, q) % q)
            for x in blocks[a2]:
                r.append(f2 * vE[x] % q * beta[x] % q * pow(x, i, q) % q)
            rows.append(r)
    if not rows:
        return len(unk)
    return len(T.nullspace_mod(rows, len(unk), q))


# ------------------------------------------------------------------ builders
def sth_power_fibres(q, s):
    fib = {}
    for x in range(1, q):
        fib.setdefault(pow(x, s, q), []).append(x)
    return {c: v for c, v in sorted(fib.items()) if len(v) == s}


def mobius(c, mob, q):
    a, b, cc, d = mob
    den = (cc * c + d) % q
    assert den, "mobius image at infinity"
    return (a * c + b) % q * inv(den, q) % q


def assemble(q, s, h, V, t0, blocks, private, slopes, name=""):
    """The E1 shape on prescribed blocks.

    U = A_0 u B_1 u ... u B_V u Y,  S_a = A_0 u (u_{b!=a} B_b) u {y_{i(a)}}.
    private=False: |Y| = V/2, perfect matching i(a) = a//2 (escape points of
    multiplicity 2).  private=True: |Y| = V (multiplicity 1).
    """
    used = set(x for b in blocks for x in b)
    rest = [x for x in range(q) if x not in used]
    p = V if private else V // 2
    assert len(rest) >= t0 + p, (len(rest), t0 + p)
    A0 = rest[:t0]
    Y = rest[t0:t0 + p]
    xs = A0 + [x for b in blocks for x in b] + Y
    n = len(xs)
    k = t0 + (V - 1) * s + 1 - h
    row = T.Row2(n, k, h, q, xs=xs)
    idx = {x: i for i, x in enumerate(xs)}
    sup = []
    for a in range(V):
        Sa = set(idx[x] for x in A0)
        for b in range(V):
            if b != a:
                Sa |= set(idx[x] for x in blocks[b])
        Sa.add(idx[Y[a if private else a // 2]])
        sup.append(tuple(sorted(Sa)))
    return dict(name=name, row=row, supports=sup, slopes=list(slopes),
                A0=A0, Y=Y, blocks=blocks, k=k, n=n, m=n - k, t0=t0, s=s,
                h=h, V=V, private=private, q=q)


def build_pencil_E1(q, s, h, V, t0=0, private=False, mob=(1, 0, 0, 1),
                    cs=None, name=""):
    fib = sth_power_fibres(q, s)
    keys = list(fib.keys()) if cs is None else list(cs)
    assert len(keys) >= V, (len(keys), V)
    cs = keys[:V]
    blocks = [fib[c] for c in cs]
    slopes = [mobius(c, mob, q) for c in cs]
    assert len(set(slopes)) == V, "slopes collided"
    out = assemble(q, s, h, V, t0, blocks, private, slopes, name=name)
    out["cs"] = cs
    out["mob"] = mob
    return out


def build_flat_E1(q, s, h, V, t0=0, private=False, seed=0, name="",
                  slopes=None):
    """Same combinatorics, blocks NOT fibres of a pencil (consecutive)."""
    rnd = random.Random(seed)
    blocks = [list(range(a * s, (a + 1) * s)) for a in range(V)]
    if slopes is None:
        pool = [x for x in range(q)]
        rnd.shuffle(pool)
        slopes = pool[:V]
    out = assemble(q, s, h, V, t0, blocks, private, slopes, name=name)
    return out


def unmatched_pair(V, private):
    return (0, 1) if private else (0, 2)


def mult_one_count(supports, n):
    mu = S.multiplicity([set(x) for x in supports], n)
    return sum(1 for i in range(n) if mu[i] == 1)


# --------------------------------------------------------------- measurement
def measure(fx, predict=None, tag=""):
    row, sup, zs = fx["row"], fx["supports"], fx["slopes"]
    q, n, k, h, V = row.q, row.n, row.k, row.h, len(sup)
    g = S.combinatorial_gates(row, sup)
    live, Ts, it, _ = UNI.phi_kernel(row, sup)
    esc = [len(Sa) - (len(Ts[a]) if a in live else 0)
           for a, Sa in enumerate(sup)]
    U = set().union(*[set(x) for x in sup])
    m = len(U) - k
    rank = S.family_rank(row, sup, zs)
    dimRel, _, _ = S.relation_space(row, sup, zs)
    ann_rank = 2 * m - rank
    ann_dual = ann_dim_dual(row, sup, zs)
    npriv = mult_one_count(sup, n)
    red = reduced_ann(q, fx["A0"], fx["blocks"], zs, h,
                      unmatched_pair(V, fx["private"]))
    ann_red = red + npriv
    _, _, _, ann_lb = LBV.ann_dims(row, sup, zs)
    # THEOREM D (3-drop floor) on the live core
    dims = sorted((len(Ts[a]) - k for a in live), reverse=True)
    drop = sum(dims[:3]) if len(live) >= 3 else 0
    capD = max(0, sum(dims) - drop)
    rec = dict(name=fx["name"] or tag, q=q, k=k, h=h, V=V, n=n, s=fx["s"],
               t0=fx["t0"], private=fx["private"], m=m, A=k + h,
               gate_clean=bool(g["size_ok"] and g["pairwise_intersecting"]
                               and g["kpacking_ok"]),
               depth_ok=g["depth_ok"], min_pair=min(g["pair"].values()),
               max_pair=g["max_pair"], max_triple=g["max_triple"],
               core=len(live), escapes=esc, rank=rank, dim_Rel=dimRel,
               dim_Ann_rank=ann_rank, dim_Ann_dual=ann_dual,
               dim_Ann_reduced=ann_red, dim_Ann_record=ann_lb,
               mult1=npriv, twom=2 * m, twoV=2 * V, Vh=V * h,
               thmD_cap=capD, charge=round(rank / V, 4))
    LOG["fixtures"].append(rec)
    print(f"  [{rec['name']}] q={q} k={k} h={h} s={fx['s']} V={V} n={n} "
          f"m={m} | pair>={rec['min_pair']} trip<={rec['max_triple']} "
          f"gate_clean={rec['gate_clean']} core={len(live)} esc={set(esc)} "
          f"| rank={rank} 2m={2*m} 2V={2*V} Vh={V*h} dimAnn={ann_rank} "
          f"dimRel={dimRel} charge={rec['charge']}")
    nm = rec["name"]
    chk(f"{nm}: rank = Vh - dim Rel", rank == V * h - dimRel,
        f"{rank} vs {V*h-dimRel}")
    chk(f"{nm}: rank = 2m - dim Ann (THEOREM 1)", rank == 2 * m - ann_rank)
    chk(f"{nm}: dual-weight dim Ann agrees", ann_dual == ann_rank,
        f"{ann_dual} vs {ann_rank}")
    chk(f"{nm}: record's ann_dims agrees", ann_lb == ann_rank,
        f"{ann_lb} vs {ann_rank}")
    if not chk(f"{nm}: REDUCED system agrees (E1-RED)", ann_red == ann_rank,
               f"reduced {red}+{npriv}={ann_red} vs {ann_rank}"):
        falsifier("SD-F5", True, f"{nm}: reduced {ann_red} != {ann_rank}")
    chk(f"{nm}: dim Rel <= THEOREM D cap", dimRel <= capD,
        f"{dimRel} vs {capD}")
    if dimRel > capD:
        falsifier("SD-F4", True, f"{nm}: dimRel {dimRel} > cap {capD}")
    chk(f"{nm}: dim Ann >= #(multiplicity-1 points)  [PROP 0]",
        ann_rank >= npriv, f"{ann_rank} vs {npriv}")
    if ann_rank < npriv:
        falsifier("SD-F14", True, f"{nm}: {ann_rank} < {npriv}")
    if predict:
        for key, val in predict.items():
            ok = chk(f"{nm}: predicted {key} = {val}", rec[key] == val,
                     f"got {rec[key]}")
            if not ok and key == "dim_Ann_rank":
                falsifier("SD-F3", True, f"{nm}: dimAnn {rec[key]} != {val}")
    return rec


# ==================================================================== PART 0
def part0_replay():
    print("\nPART 0 -- banked replays (read-only reuse)")
    E1 = E1V.build_E1(h=4, s=2, p=6, k=19)
    row, sup, zs = E1["row"], E1["supports"], E1["slopes"]
    rank = S.family_rank(row, sup, zs)
    U = set().union(*[set(x) for x in sup])
    m = len(U) - row.k
    ok = chk("replay E1 (consecutive blocks): rank = 22 = 2m",
             rank == 22 and 2 * m == 22, f"rank={rank} 2m={2*m}")
    if not ok:
        falsifier("SD-F12", True, f"E1 rank {rank}")
    g = S.combinatorial_gates(row, sup)
    chk("replay E1: gate-clean", g["size_ok"] and g["pairwise_intersecting"]
        and g["kpacking_ok"])
    live, Ts, _, _ = UNI.phi_kernel(row, sup)
    esc = [len(Sa) - (len(Ts[a]) if a in live else 0)
           for a, Sa in enumerate(sup)]
    chk("replay E1: all escapes exactly 1, core = all 12",
        set(esc) == {1} and len(live) == 12, f"{esc} {len(live)}")
    chk("replay E1: dim Ann = 0 (the recorded no-deficit value)",
        2 * m - rank == 0)

    row2 = T.Row2(16, 3, 5, 97)
    fam = S.build_mobius_family(row2, d=1, V=4, seed=1)
    r2 = S.family_rank(row2, fam["supports"], fam["slopes"])
    if not chk("replay U-mechanism (3,5,1,4): rank = 19", r2 == 19, r2):
        falsifier("SD-F12", True, f"U-mech rank {r2}")

    # K_V (3,7,1,5) from the node's own verifier semantics: no relation
    row3 = T.Row2(22, 3, 7, 97)
    fam3 = S.build_mobius_family(row3, d=1, V=5, seed=2, mob=(1, 0, 0, 1))
    if fam3 is not None:
        r3 = S.family_rank(row3, fam3["supports"], fam3["slopes"])
        LOG["sweep"]["kv_like_rank"] = r3
        print(f"    (K_V-like (3,7,1,5) rank = {r3}, Vh = 35)")


# ==================================================================== PART 1
def part1_matched():
    print("\nPART 1 -- MATCHED escape points (multiplicity 2): the sharp case")
    out = {}
    PF1 = build_pencil_E1(11, 2, 4, 4, name="PF1")
    out["PF1"] = measure(PF1, dict(dim_Ann_rank=1, rank=13, m=7, k=3, n=10,
                                   dim_Rel=3, gate_clean=True, core=4))
    chk("PF1: all escapes exactly 1", set(out["PF1"]["escapes"]) == {1},
        out["PF1"]["escapes"])
    chk("PF1: band-proper depth", out["PF1"]["depth_ok"])
    if out["PF1"]["dim_Ann_rank"] < 1:
        falsifier("SD-F2", True, "PF1 has no deficit")
    if not (out["PF1"]["gate_clean"] and set(out["PF1"]["escapes"]) == {1}
            and out["PF1"]["core"] == 4):
        falsifier("SD-F1", True, "PF1 gates/escapes")

    PF2 = build_pencil_E1(29, 2, 4, 10, name="PF2")
    out["PF2"] = measure(PF2, dict(dim_Ann_rank=1, rank=19, m=10, k=15,
                                   n=25, gate_clean=True, core=10))
    chk("PF2: CHARGE DEFEATED (rank < 2V) with a genuine deficit",
        out["PF2"]["rank"] < out["PF2"]["twoV"]
        and out["PF2"]["dim_Ann_rank"] >= 1,
        f"rank={out['PF2']['rank']} 2V={out['PF2']['twoV']}")
    if out["PF2"]["rank"] >= out["PF2"]["twoV"]:
        falsifier("SD-F8", True, f"PF2 rank {out['PF2']['rank']}")

    PF3 = build_pencil_E1(31, 2, 4, 12, name="PF3")
    out["PF3"] = measure(PF3, dict(dim_Ann_rank=1, rank=21, m=11, k=19,
                                   n=30, dim_Rel=27, gate_clean=True,
                                   core=12))
    chk("PF3: the recorded E1 pin (k=19,h=4,V=12) now has a DEFICIT",
        out["PF3"]["rank"] == 21 and out["PF3"]["dim_Ann_rank"] == 1)
    chk("PF3: charge < 2", out["PF3"]["rank"] < out["PF3"]["twoV"])

    PF4 = build_pencil_E1(29, 4, 6, 4, name="PF4")
    out["PF4"] = measure(PF4, dict(dim_Ann_rank=3, rank=19, m=11, k=7,
                                   n=18, gate_clean=True, core=4))

    PF5 = build_pencil_E1(17, 2, 4, 4, t0=2, name="PF5")
    out["PF5"] = measure(PF5, dict(dim_Ann_rank=1, rank=13, m=7, k=5,
                                   n=12, gate_clean=True, core=4))

    # THEOREM D tightness
    for nm in ("PF1", "PF2", "PF3", "PF4", "PF5"):
        r = out[nm]
        chk(f"{nm}: THEOREM D is TIGHT (dim Rel = cap)",
            r["dim_Rel"] == r["thmD_cap"], f"{r['dim_Rel']}/{r['thmD_cap']}")
        chk(f"{nm}: dim Ann = 2s - h + 1",
            r["dim_Ann_rank"] == 2 * r["s"] - r["h"] + 1,
            f"{r['dim_Ann_rank']} vs {2*r['s']-r['h']+1}")
    return out


# ==================================================================== PART 2
def part2_private():
    print("\nPART 2 -- PRIVATE escape points (multiplicity 1): PROP 0")
    out = {}
    PF6 = build_pencil_E1(29, 2, 4, 4, private=True, name="PF6")
    out["PF6"] = measure(PF6, dict(dim_Ann_rank=5, rank=13, m=9, k=3, n=12,
                                   gate_clean=True, core=4, mult1=4))
    if out["PF6"]["dim_Ann_rank"] != 5:
        falsifier("SD-F16", True, f"PF6 {out['PF6']['dim_Ann_rank']}")

    PF7 = build_flat_E1(29, 2, 4, 4, private=True, seed=7, name="PF7")
    out["PF7"] = measure(PF7, dict(dim_Ann_rank=4, rank=14, m=9, k=3, n=12,
                                   gate_clean=True, core=4, mult1=4))
    if out["PF7"]["dim_Ann_rank"] > 4:
        falsifier("SD-F15", True, f"PF7 {out['PF7']['dim_Ann_rank']}")

    PF8 = build_flat_E1(37, 2, 4, 12, private=True, seed=8, name="PF8")
    out["PF8"] = measure(PF8, dict(dim_Ann_rank=12, rank=22, m=17, k=19,
                                   n=36, gate_clean=True, core=12, mult1=12))
    chk("PF8: private-escape shape is charge-defeating AND deficient",
        out["PF8"]["rank"] < out["PF8"]["twoV"]
        and out["PF8"]["dim_Ann_rank"] >= 1,
        f"rank={out['PF8']['rank']} 2V={out['PF8']['twoV']}")
    for nm in ("PF6", "PF7", "PF8"):
        r = out[nm]
        chk(f"{nm}: dim Ann >= #mult-1 = {r['mult1']} (PROP 0)",
            r["dim_Ann_rank"] >= r["mult1"])
    return out


# ==================================================================== PART 3
def part3_controls():
    print("\nPART 3 -- controls: what a deficit needs")
    # CTRL-A: pencil supports, NON-Mobius slopes
    fib = sth_power_fibres(11, 2)
    cs = list(fib.keys())[:4]
    blocks = [fib[c] for c in cs]
    hits, total = [], 0
    for z0 in range(11):
        for z1 in range(11):
            for z2 in range(11):
                for z3 in range(11):
                    zs = [z0, z1, z2, z3]
                    if len(set(zs)) != 4:
                        continue
                    total += 1
                    fx = assemble(11, 2, 4, 4, 0, blocks, False, zs)
                    d = reduced_ann(11, fx["A0"], blocks, zs, 4, (0, 2))
                    if d:
                        hits.append((tuple(zs), d))
    crs = set()
    for zs, _ in hits:
        P = [norm_p1(z, 1, 11) for z in zs]
        crs.add(cr_proj(P, 11))
    cpar = [norm_p1(c, 1, 11) for c in cs]
    crc = cr_proj(cpar, 11)
    print(f"    pencil supports, exhaustive {total} slope tuples: "
          f"{len(hits)} deficits, slope cross-ratios {sorted(crs)}, "
          f"pencil cross-ratio {crc}")
    LOG["sweep"]["ctrlA"] = dict(total=total, hits=len(hits),
                                 crs=sorted(str(c) for c in crs),
                                 cr_pencil=str(crc))
    chk("CTRL-A: deficits occur ONLY at the Mobius-matched cross-ratio",
        len(hits) > 0 and crs == {crc}, f"{sorted(crs)} vs {crc}")
    if crs - {crc}:
        falsifier("SD-F6", True, f"non-Mobius deficit {sorted(crs)}")
    chk("CTRL-A: the Mobius locus is a proper slope condition",
        len(hits) < total, f"{len(hits)}/{total}")

    # CTRL-C: NON-pencil supports, every slope tuple
    bad = [[0, 1], [2, 3], [4, 6], [5, 9]]
    span = poly_span_dim([blk for blk in bad], 11)
    hits2, tot2 = 0, 0
    for z0 in range(11):
        for z1 in range(11):
            for z2 in range(11):
                for z3 in range(11):
                    zs = [z0, z1, z2, z3]
                    if len(set(zs)) != 4:
                        continue
                    tot2 += 1
                    fx = assemble(11, 2, 4, 4, 0, bad, False, zs)
                    if reduced_ann(11, fx["A0"], bad, zs, 4, (0, 2)):
                        hits2 += 1
    print(f"    non-pencil supports (block-poly span dim {span}), "
          f"exhaustive {tot2} slope tuples: {hits2} deficits")
    LOG["sweep"]["ctrlC"] = dict(total=tot2, hits=hits2, span=span)
    chk("CTRL-C: non-pencil supports carry NO deficit at any slope tuple",
        span > 2 and hits2 == 0, f"span={span} hits={hits2}")
    if hits2:
        falsifier("SD-F7", True, f"non-pencil deficit {hits2}")

    # SD-F17: the complete-block (no Y) fibre system reproduces THEOREM F
    for (q, s, h, V) in ((11, 2, 4, 4), (29, 4, 6, 4), (31, 2, 5, 6)):
        f2 = sth_power_fibres(q, s)
        ks = list(f2.keys())[:V]
        blk = [f2[c] for c in ks]
        xs = [x for b in blk for x in b]
        kk = (V - 1) * s - h
        rw = T.Row2(len(xs), kk, h, q, xs=xs)
        idx = {x: i for i, x in enumerate(xs)}
        sup = [tuple(sorted(idx[x] for b2, b in enumerate(blk) if b2 != a
                            for x in b)) for a in range(V)]
        zs = list(ks)
        rk = S.family_rank(rw, sup, zs)
        mm = len(xs) - kk
        da = 2 * mm - rk
        pred = max(0, s - max(0, h - s))
        ok = chk(f"THEOREM F replay (q={q},d={s},h={h},V={V}): "
                 f"dim Ann = {pred}", da == pred, f"got {da}")
        if not ok:
            falsifier("SD-F17", True, f"complete-block ({q},{s},{h},{V}): "
                      f"{da} != {pred}")


def poly_span_dim(blocks, q):
    """dim of the span of the monic block polynomials beta_a in F[X]_{<=s}."""
    s = len(blocks[0])
    rows = []
    for b in blocks:
        co = [1]
        for r in b:
            new = [0] * (len(co) + 1)
            for e, c in enumerate(co):
                new[e] = (new[e] - c * r) % q
                new[e + 1] = (new[e + 1] + c) % q
            co = new
        rows.append([c % q for c in co] + [0] * (s + 1 - len(co)))
    return T.rank_mod(rows, q)


# ==================================================================== PART 4
def part4_band(fx):
    print("\nPART 4 -- LEMMA R realisers and the FULL BAND GATE on PF1")
    row, sup, zs = fx["row"], fx["supports"], fx["slopes"]
    q, n, k, h = row.q, row.n, row.k, row.h
    U = set().union(*[set(x) for x in sup])
    m = len(U) - k
    rank = S.family_rank(row, sup, zs)
    _, cols = S.ray_columns(row, sup, zs)
    ns = T.nullspace_mod(cols, 2 * n, q)
    nontriv = len(ns) - 2 * k
    chk("PF1: LEMMA R -- dim{realisers}/(RS_k)^2 = 2m - rank",
        nontriv == 2 * m - rank, f"{nontriv} vs {2*m-rank}")
    if nontriv != 2 * m - rank:
        falsifier("SD-F9", True, f"{nontriv} vs {2*m-rank}")
    got = None
    for seed in range(60):
        r = S.realise_family(row, sup, zs, seed=seed, tries=200)
        if r is not None:
            got = r
            break
    if got is None:
        chk("PF1: a nondegenerate realiser (u,v) exists", False, "none found")
        return None
    u, v = got
    rec, pairs, band = S.gate_report(row, u, v, name="PF1")
    A = k + h
    print(f"    gate_report: FULL_GATE={rec.get('FULL_GATE')} "
          f"max_ray_agreement={rec.get('max_ray_agreement')} "
          f"max_joint={rec.get('max_joint_agreement')} A={A}")
    # are the DESIGNED rays live at agreement exactly A on this realiser?
    found = {}
    for Zf, p, d, sl in band:
        for z, sz in p["slopes"].items():
            key = (z, frozenset(p["supports"][z]))
            if found.get(key, 0) < sz:
                found[key] = sz
    live_designed = []
    for a in range(len(sup)):
        key = (zs[a] % q, frozenset(sup[a]))
        live_designed.append(found.get(key, 0))
    print(f"    designed rays' agreement on the realiser: {live_designed} "
          f"(A = {A}); live slopes seen = {len(set(k2[0] for k2 in found))}")
    LOG["sweep"]["PF1_designed_ray_agreement"] = live_designed
    chk("PF1: every designed escape-1 ray is LIVE at agreement EXACTLY A "
        "(no over-agreement)", all(x == A for x in live_designed),
        f"{live_designed} vs A={A}")
    if any(x != A for x in live_designed):
        falsifier("SD-F11", True, f"designed ray agreements {live_designed}")
    LOG["sweep"]["PF1_gate"] = {kk: rec[kk] for kk in sorted(rec)
                                if isinstance(rec[kk], (int, bool, float))}
    over = rec.get("max_ray_agreement", 0) > A
    chk("PF1: realiser exists and the band oracle ran (n=10, C(n,k)=120)",
        True)
    if over:
        falsifier("SD-F11", True,
                  f"max ray agreement {rec.get('max_ray_agreement')} > A={A}"
                  " -- over-agreement, so the fixture is deficient but not"
                  " band-admissible as it stands")
    return rec


# ==================================================================== PART 5
def part5_exhaustive():
    """DECISIVE exhaustive sweep at the smallest admissible shape.

    q = 11, s = 2, h = 4, V = 4, t0 = 0, k = 3, n = 10.  dim Ann is invariant
    under affine reparametrisation, so B_0 = {0,1} is WLOG; the conditions
    depend on the slopes only through r_j = (z_j - z_2)/(z_j - z_0), and the
    escape points Y do not enter at all (validated below).
    """
    print("\nPART 5 -- EXHAUSTIVE decisive sweep (q=11, s=2, h=4, V=4)")
    q, s, h, V = 11, 2, 4, 4
    INV = [0] * q
    for a in range(1, q):
        INV[a] = pow(a, q - 2, q)

    # --- validation of the fast path against the full rank computation
    rnd = random.Random(11)
    nval = 0
    for _ in range(120):
        pts = rnd.sample(range(q), 10)
        blocks = [pts[0:2], pts[2:4], pts[4:6], pts[6:8]]
        zs = rnd.sample(range(q), 4)
        fx = assemble(q, s, h, V, 0, blocks, False, zs)
        rank = S.family_rank(fx["row"], fx["supports"], zs)
        a1 = 2 * fx["m"] - rank
        a2 = reduced_ann(q, fx["A0"], blocks, zs, h, (0, 2))
        if a1 != a2:
            chk("PART5 validation: reduced == 2m - rank", False,
                f"{a1} vs {a2} blocks={blocks} zs={zs}")
            falsifier("SD-F5", True, "fast path invalid")
            return
        nval += 1
    chk(f"PART5 validation: reduced system == 2m - rank on {nval} random "
        "configurations", True)

    # --- Y-independence (dim Ann does not see the escape points)
    okY = True
    for _ in range(40):
        pts = rnd.sample(range(q), 8)
        blocks = [pts[0:2], pts[2:4], pts[4:6], pts[6:8]]
        rest = [x for x in range(q) if x not in pts]
        zs = rnd.sample(range(q), 4)
        vals = set()
        for i in range(len(rest)):
            for j in range(len(rest)):
                if i == j:
                    continue
                used = set(pts)
                xs = [x for b in blocks for x in b] + [rest[i], rest[j]]
                row = T.Row2(10, 3, h, q, xs=xs)
                idx = {x: t for t, x in enumerate(xs)}
                sup = []
                for a in range(V):
                    Sa = set()
                    for b in range(V):
                        if b != a:
                            Sa |= set(idx[x] for x in blocks[b])
                    Sa.add(idx[[rest[i], rest[j]][a // 2]])
                    sup.append(tuple(sorted(Sa)))
                vals.add(2 * (10 - 3) - S.family_rank(row, sup, zs))
        if len(vals) != 1:
            okY = False
            break
    chk("PART5: dim Ann is independent of the escape points Y", okY)

    # --- the exhaustive sweep
    pool = [x for x in range(q) if x not in (0, 1)]
    B0 = [0, 1]
    rvals = [r for r in range(1, q)]
    hits = []
    ncfg = ncase = 0
    for i1 in range(len(pool)):
        for j1 in range(i1 + 1, len(pool)):
            B1 = [pool[i1], pool[j1]]
            rem1 = [x for x in pool if x not in B1]
            for i2 in range(len(rem1)):
                for j2 in range(i2 + 1, len(rem1)):
                    B2 = [rem1[i2], rem1[j2]]
                    rem2 = [x for x in rem1 if x not in B2]
                    for i3 in range(len(rem2)):
                        for j3 in range(i3 + 1, len(rem2)):
                            B3 = [rem2[i3], rem2[j3]]
                            blocks = [B0, B1, B2, B3]
                            ncfg += 1
                            E = B0 + B1 + B2 + B3
                            vE = {}
                            for x in E:
                                p = 1
                                for y in E:
                                    if y != x:
                                        p = p * (x - y) % q
                                vE[x] = INV[p]
                            unk = B0 + B2
                            pre = {}
                            for j in (1, 3):
                                bj = blocks[j]
                                bt = {}
                                for x in unk:
                                    p = 1
                                    for y in bj:
                                        p = p * (x - y) % q
                                    bt[x] = p * vE[x] % q
                                pre[j] = [[bt[x] * pow(x, i, q) % q
                                           for x in unk] for i in range(h - 1)]
                            for r1 in rvals:
                                for r3 in rvals:
                                    if r1 == r3:
                                        continue
                                    ncase += 1
                                    rows = []
                                    for j, rj in ((1, r1), (3, r3)):
                                        for base in pre[j]:
                                            rows.append(
                                                [rj * base[0] % q,
                                                 rj * base[1] % q,
                                                 base[2], base[3]])
                                    if _rank_le(rows, 4, 3, q, INV):
                                        hits.append((tuple(map(tuple,
                                                               blocks)),
                                                     r1, r3))
    print(f"    configurations {ncfg}, cases {ncase}, deficits {len(hits)}")
    LOG["exhaustive"] = dict(configs=ncfg, cases=ncase, hits=len(hits))
    chk("PART5: the sweep is exhaustive over affine classes "
        "(B_0 = {0,1} WLOG)", ncfg == 7560, ncfg)
    chk("PART5: at least one deficit exists", len(hits) > 0, len(hits))

    bad = []
    for blocks, r1, r3 in hits:
        blk = [list(b) for b in blocks]
        if poly_span_dim(blk, q) != 2:
            bad.append(("non-pencil", blocks, r1, r3))
            continue
        # pencil parameters from the 2-dim span, then cross-ratio match
        params = pencil_params(blk, q)
        crc = cr_proj(params, q)
        crz = cr_proj([(1, 0), norm_p1(r1, 1, q), (0, 1),
                       norm_p1(r3, 1, q)], q)
        if crc != crz:
            bad.append(("non-mobius", blocks, r1, r3, str(crc), str(crz)))
    chk("PART5 CLASSIFICATION: every deficit is (pencil blocks) + "
        "(Mobius-matched slopes)", not bad, bad[:3])
    if bad:
        falsifier("SD-F10", True, f"{len(bad)} unexplained deficits")
    LOG["exhaustive"]["unexplained"] = len(bad)
    return hits


def pencil_params(blocks, q):
    """The pencil parameter of each block, as a P^1 point."""
    s = len(blocks[0])
    vecs = []
    for b in blocks:
        co = [1]
        for r in b:
            new = [0] * (len(co) + 1)
            for e, c in enumerate(co):
                new[e] = (new[e] - c * r) % q
                new[e + 1] = (new[e + 1] + c) % q
            co = new
        vecs.append([c % q for c in co])
    # basis of the (2-dimensional) span
    import itertools
    basis = None
    for a, b in itertools.combinations(range(len(vecs)), 2):
        if T.rank_mod([vecs[a], vecs[b]], q) == 2:
            basis = (vecs[a], vecs[b])
            break
    w, w2 = basis
    out = []
    for v in vecs:
        # solve alpha w + gamma w2 = v
        rows = [[w[i], w2[i], v[i]] for i in range(len(v))]
        sol = T.nullspace_mod([[w[i], w2[i], (-v[i]) % q]
                               for i in range(len(v))], 3, q)
        got = None
        for c in sol:
            if c[2]:
                iv = inv(c[2], q)
                got = (c[0] * iv % q, c[1] * iv % q)
                break
        out.append(norm_p1(got[0], got[1], q))
    return out


def _rank_le(rows, ncol, bound, q, INV):
    rr = [r[:] for r in rows]
    nr = len(rr)
    piv = 0
    for c in range(ncol):
        p = -1
        for r in range(piv, nr):
            if rr[r][c]:
                p = r
                break
        if p < 0:
            continue
        rr[piv], rr[p] = rr[p], rr[piv]
        pr = rr[piv]
        iv = INV[pr[c]]
        pr = [x * iv % q for x in pr]
        rr[piv] = pr
        for r in range(piv + 1, nr):
            f = rr[r][c]
            if f:
                rr[r] = [(rr[r][t] - f * pr[t]) % q for t in range(ncol)]
        piv += 1
        if piv > bound:
            return False
    return piv <= bound


# ==================================================================== PART 6
def part6_certificate():
    print("\nPART 6 -- explicit certificate, sweep completeness, supports")
    q = 11
    fx = build_pencil_E1(q, 2, 4, 4, name="PF1")
    row, sup, zs = fx["row"], fx["supports"], fx["slopes"]
    n, k, h = row.n, row.k, row.h
    _, cols = S.ray_columns(row, sup, zs)
    ns = T.nullspace_mod(cols, 2 * n, q)
    # a certificate is any element outside (RS_k|_U)^2
    cert = None
    for w in ns:
        lam, mu = w[:n], w[n:]
        if not (T.is_codeword(row, lam) and T.is_codeword(row, mu)):
            cert = (lam, mu)
            break
    if cert is None:
        chk("PF1: a NONTRIVIAL annihilator certificate exists", False)
        return
    lam, mu = cert
    ok, degs = True, []
    for a, Sa in enumerate(sup):
        Ss = sorted(Sa)
        vals = [(lam[i] + zs[a] * mu[i]) % q for i in Ss]
        f = row.interp(tuple(Ss[:k]), vals[:k])
        good = all(row.ev(f, row.xs[i]) == vv for i, vv in zip(Ss, vals))
        ok = ok and good
        degs.append(max([e for e, c in enumerate(f) if c], default=-1))
    chk("PF1 CERTIFICATE: lambda + z_a mu interpolates a deg<k polynomial "
        "on every S_a", ok, degs)
    chk("PF1 CERTIFICATE: all certificate polynomials have degree < k",
        all(d < k for d in degs), degs)
    chk("PF1 CERTIFICATE: (lambda,mu) is not in (RS_k|_U)^2", True)
    LOG["sweep"]["PF1_certificate"] = dict(lam=lam, mu=mu, degs=degs,
                                           xs=row.xs, slopes=zs,
                                           supports=[list(x) for x in sup])

    # --- completeness of the (r_1, r_3) parametrisation used by PART 5
    rnd = random.Random(5)
    bad = 0
    for _ in range(200):
        pts = rnd.sample(range(q), 8)
        blocks = [pts[0:2], pts[2:4], pts[4:6], pts[6:8]]
        z = rnd.sample(range(q), 4)
        d1 = reduced_ann(q, [], blocks, z, h, (0, 2))
        r1 = (z[1] - z[2]) % q * inv((z[1] - z[0]) % q, q) % q
        r3 = (z[3] - z[2]) % q * inv((z[3] - z[0]) % q, q) % q
        d2 = reduced_ann(q, [], blocks, [0, r1, 1, r3], h, (0, 2))
        # r-coordinates: z_0 -> inf is not representable, so use the
        # equivalent normalised slopes 1/(1-r)
        z2 = [0, inv((1 - r1) % q, q) if (1 - r1) % q else None, 1,
              inv((1 - r3) % q, q) if (1 - r3) % q else None]
        if None in z2:
            continue
        d3 = reduced_ann(q, [], blocks, z2, h, (0, 2))
        if not (d1 == d3):
            bad += 1
    chk("PART5 completeness: dim Ann depends on the slopes only through "
        "(r_1, r_3); the 90 r-classes exhaust all distinct-slope tuples",
        bad == 0, bad)

    # --- flag-6 premise and the relation supports at V = 4
    quad = len(set(sup[0]) & set(sup[1]) & set(sup[2]) & set(sup[3]))
    dimRel, rels, _ = S.relation_space(row, sup, zs)
    prof = {}
    for r in rels:
        supp = sum(1 for c in r if any(c))
        prof[supp] = prof.get(supp, 0) + 1
    print(f"    PF1: 4-wise intersection = {quad}, k+2 = {k+2}; "
          f"dim Rel = {dimRel}, basis ray-support profile {prof}")
    LOG["sweep"]["PF1_flag6"] = dict(quad=quad, k_plus_2=k + 2,
                                     dim_Rel=dimRel, profile=prof)
    chk("PF1 reproduces the L-B flag-6 premise (4-wise < k+2)",
        quad < k + 2, f"{quad} vs {k+2}")
    chk("PF1 nevertheless HAS a deficit at V = 4 (so the deficit is NOT "
        "confined to ray-support >= 5)", 2 * fx["m"]
        - S.family_rank(row, sup, zs) >= 1)
    # where the flag-6 inference breaks: S4-3/S4-5 hold, but L is NOT
    # contained in C_{intersection of the four supports}
    r0 = None
    for r in rels:
        if sum(1 for c in r if any(c)) == 4:
            r0 = r
            break
    if r0 is not None:
        dimL = T.rank_mod([c for c in r0 if any(c)], q)
        chk("PF1: S4-3 holds -- the four c_a of a support-4 relation lie in "
            "ONE 2-dimensional L", dimL == 2, dimL)
        rnd2 = random.Random(3)
        best = 0
        basis = [c for c in r0 if any(c)][:2]
        for _ in range(200):
            a1, a2 = rnd2.randrange(q), rnd2.randrange(q)
            w = [(a1 * basis[0][i] + a2 * basis[1][i]) % q for i in range(n)]
            if any(w):
                best = max(best, sum(1 for x in w if x))
        chk(f"PF1: S4-5 holds -- generic element of L has support "
            f"{best} >= k+2 = {k+2}", best >= k + 2, best)
        chk("PF1: the flag-6 STEP fails -- L is 2-dimensional yet the "
            "4-wise intersection is 0, so L is NOT inside C_{^S_a}",
            quad < k + 2 and dimL == 2, f"quad={quad} dimL={dimL}")
        LOG["sweep"]["PF1_S45"] = dict(dimL=dimL, generic_support=best,
                                       quad=quad)

    # --- LEMMA R realisers exist for the larger fixtures too
    for nm, f2 in (("PF2", build_pencil_E1(29, 2, 4, 10, name="PF2")),
                   ("PF3", build_pencil_E1(31, 2, 4, 12, name="PF3"))):
        r2, c2 = S.ray_columns(f2["row"], f2["supports"], f2["slopes"])
        ns2 = T.nullspace_mod(c2, 2 * f2["row"].n, f2["q"])
        nt = len(ns2) - 2 * f2["k"]
        rk = S.family_rank(f2["row"], f2["supports"], f2["slopes"])
        chk(f"{nm}: LEMMA R nontrivial realiser dimension = 2m - rank = "
            f"{2*f2['m']-rk}", nt == 2 * f2["m"] - rk, f"{nt}")
        chk(f"{nm}: rank <= 2m - 1, so band admissibility is NOT excluded "
            "by LEMMA R", rk <= 2 * f2["m"] - 1, f"{rk}/{2*f2['m']}")


# ======================================================================= main
def main():
    full = "--full" in sys.argv
    print("=" * 74)
    print("SUPPORT-5 / E1-FAMILY DEFICIT PILOT -- verify.py")
    print("=" * 74)
    part0_replay()
    matched = part1_matched()
    part2_private()
    part3_controls()
    part4_band(build_pencil_E1(11, 2, 4, 4, name="PF1"))
    part6_certificate()
    if full:
        part5_exhaustive()
    else:
        print("\nPART 5 skipped (pass --full under ramguard local)")
    with open(os.path.join(HERE, "verify.json"), "w") as fh:
        json.dump(LOG, fh, indent=1, default=str)
    print("\n" + "=" * 74)
    print(f"CHECKS {CHECKS[0]}  FAILS {len(FAILS)}  "
          f"FALSIFIERS_FIRED {len(set(HITS))}")
    for f in FAILS:
        print("  - FAIL", f)
    for t in sorted(set(HITS)):
        print("  - FALSIFIER", t)
    if not FAILS:
        print("SUPPORT5_DEFICIT_ALL_PASS")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
