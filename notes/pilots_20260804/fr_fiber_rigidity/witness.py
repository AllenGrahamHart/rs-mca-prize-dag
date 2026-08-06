#!/usr/bin/env python3
"""fr_fiber_rigidity -- verifier 4: the (FR) COUNTEREXAMPLE, fully audited.

Re-derives ONE explicit realised admissible pair whose selected block
splits a phi-fiber by 2 points, and checks EVERY clause of the lane's
admissibility stack against it from scratch -- including the identity of
the primitive Pade pair (P,Q) and hence of ell, which is what makes the
witness sit at the tuple-incidence boundary rather than somewhere else.

Also measures |Bset| across the whole family for the FIXED received pair,
which is the quantity the (WTB) ledger actually consumes.

Run: tools/ramguard local -- python3 \
       notes/pilots_20260804/fr_fiber_rigidity/witness.py
"""

import itertools
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from toy import Shape, build, classify, inv, rank_mod  # noqa
from gate import build_words, lagrange_tables, max_codeword_agreement  # noqa

CHECKS = []


def chk(cond, name, info=""):
    CHECKS.append({"name": name, "ok": bool(cond), "info": str(info)})


def kernel_basis(cfg, shape, B1, B2):
    """Full left kernel {(S_1,S_2): deg<d, S_1 E + S_2 E' = 0 on H}."""
    q, d = shape.q, shape.d
    rows = []
    ncols = 2 * d

    def powers(x):
        out, v = [], 1
        for _ in range(d):
            out.append(v)
            v = (v * x) % q
        return out

    for B, (al, be) in ((B1, cfg["lam1"]), (B2, cfg["lam2"])):
        for x in B:
            pw = powers(x)
            rows.append([(be * c) % q for c in pw]
                        + [(-al * c) % q for c in pw])
    for x in cfg["Out"]:
        pw = powers(x)
        rows.append([c % q for c in pw]
                    + [(-pow(x, 3, q) * c) % q for c in pw])

    # nullspace by reduced row echelon
    M = [r[:] for r in rows]
    piv_cols, rk = [], 0
    for col in range(ncols):
        sel = None
        for i in range(rk, len(M)):
            if M[i][col] % q:
                sel = i
                break
        if sel is None:
            continue
        M[rk], M[sel] = M[sel], M[rk]
        iv = inv(M[rk][col] % q, q)
        M[rk] = [(v * iv) % q for v in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][col] % q:
                f = M[i][col] % q
                M[i] = [(M[i][j] - f * M[rk][j]) % q for j in range(ncols)]
        piv_cols.append(col)
        rk += 1
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        vec = [0] * ncols
        vec[fc] = 1
        for i, pc in enumerate(piv_cols):
            vec[pc] = (-M[i][fc]) % q
        basis.append(vec)
    return basis, rk


