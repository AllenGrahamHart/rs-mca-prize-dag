#!/usr/bin/env python3
"""D1(#6): the Theorem-J domination check on #1146/#1145's row, and the
NEW defect-side (JB3)/(JB4) test that the round-24 board change legalized.

Stdlib only, exact integers / Fractions. Run via tools/ramguard tiny.

Dictionary (derived from THEIR note, not assumed):
  ell = 11, row (tau, m):
    n     = (m + tau) * ell        [their sec.3: "tau=5, m=6 RS geometry"
                                     needs 11 quotient labels = m+tau]
    k - 1 = N = m * ell            [core = m fibres]
    g     = ell - b = ell = 11     [background-free => b = 0]
    s     = (k-1) + g = (m+1)*ell  [listing threshold; agreement =
                                     N - d + h >= s  <=>  h >= d + g]
  h = petal agreement = |X| in (JB1); their S_tau is the ENVELOPE of h.
"""
from fractions import Fraction

ELL = 11
ROWS_CERTIFIED = [(6, 8), (6, 9), (6, 10), (7, 9), (7, 10), (8, 10)]
ROWS_UNSETTLED_TAU5 = [(5, 6), (5, 7), (5, 8), (5, 9)]
ENVELOPE = {6: 20, 7: 22, 8: 24, 9: 27}          # their (S_6..S_9), gcd=2 supports
ENVELOPE_G1 = {6: 18, 7: 21, 8: 24, 9: 27}       # gcd_A = 1 maxima from the census

out = []
def P(*a):
    line = " ".join(str(x) for x in a)
    out.append(line)
    print(line)

# ---------------------------------------------------------------- part 0
P("=" * 74)
P("PART 0 -- dictionary self-checks against THEIR note (internal consistency)")
P("=" * 74)
# 0a. quotient-label exclusion, note sec.3 lines 86-88
for p in (23, 67, 199, 419, 331):
    q = (p - 1) // ELL
    P("  p=%-4d |Q|=(p-1)/11 = %-3d  >= m+tau=11 (tau=5,m=6 row)? %s"
      % (p, q, "YES" if q >= 11 else "NO -> excluded"))
P("  => their exclusion of 23,67 is EXACTLY the condition |Q| >= m+tau = 11,")
P("     which PROVES the dictionary component  n = (m+tau)*ell.")
P("")
# 0b. S_h = sum of h largest fibre values (their sec. defn line 15)
def S(spec, h):
    """spec: dict size->multiplicity. Sum of the h largest values."""
    vals = []
    for size, mult in sorted(spec.items(), reverse=True):
        vals += [size] * mult
    assert len(vals) >= h, (spec, h)
    return sum(vals[:h])

wit = {5: 2, 3: 2, 2: 4, 1: 22}
P("  witness A={1,3,5,7,9} spectrum 5^2 3^2 2^4 1^22 ->",
  "(S_6..S_9) =", tuple(S(wit, h) for h in (6, 7, 8, 9)),
  "  [audit says (20,22,24,25)]")
p199 = {6: 1, 2: 8, 1: 9}
p419 = {6: 1, 2: 5, 1: 32}
P("  p=199 profile 6^1 2^8 1^9  -> S_6 =", S(p199, 6), " [note prints 20: audit F8 confirmed]")
P("  p=419 profile 6^1 2^5 1^32 -> S_6 =", S(p419, 6), " [same]")
eq199 = {4: 2, 2: 2, 1: 5}
eq199d = {4: 4, 2: 4, 1: 10}
P("  F_199 equality witness  S_3(P|Q^2) =", S(eq199, 3),
  " doubled S_6(Gamma) =", S(eq199d, 6), " [their 10 / 20]")
env = [ENVELOPE[h] for h in (6, 7, 8, 9)]
P("  envelope (20,22,24,27) increments =",
  [env[i + 1] - env[i] for i in range(3)], "-> increasing: no single state attains it (F7)")
P("")

# ---------------------------------------------------------------- part 1
P("=" * 74)
P("PART 1 -- THEOREM J (l1_program_frontier, PROVED) on their rows")
P("  clause (1): 2s > n+k-1  => |ImgFib| <= 1")
P("  clause (2): s^2 > n(k-1) => |ImgFib| <= n(n-k+1)/(s^2-n(k-1))")
P("=" * 74)
P("  row(tau,m)   n     k-1     s     2s-(n+k-1)   s^2-n(k-1)   verdict")
allrows = [(t, m, "CERTIFIED") for (t, m) in ROWS_CERTIFIED] + \
          [(t, m, "tau=5 open") for (t, m) in ROWS_UNSETTLED_TAU5]
for tau, m, tag in allrows:
    n = (m + tau) * ELL
    N = m * ELL            # = k-1
    s = (m + 1) * ELL
    c1 = 2 * s - (n + N)
    c2 = s * s - n * N
    closed = ELL * ELL * (1 - m * (tau - 2))
    assert c2 == closed, (tau, m, c2, closed)
    v = "MISSES (sub-Johnson, clause1 fails)" if (c1 <= 0 and c2 <= 0) else "??"
    P("  (%d,%2d) %-10s %-5d %-6d %-5d %-8d %-12d %s" % (tau, m, tag, n, N, s, c1, c2, v))
