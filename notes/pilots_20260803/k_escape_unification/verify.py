#!/usr/bin/env python3
r"""K/ESCAPE UNIFICATION -- machine verification (pilot 2026-08-03, round 7).

THE TWO RESIDUAL OBJECTS, in the shared ray-system notation
(z_a, S_a)_{a=1..V}, z_a in P^1(F_q) distinct, |S_a| = A = k+h,
Rel = {(c_a) in (+)_a C_{S_a} : sum_a e(z_a) (x) c_a = 0},
rank = V h - dim Rel  (per-ray accounting, BAND_LANE_DEFINITIONS item 11).

  ESC  (band lane; xr_support4_structure Claim 6 / pilot S4-15):
       S_a^(i+1) = S_a^(i) ^ W^(i), W^(i) = triple locus of the CURRENT
       supports; ALL rays are kept.  Escape floor
       rank >= sum_a min(h, |S_a \ S_a^inf|).
       Implementation of record: support4_relation/stage5_escape.py:49-70.

  KER  (P-A1 exact-k lane; D0-2 peeling + locality-death):
       drop any ray with >= h points of family-coverage <= 2 (equivalently
       |S_a ^ W| <= k), recompute coverage on the SURVIVING rays, iterate;
       the residual ray set is K.  Implementation of record:
       exact_k_heart/stage4_scan.py:59-79.

  PHI  (the operator proposed here): do BOTH -- shrink supports to the
       triple locus of the live sub-family AND drop rays whose shrunken
       support has <= k points; iterate.  State (F, (T_a)).

PRE-REGISTERED FALSIFIERS (fixed before any run; any hit refutes the
named claim and is reported as such, not silently dropped):

  F1  kernel floor > true rank on ANY system      -> refutes U3 (soundness)
  F2  escape floor > kernel floor on ANY system   -> refutes U4 (domination)
  F3  ESC needs >= 2 effective iterations anywhere -> refutes U1 (one-step)
  F4  PHI's surviving ray set != stage4_scan.peel's core, or
      T_a^PHI != S_a ^ W_infinity, on ANY system  -> refutes U2 (PHI = KER)
  F5  on the separating fixtures: K nonempty, or rank != V h, or
      escape floor >= rank                        -> kills the separation
  F6  a system whose KERNEL escapes are all >= 2 but with rank < 2V
                                                  -> refutes the relaxed heart
  F7  banked fixture replay disagrees with the node's recorded numbers
      (U-mechanism floor 16 / cap 4 / rank 19; K_V floor 35 = rank = V h)

Reuse: s4lib.py, stage5_escape.py (support4_relation) and stage4_scan.py
(exact_k_heart) are IMPORTED, never copied.  Read-only.

Run: tools/ramguard tiny -- python3 \
     notes/pilots_20260803/k_escape_unification/verify.py
"""
from __future__ import annotations

import json
import os
import random
import sys

sys.dont_write_bytecode = True

_P = "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802"
for _d in ("support4_relation", "exact_k_heart"):
    p = os.path.join(_P, _d)
    if p not in sys.path:
        sys.path.append(p)

import s4lib as S                                              # noqa: E402
import tslib as T                                              # noqa: E402
import stage5_escape as S5                                     # noqa: E402
import stage4_scan as Z4                                       # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKS = [0]
FAILS = []
LOG = {"checks": [], "fixtures": [], "sweep": {}, "separating": []}


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    LOG["checks"].append(dict(label=label, ok=bool(ok), detail=str(detail)))
    if not ok:
        FAILS.append(label)
        print("  FAIL", label, detail)
    return bool(ok)


# ------------------------------------------------------------- the operator
def locus(supports, live, n, Tsets=None):
    """Triple locus of the live sub-family (using T_a if given, else S_a)."""
    mult = [0] * n
    for a in live:
        src = supports[a] if Tsets is None else Tsets[a]
        for x in src:
            mult[x] += 1
    return frozenset(x for x in range(n) if mult[x] >= 3)


def phi_kernel(row, supports, trace=False):
    """PHI: shrink to the triple locus AND drop rays with <= k points.
    Returns (live set, {a: T_a}, #iterations, [W_i trace])."""
    n, k = row.n, row.k
    live = set(range(len(supports)))
    Ts = {a: frozenset(supports[a]) for a in live}
    it, tr = 0, []
    while True:
        it += 1
        W = locus(supports, live, n, Ts)
        tr.append(W)
        newTs = {a: Ts[a] & W for a in live}
        newlive = {a for a in live if len(newTs[a]) >= k + 1}
        if newlive == live and all(newTs[a] == Ts[a] for a in live):
            return live, Ts, it, tr
        live = newlive
        Ts = {a: newTs[a] for a in live}


