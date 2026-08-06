#!/usr/bin/env python3
"""FULL-RANK leaf pilot: which stratum do the LARGE window-divisor
families live in?   (2026-08-04)

PROFILE: local.   Run:  tools/ramguard local -- python3 <this>

PREREG items P3, P4, P7, P8, plus a SECOND-ROUND PRE-REGISTRATION for
the extremal search (part C), written here BEFORE part C was run:

  S1  The MC-5 SHIFT PENCIL is rank-DEFICIENT, exactly.  If
      v_j = u_{j+delta} (cyclically; equivalently v(x) = x^-delta u(x)
      on mu_n), the rows of R_v(d) are the rows of R_u(d) shifted by
      delta, so the stacked row set is a union of two length-d cyclic
      intervals and
          rank J_d <= d + min(|delta|_cyc, d),   |delta|_cyc =
          min(delta mod n, n - delta mod n).
      PREDICT: exact equality for gated words, hence DEFICIENT whenever
      |delta|_cyc < d.
  S2  The recorded sub-depth coset adversary of sl2_unstructured/
      planted.py is such a shift pencil (delta = rho_u - rho_v + M),
      hence rank-DEFICIENT: it routes to the SIBLING leaf
      xr_band_forced_commonroot_syzygy_count, NOT to this one.
      PREDICT: FIRES -- i.e. PREREG P3 is REFUTED and PREREG F2 fires.
  S3  EXTREMAL SEARCH.  rank J_d and the family size are both functions
      of the syndrome 2-plane pi = <sigma(u),sigma(v)> alone.  Greedily
      grow families by intersecting Syn(T)'s, then stratify the achieved
      family sizes by rank J_d.  PREDICT: the largest families are
      concentrated in the DEFICIENT strata, and the maximum over the
      FULL-rank stratum is strictly smaller at every fixture.  This is
      an empirical law about toy rows only -- toys are subcritical and
      NO count claim about (SL2-RES) follows from it.
  S4  PREDICT: a full-rank pi with family size >= 2 exists at every
      fixture (so the full-rank stratum is not vacuous), and its maximum
      grows with r' - 2d = dim of the affine window.

Part A tests S1, part B tests S2 (and P7, P8), part C tests S3/S4.
"""
import json
import os
import random
import sys
from itertools import combinations
from math import comb, log2

_SIB = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "pilots_20260803", "sl2_unstructured"))
sys.path.insert(0, _SIB)
from algebra import (direct_core, evalpoly, inv, lemmaW,  # noqa: E402
                     locator, pmul, rank, root_of_unity)
from dualform import (gamma, pair_profile, pencil_profile,  # noqa: E402
                      spanrank, toeplitz)

random.seed(20260804)
checks = []


def ck(name, tag, ok, extra=None):
    checks.append(dict(check=name, fixture=tag, ok=bool(ok), extra=extra))
    return bool(ok)


# --------------------------------------------------------------- linalg
def rref_span(vecs, q):
    """row-reduced basis of the span (list of rows), in place-safe."""
    rows = [v[:] for v in vecs]
    ncol = len(rows[0]) if rows else 0
    R = 0
    for col in range(ncol):
        piv = next((i for i in range(R, len(rows)) if rows[i][col]), None)
        if piv is None:
            continue
        rows[R], rows[piv] = rows[piv], rows[R]
        iv = inv(rows[R][col], q)
        rows[R] = [x * iv % q for x in rows[R]]
        for i in range(len(rows)):
            if i != R and rows[i][col]:
                f = rows[i][col]
                rows[i] = [(rows[i][j] - f * rows[R][j]) % q
                           for j in range(ncol)]
        R += 1
    return [r for r in rows[:R]]


