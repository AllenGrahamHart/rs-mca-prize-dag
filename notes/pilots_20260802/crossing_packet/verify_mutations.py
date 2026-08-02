#!/usr/bin/env python3
"""Mutation suite for the split-section one-packet theorem PK1.

Each mutation drops exactly one hypothesis of PK1 and exhibits an exact,
replayable witness that some part of the conclusion fails.  Every fixture is
self-contained: it names the row, the received word, the mutated hypothesis,
the exact observed data, and the moral.

Run:  tools/ramguard local -- python3 <this file>
"""
from __future__ import annotations

import json
import os
import sys
from itertools import combinations
from math import comb, gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from packet_lib import (  # noqa: E402
    ExtField,
    PrimeField,
    domain,
    exact_shell_census,
    interpolate,
    locator,
    poly_divmod,
    poly_eval,
    poly_mul,
    poly_sub,
    poly_trim,
)

HERE = os.path.dirname(os.path.abspath(__file__))
CKPT = os.path.join(HERE, "checkpoints")
FAILURES: list[str] = []
MUT: dict = {}


def check(name: str, cond: bool, detail: str = "") -> None:
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f" :: {detail}" if detail else ""))
    if not cond:
        FAILURES.append(name)


def word_shells(F, H, n, k, terms):
    U = [F.zero] * n
    for d, c in terms.items():
        U[d] = c
    Uvals = [poly_eval(F, U, x) for x in H]
    return exact_shell_census(F, H, k, Uvals) + (U,)


def subset_product(F, T):
    out = F.one
    for x in T:
        out = F.mul(out, x)
    return out


def subset_sum(F, T):
    out = F.zero
    for x in T:
        out = F.add(out, x)
    return out


# ---------------------------------------------------------------------------
# M1  affine target dropped  (the rank-one Toeplitz fence)
# ---------------------------------------------------------------------------
def m1_rank_one_fence():
    print("\n=== M1  drop the affine target (c=0): the rank-one Toeplitz fence ===")
    rec = []
    for (p, n, k) in [(17, 8, 4), (97, 8, 4), (17, 16, 8), (97, 16, 8)]:
        F = PrimeField(p)
        H, omega, x0 = domain(F, n, F.one)
        r = n - k - 1
        sign = F.one if (r + 1) % 2 == 0 else F.neg(F.one)
        c = F.mul(sign, F.power(x0, r))            # realizable target, s=0
        shells_c, _, U_c = word_shells(F, H, n, k, {n - 1: F.one, k: c})
        shells_0, _, U_0 = word_shells(F, H, n, k, {n - 1: F.one})
        row_c = tuple(U_c[n - 1 - j] for j in range(r + 1))
        row_0 = tuple(U_0[n - 1 - j] for j in range(r + 1))
        hom_c, hom_0 = row_c[:r], row_0[:r]        # coefficients of m_0..m_{r-1}
        check(f"M1 q={p} n={n}: identical homogeneous Toeplitz row",
              hom_c == hom_0, f"hom={hom_c}")
        check(f"M1 q={p} n={n}: fibre jumps C(n,r)/n -> 0 when the affine "
              f"target vanishes",
              shells_c.get(k + 1, 0) == comb(n, r) // n
              and shells_0.get(k + 1, 0) == 0
              and max(shells_0) == k,
              f"c!=0 shell_{k+1}={shells_c.get(k+1,0)}, "
              f"c=0 shells={dict(sorted(shells_0.items()))}")
        rec.append({"q": p, "n": n, "k": k, "homogeneous_row": list(hom_c),
                    "shell_k1_c_nonzero": shells_c.get(k + 1, 0),
                    "shell_k1_c_zero": shells_0.get(k + 1, 0),
                    "shells_c_zero": {str(b): v
                                      for b, v in sorted(shells_0.items())}})
    MUT["M1_rank_one_fence"] = rec


