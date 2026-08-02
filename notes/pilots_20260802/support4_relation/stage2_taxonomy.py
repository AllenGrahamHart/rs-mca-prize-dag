#!/usr/bin/env python3
"""STAGE 2 -- (a) the DECISION PROCEDURE for "does this support pattern admit
a support-4 relation for SOME slopes?", (b) the corollary that the banked K_V
family carries NO relation at any slopes, (c) the gate-failure TAXONOMY of
unconstrained relation-carrying 4-ray systems.

DECISION PROCEDURE (exact, from S4-1 + S4-3 + S4-4).  Let W be the triple
locus (points in >= 3 of the supports) and A_a := C_{S_a ^ W}.  Then
  * if some A_a = 0 there is NO support-4 relation, for ANY slopes (S4-2);
  * otherwise a relation exists for some slopes iff there is a 2-dim
    L <= C^perp with L ^ A_a != 0 for all four a and the four lines distinct;
  * and then the admissible slope 4-tuples are exactly the fibre of the
    cross-ratio map -- codimension 1 in (P^1)^4.
Searching L: fix c_1 in P(A_1) and intersect the images of A_2, A_3, A_4 in
the quotient by <c_1>; a nonzero intersection is exactly a valid L.

Run: tools/ramguard local -- python3 stage2_taxonomy.py
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
import advlib as ADV                                           # noqa: E402

CHECKS, FAIL = [0], []


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                 if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


# ---------------------------------------------------------- linear algebra
def subspace_intersect(X, Y, ncol, q):
    """Basis of span(X) ^ span(Y) (rows are vectors of length ncol)."""
    if not X or not Y:
        return []
    nx = len(X)
    M = [[X[i][c] for c in range(ncol)] for i in range(nx)]
    M += [[(-Y[j][c]) % q for c in range(ncol)] for j in range(len(Y))]
    # kernel of the (nx+ny) x ncol matrix acting on the LEFT
    rows = [[M[j][i] for j in range(len(M))] for i in range(ncol)]
    ker = T.nullspace_mod(rows, len(M), q)
    out = []
    for kv in ker:
        v = [0] * ncol
        for i in range(nx):
            t = kv[i]
            if t:
                for c in range(ncol):
                    if X[i][c]:
                        v[c] = (v[c] + t * X[i][c]) % q
        if any(v):
            out.append(v)
    red, _ = T.rref(out, q)
    return red


def quotient_images(bases, c1, ncol, q):
    """Images of the given subspaces in F^ncol / <c1>."""
    j = next(i for i, x in enumerate(c1) if x)
    ic = S.inv(c1[j], q)
    out = []
    for B in bases:
        im = []
        for b in B:
            f = b[j] * ic % q
            im.append([(b[c] - f * c1[c]) % q for c in range(ncol)])
        red, _ = T.rref(im, q)
        out.append(red)
    return out


def admits_support4(row, supports, cap=4000):
    """Return dict(verdict, reason, L, zetas) -- exact for dim A_1 = 1."""
    n, k, q = row.n, row.k, row.q
    W = S.triple_locus(supports, n)
    A = []
    for Sa in supports:
        Ia = tuple(sorted(W & frozenset(Sa)))
        A.append(T.dual_basis(Ia, row) if len(Ia) > k else [])
    dims = [len(x) for x in A]
    if min(dims) == 0:
        return dict(verdict=False, reason="S4-2: some C_{S_a ^ W} = 0",
                    dims=dims, W=len(W))
    order = sorted(range(len(A)), key=lambda a: dims[a])
    a0 = order[0]
    rest = [a for a in range(len(A)) if a != a0]
    # enumerate P(A_{a0}); exact when dims[a0] == 1
    reps = []
    if dims[a0] == 1:
        reps = [A[a0][0]]
    else:
        # projective points of a dim-2 space: (1:t) and (0:1)
        if dims[a0] == 2 and q + 1 <= cap:
            b0, b1 = A[a0]
            reps = [b1] + [[(b0[i] + t * b1[i]) % q for i in range(n)]
                           for t in range(q)]
        else:
            return dict(verdict=None, reason="search space too large",
                        dims=dims, W=len(W))
    for c1 in reps:
        ims = quotient_images([A[a] for a in rest], c1, n, q)
        cur = ims[0]
        for nxt in ims[1:]:
            cur = subspace_intersect(cur, nxt, n, q)
            if not cur:
                break
        if cur:
            return dict(verdict=True, reason="L found", dims=dims, W=len(W))
    return dict(verdict=False, reason="no common 2-dim L", dims=dims, W=len(W))


def main():
    rnd = random.Random(4488)
    res = {"decision": [], "kv": [], "taxonomy": {}}

    # ============================== E. decision procedure on designed families
    for cs in [dict(k=3, h=5, d=1, V=4, q=6421),
               dict(k=4, h=6, d=1, V=4, q=6421),
               dict(k=3, h=7, d=2, V=4, q=10007)]:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        priv = (h - 1) - (V - 1) * d
        n = (k + 2) + 6 * d + V * priv + 2
        row = T.Row2(n, k, h, q)
        fam = S.build_mobius_family(row, d, V, seed=1)
        ver = admits_support4(row, fam["supports"])
        dim, _, _ = S.relation_space(row, fam["supports"], fam["slopes"])
        chk(f"E1 k={k} h={h} d={d}: decision procedure says the U-pattern "
            f"ADMITS a support-4 relation, and the Mobius slopes realise it",
            ver["verdict"] is True and dim == 1,
            f"dims={ver['dims']} |W|={ver['W']} dim Rel={dim}")
        res["decision"].append(dict(cs=cs, **{kk: str(vv) for kk, vv
                                              in ver.items()}))

    # ================================ F. the banked K_V family carries NO relation
    for cs in [dict(k=3, h=5, d=1, V=4, q=6421),
               dict(k=3, h=7, d=1, V=5, q=6421),
               dict(k=3, h=9, d=1, V=6, q=10007),
               dict(k=3, h=8, d=2, V=4, q=10007),
               dict(k=4, h=7, d=1, V=5, q=6421)]:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        M = V * (V - 1) // 2
        n = max((k - 1) + M * (d + 1), k + h + 2)
        row = T.Row2(n, k, h, q)
        b = ADV.build_KV(row, d, V, seed=0)
        if b is None:
            continue
        _, _, info = b
        sup = [tuple(s) for s in info["supports"].values()]
        zs = list(info["zs"])
        W = S.triple_locus(sup, n)
        ver = admits_support4(row, sup[:4])
        dim, _, _ = S.relation_space(row, sup, zs)
        chk(f"F1 K_V k={k} h={h} d={d} V={V}: triple locus = Y has {len(W)} "
            f"= k-1 < k+1 points, so C_{{S_a^W}} = 0 and NO relation exists "
            f"for ANY slopes (S4-2)",
            len(W) == k - 1 and ver["verdict"] is False and dim == 0,
            f"|W|={len(W)} verdict={ver['verdict']} "
            f"reason={ver['reason']} dim Rel={dim}")
        res["kv"].append(dict(cs=cs, W=len(W), verdict=str(ver["verdict"]),
                              reason=ver["reason"], dim_rel=dim))

    # ================================================ G. gate-failure taxonomy
    for cfg in [dict(n=24, k=3, h=5, q=6421, N=600),
                dict(n=30, k=3, h=7, q=6421, N=600),
                dict(n=26, k=3, h=6, q=6421, N=600)]:
        n_, k_, h_, q_, N = cfg["n"], cfg["k"], cfg["h"], cfg["q"], cfg["N"]
        row = T.Row2(n_, k_, h_, q_)
        A = k_ + h_
        tal = dict(total=N, with_relation=0, genuine_s4=0,
                   fail_kpacking=0, fail_pairwise_intersecting=0,
                   fail_depth=0, fail_none=0, gate_clean=0)
        for _ in range(N):
            sup = [tuple(sorted(rnd.sample(range(n_), A))) for _ in range(4)]
            zs = rnd.sample(range(1, q_), 4)
            dim, _, _ = S.relation_space(row, sup, zs)
            if dim == 0:
                continue
            tal["with_relation"] += 1
            # genuine support-4 part = dim Rel - dim(sum of triple relations)
            sub = 0
            for tri in itertools.combinations(range(4), 3):
                sub += S.relation_space(row, [sup[a] for a in tri],
                                        [zs[a] for a in tri])[0]
            if dim > sub:
                tal["genuine_s4"] += 1
            cg = S.combinatorial_gates(row, sup)
            broke = False
            if not cg["kpacking_ok"]:
                tal["fail_kpacking"] += 1
                broke = True
            if not cg["pairwise_intersecting"]:
                tal["fail_pairwise_intersecting"] += 1
                broke = True
            if not cg["depth_ok"]:
                tal["fail_depth"] += 1
                broke = True
            if not broke:
                tal["gate_clean"] += 1
        key = f"n{n_}_k{k_}_h{h_}"
        res["taxonomy"][key] = tal
        chk(f"G1 {key}: EVERY unconstrained relation-carrying 4-ray system "
            f"breaks a support gate ({tal['with_relation']} found, "
            f"{tal['gate_clean']} gate-clean)",
            tal["gate_clean"] == 0,
            f"rel={tal['with_relation']}/{N} kpack_break={tal['fail_kpacking']} "
            f"not_pairwise_intersecting={tal['fail_pairwise_intersecting']} "
            f"depth_break={tal['fail_depth']} genuine_s4={tal['genuine_s4']}")
        chk(f"G2 {key}: the dominant failure is k-packing (triple "
            f"intersection >= k+1)",
            tal["fail_kpacking"] == tal["with_relation"],
            f"{tal['fail_kpacking']}/{tal['with_relation']}")

    # ================== H. gate-clean random supports + random slopes: none
    for cfg in [dict(k=3, h=5, d=1, q=6421, N=400),
                dict(k=4, h=6, d=1, q=6421, N=300)]:
        k_, h_, d_, q_, N = cfg["k"], cfg["h"], cfg["d"], cfg["q"], cfg["N"]
        priv = (h_ - 1) - 3 * d_
        n_ = (k_ + 2) + 6 * d_ + 4 * priv + 2
        row = T.Row2(n_, k_, h_, q_)
        fam = S.build_mobius_family(row, d_, 4, seed=1)
        sup = fam["supports"]
        hits = 0
        for _ in range(N):
            zs = rnd.sample(range(1, q_), 4)
            if S.relation_space(row, sup, zs)[0] > 0:
                hits += 1
        chk(f"H1 k={k_} h={h_}: on the SAME relation-admitting support "
            f"pattern, random slopes give a relation {hits}/{N} times "
            f"(codimension 1: expected {N/q_:.3f})", hits <= 1,
            f"hits={hits}")

    with open(os.path.join(HERE, "stage2_taxonomy.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()
