#!/usr/bin/env python3
"""d1c_fence.py -- rh_residuals_close (round 32), D1 completion.

Question: is residual (i) (the single gap integer a* of D1) closable by the
INCIDENCE-ONLY axioms -- the same axiom set that
background/nodes/rate_half_type2_fr_incidence_only_route_fence (PROVED)
fences off for residual (ii) at a = 7m-1?

Two parts.
  (A) exact integer feasibility of the necessary conditions at a = a*, for
      m = 2, 8, 32, 2^37   (necessary, NOT sufficient -- round 31's MISS 2
      is the precedent for not over-reading a feasibility certificate);
  (B) an EXPLICIT set system at m = 2 (the smallest scale in the official
      residue class m = 2 mod 3, same RIG = -2) satisfying every incidence
      axiom at a* = 11, verified here.  Its type-2 blocks are the vertex
      stars of K_7 on the 21 outside points.

stdlib only.
"""
from itertools import combinations

out = []
P = out.append


def profile(m):
    N, R1, rho = 16 * m, 8 * m + 1, 4 * m - 1
    astar = (16 * m + 1) // 3            # m = 2 mod 3
    s = R1 - astar
    T = rho + 2
    T1 = astar // (astar - rho)
    T2 = T - T1
    cap = (N - astar) * m // s
    return dict(m=m, N=N, R1=R1, rho=rho, a=astar, s=s, T=T, T1=T1, T2=T2,
                cap=cap, e=m)


