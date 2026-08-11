"""D1/D3 arithmetic verification for r36_m4_nonsplit.

Verifies every number registered in PREREG.md "## Pilot registrations"
BEFORE the searches use them.  Writes d1_arith_results.txt in this
directory only.  Stdlib only.
"""
import sys
from math import comb, log10

OUT = []


def p(s=""):
    OUT.append(str(s))


def slots(m, k, kp):
    """Distinct-tuple slope-SLOT count (R1.1).  Delta part + middle part."""
    dpart = 6 * m * (m - 1)
    # number of distinct tuples on the symmetric difference
    tD = -(-6 * m // k)          # ceil(6m/k)
    tM = -(-(m - 1) // kp) if m > 1 else 0
    return tD * (m - 1) + tM * (m - 2), tD, tM


def demand(m, k, kp):
    s, tD, tM = slots(m, k, kp)
    return s - (4 * m - 1), s, tD, tM


p("=== R1.1 / R1.2  COINCIDENCE DEMAND  D(k,k') = slots - rho ===")
p("m  k  k'   tD  tM  slots  rho   D(mine)   D(anchor conv.)")
for m, k, kp in [(3, 2, 2), (4, 1, 1), (4, 2, 2), (4, 3, 3),
                 (5, 2, 2), (5, 4, 4)]:
    D, s, tD, tM = demand(m, k, kp)
    rho = 4 * m - 1
    anchor = tD * (m - 1) - (rho - 1)
    p("%d  %d  %d    %2d  %2d   %3d   %3d    %3d       %3d"
      % (m, k, kp, tD, tM, s, rho, D, anchor))

p()
p("CALIBRATION CHECK (R1.1): m=3,k=k'=2 must reproduce anchor 1's 8.")
D3, _, _, _ = demand(3, 2, 2)
p("  D(3,2,2) = %d   -> %s" % (D3, "PASS" if D3 == 8 else "FAIL"))
p("R1.2 CORRECTION CHECK: anchor's m=4 2-sharing demand is 22; mine:")
D4, _, _, _ = demand(4, 2, 2)
p("  D(4,2,2) = %d   (anchor 22, difference %d)" % (D4, D4 - 22))
D5, _, _, _ = demand(5, 2, 2)
p("  D(5,2,2) = %d   (anchor 42, difference %d)" % (D5, D5 - 42))
p("R1.3: 3-sharing demand at m=4")
D43, _, _, _ = demand(4, 3, 3)
p("  D(4,3,3) = %d ; m=3 crossing level 8 ; measured m=4 supply 12" % D43)
p("  <= 8 ? %s      <= 12 ? %s" % (D43 <= 8, D43 <= 12))

p()
p("=== R1.4  (SUPPLY-CODIM) EXCESS AT m=4 ===")
for name, sup in [("(SPLIT-4)", 10), ("(QUAD-4)", 14), ("(SHARE3-4)", 15)]:
    dem = D4 if name != "(SHARE3-4)" else D43
    anc = 22 if name != "(SHARE3-4)" else 22 - 12
    p("  %-11s supply %2d  demand %2d  E = %+d" % (name, sup, dem, sup - dem))

p()
p("=== R1.5  x-DEGREE COST OF k-SHARING:  deg_x = k*deg_w <= 3(m-1) ===")
p("m   3m-3   k    deg_w max   deg_x used   waste   k | 3(m-1)?")
for m in (3, 4, 5, 6, 7):
    for k in range(2, m):
        b = 3 * (m - 1)
        dw = b // k
        p("%d    %2d    %d      %d           %2d          %d      %s"
          % (m, b, k, dw, k * dw, b - k * dw, b % k == 0))

p()
p("=== R1.8  MIXED SHARING IS IMPOSSIBLE AT m=4 (supply cap 12) ===")
sols = []
for n3 in range(0, 9):
    for n2 in range(0, 13):
        for n1 in range(0, 25):
            if 3 * n3 + 2 * n2 + n1 != 24:
                continue
            t = n1 + n2 + n3
            # total slots incl. one middle tuple of size m-2 = 2
            dem = 3 * t + 2 - 15
            if dem <= 12:
                sols.append((n3, n2, n1, t, dem))
p("  patterns with demand <= measured supply 12 : %d" % len(sols))
for s in sols:
    p("    n3=%d n2=%d n1=%d  t=%d  demand=%d" % s)

p()
p("=== R1.10 / R1.11  PER-SIDE CAP AND THE SELECTION LAYER AT k=3 ===")
p("  X'_gamma = 3*d ; per-side caps 3 and 3 ; so 3d <= 6 - 2X''")
p("  => d <= 2 (k=3)   vs   d <= 3 (k=2, X'=2d)")
p("  sum_gamma d_gamma = 8 triples * 3 = 24 ; d<=2 => s >= 12")
p("  T_2 = rho = 15 exactly, middles take 2 slopes => s = 13")
p("  degree sequence on 13 slopes with sum 24, max 2: 11 x deg2 + 2 x deg1")
p("  check: 11*2 + 2*1 = %d  -> %s" % (11 * 2 + 2 * 1,
                                       "PASS" if 11 * 2 + 2 == 24 else "FAIL"))
p("  per-side balance: sum_T a_T = 12 over 8 triples;")
p("  all splits in {(2,1),(1,2)} => 2p + (8-p) = 12 => p = %d" % (12 - 8))

# explicit certificate: K_{4,4} minus a perfect matching, then the s=13 form
A = [0, 1, 2, 3]
B = [4, 5, 6, 7]
edges = [(a, b) for a in A for b in B if b - 4 != a]     # remove matching
p("  CERTIFICATE C1 (s=12): K_{4,4} minus a perfect matching")
p("    edges = %d ; simple = %s ; bipartite = %s"
  % (len(edges), len(set(edges)) == len(edges),
     all((e[0] in A) != (e[1] in A) for e in edges)))
deg = {v: 0 for v in A + B}
for a, b in edges:
    deg[a] += 1
    deg[b] += 1
p("    degree sequence (slot-degree per triple) = %s ; 3-regular = %s"
  % (sorted(deg.values()), set(deg.values()) == {3}))
# pair multiplicity: two triples share at most one slope <=> simple graph
pm = {}
for a, b in edges:
    pm[(a, b)] = pm.get((a, b), 0) + 1
p("    max pair multiplicity (two triples sharing a slope) = %d (cap 1)"
  % max(pm.values()))
e13 = edges[:-1]
p("  CERTIFICATE C2 (s=13, the FORCED form): drop one edge, add 2 pendants")
deg2 = {v: 0 for v in A + B}
for a, b in e13:
    deg2[a] += 1
    deg2[b] += 1
pend = [v for v in A + B for _ in range(3 - deg2[v])]
p("    %d edges + %d pendant slopes = %d slopes ; slot sum = %d"
  % (len(e13), len(pend), len(e13) + len(pend), 2 * len(e13) + len(pend)))
p("    slopes = %d (need 13) -> %s"
  % (len(e13) + len(pend), "PASS" if len(e13) + len(pend) == 13 else "FAIL"))
p("    slot sum = %d (need 24) -> %s"
  % (2 * len(e13) + len(pend),
     "PASS" if 2 * len(e13) + len(pend) == 24 else "FAIL"))

p()
p("=== R1.12  (OUT-m)/(DEG-m) UNDER k-SHARING ===")
p("  (OUT-m): X' + 2X'' >= m-1-eps ;  X' = k*d")
for m in (3, 4, 5, 6):
    for k in (2, 3, m - 1):
        if k < 2 or k > m - 1:
            continue
        need = m - 1
        dmin = -(-need // k)
        p("  m=%d k=%d : k*d >= %d needs d >= %d  (X''=0 suffices: %s)"
          % (m, k, need, dmin, dmin >= 1 and k * dmin >= need))

p()
p("=== R2.1  FIRST MOMENT FOR THE 3-SHARING PENCIL ===")
N8 = 1
n = 64
for j in range(8):
    N8 *= comb(n - 3 * j, 3)
N8 //= 3628800 // 90          # 8! = 40320
p("  #(8-families of pairwise disjoint triples in a 64-set) = %d" % N8)
p("  registered 2.30e30 ; computed %.3e ; ratio %.4f"
  % (N8, N8 / 2.30e30))
p()
p("  q     q^12          E = N8 * q^-12     prediction")
for q in (193, 257, 337, 401, 449, 577, 641):
    E = N8 / float(q) ** 12
    p("  %-5d 10^%-10.3f  %-16.4g  %s"
      % (q, 12 * log10(q), E, "EXISTS" if E > 3 else
         ("BORDERLINE" if E > 0.3 else "ABSENT")))
p("  (q must satisfy 64 | q-1: %s)"
  % {q: (q - 1) % 64 == 0 for q in (193, 257, 337, 401, 449, 577, 641)})
p("  threshold q* where E = 1 : q* = N8^(1/12) = %.1f" % (N8 ** (1.0 / 12)))

p()
p("=== R1.14  PARAMETER COUNT OF (SHARE3-4) ===")
p("  w = P/Q, deg<=3   : 8 coeffs - 1 projective          =  7")
p("  Psi~ deg_w <= 3   : 4 polys x 4 coeffs - 1           = 15")
p("  minus PGL_2 on the w-line                            = -3")
p("  TOTAL                                                = %d" % (7 + 15 - 3))
p("  continuous supply usable vs coincidences (w is 0-dim) = 15")
p("  incidences needed = 8*3 + 1*2 = %d ; prescribable    = 15"
  % (8 * 3 + 2))

p()
p("=== R5.1  CAUCHY-SCHWARZ DEMAND-SIDE BOUND (pencil classes) ===")
p("  sum_j |A_j| >= |S|(m-1)^2 / sum d_j >= 6m(m-1)^2/(3(m-1)) = 2m(m-1)")
p("  |U A_j| >= (sum|A_j|)^2 / sum_{j,j'} |A_j ^ A_j'| ; need <= rho=4m-1")
p("  => sum_{j!=j'} |A_j^A_j'| >= 4m^2(m-1)^2/(4m-1) - 6m(m-1)")
p()
p("   m   4m^2(m-1)^2/(4m-1)  diag<=6m(m-1)   cross>=   pairs   avg>=   m(m-7)/(m-2)")
for m in (3, 4, 5, 6, 7, 8, 10, 12, 16, 20, 32, 64):
    lhs = 4 * m * m * (m - 1) ** 2 / float(4 * m - 1)
    diag = 6 * m * (m - 1)
    cross = lhs - diag
    pairs = (m - 1) * (m - 2)
    avg = cross / pairs if pairs else float('nan')
    approx = m * (m - 7) / float(m - 2)
    p("  %3d  %14.1f  %10d  %11.1f  %6d  %7.2f  %8.2f"
      % (m, lhs, diag, cross, pairs, avg, approx))
p()
p("  R5.1(i) VACUOUS for m <= 7 ?  (cross bound <= 0)")
for m in (3, 4, 5, 6, 7, 8):
    lhs = 4 * m * m * (m - 1) ** 2 / float(4 * m - 1) - 6 * m * (m - 1)
    p("    m=%d : cross bound = %+.1f -> %s"
      % (m, lhs, "VACUOUS" if lhs <= 0 else "BINDING"))
p()
p("  R5.1(iii) q-threshold from heuristic cross supply N^2/q = 256 m^2/q :")
p("   m    avg cross needed   N=16m   256m^2   q <= 256m^2/avg")
for m in (8, 10, 12, 16, 20, 32, 64, 128):
    lhs = 4 * m * m * (m - 1) ** 2 / float(4 * m - 1) - 6 * m * (m - 1)
    avg = lhs / ((m - 1) * (m - 2))
    p("  %4d  %14.2f  %6d  %8d  %12.0f"
      % (m, avg, 16 * m, 256 * m * m, 256 * m * m / avg))

p()
p("=== R5.3  NO DEGREE-1 FACTOR ===")
p("  a Mobius phi_j is injective on S: |A_j| = |S| = 6m > 4m-1 = rho")
for m in (2, 3, 4, 5, 10):
    p("    m=%d : 6m = %d vs rho = %d -> %s"
      % (m, 6 * m, 4 * m - 1, "EXCLUDED" if 6 * m > 4 * m - 1 else "allowed"))

with open("notes/pilots_20260811/r36_m4_nonsplit/d1_arith_results.txt", "w") as f:
    f.write("\n".join(OUT) + "\n")
print("\n".join(OUT))