def try_add(basis, pivots, rows, q, cap):
    """append rows to a row-echelon basis; None if the dim would exceed cap."""
    nb = [r[:] for r in basis]
    npv = list(pivots)
    for row in rows:
        r = list(row)
        for b, p in zip(nb, npv):
            if r[p]:
                fct = r[p]
                r = [(r[j] - fct * b[j]) % q for j in range(len(r))]
        piv = next((j for j in range(len(r)) if r[j]), None)
        if piv is None:
            continue
        iv = inv(r[piv], q)
        r = [x * iv % q for x in r]
        nb.append(r)
        npv.append(piv)
        if len(nb) > cap:
            return None
    return nb, npv


def nullspace(rows, q, ncol):
    """basis of {x : rows . x = 0}."""
    B = rref_span(rows, q) if rows else []
    pivots = []
    for r in B:
        pivots.append(next(j for j in range(ncol) if r[j]))
    free = [j for j in range(ncol) if j not in pivots]
    basis = []
    for fj in free:
        x = [0] * ncol
        x[fj] = 1
        for r, pj in zip(B, pivots):
            x[pj] = (-r[fj]) % q
        basis.append(x)
    return basis


def annihilator_of_divisor(Tp, n, k, d, q):
    """W_T = Syn(T)^perp = { Y^i * E_{T^-1}(Y) : i < d }, dim d.

    <Lambda, gamma(t)> = t^-k Lambda(t^-1), so Lambda kills Syn(T) iff
    Lambda vanishes on T^-1, i.e. E_{T^-1} | Lambda, deg < n-k.
    """
    Einv = locator([inv(t, q) for t in Tp], q)      # degree r'
    N = n - k
    out = []
    for i in range(d):
        row = [0] * N
        for j, c in enumerate(Einv):
            row[i + j] = c % q
        out.append(row)
    return out


def syn_of(w, n, k):
    return list(w[k:n])


def word_from_syndrome(s, n, k):
    return [0] * k + list(s)


# ------------------------------------------------------------- fixtures
FIXA = [dict(n=16, k=4, q=97, d=3), dict(n=16, k=4, q=97, d=4),
        dict(n=14, k=4, q=29, d=3), dict(n=12, k=4, q=13, d=3),
        dict(n=20, k=6, q=41, d=4)]
SEARCH = [dict(n=14, k=4, q=29, d=3, npi=120, ngreedy=120, cand=900),
          dict(n=16, k=4, q=97, d=3, npi=40, ngreedy=40, cand=900)]


def family_of(pi, WT, q):
    """all divisors T with pi <= Syn(T), i.e. W_T annihilates pi."""
    su, sv = pi
    out = []
    for idx, W in enumerate(WT):
        ok = True
        for row in W:
            a = 0
            b = 0
            for j, c in enumerate(row):
                if c:
                    a += c * su[j]
                    b += c * sv[j]
            if a % q or b % q:
                ok = False
                break
        if ok:
            out.append(idx)
    return out


def analyse_family(pi, Ts, H, n, k, d, q, want_profile=True):
    """maximality + liveness ledger for a family (small families only)."""
    su, sv = pi
    u = word_from_syndrome(su, n, k)
    v = word_from_syndrome(sv, n, k)
    u_vec = [evalpoly(u, x, q) for x in H]
    v_vec = [evalpoly(v, x, q) for x in H]
    A_gate = None
    if want_profile:
        A_gate = pencil_profile(u_vec, v_vec, H, n, k, q)[0]
    maximal, live2 = 0, 0
    Lps = []
    for T in Ts:
        okf, fc = direct_core(u_vec, H, T, n, k, d, q)
        okg, gc = direct_core(v_vec, H, T, n, k, d, q)
        if not (okf and okg):
            continue
        core, agr = pair_profile(fc, gc, u_vec, v_vec, H, n, q)
        if sorted(core) != sorted(set(range(n)) - set(T)):
            continue
        maximal += 1
        if A_gate is not None:
            L = sum(1 for z, a in agr.items() if a == A_gate)
            Lps.append(L)
            if L >= 2:
                live2 += 1
    return dict(raw=len(Ts), maximal=maximal, live2=live2,
                A_gate=A_gate, h=(A_gate - k) if A_gate else None,
                Lp=sorted(Lps, reverse=True)[:8])


