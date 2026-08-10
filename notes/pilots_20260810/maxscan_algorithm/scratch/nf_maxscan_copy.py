#!/usr/bin/env python3
"""nf_maxscan: EXACT max over ALL word classes at t = 1, delta = 1.

Complement form: A subset of D of size a = k+1 <-> B = D\\A of size k-1.
L_A = (1-z^n)/L_B, so mod z^3, L_A = 1/L_B, and the admissibility condition
   L_A * uhat = W  mod z^3,  deg uhat <= 1
is LINEAR in the B-truncation:
   [z^2](W * L_B) = 0  <=>  (L_B)_2 + W_1 (L_B)_1 + W_2 = 0.
So each B is a LINE in the (W_1, W_2) plane and F_SUBSET(W) = #lines through W.
Scanning every W_1 in F_q and taking the max multiplicity of
   v_B = -( (L_B)_2 + W_1 (L_B)_1 )
over the C(n, k-1) subsets gives the EXACT max of F_SUBSET over ALL q^2 word
classes -- and since F_LIST <= F_SUBSET, an exact upper bound on the flank max.
"""
import json, sys
from itertools import combinations

def is_prime(m):
    if m < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if m % p == 0: return m == p
    dd, s = m-1, 0
    while dd % 2 == 0: dd //= 2; s += 1
    for A in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(A, dd, m)
        if x in (1, m-1): continue
        for _ in range(s-1):
            x = x*x % m
            if x == m-1: break
        else: return False
    return True

def find_gen(q, n):
    co = (q-1)//n
    for g0 in range(2, 100000):
        g = pow(g0, co, q)
        if pow(g, n//2, q) != 1 and pow(g, n, q) == 1:
            if len({pow(g, i, q) for i in range(n)}) == n: return g
    raise RuntimeError

def main():
    n = int(sys.argv[1]); q = int(sys.argv[2])
    assert is_prime(q) and q % n == 1
    k = n//2
    g = find_gen(q, n); D = [pow(g, i, q) for i in range(n)]
    E1, E2 = [], []
    for B in combinations(range(n), k-1):
        c1 = 0; c2 = 0
        for i in B:
            x = D[i]
            c2 = (c2 - x*c1) % q
            c1 = (c1 - x) % q
        E1.append(c1); E2.append(c2)
    nb = len(E1)
    best = (0, None, None)
    hist_top = {}
    for W1 in range(q):
        cnt = {}
        for i in range(nb):
            v = (E2[i] + W1*E1[i]) % q
            cnt[v] = cnt.get(v, 0) + 1
        mx = 0; arg = 0
        for v, c in cnt.items():
            if c > mx: mx = c; arg = v
        hist_top[mx] = hist_top.get(mx, 0) + 1
        if mx > best[0]: best = (mx, W1, (-arg) % q)
    out = dict(n=n, q=q, k=k, subsets=nb, mean_per_class=nb/q,
               MAX_F_SUBSET_over_all_words=best[0],
               argmax_W1=best[1], argmax_W2=best[2],
               per_W1_max_histogram={str(a): b for a, b in sorted(hist_top.items())})
    print(json.dumps(out, indent=1))
    if len(sys.argv) > 3:
        with open(sys.argv[3], "w") as f: json.dump(out, f, indent=1)

if __name__ == "__main__":
    main()