# ---------------------------------------------------------------------------
# M2  realizability dropped: c != 0 but c^n != beta^r
# ---------------------------------------------------------------------------
def m2_unrealizable_target():
    print("\n=== M2  drop realizability (c^n != beta^r) ===")
    rec = []
    for (p, n, k) in [(17, 8, 4), (97, 8, 4), (113, 16, 8)]:
        F = PrimeField(p)
        H, omega, x0 = domain(F, n, F.one)
        r = n - k - 1
        bad = None
        for cand in F.units():
            if F.power(cand, n) != F.power(F.one, r):
                bad = cand
                break
        if bad is None:
            continue
        shells, _, _ = word_shells(F, H, n, k, {n - 1: F.one, k: bad})
        check(f"M2 q={p} n={n} c={bad}: unrealizable target => empty packet",
              shells.get(k + 1, 0) == 0 and max(shells) == k,
              f"shells={dict(sorted(shells.items()))}")
        rec.append({"q": p, "n": n, "k": k, "c": bad,
                    "shells": {str(b): v for b, v in sorted(shells.items())}})
    MUT["M2_unrealizable_target"] = rec


# ---------------------------------------------------------------------------
# M3  equidistribution guard dropped: gcd(r,n) != 1
# ---------------------------------------------------------------------------
def m3_gcd_guard_dropped():
    print("\n=== M3  drop the equidistribution guard gcd(r,n)=1 (rate 1/2, k odd) ===")
    n, k = 10, 5
    r = n - k - 1                                    # 4, gcd(4,10)=2
    check("M3 the guard genuinely fails at n=10,k=5", gcd(r, n) == 2,
          f"gcd({r},{n})={gcd(r,n)}")
    naive = comb(n, r) // n                          # 21, the guarded formula
    rec = []
    for p in [11, 31, 41, 61, 71, 101]:
        F = PrimeField(p)
        H, omega, x0 = domain(F, n, F.one)
        sign = F.one if (r + 1) % 2 == 0 else F.neg(F.one)
        profile = {}
        for s in range(n):
            c = F.mul(F.mul(sign, F.power(x0, r)), F.power(omega, s))
            shells, _, _ = word_shells(F, H, n, k, {n - 1: F.one, k: c})
            profile[s] = shells.get(k + 1, 0)
            if max(shells) > k + 1:
                check(f"M3 q={p}: ceiling survives the guard drop", False)
        values = sorted(set(profile.values()))
        check(f"M3 q={p}: |shell(k+1)| is gamma-DEPENDENT, not C(n,r)/n={naive}",
              len(values) > 1 and naive not in values,
              f"profile={profile}")
        rec.append({"q": p, "n": n, "k": k, "r": r,
                    "guarded_formula_would_be": naive,
                    "observed_by_gamma_index": profile})
    same = all(x["observed_by_gamma_index"] == rec[0]["observed_by_gamma_index"]
               for x in rec)
    check("M3 the split profile is still q-INDEPENDENT (only the single "
          "formula dies, not q-independence)", same)
    MUT["M3_gcd_guard_dropped"] = rec


# ---------------------------------------------------------------------------
# M4  the very next section (w=2): q-DEPENDENCE
# ---------------------------------------------------------------------------
def section_w2_counts(F, H, n, k):
    """{T : |T| = n-k-2, e_1(T) = 0, prod T = gamma} counted per gamma."""
    r2 = n - k - 2
    out = {}
    for T in combinations(H, r2):
        if subset_sum(F, T) != F.zero:
            continue
        g = subset_product(F, T)
        out[g] = out.get(g, 0) + 1
    return out


