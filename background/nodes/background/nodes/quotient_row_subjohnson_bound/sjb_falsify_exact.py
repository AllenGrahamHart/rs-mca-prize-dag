#!/usr/bin/env python3
"""sjb_falsify_exact: exact-integer refutation table for quotient_row_subjohnson_bound.

CLAIM UNDER TEST (dag.json, verbatim scope): for every dyadic quotient row
(n' = 2^{s'} >= 64, k' = rho n', rho in {1/2,1/4,1/8,1/16}) from an official row
n = M n' = 2^s (13 <= s <= 41), every prime q == 1 (mod n) with q >= n^2, every
received word U', every cell a in the open band (P1-OWN: a = k'+1, present iff
k' >= 8): the aperiodic exact-agreement-a list is <= min((63/128) n'^6, (q-3n')/2).

REFUTATION TOOL (proved in sjb_refutation_proof.md, validated exhaustively by
sjb_semantics_tiny.py): for the explicit word family W_tau = X^{k'}(X - tau),
max_tau L_P(W_tau, k'+1) >= ceil(C(n', k'+1)/q), all supports aperiodic (odd size).

This script uses ONLY exact integer arithmetic (math.comb, Miller-Rabin primes).
"""
import math
import sys

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2,3,5,7,11,13,17,19,23,29,31,37)
    for p in small:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in small:  # deterministic for n < 3.3e24
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

def smallest_admissible_prime(n: int):
    """Smallest prime q == 1 (mod n) with q >= n^2."""
    q = n * n + 1
    if (q - 1) % n:
        q += n - ((q - 1) % n)
    while not is_prime(q):
        q += n
    return q

def caps(np_, q):
    return (63 * np_**6) // 128, (q - 3 * np_) // 2

FAILS = 0
def check(label, cond):
    global FAILS
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        FAILS += 1

RHO = {"1/2": 2, "1/4": 4, "1/8": 8, "1/16": 16}