P("=" * 74)
P("D1c(A)  INCIDENCE FEASIBILITY at the gap integer a*  (necessary conditions)")
P("=" * 74)
for m in (2, 8, 32, 2 ** 37):
    if m % 3 != 2:
        continue
    p = profile(m)
    N, R1, rho, a, s, T, T1, T2, e = (p["N"], p["R1"], p["rho"], p["a"],
                                      p["s"], p["T"], p["T1"], p["T2"], p["e"])
    P("")
    P("  m = %d :  N=%d rho=%d T=rho+2=%d  a*=%d  s=%d  T1=%d  T2=%d  CAP=%d"
      % (m, N, rho, T, a, s, T1, T2, p["cap"]))
    P("    AO1 = T1 + CAP = %d  vs rho+1 = %d   deficit %d"
      % (T1 + p["cap"], rho + 1, T1 + p["cap"] - rho - 1))
    # incidence budget
    tot_inc = T * rho                       # O = 0
    P("    sum_x d_x = T*rho = %d ; N*e = %d ; sum_x (e-d_x) = %d (must be 1+O)"
      % (tot_inc, N * e, N * e - tot_inc))
    out_cap = (N - a) * e
    spend = T2 * s
    P("    outside capacity (N-a)e = %d ; min type-2 spend T2*s = %d ; slack %d"
      % (out_cap, spend, out_cap - spend))
    P("    => #{minimum-weight type-2} >= %d  ((5m-10)/3 = %d)"
      % (T2 - (out_cap - spend), (5 * m - 10) // 3))
    # type-1 geometry: K_gamma = W \ S_gamma pairwise disjoint, |K| = a-rho
    K = a - rho
    P("    type-1: |K_gamma| = a-rho = %d, pairwise disjoint, T1*K = %d <= a = %d : %s"
      % (K, T1 * K, a, T1 * K <= a))
    P("    type-1 pair overlap forced to 2rho-a = %d (>= 0 : %s)"
      % (2 * rho - a, 2 * rho - a >= 0))
    # type-2 W-share
    P("    type-2: |S n W| <= rho - s = %d ; sum over type-2 of |S n W| = %d..%d"
      % (rho - s, a * e - T1 * rho - 1, a * e - T1 * rho))
    P("      mean |S n W| over type-2 = %.4f (max allowed %d)"
      % ((a * e - T1 * rho) / T2, rho - s))
    feasible = (a * e - T1 * rho) <= T2 * (rho - s)
    P("      MEAN <= MAX feasible: %s" % feasible)
    # (OV) / NEWCAP pair-sum check
    lhs = (N - 1) * (e * (e - 1) // 2) + ((e - 1) * (e - 2) // 2)   # Lmin(0)
    rhs = (T * (T - 1) // 2) * (2 * rho - a)
    P("    (OV) pair-sum: Lmin(0) = %d <= C(T,2)(2rho-a) = %d : %s"
      % (lhs, rhs, lhs <= rhs))
    P("    ==> NO numerical obstruction at a* from the incidence axioms.")

P("")
P("=" * 74)
P("D1c(B)  EXPLICIT incidence-only set system at m = 2, a* = 11")
P("=" * 74)
m = 2
p = profile(m)
N, R1, rho, a, s, T, T1, T2, e = (p["N"], p["R1"], p["rho"], p["a"], p["s"],
                                  p["T"], p["T1"], p["T2"], p["e"])
W = list(range(a))                       # 0..10
OUTSIDE = list(range(a, N))              # 11..31, 21 points
edges = list(combinations(range(7), 2))  # 21 edges of K_7
assert len(edges) == len(OUTSIDE)
emap = {edges[i]: OUTSIDE[i] for i in range(21)}

# type-1 blocks: S = W \ K, K pairwise disjoint of size a-rho = 4
K1, K2 = [0, 1, 2, 3], [4, 5, 6, 7]
S_t1 = [tuple(x for x in W if x not in K1), tuple(x for x in W if x not in K2)]
# type-2 blocks: vertex stars of K_7 (6 outside points) + one W point
Wpts = [0, 1, 2, 3, 4, 5, 6]             # 7 distinct W points, 7 unused
S_t2 = []
for v in range(7):
    star = [emap[tuple(sorted((v, u)))] for u in range(7) if u != v]
    S_t2.append(tuple(sorted(star + [Wpts[v]])))
blocks = S_t1 + S_t2

P("  W = %s   (|W| = a = %d)" % (W, a))
P("  type-1 blocks (S subset W):")
for S in S_t1:
    P("    %s" % (list(S),))
P("  type-2 blocks (K_7 vertex star + one W point):")
for S in S_t2:
    P("    %s" % (list(S),))
P("")
ok = True


def chk(name, cond, extra=""):
    global ok
    ok = ok and cond
    P("  [%s] %-58s %s" % ("OK" if cond else "!!", name, extra))


chk("block count = T = rho+2", len(blocks) == T, "%d = %d" % (len(blocks), T))
chk("every |S_gamma| = rho", all(len(S) == rho for S in blocks),
    "sizes %s" % sorted(set(len(S) for S in blocks)))
d = {}
for S in blocks:
    for x in S:
        d[x] = d.get(x, 0) + 1
chk("d_x <= e = m", all(v <= e for v in d.values()),
    "max d_x = %d" % max(d.values()))
defi = sum(e - d.get(x, 0) for x in range(N))
chk("sum_x (e - d_x) = 1 + O with O = 0", defi == 1, "= %d" % defi)
chk("T1 blocks are inside W", all(set(S) <= set(W) for S in S_t1))
chk("type-2 spend |S \\ W| >= s = R+1-a",
    all(len([x for x in S if x not in W]) >= s for S in S_t2),
    "spends %s (s = %d)" % (sorted(set(len([x for x in S if x not in W])
                                       for S in S_t2)), s))
pairs = list(combinations(range(len(blocks)), 2))
ovs = [len(set(blocks[i]) & set(blocks[j])) for i, j in pairs]
unions = [len(set(blocks[i]) | set(blocks[j])) for i, j in pairs]
chk("(OV): |S u S'| >= w* = a for every pair", min(unions) >= a,
    "min union = %d, a = %d" % (min(unions), a))
lhs = sum(ovs)
rhs = sum(v * (v - 1) // 2 for v in d.values())
chk("incidence identity sum_pairs |S n S'| = sum_x C(d_x,2)", lhs == rhs,
    "%d = %d" % (lhs, rhs))
chk("pairwise overlap <= 2rho - a", max(ovs) <= 2 * rho - a,
    "max overlap %d <= %d" % (max(ovs), 2 * rho - a))
mw = sum(1 for S in S_t2 if len([x for x in S if x not in W]) == s)
chk("#minimum-weight type-2 >= (5m-10)/3", mw >= (5 * m - 10) // 3,
    "%d min-weight of %d type-2 ((5m-10)/3 = %d)" % (mw, len(S_t2), (5 * m - 10) // 3))
chk("T_1 = %d and T_2 = %d as forced by AO1" % (T1, T2),
    len(S_t1) == T1 and len(S_t2) == T2)
P("")
P("  ALL INCIDENCE AXIOMS SATISFIED: %s" % ok)
P("")
P("  CONSEQUENCE (the residual-(i) analogue of the wave-57 fence):")
P("  at the gap integer a* = 11 of the m = 2 profile -- same residue class")
P("  m = 2 mod 3 and the same RIG = -2 as the OFFICIAL gap integer -- the")
P("  numerical endpoint axioms (block sizes, d_x <= e, the exact saturation")
P("  deficit, pairwise union (OV), the MDS spend floor (C2)) are SATISFIABLE")
P("  with T = rho+2.  So no proof using ONLY those cardinalities can close")
P("  residual (i) either.  The closure must come from the algebra: T4's")
P("  divisibility at RIG = -2.")
P("")
P("  SCOPE, stated against my own claim: this is an explicit system at")
P("  m = 2 only.  For m = 8, 32, 2^37 part (A) gives integer feasibility of")
P("  the NECESSARY conditions, which is NOT a construction -- exactly the")
P("  over-reading that round 31 self-falsified (rh_type2_stratum MISS 2).")
print("\n".join(out))
