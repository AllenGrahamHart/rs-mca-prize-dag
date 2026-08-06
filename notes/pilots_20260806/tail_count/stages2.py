#!/usr/bin/env python3
"""Round 20 -- stages THR (family-trap thresholds), PROF (tail profiles),
TR (transport of the T2 mechanism).  Imported by verify_tail.py."""

import math
import os
import sys
from decimal import Decimal, getcontext

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tc_lib as T                                            # noqa: E402

getcontext().prec = 60

# official row, tern_route_b/PROOFS.md:58-61
P_OFF = 18446735827372343297
S_OFF = 1 << 38
R_BANKED = 4294967340
R_BALANCE = 4294967339


# ---------------------------------------------------------------------------
# THR -- the per-layer certified c-ranges and their thresholds in p
# ---------------------------------------------------------------------------

def phi_moment(c, L):
    """Z-2/Chebyshev supply certifies layer c at log2 p = L iff >= 0.

    P(u) >= 2^{cS} => V_1 >= eta_c |H|, eta_c = 2^c - 1 (Lemma 5);
    Chebyshev on the 2k-th moment with N_k <= (2k-1)!!|H|^k (k <= R) gives
    Pr <= sqrt2 (2k/(e eta^2 |H|))^k, maximised at k = min(R, eta^2 S);
    the criterion needs Pr <= 2^{-cS}.  With R/S = 1/L, |H| = 2S:
        k = R  branch:  (1/L) log2(e eta^2 L) - c
        k = eta^2 S:     log2(e) eta^2 - c        (only if eta^2 < 1/L)
    """
    eta = 2.0 ** c - 1.0
    if eta <= 0:
        return -1e18
    if eta * eta >= 1.0 / L:
        return math.log2(math.e * eta * eta * L) / L - c
    return math.log2(math.e) * eta * eta - c


def best_moment(L, n=20001):
    best, arg = -1e18, None
    for i in range(1, n + 1):
        c = i / n
        v = phi_moment(c, L)
        if v > best:
            best, arg = v, c
    return best, arg


def rho(D):
    """Fraction of residues c with d(c) = -2log2|cos(pi c/p)| <= D."""
    x = 2.0 ** (-D / 2.0)
    x = min(1.0, max(-1.0, x))
    return 2.0 * math.acos(x) / math.pi


def H2(x):
    if x <= 0 or x >= 1:
        return 0.0
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def phi_interp(c, L, m_over_p_floor=None):
    """Interpolation supply certifies layer c at log2 p = L iff >= 0.

    cost(u) <= (1-c)S => at least R coordinates have d <= D whenever
    D >= (1-c)L/(L-1); those R coordinates, with values in the admissible
    set A(D) = {c : d(c) <= D} of size m, determine u (GRS interpolation),
    so |U_c| <= C(S,R) m^R, and the criterion |U_c| <= p^R 2^{-cS} needs
        -[ H(1/L) + (1/L) log2(m/p) ] - c  >=  0.
    m = 1 (only the value 0 admissible) is the DEGENERATE branch: there u
    is forced to 0 outright with no union bound, and that is the separate
    endpoint theorem (THR-5), not this one.  This function therefore
    evaluates the genuine branch m >= 2, i.e. m/p >= 2^{1-L}.
    """
    if L <= 1:
        return -1e18
    D = (1 - c) * L / (L - 1)
    if D <= 0:
        return -1e18                              # m = 1: the m>=2 branch
    r = rho(D)                                    # does not apply
    lg_mop = max(math.log2(r) if r > 0 else -1e18, 1.0 - L)   # log2(m/p)
    if m_over_p_floor is not None:
        lg_mop = max(lg_mop, math.log2(m_over_p_floor))
    return -(H2(1.0 / L) + lg_mop / L) - c


def bisect_threshold(f, lo, hi, tol=1e-9):
    """Largest L in [lo,hi] with f(L) >= 0, assuming f decreasing."""
    if f(lo) < 0:
        return None
    if f(hi) >= 0:
        return hi
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) >= 0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return lo


