#!/usr/bin/env python3
"""F5 P8 (Modal): independent replay of upstream's exact saturation
identity (thm:saturation) + line-ray version (prop:line-ray-saturation),
PLUS the W-scan corollary that F5's aggregation actually consumes.

Claims replayed, all exact, full enumeration, official-shaped toy rows
(k = n/2, t = 2, A = k + 2):

  (1) per word U_z:   Cen(U_z; A) = sum_c C(s_c(U_z), A)
      (m = A > k, so the interpolating codeword per support is unique;
      Cen counted directly over all size-A supports).
  (2) line version:   sum_z Cen(U_z; A) = sum_{rays (z,c), s >= A} C(s, A),
      and N_slopes <= #rays <= sum_z Cen.
  (3) W-scan form:    sum_{W in C(D,k)} #{(z,c) ray: s >= A, W subset S}
                      = sum_{rays} C(s_{z,c}, k),
      both sides counted independently (left: interpolate U_z on every
      k-set W; any interpolant with agreement >= A is a ray through W,
      and W lies inside its agreement set automatically).

(3) is the W-multiplicity aggregation instrument for F5-OS stratum (i):
the per-W pencil scan sees each ray through exactly C(s, k) k-cores, so
per-W sunflower budgets aggregate by RAYS with an exact fiber factor.

One pair per worker; any identity mismatch refutes the import.
"""
import itertools
import json
import random
from math import comb

import modal

app = modal.App("rs-mca-f5-p8-lineray")
image = modal.Image.debian_slim()

# (n, q, family, seed)
JOBS = ([(12, 97, "random", 601 + i) for i in range(6)] +
        [(12, 97, "near-pencil", 621 + i) for i in range(4)] +
        [(16, 97, "random", 641 + i) for i in range(2)] +
        [(16, 97, "near-pencil", 661 + i) for i in range(2)])


@app.function(image=image, cpu=2, memory=1024, timeout=280)
def check(job):
    n, q, fam, seed = job
    rng = random.Random(seed)
    k = n // 2
    t = 2
    A = k + t
    inv_t = [0] + [pow(a, q - 2, q) for a in range(1, q)]

    def pf(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d)
                x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out

    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = sorted(pow(h, i, q) for i in range(n))

    def ev(cf, x):
        acc = 0
        for c in reversed(cf):
            acc = (acc * x + c) % q
        return acc

    def interp(pts, vals):
        m = len(pts)
        cf = [0] * m
        for i in range(m):
            xi = pts[i]
            num, den = [1], 1
            for j in range(m):
                if j == i:
                    continue
                xj = pts[j]
                new = [0] * (len(num) + 1)
                for d in range(len(num)):
                    cc = num[d]
                    new[d] = (new[d] - cc * xj) % q
                    new[d + 1] = (new[d + 1] + cc) % q
                num = new
                den = den * (xi - xj) % q
            w = vals[i] * inv_t[den] % q
            for d in range(m):
                cf[d] = (cf[d] + num[d] * w) % q if d < len(num) else cf[d]
        return tuple(cf)

    # draw the pair
    if fam == "random":
        u = {x: rng.randrange(q) for x in D}
        v = {x: rng.randrange(1, q) for x in D}
    else:
        c0 = [rng.randrange(q) for _ in range(k)]
        w0 = [rng.randrange(q) for _ in range(k)]
        z0 = rng.randrange(q)
        u = {x: (ev(c0, x) + z0 * ev(w0, x)) % q for x in D}
        v = {x: ev(w0, x) % q for x in D}
        for x in rng.sample(D, t + 1):
            u[x] = (u[x] + rng.randrange(1, q)) % q
        for x in rng.sample(D, t + 1):
            v[x] = (v[x] + rng.randrange(1, q)) % q
        for x in D:
            if v[x] == 0:
                v[x] = 1

    # --- parts (1) + (2): support census and ray census per word ---
    cen_sum = 0
    rays = {}
    for z in range(q):
        Uz = {x: (u[x] + z * v[x]) % q for x in D}
        per_cen = 0
        per_rays = {}
        for T in itertools.combinations(D, A):
            c = interp(T[:k], [Uz[x] for x in T[:k]])
            if all(ev(c, x) == Uz[x] for x in T[k:]):
                per_cen += 1
                if c not in per_rays:
                    per_rays[c] = sum(ev(c, x) == Uz[x] for x in D)
        assert per_cen == sum(comb(s, A) for s in per_rays.values()), \
            ("per-word identity FAILED", z)
        cen_sum += per_cen
        for c, s in per_rays.items():
            rays[(z, c)] = s
    ray_side = sum(comb(s, A) for s in rays.values())
    assert cen_sum == ray_side, "line identity FAILED"
    n_slopes = len({z for (z, _) in rays})
    assert n_slopes <= len(rays) <= cen_sum, "inequalities FAILED"

    # --- part (3): W-scan, left side independent of the ray census ---
    left = 0
    for W in itertools.combinations(D, k):
        for z in range(q):
            vals = [(u[x] + z * v[x]) % q for x in W]
            c = interp(list(W), vals)
            s = sum(ev(c, x) == (u[x] + z * v[x]) % q for x in D)
            if s >= A:
                left += 1
    right = sum(comb(s, k) for s in rays.values())
    assert left == right, ("W-scan corollary FAILED", left, right)

    return {"n": n, "q": q, "family": fam, "seed": seed,
            "n_slopes": n_slopes, "n_rays": len(rays), "cen_sum": cen_sum,
            "w_pairs": left,
            "mean_W_fiber": round(left / len(rays), 1) if rays else 0.0}


@app.local_entrypoint()
def main():
    res = list(check.map(JOBS, return_exceptions=True))
    print(f"{'row':>10} {'family':>12} {'slopes':>7} {'rays':>6} "
          f"{'cen_sum':>9} {'(W,z) pairs':>12} {'mean C(s,k)':>12}")
    fails = 0
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:160])
            continue
        print(f"  ({r['n']},{r['q']})".rjust(10) +
              f" {r['family']:>12} {r['n_slopes']:>7} {r['n_rays']:>6} "
              f"{r['cen_sum']:>9} {r['w_pairs']:>12} "
              f"{r['mean_W_fiber']:>12}")
    with open("/tmp/f5_p8_lineray.json", "w") as f:
        json.dump([r for r in res if isinstance(r, dict)], f, indent=1)
    if fails:
        raise SystemExit(f"F5_P8_LINERAY_SATURATION_REPLAY_FAIL ({fails})")
    print("\nall three identities held exactly on every pair "
          "(per-word, line, W-scan)")
    print("F5_P8_LINERAY_SATURATION_REPLAY_PASS")
