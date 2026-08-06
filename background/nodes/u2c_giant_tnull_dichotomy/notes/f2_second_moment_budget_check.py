#!/usr/bin/env python3
"""F2 campaign: THE UNCONDITIONAL SECOND-MOMENT BUDGET (interior
chart, page five — first unconditional control of the summit field
at growing order).

THEOREM (from the L-function diagonalization, satellite 16): odd p,
G of index m, order f even. Then, with Q^ the quotient characters
and M = max_{chi in Q^, chi != 1} |L(1,chi)|:
  (i)  S is constant on cosets of G  (m distinct values);
  (ii) sum_t S(t)^2 = (f^2 p/(p-1)) sum_{chi != 1} |1-chi(2)|^2
       |L(1,chi)|^2   [exact];
  (iii) RMS_t S <= 2 sqrt(f) M sqrt(p/(p-1))  [unconditional; with
       the classical even-character bound M <= (1/2) log p + O(1)
       (explicit Louboutin-type constants), RMS <= ~sqrt(f) log p];
  (iv) EFFECTIVE INDEX: characters trivial on <G,2> contribute 0
       (their chi(2) = 1), so S descends to the quotient modulo the
       image of 2; effective dimension m - m/d, d = ord of 2 in the
       quotient group Z/m;
  (v)  Chebyshev: #{t : |S(t)| >= A} <= 4 f^2 (m-1) M^2 / A^2 * p/(p-1).

MEASURED alongside (pre-registered reads):
  - RMS/sqrt(f): if O(1) across growing (p, m), the effective
    L-constant is bounded and the second moment is BUDGET-SCALE
    (quotient characters behave like average characters); if it
    grows ~log p, the pointwise L-bound is being saturated (bank).
  - max/RMS over the m coset values: the pointwise-vs-mean gap that
    IS the remaining open content; slow growth (~sqrt(log m)) =
    Gaussian-like field (supports square-root-cancellation summit);
    growth ~sqrt(m) = adversarial field (falsifies the summit's
    spirit at these rows — bank loudly).
  - fraction of shifts with |S| > 10 nats (the per-condition budget
    scale): the exceptional-shift mass the consumer would need to
    tolerate on an average-case route.
  - sanity: every |L(1,chi)| <= (1/2) log p + 1.
"""
import math
import cmath

ROWS = [
    (97, 3), (331, 15), (7681, 15), (12289, 12),
    (40961, 10), (65537, 16), (65537, 256),
    (786433, 96), (786433, 768),
]


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


def row(p, m):
    f = (p - 1) // m
    if f % 2:
        print(f"(p={p}, m={m}): f odd — skipped")
        return True
    g = next(c for c in range(2, p)
             if all(pow(c, (p - 1) // r, p) != 1 for r in set(pf(p - 1))))
    dl = [0] * p
    v = 1
    for i in range(p - 1):
        dl[v] = i
        v = v * g % p
    # coset partial sums of L and ell over dl mod m  (O(p))
    TL = [0.0] * m
    TE = [0.0] * m
    for s in range(1, p):
        th = math.pi * s / p
        c = dl[s] % m
        TL[c] += math.log(abs(2 * math.cos(th)))
        TE[c] += math.log(2 * math.sin(th))
    d2 = dl[2] % m
    if d2 == 0:
        print(f"(p={p}, m={m}, f={f}): DEGENERATE (2 in G, S == 0 by "
              f"doubling law) — skipped as budget row")
        return True
    # S on coset c (rep g^c): S_c = sum_{i=c mod m} L over that coset
    # of the FULL group scaled... S_c = sum_{g' in G} L(rep*g') =
    # coset-L-sum directly: elements {s : dl[s] mod m == c} = rep*G.
    S = TL[:]  # exactly the coset sums
    m2 = f * sum(x * x for x in S)          # sum over all t
    mx = max(abs(x) for x in S)
    rms = math.sqrt(m2 / (p - 1))
    # quotient characters: a_j via O(m^2) DFT of coset sums
    w = cmath.exp(2j * math.pi / m)
    d = 1
    while pow(2, d * f, p) != 1 or (d2 * d) % m != 0:
        d += 1  # ord of 2 in quotient = smallest d with d*d2 = 0 mod m
    Lvals = []
    ok = True
    zeta_tau = None
    for j in range(1, m):
        aE = sum(w ** (-j * c) * TE[c] for c in range(m)) / (p - 1)
        # |tau(chi_j)| = sqrt(p)  =>  |L(1,chi_j)| = (p-1)|aE|/sqrt(p)
        Lj = (p - 1) * abs(aE) / math.sqrt(p)
        Lvals.append((j, Lj))
        if Lj > 0.5 * math.log(p) + 1:
            print(f"   !! |L(1,chi_{j})| = {Lj:.3f} exceeds "
                  f"(1/2)log p + 1 = {0.5*math.log(p)+1:.3f}")
            ok = False
        # (iv): chi(2) = 1  =>  a_j(L) must vanish
        if (j * d2) % m == 0:
            aL = sum(w ** (-j * c) * TL[c] for c in range(m)) / (p - 1)
            if abs(aL) > 1e-9:
                print(f"   !! effective-index violation: chi_{j}(2)=1 "
                      f"but |a_L| = {abs(aL):.2e}")
                ok = False
    # (ii) exact second moment from L-values with the |1-chi(2)| weights
    rhs = 0.0
    for j, Lj in Lvals:
        w2 = abs(1 - w ** (j * d2)) ** 2
        rhs += w2 * Lj * Lj
    rhs *= f * f * p / (p - 1)
    err2 = abs(m2 - rhs) / max(1e-30, abs(m2))
    M = max(Lj for _, Lj in Lvals)
    bound = 2 * math.sqrt(f) * M * math.sqrt(p / (p - 1))
    n_eff = m - m // d
    frac10 = f * sum(1 for x in S if abs(x) > 10) / (p - 1)
    print(f"(p={p}, m={m}, f={f}, eff dim {n_eff}): "
          f"RMS = {rms:7.3f}  RMS/sqrt(f) = {rms/math.sqrt(f):5.3f}  "
          f"max = {mx:7.3f}  max/RMS = {mx/max(rms,1e-30):5.2f}  "
          f"M = {M:5.3f}  RMS<=2sqrt(f)M: "
          f"{'OK' if rms <= bound + 1e-9 else 'VIOLATED'}  "
          f"P(|S|>10) = {frac10:.3f}  (ii)err = {err2:.1e}")
    return ok and rms <= bound + 1e-9 and err2 < 1e-8


def main():
    ok = all(row(p, m) for (p, m) in ROWS)
    if not ok:
        raise SystemExit("F2_SECOND_MOMENT_BUDGET_FAIL")
    print("\nF2_SECOND_MOMENT_BUDGET_PASS")


if __name__ == "__main__":
    main()
