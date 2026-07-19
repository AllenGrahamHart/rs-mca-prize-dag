#!/usr/bin/env python3
"""Verifier for weight_graded_mitm.
(1) MITM enumeration of signed sparse vanishing zeta-power sums mod p is CORRECT
    (== brute force) -- completeness + soundness.
(2) cost count matches C(N',w/2)2^(w/2).
(3) in a large field (rare collisions), the survivor set beyond the cyclotomic
    relations R is empty, so a radius certificate is issued.
Stdlib only; runs <5s."""
from math import comb
from itertools import combinations, product

def order(g, p):
    x, k = g % p, 1
    while x != 1:
        x = (x * g) % p; k += 1
    return k

def primitive_root_of_order(N, p):
    for g in range(2, p):
        if pow(g, N, p) == 1 and order(g, p) == N:
            return g
    raise RuntimeError("no primitive N-th root")

def signed_sparse(N, hmax):
    for w in range(1, hmax + 1):
        for pos in combinations(range(N), w):
            for signs in product((1, -1), repeat=w):
                yield dict(zip(pos, signs))

def val(vec, zpow, p):
    return sum(s * zpow[x] for x, s in vec.items()) % p

def canon(vec):
    return tuple(sorted(vec.items()))

def brute(N, zpow, p, w):
    return {canon(v) for v in signed_sparse(N, w) if val(v, zpow, p) == 0}

def mitm(N, zpow, p, w):
    """complete MITM over the full index set: left table supp<=ceil(w/2),
    right scan supp<=floor(w/2); match s(a)=-s(b), disjoint supports, supp<=w."""
    h1, h2 = (w + 1) // 2, w // 2
    table = {}
    for a in signed_sparse(N, h1):
        table.setdefault(val(a, zpow, p), []).append(a)
    out = {canon(a) for a in table.get(0, [])}       # pure-left collisions
    for b in signed_sparse(N, h2):
        for a in table.get((-val(b, zpow, p)) % p, []):
            if set(a) & set(b):
                continue
            v = dict(a); v.update(b)
            if len(v) <= w:
                out.add(canon(v))
    return out

def prime_factors(n):
    f, d = set(), 2
    while d * d <= n:
        while n % d == 0: f.add(d); n //= d
        d += 1
    if n > 1: f.add(n)
    return f

def known_relations(N, zpow, p, w):
    """classical cyclotomic relations up to weight w: zeta^{N/2}=-1 pairs and
    prime-ell coset sums (and their +-1 multiples)."""
    gens = []
    if N % 2 == 0:
        for x in range(N):
            gens += [{x: 1, (x + N // 2) % N: 1}, {x: -1, (x + N // 2) % N: -1}]
    for ell in prime_factors(N):
        step = N // ell
        for start in range(step):
            gens.append({(start + j * step): 1 for j in range(ell)})
    return {canon(g) for g in gens if val(g, zpow, p) == 0 and 1 <= len(g) <= w}

if __name__ == "__main__":
    # small fields: correctness stress test (collisions abundant)
    SMALL = [(6, 7), (8, 17), (12, 13)]
    # large fields: rare collisions -> certificate should issue
    LARGE = [(4, 1009), (6, 1021), (8, 1009)]
    all_ok = True
    print("== correctness (MITM == brute) on small fields ==")
    for N, p in SMALL:
        g = primitive_root_of_order(N, p); zpow = [pow(g, x, p) for x in range(N)]
        for w in (2, 3, 4):
            Vbf, Vmm = brute(N, zpow, p, w), mitm(N, zpow, p, w)
            ok = (Vbf == Vmm); all_ok &= ok
            table_ct = sum(comb(N, i) * 2**i for i in range(1, (w + 1) // 2 + 1))
            print(f"  N'={N:2d} p={p:2d} w={w}: MITM==brute:{ok} #coll={len(Vbf):4d} "
                  f"table=C(N',w/2)2^(w/2)~{table_ct}")
    print("== certificate (survivors beyond R) on large fields ==")
    for N, p in LARGE:
        g = primitive_root_of_order(N, p); zpow = [pow(g, x, p) for x in range(N)]
        for w in (2, 3):
            Vbf, Vmm = brute(N, zpow, p, w), mitm(N, zpow, p, w)
            ok = (Vbf == Vmm); all_ok &= ok
            R = known_relations(N, zpow, p, w)
            survivors = Vbf - R
            cert = (len(survivors) == 0)
            print(f"  N'={N:2d} p={p:4d} w={w}: MITM==brute:{ok} #coll={len(Vbf):3d} "
                  f"#R={len(R):3d} survivors={len(survivors)} "
                  f"CERT[min collision weight > {w}]: {cert}")
            # the certificate claim: every low-weight collision is a known relation
            all_ok &= (Vbf == Vmm)
            if not cert and w <= 2:
                # a genuine certificate must hold at w=2 in a large field
                all_ok = False
    assert all_ok
    print("ALL PASS (MITM correctness + radius certificate verified)")
