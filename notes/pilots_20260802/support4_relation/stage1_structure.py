#!/usr/bin/env python3
"""STAGE 1 -- the support-4 STRUCTURE THEOREMS, verified exactly.

Checks S4-1 (localization), S4-2 (general position kills), S4-3 (rank-2
rigidity), S4-4 (Mobius/cross-ratio criterion), S4-5 (|U| >= k+2), S4-6
(minimal case zeta_y = x_y), plus the combinatorial bookkeeping bounds and
the codimension-1 slope statement.

Run: tools/ramguard local -- python3 stage1_structure.py
"""
from __future__ import annotations

import itertools
import json
import os
import random
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import s4lib as S                                              # noqa: E402
import tslib as T                                              # noqa: E402

CHECKS, FAIL = [0], []


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                 if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


def rel_support(cs):
    return tuple(a for a, c in enumerate(cs) if any(c))


def generic_element(rels, q, rnd):
    if not rels:
        return None
    V, n = len(rels[0]), len(rels[0][0])
    out = [[0] * n for _ in range(V)]
    for r in rels:
        t = rnd.randrange(q)
        if not t:
            continue
        for a in range(V):
            ra = r[a]
            for i in range(n):
                if ra[i]:
                    out[a][i] = (out[a][i] + t * ra[i]) % q
    return out


def span_dim(vs, q):
    return T.rank_mod([list(v) for v in vs], q)


