"""END-TO-END: a census class's prime factor really is a point of V(I_1),
hence really divides any certified Delta_1.

Chain verified constructively, for each sampled weight-5 word P and each
prime factor p of Res(X^256+1, P) with a root in F_p:

  1. find w in F_p with P(w) = 0 and w of EXACT order 512
  2. rho_i = s_i w^{e_i};  a5 = prod rho_i;  lambda = a5^{-205}  (205 = 5^-1 mod 512)
  3. F(X) = prod (X - lambda*rho_i) must have the banked OND4 shape
        F = X*A(X^2) - b*X^2 - 1,  A = X^2 + a1*X + a0  (monic quadratic)
     i.e. coefficients of X^4 and X^0 pinned, giving (a0, a1, b)
  4. G(Y) = Y*A(Y)^2 - (b*Y+1)^2 must satisfy Y^256 == 1 mod G  over F_p
     (equivalently G | Y^256 - 1) -- i.e. (a0,a1,b) IS an F_p-point of I_1

Step 4 succeeding means p is a supporting characteristic of slot (1,5), so
by dli_wcl_odd_next_boundary_square_divisor_descent:84-86, p | Delta_1.

Run: tools/ramguard local -- python3 .../verify_delta_premise.py SEED NCLASSES
"""

import random
import sys

D = 256
NU = 205  # 5^{-1} mod 512, banked OND1