def stage_thr(CHK, head):
    head("THR -- P3/P4: the per-layer certified c-ranges (FAMILY-TRAP CHECK)")
    L_off = float(Decimal(P_OFF).ln() / Decimal(2).ln())
    print("      official row: log2 p = %.9f, S = 2^38, R/S = 1/log2 p" % L_off)

    print("      (c = 0 is TRIVIAL: |U_0| = p^R and the allowance at c = 0")
    print("       is exactly 2^{S+Delta} = p^R.  The grid below is c >= 0.01.)")
    best, arg = best_moment(L_off)
    CHK("THR-1 Z-2/Chebyshev supply certifies an EMPTY c-range at log2 p=64",
        best < 0, "max_c phi = %.6f at c = %.4f (need >= 0)" % (best, arg))
    thr_m = bisect_threshold(lambda L: best_moment(L, 4001)[0], 1.0001, 64.0)
    CHK("THR-2 its threshold is COROLLARY 8's log2 p <= 3.0529 (p <= 8.30)",
        abs(thr_m - 3.0529) < 5e-3,
        "threshold log2 p = %.4f  =>  p <= %.3f" % (thr_m, 2 ** thr_m))
    print("      per-layer c-range at the threshold: attained at c = %.3f"
          % best_moment(thr_m, 4001)[1])

    bi, argi = -1e18, None
    for i in range(1, 20001):
        c = i / 20000.0
        v = phi_interp(c, L_off)
        if v > bi:
            bi, argi = v, c
    CHK("THR-3 interpolation supply (branch m>=2) is EMPTY at log2 p = 64",
        bi < 0, "max_c phi_interp = %.6f at c = %.4f" % (bi, argi))
    worst_L = []
    for L in (2.0, 3.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 1024.0, 2.0 ** 20):
        b = max(phi_interp(i / 2000.0, L) for i in range(1, 2001))
        worst_L.append((L, b))
    CHK("THR-4 interpolation supply is empty for EVERY p (no threshold)",
        all(b < 0 for _, b in worst_L),
        "max_c phi at log2 p = %s" % ", ".join("%g:%.4f" % t for t in worst_L))
    print("      it fails by H(1/L) + 1/L in the exponent as c -> 0:")
    print("      H(1/64) = %.4f vs the value gain 1/64 = %.4f -- the union"
          % (H2(1.0 / 64), 1.0 / 64))
    print("      bound over WHICH R coordinates are small costs more than")
    print("      the smallness of the values saves.")

    # THR-5: the exact endpoint  U_c = {0}
    p = Decimal(P_OFF)
    pi = Decimal("3.14159265358979323846264338327950288419716939937510")
    x = pi / p
    cosx = 1 - x * x / 2 + x ** 4 / 24
    d1 = -2 * (cosx.ln() / Decimal(2).ln())          # d(1) = -2 log2 cos(pi/p)
    frac = 1 - Decimal(R_BANKED) / Decimal(S_OFF) * 0 - Decimal(1) / Decimal(
        int(L_off))                                   # 1 - R/S = 1 - 1/log2 p
    width = d1 * frac
    lw = float(width.ln() / Decimal(2).ln())
    CHK("THR-5 endpoint: U_c = {0} for every c > 1 - 2^{%.3f}" % lw,
        lw < -100, "d(1) = 2^{%.4f}, (1-R/S) = %.6f, width = 2^{%.3f}"
        % (float(d1.ln() / Decimal(2).ln()), float(frac), lw))
    print("      => the interpolation/endpoint route proves the criterion on")
    print("         a c-range of width 2^{%.2f} -- an ENDPOINT, not a range."
          % lw)

    # THR-6: the critical layer c* = 1/ln2 - 1
    head("THR -- P5: the critical layer of the criterion")
    cstar = 1.0 / math.log(2.0) - 1.0
    for p_ in (17, 97, 673, 65537):
        m1 = sum((1 + math.cos(2 * math.pi * c / p_))
                 * math.log2(1 + math.cos(2 * math.pi * c / p_))
                 for c in range(p_)) / p_
        CHK("THR-6 m_1(p=%d) -> 1/ln2 - 1 = %.10f" % (p_, cstar),
            abs(m1 - cstar) < 30.0 / p_,
            "m_1 = %.10f, |diff| = %.2e" % (m1, abs(m1 - cstar)))
    # Lambda(theta) = log2 C(2theta,theta) - theta  in the continuum
    def Lam(th):
        return (math.lgamma(2 * th + 1) - 2 * math.lgamma(th + 1)
                ) / math.log(2) - th
    CHK("THR-7 flat-model CGF Lambda(1) = 0 (E[P] = 1 exactly)",
        abs(Lam(1.0)) < 1e-12, "Lambda(1) = %.3e" % Lam(1.0))
    dl = (Lam(1 + 1e-6) - Lam(1 - 1e-6)) / 2e-6
    CHK("THR-8 Lambda'(1) = 1/ln2 - 1 = c*  (the zero-margin layer)",
        abs(dl - cstar) < 1e-6, "Lambda'(1) = %.9f vs c* = %.9f" % (dl, cstar))
    print("\n      flat-model margin profile  I(c) - c  (0 exactly at c*):")
    print("        c      I(c)     I(c)-c")
    for c in (0.0, 0.1, 0.2, 0.3, 0.4, cstar, 0.5, 0.6, 0.8, 1.0):
        I = max(th * c - Lam(th) for th in
                [0.001 * j for j in range(1, 20001)])
        print("       %.4f  %8.4f  %8.4f%s" % (c, I, I - c,
                                               "   <== c*" if abs(c - cstar)
                                               < 1e-9 else ""))


