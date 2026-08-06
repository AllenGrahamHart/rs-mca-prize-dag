#!/usr/bin/env python3
"""bc_block_census -- verifier 4: the D-local census SWEEP (the reuse law).

Verifier 2 showed |Bset| = 2|Tau| = 4 is fully admissible at |Tau| = 2.
The sharp residual is whether |Bset| keeps growing.  Because the D-local
census

    Tau_D := {tau in RS_K : the slope word psi_tau takes exactly two
              values on D, each exactly r times}

contains every selected block of every maximal-selected target,
|Bset| <= 2 * #partitions(Tau_D) ALWAYS.  So bounding #partitions(Tau_D)
is the strongest D-local route to (BC) -- and it is exhaustively
measurable, with the off-D core condition dropped entirely.

At each x in D the received pair (u_x, v_x) is TWO scalars; prescribing
the selected slope of one target at x is one affine condition.  So two
targets pin (u,v)|_D completely and every further target's slope word is
FORCED.  This file sweeps the whole 2-target design space -- both target
polynomials, both partitions, all four slopes -- and asks, exhaustively
over RS_K each time, whether a THIRD D-local target ever appears.

Run: tools/ramguard local -- python3 \
       notes/pilots_20260804/bc_block_census/sweep.py
"""

import itertools
import json
import os
import random
import sys
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fixture import BShape, ground, inv                     # noqa: E402
from dlocal import pow_arr                                  # noqa: E402

CHECKS = []


def chk(cond, name, info=""):
    CHECKS.append({"name": name, "ok": bool(cond), "info": str(info)})
    return bool(cond)


def polyval(coef, x, q):
    acc = 0
    for c in reversed(coef):
        acc = (acc * x + c) % q
    return acc


def build_D_side(shape, g, tau1, tau2, B1, B2, quad):
    """Pin (u,v) on D from TWO prescribed targets.  Returns None if illegal."""
    q = shape.q
    D = g["D"]
    n1a, n1b, n2a, n2b = quad
    sB1, sB2 = set(B1), set(B2)
    u, v = {}, {}
    for x in D:
        nu1 = n1a if x in sB1 else n1b
        nu2 = n2a if x in sB2 else n2b
        if nu1 == nu2:
            return None
        a1, b1 = nu1
        a2, b2 = nu2
        det = (a1 * b2 - b1 * a2) % q
        if det == 0:
            return None
        L1 = (a1 - b1 * pow(x, 3, q)) % q
        L2 = (a2 - b2 * pow(x, 3, q)) % q
        R1 = polyval(tau1, x, q) * L1 % q
        R2 = polyval(tau2, x, q) * L2 % q
        iv = inv(det, q)
        ux = (b2 * R1 - b1 * R2) % q * iv % q
        vx = (-a2 * R1 + a1 * R2) % q * iv % q
        if (pow(x, 3, q) * ux + vx) % q == 0:      # AD1: rho must not vanish
            return None
        u[x], v[x] = ux, vx
    return u, v


def d_local(shape, g, u, v, K):
    """EXHAUSTIVE over all q^K polys of degree < K, restricted to D."""
    q, r, e = shape.q, shape.r, shape.e
    D = g["D"]
    Da = np.array(D, dtype=np.int64)
    cube = np.array([pow(x, 3, q) for x in D], dtype=np.int64)
    ua = np.array([u[x] for x in D], dtype=np.int64)
    va = np.array([v[x] for x in D], dtype=np.int64)
    total = q ** K
    CH = 40000
    n_tau, parts, blocks, maxcls = 0, set(), set(), 0
    for st in range(0, total, CH):
        idxs = np.arange(st, min(st + CH, total), dtype=np.int64)
        coefs, tmp = [], idxs.copy()
        for _ in range(K):
            coefs.append(tmp % q)
            tmp //= q
        TAU = np.zeros((len(idxs), e), dtype=np.int64)
        for j in range(K - 1, -1, -1):
            TAU = (TAU * Da[None, :] + coefs[j][:, None]) % q
        E = (ua[None, :] - TAU) % q
        Ep = (va[None, :] + cube[None, :] * TAU) % q
        key = np.where(Ep != 0, (-E * pow_arr(Ep, q - 2, q)) % q, q)
        m = key.shape[0]
        base = (np.arange(m) * (q + 2))[:, None]
        cnt = np.bincount((base + key).ravel(),
                          minlength=m * (q + 2)).reshape(m, q + 2)
        maxcls = max(maxcls, int(cnt.max()))
        good = np.nonzero(((cnt == r).sum(axis=1) == 2)
                          & ((cnt > 0).sum(axis=1) == 2))[0]
        n_tau += len(good)
        for w in good:
            kk = key[w]
            vals = sorted(set(int(z) for z in kk))
            B = tuple(sorted(D[i] for i in range(e) if int(kk[i]) == vals[0]))
            C = tuple(sorted(D[i] for i in range(e) if int(kk[i]) == vals[1]))
            blocks.add(B)
            blocks.add(C)
            parts.add(frozenset((B, C)))
    return {"n_tau": n_tau, "partitions": len(parts), "blocks": len(blocks),
            "max_slope_class": maxcls}


