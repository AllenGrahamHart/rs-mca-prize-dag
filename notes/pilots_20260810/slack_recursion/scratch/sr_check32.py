#!/usr/bin/env python3
"""Third-scale check of THEOREM A (A1) at n=32 (and n=64) WITHOUT enumerating
C(n,a) subsets: for random a-subsets A, verify

    (interpolant of y on A has degree < k)  <=>  prod_{x in A} x = -1/c

for y(x) = x^{-1} + c x^{n/2}.  Two fields.  Also verifies the two Lagrange
identities used in the proof.
"""
import json, random, sys
from math import comb

def find_gen(q, n):
    co = (q - 1) // n
    for g0 in range(2, 100000):
        g = pow(g0, co, q)
        if pow(g, n // 2, q) != 1 and pow(g, n, q) == 1:
            if len({pow(g, i, q) for i in range(n)}) == n:
                return g
    raise RuntimeError

def lead_coeff(A, Yv, D, q, a):
    """sum_{x in A} y(x)/L'_A(x) = coefficient of X^{a-1} in the interpolant."""
    s = 0
    for i in A:
        x = D[i]
        d = 1
        for j in A:
            if j != i:
                d = d * (x - D[j]) % q
        s = (s + Yv[i] * pow(d, q - 2, q)) % q
    return s

def run(n, q, trials, seed=29):
    k = n // 2
    a = k + 1
    g = find_gen(q, n)
    D = [pow(g, i, q) for i in range(n)]
    rng = random.Random(seed)
    c = D[3]
    Yv = [(pow(x, q - 2, q) + c * pow(x, k, q)) % q for x in D]
    tgt = (-pow(c, q - 2, q)) % q
    ok = 0
    agree_hits = 0
    ident_ok = True
    for _ in range(trials):
        A = tuple(rng.sample(range(n), a))
        prod = 1
        for i in A:
            prod = prod * D[i] % q
        lc = lead_coeff(A, Yv, D, q, a)
        pred = (prod == tgt)
        if pred:
            agree_hits += 1
        if (lc == 0) == pred:
            ok += 1
        # identity check: sum x^j / L'(x) = 0 (j<=a-2), = 1 (j=a-1)
        for j in (0, a - 2, a - 1):
            v = lead_coeff(A, [pow(x, j, q) for x in D], D, q, a)
            if v != (1 if j == a - 1 else 0):
                ident_ok = False
    # planted: subsets forced onto the target product
    planted_ok = 0
    for _ in range(trials):
        while True:
            A = list(rng.sample(range(n), a - 1))
            pr = 1
            for i in A:
                pr = pr * D[i] % q
            need = tgt * pow(pr, q - 2, q) % q
            if need in D:
                j = D.index(need)
                if j not in A:
                    A.append(j)
                    break
        lc = lead_coeff(tuple(A), Yv, D, q, a)
        if lc == 0:
            planted_ok += 1
    return dict(n=n, q=q, a=a, trials=trials, criterion_agreements=ok,
                criterion_exact=(ok == trials),
                random_hits_on_target=agree_hits,
                planted_on_target_all_agreement_sets=(planted_ok == trials),
                planted_ok=planted_ok,
                lagrange_identities_ok=ident_ok,
                THEOREM_A_count=comb(n, a) // n,
                divisible=(comb(n, a) % n == 0),
                PLATEAU=comb(n // 2 - 1, n // 4))

if __name__ == "__main__":
    out = []
    for n, qs in ((32, (10177, 12289)), (64, (10177, 12289))):
        for q in qs:
            if (q - 1) % n:
                continue
            r = run(n, q, 60)
            out.append(r)
            print(json.dumps(r), flush=True)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            json.dump(out, f, indent=1)
