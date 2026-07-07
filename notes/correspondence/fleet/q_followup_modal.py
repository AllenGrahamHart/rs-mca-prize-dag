#!/usr/bin/env python3
"""Fleet follow-up (Modal): (a) structure-classify the (41,20,10,2) argmax
fiber (raw mode-at-null violation: max 133 at z* != 0 vs null 66 — is the
fiber quotient-structured, i.e. charged to their rungs, or primitive?);
(b) float64 ladder extension to (577,96,48,2), (1153,128,64,2), validated
against the exact (101,50,25,2) row; (c) high-precision dense-bulk ratios."""
import json

import modal

app = modal.App("rs-mca-fleet-followup")
image = modal.Image.debian_slim().pip_install("numpy")


def _subgroup(p, N):
    for cand in range(2, p):
        x, seen = 1, set()
        for _ in range(p - 1):
            x = x * cand % p
            seen.add(x)
        if len(seen) == p - 1:
            g = cand
            break
    h = pow(g, (p - 1) // N, p)
    return sorted(pow(h, i, p) for i in range(N))


@app.function(image=image, cpu=2, memory=2048, timeout=120)
def argmax_structure(_):
    """Exhaustive at (41,20,10,2): C(20,10) = 184756 subsets — enumerate
    directly, find argmax fiber, classify every member."""
    import itertools
    p, N, m, w = 41, 20, 10, 2
    D = _subgroup(p, N)
    Dset = set(D)
    from collections import defaultdict
    fib = defaultdict(list)
    for S in itertools.combinations(D, m):
        p1 = sum(S) % p
        p2 = sum(x * x for x in S) % p
        fib[(p1, p2)].append(S)
    null = len(fib[(0, 0)])
    (z1, z2), members = max(fib.items(), key=lambda kv: len(kv[1]))
    mx = len(members)
    # dilation orbit of z*: (g z1, g^2 z2) for g in mu_N
    orbit = {( (g * z1) % p, (g * g * z2) % p) for g in D}
    orbit_sizes = sorted({len(fib[z]) for z in orbit})
    # classify members of the argmax fiber
    def is_pair_union(S):          # union of 5 antipodal mu_2-cosets
        Ss = set(S)
        return all((p - x) % p in Ss for x in S)
    def dilation_stab(S):          # exists g != 1 in mu_N with gS = S
        Ss = set(S)
        return [g for g in D if g != 1 and all((g * x) % p in Ss for x in S)]
    def contains_coset(S, d):      # contains a full mu_d coset
        Ss = set(S)
        mu_d = {x for x in D if pow(x, d, p) == 1}
        reps = set()
        for x in S:
            reps.add(frozenset((x * y) % p for y in mu_d))
        return any(c <= Ss for c in reps)
    cls = {"pair_union": 0, "dilation_stable": 0, "contains_mu5": 0,
           "contains_mu4": 0, "contains_mu2": 0, "plain": 0}
    plain_examples = []
    for S in members:
        tagged = False
        if is_pair_union(S): cls["pair_union"] += 1; tagged = True
        if dilation_stab(S): cls["dilation_stable"] += 1; tagged = True
        if contains_coset(S, 5): cls["contains_mu5"] += 1; tagged = True
        if contains_coset(S, 4): cls["contains_mu4"] += 1; tagged = True
        if contains_coset(S, 2): cls["contains_mu2"] += 1; tagged = True
        if not tagged:
            cls["plain"] += 1
            if len(plain_examples) < 3:
                plain_examples.append(list(S))
    # baseline: same classification rates over RANDOM subsets (the whole space)
    import random
    rng = random.Random(7)
    base = {"contains_mu2": 0, "plain_ish": 0}
    trials = 4000
    for _ in range(trials):
        S = tuple(rng.sample(D, m))
        if contains_coset(S, 2):
            base["contains_mu2"] += 1
    return {"z_star": (z1, z2), "max": mx, "null": null,
            "orbit_fiber_sizes": orbit_sizes, "classes": cls,
            "plain_examples": plain_examples,
            "baseline_mu2_rate": base["contains_mu2"] / trials,
            "n_members": len(members)}


@app.function(image=image, cpu=4, memory=8192, timeout=300)
def fiber_census_f64(job):
    """Float64 fiber census (for rows whose counts exceed int64).
    Validated against the exact row (101,50,25,2)."""
    import numpy as np
    p, N, m, w = job
    D = _subgroup(p, N)
    shape = (m + 1,) + (p,) * w
    dp = np.zeros(shape, dtype=np.float64)
    dp[(0,) + (0,) * w] = 1.0
    for x in D:
        v = [pow(x, h, p) for h in range(1, w + 1)]
        shifted = dp[:m]
        for ax in range(w):
            shifted = np.roll(shifted, v[ax], axis=1 + ax)
        dp[1:] += shifted
    fib = dp[m]
    from math import comb, log2
    total = float(fib.sum())
    expected = comb(N, m)
    checksum_rel = abs(total - expected) / expected
    mx = float(fib.max())
    nullf = float(fib[(0,) * w])
    mean = expected / p ** w
    return {"p": p, "N": N, "m": m, "w": w,
            "max_over_mean_minus1": mx / mean - 1.0,
            "null_over_mean_minus1": nullf / mean - 1.0,
            "max_is_null": bool(abs(mx - nullf) < 0.4),
            "checksum_rel_err": checksum_rel}


@app.local_entrypoint()
def main():
    jobs = [(101, 50, 25, 2), (577, 96, 48, 2), (1153, 128, 64, 2)]
    s_handle = argmax_structure.spawn(0)
    f64 = list(fiber_census_f64.map(jobs, return_exceptions=True))
    st = s_handle.get()
    print("=== (41,20,10,2) argmax fiber structure ===")
    print(json.dumps(st, indent=1))
    print("\n=== float64 ladder extension (dense bulk) ===")
    for r in f64:
        if not isinstance(r, dict):
            print("  worker error:", str(r)[:140]); continue
        print(f"  ({r['p']},{r['N']},{r['m']},{r['w']}): max/mean-1 = {r['max_over_mean_minus1']:.3e}, "
              f"null/mean-1 = {r['null_over_mean_minus1']:.3e}, max==null: {r['max_is_null']}, "
              f"checksum err {r['checksum_rel_err']:.1e}")
    with open("/tmp/fleet_followup.json", "w") as f:
        json.dump({"structure": st, "f64": [r for r in f64 if isinstance(r, dict)]}, f, indent=1)