def polytrim(a, q):
    a = [c % q for c in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def main():
    shape = Shape(h=25, k=4, q=229)
    q = shape.q
    cfg = build(shape)
    H, D, Core, Out = cfg["H"], cfg["D"], cfg["Core"], cfg["Out"]
    fod = cfg["fibers_of_D"]
    rng = random.Random(20260806)

    # ---- pick THE witness: a partition splitting a 3-fiber 2|1
    witness = None
    for B1t in itertools.combinations(D, shape.r):
        B1 = list(B1t)
        if B1[0] != D[0]:
            continue
        B2 = [x for x in D if x not in set(B1)]
        prof1 = [len(set(F) & set(B1)) for F in fod]
        if classify(B1, fod) == "strong" and 2 in prof1:
            witness = (B1, B2, prof1, [len(set(F) & set(B2)) for F in fod])
            break
    B1, B2, prof1, prof2 = witness

    # ---------------- shape is the tuple-incidence boundary
    chk(shape.ell == (shape.h - 4) // 7, "boundary-ell")
    chk(shape.r == 2 * shape.ell + 1, "boundary-r")
    chk(shape.d == shape.h - shape.r, "boundary-d")
    chk(shape.sigma == shape.h - 7 * shape.ell - 4 == 0, "boundary-sigma")
    chk(shape.ell > shape.sigma + 2, "load-bearing ell>sigma+2 HOLDS",
        f"ell={shape.ell} sigma+2={shape.sigma+2}")
    chk(max(len(F) for F in fod) <= shape.ell, "fibers<=ell")
    chk(len(fod[-1]) == shape.t < shape.ell,
        "tail fiber strictly below ell (exception NOT invoked)")

    # ---------------- the witness really splits a fiber by >= 2
    chk(any(2 <= m < len(F) for m, F in zip(prof1, fod)),
        "WITNESS splits a phi-fiber by >=2 points", f"profile B1={prof1}")

    # ---------------- explicit received words
    E, Ep = build_words(cfg, shape, B1, B2, rng)
    u = {x: E[x] for x in H}
    v = {x: Ep[x] for x in H}

    # (AD1) rho and D
    rho = {x: (pow(x, 3, q) * u[x] + v[x]) % q for x in H}
    chk(sorted(x for x in H if rho[x]) == sorted(D), "AD1 D = supp(rho)")
    chk(len(D) == shape.e, "e = 2r", f"e={len(D)}")

    # maximality: full joint core is exactly H\T of size k+d
    core = sorted(x for x in H if u[x] == 0 and v[x] == 0)
    chk(core == sorted(Core), "maximality: joint core exact")
    chk(len(core) == shape.k + shape.d, "core size = k+d")

    # (AD6) blocks
    def block(nu):
        al, be = nu
        return sorted(x for x in D if (al * u[x] + be * v[x]) % q == 0)
    chk(block(cfg["lam1"]) == sorted(B1), "AD6 B_lambda1")
    chk(block(cfg["lam2"]) == sorted(B2), "AD6 B_lambda2")
    chk(len(B1) == len(B2) == shape.r, "AD6 |B| = h-d")
    chk(not (set(B1) & set(B2)), "AD6 blocks disjoint")
    chk(len(set(D) - set(B1) - set(B2)) <= shape.sigma, "TKS2 leftover<=sigma")

    # LEMMA A: block avoids its own slope's phi-fiber
    for nu, B in ((cfg["lam1"], B1), (cfg["lam2"], B2)):
        al, be = nu
        fib = [x for x in H if (be * pow(x, 3, q) - al) % q == 0]
        chk(not (set(B) & set(fib)), "LEMMA A block avoids own fiber")
        chk(not (set(fib) & set(Out)), "AD5 z_lambda = 0")

    # (FSP3) v>=3 distinct phi values per block at r>2ell
    chk(shape.r > 2 * shape.ell, "r > 2ell")
    for B in (B1, B2):
        chk(len({pow(x, 3, q) for x in B}) >= 3, "FSP v>=3")

    # liveness: exactly two live slopes, at exact A, max over all P^1
    agr = {}
    for nu in cfg["slopes"]:
        al, be = nu
        agr[nu] = sum(1 for x in H if (al * u[x] + be * v[x]) % q == 0)
    mx = max(agr.values())
    live = sorted(nu for nu, a in agr.items() if a == mx)
    chk(mx == shape.A, "liveness max = A", f"{mx} vs {shape.A}")
    chk(live == sorted([cfg["lam1"], cfg["lam2"]]), "exactly two live slopes")

    # deficiency: dim K_d = sigma+1 = 1 and the generator IS (Z_D P, Z_D Q)
    basis, rk = kernel_basis(cfg, shape, B1, B2)
    chk(len(basis) == shape.c == 1, "dim K_d = sigma+1 = 1", len(basis))
    chk(rk < 2 * shape.d, "rank J_d < 2d")
    S1 = polytrim(basis[0][:shape.d], q)
    S2 = polytrim(basis[0][shape.d:], q)
    # Z_D
    ZD = [1]
    for x in D:
        ZD = polytrim([0] + ZD, q)[:] if False else polytrim(
            [(-x * c) % q for c in ZD] + [0], q)
        ZD = polytrim([(ZD[i] + ([0] * 1 + [0])[0]) for i in range(len(ZD))],
                      q) if False else ZD
    # rebuild Z_D cleanly
    ZD = [1]
    for x in D:
        new = [0] * (len(ZD) + 1)
        for i, c in enumerate(ZD):
            new[i + 1] = (new[i + 1] + c) % q
            new[i] = (new[i] - x * c) % q
        ZD = polytrim(new, q)
    chk(len(ZD) - 1 == len(D), "deg Z_D = e")
    # expected generator: (Z_D * X^3, Z_D * 1)
    expected1 = polytrim([0, 0, 0] + ZD, q)
    expected2 = ZD
    scale = None
    for i, c in enumerate(expected2):
        if c:
            scale = (S2[i] * inv(c, q)) % q if i < len(S2) else 0
            break
    chk(scale not in (None, 0), "kernel generator has nonzero Q-part")
    chk(S2 == polytrim([(scale * c) % q for c in expected2], q)
        and S1 == polytrim([(scale * c) % q for c in expected1], q),
        "PRIMITIVE PAIR IS (P,Q)=(X^3,1), ell=3",
        f"S1deg={len(S1)-1} S2deg={len(S2)-1}")

    # G_d = common root set of all syzygies = D here; the (PP2)/(TKS)/(ABN)
    # chain must be exactly tight
    g = len(D)
    chk(2 * shape.r <= shape.e <= g <= 2 * shape.r + shape.sigma, "TKS1")
    chk(shape.ell + g <= shape.d - 1, "PP2 ell+g<=d-1", f"{shape.ell+g}")
    chk(shape.c <= shape.d - shape.ell - g, "ABN1 c<=d-ell-g")
    chk(shape.e <= shape.d - shape.ell - 1, "AD2 e<=d-ell-1")

    # ---------------- TANGENT GATE, exhaustive over all slopes
    T = [x for x in H if x not in set(Core)]
    tables = lagrange_tables(H, T, shape.k, q)
    worst, worst_nu = 0, None
    for nu in cfg["slopes"]:
        al, be = nu
        z = {x: (al * u[x] + be * v[x]) % q for x in H}
        mm = max(max_codeword_agreement(H, z, shape.k, q, tables), agr[nu])
        if mm > worst:
            worst, worst_nu = mm, nu
    chk(worst == shape.A, "TANGENT GATE: max codeword agreement = A",
        f"{worst} at {worst_nu}, competitors={int(tables[0].shape[0])}")

    # ---------------- |Bset| for this FIXED (u,v) across the whole family
    # (PP4): (f,g) = (f_* + Q tau, g_* - P tau), deg tau < k-ell = 1
    bset, members = set(), 0
    for c in range(q):
        f = {x: c % q for x in H}                    # f_* + Q*tau, Q=1
        gg = {x: (-c * pow(x, 3, q)) % q for x in H}  # g_* - P*tau, P=X^3
        Ec = {x: (u[x] - f[x]) % q for x in H}
        Epc = {x: (v[x] - gg[x]) % q for x in H}
        cor = [x for x in H if Ec[x] == 0 and Epc[x] == 0]
        if len(cor) != shape.k + shape.d:
            continue                                # not depth-d maximal
        members += 1
        for nu in cfg["slopes"]:
            al, be = nu
            a = sum(1 for x in H if (al * Ec[x] + be * Epc[x]) % q == 0)
            if a == shape.A:
                blk = tuple(sorted(x for x in H if rho[x]
                                   and (al * Ec[x] + be * Epc[x]) % q == 0))
                if len(blk) == shape.r:
                    bset.add(blk)
    report = {
        "shape": repr(shape),
        "witness_B1": B1, "witness_B2": B2,
        "witness_fiber_profile_B1": prof1,
        "witness_fiber_profile_B2": prof2,
        "D_fiber_sizes": [len(F) for F in fod],
        "selected_slopes": [list(cfg["lam1"]), list(cfg["lam2"])],
        "gate_max_agreement": worst,
        "gate_competitors_per_slope": int(tables[0].shape[0]),
        "gate_slopes": len(cfg["slopes"]),
        "family_maximal_members": members,
        "Bset_size_fixed_uv": len(bset),
        "sixt": 6 * shape.t,
        "checks": len(CHECKS),
        "failed": [c for c in CHECKS if not c["ok"]],
    }
    report["verdict"] = ("FR-F1 FIRES -- (FR) REFUTED as stated"
                         if not report["failed"] else "CHECKS FAILED")
    with open(os.path.join(HERE, "witness.json"), "w") as fh:
        json.dump({"report": report, "all_checks": CHECKS}, fh, indent=1,
                  sort_keys=True, default=str)
    print(json.dumps(report, indent=1, sort_keys=True, default=str))
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