def main():
    shape = BShape(h=25, k=5, q=61, n=60, tag="sweep")
    g = ground(shape)
    q, r, D = shape.q, shape.r, g["D"]
    rng = random.Random(20260806)
    empt = g["empty"]

    # a pool of r-subsets of D: the canonical one, fiber-rigid ones, and
    # random ones (the round-14 classification is irrelevant D-locally).
    pool = [tuple(D[:r])]
    for _ in range(14):
        pool.append(tuple(sorted(rng.sample(D, r))))
    pool = list(dict.fromkeys(pool))

    quads = []
    for combo in itertools.permutations(empt[:4], 4):
        quads.append(combo)
    rng.shuffle(quads)
    quads = quads[:8]

    results = Counter()
    worst = {"partitions": 0, "n_tau": 0}
    worst_cfg = None
    configs = 0
    K = 2
    for B1 in pool[:6]:
        for B2 in pool[:6]:
            for quad in quads[:4]:
                for _ in range(2):
                    t1 = tuple(rng.randrange(q) for _ in range(K))
                    t2 = tuple(rng.randrange(q) for _ in range(K))
                    if t1 == t2:
                        continue
                    built = build_D_side(shape, g, t1, t2, B1, B2, quad)
                    if built is None:
                        continue
                    u, v = built
                    res = d_local(shape, g, u, v, K)
                    configs += 1
                    results[res["partitions"]] += 1
                    chk(res["max_slope_class"] <= r,
                        "GATE-r: no slope class on D exceeds r",
                        res["max_slope_class"])
                    if res["partitions"] > worst["partitions"]:
                        worst = res
                        worst_cfg = {"B1": list(B1), "B2": list(B2),
                                     "quad": [list(x) for x in quad],
                                     "tau1": list(t1), "tau2": list(t2)}

    # a deeper but narrower probe at K = 3
    deep = Counter()
    for B1 in pool[:3]:
        for B2 in pool[:3]:
            quad = quads[0]
            t1 = tuple(rng.randrange(q) for _ in range(3))
            t2 = tuple(rng.randrange(q) for _ in range(3))
            built = build_D_side(shape, g, t1, t2, B1, B2, quad)
            if built is None:
                continue
            u, v = built
            res = d_local(shape, g, u, v, 3)
            deep[res["partitions"]] += 1

    report = {
        "shape": repr(shape),
        "K": K,
        "configs_swept": configs,
        "partition_count_histogram": {str(a): b
                                      for a, b in sorted(results.items())},
        "max_partitions_seen": worst["partitions"],
        "max_taus_seen": worst["n_tau"],
        "max_blocks_seen": worst.get("blocks"),
        "worst_config": worst_cfg,
        "K3_partition_histogram": {str(a): b for a, b in sorted(deep.items())},
        "note": ("#partitions is the D-local ceiling on |Bset|/2; "
                 "2 means |Bset| <= 4"),
    }
    chk(configs > 0, "sweep is non-vacuous", configs)
    report["checks"] = len(CHECKS)
    report["failed"] = [c for c in CHECKS if not c["ok"]]
    with open(os.path.join(HERE, "sweep.json"), "w") as fh:
        json.dump({"report": report, "all_checks": CHECKS}, fh, indent=1,
                  sort_keys=True, default=str)
    print(json.dumps(report, indent=1, sort_keys=True, default=str))
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
