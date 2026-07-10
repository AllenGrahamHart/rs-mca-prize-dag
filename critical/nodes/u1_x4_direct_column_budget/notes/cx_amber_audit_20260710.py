#!/usr/bin/env python3
"""AMBER AUDITOR independent replay for the u1_x4 amber surgery proposal.

All enumerations tiny (n <= 64, p <= 7937). Exact integer arithmetic.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt

FAILS = []
def chk(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + (f"  [{detail}]" if detail else ""))
    if not ok:
        FAILS.append(label)

# ---------- 1. The substitution identity, symbolic (coefficients on n^3, n^7/3, n^2) ----------
# T3 < n^2/72 + c0*n^{7/3} + (n/36)*(36 n^2 - c1*n^{4/3} - n/2)
# coefficient bookkeeping: n^3: 1 ; n^{7/3}: c0 - c1/36 ; n^2: 1/72 - 1/72
for (c0, c1, tag) in [(Fraction(2,9), 8, "as-written C36 (2/9 | 8)"),
                      (Fraction(4,9), 16, "repaired C36' (4/9 | 16)")]:
    n73 = c0 - Fraction(c1, 36)
    n2 = Fraction(1,72) - Fraction(1,2*36)
    chk(f"identity lands at exactly n^3: {tag}", n73 == 0 and n2 == 0,
        f"n^(7/3) coeff={n73}, n^2 coeff={n2}")

# ---------- 2. threshold values at n=8192 ----------
n = 8192
n43 = n ** Fraction(4,3)  # exact? use float + exact cube compare
import math
thr_f = 36*n**2 - 8*(n**(4/3)) - n/2
chk("C36 threshold at n=8192 ~ 2414593885.0 (note prints 2414593885.0251856)",
    abs(thr_f - 2414593885.0251856) < 1e-4, f"{thr_f!r}")
worst = 66933997
chk("worst/threshold = 0.02772060238 (note)", abs(worst/thr_f - 0.02772060238167208) < 1e-12,
    f"{worst/thr_f!r}")
chk("worst/n^2 = 0.9973942786 (note)", abs(worst/n**2 - 0.9973942786455154) < 1e-12,
    f"{worst/n**2!r}")
thr_rep = 36*n**2 - 16*(n**(4/3)) - n/2
chk("repaired threshold still positive and stress margin ~unchanged",
    thr_rep > 0 and worst/thr_rep < 0.0278, f"thr'={thr_rep!r} frac={worst/thr_rep:.9f}")
# exact positivity of both thresholds at n=8192 via exact cube compare:
# 16 n^{4/3} < 36 n^2 - n/2  <=>  (16)^3 n^4 < (36n^2 - n/2)^3
lhs = 16**3 * n**4
rhs_num = (72*n**2 - n)**3      # (36n^2 - n/2) = (72n^2-n)/2
chk("exact: 16 n^(4/3) < 36n^2 - n/2 at n=8192 (threshold' > 0)", 8*lhs < rhs_num)

# ---------- 3. official prefix primes for n=8192 ----------
def is_prime(v):
    if v < 2: return False
    for sp in (2,3,5,7,11,13,17,19,23,29,31,37):
        if v % sp == 0: return v == sp
    d = v-1; s = 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a % v == 0: continue
        x = pow(a, d, v)
        if x in (1, v-1): continue
        for _ in range(s-1):
            x = x*x % v
            if x == v-1: break
        else: return False
    return True

primes = []
m = 8192
while len(primes) < 12:
    c = m*8192 + 1
    if is_prime(c): primes.append(c)
    m += 1
chk("first official prime for n=8192 with p>=n^2 is 67239937", primes[0] == 67239937,
    str(primes[:3]))

# ---------- 4. small-row exact replays ----------
def subgroup(p, nn):
    # find element of order nn in F_p^*
    assert (p-1) % nn == 0
    for g in range(2, p):
        v = pow(g, (p-1)//nn, p)
        # check order exactly nn
        ok = True
        x = v; o = 1
        while x != 1:
            x = x*v % p; o += 1
            if o > nn: ok = False; break
        if ok and o == nn:
            H = set(); x = 1
            for _ in range(nn):
                H.add(x); x = x*v % p
            return H
    raise RuntimeError

def n3to1_brute(p, H):
    A = sorted((1-h) % p for h in H if (1-h) % p != 0)
    Aset = set(A)
    cnt = 0
    for a1 in A:
        for a2 in A:
            a12 = a1*a2 % p
            for a3 in A:
                if a12*a3 % p in Aset:
                    cnt += 1
    return cnt, A, Aset

def n3to1_conv(p, H):
    # replay of the Modal script's counting method
    A = [(1-h) % p for h in H if (1-h) % p != 0]
    prod = [0]*p; quot = [0]*p
    inv = {a: pow(a, p-2, p) for a in A}
    for x in A:
        for y in A:
            prod[x*y % p] += 1
            quot[x*inv[y] % p] += 1
    return sum(prod[t]*quot[t] for t in range(1, p))

def energy(p, H):
    A = [(1-h) % p for h in H if (1-h) % p != 0]
    r = {}
    for x in A:
        for y in A:
            t = x*y % p
            r[t] = r.get(t, 0) + 1
    return sum(v*v for v in r.values())

ROWS = [(97,32,9692,10315), (4289,64,3639,10755), (7937,64,5765,13191)]
for (p, nn, Nb, Eb) in ROWS:
    H = subgroup(p, nn)
    Nbr, A, Aset = n3to1_brute(p, H)
    Ncv = n3to1_conv(p, H)
    E = energy(p, H)
    chk(f"(p,n)=({p},{nn}): brute N_3to1 == banked {Nb}", Nbr == Nb, f"got {Nbr}")
    chk(f"(p,n)=({p},{nn}): convolution method == brute (Modal counting sound)", Ncv == Nbr,
        f"conv {Ncv}")
    chk(f"(p,n)=({p},{nn}): E_x == banked {Eb}", E == Eb, f"got {E}")

# ---------- 5. trace-zero accounting at the two official-regime small rows ----------
def trace_zero_audit(p, nn):
    H = subgroup(p, nn)
    Hs = sorted(H)
    I = sum(1 for x in H if (x+1) % p in H)
    # zero-sum triples
    trips = set()
    for x in Hs:
        for y in Hs:
            if y <= x: continue
            z = (-x-y) % p
            if z in H and z != x and z != y and z > y:
                trips.add((x,y,z))
    T0 = len(trips)
    # orbits under dilation
    seen = set(); orbits = []
    for t in trips:
        if t in seen: continue
        orb = set()
        for g in Hs:
            gt = tuple(sorted(g*e % p for e in t))
            orb.add(gt); seen.add(gt)
        orbits.append(sorted(orb)[0])
        assert len(orb) == nn  # freeness of dilation on 3-sets in 2-group
    R = len(orbits)
    # A_3^0: pair-orbits {P,Q} distinct disjoint zero-sum triples, e2 equal,
    # modulo common dilation
    def e2(t): return (t[0]*t[1] + t[0]*t[2] + t[1]*t[2]) % p
    trl = sorted(trips)
    pairs = []
    for i in range(len(trl)):
        for j in range(i+1, len(trl)):
            P, Q = trl[i], trl[j]
            if set(P) & set(Q): continue
            if e2(P) == e2(Q):
                pairs.append((P, Q))
    # group pairs into common-dilation orbits
    pseen = set(); pair_orbits = 0; same_orbit_pairs = 0
    orbit_of = {}
    for t in trips:
        key = min(tuple(sorted(g*e % p for e in t)) for g in Hs)
        orbit_of[t] = key
    for (P, Q) in pairs:
        fz = frozenset((P, Q))
        if fz in pseen: continue
        for g in Hs:
            gP = tuple(sorted(g*e % p for e in P))
            gQ = tuple(sorted(g*e % p for e in Q))
            pseen.add(frozenset((gP, gQ)))
        pair_orbits += 1
        if orbit_of[P] == orbit_of[Q]:
            same_orbit_pairs += 1
    raw_pairs = len(pairs)
    return I, T0, R, pair_orbits, raw_pairs, same_orbit_pairs

for (p, nn) in [(4289,64), (7937,64)]:
    I, T0, R, A30_pair_orbits, raw0, same_orb = trace_zero_audit(p, nn)
    print(f"  (p,n)=({p},{nn}): I={I} T0={T0} R={R} "
          f"A_3^0(pair-orbits)={A30_pair_orbits} raw zero-trace pairs={raw0} "
          f"same-orbit pair-orbits={same_orb} binom(R,2)={comb(R,2)} R^2={R*R}")
    chk(f"(p,n)=({p},{nn}): R <= I/6 (note's orbit count)", 6*R <= I, f"6R={6*R} I={I}")
    chk(f"(p,n)=({p},{nn}): corrected envelope A_3^0 <= R^2 holds",
        A30_pair_orbits <= R*R)
    # the note's claimed envelope:
    note_env_ok = A30_pair_orbits <= comb(R, 2)
    print(f"  NOTE-ENVELOPE A_3^0 <= binom(R,2): {'holds' if note_env_ok else 'FAILS'}"
          f"  ({A30_pair_orbits} vs {comb(R,2)})")
    # compiler payment check: raw zero-trace pairs <= n * A_3^0(claimed binom(R,2))?
    print(f"  compiler with binom(R,2): n*binom(R,2)={nn*comb(R,2)} vs raw={raw0}"
          f"  -> {'OK' if raw0 <= nn*comb(R,2) else 'UNDERPAYS'}")
    chk(f"(p,n)=({p},{nn}): compiler with corrected R^2 pays raw pairs",
        raw0 <= nn * R * R)

# ---------- 6. nonzero-trace: 36*A_3^nz <= N_3to1 at (4289,64) ----------
def nz_audit(p, nn, N3):
    H = subgroup(p, nn); Hs = sorted(H)
    subs = list(combinations(Hs, 3))
    fibers = {}
    for t in subs:
        s1 = sum(t) % p
        s2 = (t[0]*t[1] + t[0]*t[2] + t[1]*t[2]) % p
        fibers.setdefault((s1, s2), []).append(t)
    raw_nz = 0; raw_all = 0; raw_nz_overlap = 0
    for (s1, s2), lst in fibers.items():
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                P, Q = lst[i], lst[j]
                raw_all += 1
                if s1 != 0:
                    if set(P) & set(Q):
                        raw_nz_overlap += 1
                    else:
                        raw_nz += 1
    T3_total = raw_all
    chk(f"(p,n)=({p},{nn}): overlapping same-(e1,e2) distinct pairs impossible",
        raw_nz_overlap == 0, str(raw_nz_overlap))
    # freeness for nz: raw_nz divisible by n
    chk(f"(p,n)=({p},{nn}): raw nz pairs divisible by n (free dilation)",
        raw_nz % nn == 0, f"{raw_nz}")
    A3nz = raw_nz // nn
    chk(f"(p,n)=({p},{nn}): 36*A_3^nz <= N_3to1 (charging direction)",
        36*A3nz <= N3, f"36*{A3nz}={36*A3nz} vs {N3}")
    return T3_total, A3nz

for (p, nn, Nb) in [(4289,64,3639), (7937,64,5765)]:
    T3, A3nz = nz_audit(p, nn, Nb)
    I, T0, R, A30, raw0, so = trace_zero_audit(p, nn)
    # full compiler: T3_total <= n^2/72 + n*(A30_corrected + A3nz)?
    bound_correct = Fraction(nn**2, 72) + nn*(A30 + A3nz)
    bound_note = Fraction(nn**2, 72) + nn*(comb(R,2) + A3nz)
    print(f"  (p,n)=({p},{nn}): T3_total={T3}; compiler bound w/ true A_3^0={float(bound_correct):.1f};"
          f" w/ note binom(R,2)={float(bound_note):.1f}")
    chk(f"(p,n)=({p},{nn}): T3 <= n^2/72 + n(A_3^0_true + A_3^nz)", T3 <= bound_correct)
    if T3 > bound_note:
        print(f"  *** NOTE-CHAIN UNDERPAYS T3 at this row: {T3} > {float(bound_note):.1f} ***")

# ---------- 7. h=2 constants at all 29 official rows ----------
ok = all(211**2 < 64*(1 << s) for s in range(13, 42))
chk("in-house K6: (211/8) n^(5/2) < n^3 at all 29 rows (211^2 < 64n)", ok)
ok = all(4 < 9*(1 << s) for s in range(13, 42))
chk("assembly's (2/3) constant check 4<9n at all rows (constant provenance separate)", ok)

print()
print("FAILS:", len(FAILS))
print("CX_AUDIT_" + ("PASS" if not FAILS else "SEE_FAILS"))