def main():
    res = {"designed": [], "random": {}, "perturb": []}
    rnd = random.Random(20260802)

    # ================================================== A. designed families
    CASES = [dict(k=3, h=5, d=1, V=4, q=6421),
             dict(k=4, h=6, d=1, V=4, q=6421),
             dict(k=3, h=7, d=2, V=4, q=10007),
             dict(k=5, h=6, d=1, V=4, q=10007),
             dict(k=3, h=6, d=1, V=5, q=6421),
             dict(k=4, h=7, d=1, V=6, q=10007),
             dict(k=3, h=8, d=1, V=4, q=10007)]
    for cs in CASES:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        priv = (h - 1) - (V - 1) * d
        n = (k + 2) + (V * (V - 1) // 2) * d + V * priv + 2
        row = T.Row2(n, k, h, q)
        fam = S.build_mobius_family(row, d, V, seed=1)
        tag = f"k={k} h={h} d={d} V={V} n={n}"
        if fam is None:
            chk(f"A0 {tag}: family builds", False)
            continue
        sup, zs = fam["supports"], fam["slopes"]
        cg = S.combinatorial_gates(row, sup)
        chk(f"A1 {tag}: support pattern -- |S_a|=k+h, all pairs = k+d, all "
            f"triples = k-1 (k-packing TIGHT)",
            cg["size_ok"] and set(cg["pair"].values()) == {k + d}
            and set(cg["triple"].values()) == {k - 1},
            f"pairs={sorted(set(cg['pair'].values()))} "
            f"triples={sorted(set(cg['triple'].values()))}")
        chk(f"A2 {tag}: pairwise-intersecting + band depth d in [1,h-2]",
            cg["pairwise_intersecting"] and cg["depth_ok"] and cg["kpacking_ok"])

        dim, rels, blocks = S.relation_space(row, sup, zs)
        rank = S.family_rank(row, sup, zs)
        chk(f"A3 {tag}: dim Rel = V-3 = {V-3}", dim == V - 3, f"dim={dim}")
        chk(f"A4 {tag}: rank = Vh - (V-3) = {V*h-(V-3)}",
            rank == V * h - (V - 3), f"rank={rank} Vh={V*h}")

        g = generic_element(rels, q, rnd)
        chk(f"A5 {tag}: the generic relation has FULL support (all V "
            f"components nonzero)", g is not None and len(rel_support(g)) == V,
            f"supp={rel_support(g) if g else None}")

        # S4-1 localization
        trip = S.triple_locus(sup, n)
        ok1 = all(S.support_of(g[a]) <= (trip & frozenset(sup[a]))
                  for a in range(V))
        chk(f"A6 {tag}: S4-1 supp(c_a) inside (triple locus) ^ S_a", ok1,
            f"|triple locus|={len(trip)}")

        # S4-3 rank-2 rigidity (V = 4 only; for V > 4 all c_a still in one L)
        L = span_dim(g, q)
        chk(f"A7 {tag}: S4-3 all c_a lie in ONE 2-dim L", L == 2, f"dim L={L}")
        prop = []
        for a in range(V):
            for b in range(a + 1, V):
                if span_dim([g[a], g[b]], q) < 2:
                    prop.append((a, b))
        chk(f"A8 {tag}: no two c_a proportional (else k-packing breaks)",
            not prop, f"proportional pairs={prop}")

        # S4-5/S4-6 the pencil picture
        Uset = frozenset().union(*[S.support_of(c) for c in g])
        chk(f"A9 {tag}: S4-5 |U| >= k+2 and U inside the triple locus",
            len(Uset) >= k + 2 and Uset <= trip,
            f"|U|={len(Uset)} k+2={k+2}")
        chk(f"A10 {tag}: S4-6 minimal case |U| = k+2 and weight(c_a) = k+1 "
            f"exactly", len(Uset) == k + 2
            and all(len(S.support_of(c)) == k + 1 for c in g),
            f"|U|={len(Uset)} wts={[len(S.support_of(c)) for c in g]}")
        # zeta_a = x_{y_a}: c_a vanishes on U exactly at y_a
        holes = [sorted(Uset - S.support_of(g[a])) for a in range(V)]
        chk(f"A11 {tag}: c_a vanishes on U exactly at y_a (zeta_a = x_{{y_a}})",
            all(holes[a] == [fam["ys"][a]] for a in range(V)),
            f"holes={holes} ys={fam['ys']}")

        # S4-4 cross-ratio, on every 4-subset
        bad_cr = []
        for quad in itertools.combinations(range(V), 4):
            zq = [zs[a] for a in quad]
            wq = [row.xs[fam["ys"][a]] for a in quad]
            crz = S.cross_ratio(*zq, q)
            crw = S.cross_ratio(*wq, q)
            dt = S.det_mod(S.segre_matrix(zq, wq, q), q)
            if crz != crw or dt != 0:
                bad_cr.append((quad, crz, crw, dt))
        chk(f"A12 {tag}: S4-4 CR(z) = CR(x_y) and det(Segre) = 0 on all "
            f"{len(list(itertools.combinations(range(V),4)))} 4-subsets",
            not bad_cr, f"bad={bad_cr[:2]}")

        # support <= 3 is zero
        s3 = max((S.relation_space(row, [sup[a] for a in idx],
                                   [zs[a] for a in idx])[0]
                  for idx in itertools.combinations(range(V), 3)), default=0)
        s2 = max((S.relation_space(row, [sup[a] for a in idx],
                                   [zs[a] for a in idx])[0]
                  for idx in itertools.combinations(range(V), 2)), default=0)
        chk(f"A13 {tag}: support <= 3 relations are ZERO (banked lemmas "
            f"re-verified)", s3 == 0 and s2 == 0, f"s2={s2} s3={s3}")

        # counting bookkeeping:  |U| + |Q| <= 2(k+d),  |Q|+|D_a| <= |T|
        m = S.multiplicity(sup, n)
        Q = frozenset(i for i in Uset if m[i] == V)
        Ds = [Uset - frozenset(sup[a]) for a in range(V)]
        chk(f"A14 {tag}: bookkeeping |U| = |Q| + sum|D_a|, |Q|+|D_a| <= k-1, "
            f"|U|+|Q| <= 2(k+d)",
            len(Uset) == len(Q) + sum(len(x) for x in Ds)
            and all(len(Q) + len(x) <= k - 1 for x in Ds)
            and len(Uset) + len(Q) <= 2 * (k + d),
            f"|U|={len(Uset)} |Q|={len(Q)} |D|={[len(x) for x in Ds]}")

        res["designed"].append(dict(cs=cs, n=n, dim_rel=dim, rank=rank,
                                    Vh=V * h, U=len(Uset), Q=len(Q),
                                    pairs=sorted(set(cg["pair"].values())),
                                    triples=sorted(set(cg["triple"].values())),
                                    charge_per_ray=rank / V,
                                    charge_per_datum=rank / (V * (V - 1) / 2)))

    # ============================================ B. slope perturbation test
    k, h, d, V, q = 3, 5, 1, 4, 6421
    n = (k + 2) + 6 * d + V * ((h - 1) - 3 * d) + 2
    row = T.Row2(n, k, h, q)
    fam = S.build_mobius_family(row, d, V, seed=1)
    sup, zs = fam["supports"], fam["slopes"]
    hits = 0
    trials = 300
    for _ in range(trials):
        z4 = rnd.randrange(1, q)
        if z4 in zs[:3]:
            continue
        dim, _, _ = S.relation_space(row, sup, zs[:3] + [z4])
        if dim > 0:
            hits += 1
            res["perturb"].append(z4)
    chk(f"B1 k={k} h={h}: moving z_4 off the Mobius value kills the relation "
        f"in {trials-hits}/{trials} random slopes (codimension 1)",
        hits <= 1, f"hits={hits} (expected ~{trials/q:.3f} by chance)")
    dim0, _, _ = S.relation_space(row, sup, zs)
    chk("B2 same supports, the Mobius slope: relation present",
        dim0 == 1, f"dim={dim0}")

    # ============================================= C. unconstrained randoms
    for cfg in [dict(n=24, k=3, h=5, q=6421, N=400),
                dict(n=30, k=3, h=7, q=6421, N=400),
                dict(n=28, k=4, h=6, q=10007, N=300)]:
        n_, k_, h_, q_, N = cfg["n"], cfg["k"], cfg["h"], cfg["q"], cfg["N"]
        row = T.Row2(n_, k_, h_, q_)
        A = k_ + h_
        tally = dict(total=N, with_relation=0, support2=0, support3=0,
                     support4=0, kpack_break=0, quad_break=0)
        s4_examples = []
        for _ in range(N):
            sup = [tuple(sorted(rnd.sample(range(n_), A))) for _ in range(4)]
            zs = rnd.sample(range(1, q_), 4)
            dim, rels, _ = S.relation_space(row, sup, zs)
            if dim == 0:
                continue
            tally["with_relation"] += 1
            g = generic_element(rels, q_, rnd)
            sp = rel_support(g)
            cg = S.combinatorial_gates(row, sup)
            if len(sp) == 4:
                tally["support4"] += 1
                s4_examples.append(dict(pairs=sorted(cg["pair"].values()),
                                        triples=sorted(cg["triple"].values())))
            elif len(sp) == 3:
                tally["support3"] += 1
            else:
                tally["support2"] += 1
            if not cg["kpacking_ok"]:
                tally["kpack_break"] += 1
            quad = len(set(sup[0]) & set(sup[1]) & set(sup[2]) & set(sup[3]))
            if quad >= k_ + 1:
                tally["quad_break"] += 1
        key = f"n{n_}_k{k_}_h{h_}"
        tally["support4_examples"] = s4_examples[:5]
        res["random"][key] = tally
        chk(f"C1 {key}: every unconstrained relation found breaks k-packing "
            f"on the SUPPORTS ({tally['kpack_break']}/{tally['with_relation']})",
            tally["kpack_break"] == tally["with_relation"],
            f"rel={tally['with_relation']}/{N} "
            f"supp2/3/4={tally['support2']}/{tally['support3']}/"
            f"{tally['support4']}")
        chk(f"C2 {key}: unconstrained support-4 relations are non-generic "
            f"(codim 1 in the slopes)", tally["support4"] <= 2,
            f"support4={tally['support4']}")

    with open(os.path.join(HERE, "stage1_structure.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()