print("=" * 100)
print("SECTION 1: refuted instances, one per rate + the first-open-size row (exact integers)")
print("=" * 100)
# (rate, s, n')  -- M = 2^s / n', k' = n'/den, a = k'+1
INSTANCES = [
    ("1/2", 13, 64),    # the FIRST open quotient size; (q-3n')/2 branch
    ("1/2", 14, 64),
    ("1/2", 15, 64),
    ("1/2", 13, 128),   # both branches, margin ~2^56
    ("1/2", 13, 4096),  # M=2 scale of the smallest official row
    ("1/4", 13, 128),
    ("1/8", 13, 128),
    ("1/16", 13, 256),
]
for rate, s, np_ in INSTANCES:
    den = RHO[rate]
    n = 1 << s
    M = n // np_
    kp = np_ // den
    a = kp + 1
    t = (n - n // den) // 2
    q0 = smallest_admissible_prime(n)
    C = math.comb(np_, a)
    floor_ = C // q0            # max_tau list >= ceil(C/q0) >= C//q0
    cap6, capq = caps(np_, q0)
    cap = min(cap6, capq)
    print(f"\nrate {rate}, s={s} (n=2^{s}), M={M}, n'={np_}, k'={kp}, a={a}, "
          f"q0={q0} (~2^{q0.bit_length()-1})")
    print(f"  C(n',a) = C({np_},{a}) ~ 2^{C.bit_length()-1};  pigeonhole floor C//q0 ~ 2^{max(floor_.bit_length()-1,0)}")
    print(f"  caps: (63/128)n'^6 = {cap6} (~2^{cap6.bit_length()-1}), (q0-3n')/2 = {capq} (~2^{capq.bit_length()-1})")
    # scope checks
    check("official scope: 13 <= s <= 41, M dyadic >= 2, M <= t", 13 <= s <= 41 and M >= 2 and (M & (M-1)) == 0 and M <= t)
    check("claim scope: n' >= 64, k' >= 8 (P1-OWN cell exists)", np_ >= 64 and kp >= 8)
    check("q0 admissible: prime, ==1 mod n, >= n^2", is_prime(q0) and q0 % n == 1 and q0 >= n * n)
    check("cell in open band: max(k'+1,7) <= a <= min(n'-7, isqrt((k'-1)n')) [sub-Johnson]",
          max(kp + 1, 7) <= a <= min(np_ - 7, math.isqrt((kp - 1) * np_)))
    check("a odd => every size-a subset of Z_{n'} aperiodic (k' even)", kp % 2 == 0 and a % 2 == 1)
    check(f"REFUTED: pigeonhole floor {floor_} > cap {cap}", floor_ > cap)

print()
print("=" * 100)
print("SECTION 2: violation q-windows at the flagship instances (the claim quantifies over ALL q >= n^2)")
print("=" * 100)
for rate, s, np_ in [("1/2", 13, 64), ("1/2", 13, 128)]:
    den = RHO[rate]; n = 1 << s; M = n // np_; kp = np_ // den; a = kp + 1
    C = math.comb(np_, a)
    q0 = smallest_admissible_prime(n)
    # branch 2 window: C//q > (q-3n')//2  <= solve approx then verify endpoints exactly
    lo, hi = q0, 1 << 200
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if C // mid > (mid - 3 * np_) // 2:
            lo = mid
        else:
            hi = mid - 1
    qmax_b2 = lo
    # branch 1 window: C//q > (63 n'^6)//128
    lo, hi = q0, 1 << 400
    cap6 = (63 * np_**6) // 128
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if C // mid > cap6:
            lo = mid
        else:
            hi = mid - 1
    qmax_b1 = lo
    print(f"\nrate {rate}, s={s}, n'={np_}: q-window where the claim FAILS:")
    print(f"  branch (q-3n')/2 violated for all q in [q0={q0}, {qmax_b2}] (~2^{qmax_b2.bit_length()-1})")
    print(f"  branch (63/128)n'^6 violated for all q in [q0, {qmax_b1}] (~2^{max(qmax_b1.bit_length()-1,0)})"
          + ("  (empty window)" if qmax_b1 < q0 else ""))
    check("window contains q0 itself (claim false at the minimal admissible field)",
          C // q0 > min((63 * np_**6) // 128, (q0 - 3 * np_) // 2))
    # count a few admissible primes inside the branch-2 window
    cnt, q = 0, q0
    while q <= qmax_b2 and cnt < 5:
        if is_prime(q):
            cnt += 1
        q += n
    check(f"at least {cnt} >= 3 admissible primes exhibited inside the violation window", cnt >= 3)

print()
print("=" * 100)
print("SECTION 3: ALL prize fields (q < 2^256): minimal dyadic n' per rate with C(n',k'+1) > q*(63/128)n'^6")
print("=" * 100)
Q = 1 << 256
for rate, den in RHO.items():
    np_ = 64
    while True:
        kp = np_ // den
        if kp >= 8:
            C = math.comb(np_, kp + 1)
            if C > Q * ((63 * np_**6) // 128):
                break
        np_ *= 2
    kp = np_ // den
    C = math.comb(np_, kp + 1)
    print(f"rate {rate}: first dyadic n' with pigeonhole floor > (63/128)n'^6 at EVERY q < 2^256: "
          f"n' = {np_} (C(n',k'+1) ~ 2^{C.bit_length()-1} > 2^256 * cap ~ 2^{(Q*((63*np_**6)//128)).bit_length()-1})")
    check(f"rate {rate}: word-uniform n'^6 impossible at ALL prize fields from n' = {np_} on",
          C > Q * ((63 * np_**6) // 128))
    # doubling monotonicity (Vandermonde): C(2n', 2k'+1) >= C(n',k') * C(n',k'+1)
    # >= C(n',k'+1)^2 / n'.  Since C > 2^256*(63/128)n'^6, this gives
    # C2 > 2^256*(63/128)n'^6 * C/n' > 64 * 2^256*(63/128)n'^6 = RHS at 2n',
    # so the violation persists at every larger dyadic n' by induction.
    C2 = math.comb(2 * np_, 2 * kp + 1)
    check(f"rate {rate}: doubling step C(2n',2k'+1) >= C(n',k')*C(n',k'+1) (numeric spot check)",
          C2 >= math.comb(np_, kp) * C)
    check(f"rate {rate}: violation persists at 2n' (direct check)",
          C2 > Q * ((63 * (2 * np_)**6) // 128))

print()
print("=" * 100)
print("SECTION 4: catch #115 pin unsatisfiable-by-truth (ESP capacity < true list) — per-rate exhibits")
print("=" * 100)
# ESP consumption needs L_true <= (q-3n')/2. Truth >= C//q. Exhibit pairs where
# C//q0 > (q0-3n')/2 at the MINIMAL official field (no lemma of any strength can feed ESP).
for rate, s, np_ in [("1/2", 13, 64), ("1/2", 13, 4096), ("1/4", 13, 128), ("1/8", 13, 128), ("1/16", 13, 256)]:
    den = RHO[rate]; n = 1 << s; kp = np_ // den
    q0 = smallest_admissible_prime(n)
    C = math.comb(np_, kp + 1)
    ok = C // q0 > (q0 - 3 * np_) // 2
    print(f"rate {rate}, s={s}, n'={np_}: truth floor ~2^{max((C//q0).bit_length()-1,0)} vs ESP capacity "
          f"(q0-3n')/2 ~ 2^{((q0-3*np_)//2).bit_length()-1}: ESP {'DEAD' if ok else 'alive'}")
    check(f"rate {rate}, s={s}, n'={np_}: ESP transport impossible for ANY true lemma", ok)

print()
print("=" * 100)
print("SECTION 5: what SURVIVES the pigeonhole (the fiber-starved refinement is not refuted here)")
print("=" * 100)
# At n'=64, s >= 16 the floor drops below both caps: claim not refuted there by this tool.
for s in (16, 20):
    np_, den = 64, 2
    n = 1 << s
    q0 = smallest_admissible_prime(n)
    kp = np_ // den
    C = math.comb(np_, kp + 1)
    fl = C // q0
    cap = min((63 * np_**6) // 128, (q0 - 3 * np_) // 2)
    print(f"rate 1/2, s={s}, n'=64: floor {fl} vs cap {cap} -> {'refuted' if fl > cap else 'NOT refuted (open)'}")
    check(f"s={s}, n'=64 not refuted by pigeonhole (documents the honest boundary)", fl <= cap)

print()
print(f"{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} CHECKS FAILED'}")
sys.exit(0 if FAILS == 0 else 1)
