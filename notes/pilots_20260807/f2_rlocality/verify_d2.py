"""D2 -- THE SHARPENING ATTEMPTS (A1..A6).  Round-22 f2_rlocality, DRAFT ONLY.

Every attempt was pre-registered in PREREG.md section C BEFORE this file ran.
"""

import math
import sys
import os
import cmath

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_lib as R

PASS, FAIL, MISS = [], [], []


def chk(tag, cond, msg):
    (PASS if cond else FAIL).append(tag)
    print(("PASS " if cond else "FAIL ") + tag + " :: " + msg)


L = R.L_OFF
cs = R.CSTAR
D_INSTR = R.DEF_INSTR(cs, L)

print("=" * 78)
print("D2.0  LICENSING CONTROLS (independent code path, toy rows)")
print("=" * 78)


def prim_root(p):
    fac = set()
    n = p - 1
    d = 2
    while d * d <= n:
        while n % d == 0:
            fac.add(d)
            n //= d
        d += 1
    if n > 1:
        fac.add(n)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g
    raise RuntimeError


def row(p):
    """(e_p, S, zeta) for the admissible toy row at p (2-power 2N, CATCH-Z6)."""
    e_p = 0
    n = p - 1
    while n % 2 == 0:
        n //= 2
        e_p += 1
    S = 2 ** (e_p - 1)
    g = prim_root(p)
    zeta = pow(g, (p - 1) // (2 ** e_p), p)
    assert pow(zeta, 2 ** e_p, p) == 1 and pow(zeta, 2 ** (e_p - 1), p) == p - 1
    return e_p, S, zeta


def toy(p, Rr):
    e_p, S, zeta = row(p)
    Lam = [2 * r + 1 for r in range(Rr)]
    assert 0 not in Lam, "CATCH-19B: shift-0 cell -- exponent 0 must never occur"
    assert (2 * S) & (2 * S - 1) == 0, "CATCH-Z6: 2N must be a 2-power"
    ys = [pow(zeta, s, p) for s in range(S)]
    A = [[pow(y, l, p) for y in ys] for l in Lam]        # R x S
    return e_p, S, zeta, Lam, ys, A


def z1_and_costs(p, Rr):
    """Z_1 = p^{-R} sum_u prod_s (1+cos(2 pi c_s/p))  (route_b LEMMA 1),
    and the per-u cost form log2 P = S - sum_s d(c_s) (tail_count THEOREM 1)."""
    e_p, S, zeta, Lam, ys, A = toy(p, Rr)
    cosv = [1.0 + math.cos(2.0 * math.pi * c / p) for c in range(p)]
    dv = [(-2.0 * math.log2(abs(math.cos(math.pi * c / p)))) for c in range(p)]
    tot = 0.0
    maxdev = 0.0
    logs = []
    us = [0] * Rr
    n_u = p ** Rr
    for idx in range(n_u):
        t, u = idx, []
        for _ in range(Rr):
            u.append(t % p)
            t //= p
        prod = 1.0
        cost = 0.0
        for s in range(S):
            c = 0
            for r in range(Rr):
                c += u[r] * A[r][s]
            c %= p
            prod *= cosv[c]
            cost += dv[c]
        tot += prod
        if prod > 0.0:
            maxdev = max(maxdev, abs(math.log2(prod) - (S - cost)))
        logs.append(S - cost)
    return tot / n_u, maxdev, logs, S


z1_g1, dev_g1, logs_g1, S_g1 = z1_and_costs(17, 2)
z1_g4, dev_g4, logs_g4, S_g4 = z1_and_costs(97, 2)
print("G1 p=17  S=%d R=2 : Z_1 = %.6f   (banked 1.250000)" % (S_g1, z1_g1))
print("G4 p=97  S=%d R=2 : Z_1 = %.6f   (banked 9.387207)" % (S_g4, z1_g4))
chk("D2.0a", abs(z1_g1 - 1.25) < 1e-9 and abs(z1_g4 - 9.387207) < 1e-6,
    "banked Z_1 reproduced from scratch at G1 and G4 "
    "(tern_route_b/PROOFS.md:124-127)")
chk("D2.0b", max(dev_g1, dev_g4) < 1e-9,
    "character form and cost form agree to %.1e (THEOREM 1)" % max(dev_g1, dev_g4))

print()
print("=" * 78)
print("D2.A4  HIGHER MOMENTS k > R : is the cap k <= R sharp?")
print("=" * 78)
print("N_k := #{(x,y) in H^k x H^k : sum x_i^l = sum y_i^l, l in Lambda}")
print("     = p^{-R} sum_u V_1(u)^{2k}   (route_b THEOREM 7 orthogonality)")
print()
print("%-14s %3s %14s %14s %8s" % ("row", "k", "N_k", "(2k-1)!!|H|^k", "verdict"))


def Nk_table(p, Rr, kmax):
    e_p, S, zeta, Lam, ys, A = toy(p, Rr)
    H = ys + [(-y) % p for y in ys]
    out = []
    n_u = p ** Rr
    V = []
    for idx in range(n_u):
        t, u = idx, []
        for _ in range(Rr):
            u.append(t % p)
            t //= p
        v = 0.0
        for x in H:
            c = 0
            for r in range(Rr):
                c += u[r] * pow(x, Lam[r], p)
            v += math.cos(2.0 * math.pi * (c % p) / p)
        V.append(v)
    for k in range(1, kmax + 1):
        s = sum(v ** (2 * k) for v in V) / n_u
        dfac = 1
        for j in range(1, 2 * k, 2):
            dfac *= j
        out.append((k, s, dfac * (len(H) ** k)))
    return out, len(H)


for (p, Rr, name) in [(17, 2, "G1 p=17"), (97, 2, "G4 p=97"), (113, 1, "G2 p=113")]:
    tab, Hs = Nk_table(p, Rr, Rr + 2)
    for k, nk, bd in tab:
        ok = nk <= bd * (1 + 1e-9)
        mark = "OK" if ok else "**FAILS**"
        star = "  <- k = R" if k == Rr else ("  <- k = R+1" if k == Rr + 1 else "")
        print("%-14s %3d %14.1f %14.1f %8s%s" % (name, k, nk, bd, mark, star))
    fails = [k for k, nk, bd in tab if nk > bd * (1 + 1e-9)]
    print("     first failure at k = %s (R = %d)" % (min(fails) if fails else None, Rr))

tab17, _ = Nk_table(17, 2, 4)
tab97, _ = Nk_table(97, 2, 4)
tab113, _ = Nk_table(113, 1, 3)
chk("D2.A4a",
    all(nk <= bd * (1 + 1e-9) for k, nk, bd in tab17 if k <= 2)
    and all(nk <= bd * (1 + 1e-9) for k, nk, bd in tab97 if k <= 2)
    and all(nk <= bd * (1 + 1e-9) for k, nk, bd in tab113 if k <= 1),
    "N_k <= (2k-1)!!|H|^k holds for every k <= R at G1, G4, G2")
firstfail_113 = min(k for k, nk, bd in tab113 if nk > bd * (1 + 1e-9))
print("G2 p=113 R=1: N_2 = %.0f vs bound %.0f (banked 1104 > 768)"
      % (tab113[1][1], tab113[1][2]))
chk("D2.A4b", firstfail_113 == 2 and abs(tab113[1][1] - 1104) < 1e-6,
    "banked G2 failure N_2 = 1104 > 768 reproduced independently")
ff17 = [k for k, nk, bd in tab17 if nk > bd * (1 + 1e-9)]
ff97 = [k for k, nk, bd in tab97 if nk > bd * (1 + 1e-9)]
print("G1 first failure k = %s ; G4 first failure k = %s" % (ff17[:1], ff97[:1]))
chk("D2.A4c", ff17 and ff17[0] == 3 and ff97 and ff97[0] == 3,
    "A4 VERDICT: the cap k <= R is SHARP at G1 and G4 too "
    "(first failure exactly at k = R+1) -- A4 FAILS as registered")

print()
print("=" * 78)
print("D2.A1  DROP-AMGM : the type / binomial-moment bound on the cost sum")
print("=" * 78)
for kmul, lab in [(1.0, "k = R  (R-wise independence only)"),
                  (2.0, "k = 2R (2R-wise -- NOT supplied by the MDS code)")]:
    it = R.I_TYPE(cs, L, kmul)
    print("  %-42s I_TYPE(c*) = %.6f   deficit = %.3f" % (lab, it, cs / it))
it1, it2 = R.I_TYPE(cs, L, 1.0), R.I_TYPE(cs, L, 2.0)
chk("D2.A1a", abs(cs / it1 - 64.0) < 0.5 and abs(cs / it2 - 32.0) < 0.5,
    "A1: deficits 64.0 (k=R) / 32.0 (k=2R) -- both far WORSE than %.3f; "
    "A1 FAILS as registered" % D_INSTR)
chk("D2.A1b", abs(it1 - 0.0069) < 5e-4 and abs(it2 - 0.0138) < 1e-3,
    "P-A1 numeric CONFIRMED: I_TYPE(c*) = %.5f / %.5f (predicted 0.0069/0.0138)"
    % (it1, it2))
print("  NOTE: min_nu D(nu||mu) s.t. E_nu[d] <= 1-c EQUALS I_FLAT(c) (Sanov")
print("        contraction), so I_TYPE(c) = kmul * I_FLAT(c)/L exactly.")
print("        I_FLAT(c*) = %.8f = c*  -> I_TYPE(c*) = kmul * c*/L." % R.I_FLAT(cs, L))

print()
print("=" * 78)
print("D2.A2  TRUNCATED / CENTRED-MOMENT bound on the cost sum, order k")
print("=" * 78)


def _trunc_moments(M, nq=20001):
    """Flat-model law of X' = max(X, -M), X = 1 + 2 log2|cos phi|, phi
    uniform on [0, pi/2) (the p -> oo limit of c uniform on F_p).
    Returns (mean, cgf) with cgf(theta) = log2 E[2^{theta (X' - mean)}]."""
    phiM = math.acos(2.0 ** (-(M + 1.0) / 2.0))
    h = phiM / (nq - 1)
    xs = []
    for i in range(nq):
        phi = i * h
        xs.append(1.0 + 2.0 * math.log2(math.cos(phi)) if phi < phiM else -M)
    w = [(1.0 if i in (0, nq - 1) else (4.0 if i % 2 else 2.0)) for i in range(nq)]
    norm = 2.0 / math.pi

    def E(f):
        s = sum(wi * f(x) for wi, x in zip(w, xs)) * h / 3.0
        return norm * (s + (math.pi / 2.0 - phiM) * f(-M))

    mean = E(lambda x: x)

    def cgf(theta):
        return math.log2(E(lambda x: 2.0 ** (theta * (x - mean))))

    return mean, cgf


def I_MOM_TRUNC(c, L, kmul, Ms=None, ngrid=400):
    """A2 as REGISTERED: the centred k-th moment bound (k = kmul*R) applied to
    the TRUNCATED cost sum Y' = sum_s max(X_s, -M) >= Y, so
    Pr[Y >= cS] <= Pr[Y' >= cS].  X' = g(c_s) is a coordinate function, so
    every moment of Y' of order <= k is determined by the k-wise marginals.
    exponent = max over M of min over the two sides of the branch exponents."""
    if Ms is None:
        Ms = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 20.0]
    ks = kmul / L
    best, bestM = -1e30, None
    for M in Ms:
        mean, cgf = _trunc_moments(M)
        tS = c - mean
        if tS <= 0:
            continue

        def branch(sign):
            b = -1e30
            for i in range(1, ngrid + 1):
                th = 6.0 * i / ngrid
                try:
                    l2 = cgf(sign * th)
                except (OverflowError, ValueError):
                    continue
                arg = th * math.log(2.0) * tS * math.e * L / kmul   # NOTE: factor L = S/R
                if arg <= 0.0:
                    continue
                b = max(b, ks * math.log2(arg) - l2)
            return b

        v = min(branch(+1), branch(-1))
        if v > best:
            best, bestM = v, M
    return best, bestM


