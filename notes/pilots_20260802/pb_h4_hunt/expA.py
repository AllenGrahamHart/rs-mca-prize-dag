#!/usr/bin/env python3
"""EXPERIMENT A -- EXHAUSTIVE maximisation over the WHOLE design space.

In the degree-A pencil model the design space is exactly the set of affine
lines of AG(h,q) (core.py header).  This script therefore searches ALL
pencils at a toy scale, exactly, by computing

    R := max over affine lines L of  #{ A-subsets S : E(S) in L }

together with the spread structure of the richest lines.  Every line with at
least one point passes through some point of the image, so iterating over
distinct image points and, for each, over normalised directions, is exact
and complete.

Run:  tools/ramguard local -- python3 expA.py CASE
"""
from __future__ import annotations

import json
import os
import sys
from itertools import combinations

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np

import core

HERE = os.path.dirname(os.path.abspath(__file__))

# n, q, K, h  (+ optional split-fibre reference shape m,g,a,b)
CASES = {
    #                n    q     K  h   m  g  a  b
    "A1": dict(n=16, q=97, K=4, h=3, m=2, g=1, a=3, b=7),
    "A2": dict(n=16, q=1153, K=4, h=2, m=2, g=2, a=2, b=6),
    "A3": dict(n=16, q=97, K=8, h=3, m=2, g=1, a=5, b=7),
    "A4": dict(n=16, q=241, K=4, h=3, m=2, g=1, a=3, b=7),
    "A5": dict(n=16, q=97, K=4, h=2, m=2, g=2, a=2, b=6),
    "A6": dict(n=16, q=97, K=6, h=3, m=2, g=1, a=4, b=7),
    "A7": dict(n=18, q=37, K=5, h=3, m=3, g=2, a=2, b=4),
    "A8": dict(n=16, q=193, K=4, h=3, m=2, g=1, a=3, b=7),
    # spread-faithful scales: P(|S^S'|>=K) small, so Gamma_lo is meaningful
    "B1": dict(n=24, q=2473, K=4, h=2, m=2, g=2, a=2, b=10),
    "B2": dict(n=24, q=4801, K=4, h=2, m=2, g=2, a=2, b=10),
}


def canon_dir(d, q):
    """scale a nonzero direction so its first nonzero entry is 1."""
    for x in d:
        if x % q:
            inv = pow(int(x) % q, q - 2, q)
            return tuple(int(y) * inv % q for y in d)
    raise AssertionError("zero direction")


