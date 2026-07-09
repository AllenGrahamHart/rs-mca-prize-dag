#!/usr/bin/env python3
"""F2 campaign: THE L-FUNCTION DIAGONALIZATION of the summit's
deviation field (interior chart, page four; supersedes the C(r)
autocorrelation reduction of log #89 by full diagonalization).

CLAIM (pointwise exact): odd prime p, G <= (Z/p)^x of index m, order
f = (p-1)/m EVEN (so -1 in G and every quotient character is even).
Let S(t) = sum_{g in G} log|1 + zeta_p^{tg}|.  Then for EVERY t:

    S(t) = (f p / (p-1)) * sum_{chi in Q^, chi != 1}
             (1 - chi(2)) * (L(1, chi) / tau(chi)) * chi(t)

where Q^ = the m characters trivial on G (lifted quotient
characters), tau = Gauss sum, L(1, chi) = Dirichlet L at 1.
Consequences: (i) second moment = f^2 (p-1) sum |a_chi|^2 with
|a_chi| = sqrt(p) |1-chi(2)| |L(1,chi)| / (p-1); (ii) DOUBLING
VANISHING: 2 in G  =>  chi(2) = 1 for all chi in Q^  =>  S == 0
identically (one line: 2G = G so the two ell-sums cancel).

Proof chain being verified, link by link:
  A1. S(t) = f * sum_{j != 0} a_j(L) chi_j(t)      [orthogonality]
  A2. a_j(L) = (chi_j(2) - 1) * a_j(ell)           [1+x=(1-x^2)/(1-x)]
  A3. sum_t S(t)^2 = f^2 (p-1) sum_{j != 0} |a_j(L)|^2
  B.  a_j(ell) = -p L(1,chi_j) / ((p-1) tau(chi_j))   [classical
      even-character evaluation, Washington Thm 4.9 shape; verified
      against INDEPENDENT partial-sum L(1,chi) at p = 97, 257]
  C.  doubling rows (p=7, G=<2>), (p=73, G=<2>): S == 0 identically.

PRE-REGISTERED READ: all links < 1e-8 (A) / < 5e-3 (B, partial-sum
tail is O(sqrt(p) log p / N)) / < 1e-12 (C) => the diagonalization is
EXACT and the summit's open content IS the signed cancellation of an
L-value-weighted character sum. Any link failing => the chart's page
four is wrong; bank the failure verbatim.
"""
import math
import cmath

TOL_A = 1e-8
TOL_B = 5e-3
TOL_C = 1e-12


def pf(x):
    out, d = [], 2
    while d * d <= x:
        while x % d == 0:
            out.append(d)
            x //= d
        d += 1
    if x > 1:
        out.append(x)
    return out


def build(p):
    g = next(c for c in range(2, p)
             if all(pow(c, (p - 1) // r, p) != 1 for r in set(pf(p - 1))))
    dl = [0] * p
    v = 1
    for i in range(p - 1):
        dl[v] = i
        v = v * g % p
    L = [0.0] * p
    ell = [0.0] * p
    for s in range(1, p):
        L[s] = math.log(abs(2 * math.cos(math.pi * s / p)))
        ell[s] = math.log(2 * math.sin(math.pi * s / p))
    return g, dl, L, ell


def check_row(p, m):
    g, dl, L, ell = build(p)
    f = (p - 1) // m
    hG = pow(g, m, p)
    G = [pow(hG, i, p) for i in range(f)]
    in_G = (dl[2] % m == 0)
    w = cmath.exp(2j * math.pi / m)
    aL = [sum(w ** (-j * dl[s]) * L[s] for s in range(1, p)) / (p - 1)
          for j in range(m)]
    aE = [sum(w ** (-j * dl[s]) * ell[s] for s in range(1, p)) / (p - 1)
          for j in range(m)]
    # A1: pointwise reconstruction from quotient characters only
    errA1 = 0.0
    m2 = 0.0
    for t in range(1, p):
        S = sum(L[t * gg % p] for gg in G)
        m2 += S * S
        rec = f * sum(aL[j] * w ** (j * dl[t]) for j in range(1, m))
        errA1 = max(errA1, abs(S - rec))
    # A2: the chi(2)-1 factorization
    errA2 = max(abs(aL[j] - (w ** (j * dl[2]) - 1) * aE[j])
                for j in range(1, m))
    # A3: second moment
    rhs = f * f * (p - 1) * sum(abs(aL[j]) ** 2 for j in range(1, m))
    errA3 = abs(m2 - rhs) / max(1.0, abs(m2))
    print(f"(p={p}, m={m}, f={f}, 2 in G: {in_G}, "
          f"sqrt(2nd moment/(p-1)) = {math.sqrt(m2/(p-1)):.3f} nats): "
          f"A1 {errA1:.2e}  A2 {errA2:.2e}  A3 {errA3:.2e}")
    ok = errA1 < TOL_A and errA2 < TOL_A and errA3 < TOL_A
    return ok, (g, dl, ell, w, aE)


def check_classical(p, m, ctx, N=500_000):
    """B: a_j(ell) vs independent partial-sum L(1,chi_j)."""
    g, dl, ell, w, aE = ctx
    zeta = cmath.exp(2j * math.pi / p)
    ok = True
    for j in range(1, m):
        if (j * dl[p - 1]) % m != 0:
            continue  # odd character (never occurs for f even)
        tau = sum(w ** (j * dl[a]) * zeta ** a for a in range(1, p))
        L1 = 0.0 + 0.0j
        for n in range(1, N + 1):
            r = n % p
            if r:
                L1 += w ** (j * dl[r]) / n
        pred = -p * L1 / ((p - 1) * tau)
        err = abs(aE[j] - pred)
        errflip = abs(aE[j] + pred)
        print(f"   (p={p}, chi_{j}): |L(1,chi)| = {abs(L1):.6f}, "
              f"|tau|^2/p = {abs(tau)**2/p:.6f}, "
              f"classical-formula err = {err:.2e} (flipped {errflip:.2e})")
        ok = ok and err < TOL_B
    return ok


def check_doubling(p):
    g, dl, L, ell = build(p)
    G, v = [], 1
    while True:
        G.append(v)
        v = v * 2 % p
        if v == 1:
            break
    mx = max(abs(sum(L[t * gg % p] for gg in G)) for t in range(1, p))
    print(f"   doubling row (p={p}, G=<2>, f={len(G)}): "
          f"max_t |S(t)| = {mx:.2e}")
    return mx < TOL_C


def main():
    ok = True
    ctxs = {}
    for (p, m) in [(97, 3), (257, 4), (7681, 15)]:
        good, ctx = check_row(p, m)
        ok = ok and good
        ctxs[p] = (m, ctx)
    print("B: classical even-character evaluation vs partial sums:")
    for p in (97, 257):
        m, ctx = ctxs[p]
        ok = ok and check_classical(p, m, ctx)
    print("C: doubling-closure vanishing:")
    for p in (7, 73):
        ok = ok and check_doubling(p)
    if not ok:
        raise SystemExit("F2_LFUNC_DIAGONALIZATION_FAIL")
    print("\nF2_LFUNC_DIAGONALIZATION_PASS")


if __name__ == "__main__":
    main()
