#!/usr/bin/env python3
"""FM3 mechanism pilot -- population-level (PRE-selection) statistics.

Factorises the concentration excess as

    P_selected[core >= K]  =  P_population[core >= K]  x  TILT

and measures P_population directly from the complete witness population
(enumerated with the banked prior-pilot enumerator, imported read-only), so
that "is the population itself already concentrated?" is answered by
measurement rather than by assumption.

Also measures the structure of the >= K-core pairs actually realised in each
selected family: where the symmetric difference lives, and how the two slopes
are related.

    tools/ramguard local -- python3 .../fm3_pop.py CASE [CASE...]
"""
from __future__ import annotations
import json
import math
import os
import random
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(os.path.dirname(_HERE), "pb_selector_orders")
_PRIOR = os.path.join(os.path.dirname(_HERE), "pb_split_fibre_selector")
sys.dont_write_bytecode = True
sys.path.insert(0, _PRIOR)
sys.path.insert(0, _BANK)
sys.path.insert(0, _HERE)
import pb_split_fibre_pilot as P   # noqa: E402
import k1_orders as KO             # noqa: E402
from fm3_predict import NEW        # noqa: E402
from fm3_mine import hypergeom_overlap, tail, SUPPORT_ORDERS, NULL_ORDERS  # noqa

KO.CASES.update(NEW)
PC = bin


def popc(x):
    return bin(x).count("1")


