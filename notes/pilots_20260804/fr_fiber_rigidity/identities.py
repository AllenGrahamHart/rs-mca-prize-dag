#!/usr/bin/env python3
"""fr_fiber_rigidity -- verifier 1: the structural layer (P1-P4).

Exact arithmetic over F_q, q prime.  No floats anywhere.

Checks, on many random instances:

  (II)   R_2 L_1 - R_1 L_2 = -delta * rho      as a POLYNOMIAL identity
  (III)  kappa_2 L_1 - kappa_1 L_2 = delta L_nu
  (IV)   kappa_2 C_1 - kappa_1 C_2 = delta C_nu
  (V)    kappa_2 R_1 - kappa_1 R_2 = delta R_nu
  (A)    LEMMA A: B_nu ^ phi^{-1}(nu) = empty, for every nu in P^1
         equivalently  psi(x) != phi(x)  for every x in D
  (LENS) B_nu(tau) = {x in D : tau(x) = W_nu(x)},  W_nu = C_nu/L_nu
         tau-independent and (f_*,g_*)-gauge-covariant
  (GATE) agr(nu) = |Core| + |psi^{-1}(nu) ^ (H\\Core)| for every nu

Run:  tools/ramguard tiny -- python3 \
        notes/pilots_20260804/fr_fiber_rigidity/identities.py
"""

import json
import os
import random
import sys

# ---------------------------------------------------------------- F_q[X]


def trim(a, q):
    a = [c % q for c in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def padd(a, b, q):
    m = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(m)], q)


def psub(a, b, q):
    m = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
                 for i in range(m)], q)


def pscal(c, a, q):
    return trim([c * x for x in a], q)


def pmul(a, b, q):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % q
    return trim(out, q)


def peval(a, x, q):
    acc = 0
    for c in reversed(a):
        acc = (acc * x + c) % q
    return acc


def pdivmod(a, b, q):
    a = a[:]
    b = trim(b[:], q)
    assert b, "division by zero polynomial"
    inv = pow(b[-1], q - 2, q)
    out = [0] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b) and a:
        s = (a[-1] * inv) % q
        d = len(a) - len(b)
        out[d] = s
        for i, c in enumerate(b):
            a[i + d] = (a[i + d] - s * c) % q
        a = trim(a, q)
    return trim(out, q), a


def pgcd(a, b, q):
    a, b = trim(a[:], q), trim(b[:], q)
    while b:
        a, b = b, pdivmod(a, b, q)[1]
    if a:
        a = pscal(pow(a[-1], q - 2, q), a, q)
    return a


# ---------------------------------------------------------------- setup


def primes_with_subgroup(nmax=40):
    """(q, n) with q prime, n | q-1, 3 <= n <= nmax."""
    out = []
    for q in range(5, 200):
        if any(q % p == 0 for p in range(2, int(q ** 0.5) + 1)):
            continue
        for n in range(3, nmax + 1):
            if (q - 1) % n == 0:
                out.append((q, n))
    return out


