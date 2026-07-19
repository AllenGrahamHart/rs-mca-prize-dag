#!/usr/bin/env python3
"""Exact shadow-weighted multiplicity M = sum_g s_g at every census prime with
>= 2 raw primitive orbits (the only primes where M can exceed ~1.x).

Pro's round-6 conditional theorem: R_L = 0 and M_L <= M* = 13.2907840779 for
all 34 levels => DLI-AGG.  Here s_g = 1 + sum over g's shadow orbits of
2^-(w' - L - 1) with L = 1 (these census rows are first-moment rows), i.e. a
shadow orbit of weight w' contributes 2^-(w'-2) relative to its generator's
base ledger term.  Generators = multiplier-independent components (union-find
over ternary-multiplier edges, exactly the census convention); each component
charges its minimal-weight orbit as the generator and the rest as shadow.

Output: per-prime M table for the worst primes + global maximum.
"""
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("census", HERE / "modal_dli_orbit_census.py")
census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(census)

L = 1  # first-moment census rows

def exact_M(q: int, nprime: int, wmax: int) -> tuple[float, int, int, list]:
    N = nprime // 2
    omega = census.pinned_omega(q, nprime)
    orbs = {}
    for w in range(3, wmax + 1):
        for sup, sgn in census.find_vanishers(
            census.combo_array(N, w), census.sign_matrix(w), omega, q
        ):
            k = census.orbit_key(sup, sgn, N)
            if k not in orbs and census.is_primitive(sup, sgn, omega, q):
                orbs[k] = {"w": w, "rep": (sup, sgn), "prim": True}
    # partition into multiplier components exactly as independent_components
    # does (same edges, same union-find), but keep the classes
    keys = list(orbs)
    parent = list(range(len(keys)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    import itertools
    for i, j in itertools.combinations(range(len(keys)), 2):
        if find(i) == find(j):
            continue
        vi = census.to_coeffs(*orbs[keys[i]]["rep"], N)
        vj = census.to_coeffs(*orbs[keys[j]]["rep"], N)
        if census.multiplier_edge(vi, keys[j], N) or census.multiplier_edge(vj, keys[i], N):
            parent[find(i)] = find(j)
    classes = {}
    for idx, k in enumerate(keys):
        classes.setdefault(find(idx), []).append(k)
    comps = list(classes.values())
    M = 0.0
    detail = []
    for cls in comps:
        ws = sorted(orbs[k]["w"] for k in cls)
        s_g = 1.0 + sum(2.0 ** -(w - L - 1) for w in ws[1:])
        M += s_g
        detail.append({"gen_w": ws[0], "shadow_ws": ws[1:], "s_g": round(s_g, 4)})
    return M, len(orbs), len(comps), detail


def main():
    res = json.load(open(HERE / "orbit_census_results.json"))
    rows = []
    for cfg in res["configs"]:
        if cfg["config"].startswith("E"):
            continue
        nprime, wmax = cfg["nprime"], cfg["wmax"]
        multi = {ex["q"] for ex in cfg.get("multi_indep_examples", [])}
        # also include every prime whose raw k_indep >= 2 per the stored map
        ppk = cfg.get("per_prime_k_indep", {})
        for qs, k in (ppk.items() if isinstance(ppk, dict) else []):
            if k >= 2:
                multi.add(int(qs))
        for q in sorted(multi):
            M, n_orb, n_gen, detail = exact_M(q, nprime, wmax)
            rows.append({"config": cfg["config"], "q": q, "raw_orbits": n_orb,
                         "generators": n_gen, "M": round(M, 4), "detail": detail})
    rows.sort(key=lambda r: -r["M"])
    out = {"threshold_Mstar": 13.290784077959,
           "n_multiorbit_primes": len(rows),
           "worst": rows[:10],
           "max_M": rows[0]["M"] if rows else None}
    (HERE / "empirical_M_ledger.json").write_text(json.dumps(out, indent=1))
    for r in rows[:10]:
        print(f"{r['config']} q={r['q']}: raw={r['raw_orbits']} gens={r['generators']} M={r['M']}")
    print(f"\nMAX empirical M = {out['max_M']}  vs  M* = 13.2907840779")


if __name__ == "__main__":
    main()
