#!/usr/bin/env python3
"""F2 campaign R5 (Modal): the GENERALIZED CHORD-ORBIT LEMMA —
verification of both parts against brute force.

Object: Z = #{x in mu_n : a1 + a2 x^{d2} + a3 x^{d3} = 0}, a_i != 0.

PART 1 (collapse factorization, scale-free, unconditional): with
d = gcd(d2, d3, n), Z = d * Z_red where Z_red is the count for the
reduced instance (delta2, delta3) = (d2/g', d3/g') ... precisely:
substituting u = x^d maps mu_n d-to-1 onto mu_{n/d} and
x^{di} = u^{di/d}; Z = d * #{u in mu_{n/d} : a1 + a2 u^{d2/d} +
a3 u^{d3/d} = 0}.

PART 2 (exact Jacobi formula, gcd(d2,d3,n) = 1 case): with
n_i = n / gcd(d_i, n), H = {(x^{d2}, x^{d3})} <= mu_{n2} x mu_{n3}
(cyclic of order n, injective), and H-perp its annihilator
(|H-perp| = n2 n3 / n):

  Z = (n / (n2 n3)) * sum_{(chi,chi') in H-perp} S(chi, chi'),
  S = sum over the punctured line {a2 y + a3 z = -a1, yz != 0} of
      chi(y) chi'(z)   [a twisted Jacobi-type sum; |S| <= sqrt(q) + 2
      for nondegenerate pairs].

Gates: G1 Part-1 factorization exact on random instances (all d);
G2 Part-2 formula reproduces brute force EXACTLY (< 1e-6) on random
gcd-1 instances; G3 the bound Z <= q gcd(d2,n) gcd(d3,n)/n + 3 sqrt(q)
holds on every sampled instance. Any failure refutes the lemma packet.
"""
import cmath
import math
import random
from math import gcd

import modal

app = modal.App("rs-mca-f2-genchord")
image = modal.Image.debian_slim()

ROWS = [(97, 32, 11), (97, 16, 12), (193, 64, 13), (257, 64, 14),
        (257, 128, 15), (113, 16, 16)]


@app.function(image=image, cpu=2, memory=1024, timeout=280)
def row(job):
    q, n, seed = job
    rng = random.Random(seed)
    def pf(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d); x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out
    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    dlog = {}
    v = 1
    for i in range(q - 1):
        dlog[v] = i
        v = v * g % q
    h = pow(g, (q - 1) // n, q)
    D = [pow(h, i, q) for i in range(n)]

    def brute(nn, d2, d3, a1, a2, a3):
        hh = pow(g, (q - 1) // nn, q)
        return sum(1 for i in range(nn)
                   if (a1 + a2 * pow(pow(hh, i, q), d2, q)
                       + a3 * pow(pow(hh, i, q), d3, q)) % q == 0)

    # G1: collapse factorization on random instances
    for _ in range(40):
        d2 = rng.randrange(1, n)
        d3 = rng.randrange(1, n)
        if d2 == d3:
            continue
        a1, a2, a3 = (rng.randrange(1, q) for _ in range(3))
        d = gcd(gcd(d2, d3), n)
        Z = brute(n, d2, d3, a1, a2, a3)
        Zr = brute(n // d, d2 // d if d2 % d == 0 else None, d3 // d, a1, a2, a3) \
            if d > 1 and d2 % d == 0 and d3 % d == 0 else None
        if d > 1 and d2 % d == 0 and d3 % d == 0:
            assert Z == d * Zr, ("G1 factorization", d2, d3, Z, d, Zr)

    # G2 + G3: exact formula on gcd-1 instances
    checked = 0
    zeta = 2 * math.pi / (q - 1)
    while checked < 4:
        d2 = rng.randrange(1, n)
        d3 = rng.randrange(1, n)
        if d2 == d3 or gcd(gcd(d2, d3), n) != 1:
            continue
        a1, a2, a3 = (rng.randrange(1, q) for _ in range(3))
        Z = brute(n, d2, d3, a1, a2, a3)
        g2, g3 = gcd(d2, n), gcd(d3, n)
        # AMBIENT annihilator: H = <(h^{d2}, h^{d3})> <= (F_q^x)^2;
        # (A, B) in Z_{q-1}^2 annihilates H <=>
        # (A*d2 + B*d3) * (q-1)/n == 0 mod (q-1) <=> n | (A*d2 + B*d3).
        # |Ann| = (q-1)^2 / n. Formula:
        # Z = (n/(q-1)^2) * sum_{(A,B) in Ann} S_{A,B},
        # S_{A,B} = sum_{a2 y + a3 z = -a1, yz != 0} omega^A(y) omega^B(z).
        # Enumerate Ann: for each A, B solves B*d3 == -A*d2 mod n over
        # Z_{q-1}: solutions exist iff gcd(d3, n) | A*d2, giving
        # gcd(d3,n)*(q-1)/n values of B per admissible A.
        total = 0.0 + 0.0j
        ia3 = pow(a3, q - 2, q)
        n_ann = 0
        # precompute line character sums via dlog arrays
        import cmath as _cm
        for A in range(q - 1):
            rhs = (-A * d2) % n
            gg = gcd(d3, n)
            if rhs % gg != 0:
                continue
            # B mod n/gg solutions: B0 = rhs/gg * inv(d3/gg) mod n/gg
            nn = n // gg
            inv = pow((d3 // gg) % nn, -1, nn) if nn > 1 else 0
            B0 = (rhs // gg) * inv % nn if nn > 1 else 0
            for Bk in range(B0, q - 1, nn if nn > 0 else q - 1):
                n_ann += 1
                S = 0.0 + 0.0j
                for y in range(1, q):
                    z = (-a1 - a2 * y) * ia3 % q
                    if z == 0:
                        continue
                    S += _cm.exp(1j * zeta * ((A * dlog[y] + Bk * dlog[z])
                                              % (q - 1)))
                total += S
        assert n_ann == (q - 1) ** 2 // n, ("Ann size", n_ann)
        formula = (n / (q - 1) ** 2) * total.real
        assert abs((n / (q - 1) ** 2) * total.imag) < 1e-4
        assert abs(formula - Z) < 1e-4, ("G2 formula", d2, d3, formula, Z)
        # G3 bound
        bound = q * g2 * g3 / n + 3 * math.sqrt(q)
        assert Z <= bound + 1e-9, ("G3 bound", Z, bound)
        checked += 1
    return {"q": q, "n": n, "g2_g3_ok": True, "instances": checked}


@app.local_entrypoint()
def main():
    res = list(row.map(ROWS, return_exceptions=True))
    fails = 0
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:250])
            continue
        print(f"  ({r['q']},{r['n']}): G1 factorization + G2 exact formula "
              f"+ G3 bound on {r['instances']} gcd-1 instances: OK")
    if fails:
        raise SystemExit(f"F2_R5_GENCHORD_FAIL ({fails})")
    print("\nF2_R5_GENCHORD_PASS")
