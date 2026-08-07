"""D3 -- THE STRUCTURAL TEST: the formalized k-LOCAL class and its floor.
Round-22 f2_rlocality pilot, DRAFT ONLY.  Class + predictions pre-registered
in PREREG.md section D before this file ran."""

import math
import sys
import os
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_lib as R
import lp_lib as LP

PASS, FAIL, MISS = [], [], []


def chk(tag, cond, msg):
    (PASS if cond else FAIL).append(tag)
    print(("PASS " if cond else "FAIL ") + tag + " :: " + msg)


cs = R.CSTAR
L = R.L_OFF

print("=" * 78)
print("D3.0  SIMPLEX SMOKE TESTS (the solver is written from scratch --")
print("      scipy.optimize does not import inside the ramguard wall limit)")
print("=" * 78)
A = [[1, 0, 1, 0, 0], [0, 2, 0, 1, 0], [3, 2, 0, 0, 1]]
v, x = LP.solve_max([3, 5, 0, 0, 0], A, [4, 12, 18])
print("  textbook LP optimum = %.6f (exact 36)" % v)
chk("D3.0a", abs(v - 36.0) < 1e-9, "simplex reproduces the textbook optimum 36")
val = LP.pattern_lp(8, 1, 0.5)
print("  pattern_lp(S=8,k=1,rho=0.5) = %.9f (closed form rho = 0.5)" % val)
chk("D3.0b", abs(val - 0.5) < 1e-9, "pattern LP reproduces the k=1 closed form")

print()
print("=" * 78)
print("D3.1  THE FULL LP AT G1 (p=17, S=8, R=2) -- the exact toy-scale floor")
print("=" * 78)
print("k-LOCAL(k): a bound is k-LOCAL iff valid for EVERY law on F_p^S whose")
print("every k-subset marginal is uniform on F_p^k (PREREG section D).")
print("OPT_k(c) = max Pr[cost <= (1-c)S];  I_LOC_k = -(1/S)log2 OPT_k;")
print("FLOOR_k(c) = c / I_LOC_k(c)  --  NO k-LOCAL bound beats this.")
print()

p1, S1, R1 = 17, 8, 2
L1 = math.log2(p1)
print("G1: L = log2 17 = %.4f, R/S = %.4f, 1/L = %.4f, Delta = R L - S = %.3f"
      % (L1, R1 / S1, 1.0 / L1, R1 * L1 - S1))


def prim_root(p):
    fac, n, d = set(), p - 1, 2
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


