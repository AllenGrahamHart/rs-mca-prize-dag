# F2 campaign: THE EXTRAS-CONTRACTION LEMMA — target pre-registration
# (session-2 opening brief; consolidates log entries #9-#11; contains
#  NO new claims — every fact cited here is banked with a digest)

Status: TARGET. This is the single lemma separating u2c from its flip
(given L4 constants + L5 assembly, both mechanical once this exists).

## Statement (to be proved)

Fix a sub-balance official row (generated field q, domain mu_n,
conditions t; catch-#11 beta-discipline). For 0 <= j <= t let
  N^(j)(0) = #{S in mu_n, |S| = b : p_1(S) = ... = p_j(S) = 0},
  struct^(j) = the structured census at level j (coset-union blocks
               and their proved closures; exact combinatorics).
EXTRAS-CONTRACTION(L): for every j in the q-free index set (catch #6
Frobenius discipline) and every mid-band b:

    N^(j)(0) - struct^(j)  <=  (L/q) * ( N^(j-1)(0) - struct^(j-1) )

for some L <= 2^15.

## Why this suffices (banked chain)

Tolerance chain (log #9, banked): official rows have t*log2(q) ~
2.15e12 > n ~ 1.1e12 with the window empty at every b — the flat
model predicts < 2^{-1e12}-scale occupancy vs budget n^3, so
max/mean <= L^t with L <= 2^{(1.05e12)/t} ~ 2^15 wins. Iterating
EXTRAS-CONTRACTION(L) from the exact base N^(0)(0) = C(n,b) gives
extras(b) <= (L/q)^t * C(n,b) + [struct telescoping, exact], and
summing over b (extremes EMPTY to width ~2^31/side by
f2_newton_empty_extremes as corrected) meets the n^3 budget with the
stated tolerance. L5 = this arithmetic, exact, per official row.

## Empirical support (banked, log #11)

At all 7 calibration rows the observed contraction of the FULL census
is flat (L_obs = 0.82..1.4) until the census equals struct, where it
stops (condition-immune forced blocks) — i.e. the extras form of the
statement is what the data supports, with observed L two orders below
even 32, four below the 2^15 requirement.

## Proof obligations, exactly

(O1) struct^(j) exact: the level-j structured census formula (which
     coset-union blocks satisfy the first j conditions — for full
     mu_M-cosets: all j with M not dividing j; unions accordingly;
     the giant-block closure is PROVED and covers the rest).
(O2) the inductive step: one added power-sum condition p_j = 0 cuts
     the extras fiber by q/L. Candidate routes, in order:
     (R1) exact-arithmetic Fourier on the RELATIVE census (the
          level-j arcs are 1-dimensional given level j-1; the
          chord-orbit lemma and the L2 machinery apply levelwise;
          BLOCKED-ROUTE WARNING: absolute/float methods are dead at
          mid-band — catches #5, no-go #2 — the step must be signed
          or exact);
     (R2) the energy dichotomy (f2_effective_energy_dichotomy) on the
          level-(j-1) extras fiber: if the fiber is large it is
          energy-deficient, and an energy-deficient set cannot
          concentrate under a new linear-in-indicator condition
          beyond L/q [the connection to prove];
     (R3) trade-variety / rigidity (M2): a level-j extras pair is a
          signed t-null configuration; route through
          a_universal_trade_variety.
     (R4) BEZOUT / COMPLETE-INTERSECTION (added at session close,
          route sketch only): p_1..p_j is a regular sequence, so
          W_j = {p_1 = .. = p_j = 0} in A^b is a complete intersection
          of dimension b - j and degree j! (Bezout, degrees 1..j).
          IF the successive intersections with the torsion conditions
          x_i^n = 1 are proper (the obligation: no component in a
          torsion coset eats the bound — note the structured blocks
          live EXACTLY in torsion cosets, so properness-after-
          removing-struct is the right statement), then
          N^(j) <= j! n^{b-j} / (b-j)!-scale, giving per-condition
          contraction n/q-ish with cumulative loss ~ log2(j!). The
          OBSTRUCTION, quantified: log2(j!) exceeds the 1.05e12-bit
          tolerance at j ~ 3.5e10 ~ t/2 — R4 alone covers the FIRST
          HALF of the ladder and must be spliced with R1/R2/R3 (or an
          aggregate argument) for the upper half. Frobenius (catch
          #6) prunes the ladder to q-free indices first.
(O3) the q-free/Frobenius bookkeeping (catch #6): conditions at
     indices divisible by q are free; the ladder runs on ~t(1-1/q)
     independent conditions — a negligible correction to the
     tolerance, to be printed exactly in L5.

## O1-geometric lemma (PROVED at session close; digest O1_GEOMETRIC_PASS)

For any partition of the b coordinates into blocks of sizes
M_alpha | n with every M_alpha > j, the ORBIT LOCUS {each block = a
full mu_{M_alpha}-orbit scaled by a free parameter y_alpha} lies in
W_j IDENTICALLY: p_i restricted to it equals
sum_alpha y_alpha^i * M_alpha * [M_alpha | i] = 0 for all i <= j
(the orbit power-sum fact, verified exactly at 5 (q, M) pairs). Its
dimension is the number of blocks, and its mu_n-torsion points with
distinct coordinates are EXACTLY the disjoint coset-union structured
blocks. Moreover these loci are precisely where successive torsion
intersection is IMPROPER (within a block, the 2nd..M-th torsion
conditions are implied by the first). Hence:

  R4 CRUX (the lemma in geometric clothing, now exactly posed):
  every component of W_j NOT of orbit type meets the successive
  torsion conditions properly (or with excess bounded by 2^15 per
  condition). Struct = the torsion points of the orbit components —
  obligation O1's geometric half is DONE; the crux is a statement
  about components of a fixed complete intersection, opening Galois/
  monodromy and specialization tools that fiber-counting language
  could not reach.

## Falsifier (pre-registered, immutable)

A calibration row and level j where the EXTRAS (census minus exact
struct) contract by strictly less than q/2^15 — sustained at >= 3
field scales at matched (n, b, j). The log-#11 instrument measures
exactly this; extending it to more rows is the first session-2 run.

## Non-goals

No asymptotics; no o(*); no promotion of R1-R3 sketches to results;
the lemma lands only with a proof + a green verifier at calibration
rows + the exact L5 arithmetic at official rows.
