#!/usr/bin/env python3
"""Graded tangent band ledger: exact column arithmetic at the six rows.

The ledger column is

    C(u,v) = sum_{d=1}^{h-2} N_d * L(d),      L(d) = floor((R-d)/(h-d)),

where N_d = # codeword pairs (f,g) with |Z(f,g)| = k+d carrying >= 2 live
exact-A slopes, and L(d) is the (proved) line cap.  This script computes

 1. the row pins and the exact budget headroom (recomputed from B*, not quoted);
 2. SUM_d L(d) exactly on all six rows (divisor-block sum: h ~ 2^33 on prize);
 3. the largest uniform N with N * SUM_d L(d) <= headroom, and the same
    against the printed tangent column n-A+1;
 4. the columns implied by the candidate occupancy bounds N_d <= n, n^{3/2},
    n^2, C(n,2), n^3;
 5. the separable cascade term (d = h-1), whose per-pair cap is EXACTLY the
    printed tangent column.

Run: tools/ramguard local -- python3 <this>
"""
import json
from math import comb, log2, isqrt

# ---------------------------------------------------------------- B* (banked)
B_ROWC = 1 << 122


def iroot(x, r):
    lo, hi = 1, 1 << ((x.bit_length() + r) // r + 1)
    while lo < hi - 1:
        mid = (lo + hi) // 2
        if mid ** r <= x:
            lo = mid
        else:
            hi = mid
    return lo


B_PRIZE = iroot(1 << 1279, 10)
assert B_PRIZE == 317494674775468773183020924238786383963


def quot_ub(n, k, A):
    """banked all-active-dyadic-scale floor-rounded census sum."""
    t = A - k
    tot = 0
    np_ = 2
    while np_ <= n and np_ * t <= n:
        lp = (n - A) * np_ // n
        if 1 <= lp <= np_ - 1:
            tot += comb(np_, lp)
        np_ *= 2
    return tot


ROWS = []
for name, n, rate, scale, Bs in [
    ("RowC 1/4", 1024, 4, 256, B_ROWC),
    ("RowC 1/8", 1024, 8, 256, B_ROWC),
    ("RowC 1/16", 1024, 16, 512, B_ROWC),
    ("prize 1/4", 2 ** 41, 4, 256, B_PRIZE),
    ("prize 1/8", 2 ** 41, 8, 256, B_PRIZE),
    ("prize 1/16", 2 ** 41, 16, 512, B_PRIZE),
]:
    k = n // rate
    A = k + n // scale + 1
    ROWS.append(dict(name=name, n=n, k=k, A=A, h=A - k, r=n - A, R=n - k,
                     Bstar=Bs))

BANKED_A = [261, 133, 67, 558345748481, 283467841537, 141733920769]
BANKED_SLO = [5316907684064982757706454885536879188,
              5316911983139662876649441475853304530,
              5316911982997375233704305923711011740,
              317494670476394092449112149242524378539,
              317494674775468772568055135557962897065,
              317494674775326484925109999864086683573]

out = {}
FAIL = []


def chk(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + (f"  [{detail}]" if detail else ""))
    if not ok:
        FAIL.append(label)


print("=== 0. row pins + budget headroom (recomputed from B*) ===")
print(f"{'row':<11}{'n':>14}{'k':>14}{'A':>14}{'h':>13}{'r=n-A':>14}"
      f"{'R=n-k':>14}{'band width':>13}")
for i, row in enumerate(ROWS):
    n, k, A, h = row["n"], row["k"], row["A"], row["h"]
    chk(f"{row['name']}: A pin", A == BANKED_A[i], f"A={A}")
    bq = quot_ub(n, k, A)
    bt = n - A + 1
    s_lo = row["Bstar"] - bq - bt
    chk(f"{row['name']}: s_lo pin", s_lo == BANKED_SLO[i])
    row["B_tan_printed"] = bt
    row["s_lo"] = s_lo
    row["cubic"] = s_lo // n ** 3
    row["headroom"] = s_lo - 16 * n ** 3          # the free third column
    print(f"{row['name']:<11}{n:>14}{k:>14}{A:>14}{h:>13}{row['r']:>14}"
          f"{row['R']:>14}{A - 2 - k:>13}")
for row in ROWS:
    n = row["n"]
    chk(f"{row['name']}: floor(s_lo/n^3) >= 29", row["cubic"] >= 29,
        f"floor={row['cubic']}")
    chk(f"{row['name']}: headroom (s_lo-16n^3) >= 13n^3",
        row["headroom"] >= 13 * n ** 3,
        f"headroom/n^3 = {row['headroom']/n**3:.4f}")
    chk(f"{row['name']}: headroom < 14n^3 (tight on prize)",
        row["headroom"] < 14 * n ** 3 or row["name"].startswith("RowC"))

print()
print("=== 1. the line cap L(d) = floor((R-d)/(h-d)) across the band ===")
print("d = depth = |Z| - k;  d=0 is P-A1's exact-k stratum, d in [1,h-2] is")
print("the BAND, d = h-1 is the cascade tier.")


def L(row, d):
    return (row["R"] - d) // (row["h"] - d)


for row in ROWS[:3]:
    vals = [(d, L(row, d)) for d in range(0, row["h"])]
    print(f"  {row['name']:<11} " + "  ".join(f"d={d}:L={x}" for d, x in vals))
for row in ROWS[3:]:
    print(f"  {row['name']:<11} d=0:L={L(row,0)}  d=1:L={L(row,1)}  "
          f"d=2:L={L(row,2)}  ...  d=h-3:L={L(row,row['h']-3)}  "
          f"d=h-2:L={L(row,row['h']-2)}  || cascade d=h-1:L={L(row,row['h']-1)}")

print()
print("=== 2. cascade tier identity:  L(h-1) == n-A+1 == printed B_tan ===")
for row in ROWS:
    chk(f"{row['name']}: L(h-1) = n-A+1", L(row, row["h"] - 1) == row["n"] - row["A"] + 1,
        f"{L(row, row['h']-1)}")


def divsum(M, J):
    """sum_{j=1}^{J} floor(M/j) by divisor blocks, O(sqrt(M))."""
    if M <= 0:
        return 0
    J = min(J, M)
    total = 0
    j = 1
    while j <= J:
        v = M // j
        jmax = min(J, M // v)
        total += v * (jmax - j + 1)
        j = jmax + 1
    return total


def band_sum(row, sharp=True):
    """sum_{d=1}^{h-2} L(d).  With j = h-d, L = floor((R-h)/j) + 1 (sharp) or
    floor(R/j) (the banked sunflower form (n-k)/(t-d))."""
    R, h = row["R"], row["h"]
    if h < 3:
        return 0
    if sharp:
        M = R - h
        return (h - 2) + divsum(M, h - 1) - (M if h - 1 >= 1 else 0)
    return divsum(R, h - 1) - R


print()
print("=== 3. SUM_{d=1}^{h-2} L(d), exact (validated by brute force at RowC) ===")
for row in ROWS:
    s_sharp = band_sum(row, True)
    s_bank = band_sum(row, False)
    row["sumL"] = s_sharp
    row["sumL_sunflower"] = s_bank
    if row["h"] <= 64:
        brute = sum(L(row, d) for d in range(1, row["h"] - 1))
        chk(f"{row['name']}: divisor-block SUM_d L(d) == brute force",
            brute == s_sharp, f"{s_sharp}")
    print(f"  {row['name']:<11} SUM L(d) = {s_sharp:<22}"
          f"(sunflower form {s_bank})   = {s_sharp/row['R']:.4f} * R"
          f"   = {s_sharp/row['n']:.6g} * n")

print()
print("=== 4. largest UNIFORM occupancy N (N_d <= N for all d) that fits ===")
print(f"{'row':<11}{'N for 13n^3 headroom':>24}{'N/n^2':>12}"
      f"{'N for printed n-A+1':>22}")
for row in ROWS:
    n = row["n"]
    N13 = row["headroom"] // row["sumL"]
    Ntan = row["B_tan_printed"] // row["sumL"]
    row["N_max_headroom"] = N13
    row["N_max_tangent"] = Ntan
    print(f"{row['name']:<11}{N13:>24}{N13/n**2:>12.4f}{Ntan:>22}")

print()
print("=== 5. columns implied by candidate occupancy bounds ===")
cands = [("N_d <= 1", lambda n: 1),
         ("N_d <= n", lambda n: n),
         ("N_d <= n^(3/2)", lambda n: isqrt(n ** 3)),
         ("N_d <= n^2", lambda n: n ** 2),
         ("N_d <= C(n,2)", lambda n: n * (n - 1) // 2),
         ("N_d <= n^3", lambda n: n ** 3)]
print(f"{'row':<11}{'bound':<16}{'column / n^3':>16}{'<=13n^3?':>10}"
      f"{'<=n-A+1?':>10}")
tab = {}
for row in ROWS:
    n = row["n"]
    for label, f in cands:
        col = f(n) * row["sumL"]
        tab[(row["name"], label)] = col
        print(f"{row['name']:<11}{label:<16}{col/n**3:>16.6g}"
              f"{('YES' if col <= row['headroom'] else 'no'):>10}"
              f"{('YES' if col <= row['B_tan_printed'] else 'no'):>10}")
    print()

print("=== 6. separable cascade term (if the parallel audit finds the cascade ")
print("       tier UNPAID, the band top moves k+h-1 and the ledger gains ")
print("       N_{h-1} * (n-A+1)) ===")
print(f"{'row':<11}{'per-cascade-pair cost':>24}{'# cascade pairs inside 13n^3':>32}")
for row in ROWS:
    c = row["n"] - row["A"] + 1
    print(f"{row['name']:<11}{c:>24}{row['headroom']//c:>32}")

print()
print("=== 7. how many SATURATED top-of-band pairs fit in the printed column ===")
print("max_d L(d) = L(h-2) = floor((r+2)/2); printed column = n-A+1 = r+1")
for row in ROWS:
    top = L(row, row["h"] - 2)
    print(f"  {row['name']:<11} L(h-2) = {top:<16} (n-A+1)/L(h-2) = "
          f"{(row['n']-row['A']+1)/top:.4f}")

print()
print("=== 8. DIRECT scheme (a): count band pairs by the k-packing -- KILL ===")
print("k-packing => sum_P C(J_P,k) <= C(n,k) and C(J,k) >= k+1 for J >= k+1,")
print("so #band pairs <= C(n,k)/(k+1).  Compare against the 13n^3 column:")
print(f"{'row':<11}{'log2 C(n,k)/(k+1)':>22}{'log2 headroom':>18}{'bits over':>12}")
for row in ROWS:
    n, k = row["n"], row["k"]
    if n <= 4096:
        lg = log2(comb(n, k)) - log2(k + 1)
    else:                     # binary-entropy form, exact to <1 bit
        p = k / n
        lg = n * (-p * log2(p) - (1 - p) * log2(1 - p)) - log2(k + 1)
    lh = log2(row["headroom"]) if row["headroom"] < 2 ** 1000 else \
        row["headroom"].bit_length()
    print(f"{row['name']:<11}{lg:>22.4g}{lh:>18.4g}{lg - lh:>12.4g}")
print("The k-packing count exceeds every column by hundreds to 10^12 bits:")
print("counting BAND PAIRS is hopeless; only pairs with >= 2 LIVE slopes")
print("can be counted.")

print()
print("=== 9. banked interleaving route (list_subsqrt_interleaving_collapse")
print("       + xr_mismatch_global_explanation_list_owner) applied at k+d ===")
print("N_d <= L_2(k+d) <= L(k+1)(q-1)/(q-L(k+1)), = L(k+1) if L(k+1)^2 < q.")
print("So the ledger closes if the SINGLE-WORD RS list size at agreement k+1")
print("obeys L(k+1) <= headroom / SUM_d L(d):")
print(f"{'row':<11}{'required L(k+1)':>26}{'in n^2 units':>14}")
for row in ROWS:
    print(f"{row['name']:<11}{float(row['N_max_headroom']):>26.6g}"
          f"{float(row['N_max_headroom'])/row['n']**2:>14.4g}")
print("But L(k+1) is the list size at the LOWEST nontrivial agreement: even")
print("the AVERAGE over received words is ~C(n,k+1)/q, astronomically above")
print("n^2 at every row.  The interleaving route is TRUE but VACUOUS here.")

out["rows"] = [{k: (str(v) if isinstance(v, int) and v > 10 ** 15 else v)
                for k, v in row.items()} for row in ROWS]
out["candidate_columns"] = {f"{a} | {b}": str(c) for (a, b), c in tab.items()}
with open("notes/pilots_20260802/xr_graded_band_ledger/band_arith.json", "w") as fh:
    json.dump(out, fh, indent=1)
print()
print(("ALL CHECKS PASS" if not FAIL else f"FAILURES: {FAIL}"))
print("checkpoint written: band_arith.json")