def I_MOM_RAW(c, L, kmul, ngrid=4000):
    """The same bound WITHOUT truncation (exact centred CGF
    Lambda2(theta) = log2 C(2theta,theta) up, Gamma ratio down)."""
    ks = kmul / L
    tS = 1.0 + c

    def branch(sign):
        b = -1e30
        hi = 0.49 if sign < 0 else 3.0
        for i in range(1, ngrid + 1):
            th = hi * i / ngrid
            if sign > 0:
                l2 = (math.lgamma(2.0 * th + 1.0)
                      - 2.0 * math.lgamma(th + 1.0)) / math.log(2.0)
            else:
                if 1.0 - 2.0 * th <= 1e-9:
                    continue
                l2 = (math.lgamma(1.0 - 2.0 * th)
                      - 2.0 * math.lgamma(1.0 - th)) / math.log(2.0)
            arg = th * math.log(2.0) * tS * math.e * L / kmul   # NOTE: factor L = S/R
            if arg <= 0.0:
                continue
            b = max(b, ks * math.log2(arg) - l2)
        return b

    return min(branch(+1), branch(-1))


def _def(v):
    return float("inf") if v <= 0 else cs / v


mraw1 = I_MOM_RAW(cs, L, 1.0)
m1, M1 = I_MOM_TRUNC(cs, L, 1.0)
m2, M2 = I_MOM_TRUNC(cs, L, 2.0)
print("  UNTRUNCATED, k = R : exponent %+.6f  -> the raw two-sided branch"
      % mraw1)
