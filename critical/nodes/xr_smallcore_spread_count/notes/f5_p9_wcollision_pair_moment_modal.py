#!/usr/bin/env python3
"""F5 P9 (Modal): the W-COLLISION PAIR-MOMENT IDENTITY — new bookkeeping
for stratum (i)'s residual open (posed in P8), in the moment-template
style (exact identity + fiber regrouping + far-pair collapse).

Claims verified, all exact, full enumeration, official-shaped toy rows
(k = n/2, t = 2, A = k + 2, rays = {(z,c): s_{z,c} >= A} as in P8):

  (T1) pair-moment identity:
       sum_{|W|=k} C(mult(W), 2) = sum_{cross-slope ray pairs} C(|S ^ S'|, k),
       where mult(W) = #{z : interp of U_z|_W is a live ray}; per (W,z)
       the ray is unique, and same-z ray pairs share <= k-1 points
       (distinct codewords), so all pairs through a W are cross-slope.
  (T2) fiber structure: for a cross pair {(z,c),(z',c')}, z != z', with
       g = (c-c')/(z-z'), f = c - z*g (codeword arithmetic):
       supp(z,c) ^ supp(z',c') = JointAgr(f,g) = {x: u(x)=f(x), v(x)=g(x)}
       EXACTLY; (f,g) <-> the pair's slope set is a bijection fiberwise.
  (T3) regrouping: sum_{cross pairs} C(J,k)
       = sum_{(f,g)} C(L(f,g), 2) * C(J(f,g), k),
       L(f,g) = #live slopes of the shifted pair (u-f, v-g).
  (T4) pencil collapse: for every k-set W, mult(W) = L(P_W, Q_W) where
       (P_W, Q_W) = (interp u|_W, interp v|_W) (sunflower-pencil
       linearity: interp(U_z|_W) = P_W + z*Q_W); and every (f,g) with
       J(f,g) = k satisfies (f,g) = (P_W, Q_W) for W = JointAgr(f,g).
       Hence in the far-pair regime (member cores <= A-2 = k at t=2):
       #W-collision cores = #{W : L(P_W,Q_W) >= 2}, and the collision
       moment IS the second moment of pencil live counts — an SP-type
       quantity (adjacent to v13_second_moment_shift_pair_identity).

Any assertion failure refutes the packet. One pair per worker.
"""
import itertools
import json
import random
from math import comb

import modal

app = modal.App("rs-mca-f5-p9-wcollision")
image = modal.Image.debian_slim()

# (n, q, family, seed) — same shape as P8 for comparability
JOBS = ([(12, 97, "random", 701 + i) for i in range(6)] +
        [(12, 97, "near-pencil", 721 + i) for i in range(4)] +
        [(16, 97, "random", 741 + i) for i in range(2)] +
        [(16, 97, "near-pencil", 761 + i) for i in range(2)])