def main():
    out = {}

    # =============================================== A: shift pencils S1
    A = []
    for f in FIXA:
        n, k, q, d = f["n"], f["k"], f["q"], f["d"]
        rp = n - k - d
        for delta in range(1, min(6, n)):
            u = [0] * n
            for p in range(k, n):
                u[p] = random.randrange(1, q)
            v = [u[(j + delta) % n] for j in range(n)]
            # v is supported off the window in general: keep only the
            # window part (the rank depends on the syndrome alone)
            v = [0 if j < k else v[j] for j in range(n)]
            vfull = [u[(j + delta) % n] for j in range(n)]
            J = toeplitz(u, n, d, rp) + toeplitz(vfull, n, d, rp)
            rJ = rank(J, q)
            dc = min(delta % n, n - delta % n)
            bound = d + min(dc, d)
            A.append(dict(n=n, k=k, q=q, d=d, delta=delta, rank=rJ,
                          bound=bound, cap=min(2 * d, rp + 1)))
            ck("A/S1: shift pencil rank J_d <= d + min(|delta|,d)",
               f"n{n}k{k}d{d}q{q}delta{delta}", rJ <= bound,
               dict(rank=rJ, bound=bound))
            ck("A/S1b: shift pencil is DEFICIENT when |delta| < d and "
               "2d <= r'+1", f"n{n}k{k}d{d}q{q}delta{delta}",
               (rJ < 2 * d) if (dc < d and 2 * d <= rp + 1) else True,
               dict(rank=rJ, twod=2 * d, rp1=rp + 1))
    out["A_shift"] = A

    # ======================================== B: the recorded adversary
    # sl2_unstructured/planted.py fixture, rebuilt verbatim
    q, n, k, M = 97, 16, 4, 2
    NQ, KQ, DQ, MPRIME = n // M, k // M, 2, 2
    RHO_U, RHO_V = 0, 1
    d = M * DQ
    rp = n - k - d
    g0 = root_of_unity(n, q)
    H = [pow(g0, i, q) for i in range(n)]
    gN = pow(g0, M, q)
    HQ = [pow(gN, i, q) for i in range(NQ)]
    mq = NQ - KQ - DQ
    NP, mp = NQ // MPRIME, mq // MPRIME
    A0 = [i + j * NP for i in range(mp) for j in range(MPRIME)]
    prod0 = 1
    for i in A0:
        prod0 = prod0 * HQ[i] % q
    cprime = ((-1) ** (mq + 1) * prod0) % q
    U = [0] * NQ
    U[NQ - 1] = 1
    U[KQ + DQ - 1] = cprime
    V = [U[(s + 1) % NQ] for s in range(NQ)]
    u = [0] * n
    v = [0] * n
    for s in range(NQ):
        u[(RHO_U + s * M) % n] = U[s]
        v[(RHO_V + s * M) % n] = V[s]
    # is v a cyclic shift of u?
    delta_found = None
    for delta in range(n):
        if all(v[j] == u[(j + delta) % n] for j in range(n)):
            delta_found = delta
            break
    J = toeplitz(u, n, d, rp) + toeplitz(v, n, d, rp)
    rJ = rank(J, q)
    ck("B/S2: the recorded coset adversary IS a cyclic shift pencil",
       "planted", delta_found is not None,
       dict(delta=delta_found, predicted=RHO_U - RHO_V + M))
    ck("B/S2b: the recorded coset adversary is stacked-rank DEFICIENT "
       "(routes to the SIBLING leaf, not this one)", "planted",
       rJ < 2 * d, dict(rank=rJ, twod=2 * d, cap=min(2 * d, rp + 1)))
    fam = []
    for T in combinations(range(n), rp):
        Tp = [H[i] for i in T]
        if lemmaW(u, Tp, n, k, d, q)[0] and lemmaW(v, Tp, n, k, d, q)[0]:
            fam.append(T)
    ledger = analyse_family((syn_of(u, n, k), syn_of(v, n, k)), fam,
                            H, n, k, d, q)
    equi = log2(comb(n, rp)) - 2 * d * log2(q)
    ledger["excess_bits_raw"] = (log2(len(fam)) - equi) if fam else None
    ledger["equidistribution_log2"] = equi
    ledger["rank_J"] = rJ
    ledger["delta"] = delta_found
    ck("B/P8: the recorded adversary's family survives MAXIMALITY",
       "planted", ledger["maximal"] > 0, ledger)
    out["B_planted"] = ledger

    # ======================================== C: extremal search S3/S4
    C = []
    for f in SEARCH:
        n, k, q, d = f["n"], f["k"], f["q"], f["d"]
        rp = n - k - d
        N = n - k
        g0 = root_of_unity(n, q)
        H = [pow(g0, i, q) for i in range(n)]
        Tlist = list(combinations(range(n), rp))
        WT = [annihilator_of_divisor([H[i] for i in T], n, k, d, q)
              for T in Tlist]
        # sanity: W_T really is Syn(T)^perp
        for idx in random.sample(range(len(Tlist)), 5):
            G = [gamma(H[i], n, k, q) for i in Tlist[idx]]
            okperp = all(sum(a * b for a, b in zip(row, gv)) % q == 0
                         for row in WT[idx] for gv in G)
            ck("C0: W_T = Syn(T)^perp = Y^i E_{T^-1}, dim d",
               f"n{n}k{k}d{d}", okperp and spanrank(WT[idx], q) == d)
        tag = f"n{n}k{k}d{d}q{q}"
        best = {}
        recs = []

        def record(pi, source):
            fam = family_of(pi, WT, q)
            u = word_from_syndrome(pi[0], n, k)
            v = word_from_syndrome(pi[1], n, k)
            rJ = rank(toeplitz(u, n, d, rp) + toeplitz(v, n, d, rp), q)
            rec = dict(source=source, rank=rJ, raw=len(fam))
            if len(fam) >= max(1, best.get(rJ, dict(raw=0))["raw"]):
                led = analyse_family(pi, [Tlist[i] for i in fam], H,
                                     n, k, d, q,
                                     want_profile=(len(fam) <= 400))
                rec.update(led)
                if len(fam) > best.get(rJ, dict(raw=-1))["raw"]:
                    best[rJ] = rec
            recs.append(rec)
            return rec

        # (a) random 2-planes
        for _ in range(f["npi"] // 4):
            pi = ([random.randrange(q) for _ in range(N)],
                  [random.randrange(q) for _ in range(N)])
            record(pi, "random")
        # (b) greedy growth: intersect Syn(T)'s while dim >= 2
        for _ in range(f["ngreedy"]):
            basis, pivots, chosen = [], [], []
            order = random.sample(range(len(Tlist)),
                                  min(len(Tlist), f.get("cand", 900)))
            for idx in order:
                res = try_add(basis, pivots, WT[idx], q, N - 2)
                if res is not None:
                    basis, pivots = res
                    chosen.append(idx)
            span = rref_span(basis, q) if basis else []
            ns = nullspace(span, q, N)
            if len(ns) < 2:
                continue
            for _ in range(2):
                c1 = [random.randrange(q) for _ in ns]
                c2 = [random.randrange(q) for _ in ns]
                su = [sum(c * b[j] for c, b in zip(c1, ns)) % q
                      for j in range(N)]
                sv = [sum(c * b[j] for c, b in zip(c2, ns)) % q
                      for j in range(N)]
                if spanrank([su, sv], q) == 2:
                    record((su, sv), f"greedy(seeds={len(chosen)})")
        # (c) structured seeds: MC words, shift pencils, coset lifts
        for w in range(2, d + 2):
            for cc in (1, 2, 3):
                uu = [0] * n
                uu[n - 1] = 1
                uu[k + w - 1] = cc % q
                for delta in (1, 2, 3):
                    vv = [uu[(j + delta) % n] for j in range(n)]
                    if spanrank([syn_of(uu, n, k), syn_of(vv, n, k)],
                                q) == 2:
                        record((syn_of(uu, n, k), syn_of(vv, n, k)),
                               f"MC(w={w})+shift({delta})")
                vv = [0] * n
                vv[n - 1] = 1
                vv[k + w] = cc % q
                if spanrank([syn_of(uu, n, k), syn_of(vv, n, k)], q) == 2:
                    record((syn_of(uu, n, k), syn_of(vv, n, k)),
                           f"MC(w={w})+MC(w={w+1})")
        equi = log2(comb(n, rp)) - 2 * d * log2(q)
        strat = {}
        for r in sorted(best):
            b = best[r]
            strat[r] = dict(max_raw=b["raw"], maximal=b["maximal"],
                            live2=b["live2"], source=b["source"],
                            A_gate=b["A_gate"], h=b["h"], Lp=b["Lp"],
                            excess_bits=(log2(b["raw"]) - equi)
                            if b["raw"] else None)
        C.append(dict(tag=tag, n=n, k=k, d=d, q=q, rprime=rp,
                      divisors=len(Tlist), affine_dim=rp - 2 * d,
                      equidistribution_log2=equi, strata=strat,
                      n_pi=len(recs)))
        full = strat.get(2 * d, dict(max_raw=0))["max_raw"]
        defi = max([v["max_raw"] for r, v in strat.items()
                    if r < 2 * d] or [0])
        ck("C/S3: the LARGEST family lives in a DEFICIENT stratum",
           tag, defi > full, dict(full_rank_max=full, deficient_max=defi))
        ck("C/S4: the full-rank stratum is non-vacuous (a full-rank pi "
           "with a non-empty family exists)", tag, full >= 1,
           dict(full_rank_max=full))
    out["C_search"] = C

    bad = [c for c in checks if not c["ok"]]
    print(f"checks: {len(checks)}   failures: {len(bad)}")
    for b in bad:
        print("  FAIL", b["check"], b["fixture"], b.get("extra"))
    print()
    print("--- A: shift pencils (v_j = u_{j+delta}) ---")
    for a in A[:14]:
        print(f"  n{a['n']}k{a['k']}d{a['d']} delta={a['delta']}: "
              f"rank={a['rank']}  bound d+min(|delta|,d)={a['bound']}  "
              f"cap min(2d,r'+1)={a['cap']}")
    print()
    print("--- B: the recorded coset adversary (planted.py fixture) ---")
    print(f"  cyclic shift delta = {out['B_planted']['delta']}   "
          f"rank J_d = {out['B_planted']['rank_J']} / 2d = {2*4}")
    print(f"  raw={out['B_planted']['raw']} maximal="
          f"{out['B_planted']['maximal']} live2="
          f"{out['B_planted']['live2']} A={out['B_planted']['A_gate']} "
          f"h={out['B_planted']['h']} L_P={out['B_planted']['Lp']}")
    print(f"  equidistribution log2 = "
          f"{out['B_planted']['equidistribution_log2']:.2f}; excess = "
          f"{out['B_planted']['excess_bits_raw']}")
    print()
    print("--- C: extremal search, stratified by rank J_d ---")
    for c in C:
        print(f"  {c['tag']}  r'={c['rprime']} affine dim r'-2d="
              f"{c['affine_dim']}  divisors={c['divisors']}  "
              f"pi sampled={c['n_pi']}")
        for r in sorted(c["strata"]):
            s = c["strata"][r]
            mark = "FULL" if r == 2 * c["d"] else "def "
            print(f"     rank={r:>2} [{mark}]  max raw={s['max_raw']:>4}"
                  f"  maximal={s['maximal']:>4}  L_P>=2={s['live2']:>4}"
                  f"  h={s['h']}  src={s['source']}")
    out["checks"] = checks
    out["n_checks"] = len(checks)
    out["n_fail"] = len(bad)
    out["verdict"] = "PASS" if not bad else "FAIL"
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(out, fh, indent=1)


if __name__ == "__main__":
    main()
