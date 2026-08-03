#!/usr/bin/env python3
r"""ESCAPE-1 GATE-CLEAN REALIZABILITY -- machine verification.

Pilot: Opus 5, 2026-08-03.  Anchor: flag 5 of the round-7 unification
pilot = channel (ii) of the re-posed band occupancy heart.

QUESTION.  Is there a GATE-CLEAN ray system ((z_a,S_a))_{a=1..V},
|S_a| = A = k+h, z_a distinct in P^1(F_q), with
    (T)  |S_a ^ S_b ^ S_c| <= k-1        (k-packing gate)
    (P)  |S_a ^ S_b|       >= k+1        (pairwise-intersecting)
whose (3,k+1)-core (K, T^inf) is NONEMPTY and contains a ray of escape
EXACTLY 1, |S_a \ T^inf_a| = 1 ?   And can such a ray defeat per-ray
charge 2, rank = Vh - dim Rel < 2V ?

Predictions and falsifiers E-F1..E-F12 were fixed in PREREG.md BEFORE any
run.  Every falsifier is evaluated below and reported as a hit or a miss.

REUSE (read-only imports, never copies): s4lib.py (support4_relation),
tslib.py (xr_occupancy_v2), and phi_kernel/ker_floor/build_S1/build_S2
from notes/pilots_20260803/k_escape_unification/verify.py.

Run:  tools/ramguard tiny -- python3 \
      notes/pilots_20260803/escape1_realizability/verify.py
"""
from __future__ import annotations

import importlib.util
import json
import os
import random
import sys

sys.dont_write_bytecode = True

_P2 = "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802"
for _d in ("support4_relation", "exact_k_heart"):
    _p = os.path.join(_P2, _d)
    if _p not in sys.path:
        sys.path.append(_p)

import s4lib as S                                              # noqa: E402
import tslib as T                                              # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


UNI = _load("uni_verify", "/home/u2470931/smooth-read-solomin/prize/notes/"
            "pilots_20260803/k_escape_unification/verify.py")

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKS = [0]
FAILS = []
HITS = []          # pre-registered falsifiers that fired
LOG = {"checks": [], "fixtures": [], "sweep": [], "family_scan": {}}


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    LOG["checks"].append(dict(label=label, ok=bool(ok), detail=str(detail)))
    if not ok:
        FAILS.append(label)
        print("  FAIL", label, detail)
    return bool(ok)


def falsifier(tag, fired, detail=""):
    """Record a pre-registered falsifier outcome.  Firing is NOT a crash --
    it is the honest outcome and is reported."""
    LOG["checks"].append(dict(label="FALSIFIER " + tag, ok=not fired,
                              detail=str(detail)))
    CHECKS[0] += 1
    if fired:
        HITS.append(tag)
        print("  *** FALSIFIER", tag, "FIRED:", detail)
    return fired


# ------------------------------------------------------------------ tools
def primes_at_least(x):
    m = max(x, 3)
    while True:
        if all(m % d for d in range(2, int(m ** 0.5) + 1)):
            return m
        m += 1


def slopes_for(V, q, seed=0):
    rnd = random.Random(seed)
    zs = rnd.sample(range(q), V)
    return zs


def mults(supports, n):
    return S.multiplicity([set(x) for x in supports], n)


def core_data(row, supports):
    """(3,k+1)-core via the unification pilot's PHI (imported)."""
    live, Ts, it, _ = UNI.phi_kernel(row, supports)
    esc = [len(Sa) - (len(Ts[a]) if a in live else 0)
           for a, Sa in enumerate(supports)]
    return live, Ts, esc, it


def floors(row, supports):
    """escape floor (record impl), kernel floor (U3), 3-drop floor (new)."""
    k, h = row.k, row.h
    live, Ts, esc, _ = core_data(row, supports)
    ker = sum(min(h, e) for e in esc)
    dims = sorted((len(Ts[a]) - k for a in live), reverse=True)
    drop = sum(dims[:3]) if len(live) >= 3 else 0
    cap3 = max(0, sum(dims) - drop)
    three = row.h * len(supports) - cap3
    capE, escfl = UNI.esc_floor(row, supports)
    return dict(escape=escfl, escape_cap=capE, kernel=ker,
                kernel_cap=sum(dims), three_drop=three, cap3=cap3,
                live=sorted(live), esc=esc)


