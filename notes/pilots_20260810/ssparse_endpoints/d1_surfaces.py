"""D1 / P3 (S-ROT-EXP) and P4b (S-DEPTH structural collapse).

P3: in R_A = rem_{Y^N-delta}(Y^v P_A(Y)), the coefficients of R_A that sit
in quotient-degrees >= N/2 (hence in polynomial degrees >= k) are exactly
  J(v) = { j in [0,m] : (j+v) mod N in [N/2, N-1] }.
Pigeonhole cost = N^[0 in J] * q^(|J| - [0 in J] - [m in J])
(a_m = 1 is fixed; a_0 = (-1)^m prod(A) lies in a coset of size N).
Minimise over v.

P4b: the d=2 pigeonhole needs the class of (a_0,a_1).  a_0 is MULTIPLICATIVE
(N values) but a_1/a_0 = -sum_{b in A} b^{-1} is ADDITIVE.  Measure the exact
class profile at scaled parameters IN THE SAME REGIME as the razor row, i.e.
with C(N-1,m)/(N q) < 1 so the pigeonhole bound is vacuous, and see whether
the true largest class rescues it.
"""
import math
from itertools import combinations

# ---------------- P3 ----------------
print("=== P3 (S-ROT-EXP): constrained-coefficient count over all rotations v ===")
for (N, d) in [(256, 1), (128, 1), (256, 2), (512, 3), (64, 1)]:
    m = N // 2 + d
    best = None
    for v in range(N):
        J = [j for j in range(m + 1) if (j + v) % N >= N // 2]
        free = len(J) - (1 if 0 in J else 0) - (1 if m in J else 0)
        cost_bits = (math.log2(N) if 0 in J else 0.0) + 256.0 * free
        rec = (len(J), cost_bits, v, free, 0 in J, m in J)
        if best is None or (rec[1], rec[0]) < (best[1], best[0]):
            best = rec
    lj, cb, v, free, has0, hasm = best
    print(f"  N={N:<4} d={d}  m={m:<4} min|J| over v = {lj} (= d+1: {lj == d+1})"
          f"   argmin v = {v} (printed v = N-d = {N-d}: {v == N-d})")
    print(f"        min pigeonhole cost = {cb:.4f} bits"
          f"   (printed N*q^(d-1) = {math.log2(N) + 256*(d-1):.4f} bits)"
          f"   0 in J: {has0}, m in J: {hasm}")

# ---------------- P4b ----------------
print()
print("=== P4b (S-DEPTH): exact pigeonhole class profile, d=1 vs d=2 ===")


def is_prime(x):
    if x < 2:
        return False
    for p in range(2, int(x ** 0.5) + 1):
        if x % p == 0:
            return False
    return True


def find_q(N, lo):
    x = lo - lo % N + 1
    while True:
        if x > lo and is_prime(x):
            return x
        x += N


def order_n_coset(N, q):
    """the order-N subgroup of F_q^* (a multiplicative coset with y^N = 1)"""
    g = 2
    while pow(g, (q - 1) // 2, q) == 1 or pow(g, (q - 1) // 3, q) == 1 if (q - 1) % 3 == 0 \
            else pow(g, (q - 1) // 2, q) == 1:
        g += 1
    h = pow(g, (q - 1) // N, q)
    S = {pow(h, i, q) for i in range(N)}
    assert len(S) == N, (len(S), N)
    return sorted(S)


for N in (16, 20):
    for d in (1, 2):
        m = N // 2 + d
        nA = math.comb(N - 1, m)
        # choose q so that the razor regime is reproduced: C(N-1,m)/(N q^(d-1)) ...
        # for d=2 the razor row has C/(N q) < 1 (pigeonhole vacuous); match it.
        qmin = 4 * nA // N if d == 2 else N * 4
        q = find_q(N, max(qmin, 40))
        Q = order_n_coset(N, q)
        b0 = Q[0]
        rest = [b for b in Q if b != b0]
        inv = {b: pow(b, q - 2, q) for b in rest}
        h0, h1, hsum = {}, {}, {}
        sign = (-1) ** m
        for A in combinations(rest, m):
            p = 1
            si = 0
            s1 = 0
            for b in A:
                p = p * b % q
                si = (si + inv[b]) % q
                s1 = (s1 + b) % q
            a0 = sign * p % q
            a1 = (-a0) * si % q          # a_1 = -a_0 * sum b^{-1}
            h0[a0] = h0.get(a0, 0) + 1
            h1[(a0, a1)] = h1.get((a0, a1), 0) + 1
            hsum[s1] = hsum.get(s1, 0) + 1
        mx0, mx1, mxs = max(h0.values()), max(h1.values()), max(hsum.values())
        print(f"  N={N:<3} d={d}  m={m:<3} q={q:<6} #A=C({N-1},{m})={nA}")
        print(f"     a_0 classes (multiplicative): {len(h0):>6} distinct, "
              f"largest={mx0}, C(N-1,m)/N={nA/N:.4f}, ratio={mx0/(nA/N):.6f}")
        if d >= 2:
            print(f"     (a_0,a_1) classes            : {len(h1):>6} distinct, "
                  f"largest={mx1}, pigeonhole bound C/(N q)={nA/(N*q):.6f}")
        print(f"     e_1(A)=sum(A) classes (additive, the v=0 alternative): "
              f"{len(hsum):>6} distinct, largest={mxs}")
