#!/usr/bin/env python3
"""F5 P5-E1 (Modal): exhaustive live-slope censuses at official-SHAPED toys.

Row shape: k = n/2, t = 2, A = k + 2 (supports of size n/2 + 2) — the
regime where catch #10 showed set-combinatorics is vacuous. The per-W
pencil scan is COMPLETE: every size-A support contains a k-subset W, and
codewords through W form the pencil P_W + z Q_W, so enumerating all
W in C(D, k) with their coincidence-slope histograms finds every live
(z, S, c) triple.

Per pair (u, v):
  - for each k-subset W: interpolate P_W, Q_W; for x outside W compute
    the coincidence class: unique slope zeta_W(x) (case a), DEGENERATE
    (case b: pencil matches the pair at x), or DEAD (case c);
  - >= t degenerate points => TANGENT event (the pair-level strip): flag
    and charge; slopes with >= t - d own-class points are LIVE through W;
  - aggregate live slopes over all W (a slope is live if ANY W carries
    it); report raw and post-strip counts, plus core geometry.

Words: random pairs + engineered families (pencil-perturbations designed
to stack many W-classes onto shared slopes — the stacking falsifier).
Kill standard (pre-registered): sustained super-polynomial growth of the
post-strip live-slope count across n, or engineered stacking beating the
per-stratum pencil arithmetic.
"""
import itertools
import json
import random

import modal

app = modal.App("rs-mca-f5-p5e2b")
image = modal.Image.debian_slim()

# (n, q, t, n_random_pairs, n_engineered, seed)  # SUB-MEAN windows
ROWS = [
    (12, 97, 3, 40, 20, 111),
    (16, 97, 3, 30, 15, 222),
]


@app.function(image=image, cpu=4, memory=4096, timeout=280)
def census(row):
    n, q, t, n_rand, n_eng, seed = row
    rng = random.Random(seed)
    k = n // 2
    A = k + t

    def inv(a):
        return pow(a % q, q - 2, q)

    # domain = order-n subgroup of F_q*
    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1
                    for r in {2, 3} if (q - 1) % r == 0))
    h = pow(g, (q - 1) // n, q)
    D = sorted(pow(h, i, q) for i in range(n))

    # precompute Lagrange interpolation weights per k-subset is too heavy;
    # interpolate on demand (k <= 12, cheap).
    def interp_eval(W, vals, xs):
        """Evaluate the deg<k interpolant of (W -> vals) at points xs."""
        out = []
        for x in xs:
            acc = 0
            for i, wi in enumerate(W):
                num, den = 1, 1
                for j, wj in enumerate(W):
                    if i == j:
                        continue
                    num = num * (x - wj) % q
                    den = den * (wi - wj) % q
                acc = (acc + vals[i] * num % q * inv(den)) % q
            out.append(acc)
        return out

    def live_slope_census(u, v):
        """Complete live-slope enumeration for the pair; returns stats."""
        live_raw = {}          # z -> set of frozenset supports (raw)
        live_post = {}         # post-strip
        tangent_W = 0
        vzero = [x for x in D if v[x] == 0]
        for W in itertools.combinations(D, k):
            outside = [x for x in D if x not in set(W)]
            Pv = interp_eval(W, [u[x] for x in W], outside)
            Qv = interp_eval(W, [v[x] for x in W], outside)
            classes = {}
            degen = []
            for x, px, qx in zip(outside, Pv, Qv):
                dv = (v[x] - qx) % q
                du = (px - u[x]) % q
                if dv == 0:
                    if du == 0:
                        degen.append(x)
                    continue
                z = du * inv(dv) % q
                classes.setdefault(z, []).append(x)
            d = len(degen)
            if d >= t:
                tangent_W += 1     # pair-level tangent event through W
            for z, pts in classes.items():
                if len(pts) + d >= t:
                    for extra in itertools.combinations(pts, max(t - d, 0)):
                        S = frozenset(W) | set(extra) | set(degen[:t - len(extra)])
                        if len(S) == A:
                            live_raw.setdefault(z, set()).add(S)
                if len(pts) >= t and d < t:
                    S = frozenset(W) | set(pts[:t])
                    live_post.setdefault(z, set()).add(S)
        # L1: one support per slope; pairwise core cap <= A-2 automatic for
        # distinct supports of equal size. Count slopes.
        Nraw, Npost = len(live_raw), len(live_post)
        # core geometry of the post-strip family (greedy one per slope)
        picks = [next(iter(s)) for s in live_post.values()]
        maxcore = 0
        for S1, S2 in itertools.combinations(picks[:60], 2):
            maxcore = max(maxcore, len(S1 & S2))
        return {"N_raw": Nraw, "N_post": Npost, "tangent_W": tangent_W,
                "n_vzero": len(vzero), "max_pair_core": maxcore}

    results = {"row": {"n": n, "q": q, "k": k, "A": A}, "random": [],
               "engineered": []}
    for _ in range(n_rand):
        u = {x: rng.randrange(q) for x in D}
        v = {x: rng.randrange(1, q) for x in D}
        results["random"].append(live_slope_census(u, v))
    # ENGINEERED stacking: start from a pencil (u,v) = (c0 + z0*w0, w0) with
    # c0, w0 codewords (maximally tangent-degenerate), then perturb r points
    # to escape the strip while keeping many W-pencils near-degenerate.
    for _ in range(n_eng):
        c0 = [rng.randrange(q) for _ in range(k)]
        w0 = [rng.randrange(q) for _ in range(k)]
        def ev(cf, x):
            acc = 0
            for c in reversed(cf):
                acc = (acc * x + c) % q
            return acc
        z0 = rng.randrange(q)
        u = {x: (ev(c0, x) + z0 * ev(w0, x)) % q for x in D}
        v = {x: ev(w0, x) % q for x in D}
        r = rng.randrange(t, t + 3)   # perturb just past the tangent radius
        for x in rng.sample(D, r):
            u[x] = (u[x] + rng.randrange(1, q)) % q
        for x in rng.sample(D, r):
            v[x] = (v[x] + rng.randrange(1, q)) % q
        if any(v[x] == 0 for x in D):
            for x in D:
                if v[x] == 0:
                    v[x] = 1
        results["engineered"].append(live_slope_census(u, v))
    return results


@app.local_entrypoint()
def main():
    out = list(census.map(ROWS, return_exceptions=True))
    print(f"{'row (n,q)':>12} {'family':>11} {'N_post max/med':>15} {'N_raw max':>10} "
          f"{'tangentW max':>13} {'maxcore':>8}")
    for r in out:
        if not isinstance(r, dict):
            print("worker error:", str(r)[:140]); continue
        for fam in ("random", "engineered"):
            rows = r[fam]
            if not rows:
                continue
            Np = sorted(x["N_post"] for x in rows)
            Nr = max(x["N_raw"] for x in rows)
            tw = max(x["tangent_W"] for x in rows)
            mc = max(x["max_pair_core"] for x in rows)
            print(f"  ({r['row']['n']},{r['row']['q']})".rjust(12) +
                  f" {fam:>11} {Np[-1]:>7}/{Np[len(Np)//2]:<7} {Nr:>10} {tw:>13} {mc:>8}")
    with open("/tmp/f5_p5e2.json", "w") as f:
        json.dump([r for r in out if isinstance(r, dict)], f, indent=1)
    print("\nSUB-MEAN windows: any nonzero N_post is an anti-concentration event to classify")