def true_costs(p, Rr):
    """cost(u) over ALL p^R tuples of the actual GRS value code."""
    e_p, n = 0, p - 1
    while n % 2 == 0:
        n //= 2
        e_p += 1
    S = 2 ** (e_p - 1)
    zeta = pow(prim_root(p), (p - 1) // (2 ** e_p), p)
    Lam = [2 * r + 1 for r in range(Rr)]
    assert 0 not in Lam, "CATCH-19B: exponent 0 must never occur"
    assert (2 * S) & (2 * S - 1) == 0, "CATCH-Z6: 2N is a 2-power"
    ys = [pow(zeta, s, p) for s in range(S)]
    Amat = [[pow(y, l, p) for y in ys] for l in Lam]
    dv = [-2.0 * math.log2(abs(math.cos(math.pi * cc / p))) for cc in range(p)]
    out = []
    for idx in range(p ** Rr):
        t, u = idx, []
        for _ in range(Rr):
            u.append(t % p)
            t //= p
        out.append(sum(dv[sum(u[r] * Amat[r][s] for r in range(Rr)) % p]
                       for s in range(S)))
    return np.array(out), S


tc1, _ = true_costs(p1, R1)

t0 = time.time()
A2, b2, cost2, ns = LP.build_full(p1, S1, 2)
print("built: %d states; k=R -> %d rows (%.1fs)"
      % (ns, A2.shape[0], time.time() - t0))
print("(k = 2R at G1 is 496 rows x 12870 columns and is run separately in"
      " verify_d3b.py)")
print()
print("%-8s %11s %11s %9s %10s"
      % ("c", "OPT_{k=R}", "TRUE(GRS)", "FLOOR_R", "DEF_INSTR"))
rows = []
for c in [0.20, 0.30, cs, 0.60, 0.80, 1.00]:
    t1 = time.time()
    o2 = LP.full_lp_at(A2, b2, cost2, S1, c)
    tr = float(np.mean(tc1 <= (1.0 - c) * S1 + 1e-12))
    f2 = c / (-math.log2(o2) / S1) if o2 > 0 else float("inf")
    rows.append((c, o2, None, tr, f2, None))
    print("%-8.4f %11.4e %11.4e %9.4f %10.4f   [%.1fs]"
          % (c, o2, tr, f2, R.DEF_INSTR(c, L1), time.time() - t1))

o2_1 = rows[-1][1]
o4_1 = float(p1) ** (-2 * R1)
print()
print("c = 1 endpoint: OPT_{k=R} = %.10e   p^{-R} = %.10e"
      % (o2_1, float(p1) ** (-R1)))
chk("D3.1a", abs(o2_1 - float(p1) ** (-R1)) < 1e-9,
    "P9 CONFIRMED: OPT_R(1) = p^{-R} EXACTLY -- R-locality costs NOTHING at "
    "c = 1, the very layer at which 8.60 was computed (and the layer "
    "tail_count THEOREM 12 proves outright)")
print("(the k = 2R endpoint and binding layer are in VERIFY_D3B.txt)")
f2_1 = 1.0 / (-math.log2(o2_1) / S1)
print("FLOOR_R(1) = %.6f   ( <= 1 means: no R-local deficit at all )" % f2_1)
chk("D3.1c", f2_1 <= 1.0 + 1e-9, "FLOOR_R(1) = %.4f <= 1" % f2_1)

star = [r for r in rows if abs(r[0] - cs) < 1e-9][0]
print()
print("binding layer c* at G1: OPT_R = %.4e, FLOOR_R = %.4f"
      % (star[1], star[4]))
chk("D3.1d", star[4] > 1.0,
    "a genuine EXACT toy-scale FLOOR at the binding layer: no k=R-local "
    "estimate beats factor X = %.4f at G1 (EVIDENCE, not a theorem uniform "
    "in the row)" % star[4])

inband = 1.2 <= star[4] <= 4.0
if not inband:
    MISS.append("P7/D3 FLOOR_R(c*) at G1: registered [1.2,4.0], measured %.4f"
                % star[4])
chk("D3.1f", True, "registered band for FLOOR at G1 was [1.2, 4.0]: measured "
    "%.4f -- %s" % (star[4], "HIT" if inband else "MISS (reported)"))
bad = [r for r in rows if r[1] < r[3] - 1e-9]
chk("D3.1g", not bad,
    "sanity: OPT_R(c) >= the TRUE GRS tail at every layer (the object is a "
    "member of the class)")

print()
print("=" * 78)
print("D3.2  A SECOND EXACT ROW (p = 41, S = 4, R = 1)")
print("=" * 78)
p2, S2, R2 = 41, 4, 1
L2 = math.log2(p2)
A1m, b1m, cost1m, ns2 = LP.build_full(p2, S2, 1)
o41 = LP.full_lp_at(A1m, b1m, cost1m, S2, cs)
f_41 = cs / (-math.log2(o41) / S2)
print("p=41: L = %.4f, R/S = %.4f, 1/L = %.4f, %d states, %d rows"
      % (L2, R2 / S2, 1.0 / L2, ns2, A1m.shape[0]))
print("  OPT_{k=R=1}(c*) = %.6e   FLOOR_R(c*) = %.4f" % (o41, f_41))
print("  G1  (L = %.2f, R/S = %.3f): FLOOR_R(c*) = %.4f" % (L1, R1 / S1, star[4]))
print("  p41 (L = %.2f, R/S = %.3f): FLOOR_R(c*) = %.4f" % (L2, R2 / S2, f_41))
chk("D3.2a", True,
    "two exact rows only, both with R/S far off the official 1/L and tiny S: "
    "the L-dependence is NOT decidable from them")
MISS.append("P13 (L-dependence of FLOOR_k) UNRESOLVED: the exact full LP is "
            "feasible only at p <= ~41 (states = C(S+(p-1)/2, (p-1)/2)), too "
            "narrow an L-range to fit a law")

print()
print("=" * 78)
print("D3.3  THE PATTERN LP (LEMMA RL-5 lifted floor) -- exact at moderate S")
print("=" * 78)
rho_star = R.rho_interval(1.0 - cs)
print("rho(1-c*) = (2/pi) arccos(2^{-(1-c*)/2}) = %.6f" % rho_star)
print("k = 2R  =>  L = S/R = 2S/k ;  k = R  =>  L = S/k")
print()
print("%-6s %-4s %-9s %-7s %13s %11s %11s %10s"
      % ("S", "k", "kmul", "L", "OPTPAT", "exp/S", "asym exp/S", "FLOOR"))
scan = []
for (S, k, kmul) in [(32, 4, 2.0), (64, 4, 2.0), (128, 4, 2.0), (256, 4, 2.0),
                     (64, 8, 2.0), (128, 8, 2.0), (256, 8, 2.0),
                     (192, 12, 2.0), (256, 16, 2.0)]:
    Lx = kmul * S / k
    try:
        v = LP.pattern_lp(S, k, rho_star)
    except Exception as e:
        print("%-6d %-4d %-9.1f %-7.1f  solver: %s" % (S, k, kmul, Lx, e))
        continue
    if v <= 1e-7:            # my float simplex is not trustworthy below this
        print("%-6d %-4d %-9.1f %-7.1f  OPT = %.2e BELOW SOLVER TOLERANCE "
              "-- DISCARDED" % (S, k, kmul, Lx, v))
        continue
    em = -math.log2(v) / S
    ea = R.OPTPAT_asym(rho_star, Lx, kmul)
    scan.append((S, k, kmul, Lx, em, ea))
    print("%-6d %-4d %-9.1f %-7.1f %13.4e %11.6f %11.6f %10.4f"
          % (S, k, kmul, Lx, v, em, ea, cs / em))

print()
print("CONVERGENCE AT FIXED LOCALITY RATIO k/S (the quantity that is pinned")
print("at the official row): the exact exponent RISES toward the closed form,")
print("so the exact FLOOR FALLS toward FLOOR_asym as S grows.")
ok, nser = True, 0
uniq = {}
for (S, k, km, Lx, em, ea) in scan:
    uniq[(S, k)] = (S, k, em, ea)
for ratio, lab in [(1.0 / 8, "k/S = 1/8 ")]:
    seq = sorted([(S, em, ea) for (S, k, em, ea) in uniq.values()
                  if abs(k / S - ratio) < 1e-12])
    if len(seq) < 2:
        continue
    nser += 1
    print("   %s :" % lab, end="")
    for S, em, ea in seq:
        print("  S=%d exact %.6f" % (S, em), end="")
    print("   -> closed form %.6f" % seq[0][2])
    ok = ok and all(seq[i][1] < seq[i + 1][1] for i in range(len(seq) - 1))
    ok = ok and all(t[1] < t[2] for t in seq)
ok = ok and nser >= 1
print("CONVERGENCE at fixed k = 4 as S grows (all four points are well above")
print("the solver's reliable range):")
fix4 = sorted([(S, em, ea) for (S, k, em, ea) in uniq.values() if k == 4])
devs = [100 * (ea / em - 1.0) for _, em, ea in fix4]
for (S, em, ea), dv in zip(fix4, devs):
    print("   S = %-5d exact %.6f   closed form %.6f   +%.1f%%" % (S, em, ea, dv))
ok = ok and all(devs[i] > devs[i + 1] for i in range(len(devs) - 1))
chk("D3.3a", ok,
    "at FIXED k/S the exact pattern-LP exponent increases with S and stays "
    "below the closed form -- the closed form is the S -> infinity limit, "
    "which is the relevant value at S = 2^38, and finite-S floors OVERSTATE "
    "it")

print()
print("official-row LIFTED floor (ASYMPTOTIC -- evidence, not a theorem):")
for kmul, lab in [(1.0, "k = R "), (2.0, "k = 2R")]:
    fl, ex, rho = R.FLOOR_asym(cs, L, kmul)
    print("   %s : exponent %.6f   FLOOR = %.4f" % (lab, ex, fl))
flR, _, _ = R.FLOOR_asym(cs, L, 1.0)
fl2R, _, _ = R.FLOOR_asym(cs, L, 2.0)
d_instr = R.DEF_INSTR(cs, L)
okR = abs(flR - 6.2) <= 0.4
ok2R = abs(fl2R - 3.5) <= 0.3
chk("D3.3b", okR and ok2R,
    "P10: asymptotic FLOOR_R(c*) = %.3f (registered 6.2+-0.4) and "
    "FLOOR_2R(c*) = %.3f (registered 3.5+-0.3) -- %s"
    % (flR, fl2R, "CONFIRMED" if (okR and ok2R) else "MISS"))
if not (okR and ok2R):
    MISS.append("P10: FLOOR_R = %.3f (reg 6.2+-0.4), FLOOR_2R = %.3f "
                "(reg 3.5+-0.3)" % (flR, fl2R))
near = abs(d_instr / flR - 1.0) < 0.05
chk("D3.3c", True,
    "P11: DEF_INSTR(c*) = %.4f vs asymptotic FLOOR_R = %.4f (%+.1f%%), "
    "FLOOR_2R = %.4f (%.2fx) -- %s against the ASYMPTOTIC floor"
    % (d_instr, flR, 100 * (d_instr / flR - 1), fl2R, d_instr / fl2R,
       "CONFIRMED" if near else "MISS"))
if not near:
    MISS.append("P11: DEF_INSTR/FLOOR_asym_R = %.4f, registered within 5%%"
                % (d_instr / flR))
print()
print("THE READING (official row, S = 2^38, so the S -> oo limit applies):")
print("   FLOOR_R (lifted, k = R)   = %.4f" % flR)
print("   DEF_INSTR(c*)             = %.4f   (+%.1f%%)"
      % (d_instr, 100 * (d_instr / flR - 1)))
print("   FLOOR_2R (lifted, k = 2R) = %.4f   (headroom factor %.2f)"
      % (fl2R, d_instr / fl2R))
chk("D3.3d", flR < d_instr and d_instr > fl2R,
    "the banked instrument sits +%.1f%% above the k=R lifted floor and "
    "%.2fx above the k=2R lifted floor.  Since THEOREM Z-2 places the "
    "object's supply STRICTLY BETWEEN R-wise and 2R-wise uniformity, the "
    "honest reading is: essentially OPTIMAL for what R-wise independence "
    "alone allows, with up to a %.2fx gain still on the table if Z-2's "
    "2R-order information could be used in full"
    % (100 * (d_instr / flR - 1), d_instr / fl2R, d_instr / fl2R))

print()
print("D3 SUMMARY: %d PASS, %d FAIL, %d MISS/UNRESOLVED"
      % (len(PASS), len(FAIL), len(MISS)))
for m in MISS:
    print("  MISS/UNRESOLVED: " + m)
sys.exit(1 if FAIL else 0)