def esc_residual(row, supports):
    """The band lane's escape residual, from the record implementation."""
    return S5.peel(row, supports)


def esc_floor(row, supports):
    _, cap, floor = S5.peel_bound(row, supports)
    return cap, floor


def ker_floor(row, supports):
    """rank >= sum_a min(h, |S_a \\ T_a^*|), T_a^* = T_a^PHI (a in K), else
    empty; and dim Rel <= sum_{a in K} (|T_a| - k)^+."""
    k, h = row.k, row.h
    live, Ts, _, _ = phi_kernel(row, supports)
    floor = 0
    for a, Sa in enumerate(supports):
        t = len(Ts[a]) if a in live else 0
        floor += min(h, len(Sa) - t)
    cap = sum(max(0, len(Ts[a]) - k) for a in live)
    return live, Ts, cap, floor


def ker_escapes(row, supports):
    live, Ts, _, _ = phi_kernel(row, supports)
    return [len(S_) - (len(Ts[a]) if a in live else 0)
            for a, S_ in enumerate(supports)]


# ------------------------------------------------------------- separating S1
def build_S1(k, h):
    """MINIMAL SEPARATING FIXTURE.  H = k+h-1 points shared by two survivor
    rays; each point of H gets its third coverer from a doomed ray that
    touches <= k-1 points of H (so (T) holds).  Both survivors clear the
    round-1 death test (|S ^ W_0| = k+h-1 >= k+1) and then die in round 2.
    One-step escape of the survivors is exactly 1 (< 2): the escape form of
    the occupancy heart FAILS, while every ray's KERNEL escape is >= h."""
    A = k + h
    Hn = k + h - 1
    H = list(range(Hn))
    nxt = Hn
    sup = [tuple(sorted(H + [nxt])), tuple(sorted(H + [nxt + 1]))]
    nxt += 2
    c = max(1, k - 1)
    doomed, i = [], 0
    while i < Hn:
        blk = H[i:i + c]
        i += c
        priv = list(range(nxt, nxt + A - len(blk)))
        nxt += len(priv)
        doomed.append(tuple(sorted(blk + priv)))
    sup += doomed
    return sup, nxt


# ------------------------------------------------------------- separating S2
def build_S2(k):
    """GATE-CLEAN SEPARATING FIXTURE.  Two survivors, each with a (k+1)-cycle
    of doomed rays supplying the third coverer of its k+1 triple-locus points
    (each doomed ray in exactly 2 of them, so <= k: it dies at round 1).
    Pair fillers (2-covered) then make the system PAIRWISE-INTERSECTING and
    padding equalises |S_a| = A, without touching the triple locus."""
    surv = [0, 1]
    V = 2 + 2 * (k + 1)
    dead = {0: list(range(2, 2 + k + 1)),
            1: list(range(2 + k + 1, V))}
    specs = []
    for s in surv:
        D = dead[s]
        for i in range(k + 1):
            specs.append((s, D[i], D[(i + 1) % (k + 1)]))
    sets = [set() for _ in range(V)]
    nxt = 0
    for sp in specs:
        for a in sp:
            sets[a].add(nxt)
        nxt += 1
    W0 = frozenset(range(nxt))
    for a in range(V):
        for b in range(a + 1, V):
            need = k - len(sets[a] & sets[b])
            for _ in range(max(0, need)):
                sets[a].add(nxt)
                sets[b].add(nxt)
                nxt += 1
    A = max(len(s) for s in sets)
    for a in range(V):
        while len(sets[a]) < A:
            sets[a].add(nxt)
            nxt += 1
    return [tuple(sorted(s)) for s in sets], nxt, A, W0


# ------------------------------------------------------------ random systems
def rand_system(rng, n, k, h, V):
    A = k + h
    return [tuple(sorted(rng.sample(range(n), A))) for _ in range(V)]


def slopes_for(rng, q, V):
    return rng.sample(range(1, q), V)


def gates(supports, k):
    """(T) triple gate and pairwise-intersecting flag."""
    V = len(supports)
    ss = [set(s) for s in supports]
    tmax = 0
    for a in range(V):
        for b in range(a + 1, V):
            for c in range(b + 1, V):
                tmax = max(tmax, len(ss[a] & ss[b] & ss[c]))
    pmin = min((len(ss[a] & ss[b]) for a in range(V)
                for b in range(a + 1, V)), default=0)
    return tmax, pmin


