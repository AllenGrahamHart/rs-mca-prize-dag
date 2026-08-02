#!/usr/bin/env python3
"""Exact verification of the split-section one-packet theorem (PK1).

Theorem under test (see REPORT text).  Row: H = roots of Z^n - beta in F_q,
|H| = n, C = RS[F_q, H, k], r = n-k-1, a = k+1.  Received word

    U_c = X^(n-1) + c X^k      (any codeword shift and any nonzero scaling
                                gives the same shells)

(A) c != 0 => no codeword agrees with U_c in >= k+2 places.
(B) c  = 0 => no codeword agrees with U_c in >= k+1 places (the rank-one
    fence: same homogeneous Toeplitz row, empty fibre).
(C) c != 0 and c^n = beta^r  => the exact shell at k+1 is the packet
        Pi = { P_T : T subset H, |T| = r, prod T = (-1)^(r+1) c }
    with the closed form
        P_T = [ c X^k (M - X^r) + beta (M + c)/X ] / M,     M = prod_{x in T}(X-x)
    and T -> P_T is a bijection.
(D) if in addition gcd(r,n) = 1 then |Pi| = C(n,r)/n exactly, independent of
    q, beta and c.
(E) index-set form: fixing H = (x0 omega^i)_i, the packet of the word with
    c = (-1)^(r+1) x0^r omega^s is exactly { T subset Z/n : |T| = r, sum T = s },
    the SAME index family for every admissible (q, beta, generator choice).

Everything below is brute force and independent of the proof: shells are
computed by interpolating every k-subset.

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
RECORD: dict = {"theorem": "PK1", "fixtures": []}


def check(name: str, cond: bool, detail: str = "") -> None:
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f" :: {detail}" if detail else ""))
    if not cond:
        FAILURES.append(name)


# ---------------------------------------------------------------------------
def packet_closed_form(F, n, k, beta, c, T):
    """P_T = [ c X^k (M - X^r) + beta (M + c)/X ] / M ; returns (P, ok_div)."""
    r = n - k - 1
    M = locator(F, T)
    Xr = [F.zero] * r + [F.one]
    Xk = [F.zero] * k + [F.one]
    term1 = poly_mul(F, Xk, poly_sub(F, M, Xr))
    term1 = [F.mul(c, t) for t in term1]
    Mplusc = list(M)
    Mplusc[0] = F.add(Mplusc[0], c)
    check_const = (Mplusc[0] == F.zero)
    shifted = poly_trim(F, Mplusc[1:]) if len(Mplusc) > 1 else [F.zero]
    term2 = [F.mul(beta, t) for t in shifted]
    num = poly_trim(F, [F.add(x, y) for x, y in zip(
        term1 + [F.zero] * max(0, len(term2) - len(term1)),
        term2 + [F.zero] * max(0, len(term1) - len(term2)))])
    Q, rem = poly_divmod(F, num, M)
    ok = (len(rem) == 1 and rem[0] == F.zero) and check_const
    return poly_trim(F, Q), ok


def subset_product(F, T):
    out = F.one
    for x in T:
        out = F.mul(out, x)
    return out


def run_row(F, n, k, beta, s_values, label, do_closed_form=True,
            record_key=None):
    """Full exact check of PK1 for one (field, beta) row."""
    r = n - k - 1
    dom = domain(F, n, beta)
    if dom is None:
        return None
    H, omega, x0 = dom
    idx = {x: i for i, x in enumerate(H)}
    guard = (gcd(r, n) == 1)
    predicted_top = comb(n, r) // n if guard else None
    # the section condition is m_0 = -c, i.e. prod T = (-1)^(r+1) c
    sign = F.one if (r + 1) % 2 == 0 else F.neg(F.one)
    x0r = F.power(x0, r)

    out = []
    for s in s_values:
        c = F.mul(F.mul(sign, x0r), F.power(omega, s))
        U = [F.zero] * n
        U[n - 1] = F.one
        U[k] = c
        Uvals = [poly_eval(F, U, x) for x in H]
        shells, cw = exact_shell_census(F, H, k, Uvals)

        top = shells.get(k + 1, 0)
        above = sum(v for b, v in shells.items() if b >= k + 2)
        base = shells.get(k, 0)
        conservation = sum(comb(b, k) * v for b, v in shells.items())

        check(f"{label} s={s}: ceiling, no agreement >= k+2", above == 0,
              f"shells={dict(sorted(shells.items()))}")
        if guard:
            check(f"{label} s={s}: |Pi| = C(n,r)/n = {predicted_top}",
                  top == predicted_top, f"observed={top}")
            check(f"{label} s={s}: exact shell at k equals "
                  f"C(n,k)-(k+1)C(n,k+1)/n",
                  base == comb(n, k) - (k + 1) * predicted_top,
                  f"observed={base}")
        check(f"{label} s={s}: k-subset conservation identity",
              conservation == comb(n, k), f"sum={conservation}")

        # index-set form (E)
        observed_idx = set()
        for P, agree in cw.items():
            if len(agree) == k + 1:
                T = frozenset(set(range(n)) - set(agree))
                observed_idx.add(tuple(sorted(T)))
        expected_idx = set(t for t in combinations(range(n), r)
                           if sum(t) % n == s % n)
        check(f"{label} s={s}: packet index family = "
              f"{{T : |T|={r}, sum T = {s} mod {n}}}",
              observed_idx == expected_idx,
              f"|obs|={len(observed_idx)} |exp|={len(expected_idx)}")

        # subset-product form (C) and closed form
        prod_ok = True
        form_ok = True
        for P, agree in cw.items():
            if len(agree) != k + 1:
                continue
            T = [H[i] for i in sorted(set(range(n)) - set(agree))]
            gamma = subset_product(F, T)
            if gamma != F.mul(sign, c):  # prod T = (-1)^(r+1) c
                prod_ok = False
            if do_closed_form:
                PT, okdiv = packet_closed_form(F, n, k, beta, c, T)
                if not okdiv or tuple(PT) != tuple(poly_trim(F, list(P))):
                    form_ok = False
        check(f"{label} s={s}: every packet member has prod T = (-1)^(r+1) c",
              prod_ok)
        if do_closed_form:
            check(f"{label} s={s}: closed-form template reproduces every member",
                  form_ok)

        out.append({"s": s, "shells": {str(b): v for b, v in
                                       sorted(shells.items())},
                    "top": top, "index_family_size": len(observed_idx)})

    if record_key:
        RECORD["fixtures"].append(
            {"key": record_key, "field": F.name, "q": F.q, "n": n, "k": k,
             "r": r, "gcd_guard": guard, "predicted_top": predicted_top,
             "rows": out})
    return out


# ---------------------------------------------------------------------------
def v1_small_row():
    """n=8, k=4 (rate 1/2, r=3, gcd(3,8)=1): all s, several q, both beta."""
    print("\n=== V1  n=8, k=4, r=3  (gcd(3,8)=1) ===")
    n, k = 8, 4
    fields = [PrimeField(17), PrimeField(41), PrimeField(73),
              PrimeField(89), PrimeField(97), PrimeField(113),
              ExtField(3, 2), ExtField(5, 2), ExtField(7, 2)]
    for F in fields:
        betas = sorted({F.power(x, n) for x in F.units()}, key=F.key)
        for beta in betas[:2]:
            run_row(F, n, k, beta, list(range(n)),
                    f"V1 {F.name} beta={beta}",
                    record_key=f"V1:{F.name}:beta={beta}")


def v1b_index_family_across_fields():
    """(E) the SAME index family appears in every field: cross-field equality."""
    print("\n=== V1b  cross-field identity of the packet index family ===")
    n, k, r = 8, 4, 3
    families = {}
    for F in [PrimeField(17), PrimeField(41), PrimeField(97), ExtField(3, 2)]:
        H, omega, x0 = domain(F, n, F.one)
        fam = {}
        for s in range(n):
            sign = F.one if (r + 1) % 2 == 0 else F.neg(F.one)
            c = F.mul(F.mul(sign, F.power(x0, r)), F.power(omega, s))
            U = [F.zero] * n
            U[n - 1] = F.one
            U[k] = c
            Uvals = [poly_eval(F, U, x) for x in H]
            _, cw = exact_shell_census(F, H, k, Uvals)
            fam[s] = frozenset(
                tuple(sorted(set(range(n)) - set(a)))
                for P, a in cw.items() if len(a) == k + 1)
        families[F.name] = fam
    names = list(families)
    ref = families[names[0]]
    same = all(families[nm] == ref for nm in names[1:])
    check("V1b index families identical across F_17,F_41,F_97,F_9",
          same, f"fields={names}")
    RECORD["cross_field_index_family"] = {
        str(s): sorted(list(t) for t in ref[s]) for s in ref}


def v2_medium_row():
    """n=16, k=8 (r=7, gcd(7,16)=1): heavier census, fewer words."""
    print("\n=== V2  n=16, k=8, r=7  (gcd(7,16)=1) ===")
    n, k = 16, 8
    for F in [PrimeField(17), PrimeField(97), PrimeField(113)]:
        run_row(F, n, k, F.one, [0, 1], f"V2 {F.name}",
                do_closed_form=True, record_key=f"V2:{F.name}")


def v3_official_row_arithmetic():
    """Exact integer arithmetic for the official razor row."""
    print("\n=== V3  official razor-row instantiation (exact integers) ===")
    n, k = 2 ** 41, 2 ** 40
    r = n - k - 1
    check("V3 razor row is rate 1/2", n == 2 * k)
    check("V3 equidistribution guard gcd(r,n)=1 holds at the razor row",
          gcd(r, n) == 1, f"r={r}, n={n}")
    # |Pi| = C(n,r)/n is a ~2^41-bit integer: certify > 2^128 by a poly-size
    # chain, never by writing the integer.
    # C(n, n/2-1) = C(n, n/2) * (n/2) / (n/2+1) >= C(n,n/2)/2 >= 2^n/(2(n+1)).
    # so |Pi| >= 2^n / (2 n (n+1)).
    lower_log2 = n - 1 - (n + 1).bit_length() - n.bit_length()
    check("V3 |Pi| >= 2^n/(2n(n+1)) exceeds every prize budget B* < 2^128",
          lower_log2 > 128, f"log2 lower bound = {lower_log2}")
    # verify the chain exactly at small n
    ok = True
    for m in range(6, 220, 2):
        val = comb(m, m // 2 - 1) // m
        if not (val * 2 * m * (m + 1) >= 2 ** m):
            ok = False
    check("V3 the poly-size bound chain |Pi|*2n(n+1) >= 2^n verified "
          "exactly for all even n in [6,218]", ok)
    # smallest rate-1/2 row (k even) with |Pi| > 2^128
    smallest = None
    for kk in range(2, 400, 2):
        nn = 2 * kk
        if comb(nn, nn - kk - 1) // nn > 2 ** 128:
            smallest = (nn, kk)
            break
    check("V3 smallest rate-1/2 packet row with |Pi| > 2^128 is n=140",
          smallest == (140, 70), f"smallest={smallest}")
    # frontier accounting: our agreement vs the banked staircase
    a_packet = k + 1
    a_staircase_lowest_tier = 3 * n // 4 - 1
    a_cap_uniform = k + 2 ** 34 - 1
    check("V3 packet agreement k+1 is far BELOW the banked unsafe frontier",
          a_packet < a_cap_uniform < a_staircase_lowest_tier,
          f"k+1={a_packet} < k+2^34-1={a_cap_uniform} < 3n/4-1="
          f"{a_staircase_lowest_tier}")
    RECORD["official_row"] = {
        "n": n, "k": k, "r": r, "gcd_guard": gcd(r, n) == 1,
        "log2_lower_bound_on_packet": lower_log2,
        "a_packet": a_packet, "a_cap_uniform_floor": a_cap_uniform,
        "a_lowest_staircase_tier": a_staircase_lowest_tier,
        "frontier_movement": 0}


def main():
    v1_small_row()
    v1b_index_family_across_fields()
    v2_medium_row()
    v3_official_row_arithmetic()
    os.makedirs(CKPT, exist_ok=True)
    with open(os.path.join(CKPT, "packet_theorem.json"), "w") as fh:
        json.dump(RECORD, fh, indent=1, sort_keys=True)
    print()
    if FAILURES:
        print("FAILURES:", FAILURES)
        print("PK1_VERIFICATION_FAIL")
        raise SystemExit(1)
    print("PK1_VERIFICATION_PASS")


if __name__ == "__main__":
    main()