def m4_next_section_q_dependence():
    print("\n=== M4  the very next section (w=2, a=k+2) is q-DEPENDENT ===")
    n, k = 16, 8
    r1, r2 = n - k - 1, n - k - 2
    primes = [17, 97, 113, 193, 241, 257, 337, 353, 401, 433, 449, 577,
              593, 641, 673, 769, 881, 929, 977]
    rec = []
    for p in primes:
        F = PrimeField(p)
        H, omega, x0 = domain(F, n, F.one)
        counts = section_w2_counts(F, H, n, k)
        total = sum(counts.values())
        rec.append({"q": p, "total_zero_sum_6subsets": total,
                    "max_per_gamma": max(counts.values()) if counts else 0,
                    "distinct_gamma": len(counts)})
    F81 = ExtField(3, 4)
    H, omega, x0 = domain(F81, n, F81.one)
    counts81 = section_w2_counts(F81, H, n, k)
    rec.append({"q": 81, "total_zero_sum_6subsets": sum(counts81.values()),
                "max_per_gamma": max(counts81.values()) if counts81 else 0,
                "distinct_gamma": len(counts81)})
    totals = sorted({x["total_zero_sum_6subsets"] for x in rec})
    check("M4 the w=2 section fibre count VARIES with q "
          "(the packet bound is q-dependent one step up)",
          len(totals) > 1, f"observed totals={totals}")
    structured = comb(n // 2, r2 // 2) * 1   # r2/2 antipodal pairs
    check("M4 every q admits at least the structured antipodal solutions "
          f"C(8,3)={structured}",
          all(x["total_zero_sum_6subsets"] >= structured for x in rec),
          f"min={min(x['total_zero_sum_6subsets'] for x in rec)}")
    # control: the w=1 pure-product count does NOT vary
    control = []
    for p in primes[:8]:
        F = PrimeField(p)
        H, omega, x0 = domain(F, n, F.one)
        cnt = {}
        for T in combinations(H, r1):
            g = subset_product(F, T)
            cnt[g] = cnt.get(g, 0) + 1
        control.append(sorted(set(cnt.values())))
    check("M4 control: the w=1 pure-product fibre is constant = C(n,r)/n = "
          f"{comb(n, r1) // n} at every q",
          all(cv == [comb(n, r1) // n] for cv in control),
          f"observed={sorted({tuple(cv) for cv in control})}")
    MUT["M4_w2_q_dependence"] = {"rows": rec,
                                 "structured_lower_bound": structured,
                                 "w1_control": comb(n, r1) // n}


def m4b_w2_full_census():
    """Confirm the section count IS the exact shell (gcd guard) at w=2."""
    print("\n=== M4b  w=2 full exact-shell census at two fields ===")
    n, k = 16, 8
    rec = []
    for p in [17, 97]:
        F = PrimeField(p)
        H, omega, x0 = domain(F, n, F.one)
        r2 = n - k - 2
        counts = section_w2_counts(F, H, n, k)
        # pick the gamma with the largest section fibre and build its word
        gamma, best = max(counts.items(), key=lambda kv: kv[1])
        # prod T = (-1)^(r2+1) c  =>  c = (-1)^(r2+1) gamma
        sgn = F.one if (r2 + 1) % 2 == 0 else F.neg(F.one)
        c = F.mul(sgn, gamma)
        shells, cw, U = word_shells(F, H, n, k, {n - 1: F.one, k + 1: c})
        check(f"M4b q={p}: exact shell at k+2 equals the w=2 section fibre",
              shells.get(k + 2, 0) == best,
              f"shell={shells.get(k+2,0)} section={best}")
        check(f"M4b q={p}: ceiling at k+2 (nothing at k+3 or above)",
              max(shells) <= k + 2, f"shells={dict(sorted(shells.items()))}")
        check(f"M4b q={p}: k-subset conservation identity",
              sum(comb(b, k) * v for b, v in shells.items()) == comb(n, k))
        rec.append({"q": p, "shells": {str(b): v
                                       for b, v in sorted(shells.items())},
                    "w2_section_fibre": best})
    check("M4b the w=2 exact shell differs between q=17 and q=97",
          rec[0]["shells"].get(str(k + 2)) != rec[1]["shells"].get(str(k + 2)),
          f"{rec[0]['shells'].get(str(k+2))} vs {rec[1]['shells'].get(str(k+2))}")
    MUT["M4b_w2_full_census"] = rec


# ---------------------------------------------------------------------------
# M5  drop splitness: the affine section is not the fibre
# ---------------------------------------------------------------------------
def m5_split_variety():
    print("\n=== M5  drop splitness: affine section vs split-divisor fibre ===")
    p, n, k = 17, 8, 4
    F = PrimeField(p)
    H, omega, x0 = domain(F, n, F.one)
    r = n - k - 1
    sign = F.one if (r + 1) % 2 == 0 else F.neg(F.one)
    c = F.mul(sign, F.power(x0, r))
    beta = F.one
    Xr = [F.zero] * r + [F.one]
    Xk = [F.zero] * k + [F.one]
    section_points, packet_points, div_ok = 0, 0, 0
    non_split_witness = None
    for tail in combinations(range(p), 0):
        pass
    for m0 in [F.neg(c)]:
        for m1 in range(p):
            for m2 in range(p):
                M = [m0, m1, m2, F.one]
                section_points += 1
                term1 = [F.mul(c, t) for t in
                         poly_mul(F, Xk, poly_sub(F, M, Xr))]
                Mplusc = list(M)
                Mplusc[0] = F.add(Mplusc[0], c)
                term2 = [F.mul(beta, t) for t in poly_trim(F, Mplusc[1:])]
                L = max(len(term1), len(term2))
                num = poly_trim(F, [F.add(term1[i] if i < len(term1) else F.zero,
                                          term2[i] if i < len(term2) else F.zero)
                                    for i in range(L)])
                _, rem = poly_divmod(F, num, M)
                exact = (len(rem) == 1 and rem[0] == F.zero)
                # is M split squarefree over H?
                roots = [x for x in H if poly_eval(F, M, x) == F.zero]
                split = (len(roots) == r)
                if split:
                    packet_points += 1
                if exact:
                    div_ok += 1
                if exact and not split:
                    non_split_witness = list(M)
    check("M5 the affine section has q^(r-1) points",
          section_points == p ** (r - 1), f"{section_points} = {p}^{r-1}")
    check(f"M5 only C(n,r)/n = {comb(n, r) // n} of them are split divisors",
          packet_points == comb(n, r) // n, f"split={packet_points}")
    check("M5 divisibility (hence a codeword) holds exactly on the split "
          "points; no linear-algebra proxy exists",
          div_ok == packet_points and non_split_witness is None,
          f"divisible={div_ok}, non-split divisible witness="
          f"{non_split_witness}")
    MUT["M5_split_variety"] = {"q": p, "n": n, "k": k, "r": r,
                               "affine_section_points": section_points,
                               "split_points": packet_points,
                               "divisible_points": div_ok,
                               "ratio_section_over_packet":
                                   section_points // max(1, packet_points)}


# ---------------------------------------------------------------------------
# M6  drop the exactness (gcd) guard: sections count subsets, not codewords
# ---------------------------------------------------------------------------
def m6_exactness_guard():
    print("\n=== M6  drop the exactness guard gcd(Q,M)=1 (w=0 shell at a=k) ===")
    p, n, k = 17, 8, 4
    F = PrimeField(p)
    H, omega, x0 = domain(F, n, F.one)
    r = n - k - 1
    sign = F.one if (r + 1) % 2 == 0 else F.neg(F.one)
    c = F.mul(sign, F.power(x0, r))
    U = [F.zero] * n
    U[n - 1] = F.one
    U[k] = c
    Uvals = [poly_eval(F, U, x) for x in H]
    guard_fail, guard_ok = 0, 0
    mismatch = 0
    for idxs in combinations(range(n), k):
        A = [H[i] for i in idxs]
        comp = [H[i] for i in range(n) if i not in idxs]
        M = locator(F, comp)
        L = locator(F, A)
        P = interpolate(F, A, [Uvals[i] for i in idxs])
        UmP = poly_sub(F, U, P)
        Q, rem = poly_divmod(F, UmP, L)
        assert len(rem) == 1 and rem[0] == F.zero
        bad_roots = [x for x in comp if poly_eval(F, Q, x) == F.zero]
        agree = sum(1 for i in range(n)
                    if poly_eval(F, P, H[i]) == Uvals[i])
        if bad_roots:
            guard_fail += 1
            if agree == k:
                mismatch += 1
        else:
            guard_ok += 1
            if agree != k:
                mismatch += 1
    check("M6 the unguarded w=0 section has C(n,k)=70 members",
          guard_ok + guard_fail == comb(n, k))
    check("M6 the guard fails on exactly half of them (35), and failure is "
          "equivalent to agreement > k",
          guard_fail == 35 and guard_ok == 35 and mismatch == 0,
          f"guard_fail={guard_fail} guard_ok={guard_ok} mismatch={mismatch}")
    check("M6 the 35 guard failures are the (k+1)-choose-k re-countings of "
          "the 7 packet members",
          guard_fail == (k + 1) * (comb(n, r) // n))
    MUT["M6_exactness_guard"] = {"q": p, "n": n, "k": k,
                                 "section_members": guard_ok + guard_fail,
                                 "guard_fail": guard_fail,
                                 "guard_ok": guard_ok,
                                 "packet_recount": (k + 1) * (comb(n, r) // n)}


# ---------------------------------------------------------------------------
# M7  per-shell caps do not compose
# ---------------------------------------------------------------------------
def m7_cumulative():
    print("\n=== M7  per-shell caps do not compose (cumulative discipline) ===")
    p, n, k = 17, 8, 4
    F = PrimeField(p)
    H, omega, x0 = domain(F, n, F.one)
    r = n - k - 1
    sign = F.one if (r + 1) % 2 == 0 else F.neg(F.one)
    c = F.mul(sign, F.power(x0, r))
    shells, _, _ = word_shells(F, H, n, k, {n - 1: F.one, k: c})
    top = shells.get(k + 1, 0)
    cum_k = sum(v for b, v in shells.items() if b >= k)
    check("M7 shell(k+1)=7 but the threshold list at a=k is 42",
          top == 7 and cum_k == 42, f"shells={dict(sorted(shells.items()))}")
    check("M7 the packet theorem IS a threshold theorem at a=k+1 only "
          "because the ceiling makes higher shells empty",
          sum(v for b, v in shells.items() if b >= k + 1) == top)
    MUT["M7_cumulative"] = {"shells": {str(b): v
                                       for b, v in sorted(shells.items())},
                            "threshold_at_k": cum_k,
                            "threshold_at_k1": top}


# ---------------------------------------------------------------------------
# M8  the F_17 three-codeword same-word trap
# ---------------------------------------------------------------------------
def m8_f17_trap():
    print("\n=== M8  the Brief-6 F_17 three-codeword same-word trap ===")
    p, n, k, d = 17, 16, 8, 4
    F = PrimeField(p)
    H, omega, x0 = domain(F, n, F.one)
    zeta = omega
    i_unit = F.power(zeta, d)
    check("M8 F_17 toy: i^2 = -1", F.mul(i_unit, i_unit) == F.neg(F.one),
          f"i={i_unit}")
    fibers: dict = {}
    for x in H:
        fibers.setdefault(F.power(x, d), []).append(x)
    minus_i = F.neg(i_unit)
    x_drop = min(fibers[minus_i])
    G = locator(F, [x for x in fibers[minus_i] if x != x_drop])
    y_minus = [F.neg(F.one)] + [F.zero] * 3 + [F.one]     # X^4 - 1
    y_plus = [F.one] + [F.zero] * 3 + [F.one]             # X^4 + 1
    c0 = [F.zero]
    c1 = poly_mul(F, G, y_minus)
    c2 = [F.mul(i_unit, t) for t in poly_mul(F, G, y_plus)]
    received = {}
    for x in H:
        y = F.power(x, d)
        received[x] = (poly_eval(F, c1, x) if y == i_unit else F.zero)
    Uvals = [received[x] for x in H]
    agr = [sum(1 for x in H if poly_eval(F, cw, x) == received[x])
           for cw in (c0, c1, c2)]
    check("M8 the three-codeword witness reproduces agreements 12/11/11",
          sorted(agr, reverse=True) == [12, 11, 11], f"agreements={agr}")
    shells, cwmap = exact_shell_census(F, H, k, Uvals)
    check("M8 conservation identity holds for the trap word",
          sum(comb(b, k) * v for b, v in shells.items()) == comb(n, k),
          f"shells={dict(sorted(shells.items()))}")
    U = interpolate(F, H, Uvals)
    U = U + [F.zero] * (n - len(U))
    window = [U[n - 1 - j] for j in range(n - k)]
    pure = (window[0] != F.zero
            and all(w == F.zero for w in window[1:-1]))
    check("M8 the trap word's shell-(k+1) window is NOT pure-product, so PK1 "
          "does not apply to it", not pure, f"window={window}")
    check("M8 the trap lives ABOVE the packet ceiling: its top shell is 12, "
          "PK1 words have top shell k+1=9",
          max(shells) == 12, f"top_shell={max(shells)}")
    check("M8 the trap sits at the Johnson anchor 3n/4 and its predecessor, "
          "not at the packet agreement k+1",
          agr[0] == 3 * n // 4 and agr[1] == 3 * n // 4 - 1
          and k + 1 == 9, f"3n/4={3*n//4}, k+1={k+1}")
    check("M8 lift obligation (degree cap) is TIGHT at the toy: "
          "deg(G*(X^d-1)) = 2d-1 = 7 < k = 8",
          (len(c1) - 1) == 2 * d - 1 and 2 * d - 1 == k - 1,
          f"deg c1={len(c1)-1}, k={k}")
    MUT["M8_f17_trap"] = {"q": p, "n": n, "k": k, "agreements": agr,
                          "shells": {str(b): v
                                     for b, v in sorted(shells.items())},
                          "window_top_to_bottom": window,
                          "pure_product_window": pure}


# ---------------------------------------------------------------------------
# M9  succinctness killer: a generic w=1 window
# ---------------------------------------------------------------------------
def m9_succinctness():
    print("\n=== M9  generic w=1 window: the certificate must enumerate ===")
    n, k = 8, 4
    rec = {}
    for p in [17, 41, 73, 89, 97, 113]:
        F = PrimeField(p)
        H, omega, x0 = domain(F, n, F.one)
        # q-free recipe: U = X^7 + X^6 + X^4 (all coefficients 0/1)
        shells, cw, _ = word_shells(F, H, n, k,
                                    {n - 1: F.one, n - 2: F.one, k: F.one})
        idxs = sorted(tuple(sorted(set(range(n)) - set(a)))
                      for P, a in cw.items() if len(a) == k + 1)
        rec[p] = {"shells": {str(b): v for b, v in sorted(shells.items())},
                  "packet_index_family": [list(t) for t in idxs]}
    sizes = {p: len(v["packet_index_family"]) for p, v in rec.items()}
    families = {p: {tuple(t) for t in v["packet_index_family"]}
                for p, v in rec.items()}
    check("M9 the generic-window fibre SIZE varies with q",
          len(set(sizes.values())) > 1, f"sizes={sizes}")
    check("M9 the generic-window fibre INDEX FAMILY varies with q "
          "(no q-free template exists; a certificate must enumerate)",
          len({frozenset(f) for f in families.values()}) > 1,
          f"families={ {p: sorted(map(list, f)) for p, f in families.items()} }")
    MUT["M9_succinctness"] = rec


def main():
    m1_rank_one_fence()
    m2_unrealizable_target()
    m3_gcd_guard_dropped()
    m4_next_section_q_dependence()
    m4b_w2_full_census()
    m5_split_variety()
    m6_exactness_guard()
    m7_cumulative()
    m8_f17_trap()
    m9_succinctness()
    os.makedirs(CKPT, exist_ok=True)
    with open(os.path.join(CKPT, "mutations.json"), "w") as fh:
        json.dump(MUT, fh, indent=1, sort_keys=True, default=str)
    print()
    if FAILURES:
        print("FAILURES:", FAILURES)
        print("MUTATION_SUITE_FAIL")
        raise SystemExit(1)
    print("MUTATION_SUITE_PASS")


if __name__ == "__main__":
    main()
