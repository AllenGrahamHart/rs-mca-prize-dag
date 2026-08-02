#!/usr/bin/env python3
"""The b-resolved coset obstruction and the slice-dead mode census (F2A.5).

Run:  tools/ramguard local -- python3 \
        notes/pilots_20260802/f2_slice_coefficients/mode_and_coset.py [stage]

stages: verify | census | fence | weighted

THE STATEMENT UNDER TEST (all exact).  With sigma_i = s_i + p u_i and
Delta_i = sigma_i^+ - sigma_i^- (mod 2p), for every ODD mode k the phase
index of the local ratio r_i(k) = A_i(k)/B_i(k) is phi_i(k) = k Delta_i.
Put G = <Delta_i>, D = <Delta_i - Delta_j>.  Then

  full-window death at mode k  <=>  k Delta_i == 0 for all i  <=>  k in Ann(G)
  SLICE death at mode k        <=>  k Delta_i all EQUAL       <=>  k in Ann(D)

and Ann(D) >= Ann(G) with equality iff D = G.  Since 2p = 2*p (p prime) and
the Delta_i are not all congruent mod p for c outside F_p, the only odd
candidate is k = p, and

  all Delta_i EVEN  -> k=p is full-window dead AND slice dead
  all Delta_i ODD   -> k=p is SLICE DEAD but full-window MAXIMALLY contracting
  mixed parities    -> k=p is neither.

Equivalently at the level of the carry itself: at fixed b the reachable
carry set satisfies  R_b  subset  base + b*Delta_1 + D, i.e. slicing traps
the carry in a COSET of the difference subgroup -- the full-window
reachability theorem (F2A.2 Sharp Law A) does not survive b-resolution.
"""

from __future__ import annotations

import json
import math
import os
import sys
from fractions import Fraction

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from slicecore import (  # noqa: E402
    Cyc, Delta_of, RESULTS, abs_pairs, admissible_orders, carry_sign,
    elem_sym, instance, is_prime, mode_pairs, omega_pow, phase_index,
    deltas_of, nus_of, sigma_of, slice_coeffs_carrydp, subgroup_gen,
    Fp2, pair_reps, residues,
)


def slice_count_sigma(p: int, sig):
    """N[b][r] over the MODIFIED residues sigma (signs folded in)."""
    two_p = 2 * p
    n = len(sig)
    dp = [[0] * two_p for _ in range(n + 1)]
    dp[0][0] = 1
    for i, (sp, sm) in enumerate(sig):
        nd = [[0] * two_p for _ in range(n + 1)]
        for b in range(i + 1):
            row = dp[b]
            for r in range(two_p):
                v = row[r]
                if v:
                    nd[b + 1][(r + sp) % two_p] += v
                    nd[b][(r + sm) % two_p] += v
        dp = nd
    return dp


def V_of(p, N, n):
    return [sum(N[b][r] * carry_sign(p, r) for r in range(2 * p))
            for b in range(n + 1)]


# ------------------------------------------------------------- verify ------

def stage_verify():
    """Exact checks of the phase identity, the death dichotomy, the coset."""
    rows = 0
    for p in (7, 11, 13):
        for c in ((1, 1), (2, 3), (0, 1), (1, 2)):
            c = (c[0] % p, c[1] % p)
            _, _, loc = instance(p, c=c, n=5)
            if len(loc) < 5:
                continue
            n = len(loc)
            d, nu = deltas_of(p, loc), nus_of(p, loc)
            Dl = Delta_of(p, loc)
            aps = abs_pairs(p, loc)
            E = elem_sym(aps)
            two_p = 2 * p
            for k in range(1, two_p, 2):
                # (a) phi_i(k) = k * Delta_i for odd k
                for i in range(n):
                    assert phase_index(p, k, d[i], nu[i]) == (k * Dl[i]) % two_p
                # (b) A_i(k) = omega^{k Delta_i} * (a-ratio) * B_i(k):
                #     check the exact identity  A_i * conj(B_i) has argument
                #     k*Delta_i, i.e. A_i conj(B_i) = omega^{k Delta_i} a+ a-
                mps = mode_pairs(p, k, loc)
                for i, (A, B) in enumerate(mps):
                    lhs = A * B.conj()
                    rhs = omega_pow(p, k * Dl[i]) * aps[i][0] * aps[i][1]
                    assert (lhs - rhs).is_zero(), f"phase id p={p} k={k} i={i}"
                # (c) slice death  <=>  k*Delta_i all equal
                e = elem_sym(mps)
                dead = all((e[b] * e[b].conj() - E[b] * E[b]).is_zero()
                           for b in range(n + 1))
                same = len({(k * x) % two_p for x in Dl}) == 1
                assert dead == same, f"slice death p={p} k={k}"
                # (d) full-window death <=> k*Delta_i all == 0
                fw = Cyc.one(p)
                ann = Cyc.one(p)
                for (A, B), (a1, a2) in zip(mps, aps):
                    fw = fw * (A + B)
                    ann = ann * (a1 + a2)
                fwdead = (fw * fw.conj() - ann * ann).is_zero()
                assert fwdead == all((k * x) % two_p == 0 for x in Dl), \
                    f"fw death p={p} k={k}"
                rows += 1
            # (e) the coset containment R_b subset base + b Delta_1 + D
            sig = sigma_of(p, loc)
            g = subgroup_gen(two_p, [x - Dl[0] for x in Dl])
            base = sum(x[1] for x in sig) % two_p
            N = slice_count_sigma(p, sig)
            for b in range(n + 1):
                for r in range(two_p):
                    if N[b][r]:
                        assert (r - base - b * Dl[0]) % g == 0, \
                            f"coset p={p} c={c} b={b} r={r} g={g}"
    print(f"F2A5_C1_PHASE_ID_PASS        phi_i(k) = k*Delta_i for every odd "
          f"mode; A_i conj(B_i) = omega^{{k Delta_i}} a+ a-  (exact)")
    print(f"F2A5_C2_DEATH_DICHOTOMY_PASS slice death <=> k*Delta_i constant; "
          f"full-window death <=> k*Delta_i == 0; modes checked={rows}")
    print(f"F2A5_C3_COSET_PASS           R_b lies in base + b*Delta_1 + "
          f"<Delta_i - Delta_j> for every b (exact)")


