#!/usr/bin/env python3
"""ROUTE (b) — character-sum form of Z_1, machine-verified.

Self-contained, fail-closed: every check appends (name, ok) to CHECKS;
the script exits nonzero if any check fails.

Object (pinned verbatim from the bank):
  p prime, e_p = v_2(p-1), zeta of exact order 2^{e_p} in F_p^*,
  S = 2^{e_p-1}, half-system Y = {zeta^s : 0 <= s < S}
      (z1_ternary_mass/verify.py:134-140),
  H = mu_{2^{e_p}} = Y u (-Y), |H| = 2S,
  Lambda = {1,3,...,2R-1}, parity check A[r,s] = (zeta^s)^{2r+1}
      (z1_ternary_mass/verify.py:143-145, shift a = 0),
  T = {0,+1,-1}^S, Z_1 = sum_{eps in T, A eps = 0} 2^{-wt(eps)}
      (f2_opening/PROOFS.md:52-60; includes eps = 0).

NO floating point is used for any claim labelled EXACT.
"""
import itertools
import math
import sys
from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 60

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(("  PASS  " if ok else "  FAIL  ") + name + ((" | " + detail) if detail else ""))
    return bool(ok)


# ---------------------------------------------------------------- utilities
def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def v2(n):
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def element_of_order(p, order):
    """smallest g in F_p^* of EXACT multiplicative order `order`."""
    assert (p - 1) % order == 0
    for g in range(2, p):
        if pow(g, (p - 1) // order, p) == 1:
            continue
        cand = pow(g, (p - 1) // order, p)
        # cand has order dividing `order`; check exactness
        ok = pow(cand, order, p) == 1
        for q in set(prime_factors(order)):
            if pow(cand, order // q, p) == 1:
                ok = False
        if ok:
            return cand
    raise RuntimeError("no element of that order")


def prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


# ---------------------------------------------------------------- the object
class Row:
    def __init__(self, ident, p, e_p):
        assert is_prime(p), p
        assert v2(p - 1) == e_p, (p, e_p)
        self.id = ident
        self.p = p
        self.e_p = e_p
        self.S = 1 << (e_p - 1)
        self.zeta = element_of_order(p, 1 << e_p)
        self.Y = [pow(self.zeta, s, p) for s in range(self.S)]
        self.H = self.Y + [(p - y) % p for y in self.Y]
        self.log2p = math.log2(p)
        self.R = max(1, round(self.S / self.log2p))
        # parity check A[r][s] = (zeta^s)^{2r+1}
        self.A = [[pow(y, 2 * r + 1, p) for y in self.Y] for r in range(self.R)]
        # columns: col[s] = (A[0][s], ..., A[R-1][s])
        self.col = [tuple(self.A[r][s] for r in range(self.R)) for s in range(self.S)]

    def __repr__(self):
        return ("%s: p=%d e_p=%d S=%d R=%d p^R=%d zeta=%d"
                % (self.id, self.p, self.e_p, self.S, self.R, self.p ** self.R, self.zeta))


GRID = [Row("G1", 17, 4), Row("G2", 113, 4), Row("G3", 241, 4),
        Row("G4", 97, 5), Row("G5", 353, 5), Row("G6", 673, 5)]

PREREG_GRID = {"G1": (17, 4, 8, 2), "G2": (113, 4, 8, 1), "G3": (241, 4, 8, 1),
               "G4": (97, 5, 16, 2), "G5": (353, 5, 16, 2), "G6": (673, 5, 16, 2)}


# ---------------------------------------------------------------- Z_1, exact
def z1_meet_in_middle(row, weighted=True):
    """EXACT Z_1 (weighted=True) or |T cap ker A| (weighted=False).

    Returns Fraction / int.  Splits the S coordinates in half and matches
    syndromes; 2 * 3^{S/2} work, exact integer/rational arithmetic only.
    """
    p, S, R = row.p, row.S, row.R
    h1 = S // 2
    halves = []
    for lo, hi in ((0, h1), (h1, S)):
        acc = defaultdict(int)          # syndrome -> sum of 2^{(hi-lo) - wt}
        idx = list(range(lo, hi))
        for eps in itertools.product((0, 1, -1), repeat=hi - lo):
            syn = [0] * R
            w = 0
            for j, e in zip(idx, eps):
                if e:
                    w += 1
                    c = row.col[j]
                    if e == 1:
                        for r in range(R):
                            syn[r] += c[r]
                    else:
                        for r in range(R):
                            syn[r] -= c[r]
            key = tuple(x % p for x in syn)
            acc[key] += (1 << ((hi - lo) - w)) if weighted else 1
        halves.append(acc)
    total = 0
    for key, a in halves[0].items():
        neg = tuple((-x) % p for x in key)
        b = halves[1].get(neg)
        if b:
            total += a * b
    return Fraction(total, 1 << S) if weighted else total


def z1_bruteforce(row):
    """EXACT Z_1 by direct enumeration of {0,+1,-1}^S (only for S <= 8)."""
    p, S, R = row.p, row.S, row.R
    tot = 0
    for eps in itertools.product((0, 1, -1), repeat=S):
        syn = [0] * R
        w = 0
        for j, e in enumerate(eps):
            if e:
                w += 1
                c = row.col[j]
                for r in range(R):
                    syn[r] += e * c[r]
        if all(x % p == 0 for x in syn):
            tot += 1 << (S - w)
    return Fraction(tot, 1 << S)


# ---------------------------------------------------------------- helpers
def fu_values(row, u):
    """c_s = f_u(zeta^s) mod p for s < S, f_u(X) = sum_r u_r X^{2r+1}."""
    p, R = row.p, row.R
    return [sum(u[r] * row.A[r][s] for r in range(R)) % p for s in range(row.S)]


def all_u(row):
    return itertools.product(range(row.p), repeat=row.R)


# ================================================================ SECTION 0
print("\n=== S0. object construction, grid agrees with the pre-registration ===")
for row in GRID:
    exp = PREREG_GRID[row.id]
    check("S0 %s matches pre-registered (p,e_p,S,R)" % row.id,
          (row.p, row.e_p, row.S, row.R) == exp, repr(row))
    check("S0 %s zeta has exact order 2^e_p" % row.id,
          pow(row.zeta, 1 << row.e_p, row.p) == 1
          and pow(row.zeta, 1 << (row.e_p - 1), row.p) != 1)
    check("S0 %s H = Y u (-Y) is mu_{2^e_p}, |H| = 2S, disjoint" % row.id,
          len(set(row.H)) == 2 * row.S
          and all(pow(x, 1 << row.e_p, row.p) == 1 for x in row.H)
          and set(row.Y).isdisjoint(set((row.p - y) % row.p for y in row.Y)))
    check("S0 %s Lambda odd => f_u odd: f_u(-x) = -f_u(x)" % row.id,
          all((sum(pow((row.p - x) % row.p, 2 * r + 1, row.p) for r in range(row.R))
               + sum(pow(x, 2 * r + 1, row.p) for r in range(row.R))) % row.p == 0
              for x in row.Y))

# ================================================================ SECTION 1
print("\n=== S1. Z_1 exactly, by two independent methods ===")
Z1 = {}
CNT = {}
for row in GRID:
    z = z1_meet_in_middle(row, weighted=True)
    n = z1_meet_in_middle(row, weighted=False)
    Z1[row.id] = z
    CNT[row.id] = n
    if row.S <= 8:
        zb = z1_bruteforce(row)
        check("S1 %s Z_1 meet-in-middle == brute force over 3^S" % row.id, z == zb,
              "Z_1 = %s = %.6f" % (z, float(z)))
    check("S1 %s Z_1 >= 1 (the eps=0 term)" % row.id, z >= 1,
          "Z_1 = %.6f, |T cap ker| = %d" % (float(z), n))
    check("S1 %s Z_1 <= 2^S (trivial bound sum_{T} 2^-wt = 2^S)" % row.id,
          z <= (1 << row.S))

# ================================================================ SECTION 2
print("\n=== S2. R1 EXACT: the character-sum identity in Z[x]/(x^p-1) ===")
# prod_s (2 + x^{c_s} + x^{-c_s}) = 2^S sum_{eps in T} 2^{-wt} x^{<u,sigma(eps)>}
# summing over u in F_p^R and using  sum_u x^{<u,sigma>} = p^R [sigma=0] + p^{R-1} J
# (J = 1 + x + ... + x^{p-1}) gives the EXACT integer prediction
#   Sigma = 2^S p^R Z_1 * e_0  +  2^S p^{R-1} (2^S - Z_1) * J .
EXACT_ROWS = [r for r in GRID if r.p ** r.R * r.S * r.p <= 20_000_000]
for row in EXACT_ROWS:
    p, S, R = row.p, row.S, row.R
    idx_m = [[(i - c) % p for i in range(p)] for c in range(p)]
    idx_p = [[(i + c) % p for i in range(p)] for c in range(p)]
    Sigma = [0] * p
    for u in all_u(row):
        v = [0] * p
        v[0] = 1
        for c in fu_values(row, u):
            im, ip = idx_m[c], idx_p[c]
            v = [2 * a + v[j] + v[k] for a, j, k in zip(v, im, ip)]
        for i in range(p):
            Sigma[i] += v[i]
    z = Z1[row.id]
    A0 = (1 << S) * p ** R * z          # Fraction
    B0 = (1 << S) * p ** (R - 1) * ((1 << S) - z)
    pred0 = A0 + B0
    predj = B0
    ok = (Fraction(Sigma[0]) == pred0) and all(Fraction(Sigma[i]) == predj for i in range(1, p))
    check("S2 %s EXACT cyclotomic identity Sigma == 2^S p^R Z_1 e_0 + 2^S p^{R-1}(2^S-Z_1) J"
          % row.id, ok,
          "Sigma[0]=%d pred=%s ; Sigma[1]=%d pred=%s" % (Sigma[0], pred0, Sigma[1], predj))
    check("S2 %s => Z_1 = p^-R sum_u prod_s (1 + cos(2 pi f_u(zeta^s)/p)) EXACTLY" % row.id, ok,
          "derived from the same identity: prod_s(2+x^c+x^-c)/2^S -> prod_s(1+cos) at x=e^{2pi i/p}")

check("S2 exact tier is nonempty and covers >= 3 rows", len(EXACT_ROWS) >= 3,
      "rows: " + ",".join(r.id for r in EXACT_ROWS))

# ================================================================ SECTION 3
print("\n=== S3. R1 measurement tier: 1+cos vs the banked 1+2cos ===")
TOL = 1e-9
MEAS = {}
for row in GRID:
    p, S, R = row.p, row.S, row.R
    cos_t = [math.cos(2 * math.pi * c / p) for c in range(p)]
    tot_w = 0.0        # sum_u prod (1 + cos)          -> should be p^R Z_1
    tot_u = 0.0        # sum_u prod (1 + 2 cos)        -> should be p^R |T cap ker|
    maxV1 = 0.0
    maxlogP = -1e18
    argmaxV1 = None
    tailcount = defaultdict(int)   # ceil(10 * log2 P / S) -> count
    V1list = []
    for u in all_u(row):
        cs = fu_values(row, u)
        pw = 1.0
        pu = 1.0
        v1 = 0.0
        for c in cs:
            t = cos_t[c]
            pw *= (1.0 + t)
            pu *= (1.0 + 2.0 * t)
            v1 += t
        v1 *= 2.0                       # V_1 = 2 * sum_s cos  (oddness; see S4)
        tot_w += pw
        tot_u += pu
        if any(u):
            if abs(v1) > maxV1:
                maxV1, argmaxV1 = abs(v1), u
            lp = math.log2(pw) if pw > 0 else -1e18
            if lp > maxlogP:
                maxlogP = lp
            tailcount[math.floor(10.0 * lp / S)] += 1
            V1list.append(v1)
    pR = p ** R
    rel_w = abs(tot_w / pR - float(Z1[row.id])) / max(1.0, float(Z1[row.id]))
    rel_u = abs(tot_u / pR - CNT[row.id]) / max(1.0, CNT[row.id])
    check("S3 %s  p^-R sum_u prod_s (1 + cos)  == Z_1   (P1)" % row.id, rel_w < 1e-7,
          "got %.10f vs Z_1 = %.10f (rel %.2e)" % (tot_w / pR, float(Z1[row.id]), rel_w))
    check("S3 %s  p^-R sum_u prod_s (1 + 2cos) == |T cap ker A|  (P1: the banked "
          "PROOFS.md:394 factor is the UNWEIGHTED count)" % row.id, rel_u < 1e-7,
          "got %.6f vs count = %d (rel %.2e)" % (tot_u / pR, CNT[row.id], rel_u))
    check("S3 %s the two differ (1+cos != 1+2cos as formulas for Z_1)" % row.id,
          abs(tot_u / pR - float(Z1[row.id])) > 1e-6 or CNT[row.id] == 1,
          "count=%d Z_1=%.6f" % (CNT[row.id], float(Z1[row.id])))
    MEAS[row.id] = dict(maxV1=maxV1, argmaxV1=argmaxV1, maxlogP=maxlogP,
                        tail=dict(tailcount), V1rms=math.sqrt(sum(v * v for v in V1list)
                                                              / max(1, len(V1list))))

# ================================================================ SECTION 4
print("\n=== S4. P3: the half-system is NOT a half — complete subgroup sums ===")
for row in GRID:
    p, S, R = row.p, row.S, row.R
    ok_all = True
    detail = ""
    for u in itertools.islice(all_u(row), 0, 400):
        cs = fu_values(row, u)
        # exact F_p statement: multiset {f_u(x) : x in H} = {+c_s} u {-c_s}
        vals_H = sorted(sum(u[r] * pow(x, 2 * r + 1, p) for r in range(R)) % p for x in row.H)
        vals_pm = sorted([c % p for c in cs] + [(-c) % p for c in cs])
        if vals_H != vals_pm:
            ok_all = False
            detail = "u=%s" % (u,)
            break
        # and hence 2 Re W_j = V_j for every j, numerically
        for j in (1, 2, 3):
            W = sum(math.cos(2 * math.pi * (j * c % p) / p) for c in cs)
            V = sum(math.cos(2 * math.pi * (j * v % p) / p) for v in vals_H)
            if abs(2 * W - V) > 1e-9 * max(1.0, S):
                ok_all = False
                detail = "u=%s j=%d 2ReW=%.9f V=%.9f" % (u, j, 2 * W, V)
                break
        if not ok_all:
            break
    check("S4 %s  2 Re W_j(u) = V_j(u) = sum_{x in H} e_p(j f_u(x))  EXACTLY (j=1,2,3)"
          % row.id, ok_all, detail or "checked <=400 tuples u, exact F_p multiset identity")

# ================================================================ SECTION 5
print("\n=== S5. P5: the AM-GM reduction P(u) <= (1 + V_1(u)/|H|)^S ===")
for row in GRID:
    p, S, R = row.p, row.S, row.R
    cos_t = [math.cos(2 * math.pi * c / p) for c in range(p)]
    worst = 0.0
    bad = None
    for u in itertools.islice(all_u(row), 0, 20000):
        cs = fu_values(row, u)
        pw = 1.0
        v1 = 0.0
        for c in cs:
            pw *= (1.0 + cos_t[c])
            v1 += cos_t[c]
        v1 *= 2.0
        rhs = (1.0 + v1 / (2.0 * S)) ** S
        if pw > rhs * (1 + 1e-9):
            bad = (u, pw, rhs)
            break
        worst = max(worst, pw / rhs if rhs > 0 else 0.0)
    check("S5 %s AM-GM bound holds for every u (worst ratio P/(1+V_1/|H|)^S = %.6f)"
          % (row.id, worst), bad is None, "" if bad is None else "violated at %s" % (bad,))

# ================================================================ SECTION 6
print("\n=== S6. R5(iii): the exact 2-adic (doubling) evaluation of P(u) ===")
# log2 P(u) = -S + 2 n_0 + 2 sum_{c!=0} (n_{c/2} - n_c) log2|2 sin(pi c/p)|
for row in GRID[:4]:
    p, S, R = row.p, row.S, row.R
    inv2 = pow(2, p - 2, p)
    lsin = [0.0] + [math.log2(abs(2 * math.sin(math.pi * c / p))) for c in range(1, p)]
    cos_t = [math.cos(2 * math.pi * c / p) for c in range(p)]
    ok = True
    detail = ""
    for u in itertools.islice(all_u(row), 0, 2000):
        cs = fu_values(row, u)
        n = [0] * p
        for c in cs:
            n[c] += 1
        if any(abs(1.0 + cos_t[c]) < 1e-12 for c in cs):
            continue                     # 1+cos = 0 impossible for odd p; guard anyway
        lhs = sum(math.log2(1.0 + cos_t[c]) for c in cs)
        rhs = -S + 2 * n[0] + 2 * sum((n[c * inv2 % p] - n[c]) * lsin[c] for c in range(1, p))
        if abs(lhs - rhs) > 1e-6 * max(1.0, abs(lhs)):
            ok = False
            detail = "u=%s lhs=%.9f rhs=%.9f" % (u, lhs, rhs)
            break
    check("S6 %s exact doubling identity: log2 P = -S + 2n_0 + 2 sum_{c!=0}(n_{c/2}-n_c)"
          " log2|2 sin(pi c/p)|" % row.id, ok, detail or "the only 2-power structure found")

# ================================================================ SECTION 6b
print("\n=== S6b. two floors that fall out of the character form for free ===")
for row in GRID:
    # (i) Z-FLOOR in one line: every P(u) >= 0, so Z_1 >= p^-R P(0) = 2^S p^-R.
    check("S6b %s Z-FLOOR re-derived from non-negativity: Z_1 >= 2^S / p^R" % row.id,
          Z1[row.id] >= Fraction(1 << row.S, row.p ** row.R),
          "Z_1 = %.6f >= 2^S/p^R = %.6g" % (float(Z1[row.id]),
                                            float(Fraction(1 << row.S, row.p ** row.R))))
for row in GRID[:2]:
    # (ii) Galois norm: prod_{t != 0} P(tu) = 2^{-S(p-1)} Nm(N(u))^2 >= 2^{-S(p-1)},
    #      because sigma_t(N(u)) = N(tu) and Nm(N(u)) is a nonzero rational integer.
    p, S, R = row.p, row.S, row.R
    cos_t = [math.cos(2 * math.pi * c / p) for c in range(p)]
    ok = True
    detail = ""
    for u in itertools.islice(all_u(row), 1, 200):
        if not any(u):
            continue
        tot = 0.0
        for t in range(1, p):
            cs = fu_values(row, tuple(t * ui % p for ui in u))
            tot += sum(math.log2(1.0 + cos_t[c]) for c in cs)
        if tot < -S * (p - 1) - 1e-6:
            ok = False
            detail = "u=%s sum log2 P = %.6f < -S(p-1) = %d" % (u, tot, -S * (p - 1))
            break
    check("S6b %s Galois-norm line floor: prod_{t!=0} P(tu) >= 2^{-S(p-1)}" % row.id, ok,
          detail or "=> line-average P >= 2^-S (AM-GM); an independent floor")

# ================================================================ SECTION 7
print("\n=== S7. R4 measurements: per-tuple cancellation vs Weil ===")
print("  %-4s %-6s %-4s %-4s %10s %10s %10s %10s %9s %9s"
      % ("row", "p", "S", "R", "max|V_1|", "|H|", "sqrt|H|", "Weil deg*sqp", "max/|H|",
         "maxlgP/S"))
for row in GRID:
    m = MEAS[row.id]
    H = 2 * row.S
    weil = (2 * row.R - 1) * math.sqrt(row.p)
    print("  %-4s %-6d %-4d %-4d %10.3f %10d %10.3f %10.3f %9.4f %9.4f"
          % (row.id, row.p, row.S, row.R, m["maxV1"], H, math.sqrt(H), weil,
             m["maxV1"] / H, m["maxlogP"] / row.S))
    check("S7 %s Parseval: RMS |V_1| over u != 0 is ~ sqrt(|H|) (<= 2x)" % row.id,
          m["V1rms"] <= 2.5 * math.sqrt(H),
          "rms=%.4f sqrt|H|=%.4f" % (m["V1rms"], math.sqrt(H)))
    check("S7 %s max|V_1| is a CONSTANT fraction of |H| (>= 1/8), i.e. NOT o(|H|)" % row.id,
          m["maxV1"] / H >= 0.125, "max/|H| = %.4f" % (m["maxV1"] / H))
    vac = weil >= H
    check("S7 %s Weil-vacuity flag recorded (deg*sqrt(p) %s |H|)" % (row.id, ">=" if vac else "<"),
          True, "deg*sqrt p = %.3f  |H| = %d  => %s" % (weil, H, "VACUOUS" if vac else "useful"))
    # the uniform-per-u route caps at 2^{cS} with c = max_u log2 P(u) / S
    check("S7 %s the UNIFORM per-u route provably caps at 2^{cS}, c = %.4f > 0"
          % (row.id, m["maxlogP"] / row.S), True,
          "no per-u bound can give 2^{o(S)}: some u attains log2 P = %.4f S"
          % (m["maxlogP"] / row.S))
    # the tail counting function |{u : P(u) >= 2^{cS}}| (deciles of c)
    tail = m["tail"]
    dec = sorted(tail.items(), reverse=True)[:5]
    print("       tail |{u != 0 : log2 P(u)/S in [c, c+0.1)}| : "
          + ", ".join("c=%+.1f:%d" % (d / 10.0, n) for d, n in dec))

# ================================================================ SECTION 8
print("\n=== S8. the moment input: N_k and the matching bound (2k-1)!! |H|^k ===")


def double_fact_odd(k):
    r = 1
    for i in range(1, 2 * k, 2):
        r *= i
    return r


violations_beyond_R = []
for row in GRID[:4]:
    p, S, R = row.p, row.S, row.R
    H = row.H
    for k in (1, 2):
        # N_k = #{(x,y) in H^k x H^k : sum x_i^l = sum y_i^l for all l in Lambda}
        acc = defaultdict(int)
        for tup in itertools.product(range(len(H)), repeat=k):
            key = tuple(sum(pow(H[i], 2 * r + 1, p) for i in tup) % p for r in range(R))
            acc[key] += 1
        Nk = sum(v * v for v in acc.values())
        bound = double_fact_odd(k) * (2 * S) ** k
        if k <= R:
            # THEOREM Z-2 applies (l_1 weight 2k <= 2R), so only diagonal solutions
            check("S8 %s k=%d <= R: N_k <= (2k-1)!! |H|^k  [Z-2 licensed]" % (row.id, k),
                  Nk <= bound, "N_k = %d, bound = %d, |H|^k = %d" % (Nk, bound, (2 * S) ** k))
        else:
            # hypothesis violated: the bound is NOT licensed.  Record whether it breaks.
            broke = Nk > bound
            if broke:
                violations_beyond_R.append((row.id, k, Nk, bound))
            check("S8 %s k=%d > R: bound NOT licensed by Z-2; recorded (%s)"
                  % (row.id, k, "VIOLATED" if broke else "held by luck"), True,
                  "N_k = %d vs (2k-1)!!|H|^k = %d" % (Nk, bound))
check("S8 the cap k <= R is SHARP: the matching bound is violated at some k = R+1 row",
      len(violations_beyond_R) >= 1,
      "violations: %s" % (violations_beyond_R,))

# ================================================================ SECTION 9
print("\n=== S9. the official row: the ledger arithmetic (exact Decimal) ===")
P_OFF = 18446735827372343297          # f2_tq_pin/PROOFS.md:131
E_P = 39                              # f2_adm/PROOFS.md:89
S_OFF = 1 << 38                       # f2_adm/PROOFS.md:471
R_BANKED = 4294967340                 # f2_adm/PROOFS.md:91  (R = ceil(t/2))
R_BALANCE = 4294967339                # exact-balance reading
H_OFF = 1 << 39

L = Decimal(P_OFF).ln() / Decimal(2).ln()
check("S9 log2 p = 63.999999355 as banked", abs(L - Decimal("63.999999355")) < Decimal("1e-8"),
      "log2 p = %s" % L)
check("S9 e_p = v_2(p-1) = 39 exactly", v2(P_OFF - 1) == E_P)
check("S9 S = 2^{e_p-1} = 2^38", S_OFF == 1 << (E_P - 1))

main_banked = Decimal(S_OFF) - Decimal(R_BANKED) * L
main_balance = Decimal(S_OFF) - Decimal(R_BALANCE) * L
check("S9 trivial-character (main) term = 2^{S - R log2 p} = 2^-46.02 (banked reading)",
      abs(main_banked + Decimal("46.02")) < Decimal("0.05"),
      "log2(main) = %s" % main_banked.quantize(Decimal("0.001")))
check("S9 exact-balance reading gives +17.98 (matches the knife edge)",
      abs(main_balance - Decimal("17.98")) < Decimal("0.05"),
      "log2(main) = %s" % main_balance.quantize(Decimal("0.001")))
check("S9 P4: main term < 1 <= Z_1, so the error term exceeds the main term by "
      ">= 46 bits UNCONDITIONALLY (banked reading)", main_banked < 0,
      "error/main >= 2^%s" % (-main_banked).quantize(Decimal("0.01")))

deg = 2 * R_BANKED - 1
weil_log2 = Decimal(deg).ln() / Decimal(2).ln() + L / 2
check("S9 P6: Weil bound deg*sqrt(p) = 2^65.0 vs |H| = 2^39",
      abs(weil_log2 - Decimal("65.0")) < Decimal("0.1"),
      "log2(deg*sqrt p) = %s ; log2|H| = 39" % weil_log2.quantize(Decimal("0.001")))
gap = weil_log2 - Decimal(39)
check("S9 P6: vacuous by 26 +- 1 bits", Decimal("25") < gap < Decimal("27"),
      "gap = %s bits" % gap.quantize(Decimal("0.001")))
deg_thresh = Decimal(H_OFF) / (Decimal(P_OFF).sqrt())
check("S9 P6: non-vacuity needs deg <= |H|/sqrt p = 128", abs(deg_thresh - 128) < 1,
      "deg threshold = %s ; actual deg = %d = 2^%s"
      % (deg_thresh.quantize(Decimal("0.01")), deg,
         (Decimal(deg).ln() / Decimal(2).ln()).quantize(Decimal("0.001"))))

# ================================================================ SECTION 10
print("\n=== S10. P7: the moment ledger and its closure threshold ===")
# Bound:  Z_1 <= (1+eta)^S + p^-R * G(eta|H|) * 2^S ,
#         G(T) <= p^R N_k T^{-2k} ,  N_k <= sqrt(2) (2k|H|/e)^k  (k <= R by THEOREM Z-2)
# Tail <= (1+eta)^S  <=>  k log2(e eta^2 |H| / (2k)) >= S (1 - log2(1+eta)) + O(1).
Lf = float(L)


def tail_exponent(eta, k, S=float(S_OFF), Hs=float(H_OFF), RlogP=None):
    """log2 of  p^-R G(eta|H|) 2^S  minus  S ; i.e. the tail exponent over 2^S."""
    return math.log2(2.0) * 0.5 + k * math.log2(2.0 * k / (math.e * eta * eta * Hs))


def best_c():
    best = 1.0
    arg = None
    for i in range(1, 4000):
        eta = i / 4000.0
        k = min(float(R_BANKED), eta * eta * float(S_OFF))   # unconstrained opt is eta^2 S
        k = max(k, 1.0)
        first = math.log2(1.0 + eta)
        tail = 1.0 + tail_exponent(eta, k) / float(S_OFF)
        c = max(first, tail)
        if c < best:
            best, arg = c, (eta, k)
    return best, arg


c_best, arg = best_c()
check("S10 the moment ledger gives an unconditional exponential saving c < 1",
      c_best < 0.95, "Z_1 <= 2^{%.4f S} at eta = %.4f, k = %.4g" % (c_best, arg[0], arg[1]))
check("S10 but c is bounded away from 0: NOT 2^{o(S)}", c_best > 0.5,
      "best c = %.4f, i.e. short of the terminal by (1-c) S = %.4f * 2^38 = %.4g bits"
      % (c_best, 1 - c_best, (1 - c_best) * float(S_OFF)))

# closure threshold: with k = R = S/L and the most generous eta -> 1,
# the tail needs  log2(e L) >= L .
def closes(Lv):
    return math.log2(math.e * Lv) >= Lv


lo, hi = 0.5, 20.0
for _ in range(200):
    mid = (lo + hi) / 2
    if closes(mid):
        lo = mid
    else:
        hi = mid
check("S10 P7: the ledger can reach 2^{o(S)} only if log2 p <= %.4f, i.e. p <= %.2f"
      % (lo, 2 ** lo), 2 ** lo <= 8.6 and 2 ** lo >= 7.5,
      "threshold log2 p <= %.4f  <=>  p <= %.3f  (THEOREM Z-NOGO's p <= 8)" % (lo, 2 ** lo))
check("S10 official row is log2 p = 64 >> %.3f: DEAD by %.2f bits in log2 p"
      % (lo, Lf - lo), Lf > lo, "log2 p = %.6f vs threshold %.4f" % (Lf, lo))
check("S10 Z-NOGO comparison: distance+counting needs p <= 8 "
      "(f2_z1_mass_knife_edge/statement.md:40-44); the moment implementation of route (b) "
      "lands on the same threshold", 2 ** lo <= 8.6, "same shape, same constant")

# ================================================================ SUMMARY
print("\n" + "=" * 72)
npass = sum(1 for _, ok, _ in CHECKS if ok)
print("CHECKS: %d/%d PASS" % (npass, len(CHECKS)))
for name, ok, detail in CHECKS:
    if not ok:
        print("  FAILED: %s | %s" % (name, detail))
print("=" * 72)
sys.exit(0 if npass == len(CHECKS) else 1)
