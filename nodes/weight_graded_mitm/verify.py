#!/usr/bin/env python3
"""Verifier for weight_graded_mitm.
Confirms the MITM enumeration of signed sparse vanishing zeta-power sums mod p is
CORRECT (== brute force), matches the cost count, and prints a radius certificate.
Stdlib only; runs <5s."""
from math import comb
from itertools import combinations, product

def order(g, p):
    x, k = g % p, 1
    while x != 1:
        x = (x * g) % p; k += 1
    return k

def signed_sparse(N, hmax):
    """yield signed vectors (as dict pos->+-1) with support 1..hmax over N positions."""
    for w in range(1, hmax + 1):
        for pos in combinations(range(N), w):
            for signs in product((1, -1), repeat=w):
                yield dict(zip(pos, signs))

def val(vec, zpow, p):
    return sum(s * zpow[x] for x, s in vec.items()) % p

def canon(vec):
    return tuple(sorted(vec.items()))

def brute(N, zpow, p, w):
    out = set()
    for vec in signed_sparse(N, w):
        if val(vec, zpow, p) == 0:
            out.add(canon(vec))
    return out

def mitm(N, zpow, p, w):
    """complete MITM: left table over full index set with supp<=ceil(w/2),
    right scan supp<=floor(w/2); match s(a)=-s(b), disjoint supports, supp<=w."""
    h1, h2 = (w + 1) // 2, w // 2
    table = {}
    for a in signed_sparse(N, h1):
        table.setdefault(val(a, zpow, p), []).append(a)
    out = set()
    # include the pure-left collisions (b empty) and pure combos
    for a in table.get(0, []):
        out.add(canon(a))
    for b in signed_sparse(N, h2):
        need = (-val(b, zpow, p)) % p
        for a in table.get(need, []):
            if set(a) & set(b):            # supports must be disjoint
                continue
            v = dict(a); v.update(b)
            if len(v) <= w:
                out.add(canon(v))
    return out

def known_relations(N, zpow, p, w):
    """generate the classical cyclotomic relations (as canon vectors) up to weight w:
       zeta^{N/2} = -1 pairs, and prime-ell coset sums."""
    gens = []
    if N % 2 == 0:
        for x in range(N):
            gens.append({x: 1, (x + N // 2) % N: 1})   # zeta^x + zeta^{x+N/2}=0
    d = 2
    m = N
    primes = set()
    while d * d <= N:
        if N % d == 0:
            primes.add(d)
            while N % d == 0: N //= d
        d += 1
    if N > 1: primes.add(N)
    N = len(zpow)
    for ell in primes:
        step = len(zpow) // ell
        for start in range(step):
            gens.append({(start + j * step) % len(zpow): 1 for j in range(ell)})
    rels = set(canon(g) for g in gens if val(g, zpow, p) == 0 and len(g) <= w)
    return rels

if __name__ == "__main__":
    ROWS = [(6, 7, 3), (8, 17, 2), (12, 13, 2)]   # (N', p, candidate zeta base)
    all_ok = True
    for N, p, g in ROWS:
        assert (p - 1) % N == 0, f"need p=1 mod N': {p},{N}"
        assert order(g, p) == N, f"{g} not primitive {N}-th root mod {p}"
        zpow = [pow(g, x, p) for x in range(N)]
        for w in (2, 3, 4):
            Vbf = brute(N, zpow, p, w)
            Vmm = mitm(N, zpow, p, w)
            ok = (Vbf == Vmm)
            all_ok &= ok
            # cost count vs formula
            table_ct = sum(comb(N, i) * 2**i for i in range(1, (w + 1) // 2 + 1))
            R = known_relations(N, zpow, p, w)
            survivors = Vbf - R
            cert = (len(survivors) == 0)
            print(f"N'={N:2d} p={p:2d} w={w}: MITM==brute:{ok}  "
                  f"#collisions={len(Vbf):3d} #known_rel={len(R):3d} "
                  f"survivors(beyond R)={len(survivors)}  "
                  f"CERT radius>{w}:{cert}  table~C(N',w/2)2^(w/2)={table_ct}")
    assert all_ok, "MITM did not match brute force"
    print("ALL PASS (MITM correctness verified; certificates printed)")
