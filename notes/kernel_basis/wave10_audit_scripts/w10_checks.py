#!/usr/bin/env python3
"""wave-10 independent checks: cluster-1 constants + own-code toy MCA replays.

All computations from scratch (no v4 code imported).
"""
import math
from itertools import product
from math import isqrt

PASS = []

def ck(name, cond):
    assert cond, name
    PASS.append(name)

# ---------- 1. quadratic exact range constants ----------
k = 1 << 40
n = 1 << 41
s = isqrt(7 * k * k)
ck("isqrt(7k^2) two-sided", s * s < 7 * k * k < (s + 1) ** 2)
r_Q = 3 * k - s - 1
ck("r_Q value", r_Q == 389_500_552_608)
B_Q = r_Q + 1
# staircase hypothesis margin m(r) = (n-r)^2 - n(k+r), rate half => r^2 - 6kr + 2k^2
def marg(r):
    return (n - r) ** 2 - n * (k + r)
ck("hypothesis holds at r_Q", marg(r_Q) > 0)
ck("hypothesis fails at r_Q+1", marg(r_Q + 1) < 0)
ck("marg identity rate-half", all(marg(r) == r * r - 6 * k * r + 2 * k * k for r in (0, 1, r_Q, r_Q + 1)))
q_excl = (B_Q + 1) << 128
ck("q_exclusive value", q_excl == 132_540_169_959_144_315_698_788_704_090_115_531_231_543_332_700_160)
ck("log2 endpoint", abs(math.log2(q_excl) - 166.502834419) < 1e-9)
# wave-6 certified rate-half row sits exactly at the last determined budget
p_row = 132540169958804033333249306710494641010898987122689
ck("row budget == B_Q", p_row >> 128 == B_Q)
ck("row admissible n|p-1", (p_row - 1) % n == 0)
ck("row inside determined range", p_row < q_excl)
# bracket coherence with wave-9 unsafe reach
sigma0 = 8_594_128_895
ck("a_RH lower bracket coherent at B_Q", n - B_Q + 1 >= k + sigma0 + 1)
# (RQ4) range: r = B-1 <= tau = k-B+1 iff B <= 2^39+1 (two-sided)
Bq4 = (1 << 39) + 1
ck("sparse-auto boundary holds", (Bq4 - 1) <= k - Bq4 + 1)
ck("sparse-auto boundary tight", (Bq4 + 1 - 1) > k - (Bq4 + 1) + 1)

# ---------- 2. sparse safe curve / half-distance brackets ----------
# r <= tau at agreement a=n-r  iff  r <= (n-k)/2  (tau = n-r-k)
ck("half-distance algebra", all((r <= n - r - k) == (r <= (n - k) // 2) for r in ((1 << 39) - 1, 1 << 39, (1 << 39) + 1)))
# floor(q/2^128) >= 2^39 iff q >= 2^167 (two-sided)
ck("2^167 sparse curve boundary", ((1 << 167) >> 128) == 1 << 39 and (((1 << 167) - 1) >> 128) == (1 << 39) - 1)
# half-distance bracket budget: n <= floor(q/2^128) iff q >= 2^169 (two-sided)
ck("2^169 half-distance boundary", ((1 << 169) >> 128) == n and (((1 << 169) - 1) >> 128) == n - 1)
ck("3n/4 agreement constant", 3 * n // 4 == 1_649_267_441_664)

# ---------- 3. post-quadratic fence (PF1)-(PF3) by hand, own code ----------
# parity view: columns h_x=(1,x), x in 0..3 over F_5; y0=(0,1), y1=(1,4)
F = 5
cols = {x: (1, x) for x in range(4)}
def is_col_multiple(v):
    hits = []
    for x, h in cols.items():
        for lam in range(1, F):
            if ((lam * h[0]) % F, (lam * h[1]) % F) == v:
                hits.append((x, lam))
    return hits
y0, y1 = (0, 1), (1, 4)
ck("y0 column-far", not is_col_multiple(y0))
ck("y1 column-far", not is_col_multiple(y1))
bad = []
for g in range(1, F):
    v = ((y0[0] + g * y1[0]) % F, (y0[1] + g * y1[1]) % F)
    if is_col_multiple(v):
        bad.append(g)
ck("fence: 4 CA-bad slopes", len(bad) == 4)
ck("fence beats r+1", 4 > 1 + 1)
ck("fence quadratic margins", marg_ := ((4 - 0) ** 2 - 4 * (2 + 0)) > 0 and ((4 - 1) ** 2 - 4 * (2 + 1)) == -3)

# ---------- 4. own-code exhaustive toy: staircase equality on RS(4,1,F_5) ----------
# hypothesis (n-r)^2 >= n(k+r): n=4,k=1: r=0: 16>=4 T; r=1: 9>=8 T; r=2: 4>=12 F.
# support-wise MCA convention: slope g bad at agreement a iff fold agrees with some
# codeword on >= a coords AND no (c1,c2) with common agreement support >= a.
tn, tk, tq = 4, 1, 5
code = [tuple(c for _ in range(tn)) for c in range(tq)]  # RS(4,1): constants
words = list(product(range(tq), repeat=tn))
best_fold = {}
for w in words:
    best_fold[w] = max(sum(1 for i in range(tn) if w[i] == c[i]) for c in code)
maxima = {a: 0 for a in (tn, tn - 1)}
argmax_pairs = {}
for f1 in words:
    for f2 in words:
        # mutual: max over (c1,c2) common agreement
        mut = 0
        for c1 in range(tq):
            m1 = [f1[i] == c1 for i in range(tn)]
            for c2 in range(tq):
                agree = sum(1 for i in range(tn) if m1[i] and f2[i] == c2)
                mut = max(mut, agree)
        for a in (tn, tn - 1):
            if mut >= a:
                continue  # mutually explained at level a: no bad slopes
            cnt = 0
            for g in range(tq):
                fold = tuple((f1[i] + g * f2[i]) % tq for i in range(tn))
                if best_fold[fold] >= a:
                    cnt += 1
            if cnt > maxima[a]:
                maxima[a] = cnt
                argmax_pairs[a] = (f1, f2)
ck("toy staircase B(n)=1", maxima[tn] == 1)
ck("toy staircase B(n-1)=2", maxima[tn - 1] == 2)
ck("toy nonempty witnesses", all(a in argmax_pairs for a in (tn, tn - 1)))

print("W10_CHECKS_PASS", len(PASS), "checks")
for p in PASS:
    print(" ", p)