# ---------------------------------------------------------------------------
# TR -- transport of the T2 decimation mechanism to the official row
# ---------------------------------------------------------------------------

def stage_tr(CHK, head):
    head("TR -- P7: does the decimation CREATION mechanism transport?")
    # THEOREM D: at level k the sublattice has length A = 2^{38-k}; the
    # window Lambda = {1,3,...,2R-1} collapses mod 2A iff two of its
    # elements are congruent mod 2A, i.e. iff 2A <= 2R-2, i.e. A <= R-1;
    # the sublattice code has positive dimension iff A > R.
    for R in (R_BANKED, R_BALANCE):
        bad = []
        for k in range(0, 39):
            A = 1 << (38 - k) if k <= 38 else 0
            collapse = (A <= R - 1)
            positive = (A > R)
            if collapse and positive:
                bad.append(k)
        CHK("TR-1 (R=%d) no decimation level has BOTH collapse and dim>0" % R,
            not bad, "levels with both: %s" % (bad or "none"))
    A_star = 1 << 32
    CHK("TR-2 the crossover is exactly saturation: 2^32 < R < 2^33",
        (1 << 32) < R_BANKED < (1 << 33),
        "R = %d, 2^32 = %d, 2^33 = %d" % (R_BANKED, 1 << 32, 1 << 33))
    CHK("TR-3 A = R is impossible (R is not a 2-power)",
        R_BANKED != A_star and (R_BANKED & (R_BANKED - 1)) != 0,
        "v_2(R) = %d" % T.v2(R_BANKED))
    print("      window diameter 2R-2 = %d vs half-length S = %d;"
          % (2 * R_BANKED - 2, S_OFF))
    print("      2R-2 < S by a factor %.2f = log2(p)/2 -- the SATURATION"
          % (S_OFF / (2.0 * R_BANKED - 2)))
    print("      constant.  The official window is a SHORT INITIAL SEGMENT.")
    # toy replication of the dichotomy on the I1 shape
    ok = True
    detail = []
    for p, R in [(17, 2), (97, 2), (353, 2), (673, 2), (193, 4), (577, 3)]:
        row = T.Row(p, R)
        S = row.S
        for k in range(1, int(math.log2(S)) + 1):
            A = S >> k
            collapse = (2 * A <= 2 * R - 2)
            positive = (A > R)
            if collapse and positive:
                ok = False
                detail.append((p, R, k))
    CHK("TR-4 the dichotomy holds on every toy I1 row and every level",
        ok, "violations: %s" % (detail or "none"))
    print("      (SELF-ORTH/TWT, the second ingredient, needs |T| >= N/2 and")
    print("       p <= sublattice length; at the official row R/S = 1/64 and")
    print("       log2 p >= 39, so BOTH fail -- CATCH-19D independently.)")


# ---------------------------------------------------------------------------
# PROF -- T3: the measured tail profile
# ---------------------------------------------------------------------------

CGRID = [i / 20.0 for i in range(0, 21)]

FAM_A = [(17, 2), (113, 1), (241, 1), (97, 2), (353, 2), (673, 2), (65537, 1)]
FAM_B = [(193, 2), (193, 3), (577, 2), (641, 2), (257, 1), (769, 2)]