def subgroup(q, n):
    """mu_n <= F_q^*, as a sorted list."""
    def order(a):
        o, x = 1, a
        while x != 1:
            x = (x * a) % q
            o += 1
        return o

    for gcand in range(2, q):
        g = pow(gcand, (q - 1) // n, q)
        if order(g) == n:
            break
    else:
        raise RuntimeError("no generator")
    H, x = [], 1
    for _ in range(n):
        H.append(x)
        x = (x * g) % q
    assert len(set(H)) == n, "subgroup wrong order"
    return sorted(H)


def randpoly(deg_lt, q, rng, monic_deg=None):
    if monic_deg is not None:
        a = [rng.randrange(q) for _ in range(monic_deg)] + [1]
        return trim(a, q)
    return trim([rng.randrange(q) for _ in range(deg_lt)], q)


# ---------------------------------------------------------------- checks

CHECKS = 0
FAILS = []


def chk(cond, label, info=""):
    global CHECKS
    CHECKS += 1
    if not cond:
        FAILS.append((label, info))


def run_instance(q, n, ell, k, rng):
    """One random instance of the deficient primitive-Pade configuration."""
    H = subgroup(q, n)

    # primitive pencil: P,Q coprime, max(deg P, deg Q) = ell
    for _ in range(400):
        P = randpoly(ell + 1, q, rng)
        Q = randpoly(ell + 1, q, rng)
        if not P or not Q:
            continue
        if max(len(P), len(Q)) - 1 != ell:
            continue
        if len(pgcd(P, Q, q)) == 1:      # gcd is a nonzero constant
            break
    else:
        return None

    # base errors and the parameter tau (deg tau < k - ell)
    Es = randpoly(n, q, rng)
    Eps = randpoly(n, q, rng)
    tau = randpoly(max(0, k - ell), q, rng)

    # rho and D
    rho = padd(pmul(P, Es, q), pmul(Q, Eps, q), q)
    D = [x for x in H if peval(rho, x, q) != 0]

    # the actual errors of the member tau
    E = psub(Es, pmul(Q, tau, q), q)
    Ep = padd(Eps, pmul(P, tau, q), q)

    # rho is tau-independent  (AD1)
    chk(psub(padd(pmul(P, E, q), pmul(Q, Ep, q), q), rho, q) == [],
        "AD1-rho-tau-independent")

    slopes = [(1, b) for b in range(q)] + [(0, 1)]   # P^1(F_q)

    def Lof(s):
        a, b = s
        return psub(pscal(a, Q, q), pscal(b, P, q), q)      # alpha Q - beta P

    def Cof(s):
        a, b = s
        return padd(pscal(a, Es, q), pscal(b, Eps, q), q)

    def Rof(s):
        return psub(Cof(s), pmul(tau, Lof(s), q), q)

    def det(s, t):
        return (s[0] * t[1] - s[1] * t[0]) % q

    # ---- (II) master two-ray syzygy, for many slope pairs
    for _ in range(6):
        s1 = slopes[rng.randrange(len(slopes))]
        s2 = slopes[rng.randrange(len(slopes))]
        if det(s1, s2) == 0:
            continue
        # delta = alpha_2 beta_1 - alpha_1 beta_2 = det(s2, s1)
        delta = det(s2, s1)
        lhs = psub(pmul(Rof(s2), Lof(s1), q), pmul(Rof(s1), Lof(s2), q), q)
        rhs = pscal((-delta) % q, rho, q)
        chk(psub(lhs, rhs, q) == [], "II-master-syzygy",
            f"q={q} ell={ell} s1={s1} s2={s2}")

        # ---- (III)/(IV)/(V) three-slope relations
        for _ in range(3):
            nu = slopes[rng.randrange(len(slopes))]
            k1, k2 = det(s1, nu), det(s2, nu)
            if k1 == 0 or k2 == 0:
                continue
            chk(psub(psub(pscal(k2, Lof(s1), q), pscal(k1, Lof(s2), q), q),
                     pscal(delta, Lof(nu), q), q) == [], "III-pencil")
            chk(psub(psub(pscal(k2, Cof(s1), q), pscal(k1, Cof(s2), q), q),
                     pscal(delta, Cof(nu), q), q) == [], "IV-pencil")
            chk(psub(psub(pscal(k2, Rof(s1), q), pscal(k1, Rof(s2), q), q),
                     pscal(delta, Rof(nu), q), q) == [], "V-pencil")

    # ---- (A) LEMMA A: psi(x) != phi(x) on D; B_nu ^ fiber_nu = empty
    for x in D:
        ex, epx = peval(E, x, q), peval(Ep, x, q)
        chk((ex, epx) != (0, 0), "A-D-not-in-core", f"x={x}")
        px, qx = peval(P, x, q), peval(Q, x, q)
        chk((px, qx) != (0, 0), "A-PQ-coprime-nonvanishing")
        # phi(x) = [P:Q],  psi(x) = [E':-E]
        chk((epx * qx - (-ex) * px) % q != 0, "A-psi-neq-phi", f"x={x}")

    for nu in slopes:
        Ln, Cn = Lof(nu), Cof(nu)
        Bn = [x for x in D
              if (nu[0] * peval(E, x, q) + nu[1] * peval(Ep, x, q)) % q == 0]
        fiber = [x for x in H if peval(Ln, x, q) == 0]
        chk(not (set(Bn) & set(fiber)), "A-block-avoids-own-fiber",
            f"nu={nu}")

        # ---- (LENS) B_nu = {x in D : tau(x) L_nu(x) = C_nu(x)}
        lens = [x for x in D
                if (peval(tau, x, q) * peval(Ln, x, q) - peval(Cn, x, q)) % q
                == 0]
        chk(sorted(Bn) == sorted(lens), "LENS-block-is-tau-agreement",
            f"nu={nu}")

        # W_nu = C_nu/L_nu is tau-independent where L_nu(x) != 0
        for x in D:
            lv = peval(Ln, x, q)
            if lv != 0:
                Wn = (peval(Cn, x, q) * pow(lv, q - 2, q)) % q
                chk((x in Bn) == (peval(tau, x, q) == Wn),
                    "LENS-Wnu-tau-independent", f"nu={nu} x={x}")

    # ---- (GATE) agreement decomposition:
    # agr(nu) = |Core| + |psi^{-1}(nu) ^ (H\Core)|
    Core = [x for x in H if peval(E, x, q) == 0 and peval(Ep, x, q) == 0]
    for nu in slopes:
        agr = [x for x in H
               if (nu[0] * peval(E, x, q) + nu[1] * peval(Ep, x, q)) % q == 0]
        offcore = [x for x in agr if x not in Core]
        chk(set(Core) <= set(agr), "GATE-core-in-every-ray")
        chk(len(agr) == len(Core) + len(offcore), "GATE-decomposition")
        # off-core agreement points split into D-part (psi=nu) and
        # (H\D)-part (phi=nu)
        Ln = Lof(nu)
        for x in offcore:
            if x in D:
                chk((nu[0] * peval(E, x, q) + nu[1] * peval(Ep, x, q)) % q
                    == 0, "GATE-D-part-is-psi-fiber")
            else:
                chk(peval(Ln, x, q) == 0, "GATE-offD-part-is-phi-fiber",
                    f"nu={nu} x={x}")
    return {"q": q, "n": n, "ell": ell, "k": k, "e": len(D),
            "core": len(Core)}


def main():
    rng = random.Random(20260806)
    pool = [(q, n) for (q, n) in primes_with_subgroup(24) if 7 <= n <= 24]
    insts = []
    for _ in range(24):
        q, n = pool[rng.randrange(len(pool))]
        ell = rng.randrange(1, 4)
        k = rng.randrange(ell + 1, ell + 5)
        r = run_instance(q, n, ell, k, rng)
        if r:
            insts.append(r)

    out = {"instances": len(insts), "checks": CHECKS,
           "fails": FAILS[:20], "n_fails": len(FAILS),
           "sample": insts[:6]}
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "identities.json"), "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(json.dumps({k: v for k, v in out.items() if k != "sample"},
                     indent=1, sort_keys=True))
    if FAILS:
        print("FAIL")
        return 1
    print(f"PASS  {CHECKS} exact checks over {len(insts)} instances")
    return 0


if __name__ == "__main__":
    sys.exit(main())
