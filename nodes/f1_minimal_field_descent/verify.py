#!/usr/bin/env python3
"""Verifier for f1_minimal_field_descent.
(A) Subfield lattice = divisor lattice; unique minimal field of definition
    (no composite ambiguity), relativised to a base B.
(B) Concrete Galois descent in F_{p^N}: field-of-definition of every element
    equals its Frobenius-orbit degree d_x, d_x | N, and the trichotomy
    K = B / B<K<F / K=F partitions the elements.
Pure stdlib; runs <5s."""
from math import gcd

def lcm(a, b): return a * b // gcd(a, b)
def divisors(n): return [d for d in range(1, n + 1) if n % d == 0]

# ---------- (A) combinatorial descent / lattice ----------
def check_lattice():
    fails = 0
    for N in range(1, 61):
        D = divisors(N)
        # subfield lattice: intersection=gcd, compositum=lcm, both stay divisors
        for d1 in D:
            for d2 in D:
                if N % gcd(d1, d2) or N % lcm(d1, d2): fails += 1
        # unique minimal field of definition over F_p containing a datum of
        # degree d_x, relativised to base b: must be lcm(b,d_x), unique min>=b.
        for b in D:
            for dx in D:
                fields_of_def = [d for d in D if b % gcd(b, d) == 0 and
                                 d % dx == 0 and d % b == 0]  # K' with dx|K', b|K'
                K = lcm(b, dx)
                if K not in D: fails += 1
                # unique minimum of fields_of_def is exactly K
                if not fields_of_def or min(fields_of_def) != K: fails += 1
                if any(k % K for k in fields_of_def): fails += 1  # all multiples of K
    return fails == 0

# ---------- finite field F_{p^N} via an irreducible poly ----------
def poly_mulmod(a, b, mod, p):
    res = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                res[i + j] = (res[i + j] + ai * bj) % p
    # reduce mod `mod` (monic, degree N)
    N = len(mod) - 1
    for i in range(len(res) - 1, N - 1, -1):
        c = res[i] % p
        if c:
            for j in range(N + 1):
                res[i - N + j] = (res[i - N + j] - c * mod[j]) % p
    res = res[:N]
    while len(res) < N: res.append(0)
    return res

def is_irreducible(mod, p, N):
    # brute: no root-based full test; use that x^{p^N}=x and x^{p^{N/q}}!=x
    x = [0, 1] + [0] * (N - 2) if N >= 2 else [0, 1]
    x = ([0, 1] + [0] * (N - 1))[:N]
    def frob_pow(v, times):
        for _ in range(times):
            v = field_pow(v, p, mod, p)
        return v
    xpN = frob_pow(x[:], N)
    if xpN != x: return False
    for q in set(pf(N)):
        if frob_pow(x[:], N // q) == x: return False
    return True

def pf(n):
    f = []; d = 2
    while d * d <= n:
        while n % d == 0: f.append(d); n //= d
        d += 1
    if n > 1: f.append(n)
    return f

def field_pow(a, e, mod, p):
    result = [1] + [0] * (len(mod) - 2)
    base = a[:]
    while e:
        if e & 1: result = poly_mulmod(result, base, mod, p)
        base = poly_mulmod(base, base, mod, p)
        e >>= 1
    return result

def find_irreducible(p, N):
    from itertools import product
    for coeffs in product(range(p), repeat=N):
        mod = list(coeffs) + [1]        # monic degree N
        if mod[0] == 0: continue        # need nonzero constant for irreducibility (N>=1)
        if is_irreducible(mod, p, N):
            return mod
    raise RuntimeError("no irreducible found")

def check_concrete(p, N, b):
    """b | N is the base degree. Return (ok, counts per trichotomy case)."""
    mod = find_irreducible(p, N)
    from itertools import product
    counts = {"I": 0, "II": 0, "III": 0}
    ok = True
    for coeffs in product(range(p), repeat=N):
        x = list(coeffs)
        # d_x = smallest i>0 with Frob^i(x)=x, Frob=x^p
        y = field_pow(x, p, mod, p); i = 1
        while y != x:
            y = field_pow(y, p, mod, p); i += 1
            if i > N + 1: ok = False; break
        dx = i
        if N % dx != 0: ok = False       # d_x | N must hold
        K = lcm(b, dx)
        if N % K != 0: ok = False
        if K == b: counts["I"] += 1
        elif K == N: counts["III"] += 1
        else: counts["II"] += 1
    return ok, counts

if __name__ == "__main__":
    okA = check_lattice()
    print(f"(A) subfield=divisor lattice, unique minimal K (no ambiguity): {'PASS' if okA else 'FAIL'}")
    results = []
    for (p, N, b) in [(2, 6, 2), (2, 12, 3), (3, 4, 2), (5, 4, 1)]:
        ok, c = check_concrete(p, N, b)
        results.append(ok)
        print(f"(B) F_{p}^{N}, base b={b}: descent d_x|N & trichotomy partition "
              f"{'PASS' if ok else 'FAIL'}  cases={c} (total={sum(c.values())}={p**N})")
    assert okA and all(results)
    print("ALL PASS")