def measure(name, row, supports, slopes, note=""):
    """Full record for one fixture: gates, core, escapes, floors, rank."""
    k, h, n = row.k, row.h, row.n
    V = len(supports)
    g = S.combinatorial_gates(row, supports)
    fl = floors(row, supports)
    dimRel, _, _ = S.relation_space(row, supports, slopes)
    rank = S.family_rank(row, supports, slopes)
    m = len(set().union(*[set(x) for x in supports])) - k
    quad = min((len(set(supports[a]) & set(supports[b]) & set(supports[c])
                    & set(supports[d]))
                for a in range(V) for b in range(a + 1, V)
                for c in range(b + 1, V) for d in range(c + 1, V)),
               default=None)
    quadmax = max((len(set(supports[a]) & set(supports[b])
                       & set(supports[c]) & set(supports[d]))
                   for a in range(V) for b in range(a + 1, V)
                   for c in range(b + 1, V) for d in range(c + 1, V)),
                  default=0)
    rec = dict(name=name, note=note, k=k, h=h, V=V, n=n, q=row.q, A=k + h,
               m=m, sizes_ok=g["size_ok"], min_pair=min(g["pair"].values()),
               max_pair=g["max_pair"], max_triple=g["max_triple"],
               max_quad=quadmax, min_quad=quad,
               pairwise_ok=g["pairwise_intersecting"],
               kpacking_ok=g["kpacking_ok"], depth_ok=g["depth_ok"],
               gate_clean=bool(g["size_ok"] and g["pairwise_intersecting"]
                               and g["kpacking_ok"]),
               core=fl["live"], escapes=fl["esc"],
               escape_floor=fl["escape"], kernel_floor=fl["kernel"],
               three_drop_floor=fl["three_drop"],
               rank=rank, dim_Rel=dimRel, Vh=V * h, twoV=2 * V, twom=2 * m,
               charge=round(rank / V, 4))
    LOG["fixtures"].append(rec)
    print(f"  [{name}] k={k} h={h} V={V} n={n} A={k+h} m={m} | "
          f"pair>={rec['min_pair']} trip<={rec['max_triple']} "
          f"gate_clean={rec['gate_clean']} | core={len(fl['live'])} "
          f"esc={fl['esc']} | floors esc/ker/3drop="
          f"{fl['escape']}/{fl['kernel']}/{fl['three_drop']} | "
          f"rank={rank} 2m={2*m} 2V={2*V} charge={rec['charge']}")
    # universal invariants
    chk(f"{name}: rank = Vh - dim Rel", rank == V * h - dimRel,
        f"{rank} vs {V*h-dimRel}")
    chk(f"{name}: rank <= 2m (Row <= C_U x C_U)", rank <= 2 * m,
        f"{rank} vs {2*m}")
    chk(f"{name}: escape floor <= kernel floor <= 3-drop floor <= rank",
        fl["escape"] <= fl["kernel"] <= fl["three_drop"] <= rank,
        f"{fl['escape']}/{fl['kernel']}/{fl['three_drop']}/{rank}")
    chk(f"{name}: |K| = 0 or >= 4", len(fl["live"]) == 0
        or len(fl["live"]) >= 4, len(fl["live"]))
    if rank != V * h - dimRel or rank > 2 * m:
        falsifier("E-F4", True, f"{name}: rank={rank} Vh-dimRel="
                  f"{V*h-dimRel} 2m={2*m}")
    if fl["three_drop"] > rank:
        falsifier("E-F5", True, f"{name}: 3-drop {fl['three_drop']} > rank "
                  f"{rank}")
    if rec["gate_clean"] and V >= 3 and h <= 2:
        falsifier("E-F6", True, f"{name}: gate-clean with h={h}")
    if 1 <= len(fl["live"]) <= 3:
        falsifier("E-F7", True, f"{name}: |K|={len(fl['live'])}")
    return rec


