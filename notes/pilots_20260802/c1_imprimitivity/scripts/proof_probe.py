#!/usr/bin/env python3
"""Numerical adjudication of the three proof angles (a) flatness/majorization,
(b) autocorrelation / even-part domination, (c) local moves.

Also verifies two new exact identities used in the report:
  LEMMA C   Norm_N(f) <= Norm_M(p p* + q q*)   (M = N/2, f = p(x^2)+x q(x^2))
  ROTATION  prod_{c=0}^{M-1} Norm_N(p(x^2)+x^{2c+1}q(x^2)) = Norm_M(p^{2M}+q^{2M})
"""
from __future__ import annotations
import json, os, sys, random
from itertools import product as iproduct
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_norm_ladder/scripts")
from norm_core import norm_descent_py, norm_bareiss
from affine import affine_reps, masks_to_positions, sign_patterns, build_block

# ---------- exact ring arithmetic in R_M = Z[y]/(y^M+1) (python ints) ----------
def rmul(a, b):
    M = len(a); out = [0]*M
    for i, ai in enumerate(a):
        if not ai: continue
        for j, bj in enumerate(b):
            if not bj: continue
            k = i + j
            if k < M: out[k] += ai*bj
            else: out[k-M] -= ai*bj
    return out

def rstar(a):
    """a(y^-1) mod y^M+1 : y^-k = -y^(M-k)."""
    M = len(a); out = [0]*M; out[0] = a[0]
    for k in range(1, M): out[M-k] = -a[k]
    return out

def rpow(a, e):
    M = len(a); r = [0]*M; r[0] = 1; b = a[:]
    while e:
        if e & 1: r = rmul(r, b)
        b = rmul(b, b); e >>= 1
    return r

def radd(a, b): return [x+y for x, y in zip(a, b)]

def split_eo(d):
    return list(d[0::2]), list(d[1::2])

def spectrum(d):
    """|f(zeta^j)|^2 for the N odd residues j mod 2N (float)."""
    N = len(d); j = np.arange(1, 2*N, 2)
    E = np.exp(2j*np.pi*np.outer(j, np.arange(N))/(2*N))
    v = E @ np.asarray(d, dtype=float)
    return np.abs(v)**2

def main():
    rng = random.Random(20260802)
    out = {}

    # ---------------- LEMMA C: exhaustive at N = 8, sampled at N = 16 ---------
    bad = 0; tight = 0; tot = 0
    for d in iproduct((-1, 0, 1), repeat=8):
        if not any(d): continue
        p, q = split_eo(d)
        lhs = norm_descent_py(list(d))
        rhs = norm_descent_py(radd(rmul(p, rstar(p)), rmul(q, rstar(q))))
        tot += 1
        if lhs > rhs: bad += 1
        if lhs == rhs: tight += 1
    out["lemmaC_exhaustive_N8"] = {"tested": tot, "violations": bad, "equalities": tight}

    bad16 = 0
    for _ in range(3000):
        d = [0]*16
        w = rng.randint(1, 16)
        for i in rng.sample(range(16), w): d[i] = rng.choice((-1, 1))
        p, q = split_eo(d)
        if norm_descent_py(d) > norm_descent_py(radd(rmul(p, rstar(p)), rmul(q, rstar(q)))):
            bad16 += 1
    out["lemmaC_random_N16"] = {"tested": 3000, "violations": bad16}

    # LEMMA C is INSUFFICIENT: explicit p,q at M=8 with Norm_M(pp*+qq*) = 4^8
    M = 8; a = 1
    p = [0]*M; p[0] = 1; p[a] = 1
    q = [0]*M; q[0] = 1; q[M-a] = 1
    B = radd(rmul(p, rstar(p)), rmul(q, rstar(q)))
    out["lemmaC_insufficiency_witness"] = {
        "M": M, "p": p, "q": q, "pp*+qq*": B,
        "Norm_M(pp*+qq*)": str(norm_descent_py(B)),
        "amgm_ceiling_w^M (w=4)": str(4**M),
        "maxnorm(M=8,w=4)^2": str(196**2),
        "bound_exceeds_target": norm_descent_py(B) > 196**2,
    }

    # ---------------- ROTATION identity ---------------------------------------
    rot = {"tested": 0, "violations": 0, "examples": []}
    for M in (4, 8):
        N = 2*M
        for _ in range(60):
            p = [rng.choice((-1, 0, 1)) for _ in range(M)]
            q = [rng.choice((-1, 0, 1)) for _ in range(M)]
            lhs = 1
            for c in range(M):
                d = [0]*N
                for k in range(M): d[2*k] = p[k]
                # x^(2c+1) q(x^2): monomial y^c times x times q(y)
                yc = [0]*M; yc[c % M] = 1 if c < M else -1
                qq = rmul(q, yc)
                for k in range(M): d[2*k+1] = qq[k]
                if not any(d): lhs = None; break
                lhs *= norm_descent_py(d)
            if lhs is None: continue
            rhs = norm_descent_py(radd(rpow(p, 2*M), rpow(q, 2*M)))
            rot["tested"] += 1
            if lhs != rhs:
                rot["violations"] += 1
                if len(rot["examples"]) < 3:
                    rot["examples"].append({"M": M, "p": p, "q": q, "lhs": str(lhs), "rhs": str(rhs)})
    out["rotation_identity"] = rot

    # ---------------- MAJORIZATION (attack a) ---------------------------------
    maj = {}
    for N, imp_max in ((8, {2: 16, 3: 81}), (16, {2: 256, 3: 6561, 4: 38416, 5: 279841,
                                                 6: 1331716, 7: 5764801})):
        M = N//2
        for w, _ in imp_max.items():
            # imprimitive optimum profile
            reps = affine_reps(N, w); pos = masks_to_positions(reps, N, w)
            S = sign_patterns(w-1); flat = build_block(pos, S, N)
            best = None; bestv = -1
            for r in flat:
                if len(set(int(i) % 2 for i in np.nonzero(r)[0])) != 1: continue
                v = norm_descent_py([int(z) for z in r])
                if v > bestv: bestv, best = v, [int(z) for z in r]
            Xopt = np.sort(spectrum(best))[::-1]
            copt = np.cumsum(Xopt)
            nfail = 0; worst = None
            for r in flat:
                X = np.sort(spectrum([int(z) for z in r]))[::-1]
                c = np.cumsum(X)
                if np.any(c < copt - 1e-8):
                    nfail += 1
                    if worst is None: worst = [int(z) for z in r]
            maj["N%d_w%d" % (N, w)] = {
                "imprimitive_optimum": best, "imprimitive_max": str(bestv),
                "n_ternary_tested": int(flat.shape[0]),
                "n_NOT_majorizing_the_optimum": nfail,
                "majorization_argument_viable": nfail == 0,
                "first_counterexample": worst,
                "counterexample_norm": (str(norm_descent_py(worst)) if worst else None)}
    out["majorization"] = maj

    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