print("                       (cost of the heavy LOWER tail of d)")
print("  TRUNCATED  , k = R : exponent %+.6f  deficit %8.3f  (best M = %.1f)"
      "   [LICENSED by R-wise independence]" % (m1, _def(m1), M1))
print("  TRUNCATED  , k = 2R: exponent %+.6f  deficit %8.3f  (best M = %.1f)"
      "   [NOT licensed -- see PROOFS section 4]" % (m2, _def(m2), M2))
chk("D2.A2a", 0 < mraw1 < m1,
    "truncation HELPS but is not necessary: exponent %.5f -> %.5f (+%.1f%%); "
    "the heavy lower tail of d costs the raw centred moment that much"
    % (mraw1, m1, 100.0 * (m1 / mraw1 - 1.0)))
chk("D2.A2b", _def(m1) > D_INSTR,
    "A2 at the LICENSED radius k = R gives deficit %.3f > %.3f: A2 FAILS"
    % (_def(m1), D_INSTR))
if not (abs(_def(m1) - 8.6) < 0.7):
    MISS.append("A2 numeric: registered deficit 8.6 +- 0.7, measured %.3f"
                % _def(m1))
print("  *** REGISTERED-PREDICTION CHECK: I predicted A2 deficit 8.6 +- 0.7;")
print("      measured %.3f at k = R (verdict A2-FAILS as registered)." % _def(m1))

