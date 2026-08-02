#!/usr/bin/env python3
"""Light exact census of live slopes |Gamma| for split-fibre pencils.

Lane P-B, pilot pb_gamma_exposure.  READ-ONLY use of the two banked pilots:
the construction, all parameter/strip/genericity checks and the candidate
family come from
    notes/pilots_20260802/pb_split_fibre_selector/pb_split_fibre_pilot.py
(imported, never modified).  The enumeration is the SAME meet-in-the-middle
identity used by
    notes/pilots_20260802/pb_selector_orders/k1_orders.py
    (for U = G X^{ma}, V = -G X^{m(a-1)}:  membership at slope z reads
     e_j(S) = (-1)^j (alpha_j + z beta_j), j = 1..h; beta_j = 0 for j < m so
     the first m-1 constraints are slope-free; beta_m = -1 so j = m
     DETERMINES z; j = m+1..h verify),
but it accumulates only per-slope COUNTS and the lex-minimum mask, in dicts
rather than length-q arrays, so that q may be pushed far past the banked
grid into the low-density (official) regime.

`crosscheck` replays all 12 banked k1 cases and asserts bit-exact agreement
with the banked witness census, so the two instruments cannot diverge.
"""

from __future__ import annotations

import json
import os
import sys
from itertools import combinations

sys.dont_write_bytecode = True          # never write into the prior pilots
HERE = os.path.dirname(os.path.abspath(__file__))
PILOTS = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(PILOTS, "pb_split_fibre_selector"))
import pb_split_fibre_pilot as P        # noqa: E402

K1DIR = os.path.join(PILOTS, "pb_selector_orders")


# ---------------------------------------------------------------------------
# half tables: size, power sums p_1..p_H, bit-reversed mask (for the lex key)
# ---------------------------------------------------------------------------
def build_half(vals, gidx, H, q, n):
    L = len(vals)
    N = 1 << L
    size = [0] * N
    ps = [[0] * N for _ in range(H + 1)]
    rev = [0] * N
    powv = [[pow(v, j, q) for j in range(H + 1)] for v in vals]
    for mask in range(1, N):
        low = mask & -mask
        i = low.bit_length() - 1
        rest = mask ^ low
        size[mask] = size[rest] + 1
        pv = powv[i]
        for j in range(1, H + 1):
            ps[j][mask] = (ps[j][rest] + pv[j]) % q
        rev[mask] = rev[rest] | (1 << (n - 1 - gidx[i]))
    return dict(size=size, ps=ps, rev=rev)


def census(case, want_lexmin=True):
    """Exact per-slope witness counts (and the lex-min support) for `case`.

    Returns dict: total, per_slope {z: count}, lexmin {z: mask}.
    """
    q, n, m, K, h, A = case.q, case.n, case.m, case.K, case.h, case.A
    U, V, D = case.U, case.V, case.D
    H = h
    L1 = n // 2
    T1 = build_half(D[:L1], list(range(L1)), H, q, n)
    T2 = build_half(D[L1:], list(range(L1, n)), H, q, n)

    alpha = [0] * (h + 1)
    beta = [0] * (h + 1)
    for j in range(1, h + 1):
        t = A - j
        alpha[j] = U[t] if 0 <= t < len(U) else 0
        beta[j] = V[t] if 0 <= t < len(V) else 0
    assert all(beta[j] % q == 0 for j in range(1, m)), beta
    assert beta[m] % q != 0, beta
    inv_beta_m = pow(beta[m] % q, q - 2, q)
    sgn_m = 1 if m % 2 == 0 else -1

    e_free = [0] * (m + 1)
    for j in range(1, m):
        e_free[j] = (((-1) ** j) * alpha[j]) % q
    p_free = [0, 0] if m == 1 else P.newton_power_sums(e_free, m - 1, q)

    invj = [pow(j % q, q - 2, q) for j in range(H + 1)]

    s1, ps1, rev1 = T1["size"], T1["ps"], T1["rev"]
    s2, ps2, rev2 = T2["size"], T2["ps"], T2["rev"]
    ALLN = (1 << n) - 1

    table: dict[int, list[int]] = {}
    for mask in range(1 << L1):
        sz = s1[mask]
        if sz > A:
            continue
        k = sz
        for j in range(1, m):
            k = k * q + ps1[j][mask]
        table.setdefault(k, []).append(mask)

    per: dict[int, int] = {}
    lexmin: dict[int, tuple[int, int]] = {}
    total = 0
    rng = range(1, h + 1)
    rng2 = range(m + 1, h + 1)
    for m2 in range(1 << (n - L1)):
        sz2 = s2[m2]
        need = A - sz2
        if need < 0 or need > L1:
            continue
        k = need
        for j in range(1, m):
            k = k * q + (p_free[j] - ps2[j][m2]) % q
        bucket = table.get(k)
        if not bucket:
            continue
        r2 = [ps2[j][m2] for j in range(H + 1)]
        for m1 in bucket:
            pw = [0] * (H + 1)
            for j in rng:
                pw[j] = (r2[j] + ps1[j][m1]) % q
            e = [0] * (H + 1)
            e[0] = 1
            for j in rng:
                s = 0
                for i in range(1, j + 1):
                    t = e[j - i] * pw[i]
                    s = s + t if (i & 1) else s - t
                e[j] = (s * invj[j]) % q
            z = ((sgn_m * e[m] - alpha[m]) * inv_beta_m) % q
            ok = True
            for j in rng2:
                if e[j] != (((-1) ** j) * (alpha[j] + z * beta[j])) % q:
                    ok = False
                    break
            if not ok:
                continue
            total += 1
            per[z] = per.get(z, 0) + 1
            if want_lexmin:
                key = ALLN ^ (rev1[m1] | rev2[m2])
                cur = lexmin.get(z)
                if cur is None or key < cur[0]:
                    lexmin[z] = (key, m1 | (m2 << L1))
    return dict(total=total, per_slope=per,
                lexmin={z: v[1] for z, v in lexmin.items()})