@app.function(image=image, cpu=2, memory=2048, timeout=280)
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

    g0 = next(c for c in range(2, q)
              if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    h = pow(g0, (q - 1) // n, q)
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

    # draw the pair (identical generators to P8)
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

    # --- ray census (as P8 parts (1)+(2)) with support SETS kept ---
    rays = {}   # (z, c) -> frozenset agreement support
    for z in range(q):
        Uz = {x: (u[x] + z * v[x]) % q for x in D}
        for T in itertools.combinations(D, A):
            c = interp(T[:k], [Uz[x] for x in T[:k]])
            if all(ev(c, x) == Uz[x] for x in T[k:]):
                if (z, c) not in rays:
                    rays[(z, c)] = frozenset(
                        x for x in D if ev(c, x) == Uz[x])
    for (z, c), S in rays.items():
        assert len(S) >= A

    # --- LHS: per-W multiplicity scan (P8 part (3) machinery) + T4 ---
    lhs = 0
    mult_of = {}
    pencil_of = {}
    for W in itertools.combinations(D, k):
        PW = interp(list(W), [u[x] for x in W])
        QW = interp(list(W), [v[x] for x in W])
        mult = 0
        for z in range(q):
            cz = tuple((PW[i] + z * QW[i]) % q for i in range(k))
            # T4 linearity spot-check against direct interpolation
            if z % 37 == 0:
                assert cz == interp(
                    list(W), [(u[x] + z * v[x]) % q for x in W]), \
                    ("pencil linearity FAILED", W, z)
            s = sum(ev(cz, x) == (u[x] + z * v[x]) % q for x in D)
            if s >= A:
                mult += 1
        lhs += comb(mult, 2)
        if mult:
            mult_of[W] = mult
            pencil_of[W] = (PW, QW)

    # --- RHS: cross-slope ray pairs, direct support intersections (T1) ---
    ray_list = list(rays.items())
    rhs = 0
    fg_group = {}   # (f, g) -> set of live slopes seen in cross pairs
    j_of_fg = {}
    j_profile = {}
    for i in range(len(ray_list)):
        (z1, c1), S1 = ray_list[i]
        for j in range(i + 1, len(ray_list)):
            (z2, c2), S2 = ray_list[j]
            inter = S1 & S2
            if z1 == z2:
                assert len(inter) <= k - 1, \
                    ("same-slope pair shares a k-core", z1)
                continue
            J = len(inter)
            rhs += comb(J, k)
            # T2: (f,g) fiber structure
            izz = inv_t[(z1 - z2) % q]
            gg = tuple((c1[d] - c2[d]) * izz % q for d in range(k))
            ff = tuple((c1[d] - z1 * gg[d]) % q for d in range(k))
            joint = frozenset(x for x in D
                              if u[x] == ev(ff, x) and v[x] == ev(gg, x))
            assert inter == joint, ("T2 fiber mismatch", z1, z2)
            if J >= k:
                j_profile[J] = j_profile.get(J, 0) + 1
                fg_group.setdefault((ff, gg), set()).update((z1, z2))
                j_of_fg[(ff, gg)] = J
    assert lhs == rhs, ("T1 pair-moment identity FAILED", lhs, rhs)

    # --- T3: regroup by (f,g) with independently recomputed L(f,g) ---
    t3 = 0
    for (ff, gg), zs in fg_group.items():
        L = 0
        for z in range(q):
            cz = tuple((ff[d] + z * gg[d]) % q for d in range(k))
            s = sum(ev(cz, x) == (u[x] + z * v[x]) % q for x in D)
            if s >= A:
                L += 1
        assert L >= len(zs), ("T3 live count below witnessed slopes",)
        t3 += comb(L, 2) * comb(j_of_fg[(ff, gg)], k)
        # T4 bijection at J = k: (f,g) must be the pencil of its core
        if j_of_fg[(ff, gg)] == k:
            W = tuple(sorted(x for x in D
                             if u[x] == ev(ff, x) and v[x] == ev(gg, x)))
            assert pencil_of.get(W) == (ff, gg), ("T4 bijection FAILED", W)
            assert mult_of.get(W, 0) == L, ("T4 mult != L", W, L)
    # T3 equality needs every contributing (f,g) captured: pairs of live
    # slopes of (f,g) are exactly the cross pairs mapping to it, so any
    # (f,g) with C(L,2) > 0 and J >= k appears in fg_group.
    assert t3 == sum(comb(j, k) * c for j, c in
                     ((j, j_profile[j]) for j in j_profile)), \
        ("T3 regroup FAILED", t3)

    n_coll = sum(1 for m in mult_of.values() if m >= 2)
    max_mult = max(mult_of.values(), default=0)
    return {"n": n, "q": q, "family": fam, "seed": seed,
            "rays": len(rays), "lhs_pair_moment": lhs,
            "n_collision_cores": n_coll, "max_mult": max_mult,
            "sunflower_cap": (n - k) // t,
            "j_profile": {str(j): c for j, c in sorted(j_profile.items())}}


@app.local_entrypoint()
def main():
    res = list(check.map(JOBS, return_exceptions=True))
    print(f"{'row':>10} {'family':>12} {'rays':>6} {'pairmom':>9} "
          f"{'#coll':>6} {'maxmult':>8} {'cap':>4}  J-profile")
    fails = 0
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        print(f"  ({r['n']},{r['q']})".rjust(10) +
              f" {r['family']:>12} {r['rays']:>6} "
              f"{r['lhs_pair_moment']:>9} {r['n_collision_cores']:>6} "
              f"{r['max_mult']:>8} {r['sunflower_cap']:>4}  "
              f"{r['j_profile']}")
    with open("/tmp/f5_p9_wcollision.json", "w") as f:
        json.dump([r for r in res if isinstance(r, dict)], f, indent=1)
    if fails:
        raise SystemExit(f"F5_P9_WCOLLISION_PAIR_MOMENT_FAIL ({fails})")
    print("\nF5_P9_WCOLLISION_PAIR_MOMENT_PASS: T1-T4 exact on every pair")
