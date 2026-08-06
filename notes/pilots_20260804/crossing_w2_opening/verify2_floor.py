#!/usr/bin/env python3
"""Crossing w >= 2 -- round 2: resolve the three round-1 failures and build
the q-FREE STRUCTURAL FLOOR.

Profile: tiny. Pure python, deterministic, no third-party imports.

(CAL2) PK2's measured shells 30/9/7/8 vs the Lemma-X class-fibre SET.
       Round-1 "mismatches" were a choice-of-c artefact: PK2 fixes c, whose
       discrete-log class varies with the field. Lemma X predicts the shell
       takes exactly d = gcd(r',n) values; PK2's number must be one of them.
(Y2)   Corrected form: W_w SUBSET BCH_w unconditionally (Newton one way);
       equality when w <= p; the CONVERSE is FALSE (round-1 counterexample).
(FL)   The q-free structural floor: disjoint unions of PRIME-ORDER cosets
       (mixed moduli allowed) all satisfy e_1 = 0 in EVERY characteristic.
       Compare against the char-0 structural window and against MC-3.
"""

from itertools import combinations
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_crossing_w2 import (GF, window_set, bch_set, sig_profile,
                                lemma_x_ok, structural_window, gcd,
                                mc_shell_count)

FAILURES = []
CHECKS = [0]


def check(name, cond, detail=""):
    CHECKS[0] += 1
    if not cond:
        FAILURES.append((name, detail))
    return cond


def primes_of(n):
    out, m, d = [], n, 2
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def prime_cosets(n):
    """All cosets of mu_p inside Z/n, for p prime dividing n."""
    out = []
    for p in primes_of(n):
        step = n // p
        for i in range(step):
            out.append(frozenset((i + j * step) % n for j in range(p)))
    return sorted(set(out), key=lambda s: (len(s), sorted(s)))


def coset_union_sets(n, rp):
    """DISTINCT subsets of Z/n of size rp that are disjoint unions of
    prime-order cosets (mixed moduli allowed). Deduplicated as sets."""
    cos = prime_cosets(n)
    found = set()

    def rec(idx, cur, size):
        if size == rp:
            found.add(frozenset(cur))
            return
        if size > rp or idx == len(cos):
            return
        for j in range(idx, len(cos)):
            c = cos[j]
            if size + len(c) <= rp and not (cur & c):
                rec(j + 1, cur | c, size + len(c))

    rec(0, frozenset(), 0)
    return found