def profile(row, chunk=None):
    import numpy as np
    p, S, R = row.p, row.S, row.R
    if chunk is None:
        chunk = max(1024, (1 << 22) // S)
    M = np.array(row.M, dtype=np.int64)                 # S x R
    tbl = np.array([math.log2(1.0 + math.cos(2.0 * math.pi * c / p))
                    for c in range(p)], dtype=np.float64)
    total = p ** R
    thr = np.array([c * S for c in CGRID])
    counts = np.zeros(len(CGRID), dtype=np.int64)
    Zsum = 0.0
    lgsum = 0.0
    lgmax = -1e300
    nmax = 0
    for start in range(0, total, chunk):
        stop = min(total, start + chunk)
        idx = np.arange(start, stop, dtype=np.int64)
        U = np.empty((stop - start, R), dtype=np.int64)
        t = idx.copy()
        for r in range(R - 1, -1, -1):
            U[:, r] = t % p
            t //= p
        vals = (U @ M.T) % p                            # (n, S)
        lg = tbl[vals].sum(axis=1)
        Zsum += float(np.exp2(lg).sum())
        lgsum += float(lg.sum())
        mx = float(lg.max())
        if mx > lgmax + 1e-9:
            lgmax, nmax = mx, int((lg > mx - 1e-9).sum())
        elif abs(mx - lgmax) <= 1e-9:
            nmax += int((lg > lgmax - 1e-9).sum())
        counts += (lg[:, None] >= thr[None, :] - 1e-9).sum(axis=0)
    return {"Z": Zsum / total, "mean": lgsum / total, "max": lgmax,
            "nmax": nmax, "counts": counts, "total": total}


def stage_prof(CHK, head):
    head("PROF -- T3: the measured tail profile E(c) = log2 Pr + cS")
    print("      criterion (normalised): E(c) <= o(S) for every c;")
    print("      E(c) = log2|U_c| - [(1-c)S + Delta], Delta = R log2 p - S.")
    cstar = 1.0 / math.log(2.0) - 1.0
    rows = [(p, R, "A") for p, R in FAM_A] + [(p, R, "B") for p, R in FAM_B]
    for p, R, fam in rows:
        row = T.Row(p, R)
        work = p ** R * row.S
        if p ** R > 8_000_000 or work > 300_000_000:
            print("\n   [UNREACHED] %s: p^R = %d, p^R*S = %.3g evaluations"
                  " -- exceeds the compute law (declared unreached, NOT"
                  " estimated)" % (row.tag(), p ** R, float(work)))
            continue
        pr = profile(row)
        S = row.S
        m1 = sum((1 + math.cos(2 * math.pi * c / p))
                 * math.log2(1 + math.cos(2 * math.pi * c / p))
                 for c in range(p)) / p
        print("\n   FAMILY %s  %s   R_sat = %d   Delta = %+.3f"
              % (fam, row.tag(), row.Rsat, row.Delta))
        CHK("PROF-mean %s: E_u[log2 P] = -S(1-2/p)" % row.tag(),
            abs(pr["mean"] + S * (1 - 2.0 / p)) < 1e-6,
            "measured %.8f predicted %.8f" % (pr["mean"], -S * (1 - 2.0 / p)))
        CHK("PROF-max %s: max log2 P = S attained only at u = 0" % row.tag(),
            abs(pr["max"] - S) < 1e-9 and pr["nmax"] == 1,
            "max = %.6f (S=%d), attained %d times" % (pr["max"], S,
                                                      pr["nmax"]))
        print("      Z_1 = %.9f   m_1(p) = %.6f (c* = %.6f)"
              % (pr["Z"], m1, cstar))
        # u = 0 lies in EVERY U_c (P(0) = 2^S); E_nz strips that atom, which
        # is the trivial-character term, and measures the GENUINE tail.
        def Lam(th):
            return (math.lgamma(2 * th + 1) - 2 * math.lgamma(th + 1)
                    ) / math.log(2) - th
        def Irate(c):
            return max(th * c - Lam(th) for th in
                       [0.002 * j for j in range(1, 5001)])
        print("        c     |U_c|   E(c)      |U_c\\0|   E_nz(c)   flat"
              "      excess")
        best, argb = -1e18, None
        bestnz, argnz = -1e18, None
        for i, c in enumerate(CGRID):
            n = int(pr["counts"][i])
            lpr = math.log2(n / pr["total"]) if n else float("-inf")
            E = lpr + c * S if n else float("-inf")
            if E > best:
                best, argb = E, c
            nz = n - 1
            flat = (c - Irate(c)) * S
            if nz > 0:
                lprz = math.log2(nz / pr["total"])
                Enz = lprz + c * S
                if Enz > bestnz:
                    bestnz, argnz = Enz, c
                print("       %.2f %8d %+8.3f %8d  %+8.3f  %+8.3f  %+8.3f"
                      % (c, n, E, nz, Enz, flat, Enz - flat))
            else:
                print("       %.2f %8d %+8.3f %8d      -inf  %+8.3f      -inf"
                      % (c, n, E, nz, flat))
        print("      max_c E(c)    = %+.4f at c = %.2f  (= -Delta at c=1"
              " because |U_1| = 1)" % (best, argb))
        if argnz is not None:
            print("      max_c E_nz(c) = %+.4f at c = %.2f   (c* = %.4f)"
                  % (bestnz, argnz, cstar))
        else:
            print("      E_nz is empty on the grid (tail = the u=0 atom only)")