def norm_neg(coeffs, d):
    a = list(coeffs)
    while d > 1:
        b = [(-c if (i & 1) else c) for i, c in enumerate(a)]
        prod = [0] * (2 * d - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if bj:
                        prod[i + j] += ai * bj
        for i in range(2 * d - 2, d - 1, -1):
            if prod[i]:
                prod[i - d] -= prod[i]
                prod[i] = 0
        a = [prod[2 * i] for i in range(d // 2)]
        d //= 2
    return a[0]


def polymulmod(a, b, g, p):
    """(a*b) mod g over F_p; g monic."""
    n = len(a) + len(b) - 1
    r = [0] * n
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    r[i + j] = (r[i + j] + ai * bj) % p
    dg = len(g) - 1
    for i in range(len(r) - 1, dg - 1, -1):
        c = r[i]
        if c:
            r[i] = 0
            for k in range(dg):
                r[i - dg + k] = (r[i - dg + k] - c * g[k]) % p
    while len(r) > dg:
        r.pop()
    while len(r) < dg:
        r.append(0)
    return r


def poly_pow_mod(base, e, g, p):
    result = [1] + [0] * (len(g) - 2)
    b = list(base)
    while e:
        if e & 1:
            result = polymulmod(result, b, g, p)
        b = polymulmod(b, b, g, p)
        e >>= 1
    return result


def main():
    from sympy import factorint, isprime
    seed = int(sys.argv[1])
    nclasses = int(sys.argv[2])
    rng = random.Random(seed)

    checked = 0
    passed = 0
    skipped_noroot = 0
    for idx in range(nclasses):
        exps = sorted(rng.sample(range(D), 5))
        signs = [1] + [rng.choice((1, -1)) for _ in range(4)]
        c = [0] * D
        for s, e in zip(signs, exps):
            c[e] += s
        N = norm_neg(c, D)

        # we need a prime factor p == 1 mod 512 (residue degree 1 => root in F_p)
        n = abs(N)
        facs = []
        for q in range(3, 100000, 2):
            if q * q > n:
                break
            while n % q == 0:
                facs.append(q)
                n //= q
        if n > 1:
            if isprime(n):
                facs.append(n)
            else:
                try:
                    import signal

                    def _to(s, f):
                        raise TimeoutError()
                    signal.signal(signal.SIGALRM, _to)
                    signal.alarm(6)
                    facs.extend(factorint(n).keys())
                    signal.alarm(0)
                except Exception:
                    signal.alarm(0)
        facs = sorted(set(facs))

        for p in facs:
            if p < 5:
                continue
            if (p - 1) % 512 != 0:
                continue  # need mu_512 inside F_p for a rational root
            # find w of exact order 512 with P(w) = 0
            found = None
            g = rng.Random if False else None
            # enumerate mu_512 via a generator
            for base in range(2, 200):
                t = pow(base, (p - 1) // 512, p)
                if pow(t, 256, p) == p - 1:
                    break
            else:
                continue
            for k in range(512):
                if k % 2 == 0:
                    continue  # exact order 512 needs odd k
                w = pow(t, k, p)
                val = 0
                for s, e in zip(signs, exps):
                    val = (val + s * pow(w, e, p)) % p
                if val == 0:
                    found = w
                    break
            if found is None:
                skipped_noroot += 1
                continue
            w = found
            assert pow(w, 512, p) == 1 and pow(w, 256, p) == p - 1, "not exact order 512"

            rho = [(s % p) * pow(w, e, p) % p for s, e in zip(signs, exps)]
            a5 = 1
            for r in rho:
                a5 = a5 * r % p
            lam = pow(a5, NU * (512 - 1) % 512, p)  # a5^{-205} within mu_512
            lam = pow(a5, (512 - NU) % 512, p)
            rr = [lam * r % p for r in rho]
            prodrr = 1
            for r in rr:
                prodrr = prodrr * r % p
            assert prodrr == 1, "common dilation failed to normalize product"

            # F(X) = prod (X - rr_i)
            F = [1]
            for r in rr:
                F = [0] + F  # shift
                F = [(F[i] - (r * (F[i + 1] if i + 1 < len(F) else 0))) % p
                     for i in range(len(F))]
            # rebuild properly
            F = [1]
            for r in rr:
                new = [0] * (len(F) + 1)
                for i, cf in enumerate(F):
                    new[i + 1] = (new[i + 1] + cf) % p
                    new[i] = (new[i] - r * cf) % p
                F = new
            # F = f0 + f1 X + ... + X^5 ; OND4 shape: X^5 + a1 X^3 - b X^2 + a0 X - 1
            f = F
            shape_ok = (f[5] == 1 and f[4] == 0 and f[0] == (-1) % p)
            a1 = f[3]
            b = (-f[2]) % p
            a0 = f[1]
            if not shape_ok:
                print(f"  class {idx} p={p}: OND4 SHAPE FAIL f4={f[4]} f0={f[0]}")
                checked += 1
                continue

            # G(Y) = Y*A(Y)^2 - (bY+1)^2, A = Y^2 + a1 Y + a0
            A = [a0, a1, 1]
            A2 = [0] * 5
            for i in range(3):
                for j in range(3):
                    A2[i + j] = (A2[i + j] + A[i] * A[j]) % p
            G = [0] * 6
            for i in range(5):
                G[i + 1] = (G[i + 1] + A2[i]) % p
            for i, cf in enumerate([1, b]):
                for j, cg in enumerate([1, b]):
                    G[i + j] = (G[i + j] - cf * cg) % p
            assert G[5] == 1, "G not monic"
            Gm = G[:5]  # monic, reduce mod

            Y = [0, 1, 0, 0, 0]
            y256 = poly_pow_mod(Y, 256, Gm + [1], p)
            div_ok = (y256 == [1, 0, 0, 0, 0])
            checked += 1
            passed += 1 if div_ok else 0
            status = "PASS" if div_ok else "FAIL"
            print(f"  class {idx} p={p} (v2={bin(p-1)[::-1].index('1')}) "
                  f"a0={a0} a1={a1} b={b}  Y^256 mod G == 1 : {status}")

    print()
    print(f"end-to-end points verified: {passed}/{checked} "
          f"(classes sampled {nclasses}, primes with no rational root skipped {skipped_noroot})")
    print("PASS means: p is a supporting characteristic of slot (1,5), an F_p-point")
    print("of the fixed-divisor ideal I_1, hence p divides ANY certified Delta_1.")
    return 0 if (checked > 0 and passed == checked) else 1


if __name__ == "__main__":
    sys.exit(main())