# ===========================================================================
def part1_banked():
    """F7: replay the two banked escape-floor fixtures of the node."""
    print("\n[1] banked fixture replay (xr_support4_structure claim 6)")
    # U-mechanism (3,5,1,4): floor 16, cap 4, rank 19
    k, h, d, V, q = 3, 5, 1, 4, 6421
    priv = (h - 1) - (V - 1) * d
    n = (k + 2) + (V * (V - 1) // 2) * d + V * priv + 2
    row = T.Row2(n, k, h, q)
    fam = S.build_mobius_family(row, d, V, seed=1)
    sup, zs = fam["supports"], fam["slopes"]
    cap, floor = esc_floor(row, sup)
    rank = S.family_rank(row, sup, zs)
    live, Ts, kcap, kfloor = ker_floor(row, sup)
    chk("F7a U-mechanism escape floor 16 / cap 4 / rank 19",
        (floor, cap, rank) == (16, 4, 19), f"{floor} {cap} {rank}")
    chk("F7a U-mechanism: PHI kernel = ALL 4 rays, kernel floor = escape",
        live == set(range(V)) and kfloor == floor and kcap == cap,
        f"live={sorted(live)} kfloor={kfloor} kcap={kcap}")
    LOG["fixtures"].append(dict(name="U-mechanism(3,5,1,4)", n=n, V=V,
                                esc_floor=floor, esc_cap=cap, rank=rank,
                                ker_floor=kfloor, ker_cap=kcap,
                                K=sorted(live), Vh=V * h))
    # K_V (3,7,1,5): floor 35 = rank = V h, S^inf sizes 2
    k, h, d, V, q = 3, 7, 1, 5, 6421
    M = V * (V - 1) // 2
    n = max((k - 1) + M * (d + 1), k + h + 2)
    row = T.Row2(n, k, h, q)
    _, _, info = S5.ADV.build_KV(row, d, V, seed=0)
    sup = [tuple(s) for s in info["supports"].values()]
    zs = list(info["zs"])
    lim = esc_residual(row, sup)
    cap, floor = esc_floor(row, sup)
    rank = S.family_rank(row, sup, zs)
    live, Ts, kcap, kfloor = ker_floor(row, sup)
    chk("F7b K_V escape floor 35 = rank = V h, |S^inf| = 2",
        floor == 35 and rank == 35 and rank == V * h
        and sorted(len(x) for x in lim) == [2] * V, f"{floor} {rank}")
    chk("F7b K_V: PHI kernel EMPTY (every ray dies), floors agree",
        live == set() and kfloor == floor, f"live={sorted(live)} {kfloor}")
    chk("F7b K_V uncapped sum 40 would be FALSE (cap load-bearing)",
        sum(len(sup[a]) - len(lim[a]) for a in range(V)) == 40
        and 40 > rank, "")
    LOG["fixtures"].append(dict(name="K_V(3,7,1,5)", n=n, V=V,
                                esc_floor=floor, rank=rank, ker_floor=kfloor,
                                K=sorted(live), Vh=V * h))


def part2_onestep_and_equiv(systems):
    """U1 (one step), U2 (PHI = KER = stage4_scan.peel)."""
    print("\n[2] U1 one-step collapse of ESC; U2  PHI = KER")
    bad1 = bad2 = bad2b = 0
    for (row, sup, zs) in systems:
        n = row.n
        W0 = locus(sup, range(len(sup)), n)
        onestep = [frozenset(s) & W0 for s in sup]
        lim = esc_residual(row, sup)
        if [frozenset(x) for x in lim] != onestep:
            bad1 += 1
        live, Ts, _, _ = phi_kernel(row, sup)
        rays = [(zs[a], tuple(sup[a])) for a in range(len(sup))]
        _, core = Z4.peel(row, rays)
        core_sup = {tuple(sorted(s)) for _, s in core}
        if {tuple(sorted(sup[a])) for a in live} != core_sup:
            bad2 += 1
        Winf = locus(sup, live, n)
        if any(Ts[a] != frozenset(sup[a]) & Winf for a in live):
            bad2b += 1
    chk("F3/U1: ESC residual = S_a ^ W_0 on every system (one step)",
        bad1 == 0, f"{bad1} deviations / {len(systems)}")
    chk("F4/U2: PHI live set = stage4_scan.peel core on every system",
        bad2 == 0, f"{bad2} deviations / {len(systems)}")
    chk("F4/U2: T_a^PHI = S_a ^ W_infinity on every system",
        bad2b == 0, f"{bad2b} deviations / {len(systems)}")


def part3_floors(systems):
    """U3 (soundness), U4 (domination), F6 (relaxed heart)."""
    print("\n[3] U3 soundness, U4 domination, F6 relaxed heart")
    n_unsound = n_dom = n_strict = n_f6 = n_f6hyp = 0
    n_esc2 = 0
    tbl = []
    for (row, sup, zs) in systems:
        V, h = len(sup), row.h
        cap_e, fl_e = esc_floor(row, sup)
        live, Ts, cap_k, fl_k = ker_floor(row, sup)
        dim, _, _ = S.relation_space(row, sup, zs)
        rank = V * h - dim
        rank2 = S.family_rank(row, sup, zs)
        if rank != rank2:
            chk("rank consistency (Vh - dim Rel == family_rank)", False,
                f"{rank} {rank2}")
        if fl_k > rank:
            n_unsound += 1
        if dim > cap_k:
            n_unsound += 1
        if fl_e > fl_k:
            n_dom += 1
        if fl_k > fl_e:
            n_strict += 1
        esc1 = [len(s) - len(x) for s, x in zip(sup, esc_residual(row, sup))]
        eK = ker_escapes(row, sup)
        if min(esc1) >= 2:
            n_esc2 += 1
        if min(eK) >= 2:
            n_f6hyp += 1
            if rank < 2 * V:
                n_f6 += 1
        tbl.append((fl_e, fl_k, rank, V * h, len(live)))
    chk("F1/U3: kernel floor <= rank and dim Rel <= kernel cap, ALWAYS",
        n_unsound == 0, f"{n_unsound} violations / {len(systems)}")
    chk("F2/U4: escape floor <= kernel floor, ALWAYS",
        n_dom == 0, f"{n_dom} violations / {len(systems)}")
    chk("F6: kernel-escape >= 2 everywhere => rank >= 2V, ALWAYS",
        n_f6 == 0, f"{n_f6} violations in {n_f6hyp} hypothesis-holding")
    LOG["sweep"] = dict(systems=len(systems), unsound=n_unsound,
                        domination_violations=n_dom,
                        strictly_better=n_strict,
                        onestep_escape2_systems=n_esc2,
                        kernel_escape2_systems=n_f6hyp,
                        f6_violations=n_f6)
    print(f"    {len(systems)} systems: kernel floor STRICTLY better on "
          f"{n_strict}; one-step escape>=2 on {n_esc2}, kernel escape>=2 on "
          f"{n_f6hyp}")


def part4_separating():
    """F5: the two separating fixtures."""
    print("\n[4] separating fixtures")
    for (k, h) in [(2, 2), (3, 3), (2, 4), (4, 2), (5, 3)]:
        sup, n = build_S1(k, h)
        V, A = len(sup), k + h
        q = 1009 if n < 1000 else 100003
        row = T.Row2(n, k, h, q)
        assert all(len(s) == A for s in sup), (k, h)
        tmax, pmin = gates(sup, k)
        cap_e, fl_e = esc_floor(row, sup)
        live, Ts, cap_k, fl_k = ker_floor(row, sup)
        esc1 = [len(s) - len(x) for s, x in zip(sup, esc_residual(row, sup))]
        eK = ker_escapes(row, sup)
        ranks = set()
        for seed in range(4):
            rng = random.Random(1000 + seed)
            zs = slopes_for(rng, q, V)
            ranks.add(S.family_rank(row, sup, zs))
        ok = (live == set() and ranks == {V * h} and fl_k == V * h
              and fl_e < V * h and min(esc1) == 1 and min(eK) >= h
              and tmax <= k - 1)
        chk(f"F5 S1(k={k},h={h}): K empty, rank = Vh = {V*h}, escape floor "
            f"{fl_e} < {V*h}, min one-step escape 1, (T) ok",
            ok, f"ranks={sorted(ranks)} fl_e={fl_e} fl_k={fl_k} "
                f"esc1={esc1} eK={eK} tmax={tmax} pmin={pmin}")
        LOG["separating"].append(dict(kind="S1", k=k, h=h, n=n, V=V,
                                      A=A, esc_floor=fl_e, ker_floor=fl_k,
                                      rank=sorted(ranks), Vh=V * h,
                                      one_step_escapes=esc1,
                                      kernel_escapes=eK,
                                      triple_max=tmax, pair_min=pmin,
                                      supports=[list(s) for s in sup]))
        print(f"    S1(k={k},h={h}): V={V} n={n} esc_floor={fl_e} "
              f"ker_floor={fl_k} rank={sorted(ranks)} esc1={esc1}")

    for k in (2, 3):
        sup, n, A, W0 = build_S2(k)
        h = A - k
        V = len(sup)
        q = 1009 if n < 1000 else 100003
        row = T.Row2(n, k, h, q)
        tmax, pmin = gates(sup, k)
        cap_e, fl_e = esc_floor(row, sup)
        live, Ts, cap_k, fl_k = ker_floor(row, sup)
        esc1 = [len(s) - len(x) for s, x in zip(sup, esc_residual(row, sup))]
        eK = ker_escapes(row, sup)
        rng = random.Random(77)
        zs = slopes_for(rng, q, V)
        rank = S.family_rank(row, sup, zs)
        W0c = locus(sup, range(V), n)
        ok = (live == set() and rank == V * h and fl_k == V * h
              and fl_e == V * h - 2 and tmax <= k - 1 and pmin >= k
              and W0c == W0)
        chk(f"F5 S2(k={k}): GATE-CLEAN (triples <= {k-1}, pairs >= {k}), "
            f"K empty, kernel floor {fl_k} = rank, escape floor {fl_e}",
            ok, f"rank={rank} fl_e={fl_e} fl_k={fl_k} tmax={tmax} "
                f"pmin={pmin} h={h} V={V} n={n}")
        LOG["separating"].append(dict(kind="S2", k=k, h=h, n=n, V=V, A=A,
                                      esc_floor=fl_e, ker_floor=fl_k,
                                      rank=rank, Vh=V * h,
                                      one_step_escapes=esc1,
                                      kernel_escapes=eK,
                                      triple_max=tmax, pair_min=pmin))
        print(f"    S2(k={k}): V={V} n={n} A={A} h={h} esc_floor={fl_e} "
              f"ker_floor={fl_k} rank={rank} triples<={tmax} pairs>={pmin}")


def main():
    part1_banked()
    print("\n[*] building the random/structured sweep")
    systems = []
    rng = random.Random(20260803)
    for _ in range(90):
        k = rng.choice([2, 3, 4])
        h = rng.choice([2, 3, 4])
        V = rng.choice([4, 5, 6])
        n = rng.choice([k + h + 2, k + h + 4, k + h + 6])
        q = 1009
        row = T.Row2(n, k, h, q)
        sup = rand_system(rng, n, k, h, V)
        zs = slopes_for(rng, q, V)
        systems.append((row, sup, zs))
    # structured: U-cliques, K_V, and cascade fixtures
    for (k, h, d, V) in [(9, 4, 1, 4), (13, 4, 1, 5), (5, 4, 2, 4)]:
        n = k + 2 * h - d + 2
        row = T.Row2(n, k, h, 6421)
        cl = S5.build_u_clique(row, d, V)
        if cl:
            systems.append((row, cl["supports"],
                            [1 + 7 * a for a in range(V)]))
    for (k, h, d, V) in [(3, 7, 1, 5), (4, 7, 1, 5), (3, 5, 1, 4)]:
        M = V * (V - 1) // 2
        n = max((k - 1) + M * (d + 1), k + h + 2)
        row = T.Row2(n, k, h, 6421)
        got = S5.ADV.build_KV(row, d, V, seed=0)
        if got:
            _, _, info = got
            systems.append((row, [tuple(s) for s in info["supports"].values()],
                            list(info["zs"])))
    for (k, h) in [(2, 2), (3, 3), (2, 4)]:
        sup, n = build_S1(k, h)
        row = T.Row2(n, k, h, 1009)
        systems.append((row, sup, slopes_for(random.Random(5), 1009,
                                             len(sup))))
    part2_onestep_and_equiv(systems)
    part3_floors(systems)
    part4_separating()

    LOG["total_checks"] = CHECKS[0]
    LOG["fails"] = FAILS
    with open(os.path.join(HERE, "verify.json"), "w") as fh:
        json.dump(LOG, fh, indent=1, sort_keys=True)
    print(f"\nCHECKS {CHECKS[0]}  FAILS {len(FAILS)}")
    if FAILS:
        for f in FAILS:
            print("  -", f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
