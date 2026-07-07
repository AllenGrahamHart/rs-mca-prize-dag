#!/usr/bin/env python3
"""F5-A2 (floor campaign, Modal): engineered spread stacking — second attack
family on the xr_smallcore 16n^3 floor.

MECHANISM: adversarially CONSTRUCT the pair (u, v) to align as many
distinct-slope supports as possible (each support = A points where a
codeword agrees with u + z_i v), all pairwise-small-core. Dimension count
predicts the engineered maximum ~ (fresh-point budget)/(overdetermination)
= O(n/sigma) — far under 16n^3; the attack measures whether greedy
construction can beat that scaling (an alarm would mean the dimension
argument leaks and the floor's margin is not structural).

Greedy exact construction per row: maintain partial assignments of u, v
over the domain; for each new slope z_i, pick a support S_i (pairwise
core < k+t-1 with all previous, |S_i| = A = k+sigma) maximizing fresh
points; the codeword c_i must interpolate the forced values on
already-assigned points of S_i (deg < k), assign the rest freely. Count
alignments achieved until saturation. PRE-REGISTERED: alarm = achieved
family exceeding 8 * (2n/sigma) at any row, sustained across scales
(vs the 16n^3 budget the floor allows — the alarm is set at the
dimension-count scale to detect leaks early; an actual floor violation
would need n^3-scale families, wildly beyond).
"""
import json
import random

import modal

app = modal.App("rs-mca-f5a2-engspread")
image = modal.Image.debian_slim()

ROWS = [(2, 47, 2), (2, 97, 2), (2, 193, 2), (3, 97, 2), (3, 193, 2)]
TRIES_PER_ROW = 8


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def engineer_row(payload):
    k, q, t, seed = payload
    rng = random.Random(seed)
    n = q - 1
    domain = list(range(1, q))
    A = k + 1                      # sigma = 1
    core_thresh = k + t - 1

    def interp(pts, vals):
        # Lagrange deg<k through len(pts) <= k points -> coeff tuple, or
        # evaluator via coefficients
        m = len(pts)
        coeffs = [0] * k
        for xi, yi in zip(pts, vals):
            num = [1]
            den = 1
            for xj in pts:
                if xj == xi:
                    continue
                new = [0] * (len(num) + 1)
                for tt, a in enumerate(num):
                    new[tt] = (new[tt] - a * xj) % q
                    new[tt + 1] = (new[tt + 1] + a) % q
                num = new
                den = den * (xi - xj) % q
            s = yi * pow(den, -1, q) % q
            for tt in range(len(num)):
                coeffs[tt] = (coeffs[tt] + s * num[tt]) % q
        return coeffs

    def ev(coeffs, x):
        acc = 0
        for c in reversed(coeffs):
            acc = (acc * x + c) % q
        return acc

    best = 0
    for _ in range(TRIES_PER_ROW):
        u = {}
        v = {}
        fam = []                    # (z, support)
        slopes = list(range(q))
        rng.shuffle(slopes)
        for z in slopes:
            # choose support: prefer fresh points; enforce pairwise small core
            placed = False
            for attempt in range(12):
                fresh = [x for x in domain if x not in u]
                used = [x for x in domain if x in u]
                rng.shuffle(fresh)
                rng.shuffle(used)
                # need c_i deg<k through forced values on used∩S; keep
                # used-part <= k so interpolation is free
                take_used = used[:rng.randrange(0, min(len(used), k) + 1)]
                S = take_used + fresh[:A - len(take_used)]
                if len(S) < A:
                    continue
                S = S[:A]
                if any(len(set(S) & set(S2)) >= core_thresh for _, S2 in fam):
                    continue
                forced_pts = [x for x in S if x in u]
                if len(forced_pts) > k:
                    continue
                forced_vals = [(u[x] + z * v[x]) % q for x in forced_pts]
                # build codeword through forced points (pad with random fresh)
                pts = forced_pts[:]
                vals = forced_vals[:]
                for x in S:
                    if x not in u and len(pts) < k:
                        pts.append(x)
                        vals.append(rng.randrange(q))
                cw = interp(pts, vals) if pts else [rng.randrange(q) for _ in range(k)]
                # assign u, v on fresh points of S: u(x) + z v(x) = cw(x);
                # one free dof per point — set v randomly, solve u
                ok = True
                for x in S:
                    cx = ev(cw, x)
                    if x in u:
                        if (u[x] + z * v[x]) % q != cx:
                            ok = False
                            break
                    else:
                        vv = rng.randrange(q)
                        u[x] = (cx - z * vv) % q
                        v[x] = vv
                if ok:
                    fam.append((z, S))
                    placed = True
                    break
            if not placed and len(u) >= n:
                break
        best = max(best, len(fam))
    dim_bound = 8 * 2 * n          # 8 * (2n / sigma), sigma = 1
    return {"k": k, "q": q, "n": n, "achieved": best,
            "dim_scale_2n": 2 * n, "alarm": best > dim_bound,
            "budget_16n3": 16 * n**3}


@app.local_entrypoint()
def main():
    payloads = [(k, q, t, 4200 + i) for i, (k, q, t) in enumerate(ROWS)]
    results = [r for r in engineer_row.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    for r in sorted(results, key=lambda r: (r["k"], r["q"])):
        flag = "  <-- ALARM" if r["alarm"] else ""
        print(f"k={r['k']} q={r['q']} n={r['n']}: engineered family = {r['achieved']} "
              f"(2n = {r['dim_scale_2n']}, budget = {r['budget_16n3']}){flag}")
    with open("/tmp/f5a2_results.json", "w") as f:
        json.dump(results, f, indent=1)