def main():
    print("=" * 78)
    print("CROSSING w >= 2 -- round 2: PK2 reconciliation + q-free floor")
    print("=" * 78)

    fields = {}

    def gf(p, e):
        if (p, e) not in fields:
            fields[(p, e)] = GF(p, e)
        return fields[(p, e)]

    # ------------------------------------------------ CAL2
    print("\n[CAL2] PK2 fixture n=16,k=8,w=2,r'=6: Lemma-X class fibres vs PK2")
    print("       Lemma X: the shell takes EXACTLY d = gcd(6,16) = 2 values.")
    pk2 = {17: 30, 81: 8, 97: 9, 241: 7, 257: 7}
    for q, want in sorted(pk2.items()):
        p, e = (3, 4) if q == 81 else (q, 1)
        F = gf(p, e)
        zp = F.powers(F.elem_of_order(16), 16)
        W = window_set(16, 6, 2, F, zp)
        prof = sig_profile(16, W)
        okx, d = lemma_x_ok(16, 6, prof)
        fib = sorted(set(prof[t] for t in range(16)))
        inset = want in fib
        check("CAL2 q=%d PK2 value is a Lemma-X fibre" % q, inset,
              "want %d fibres %s" % (want, fib))
        check("CAL2 q=%d lemmaX" % q, okx)
        print("       q=%-4d |W_2|=%-4d class fibres = %-10s  PK2's %-3d is a "
              "fibre: %s" % (q, len(W), str(fib), want, inset))

    # ------------------------------------------------ Y2
    print("\n[Y2] Newton one-way: W_w SUBSET BCH_w in EVERY characteristic")
    subs = []
    for (n, rp, w, p, e) in [(16, 6, 2, 17, 1), (16, 6, 3, 17, 1),
                             (16, 6, 3, 3, 4), (16, 6, 4, 3, 4),
                             (15, 5, 3, 2, 4), (15, 6, 3, 2, 4),
                             (21, 7, 3, 2, 6), (12, 5, 3, 13, 1),
                             (15, 5, 4, 2, 4), (16, 6, 4, 17, 1)]:
        F = gf(p, e)
        if (F.size - 1) % n:
            continue
        zp = F.powers(F.elem_of_order(n), n)
        A = set(window_set(n, rp, w, F, zp))
        B = set(bch_set(n, rp, w, F, zp))
        sub, eq, expect_eq = A.issubset(B), A == B, (w <= p)
        check("Y2 subset n=%d w=%d p=%d" % (n, w, p), sub,
              "|W|=%d |BCH|=%d" % (len(A), len(B)))
        if expect_eq:
            check("Y2 equality when w<=p n=%d w=%d p=%d" % (n, w, p), eq,
                  "|W|=%d |BCH|=%d" % (len(A), len(B)))
        subs.append((n, rp, w, p, len(A), len(B), sub, eq, expect_eq))
        print("     n=%2d r'=%d w=%d p=%2d |W|=%5d |BCH|=%5d subset=%s "
              "equal=%-5s w<=p=%-5s" % (n, rp, w, p, len(A), len(B), sub, eq,
                                        expect_eq))
    conv = [r for r in subs if r[7] and not r[8]]
    print("     -> W subset BCH in ALL %d cases (no char restriction)"
          % len(subs))
    print("     -> equality with w > p occurs (%d case(s)): the pre-registered"
          " 'iff' is REFUTED; only 'w <= p => equal' survives" % len(conv))
    for r in conv:
        print("        counterexample: n=%d r'=%d w=%d p=%d, |W|=|BCH|=%d"
              % (r[0], r[1], r[2], r[3], r[4]))

    # ------------------------------------------------ FL
    print("\n[FL] q-FREE STRUCTURAL FLOOR at w=2 (disjoint prime-coset unions)")
    print("     every such T has e_1(T) = 0 in EVERY characteristic")
    print("     %-14s %8s %8s %8s %8s %8s" % ("(n, r')", "cosetU", "char0",
                                              "equal?", "MC-3", "floor"))
    rows = [(12, 4), (12, 5), (12, 6), (15, 5), (15, 6), (16, 6), (16, 8),
            (18, 6), (20, 8), (21, 7)]
    for (n, rp) in rows:
        CU = coset_union_sets(n, rp)
        ST = set(frozenset(S) for S in structural_window(n, rp, 2))
        eq = (CU == ST)
        check("FL coset-unions subset char0 n=%d r'=%d" % (n, rp),
              CU.issubset(ST), "%d vs %d" % (len(CU), len(ST)))
        # MC-3 best single scale M
        best_mc3, best_M = 0, None
        for M in range(2, n + 1):
            if n % M or rp % M or 2 > M:
                continue
            N, m = n // M, rp // M
            if gcd(m, N) != 1:
                continue
            c = 1
            for i in range(m):
                c = c * (N - i) // (i + 1)
            if c % N == 0 and c // N > best_mc3:
                best_mc3, best_M = c // N, M
        d = gcd(rp, n)
        prof = [0] * n
        for S in CU:
            prof[sum(S) % n] += 1
        okx, _ = lemma_x_ok(n, rp, prof)
        check("FL lemmaX on coset unions n=%d r'=%d" % (n, rp), okx, str(prof))
        floor = max(prof)
        print("     n=%2d r'=%2d   %8d %8d %8s %8s %8d   (d=%d, MC-3 M=%s)"
              % (n, rp, len(CU), len(ST), eq, best_mc3, floor, d, best_M))
        check("FL floor >= MC-3 n=%d r'=%d" % (n, rp), floor >= best_mc3,
              "floor %d mc3 %d" % (floor, best_mc3))

    print("\n     The 'floor' column is a q-FREE LOWER BOUND on the crossing")
    print("     shell at agreement k+2, valid for EVERY admissible q.")

    # ------------------------------------------------ FL2: floor <= measured
    print("\n[FL2] floor <= measured |W_2| shell fibre, over a p-sweep")
    for (n, rp) in [(12, 5), (15, 5), (15, 6), (16, 6)]:
        CU = coset_union_sets(n, rp)
        prof0 = [0] * n
        for S in CU:
            prof0[sum(S) % n] += 1
        bad = []
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 61, 97, 151,
                  181, 211, 241]:
            ee = None
            for cand in range(1, 9):
                if (p ** cand - 1) % n == 0:
                    ee = cand
                    break
            if ee is None or p ** ee > 700:
                continue
            F = gf(p, ee)
            zp = F.powers(F.elem_of_order(n), n)
            prof = sig_profile(n, window_set(n, rp, 2, F, zp))
            for t in range(n):
                if prof[t] < prof0[t]:
                    bad.append((p, ee, t, prof[t], prof0[t]))
        check("FL2 floor holds fibrewise n=%d r'=%d" % (n, rp), not bad,
              str(bad[:3]))
        print("     n=%2d r'=%d : floor respected FIBREWISE at every tested p:"
              " %s" % (n, rp, not bad))

    print("\n" + "=" * 78)
    print("checks run: %d   failures: %d" % (CHECKS[0], len(FAILURES)))
    for nm, dd in FAILURES:
        print("  FAILED: %s | %s" % (nm, dd))
    print("=" * 78)


if __name__ == "__main__":
    main()
