#!/usr/bin/env python3
"""qra_audit: INDEPENDENT fresh-context replay of the qrl packet r1.
All logic written from the packet's *statements*, not its code.
Exact integer arithmetic. Runs in /work (files flat)."""
import json
import re
import sys
from math import comb, isqrt

FAIL = []
def check(cond, label):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        FAIL.append(label)

def cap(npr):
    return 63 * npr**6 // 64

RHOS = [(2, "1/2"), (4, "1/4"), (8, "1/8"), (16, "1/16")]

def pairs():
    for s in range(13, 42):
        n = 2**s
        for den, rs in RHOS:
            k = n // den
            t = (n - k) // 2
            M = 2
            while M <= t:
                yield s, n, den, rs, k, t, M
                M *= 2

# ---------------------------------------------------------------- A: windows
print("== A: window arithmetic (independent, exact)")
vals = {npr: max(comb(npr, a) for a in range(npr + 1))
        for npr in (2, 4, 8, 16, 32, 64)}
check(all(vals[x] <= cap(x) for x in (2, 4, 8, 16, 32)),
      "max_a C(n',a) <= (63/64)n'^6 for n' in {2,4,8,16,32}: "
      + ", ".join(f"{x}:{vals[x]}<={cap(x)}" for x in (4, 8, 16, 32)))
check(vals[64] > cap(64),
      f"window genuinely fails at 64: C(64,32)={vals[64]} > {cap(64)}")
check(comb(32, 16) == 601080390 and cap(32) == 1056964608,
      "packet's quoted n'=32 numbers exact: 601,080,390 vs 1,056,964,608")
check(all(comb(npr, a) <= npr**6 // 720 <= cap(npr)
          for npr in (64, 128, 2**12, 2**20) for a in range(7)),
      "edge cells a<=6: C(n',a) <= n'^6/720 <= cap (spot n' up to 2^20)")

ok_j = True
for npr, kpr in [(64, 32), (64, 4), (128, 64), (4096, 2048), (4096, 256)]:
    lo = isqrt((kpr - 1) * npr) + 1
    for a in range(max(lo, kpr + 1), npr + 1):
        b = (npr * (a - kpr + 1)) // (a * a - (kpr - 1) * npr)
        if not (0 <= b <= npr * npr):
            ok_j = False
check(ok_j, "Johnson floor(n'(a-k'+1)/(a^2-(k'-1)n')) <= n'^2 on full windows"
            " at 5 (n',k') shapes")