def run(name):
    prm = CASES[name]
    n, q, K, h = prm["n"], prm["q"], prm["K"], prm["h"]
    A = K + h
    D = core.domain(q, n)
    assert n <= 62

    # ---- full image of the moment map -------------------------------
    pts = {}
    for S in combinations(range(n), A):
        E = core.moment_vector([D[i] for i in S], h, q)
        pts.setdefault(E, []).append(S)
    keys = list(pts.keys())
    N = len(keys)
    mult = np.array([len(pts[k]) for k in keys], dtype=np.int64)
    P = np.array(keys, dtype=np.int64)                      # (N,h)
    C_nA = sum(len(v) for v in pts.values())

    # ---- exact max-collinearity -------------------------------------
    pw = np.array([q ** j for j in range(h)], dtype=np.int64)
    INV = np.zeros(q, dtype=np.int64)
    for x in range(1, q):
        INV[x] = pow(x, q - 2, q)
    best = (0, -1, None)          # (count, i, direction)
    for i in range(N):
        d = (P - P[i]) % q                                  # (N,h)
        nz = np.any(d != 0, axis=1)
        dd = d[nz]
        mm = mult[nz]
        if dd.size == 0:
            tot = int(mult[i])
            if tot > best[0]:
                best = (tot, i, None)
            continue
        # normalise: divide by first nonzero coordinate
        first = np.argmax(dd != 0, axis=1)
        lead = dd[np.arange(dd.shape[0]), first]
        inv = INV[lead]                                      # exact table
        dn = (dd * inv[:, None]) % q
        code = dn @ pw
        order = np.argsort(code, kind="stable")
        cs = code[order]
        ms = mm[order]
        cut = np.flatnonzero(np.diff(cs)) + 1
        sums = np.add.reduceat(ms, np.concatenate(([0], cut)))
        j = int(np.argmax(sums))
        tot = int(sums[j]) + int(mult[i])
        if tot > best[0]:
            starts = np.concatenate(([0], cut))
            best = (tot, i, int(cs[starts[j]]))

    # ---- pass 2: every line with count >= tau, then the gauge-invariant
    #      admissibility gate (see gate() below) -----------------------
    tau = max(3, int(0.34 * best[0]) + 1)
    lines = {}
    for i in range(N):
        d = (P - P[i]) % q
        nz = np.any(d != 0, axis=1)
        dd, mm = d[nz], mult[nz]
        if dd.size == 0:
            continue
        first = np.argmax(dd != 0, axis=1)
        inv = INV[dd[np.arange(dd.shape[0]), first]]
        dn = (dd * inv[:, None]) % q
        code = dn @ pw
        order = np.argsort(code, kind="stable")
        cs, ms = code[order], mm[order]
        starts = np.concatenate(([0], np.flatnonzero(np.diff(cs)) + 1))
        sums = np.add.reduceat(ms, starts)
        hits = np.flatnonzero(sums + mult[i] >= tau)
        for j in hits:
            c = int(cs[starts[j]])
            dv, cc = [], c
            for _ in range(h):
                dv.append(cc % q)
                cc //= q
            t0 = next(t for t in range(h) if dv[t])
            base = tuple((int(P[i][t]) - int(P[i][t0]) * dv[t]) % q
                         for t in range(h))
            lines[(tuple(dv), base)] = int(sums[j]) + int(mult[i])

    def gate(dv, base):
        """GAUGE-INVARIANT admissibility of the line L = base + z*dv.

        The witness family depends ONLY on the top-h data (alpha,beta) = the
        line; every coefficient of degree < K is invisible.  So T1/T3/T4 and
        'v nowhere zero', read off the WORDS (u,v), can be switched on and
        off by an invisible perturbation and are vacuous as stated.  Their
        gauge-invariant forms are:
          (GI-strip)  beta != 0   (v not a codeword; equivalently deg V >= K)
          (GI-T3)     L is not invariant under the fold diag(zeta^j)_j for
                      any M > 1 dividing gcd(n,K), zeta = omega^(n/M)
          (GI-gen)    no A-set is a witness at two slopes: automatic if
                      beta != 0.
        """
        if not any(dv):
            return False, "beta=0"
        w = core.root_of_unity(q, n)
        gc = np.gcd(n, K)
        for M in range(2, int(gc) + 1):
            if gc % M:
                continue
            zt = pow(w, n // M, q)
            zz = [pow(zt, j + 1, q) for j in range(h)]
            dv2 = tuple(dv[t] * zz[t] % q for t in range(h))
            b2 = tuple(base[t] * zz[t] % q for t in range(h))
            cd2 = canon_dir(dv2, q)
            if cd2 != tuple(dv):
                continue
            t0 = next(t for t in range(h) if dv[t])
            b2r = tuple((b2[t] - b2[t0] * dv[t]) % q for t in range(h))
            if b2r == tuple(base):
                return False, f"fold-invariant M={M}"
        return True, "ok"

    def line_family(dv, base):
        t0 = next(t for t in range(h) if dv[t])
        inv0 = pow(dv[t0], q - 2, q)
        fam = []
        for E, sl in pts.items():
            z = (E[t0] - base[t0]) * inv0 % q
            if all((base[t] + z * dv[t]) % q == E[t] for t in range(h)):
                fam.extend((z, S) for S in sl)
        return fam

    ranked = sorted(lines.items(), key=lambda kv: -kv[1])
    report = []
    for (dv, base), cnt in ranked[:24]:
        ok, why = gate(dv, base)
        fam = line_family(dv, base)
        assert len(fam) == cnt, (len(fam), cnt)
        masks = [core.mask_of(S) for _, S in fam]
        byz = {}
        for z, S in fam:
            byz.setdefault(z, []).append(S)
        selm = [core.mask_of(min(v)) for v in byz.values()]
        report.append(dict(direction=list(dv), base=list(base), count=cnt,
                           admissible=ok, gate=why,
                           distinct_slopes=len(byz),
                           max_pair_core=core.max_pair_core(masks),
                           gamma_lo_full=len(core.gamma_lo(masks, K)),
                           greedy_spread=len(core.greedy_spread(masks, K)),
                           lex_selected=len(selm),
                           gamma_lo_lex=len(core.gamma_lo(selm, K)),
                           example_supports=[list(S) for _, S in fam[:6]]))

    # ---- reconstruct the richest line -------------------------------
    R, bi, bcode = best
    online = list(pts[keys[bi]])
    if bcode is not None:
        dvec = []
        c = bcode
        for _ in range(h):
            dvec.append(c % q)
            c //= q
        dvec = tuple(dvec)
        for j in range(N):
            if j == bi:
                continue
            d = tuple((int(P[j][t]) - int(P[bi][t])) % q for t in range(h))
            if any(d) and canon_dir(d, q) == dvec:
                online.extend(pts[keys[j]])
    else:
        dvec = None
    assert len(online) == R

    # ---- structure of the richest line ------------------------------
    masks = [core.mask_of(S) for S in online]
    lo = core.gamma_lo(masks, K)
    mx = core.max_pair_core(masks)
    spread = core.greedy_spread(masks, K)

    # slopes: parametrise the line by t with point = P[bi] + t*dvec
    slope_of = {}
    if dvec is not None:
        tfrom = None
        for t in range(h):
            if dvec[t]:
                tfrom = t
                break
        inv = pow(dvec[tfrom], q - 2, q)
        for S in online:
            E = core.moment_vector([D[i] for i in S], h, q)
            z = (E[tfrom] - int(P[bi][tfrom])) * inv % q
            slope_of.setdefault(z, []).append(S)
    else:
        slope_of[0] = online
    # ORD-LEX first match per slope
    sel = [core.mask_of(min(v)) for v in slope_of.values()]
    sel_lo = core.gamma_lo(sel, K)

    # ---- split-fibre reference line (if the shape is declared) ------
    sf = None
    if "m" in prm:
        m, g, a, b = prm["m"], prm["g"], prm["a"], prm["b"]
        if g + m * a == A and m <= h < 2 * m and b + g <= n // m:
            nf = n // m
            fib = [[j + t * nf for t in range(m)] for j in range(nf)]
            core_idx = [j for j in range(b, b + g)]
            fam, fmask, fslope = [], [], []
            for J in combinations(range(b), a):
                sup = sorted(set(core_idx) | {i for j in J for i in fib[j]})
                assert len(sup) == A
                fam.append(sup)
                fmask.append(core.mask_of(sup))
                fslope.append(sum(pow(D[m * j], 1, q) for j in J) % q)
            Esf = {core.moment_vector([D[i] for i in s], h, q) for s in fam}
            # collinear?
            Elist = sorted(Esf)
            col = True
            if len(Elist) >= 2:
                d0 = tuple((Elist[1][t] - Elist[0][t]) % q for t in range(h))
                cd = canon_dir(d0, q)
                for E in Elist[2:]:
                    d = tuple((E[t] - Elist[0][t]) % q for t in range(h))
                    if not any(d) or canon_dir(d, q) != cd:
                        col = False
                        break
            sfsel = {}
            for s, z in zip(fmask, fslope):
                if z not in sfsel or s < sfsel[z]:
                    sfsel[z] = s
            sf = dict(family_size=len(fam), distinct_moment_points=len(Esf),
                      collinear=col, distinct_slopes=len(set(fslope)),
                      max_pair_core=core.max_pair_core(fmask),
                      gamma_lo_full=len(core.gamma_lo(fmask, K)),
                      greedy_spread=len(core.greedy_spread(fmask, K)),
                      lex_selected=len(sfsel),
                      gamma_lo_lex_selected=len(
                          core.gamma_lo(list(sfsel.values()), K)))

    mu_num, mu_den = C_nA, q ** (h - 1)
    out = dict(
        case=name, params=dict(n=n, q=q, K=K, h=h, A=A, rate=f"{K}/{n}"),
        image=dict(subsets=C_nA, distinct_moment_points=N,
                   ambient=q ** h,
                   max_fibre=int(mult.max())),
        supply=dict(mean_witnesses_per_line_num=mu_num,
                    mean_witnesses_per_line_den=mu_den,
                    mean_witnesses_per_line=mu_num / mu_den,
                    mean_per_slope=mu_num / q ** h),
        dof_ceiling=dict(pencil_model_free_witnesses=2,
                         word_model=2 * (n - K) // max(h - 1, 1)),
        richest_line=dict(count=R, base=[int(x) for x in P[bi]],
                          direction=list(dvec) if dvec else None,
                          excess_over_mean=R / (mu_num / mu_den),
                          distinct_slopes=len(slope_of),
                          max_pair_core=mx, K=K,
                          gamma_lo_full_family=len(lo),
                          greedy_spread_subfamily=len(spread),
                          lex_selected=len(sel),
                          gamma_lo_lex_selected=len(sel_lo),
                          supports=[list(s) for s in online[:40]]),
        split_fibre_reference=sf,
        tau=tau, lines_at_or_above_tau=len(lines), top_lines=report,
    )
    adm = [r for r in report if r["admissible"]]
    out["richest_admissible"] = adm[0] if adm else None
    path = os.path.join(HERE, f"EXPA_{name}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(f"[{name}] n={n} q={q} K={K} h={h} A={A} | C(n,A)={C_nA} "
          f"distinct-E={N} mean/line={mu_num/mu_den:.4g}")
    print(f"   RICHEST LINE: {R} subsets  (x{R/(mu_num/mu_den):.3g} the mean) "
          f"maxcore={mx} (K={K}) Gamma_lo(full)={len(lo)} "
          f"greedy-spread={len(spread)} lex-sel={len(sel)} "
          f"Gamma_lo(lex)={len(sel_lo)}")
    r0 = out["richest_admissible"]
    if r0:
        print(f"   RICHEST ADMISSIBLE (gauge-invariant gate): {r0['count']} "
              f"(x{r0['count']/(mu_num/mu_den):.3g}) maxcore={r0['max_pair_core']} "
              f"Gamma_lo(full)={r0['gamma_lo_full']} "
              f"greedy-spread={r0['greedy_spread']} "
              f"Gamma_lo(lex)={r0['gamma_lo_lex']}")
    print(f"   lines>=tau({tau}): {len(lines)}; rejected-by-gate: "
          f"{sum(1 for r in report if not r['admissible'])}/24")
    if sf:
        print(f"   SPLIT-FIBRE line: size={sf['family_size']} "
              f"collinear={sf['collinear']} maxcore={sf['max_pair_core']} "
              f"Gamma_lo(full)={sf['gamma_lo_full']} "
              f"greedy-spread={sf['greedy_spread']} "
              f"Gamma_lo(lex)={sf['gamma_lo_lex_selected']}")
    print(f"   -> {path}")
    return out


if __name__ == "__main__":
    for nm in (sys.argv[1:] or ["A1"]):
        run(nm)