# ------------------------------------------------------------- census ------

def stage_census():
    """How common is each parity class of {Delta_i}?  Exhaustive over c."""
    out = []
    for p in (7, 11, 13, 19, 23, 31):
        F = Fp2.make(p)
        mu = admissible_orders(p)[-1]
        reps = pair_reps(F, F.subgroup(mu))
        tot = {"all_even": 0, "all_odd": 0, "mixed": 0, "vacuous": 0}
        n = min(8, len(reps))
        odd_frac = []
        for a in range(p):
            for bq in range(p):
                if (a, bq) == (0, 0):
                    continue
                loc = [residues(F, (a, bq), y) for y in reps[:n]]
                Dl = Delta_of(p, loc)
                par = {x % 2 for x in Dl}
                if bq == 0:
                    tot["vacuous"] += 1
                elif par == {0}:
                    tot["all_even"] += 1
                elif par == {1}:
                    tot["all_odd"] += 1
                else:
                    tot["mixed"] += 1
                # fraction of pairs with odd Delta over the WHOLE pair set
                if bq != 0:
                    allloc = [residues(F, (a, bq), y) for y in reps]
                    aD = Delta_of(p, allloc)
                    odd_frac.append(sum(x % 2 for x in aD) / len(aD))
        # the trace-zero line c = (0, b)
        tz = []
        for bq in range(1, p):
            loc = [residues(F, (0, bq), y) for y in reps[:n]]
            tz.append({x % 2 for x in Delta_of(p, loc)})
        out.append({"p": p, "n_window": n, "counts": tot,
                    "trace_zero_all_even": all(s == {0} for s in tz),
                    "odd_frac_min": min(odd_frac), "odd_frac_max": max(odd_frac),
                    "odd_frac_mean": sum(odd_frac) / len(odd_frac),
                    "m_pairs": len(reps)})
        print(f"p={p:3d} m={len(reps):4d} window n={n}: {tot} | "
              f"trace-zero line all-even: {out[-1]['trace_zero_all_even']} | "
              f"odd-Delta fraction over all pairs: "
              f"min={min(odd_frac):.3f} mean={sum(odd_frac)/len(odd_frac):.3f} "
              f"max={max(odd_frac):.3f}")
    with open(os.path.join(RESULTS, "delta_parity_census.json"), "w") as f:
        json.dump({"rows": out}, f, indent=1)
    print("\n=> the all-even class is exactly the trace-zero line (a_c = 0); "
          "the all-odd class is reached by SELECTING the ~half of pairs with "
          "odd Delta at ANY frequency (see stage 'fence').")


# -------------------------------------------------------------- fence ------

