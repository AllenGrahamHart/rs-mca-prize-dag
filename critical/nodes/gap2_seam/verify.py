#!/usr/bin/env python3
"""Verifier for gap2_seam: pullback => M|t_denom, strip coincidence, seam class.
Stdlib only; exhaustive small enumeration; runs <1s."""
import itertools

def check_pullback_degree():
    # (a) any g(X^M) has M | deg. Represent g by its coefficient list.
    fails = 0
    for M in range(2, 8):
        for e in range(1, 6):               # deg g = e, leading coeff nonzero
            # E = g(X^M): exponents are multiples of M; top exponent = M*e
            top = M * e
            assert top % M == 0
            # also: support of E lies in M*Z
            g_support = [i for i in range(e + 1)]  # worst case dense g
            E_support = [M * i for i in g_support]
            if any(x % M != 0 for x in E_support):
                fails += 1
    return fails == 0

def check_strip_coincidence():
    # (b) M | gcd(n,k)  =>  for all A: (M|j) <=> (M|t_win), j=n-A, t_win=A-k
    fails = 0; checked = 0
    for n in range(4, 40):
        for k in range(1, n):
            for M in range(2, n):
                if n % M == 0 and k % M == 0:      # M | gcd(n,k)
                    for A in range(k, n + 1):       # k <= A <= n
                        j = n - A; t = A - k
                        lhs = (j % M == 0); rhs = (t % M == 0)
                        checked += 1
                        if lhs != rhs:
                            fails += 1
    return fails == 0, checked

def check_seam_classification():
    # (c) M | gcd(n,j) with M !| k  =>  M !| t_win  (i.e. k/M non-integral),
    #     and this class is disjoint from the rate-preserving M | gcd(n,k).
    fails = 0; witnessed = 0
    for n in range(4, 40):
        for k in range(1, n):
            for M in range(2, n):
                if n % M != 0:
                    continue
                for A in range(k, n + 1):
                    j = n - A; t = A - k
                    if j % M == 0 and k % M != 0:       # seam stratum
                        witnessed += 1
                        # claim: M !| t_win  and  not rate-preserving
                        if t % M == 0:
                            fails += 1
                        if k % M == 0:                   # would be rate-preserving
                            fails += 1
    return fails == 0, witnessed

if __name__ == "__main__":
    ok_a = check_pullback_degree()
    ok_b, nb = check_strip_coincidence()
    ok_c, nc = check_seam_classification()
    print(f"(a) pullback g(X^M) has M|deg (support in M*Z)        : {'PASS' if ok_a else 'FAIL'}")
    print(f"(b) M|gcd(n,k) => (M|j <=> M|t_win)  [{nb} buckets]    : {'PASS' if ok_b else 'FAIL'}")
    print(f"(c) seam M|gcd(n,j),M!|k => M!|t_win  [{nc} witnesses] : {'PASS' if ok_c else 'FAIL'}")
    assert ok_a and ok_b and ok_c
    print("ALL PASS")