print()
print("=" * 78)
print("D2.A3  NO-POSITION-ENTROPY : tail_count THEOREM 10 repaired")
print("=" * 78)
print("THEOREM 10 (banked):  |U_c| <= C(S,R) m^R")
print("   exponent per S = -H(1/L) + (1/L) log2(1/rho)   <- position entropy PAID")
print("REPAIR:               Pr[N_A >= m] <= E[C(N_A,R)]/C(m,R) = C(S,R)rho^R/C(m,R)")
print("   exponent per S = (1/S)[log2 C(m,R) - log2 C(S,R)] + (1/L)log2(1/rho)")
print("   -> the C(S,R) CANCELS against C(m,R): the position entropy is an ARTIFACT")
print()
H1L = -(1.0 / L) * math.log2(1.0 / L) - (1 - 1.0 / L) * math.log2(1 - 1.0 / L)
print("H(1/L) = %.6f   (the banked 0.1161)" % H1L)
best_old = -1e30
for i in range(1, 20000):
    delta = i / 20000.0
    if (1 - delta) * R.S_OFF < R.R_OFF + 1:
        continue
    D = (1.0 - cs) / delta
    rho = R.rho_interval(D)
    if rho <= 0 or rho >= 1:
        continue
    best_old = max(best_old, -H1L - math.log2(rho) / L)