# ---------------------------------------------------------------------------
# low-core-only candidate family (drops the banked builder's Sidon clause)
# ---------------------------------------------------------------------------
def lowcore_family(case, cap=None):
    """Greedy maximal family of a-subsets J of the label pool with

        |J ^ J'| <= a - 2      (=> |S_J ^ S_J'| = g + m|J^J'| <= K-1)
        z_J pairwise distinct in F_q

    i.e. the P-B Gamma_lo obligation ONLY -- no distinct-oriented-difference
    (Sidon) clause, which the adversarial audit needs for the ENERGY producer
    but which |Gamma_lo| does not require.
    """
    q, a, b = case.q, case.a, case.b
    fam: list[tuple[int, ...]] = []
    famsets: list[set] = []
    sums: set[int] = set()
    seen = 0
    for J in combinations(range(b), a):
        seen += 1
        if cap is not None and seen > cap:
            break
        Js = set(J)
        if any(len(Js & S2) > a - 2 for S2 in famsets):
            continue
        zJ = sum(case.labels[i] for i in J) % q
        if zJ in sums:
            continue
        fam.append(J)
        famsets.append(Js)
        sums.add(zJ)
    return fam


def sum_class_family_size(b: int, a: int) -> int:
    """Exact size of the largest residue class of sum(J) mod b among the
    C(b,a) weight-a subsets of {0,...,b-1}.  Every such class is a
    constant-weight code of minimum distance >= 4 (if |J ^ J'| = a-1 then
    the sums differ by a nonzero residue mod b), hence a valid low-core
    family; this is an EXACT, constructive lower bound on A(b,4,a).
    """
    dp = [0] * b
    dp[0] = 1
    # dp over (chosen count, sum mod b)
    cur = [[0] * b for _ in range(a + 1)]
    cur[0][0] = 1
    for i in range(b):
        for c in range(min(i, a - 1), -1, -1):
            row = cur[c]
            nxt = cur[c + 1]
            for s in range(b):
                v = row[s]
                if v:
                    nxt[(s + i) % b] += v
    return max(cur[a])


# ---------------------------------------------------------------------------
def crosscheck() -> None:
    """Replay the 12 banked k1 cases; assert bit-exact census agreement."""
    sys.path.insert(0, K1DIR)
    import k1_orders as K1                                   # noqa: E402
    bad = []
    for name, prm in K1.CASES.items():
        path = os.path.join(K1DIR, f"k1_{name}.json")
        if not os.path.exists(path):
            continue
        with open(path) as fh:
            banked = json.load(fh)["witness_census"]
        case = P.Case(name, dict(prm))
        cs = census(case, want_lexmin=False)
        live = len(cs["per_slope"])
        ok = (cs["total"] == banked["total_exact_A_witnesses"]
              and live == banked["live_slopes"])
        if ok:
            bp = {int(k): v for k, v in banked["per_slope_counts"].items()}
            ok = bp == cs["per_slope"]
        print(f"  {name:<5} total={cs['total']:>9} "
              f"(banked {banked['total_exact_A_witnesses']:>9})  "
              f"live={live:>4} (banked {banked['live_slopes']:>4})  "
              f"{'MATCH' if ok else 'MISMATCH'}")
        if not ok:
            bad.append(name)
    if bad:
        raise SystemExit(f"CROSSCHECK FAILED: {bad}")
    print("CROSSCHECK PASS: census agrees bit-exactly with the banked k1 "
          "witness census (totals, live slopes, full per-slope histograms)")


if __name__ == "__main__":
    crosscheck()
