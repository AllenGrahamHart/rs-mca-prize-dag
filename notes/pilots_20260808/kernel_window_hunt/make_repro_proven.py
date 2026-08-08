#!/usr/bin/env python3
"""Emit repro_witness_proven.py — the headline artifact: a standalone script
that PROVES its prime (BLS n-1) and exhibits the kernel vector.  No imports
from this pilot's library."""
import glob
import json
import sys
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
from bls import bls_prove
from hunt import verify_hit

best = None
tot = {"inband": 0, "top": 0}
for f in sorted(glob.glob(
        "notes/pilots_20260808/kernel_window_hunt/state/climbproof_*.json")):
    st = json.load(open(f))
    tot["inband"] += st["inband"]
    tot["top"] += st["top"]
    for r in st["proven"]:
        if best is None or r["pbits"] > best["pbits"]:
            best = r
print("climbproof totals: in-band %d, W_TOP PRP %d" % (tot["inband"], tot["top"]))
p = int(best["p"])
ok, cert = bls_prove(p)
assert ok, cert
rep = verify_hit(best["w"], p, 128)
assert rep["ok"], rep
print("headline: %d bits, cof=%d, l1=%d, v2(p-1)=%d, BLS branch=%s, F=2^%.1f"
      % (rep["p_bits"], rep["cofactor"], rep["l1"], rep["v2_p_minus_1"],
         cert["branch"], cert["F"].bit_length() - 1))