P("  closed form: s^2 - n(k-1) = ell^2 * (1 - m*(tau-2)); clause1 <=> tau < 2.")
P("  Enlarging n beyond the minimal support domain only decreases s^2-n(k-1).")
P("")

# ---------------------------------------------------------------- part 2
P("=" * 74)
P("PART 2 -- THE NEW TEST: defect-side (JB2)/(JB3)/(JB4)")
P("  N=k-1=m*ell, h=petal agreement, r_J=2d-h, e=max(0,r_J+1),")
P("  J=d^2-N*r_J; r_J<0 => |Z|<=1;  J>0 => |Z| <= N(d-r_J)/J")
P("  background-free: g=ell=11, list threshold h >= d+g")
P("=" * 74)

def jb(N, d, h):
    r = 2 * d - h
    if r < 0:
        return ("UNIQUE", r, None, 1)
    J = d * d - N * r
    if J <= 0:
        return ("VACUOUS", r, J, None)
    b = Fraction(N * (d - r), J)
    return ("BOUND", r, J, b)

P("")
P("(2a) CONDITIONAL ON THEIR ENVELOPE  h <= S_tau  (parity supports)")
P("     d_max = S_tau - g ;  r_J = 2d-h <= d-g")
for tau, m in ROWS_CERTIFIED:
    N = m * ELL
    Stau = ENVELOPE[tau]
    dmax = Stau - ELL
    worst = None
    kinds = set()
    for d in range(1, dmax + 1):
        for h in range(d + ELL, Stau + 1):
            k_, r, J, b = jb(N, d, h)
            kinds.add(k_)
            if k_ == "BOUND":
                if worst is None or b > worst[0]:
                    worst = (b, d, h, r, J)
    P("  (tau=%d,m=%2d) N=%3d  S_tau=%2d  d in [1,%2d]  outcomes=%s  worst-bound=%s"
      % (tau, m, N, Stau, dmax, sorted(kinds),
         "none" if worst is None else
         "|Z|<=%d at d=%d,h=%d (r_J=%d,J=%d, exact %s)"
         % (int(worst[0]), worst[1], worst[2], worst[3], worst[4], worst[0])))
P("")
P("(2b) UNCONDITIONAL (their theorem NOT used): only the quintic fibre cap")
P("     h <= 5*tau. d_max = 5*tau - g.")
for tau, m in ROWS_CERTIFIED:
    N = m * ELL
    cap = 5 * tau
    dmax = cap - ELL
    fires, vac = [], []
    worst = None
    for d in range(1, dmax + 1):
        anyfire = False
        for h in range(d + ELL, cap + 1):
            k_, r, J, b = jb(N, d, h)
            if k_ in ("UNIQUE", "BOUND"):
                anyfire = True
                if k_ == "BOUND" and (worst is None or b > worst[0]):
                    worst = (b, d, h, r, J)
        (fires if anyfire else vac).append(d)
    P("  (tau=%d,m=%2d) N=%3d cap=%2d d in [1,%2d]: sieve LIVE for d in %s ; VACUOUS for d in %s"
      % (tau, m, N, cap, dmax, fires if len(fires) < 12 else "1..%d" % max(fires), vac))
    if worst:
        P("        worst per-pattern bound |Z| <= %d  (d=%d,h=%d,r_J=%d,J=%d, exact %s)"
          % (int(worst[0]), worst[1], worst[2], worst[3], worst[4], worst[0]))
P("")
P("(2c) THE CROSSOVER: with h at the trivial cap and h=d+g the two extremes,")
P("     r_J<0 <=> h>2d;  combined with h>=d+g this holds for all d<g=11.")
P("     => on EVERY background-free ell=11 row, d<=10 forces |Z|<=1 outright.")
for tau in (6, 7, 8, 9):
    P("       tau=%d: envelope S_tau=%2d -> d <= %2d ; d<=10 forced? %s"
      % (tau, ENVELOPE[tau], ENVELOPE[tau] - ELL,
         "YES" if ENVELOPE[tau] - ELL <= 10 else "NO (d can reach %d)" % (ENVELOPE[tau] - ELL)))
P("")
P("(2d) the same for the gcd_A=1 (250-support) census maxima")
for tau in (6, 7, 8, 9):
    P("       tau=%d: S_tau(gcd1)=%2d -> d <= %2d ; d<=10 forced? %s"
      % (tau, ENVELOPE_G1[tau], ENVELOPE_G1[tau] - ELL,
         "YES" if ENVELOPE_G1[tau] - ELL <= 10 else "NO (d can reach %d)" % (ENVELOPE_G1[tau] - ELL)))

with open("notes/pilots_20260809/pr_harvest/jcheck.txt", "w") as f:
    f.write("\n".join(out) + "\n")