newv, newd, _ = R.I_BINOM(cs)
print("THEOREM 10 as banked, best over delta at c*   : %.6f  (NEGATIVE => dead)" % best_old)
print("REPAIRED bound,        best over delta at c*   : %.6f  at delta = %.4f"
      % (newv, newd))
print("required at c*                                 : %.6f" % cs)
chk("D2.A3a", best_old < 0 < newv,
    "A3(i) CONFIRMED: the banked THEOREM 10 exponent is NEGATIVE (%.5f) while "
    "the repaired one is POSITIVE (%.5f) -- 'dies at EVERY p' is an ARTIFACT "
    "of the union bound over position sets" % (best_old, newv))
chk("D2.A3b", abs(newv - 0.0017) < 0.0005,
    "A3(ii) numeric CONFIRMED: I_BINOM(c*) = %.5f (predicted 0.0017 +- 0.0005), "
    "deficit %.1f -- still far short; A3 FAILS numerically" % (newv, cs / newv))
# does the repaired bound have a threshold in p at all?
print()
print("repaired-bound threshold scan in L = log2 p (best c-independent check at c*):")
for Lx in [2, 3, 4, 8, 16, 32, 64, 128]:
    v, dd, _ = R.I_BINOM(cs, S=2 ** 20, R=max(1, int(2 ** 20 / Lx)))
    print("   log2 p = %-5d  I_BINOM(c*) = %+.6f  deficit = %8.2f"
          % (Lx, v, cs / v if v > 0 else float("inf")))

print()
print("=" * 78)
print("D2.A5  LONGER WINDOW (raise R at fixed S)")
print("=" * 78)
print("DEF_INSTR(c*) as a function of the locality fraction R/S = 1/Lx:")
for Lx in [4, 8, 16, 32, 64, 128]:
    print("   1/(R/S) = %-5d  I_INSTR(c*) = %.6f   deficit = %8.3f"
          % (Lx, R.I_INSTR(cs, Lx), cs / R.I_INSTR(cs, Lx)))
chk("D2.A5a", R.DEF_INSTR(cs, 32.0) < R.DEF_INSTR(cs, 64.0),
    "A5: the deficit does fall if R/S may be raised -- but saturation pins "
    "R/S = 1/log2 p exactly (THEOREM Z-NOGO), so no admissible row offers it: "
    "A5 FAILS structurally, as registered")

print()
print("=" * 78)
print("D2.A6  BEST-OF at the binding layer c*")
print("=" * 78)
cands = [("banked instrument (AM-GM + Z-2 + Chebyshev, k<=R)", R.I_INSTR(cs, L)),
         ("A1 type bound, k = R", it1),
         ("A2 truncated centred moment, k = R", m1),
         ("A3 repaired THEOREM 10", newv)]
cands.sort(key=lambda z: -z[1])
for nm, v in cands:
    print("   %-52s exponent %.6f  deficit %8.3f" % (nm, v, cs / v))
chk("D2.A6a", cands[0][0].startswith("banked"),
    "A6 CONFIRMED: no licensed attempt beats the banked instrument at c*; "
    "best deficit stays %.4f" % D_INSTR)

print()
print("D2 SUMMARY: %d PASS, %d FAIL, %d registered-prediction MISS"
      % (len(PASS), len(FAIL), len(MISS)))
for m in MISS:
    print("  MISS: " + m)
sys.exit(1 if FAIL else 0)