TPL = '''#!/usr/bin/env python3
"""HEADLINE ARTIFACT (round 24, kernel_window_hunt).

A nonzero non-cyclotomic ternary kernel vector at an admissible N'=128 prize
row, with the row prime PROVEN (not merely probable) by Brillhart-Lehmer-
Selfridge.  This falsifies the FAMILY-UNIFORM emptiness conjecture.

Standalone: imports nothing.  Run
  tools/ramguard local -- python3 notes/pilots_20260808/kernel_window_hunt/repro_witness_proven.py
"""
from math import gcd, isqrt

# ------------------------------------------------------------- CONSTANTS
W = %(w)r

P = %(p)d

# complete factorisation of the proven part F of P-1 (BLS certificate data)
FFAC = %(ffac)r
BASES = %(bases)r

H = len(W)              # 64
NPRIME = 2 * H          # 128 = the quotient order N'
SMAX = 4 * (H - 1) + 1  # 253


def negasq(a):
    m = len(a)
    c = [0] * m
    for i in range(m):
        if a[i] == 0:
            continue
        for j in range(m):
            if a[j] == 0:
                continue
            s = i + j
            if s < m:
                c[s] += a[i] * a[j]
            else:
                c[s - m] -= a[i] * a[j]
    return c


def norm(w):
    n = len(w)
    while n > 1:
        m = n >> 1
        A, B = negasq(w[0::2]), negasq(w[1::2])
        u = [A[0] + B[m - 1]]
        for i in range(1, m):
            u.append(A[i] - B[i - 1])
        w, n = u, m
    return w[0]


def is_small_prime(q):
    if q < 2:
        return False
    d = 2
    while d * d <= q:
        if q %% d == 0:
            return False
        d += 1
    return True


ok = True


def ck(name, cond, extra=""):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + extra if extra else ""))


print("--- 1. P IS PRIME (Brillhart-Lehmer-Selfridge n-1, cube-root form) ---")
ck("every q in the certificate is prime (trial division)",
   all(is_small_prime(q) for q in FFAC))
F = 1
for q, e in FFAC.items():
    F *= q ** e
ck("F divides P-1", (P - 1) %% F == 0)
R = (P - 1) // F
ck("gcd(F, R) = 1", gcd(F, R) == 1)
ck("F^3 > P  (F = 2^%%.1f, P = 2^%%.1f)" %% (F.bit_length() - 1, P.bit_length() - 1),
   F ** 3 > P)
good = True
for q, a in BASES.items():
    if pow(a, P - 1, P) != 1:
        good = False
    if gcd(pow(a, (P - 1) // q, P) - 1, P) != 1:
        good = False
ck("Pocklington conditions hold for every prime q | F", good)
s, r = divmod(R, 2 * F)
disc = r * r - 8 * s
ck("s = 0 or r^2-8s is not a perfect square  (s=%%d)" %% s,
   s == 0 or not (disc >= 0 and isqrt(disc) ** 2 == disc))
ck("==> P IS PRIME (PROVEN, not probable)", ok)

print()
print("--- 2. P IS AN ADMISSIBLE N'=128 ROW PRIME ---")
ck("P = 1 mod 128 (F_P contains a primitive 128th root)", P %% NPRIME == 1)
ck("P < 2^256 (the spec's field cap |F| < 2^256)", P < 2 ** 256)
ck("P <= 253^32 (BELOW the PROVED high-field emptiness threshold)",
   P <= SMAX ** (H // 2))
v2 = ((P - 1) & -(P - 1)).bit_length() - 1
print("     P has %%d bits; v2(P-1) = %%d, so the largest power-of-two smooth"
      %% (P.bit_length(), v2))
print("     domain on this row is n = 2^%%d (k <= 2^%%d, well under the 2^40 cap)."
      %% (v2, v2))

print()
print("--- 3. THE KERNEL VECTOR ---")
l1 = sum(abs(t) for t in W)
ck("w is nonzero and lies in {-2,...,2}^64", any(W) and all(-2 <= t <= 2 for t in W))
ck("||w||_1 = %%d <= 2l' = %%d (inside the full N'=128 support bound)" %% (l1, NPRIME),
   l1 <= NPRIME)
N = abs(norm(W))
ck("|Norm(w)| = 2^%%.1f <= S^(H/2) (AM-GM/Parseval ceiling)"
   %% (N.bit_length() - 1), N <= sum(t * t for t in W) ** (H // 2))
ck("P divides Norm(w)", N %% P == 0, "cofactor = %%d" %% (N // P))

e = (P - 1) // NPRIME
rho = None
for g in range(2, 500):
    c = pow(g, e, P)
    if pow(c, NPRIME // 2, P) == P - 1:
        rho = c
        break
ck("found rho in F_P of exact order 128", rho is not None)
hit = None
for sx in range(1, NPRIME, 2):
    rs = pow(rho, sx, P)
    acc, cur = 0, 1
    for j in range(H):
        acc = (acc + W[j] * cur) %% P
        cur = cur * rs %% P
    if acc %% P == 0:
        hit = sx
        break
ck("sum_j w_j zeta^j = 0 mod P for zeta = rho^s of exact order 128", hit is not None,
   "s = %%s" %% hit)

v = [0] * NPRIME
for i, t in enumerate(W):
    if t == 2:
        v[i], v[i + H] = 1, -1
    elif t == -2:
        v[i], v[i + H] = -1, 1
    elif t == 1:
        v[i] = 1
    elif t == -1:
        v[i] = -1
zeta = pow(rho, hit, P)
acc, cur = 0, 1
for j in range(NPRIME):
    acc = (acc + v[j] * cur) %% P
    cur = cur * zeta %% P
ck("the TERNARY lift v in {-1,0,1}^128 satisfies sum_j v_j zeta^j = 0 mod P",
   acc %% P == 0)
ck("supp(v) = ||w||_1 = %%d <= 2l' = 128" %% l1, sum(1 for t in v if t) == l1)
ck("v is NON-CYCLOTOMIC: v_i != v_{i+64} for some i (equivalently w != 0)",
   any(v[i] != v[i + H] for i in range(H)))

print()
print("REPRO %%s" %% ("PASS" if ok else "FAIL"))
if ok:
    print("K_P contains a non-cyclotomic ternary vector of support %%d <= 2l' = 128"
          %% l1)
    print("at the PROVEN prime P = 1 mod 128, P < 2^256.  The family-uniform")
    print("emptiness conjecture for admissible N'=128 rows is FALSE.")
'''

open("notes/pilots_20260808/kernel_window_hunt/repro_witness_proven.py", "w").write(
    TPL % {"w": best["w"], "p": p,
           "ffac": {int(k): int(v) for k, v in cert["fac"].items()},
           "bases": {int(k): int(v) for k, v in cert["bases"].items()}})
json.dump({"w": best["w"], "p": best["p"]},
          open("notes/pilots_20260808/kernel_window_hunt/state/"
               "best_witness_top_proven.json", "w"))
print("wrote repro_witness_proven.py")