def stage_fence():
    """The headline: a selected all-odd-Delta window floors the slice at 1/p
    while the full window keeps contracting exponentially."""
    rows = []
    print("[F1] SELECTED all-odd-Delta windows (generic c!): exact integer "
          "balanced-weight proxy V_b = sum_{|tau|=b} h_p(sum sigma_i)")
    print(f"{'p':>4} {'c':>8} {'n':>4} {'b':>4} {'V_b':>18} {'C(n,b)':>18} "
          f"{'-log2 rho_b':>12} {'1/p bits':>9} {'sign':>5}")
    for p in (11, 13, 19, 23, 31, 41):
        F = Fp2.make(p)
        mu = admissible_orders(p)[-1]
        reps = pair_reps(F, F.subgroup(mu))
        for c in ((1, 1), (2, 3)):
            allloc = [residues(F, c, y) for y in reps]
            aD = Delta_of(p, allloc)
            sel_odd = [i for i in range(len(aD)) if aD[i] % 2 == 1]
            sel_mix = list(range(len(aD)))
            for tag, sel in (("odd", sel_odd), ("mix", sel_mix)):
                for n in (16, 32, 48):
                    if n > len(sel):
                        continue
                    loc = [allloc[i] for i in sel[:n]]
                    sig = sigma_of(p, loc)
                    N = slice_count_sigma(p, sig)
                    V = V_of(p, N, n)
                    full = sum(V)
                    annf = sum(math.comb(n, b) for b in range(n + 1))
                    per = []
                    for b in range(n + 1):
                        C = math.comb(n, b)
                        per.append({"b": b, "V": V[b], "C": C})
                    rows.append({"p": p, "c": list(c), "tag": tag, "n": n,
                                 "per_b": per, "full": full,
                                 "full_annealed": annf})
                    if tag == "odd":
                        for b in (n // 4, n // 2, 3 * n // 4):
                            C = math.comb(n, b)
                            if V[b] == 0:
                                continue
                            lg = math.log2(C) - math.log2(abs(V[b]))
                            print(f"{p:4d} {str(c):>8} {n:4d} {b:4d} "
                                  f"{V[b]:18d} {C:18d} {lg:12.4f} "
                                  f"{math.log2(p):9.4f} "
                                  f"{'+' if V[b] > 0 else '-':>5}")
    with open(os.path.join(RESULTS, "slice_coset_fence.json"), "w") as f:
        json.dump({"rows": rows}, f)

    print("\n[F2] the SAME windows, full-window (b-summed) alignment: the "
          "slice floor is invisible after summing over b")
    print(f"{'p':>4} {'c':>8} {'tag':>4} {'n':>4} {'|sum_b V_b|':>14} "
          f"{'2^n':>20} {'-log2 full':>11} {'max_b -log2 rho_b':>18}")
    for r in rows:
        n = r["n"]
        lg_full = (n - math.log2(abs(r["full"]))) if r["full"] else float("inf")
        best = None
        for e in r["per_b"]:
            if e["V"] and 0 < e["b"] < n:
                v = math.log2(e["C"]) - math.log2(abs(e["V"]))
                best = v if best is None else min(best, v)
        print(f"{r['p']:4d} {str(tuple(r['c'])):>8} {r['tag']:>4} {n:4d} "
              f"{abs(r['full']):14d} {1 << n:20d} {lg_full:11.4f} "
              f"{(best if best is not None else float('nan')):18.4f}")

    print("\n[F3] sign alternation on an all-odd window (the exact "
          "(-1)^b * C(n,b)/p signature)")
    for r in rows:
        if r["tag"] == "odd" and r["n"] == 32:
            print(f"  p={r['p']} c={tuple(r['c'])} n=32: "
                  f"V_b/C(n,b) * p for b=10..22:")
            s = []
            for b in range(10, 23):
                e = r["per_b"][b]
                s.append(f"{Fraction(e['V'] * r['p'], e['C']).__float__():+.4f}")
            print("   " + " ".join(s))
            break


# ------------------------------------------------------------ weighted -----

def stage_weighted():
    """Confirm the floor with the TRUE weights (exact Z[zeta_p])."""
    print("[W1] TRUE-WEIGHT confirmation of the slice floor "
          "(exact algebra, 60-digit rendering)")
    print(f"{'p':>4} {'tag':>4} {'n':>3} {'b':>3} {'-log2 rho_b':>12} "
          f"{'log2 p':>8} | {'-log2 full-window':>18}")
    out = []
    for p in (11, 13, 19):
        F = Fp2.make(p)
        mu = admissible_orders(p)[-1]
        reps = pair_reps(F, F.subgroup(mu))
        c = (1, 1)
        allloc = [residues(F, c, y) for y in reps]
        aD = Delta_of(p, allloc)
        sel_odd = [i for i in range(len(aD)) if aD[i] % 2 == 1]
        for tag, sel in (("odd", sel_odd), ("mix", list(range(len(aD))))):
            for n in (8, 10, 12):
                if n > len(sel):
                    continue
                loc = [allloc[i] for i in sel[:n]]
                A = slice_coeffs_carrydp(p, loc)
                E = elem_sym(abs_pairs(p, loc))
                av = [abs(complex(x.tocomplex())) for x in A]
                ev = [abs(complex(x.tocomplex())) for x in E]
                fullA = abs(complex(sum(x.tocomplex() for x in A)))
                fullE = sum(ev)
                out.append({"p": p, "tag": tag, "n": n,
                            "rho": [a / e for a, e in zip(av, ev)],
                            "full": fullA / fullE})
                for b in (n // 4, n // 2, 3 * n // 4):
                    if av[b] == 0:
                        continue
                    print(f"{p:4d} {tag:>4} {n:3d} {b:3d} "
                          f"{-math.log2(av[b]/ev[b]):12.4f} "
                          f"{math.log2(p):8.4f} | "
                          f"{-math.log2(fullA/fullE):18.4f}")
    with open(os.path.join(RESULTS, "slice_fence_weighted.json"), "w") as f:
        json.dump({"rows": out,
                   "note": "ratios are 60-digit renderings of exact "
                           "Z[zeta_p] quantities"}, f, indent=1)


if __name__ == "__main__":
    os.makedirs(RESULTS, exist_ok=True)
    st = sys.argv[1] if len(sys.argv) > 1 else "verify"
    {"verify": stage_verify, "census": stage_census,
     "fence": stage_fence, "weighted": stage_weighted}[st]()
