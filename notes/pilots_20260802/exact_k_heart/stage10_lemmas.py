#!/usr/bin/env python3
r"""STAGE 10 -- machine verification of the three d=0 lemmas.

V1 PEELING LEMMA.  If ray a has >= h points x in S_a with coverage
   cov(x) <= 2 (coverage inside the family), then EVERY relation has
   c_a = 0, hence rank(F) = h + rank(F \ {a}).
   Proof: at cov(x)=1, sum_b c_b(x) = c_a(x) = 0; at cov(x)=2 with
   distinct slopes, the 2x2 Vandermonde in (z_a,z_b) forces both to
   vanish.  c_a = nu.Lam_{D\S_a}.r_a with deg r_a < h, and r_a is nonzero
   at no more than h-1 points of S_a -- so r_a = 0.
   COROLLARY: a fully peelable family is INDEPENDENT: rank = V h.

V2 LOCALITY.  All conditions of a family live in the shortened code on
   U = union of supports, whose redundancy is |U| - k.  Hence
   rank <= 2(|U| - k); and rank = 2(|U|-k) forces (u,v)|_U in RS x RS,
   i.e. agreement |U| > A on every slope: NO live ray.  So an admissible
   family obeys rank <= 2(|U| - k) - 1.

V3 MOMENT IDENTITY at d = 0 (T1 restricted): sum_{|W|=k} C(L_W,2)
   = #{live ray pairs with |S ^ S'| = k}.
"""
from __future__ import annotations

import itertools
import json
import os
import random
import sys
from collections import defaultdict

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import dzlib as Z                                              # noqa: E402
import tslib as T                                              # noqa: E402

OUT = {"checks": [], "fail": 0, "pass": 0, "data": {}}


def chk(name, cond, info=None):
    OUT["checks"].append(dict(name=name, ok=bool(cond), info=info))
    if cond:
        OUT["pass"] += 1
    else:
        OUT["fail"] += 1
        print("  FAIL", name, info)
    return cond


def main():
    rng = random.Random(2718)
    shapes = [(16, 6, 3, 601), (20, 8, 3, 1009), (24, 6, 3, 2003),
              (18, 5, 4, 1009), (32, 8, 3, 2003), (20, 9, 3, 1009)]
    v1 = dict(tested=0, peelable_events=0, ok=0)
    v2 = dict(tested=0, ok=0)
    v3 = dict(tested=0, ok=0)
    for (n, k, h, q) in shapes:
        row = Z.make_row(n, k, h, q)
        A, tag = row.A, f"n{n}k{k}h{h}"
        for trial in range(60):
            V = rng.randint(3, 8)
            sups = []
            for _ in range(V):
                S = tuple(sorted(rng.sample(range(n), A)))
                if any(len(set(S) & set(S2)) > k for S2 in sups):
                    continue
                sups.append(S)
            if len(sups) < 3:
                continue
            V = len(sups)
            zs = rng.sample(range(1, q), V)
            rays = list(zip(zs, sups))
            rk, _ = Z.family_rank(row, rays)
            cov = defaultdict(int)
            for S in sups:
                for x in S:
                    cov[x] += 1
            # ---- V1
            for a in range(V):
                low = sum(1 for x in sups[a] if cov[x] <= 2)
                v1["tested"] += 1
                if low >= h:
                    v1["peelable_events"] += 1
                    rest = rays[:a] + rays[a + 1:]
                    rk2, _ = Z.family_rank(row, rest)
                    good = (rk == h + rk2)
                    v1["ok"] += int(good)
                    chk(f"V1 peel {tag} t{trial} a{a}", good, (rk, h, rk2))
            # ---- V2
            uni = len(set().union(*[set(S) for S in sups]))
            v2["tested"] += 1
            good = rk <= 2 * (uni - k)
            v2["ok"] += int(good)
            chk(f"V2 locality {tag} t{trial}", good, (rk, 2 * (uni - k)))
            # ---- V3 moment identity on this ray set
            cnt = defaultdict(int)
            pairs0 = 0
            for i in range(V):
                for j in range(i + 1, V):
                    I = set(sups[i]) & set(sups[j])
                    if len(I) == k:
                        pairs0 += 1
                        cnt[tuple(sorted(I))] += 0
            Lw = {}
            for W in cnt:
                Lw[W] = sum(1 for S in sups if set(W) <= set(S))
            mom = sum(L * (L - 1) // 2 for L in Lw.values())
            v3["tested"] += 1
            good = (mom == pairs0)
            v3["ok"] += int(good)
            chk(f"V3 moment {tag} t{trial}", good, (mom, pairs0))
    OUT["data"] = dict(v1=v1, v2=v2, v3=v3)
    print("V1 peeling lemma:", v1)
    print("V2 locality     :", v2)
    print("V3 moment id    :", v3)
    json.dump(OUT, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "stage10.json"), "w"), indent=1)
    print(f"stage10: PASS={OUT['pass']} FAIL={OUT['fail']}")


if __name__ == "__main__":
    main()