def run(name, seed=20260802, pair_samples=400000, probe=120):
    prm = dict(KO.CASES[name])
    case = P.Case(name, dict(prm))
    case.build_family()
    n, q, K, A, m, h = case.n, case.q, case.K, case.A, case.m, case.h
    byslope = {}
    tot = 0

    def on_sol(z, mask):
        nonlocal tot
        byslope.setdefault(z, []).append(mask)
        tot += 1

    P.enumerate_all_witnesses(case, on_sol)
    live = sorted(byslope)
    rnd = random.Random(seed)

    # --- population coordinate marginals (exact) --------------------------
    freq = [0] * n
    for z in live:
        for msk in byslope[z]:
            for i in range(n):
                if (msk >> i) & 1:
                    freq[i] += 1
    pop_marg = [f / tot for f in freq]

    # --- population pairwise-core law over DISTINCT-slope pairs -----------
    flat = [(z, msk) for z in live for msk in byslope[z]]
    N = len(flat)
    hist = [0] * (A + 1)
    got = 0
    npair_exact = None
    if N * (N - 1) // 2 <= 20_000_000:
        for i in range(N):
            zi, mi = flat[i]
            for j in range(i + 1, N):
                if flat[j][0] == zi:
                    continue
                hist[popc(mi & flat[j][1])] += 1
                got += 1
        npair_exact = got
    else:
        for _ in range(pair_samples):
            i = rnd.randrange(N)
            j = rnd.randrange(N)
            if flat[i][0] == flat[j][0]:
                continue
            hist[popc(flat[i][1] & flat[j][1])] += 1
            got += 1
    pop_hist = [c / got for c in hist]

    # --- population: expected number of >=K partners per witness ----------
    probe = max(20, min(probe, 4_000_000 // max(N, 1)))
    probe_idx = [rnd.randrange(N) for _ in range(min(probe, N))]
    partners = []
    for pi in probe_idx:
        zi, mi = flat[pi]
        c = 0
        for zj, mj in flat:
            if zj == zi:
                continue
            if popc(mi & mj) >= K:
                c += 1
        partners.append(c)
    mean_partners = sum(partners) / len(partners)
    analytic = sum(math.comb(A, c) * math.comb(n - A, A - c) / q ** (h - 1)
                   for c in range(K, A - m + 1))

    n0 = hypergeom_overlap(n, A)
    out = dict(case=name, n=n, q=q, K=K, A=A, m=m, h=h,
               total_witnesses=tot, live=len(live),
               mean_Wz=tot / len(live),
               pop_marginals=pop_marg,
               pop_marg_max=max(pop_marg), pop_marg_min=min(pop_marg),
               pop_marg_chi=sum(p * p for p in pop_marg),
               uniform_chi=A * A / n,
               pop_hist=pop_hist, pop_pairs=got, pop_pairs_exact=npair_exact,
               pop_mean_core=sum(t * pop_hist[t] for t in range(A + 1)),
               pop_p_ge_K=tail(pop_hist, K),
               null_uniform_p_ge_K=tail(n0, K),
               null_uniform_mean=sum(t * n0[t] for t in range(A + 1)),
               mean_ge_K_partners_measured=mean_partners,
               mean_ge_K_partners_analytic=analytic,
               frac_witness_with_partner=sum(1 for c in partners if c) /
               len(partners),
               )

    # --- selected families: tilt + >=K pair structure ---------------------
    bank = os.path.join(_BANK, f"k1_{name}.json")
    if not os.path.exists(bank):
        bank = os.path.join(_HERE, f"k1_{name}.json")
    sel = json.load(open(bank))["orders"]
    out["orders"] = {}
    for o in SUPPORT_ORDERS + NULL_ORDERS:
        sm = sel[o]["selected_masks"]
        zs = sorted(int(z) for z in sm)
        masks = [sm[str(z)] for z in zs]
        M = len(masks)
        h2 = [0] * (A + 1)
        dfreq = [0] * n
        zdiff = {}
        npairs = 0
        hipairs = 0
        for i in range(M):
            for j in range(i + 1, M):
                c = popc(masks[i] & masks[j])
                h2[c] += 1
                npairs += 1
                if c >= K:
                    hipairs += 1
                    d = masks[i] ^ masks[j]
                    for t in range(n):
                        if (d >> t) & 1:
                            dfreq[t] += 1
                    dz = (zs[i] - zs[j]) % q
                    dz = min(dz, q - dz)
                    zdiff[dz] = zdiff.get(dz, 0) + 1
        sel_p = sum(h2[K:]) / npairs if npairs else 0.0
        out["orders"][o] = dict(
            sel_p_ge_K=sel_p,
            sel_mean_core=sum(t * h2[t] for t in range(A + 1)) / npairs,
            hi_pairs=hipairs,
            tilt_over_population=(sel_p / out["pop_p_ge_K"]
                                  if out["pop_p_ge_K"] > 0 else None),
            tilt_over_uniform=(sel_p / out["null_uniform_p_ge_K"]
                               if out["null_uniform_p_ge_K"] > 0 else None),
            symdiff_coord_freq=dfreq,
            slope_gap_hist=dict(sorted(zdiff.items())),
            slope_gap_distinct=len(zdiff),
        )
    return out


def main():
    names = sys.argv[1:] or ["Q1", "Q3", "Q8"]
    allout = {}
    fn = os.path.join(_HERE, "POP.json")
    if os.path.exists(fn):
        allout = json.load(open(fn))
    for nm in names:
        r = run(nm)
        allout[nm] = r
        print(f"[{nm}] n={r['n']} q={r['q']} K={r['K']} A={r['A']} "
              f"h={r['h']} witnesses={r['total_witnesses']} "
              f"live={r['live']} meanW={r['mean_Wz']:.1f}")
        print(f"    POPULATION: marg in [{r['pop_marg_min']:.4f},"
              f"{r['pop_marg_max']:.4f}] (uniform {r['A']/r['n']:.4f}) "
              f"chi={r['pop_marg_chi']:.4f} (uniform {r['uniform_chi']:.4f})")
        print(f"    POPULATION core: mean={r['pop_mean_core']:.4f} "
              f"(uniform null {r['null_uniform_mean']:.4f})  "
              f"P>=K={r['pop_p_ge_K']:.3e} "
              f"(uniform null {r['null_uniform_p_ge_K']:.3e})  "
              f"pairs={r['pop_pairs']}"
              f"{' EXACT' if r['pop_pairs_exact'] else ' sampled'}")
        print(f"    POPULATION >=K partners per witness: "
              f"measured={r['mean_ge_K_partners_measured']:.3f} "
              f"analytic={r['mean_ge_K_partners_analytic']:.3f} "
              f"frac with >=1 partner={r['frac_witness_with_partner']:.3f}")
        for o in SUPPORT_ORDERS + NULL_ORDERS:
            e = r["orders"][o]
            print(f"    {o:21s} P_sel>=K={e['sel_p_ge_K']:.5f} "
                  f"tilt/pop={e['tilt_over_population']} "
                  f"tilt/unif={e['tilt_over_uniform']} "
                  f"hi_pairs={e['hi_pairs']} "
                  f"symdiff_span={sum(1 for x in e['symdiff_coord_freq'] if x)}")
    with open(fn, "w") as fh:
        json.dump(allout, fh, sort_keys=True)
    print("->", fn)


if __name__ == "__main__":
    main()
