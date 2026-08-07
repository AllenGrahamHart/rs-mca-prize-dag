#!/usr/bin/env python3
"""D3 MANDATORY ADVERSARIAL: hill-climb for a violating FPC5 rate-half
M=4,t=2 witness at reachable scale.

Escape test (registered in PREREG R3, ESCAPE-RH):
  (a) some admissible sharp-cell source at ell in {4,5,6} yields
      N_exact >= 4*(ell-2) for a single touched pair; or
  (b) max_source N_exact doubles from ell=4 to 5 and again 5 to 6.

Search moves: swap a core point with a background/petal point; permute a
petal point with a core point; resample a label.  Objective: N_split
(coarse) then N_exact (fine), on ONE fixed touched pair, with a restart
schedule.  Also reports the primitivity/exactness suppression ratio.
"""
from __future__ import annotations

import json
import random
import sys
from itertools import combinations

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from rh_fast import census_fast, make_source  # noqa: E402
from rh_m4t2_census import domain  # noqa: E402


def score(core, bg, petals, labels, pair, ell, q, rng):
    ns, npm, nex, w, _ = census_fast(core, bg, petals, labels, pair,
                                     ell, q, rng)
    return ns, npm, nex, w


def mutate(core, bg, petals, labels, q, rng):
    core = core[:]
    bg = bg[:]
    petals = [p[:] for p in petals]
    labels = labels[:]
    m = rng.randrange(4)
    if m == 0:                       # swap core <-> background
        i = rng.randrange(len(core))
        j = rng.randrange(len(bg))
        core[i], bg[j] = bg[j], core[i]
    elif m == 1:                     # swap core <-> a petal point
        i = rng.randrange(len(core))
        pi = rng.randrange(4)
        j = rng.randrange(len(petals[pi]))
        core[i], petals[pi][j] = petals[pi][j], core[i]
    elif m == 2:                     # swap two petals' points
        p1, p2 = rng.sample(range(4), 2)
        j1 = rng.randrange(len(petals[p1]))
        j2 = rng.randrange(len(petals[p2]))
        petals[p1][j1], petals[p2][j2] = petals[p2][j2], petals[p1][j1]
    else:                            # resample one label
        i = rng.randrange(4)
        cand = rng.randrange(1, q)
        while cand in labels:
            cand = rng.randrange(1, q)
        labels[i] = cand
    return sorted(core), bg, petals, labels


def main():
    ell = int(sys.argv[1])
    q = int(sys.argv[2])
    restarts = int(sys.argv[3])
    steps = int(sys.argv[4])
    seed = int(sys.argv[5]) if len(sys.argv) > 5 else 20260807
    n = 10 * ell - 8
    pts, cyc = domain(n, q)
    rng = random.Random(seed)
    pair = (0, 1)
    best = {"split": -1, "prim": -1, "exact": -1}
    best_src = None
    trace = []
    total_evals = 0
    split_hist = {}
    supp = []          # (split, prim, exact) whenever split >= 2
    for R in range(restarts):
        core, bg, petals, labels = make_source(pts, ell, q, rng)
        cur = score(core, bg, petals, labels, pair, ell, q, rng)
        total_evals += 1
        for _ in range(steps):
            c2, b2, p2, l2 = mutate(core, bg, petals, labels, q, rng)
            cand = score(c2, b2, p2, l2, pair, ell, q, rng)
            total_evals += 1
            key = cand[0]
            split_hist[key] = split_hist.get(key, 0) + 1
            if cand[0] >= 2:
                supp.append([cand[0], cand[1], cand[2]])
            # lexicographic (exact, prim, split) improvement, accept ties
            if (cand[2], cand[1], cand[0]) >= (cur[2], cur[1], cur[0]):
                core, bg, petals, labels = c2, b2, p2, l2
                cur = cand
            if (cur[2], cur[1], cur[0]) > (best["exact"], best["prim"],
                                           best["split"]):
                best = {"split": cur[0], "prim": cur[1], "exact": cur[2]}
                best_src = {"core": core, "bg": bg, "petals": petals,
                            "labels": labels,
                            "witness_D": cur[3]["D"] if cur[3] else None}
                trace.append(dict(best, restart=R))
    thr = 4 * (ell - 2)
    print(json.dumps({
        "mode": "adversary", "ell": ell, "q": q, "n": n,
        "two_power_n": (n & (n - 1)) == 0, "mu_n_domain": cyc,
        "restarts": restarts, "steps": steps, "evals": total_evals,
        "best": best,
        "escape_threshold_N_exact": thr,
        "ESCAPE_RH_a_FIRED": best["exact"] >= thr,
        "split_histogram": dict(sorted(split_hist.items())),
        "suppression_samples": supp[:40],
        "n_suppression_samples": len(supp),
        "trace": trace[-8:],
        "best_source": best_src,
    }))


if __name__ == "__main__":
    main()