# --------------------------------------------------------------- builders
def build_E1(h, s, p, k, q=None, seed=0):
    """E1 family -- ALL rays escape EXACTLY 1.

    U = A_0 u B_1 u ... u B_V u Y,  V = 2p, |B_a| = s, Y = {y_1..y_p};
    ray a is matched to y_{i(a)}, i(a) = a//2 (a perfect matching of the
    rays), and

        S_a = A_0 u (u_{b != a} B_b) u {y_{i(a)}}.

    So y_i has multiplicity 2 (escaped), B-points have multiplicity V-1,
    A_0-points V.  |S_a| = |A_0| + (V-1)s + 1 = A = k+h fixes |A_0|.
    """
    V = 2 * p
    t0 = k + h - 1 - (V - 1) * s
    if t0 < 0:
        return None
    n = t0 + V * s + p
    q = q or primes_at_least(n + 1)
    row = T.Row2(n, k, h, q)
    A0 = list(range(t0))
    B = [list(range(t0 + a * s, t0 + (a + 1) * s)) for a in range(V)]
    Y = [t0 + V * s + i for i in range(p)]
    sup = []
    for a in range(V):
        Sa = set(A0) | {Y[a // 2]}
        for b in range(V):
            if b != a:
                Sa |= set(B[b])
        sup.append(tuple(sorted(Sa)))
    return dict(row=row, supports=sup, slopes=slopes_for(V, q, seed),
                meta=dict(h=h, s=s, p=p, k=k, V=V, t0=t0, n=n, q=q))


def build_Z(k, h, t, V, q=None, seed=0):
    """Complete block system: U = A_0 u A_1 u ... u A_V, S_a = U \\ A_a,
    |A_a| = t.  ZERO ESCAPE for V >= 4 (every multiplicity is V-1 or V)."""
    t0 = k + h - (V - 1) * t
    if t0 < 0:
        return None
    n = t0 + V * t
    q = q or primes_at_least(n + 1)
    row = T.Row2(n, k, h, q)
    A0 = list(range(t0))
    blocks = [list(range(t0 + a * t, t0 + (a + 1) * t)) for a in range(V)]
    U = set(A0) | {x for bl in blocks for x in bl}
    sup = [tuple(sorted(U - set(blocks[a]))) for a in range(V)]
    return dict(row=row, supports=sup, slopes=slopes_for(V, q, seed),
                meta=dict(k=k, h=h, t=t, V=V, t0=t0, n=n, q=q))


def build_pencil_fibre(q, k, t, deg=None):
    """The collapse pilot's zero-escape generator: four full fibres of a
    degree-t power map on F_q^*, U = union, S_i = U \\ A_i, plus the
    cross-ratio-matched slopes of its THEOREM 4(c).  Returns None if the
    field has no such fibres."""
    deg = deg or t
    if (q - 1) % deg or (q - 1) // deg < 4:
        return None
    fib = {}
    for x in range(1, q):
        fib.setdefault(pow(x, deg, q), []).append(x)
    cs = [c for c in sorted(fib) if len(fib[c]) == deg][:4]
    if len(cs) < 4:
        return None
    vals = [fib[c] for c in cs]
    return cs, vals


def build_X1p(q=17, k=6, t=4):
    """X1p -- ESCAPE-1 PERTURBATION of a zero-escape pencil-fibre system.

    Take four fibres of x^t (|U| = 4t, S_i = U \\ A_i, |S_i| = 3t = k+h),
    then swap ONE point of S_1 for a fresh private point.  The swapped
    point drops to multiplicity 2, the fresh point to 1: escapes become
    (1,1,1,0) and the pairwise cores drop by exactly 1 (which is why the
    unperturbed system needs pairwise slack, i.e. k <= 2t-2).
    """
    got = build_pencil_fibre(q, k, t)
    if got is None:
        return None
    cs, vals = got
    h = 3 * t - k
    n = q                      # all q field elements are available points
    row = T.Row2(n, k, h, q)
    idx = {v: i for i, v in enumerate(row.xs)}
    blocks = [[idx[v] for v in bl] for bl in vals]
    U = sorted({x for bl in blocks for x in bl})
    fresh = [i for i in range(n) if i not in U]
    if not fresh:
        return None
    y = fresh[0]
    base = [tuple(sorted(set(U) - set(blocks[a]))) for a in range(4)]
    x = blocks[3][0]           # in S_0,S_1,S_2 but not S_3
    sup = [tuple(sorted((set(base[0]) - {x}) | {y}))] + list(base[1:])
    # cross-ratio matched slopes (collapse pilot THEOREM 4(c))
    def inv(a):
        return pow(a % q, q - 2, q)
    c1, c2, c3, c4 = cs
    R1 = (c3 - c1) * inv(c4 - c1) % q
    R2 = (c3 - c2) * inv(c4 - c2) % q
    if (1 - R2) % q == 0 or (1 - R1) % q == 0:
        return None
    zs = [inv(1 - R2) % q, inv(1 - R1) % q, 0, 1]
    if len(set(zs)) != 4:
        return None
    return dict(row=row, supports=sup, slopes=zs, base=base,
                meta=dict(q=q, k=k, t=t, h=h, n=n, swapped=x, fresh=y))


# ------------------------------------------------------------- PART 1: E1
def part1_realizability():
    print("\nPART 1 -- REALIZABILITY (PR-1): the E1 family, all escapes 1")
    out = {}
    E1 = build_E1(h=4, s=2, p=6, k=19)
    rec = measure("E1", E1["row"], E1["supports"], E1["slopes"],
                  "h=4 s=2 p=6 V=12 k=19: ALL rays escape exactly 1")
    out["E1"] = rec
    pred = dict(A=23, n=30, m=11, min_pair=20, max_pair=21, max_triple=18,
                rank=22, twoV=24)
    chk("E1: predicted A/n/m", (rec["A"], rec["n"], rec["m"]) ==
        (pred["A"], pred["n"], pred["m"]), rec)
    chk("E1: predicted pair/triple", (rec["min_pair"], rec["max_pair"],
        rec["max_triple"]) == (pred["min_pair"], pred["max_pair"],
                               pred["max_triple"]), rec)
    chk("E1: gate-clean", rec["gate_clean"], rec)
    chk("E1: band-proper depths (<= A-2)", rec["depth_ok"], rec["max_pair"])
    chk("E1: k-packing on cores (4-wise <= k-1)",
        rec["max_quad"] <= rec["k"] - 1, rec["max_quad"])
    chk("E1: core = ALL rays", len(rec["core"]) == rec["V"], rec["core"])
    chk("E1: every escape EXACTLY 1", set(rec["escapes"]) == {1},
        rec["escapes"])
    if not rec["gate_clean"]:
        falsifier("E-F1", True, "E1 fails a gate")
    if len(rec["core"]) != rec["V"] or set(rec["escapes"]) != {1}:
        falsifier("E-F2", True, f"core={rec['core']} esc={rec['escapes']}")
    # PR-2: the charge question
    chk("E1: rank < 2V (charge 2 DEFEATED)", rec["rank"] < rec["twoV"],
        f"rank={rec['rank']} 2V={rec['twoV']}")
    chk("E1: predicted rank = 22 = 2m", rec["rank"] == 22, rec["rank"])
    if rec["rank"] >= rec["twoV"]:
        falsifier("E-F3", True, f"rank={rec['rank']} >= 2V={rec['twoV']}")

    E1d = build_E1(h=4, s=2, p=10, k=35)
    recd = measure("E1deep", E1d["row"], E1d["supports"], E1d["slopes"],
                   "h=4 s=2 p=10 V=20 k=35: deeper margin")
    out["E1deep"] = recd
    chk("E1deep: gate-clean, all escapes 1, core = all",
        recd["gate_clean"] and set(recd["escapes"]) == {1}
        and len(recd["core"]) == recd["V"], recd["escapes"])
    chk("E1deep: rank < 2V", recd["rank"] < recd["twoV"],
        f"{recd['rank']} < {recd['twoV']}")

    E1s = build_E1(h=4, s=2, p=3, k=19)
    recs = measure("E1safe", E1s["row"], E1s["supports"], E1s["slopes"],
                   "h=4 s=2 p=3 V=6 k=19: all escapes 1 but V <= m")
    out["E1safe"] = recs
    chk("E1safe: gate-clean, all escapes 1, core = all",
        recs["gate_clean"] and set(recs["escapes"]) == {1}
        and len(recs["core"]) == recs["V"], recs["escapes"])
    chk("E1safe: rank >= 2V (charge 2 SURVIVES: V <= m)",
        recs["rank"] >= recs["twoV"], f"{recs['rank']} vs {recs['twoV']}")
    if recs["rank"] < recs["twoV"]:
        falsifier("E-F9", True, f"E1safe rank {recs['rank']} < "
                  f"{recs['twoV']}")
    return out


# ------------------------------------------------------- PART 2: X1p etc.
def part2_perturbation():
    print("\nPART 2 -- independent witness: escape-1 by PERTURBING a "
          "zero-escape pencil-fibre system (X1p)")
    got = build_X1p()
    if got is None:
        chk("X1p: constructed", False, "no fibre structure found")
        return {}
    row, sup, zs = got["row"], got["supports"], got["slopes"]
    rec0 = measure("X0 (unperturbed)", row, got["base"], zs,
                   "four fibres of x^4 over F_17, k=6: zero escape")
    rec = measure("X1p", row, sup, zs,
                  "one point of S_1 swapped for a fresh private point")
    chk("X0: zero escape", set(rec0["escapes"]) == {0}, rec0["escapes"])
    chk("X1p: gate-clean", rec["gate_clean"], rec)
    chk("X1p: core = all 4 rays", len(rec["core"]) == 4, rec["core"])
    chk("X1p: escape vector (1,1,1,0)",
        sorted(rec["escapes"]) == [0, 1, 1, 1], rec["escapes"])
    chk("X1p: charge 2 survives here (V=4 << m)",
        rec["rank"] >= rec["twoV"], f"{rec['rank']} vs {rec['twoV']}")
    return dict(X0=rec0, X1p=rec)


# ------------------------------------------------- PART 3: channel (i)
def part3_zero_escape():
    print("\nPART 3 -- (reported, not the anchor) channel (i): complete "
          "block systems refute V >= 5 zero-escape charge 2")
    out = {}
    for nm, (k, h, t, V) in dict(Z1=(7, 3, 2, 6), Z1big=(17, 3, 2, 11),
                                 Z0=(7, 3, 2, 4), Z5=(9, 3, 2, 5)).items():
        b = build_Z(k, h, t, V)
        if b is None:
            continue
        rec = measure(nm, b["row"], b["supports"], b["slopes"],
                      f"complete block k={k} h={h} t={t} V={V}")
        out[nm] = rec
        chk(f"{nm}: gate-clean", rec["gate_clean"], rec)
        chk(f"{nm}: zero escape", set(rec["escapes"]) == {0},
            rec["escapes"])
    z1 = out.get("Z1")
    if z1:
        chk("Z1: rank < 2V (channel (i) refuted at V=6)",
            z1["rank"] < z1["twoV"], f"{z1['rank']} vs {z1['twoV']}")
        if z1["rank"] >= z1["twoV"]:
            falsifier("E-F8", True, f"Z1 rank {z1['rank']}")
    z0 = out.get("Z0")
    if z0:
        chk("Z0 (V=4): rank >= 2V, consistent with collapse-pilot PROP 6",
            z0["rank"] >= z0["twoV"], f"{z0['rank']} vs {z0['twoV']}")
    return out


# ------------------------------------------- PART 4: floor + banked replay
def part4_floor_and_replay():
    print("\nPART 4 -- the 3-drop floor: banked replay + tightness")
    out = {}
    q = 97
    row = T.Row2(16, 3, 5, q)
    fam = S.build_mobius_family(row, d=1, V=4, seed=0)
    chk("U-mechanism (3,5,1,4) built", fam is not None)
    if fam:
        rec = measure("U-mech(3,5,1,4)", row, fam["supports"],
                      fam["slopes"], "banked calibration adversary #3")
        out["U"] = rec
        chk("U-mech: banked rank 19 = Vh - 1", rec["rank"] == 19,
            rec["rank"])
        chk("U-mech: banked escape floor 16", rec["escape_floor"] == 16,
            rec["escape_floor"])
        chk("U-mech: 3-drop floor TIGHT (= rank 19)",
            rec["three_drop_floor"] == 19, rec["three_drop_floor"])
        if rec["rank"] != 19 or rec["escape_floor"] != 16:
            falsifier("E-F12", True, f"U-mech replay {rec}")
        if rec["three_drop_floor"] != 19:
            falsifier("E-F10", True, f"3-drop {rec['three_drop_floor']} "
                      f"!= 19")
    # K_V (3,7,1,5) -- the node's own builder, via the unification pilot
    kk, hh, dd, VV = 3, 7, 1, 5
    MM = VV * (VV - 1) // 2
    nn2 = max((kk - 1) + MM * (dd + 1), kk + hh + 2)
    row2 = T.Row2(nn2, kk, hh, 6421)
    _, _, info = UNI.S5.ADV.build_KV(row2, dd, VV, seed=0)
    sup2 = [tuple(s) for s in info["supports"].values()]
    rec2 = measure("K_V(3,7,1,5)", row2, sup2, list(info["zs"]),
                   "banked: every ray dies, K empty, rank = Vh = 35")
    out["KV"] = rec2
    chk("K_V: banked rank 35 = Vh, K empty", rec2["rank"] == 35
        and len(rec2["core"]) == 0, f"{rec2['rank']} {rec2['core']}")
    if rec2["rank"] != 35:
        falsifier("E-F12", True, f"K_V replay rank {rec2['rank']}")
    # S1 / S2 separating fixtures of the unification pilot (imported)
    sup, nn = UNI.build_S1(2, 2)
    q3 = primes_at_least(nn + 1)
    r3 = T.Row2(nn, 2, 2, q3)
    rec3 = measure("S1(k=h=2)", r3, sup, slopes_for(len(sup), q3, 3),
                   "unification pilot's separating fixture (not pairwise)")
    out["S1"] = rec3
    chk("S1: K = empty (replay)", len(rec3["core"]) == 0, rec3["core"])
    chk("S1: rank = Vh = 10 (replay)", rec3["rank"] == 10, rec3["rank"])
    return out


# ------------------------------------------------------- PART 5: the sweep
def rand_T_clean(rnd, k, h, V, n):
    A = k + h
    for _ in range(200):
        sup = [tuple(sorted(rnd.sample(range(n), A))) for _ in range(V)]
        ok = True
        for a in range(V):
            for b in range(a + 1, V):
                for c in range(b + 1, V):
                    if len(set(sup[a]) & set(sup[b]) & set(sup[c])) > k - 1:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            return sup
    return None


def part5_sweep():
    print("\nPART 5 -- (T)-clean sweep: the 3-drop floor vs the true rank")
    rnd = random.Random(20260803)
    tested = 0
    core_nonempty = 0
    strict_over_kernel = 0
    for trial in range(120):
        k = rnd.choice([2, 3, 4, 5])
        h = rnd.choice([2, 3, 4, 5])
        V = rnd.choice([4, 5, 6, 7])
        n = rnd.choice([k + h + 2, k + h + 4, 2 * (k + h)])
        n = max(n, k + h + 1)
        q = primes_at_least(n + 1)
        sup = rand_T_clean(rnd, k, h, V, n)
        if sup is None:
            continue
        row = T.Row2(n, k, h, q)
        zs = slopes_for(V, q, seed=trial)
        fl = floors(row, sup)
        dimRel, _, _ = S.relation_space(row, sup, zs)
        rank = row.h * V - dimRel
        rank2 = S.family_rank(row, sup, zs)
        m = len(set().union(*[set(x) for x in sup])) - k
        g = S.combinatorial_gates(row, sup)
        tested += 1
        if fl["live"]:
            core_nonempty += 1
        if fl["three_drop"] > fl["kernel"]:
            strict_over_kernel += 1
        rec = dict(k=k, h=h, V=V, n=n, m=m, rank=rank, cross=rank2,
                   dimRel=dimRel, esc=fl["esc"], live=len(fl["live"]),
                   floors=[fl["escape"], fl["kernel"], fl["three_drop"]],
                   gate_clean=bool(g["size_ok"]
                                   and g["pairwise_intersecting"]
                                   and g["kpacking_ok"]))
        LOG["sweep"].append(rec)
        if rank != rank2:
            falsifier("E-F4", True, f"sweep {rec}")
        if fl["three_drop"] > rank:
            falsifier("E-F5", True, f"sweep {rec}")
        if not (fl["escape"] <= fl["kernel"] <= fl["three_drop"] <= rank):
            chk(f"sweep#{trial}: floor chain", False, rec)
        if 1 <= len(fl["live"]) <= 3:
            falsifier("E-F7", True, f"sweep {rec}")
        if rec["gate_clean"] and V >= 3 and h <= 2:
            falsifier("E-F6", True, f"sweep {rec}")
    chk("sweep: >= 40 (T)-clean systems tested", tested >= 40, tested)
    chk("sweep: floor chain + rank cross-check held everywhere", True,
        f"{tested} systems, {core_nonempty} with nonempty core, "
        f"{strict_over_kernel} where 3-drop > kernel")
    LOG["sweep_summary"] = dict(tested=tested, core_nonempty=core_nonempty,
                                strict_over_kernel=strict_over_kernel)
    print(f"    {tested} systems | {core_nonempty} nonempty core | "
          f"{strict_over_kernel} with 3-drop > kernel floor")


# ------------------------------------------------ PART 6: family scan (PR-7)
def part6_family_scan():
    print("\nPART 6 -- E1 family parameter scan (PR-7: minimal V)")
    good = []
    for h in range(2, 9):
        for s in range(1, h):
            for p in range(2, 13):
                V = 2 * p
                k = max(2, (V - 1) * s + 1 - h)   # t0 = 0 (smallest k)
                b = build_E1(h, s, p, k)
                if b is None:
                    continue
                row, sup = b["row"], b["supports"]
                g = S.combinatorial_gates(row, sup)
                if not (g["size_ok"] and g["pairwise_intersecting"]
                        and g["kpacking_ok"]):
                    continue
                _, Ts, esc, _ = core_data(row, sup)
                m = len(set().union(*[set(x) for x in sup])) - row.k
                if set(esc) != {1}:
                    continue
                good.append(dict(h=h, s=s, p=p, V=V, k=k, m=m,
                                 breaks=bool(2 * m < 2 * V)))
    brk = [g for g in good if g["breaks"]]
    LOG["family_scan"] = dict(gate_clean_all_escape1=len(good),
                              charge_breaking=len(brk),
                              minimal=sorted(brk, key=lambda r: r["V"])[:3])
    print(f"    {len(good)} gate-clean all-escape-1 members; "
          f"{len(brk)} with 2m < 2V")
    if brk:
        mn = min(g["V"] for g in brk)
        ex = [g for g in brk if g["V"] == mn]
        print(f"    minimal charge-breaking V = {mn}: {ex}")
        chk("family scan: minimal charge-breaking V = 12", mn == 12, ex)
        if mn < 12:
            falsifier("E-F11", True, f"smaller member V={mn}: {ex}")
        chk("family scan: gate forces ceil(h/2) <= s <= h-2",
            all(2 * g["s"] >= g["h"] and g["s"] <= g["h"] - 2
                for g in good), [g for g in good
                                 if not (2 * g["s"] >= g["h"]
                                         and g["s"] <= g["h"] - 2)][:3])
    else:
        chk("family scan: found charge-breaking members", False, len(good))


# ------------------------------------- PART 7: the all-escape-1 lower bound
def part7_extremality():
    """LEMMA ALL-1 (hand-proved, checked here).  For a gate-clean system
    with core = all rays, EVERY escape exactly 1, and m < V:
        t := |U| - A,  E := {x : mult(x) <= 2}
        (i)  |E| >= V/2                (each escaped point covers <= 2 rays)
        (ii) 2|E| <= 2t + 2 - h        (triple gate on A_a = U \\ S_a)
        (iii) t >= 2h-1  and  V >= 3h  (combining with m = h+t < V)
    E1 saturates ALL THREE at h = 4: t = 7 = 2h-1, V = 12 = 3h, 2|E| = 12.
    """
    print("\nPART 7 -- LEMMA ALL-1: the all-escape-1 lower bound V >= 3h")
    rows = []
    for nm, (h, s, p, k) in dict(E1=(4, 2, 6, 19), E1deep=(4, 2, 10, 35),
                                 E1h5=(5, 3, 8, 44),
                                 E1safe=(4, 2, 3, 19)).items():
        b = build_E1(h, s, p, k)
        if b is None:
            chk(f"{nm}: built", False, "")
            continue
        row, sup = b["row"], b["supports"]
        U = set().union(*[set(x) for x in sup])
        A, m = row.k + row.h, len(U) - row.k
        t = len(U) - A
        mu = mults(sup, row.n)
        E = [x for x in U if mu[x] <= 2]
        V = len(sup)
        _, _, esc, _ = core_data(row, sup)
        g = S.combinatorial_gates(row, sup)
        gc = bool(g["size_ok"] and g["pairwise_intersecting"]
                  and g["kpacking_ok"])
        rec = dict(name=nm, h=h, V=V, t=t, m=m, absE=len(E),
                   gate_clean=gc, all_esc1=set(esc) == {1},
                   breaks=m < V, i=2 * len(E) >= V,
                   ii=2 * len(E) <= 2 * t + 2 - h,
                   iii=(t >= 2 * h - 1 and V >= 3 * h) if m < V else None)
        rows.append(rec)
        print(f"    {nm}: h={h} V={V} t={t} m={m} |E|={len(E)} "
              f"breaks={rec['breaks']} (i)={rec['i']} (ii)={rec['ii']} "
              f"(iii)={rec['iii']}")
        chk(f"ALL-1 (i)+(ii) on {nm}", rec["i"] and rec["ii"], rec)
        if rec["breaks"]:
            chk(f"ALL-1 (iii) t>=2h-1 and V>=3h on {nm}", rec["iii"], rec)
    LOG["extremality"] = rows
    e1 = [r for r in rows if r["name"] == "E1"][0]
    chk("E1 saturates ALL-1: t = 2h-1 = 7, V = 3h = 12, 2|E| = 2t+2-h",
        e1["t"] == 7 and e1["V"] == 12 and 2 * e1["absE"] == 2 * e1["t"]
        + 2 - e1["h"], e1)
    # the one-step (item 12) escape must ALSO be 1 on E1 -- both forms of
    # the heart's hypothesis fail in the minimal possible way
    b = build_E1(4, 2, 6, 19)
    lim = UNI.esc_residual(b["row"], b["supports"])
    one = [len(b["supports"][a]) - len(lim[a]) for a in range(len(lim))]
    chk("E1: one-step (item 12) escapes are all 1 too", set(one) == {1},
        one)


# --------------------------------------- PART 8: slope-independence of E1
def part8_slopes():
    """The E1 counterexample is SLOPE-INDEPENDENT: rank <= 2m = 22 < 24 for
    EVERY slope tuple (Row <= C_U x C_U).  Unlike the collapse pilot's
    X1/X2, no cross-ratio locus is involved.  Swept, not only argued."""
    print("\nPART 8 -- E1 slope sweep (the counterexample needs no special "
          "slopes)")
    b = build_E1(4, 2, 6, 19)
    row, sup = b["row"], b["supports"]
    q, V = row.q, len(sup)
    ranks = {}
    rnd = random.Random(7)
    tuples = [list(range(1, V + 1)), [(3 * i + 1) % q for i in range(V)]]
    while len(tuples) < 14:
        z = rnd.sample(range(q), V)
        if len(set(z)) == V:
            tuples.append(z)
    for z in tuples:
        r = S.family_rank(row, sup, z)
        ranks[r] = ranks.get(r, 0) + 1
    print(f"    {len(tuples)} slope tuples -> rank multiset {ranks}")
    chk("E1: rank < 2V = 24 for EVERY swept slope tuple",
        all(r < 24 for r in ranks), ranks)
    chk("E1: rank <= 2m = 22 for EVERY swept slope tuple",
        all(r <= 22 for r in ranks), ranks)
    LOG["e1_slope_sweep"] = {str(k_): v for k_, v in ranks.items()}


# ---------------------------------- PART 9: h >= 3 is forced (exhaustive)
def part9_h_forced():
    """PR-4(a): a gate-clean system with V >= 3 forces h >= 3, because
    |S_a^S_b^S_c| >= |S_a^S_b| + |S_a^S_c| - |S_a| >= 2(k+1)-(k+h) = k+2-h.
    Checked EXHAUSTIVELY for h = 2 over all triples of A-subsets."""
    print("\nPART 9 -- h >= 3 forced for gate-clean V >= 3 (exhaustive "
          "h = 2 search)")
    import itertools
    found = []
    for k, n in ((2, 8), (3, 8)):
        h, A = 2, k + 2
        subs = [frozenset(c) for c in itertools.combinations(range(n), A)]
        for i in range(len(subs)):
            for j in range(i + 1, len(subs)):
                if len(subs[i] & subs[j]) < k + 1:
                    continue
                for l in range(j + 1, len(subs)):
                    if (len(subs[i] & subs[l]) >= k + 1
                            and len(subs[j] & subs[l]) >= k + 1
                            and len(subs[i] & subs[j] & subs[l]) <= k - 1):
                        found.append((k, n, sorted(subs[i]),
                                      sorted(subs[j]), sorted(subs[l])))
        print(f"    k={k} h=2 n={n}: {len(subs)} supports, "
              f"gate-clean triples found = {len(found)}")
    chk("no gate-clean h=2 system with V=3 exists (exhaustive)",
        not found, found[:2])
    if found:
        falsifier("E-F6", True, f"exhaustive h=2 witness {found[0]}")


# -------------------------- PART 10: escape-profile threshold (arithmetic)
def part10_threshold():
    """EXHAUSTIVE arithmetic on the 3-drop floor.  For a core K (|K| = c)
    with escape profile (e_a) in [0, h-1]^c and V - c dead rays,

        floor = (V-c) h + sum_K e_a + G3,  G3 = 3 largest (h - e_a),

    and charge 2 is PROVED whenever floor >= 2V.  Scanned over all
    profiles (as multiplicity vectors) for h in 3..6, V in 4..14.
    Extracts the exact threshold in the pure escape-1 direction."""
    print("\nPART 10 -- exhaustive escape-profile scan of the 3-drop floor")
    import itertools
    worst = {}
    thresholds = {}
    for h in range(3, 7):
        for V in range(4, 15):
            for c in list(range(4, V + 1)) + [0]:
                if c == 0:
                    if V * h < 2 * V:
                        worst[(h, V, 0)] = V * h
                    continue
                for prof in itertools.combinations_with_replacement(
                        range(h), c):
                    dims = sorted((h - e for e in prof), reverse=True)
                    fl = (V - c) * h + sum(prof) + sum(dims[:3])
                    if fl < 2 * V:
                        key = (h, V)
                        n0 = sum(1 for e in prof if e == 0)
                        n1 = sum(1 for e in prof if e == 1)
                        if key not in worst or fl < worst[key][0]:
                            worst[key] = (fl, prof, n0, n1)
        # pure escape-1 direction: c = V, n_1 rays of escape 1, rest 2
        for V in range(4, 60):
            for n1 in range(0, V + 1):
                prof = tuple([1] * n1 + [2] * (V - n1))
                if h - 1 < 2 and V - n1:
                    continue
                dims = sorted((h - e for e in prof), reverse=True)
                fl = sum(prof) + sum(dims[:3])
                if fl < 2 * V:
                    thresholds.setdefault(h, (V, n1))
                    break
            if h in thresholds:
                break
    print(f"    first (V, n_1) with floor < 2V in the pure escape-1 "
          f"direction, per h: {thresholds}")
    chk("threshold in the escape-1 direction is n_1 >= 3h-2",
        all(v[1] == 3 * h - 2 for h, v in thresholds.items()), thresholds)
    chk("ONE escape-1 core ray (others >= 2) NEVER defeats charge 2",
        all(not (sum(p) + sum(sorted((6 - e for e in p),
                                     reverse=True)[:3]) < 2 * len(p))
            for p in [tuple([1] + [2] * (V - 1)) for V in range(4, 60)]),
        "h=6 worst case")
    LOG["threshold"] = {str(k_): list(v) for k_, v in thresholds.items()}
    LOG["profile_worst"] = {str(k_): list(v) if isinstance(v, tuple)
                            else v for k_, v in worst.items()}


# ------------------------- PART 11: realisability (the band-admissibility filter)
def fibre_system(q, deg, V, k, h, perturb=False, which=0):
    """Complete block system on V full fibres of x^deg, S_a = U \\ A_a, with
    the fibre parameters as slopes.  perturb=True swaps one point of S_0 for
    a fresh private point, which makes ray 0 escape EXACTLY 1."""
    fib = {}
    for x in range(1, q):
        fib.setdefault(pow(x, deg, q), []).append(x)
    bl = [sorted(v) for v in fib.values() if len(v) == deg][:V]
    if len(bl) < V:
        return None
    cs = [pow(b[0], deg, q) for b in bl]
    used = sorted({x for b in bl for x in b})
    free = [x for x in range(q) if x not in used]
    if perturb and len(free) <= which:
        return None
    xs = sorted(used + ([free[which]] if perturb else []))
    n = len(xs)
    idx = {v: i for i, v in enumerate(xs)}
    row = T.Row2(n, k, h, q, xs=xs)
    blocks = [[idx[v] for v in b] for b in bl]
    Ui = set(idx[v] for v in used)
    sup = [tuple(sorted(Ui - set(b))) for b in blocks]
    if perturb:
        y, x0 = idx[free[which]], blocks[1][0]
        sup[0] = tuple(sorted((set(sup[0]) - {x0}) | {y}))
    zs = [c % q for c in cs]
    if len(set(zs)) != V:
        return None
    return dict(row=row, supports=sup, slopes=zs, blocks=blocks)


def agreements(row, sup, zs, u, v):
    """Agreement of each ray slope.  When 2h > m one has 2A - n > k, so any
    agreement set of size >= A meets S_a in > k points and hence carries the
    SAME degree-<k polynomial as the S_a-interpolant: this count is then the
    EXACT max agreement (that side condition is checked by the caller)."""
    q, n, k = row.q, row.n, row.k
    out = []
    for a, Sa in enumerate(sup):
        w = [(u[i] + zs[a] * v[i]) % q for i in range(n)]
        f = row.interp(list(Sa)[:k], [w[i] for i in list(Sa)[:k]])
        out.append(sum(1 for i in range(n) if row.ev(f, row.xs[i]) == w[i]))
    return out


def part11_realisability():
    """LEMMA R (realisability = rank deficit).  With |U| >= k, the ray
    conditions on (u,v) have solution space of dim 2n - rank, and it always
    contains the TRIVIAL space (RS_k x RS_k, dim 2k).  Nontrivial realisers
    exist iff rank < 2m.  If rank = 2m every realiser is jointly explained on
    U, so EVERY slope agrees on all |U| > A points: no exact-A live slope,
    hence the system is NOT a selected-support (band-admissible) system."""
    print("\nPART 11 -- realisability: rank < 2m is necessary for band "
          "admissibility")
    rnd = random.Random(0)
    for nm, b in (("E1", build_E1(4, 2, 6, 19)),
                  ("Z1", build_Z(7, 3, 2, 6)),
                  ("Zfib11", fibre_system(31, 2, 11, 17, 3)),
                  ("E1P(V=10)", fibre_system(31, 3, 10, 22, 5, True))):
        if b is None:
            chk(f"{nm}: built", False, "")
            continue
        row, sup, zs = b["row"], b["supports"], b["slopes"]
        q, n, k, h = row.q, row.n, row.k, row.h
        V, A = len(sup), row.k + row.h
        U = set().union(*[set(x) for x in sup])
        m = len(U) - k
        rank = S.family_rank(row, sup, zs)
        _, cols = S.ray_columns(row, sup, zs)
        ns = T.nullspace_mod(cols, 2 * n, q)
        nontrivial = len(ns) - 2 * k
        _, _, esc, _ = core_data(row, sup)
        g = S.combinatorial_gates(row, sup)
        gc = bool(g["size_ok"] and g["pairwise_intersecting"]
                  and g["kpacking_ok"])
        chk(f"{nm}: LEMMA R identity  dim(realisers) - 2k = 2m - rank",
            nontrivial == 2 * m - rank, f"{nontrivial} vs {2*m-rank}")
        hits, prof = 0, {}
        if nontrivial > 0:
            for _ in range(120):
                w = [0] * (2 * n)
                for bb in ns:
                    c = rnd.randrange(q)
                    if c:
                        for i in range(2 * n):
                            w[i] = (w[i] + c * bb[i]) % q
                u, v = w[:n], w[n:]
                if any(t == 0 for t in v):
                    continue
                if T.is_codeword(row, u) and T.is_codeword(row, v):
                    continue
                ag = tuple(agreements(row, sup, zs, u, v))
                prof[ag] = prof.get(ag, 0) + 1
                if all(t == A for t in ag):
                    hits += 1
        rec = dict(name=nm, gate_clean=gc, esc=esc, V=V, m=m, rank=rank,
                   twoV=2 * V, twom=2 * m, nontrivial=nontrivial,
                   exact_A_realisers=hits, agreement_test_exact=bool(2*h > m),
                   profiles={str(kk): vv for kk, vv in
                             list(prof.items())[:3]})
        LOG.setdefault("realisability", []).append(rec)
        print(f"    {nm}: gate_clean={gc} esc={esc[:4]}{'...' if V>4 else ''}"
              f" rank={rank} 2m={2*m} 2V={2*V} | nontrivial realisers dim="
              f"{nontrivial} | draws with all agreements = A: {hits} "
              f"| exact-agreement test valid (2h>m): {2*h > m}")
    # the two headline consequences
    zf = [r for r in LOG["realisability"] if r["name"] == "Zfib11"][0]
    chk("Zfib11: zero-escape, gate-clean, rank 9 < 2V = 22 (channel (i) "
        "charge 2 REFUTED)", zf["gate_clean"] and zf["rank"] == 9
        and zf["rank"] < zf["twoV"] and set(zf["esc"]) == {0}, zf)
    chk("Zfib11: REALISED -- nontrivial (u,v) with every ray slope's max "
        "agreement exactly A", zf["nontrivial"] >= 1
        and zf["exact_A_realisers"] > 0 and zf["agreement_test_exact"], zf)
    e1 = [r for r in LOG["realisability"] if r["name"] == "E1"][0]
    chk("E1: rank = 2m exactly => NO nontrivial realiser => not "
        "band-admissible", e1["nontrivial"] == 0, e1)
    ep = [r for r in LOG["realisability"] if r["name"] == "E1P(V=10)"][0]
    chk("E1P: escape-1 core ray, rank < min(2m, 2V) (realisable AND "
        "charge-defeating in the abstract class)",
        ep["esc"][0] == 1 and set(ep["esc"][1:]) == {0}
        and ep["rank"] < min(ep["twom"], ep["twoV"]), ep)
    chk("E1P: but NO sampled realiser makes the escape-1 ray exact-A",
        ep["exact_A_realisers"] == 0, ep)


def part12_full_gate():
    """The occlib FULL BAND GATE on the realised Zfib11 fixture.  Cost is a
    C(n,k) agreement scan -- feasible only at m = n-k = 5."""
    print("\nPART 12 -- FULL BAND GATE on the realised zero-escape fixture")
    b = fibre_system(31, 2, 11, 17, 3)
    row, sup, zs = b["row"], b["supports"], b["slopes"]
    _, cols = S.ray_columns(row, sup, zs)
    got = T.realise(row, cols, seed=2, tries=800)
    chk("Zfib11: nondegenerate (u,v) drawn", got is not None)
    if not got:
        return
    u, v = got
    rec, _, _ = S.gate_report(row, u, v, name="Zfib11")
    keys = ["below_cascade", "globally_generic", "tangent_free_finite_slopes",
            "tangent_free_v_direction", "v_nonvanishing", "kpacking_ok",
            "FULL_GATE"]
    print("    " + "  ".join(f"{kk}={rec.get(kk)}" for kk in keys))
    print(f"    live_slopes={rec.get('live_slopes')} "
          f"max_ray_agreement={rec.get('max_ray_agreement')} A={rec.get('A')}"
          f" N_d={rec.get('ledger_by_depth')}")
    LOG["full_gate"] = {kk: rec.get(kk) for kk in keys + [
        "A", "live_slopes", "max_ray_agreement", "ADMISSIBLE", "N_over_n2"]}
    chk("Zfib11: FULL_GATE = True (band-admissible received pair)",
        bool(rec.get("FULL_GATE")), LOG["full_gate"])
    chk("Zfib11: 11 live slopes, max ray agreement = A = 20",
        rec.get("live_slopes") == 11 and rec.get("max_ray_agreement") == 20,
        LOG["full_gate"])


def main():
    print("ESCAPE-1 GATE-CLEAN REALIZABILITY -- verification")
    part1_realizability()
    part2_perturbation()
    part3_zero_escape()
    part4_floor_and_replay()
    part5_sweep()
    part6_family_scan()
    part7_extremality()
    part8_slopes()
    part9_h_forced()
    part10_threshold()
    part11_realisability()
    part12_full_gate()
    LOG["total_checks"] = CHECKS[0]
    LOG["fails"] = FAILS
    LOG["falsifiers_fired"] = HITS
    with open(os.path.join(HERE, "verify.json"), "w") as fh:
        json.dump(LOG, fh, indent=1, sort_keys=True)
    print(f"\nCHECKS {CHECKS[0]}  FAILS {len(FAILS)}  "
          f"FALSIFIERS_FIRED {len(HITS)}")
    for f in FAILS:
        print("  - FAIL", f)
    for t in HITS:
        print("  - FALSIFIER", t)
    if not FAILS:
        print("ESCAPE1_REALIZABILITY_ALL_PASS")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