ok_e = True
for npr in (2, 3, 8, 64, 4096):
    L = npr * npr
    for a in (1, npr // 2 + 1, npr):
        r = npr - a
        for q in (4 * npr * npr, 4 * npr * npr + 1, 64 * npr**4):
            D = (q - r) ** 2 - L * q
            if D <= 0 or (L * q * (q - r - 1)) // D > 2 * L:
                ok_e = False
check(ok_e, "ESP output floor(Lq(q-r-1)/D) <= 2L for L=n'^2, r<n', q>=4n'^2"
            " (exact sweep incl. boundary q=4n'^2)")

# ------------------------------------------------- B: Lemma 0 / crux, exact
print("== B: Lemma 0 reconciliation (independent)")
ok_div = ok_edge = ok_amin = True
npairs = mgtk = 0
for s, n, den, rs, k, t, M in pairs():
    npairs += 1
    if M <= k:
        if k % M != 0:
            ok_div = False
        if (k // M + 1) * M != k + M:
            ok_amin = False
        if (k + 1) % M == 0:
            ok_edge = False
    else:
        mgtk += 1
        if k % M == 0:
            ok_div = False
check(npairs == 2900, f"official (row,M) pair count = {npairs} == 2900")
check(ok_div, "dyadic M <= k => M | k; M > k => M does not divide k (all pairs)")
check(ok_amin, "M|A, M|k, A>=k+1 => A>=k+M => a>=k'+1 (all M<=k pairs)")
check(ok_edge, "edge band A=k+1 never divisible by M>=2 (k even at official rows)")
check(mgtk == 87, f"M in (k,t] pair count = {mgtk} == 87 (catch #111 scope)")

# --------------------------------------- C: coverage table full re-derivation
print("== C: coverage table re-derivation and diff")
def band(npr, kpr):
    return max(kpr + 1, 7), min(npr - 7, isqrt((kpr - 1) * npr))

mytab = {}
counts = dict(proved=0, opened=0, deep=0)
own_open = {}
for s, n, den, rs, k, t, M in pairs():
    npr = n // M
    j = M.bit_length() - 1
    if npr <= 32:
        counts["proved"] += 1
    else:
        counts["opened"] += 1
        kpr = k // M
        lo, hi = band(npr, kpr)
        assert lo <= hi, (s, rs, M)
        mytab.setdefault((s, rs), {})[j] = (npr, kpr, lo, hi)
        if npr == 64 and s >= 33:
            counts["deep"] += 1
        own_open[(s, rs, j)] = (7 <= kpr + 1 <= min(npr - 7,
                                isqrt((kpr - 1) * npr)))
check(counts["proved"] == 464 and counts["opened"] == 2436,
      f"proved/open pair counts = {counts['proved']}/{counts['opened']}"
      " == 464/2436 (of 2900)")
check(counts["deep"] == 36, f"deep sliver (n'=64, s>=33) = {counts['deep']} == 36")

ok_band = True
for (s, rs), row in mytab.items():
    for j, (npr, kpr, lo, hi) in row.items():
        if npr <= 4096:
            arange = range(kpr + 1, npr + 1)
        else:
            X = isqrt((kpr - 1) * npr)
            arange = [a for a in {kpr + 1, 6, 7, lo - 1, lo, hi, hi + 1,
                                  npr - 7, npr - 6, npr, X, X + 1}
                      if kpr + 1 <= a <= npr]          # NO set(range(...)) !
        for a in arange:
            covered = (a <= 6 or a >= npr - 6 or a * a > (kpr - 1) * npr)
            if covered == (lo <= a <= hi):
                ok_band = False
check(ok_band, "open band == complement of T1/T2 coverage: EXHAUSTIVE for all"
               " open pairs with n' <= 4096, boundary probes beyond")

patt = re.compile(r"\| (\d+) \| (1/\d+) \| j=1\.\.(\d+) \((\d+)\) \| "
                  r"j=(\d+)\.\.(\d+) \(4\) \| M=2: a in \[(\d+),(\d+)\]; "
                  r"M=2\^(\d+): a in \[(\d+),(\d+)\] \|")
tab_ok = True
nrows = 0
for line in open("qrl_coverage_table.md"):
    m = patt.match(line.strip())
    if not m:
        continue
    nrows += 1
    s, rs = int(m.group(1)), m.group(2)
    jmax, cnt = int(m.group(3)), int(m.group(4))
    pj0, pj1 = int(m.group(5)), int(m.group(6))
    lo2, hi2 = int(m.group(7)), int(m.group(8))
    jS, loS, hiS = int(m.group(9)), int(m.group(10)), int(m.group(11))
    row = mytab[(s, rs)]
    exp = (jmax == s - 6 == cnt == max(row) and pj0 == s - 5 and pj1 == s - 2
           and jS == s - 6
           and (row[1][2], row[1][3]) == (lo2, hi2)
           and (row[s - 6][2], row[s - 6][3]) == (loS, hiS)
           and row[s - 6][0] == 64)
    if not exp:
        tab_ok = False
        print("   ROW MISMATCH:", line.strip())
check(tab_ok and nrows == 116,
      f"all {nrows} packet table rows match independent re-derivation"
      " (open j-range, proved j-range, M=2 and n'=64 bands)")

exc = [(s, rs, j) for (s, rs, j), o in own_open.items() if not o]
check(all((mytab[(s, rs)][j][1] >= 8) == own_open[(s, rs, j)]
          for (s, rs, j) in own_open),
      "P1-own cell a=k'+1 open <=> k' >= 8 (all open pairs)")
check(all(mytab[(s, rs)][j][0] == 64 and rs == "1/16" for s, rs, j in exc)
      and len(exc) == 29,
      f"P1-own covered exceptions exactly (rho=1/16,n'=64): {len(exc)} pairs (a=5<=6)")

# ------------------------------- D: ledger consumption seam (sum over cells)
print("== D: ledger-hypothesis aggregation over cells a (sum-vs-max)")
seam = []
for den, rs in RHOS:
    for npr in (4, 8, 16, 32):
        kpr = npr // den
        tot_T1 = sum(comb(npr, a) for a in range(kpr + 1, npr + 1))
        tot_best = sum(min(comb(npr, a), 2 * npr * npr)
                       if a * a > (kpr - 1) * npr else comb(npr, a)
                       for a in range(kpr + 1, npr + 1))
        seam.append((rs, npr, tot_T1, tot_best,
                     tot_T1 <= cap(npr), tot_best <= cap(npr)))
for rs, npr, t1, tb, ok1, ok2 in seam:
    if not ok1:
        print(f"   SEAM: rho={rs} n'={npr}: sum_a C(n',a) = {t1} > cap ="
              f" {cap(npr)}; with T2 best: {tb} {'<=' if ok2 else '>'} cap")
check(all(ok1 for rs, npr, t1, tb, ok1, ok2 in seam if npr <= 16),
      "class-TOTAL (sum over cells a) within cap for ALL rho at n' <= 16"
      " (T1 alone, widest ALL-band reading)")
bad32 = sorted(rs for rs, npr, t1, tb, ok1, ok2 in seam
               if npr == 32 and not ok2)
check(bad32 == ["1/2", "1/4"],
      "at n'=32 class-TOTAL exceeds cap under ALL-band for rho in {1/2,1/4}"
      " even with T1+T2 combined (catch #113 material)")

# ----------------------------------------- E: catch #109 exhibit + thresholds
print("== E: catch #109 arithmetic (independent)")
q, npr = 2**26, 64
D = (q - 31) ** 2 - cap(npr) * q          # a = 33, r = 31
check(D == -4535124828922838079,
      f"exhibit s=13,M=128,n'=64,a=33: D = {D} == -4,535,124,828,922,838,079 < 0")
thr = {}
for s in range(13, 42):
    q = 4**s
    best, npr = 32, 64
    while npr <= 2**(s - 1):
        worstD = min((q - (npr - (npr // den + 1))) ** 2 - cap(npr) * q
                     for den, _ in RHOS)
        if worstD > 0:
            best = npr
        npr *= 2
    thr[s] = best
exp_thr = {13: 32, 17: 32, 21: 128, 25: 256, 29: 512, 33: 2048, 37: 4096, 41: 8192}
check(all(thr[s] == v for s, v in exp_thr.items()),
      "per-s ESP-transport thresholds match packet: "
      + ", ".join(f"s={s}:{thr[s]}" for s in sorted(exp_thr)))

# transportability != consumability: L = cap can have D>0 yet output >> cap
q = 4**21; npr = 2**21 // 32; kpr = npr // 2; r = npr - (kpr + 1)
L = cap(npr)
D = (q - r) ** 2 - L * q
out = L * q * (q - r - 1) // D
check(D > 0 and out > cap(npr),
      f"repair-spec gap exhibit s=21,M=32,n'=128,rho=1/2: D={D}>0 (feeds ESP)"
      f" BUT ESP output = {out/cap(npr):.1f} x cap -- catch #115 material")
import random
random.seed(7)
ok_pin = True
for _ in range(4000):
    npr = 2 ** random.randint(6, 20)
    q = random.choice([4 * npr * npr, 16 * npr**4, 2**52])
    if q <= 3 * npr:
        continue
    Lp = min(63 * npr**6 // 128, (q - 3 * npr) // 2)
    r = random.randint(0, npr - 1)
    D = (q - r) ** 2 - Lp * q
    if D <= 0 or Lp * q * (q - r - 1) // D > cap(npr):
        ok_pin = False
check(ok_pin, "corrected pin L<=min((63/128)n'^6,(q-3n')/2) => D>0 AND ESP"
              " output <= (63/64)n'^6 (4000-point exact sweep)")

# ------------------------------------------------ F: banked ground truth
print("== F: independent 514-cell ground-truth pass")
gt = json.load(open("cg_petal_census_results.json"))
ncell = 0
ok_gt = True
worst = (0.0, None)
for rec in gt:
    n, k, t = rec["n"], rec["k"], rec["t"]
    for fp in (0, 1):
        for bd in ("edge", "own", "all"):
            for key, v in rec[f"fp{fp}_{bd}"].items():
                M, A = map(int, key.split(","))
                ncell += 1
                npr, aa = n // M, A // M
                conds = [2 <= M <= t, A % M == 0, A >= k + 1,
                         v["classes"] == v["codewords"],
                         v["classes"] <= comb(npr, aa),
                         v["classes"] <= cap(npr)]
                if k % M == 0:
                    conds.append(A >= k + M)
                if k % 2 == 0 and bd == "edge":
                    conds.append(False)
                if not all(conds):
                    ok_gt = False
                    print("   GT VIOLATION:", rec["n"], k, rec["p"], key, v)
                rt = v["classes"] / comb(npr, aa)
                if rt > worst[0]:
                    worst = (rt, (n, k, rec["p"], f"fp{fp}_{bd}", key))
check(ncell == 514, f"profile cell count = {ncell} == 514")
check(ok_gt, "all cells: M|A, 2<=M<=t, A>=k+1 (+A>=k+M when M|k; edge empty at"
             " even k), multiplicity 1, <= C(n',a), <= cap")
check(abs(worst[0] - 2 / 3) < 1e-12 and worst[1][:3] == (8, 3, 17),
      f"tightest cell = {worst[1]} ratio {worst[0]:.3f} == 2/3")

print()
print(f"RESULT: {len(FAIL)} FAILURES" if FAIL else
      "RESULT: ALL INDEPENDENT CHECKS PASS")
sys.exit(1 if FAIL else 0)
