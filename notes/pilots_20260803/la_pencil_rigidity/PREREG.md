# L-A (pencil rigidity at e >= 2) — pre-registration

Written BEFORE any computation.  Pilot: Opus 5, 2026-08-03.
Target: extend THEOREM C' (v5_occupancy, e = 1) to e >= 2.

## Setting

Block system B(V,t,t_0,k): U = A_0 |_| A_1 |_| ... |_| A_V, |A_a| = t,
S_a = U \ A_a, distinct slopes z_a, sigma = t_0+(V-3)t, e = k-sigma,
h = A-k, m = t+h, e = 2t-h, gates: t >= 2, t+1 <= h <= 2t-1 (so
1 <= e <= t-1), pairwise = k+1+(h-t-1) >= k+1, triples sigma <= k-1.
B_a := prod_{x in A_a}(X-x).  Ann as in THEOREM 1 (duality).

## Claim under test (L-A)

dim Ann >= 1  =>  all B_a lie in one 2-dim space <B_1,B_2> (pencil).

## Route to be used (declared in advance)

LEMMA 1 normalisation p_1 = p_2 = 0; g_a := p_a / (D prod_{j>=3,j!=a}B_j)
of degree < e; the pair relations R_ab = 0 mod B_1, R'_ab = 0 mod B_2;
the 2x2 slope inversion (determinant (z_b-z_a)(z_1-z_2) != 0) giving
B_b g_a in M := B_1 F_{<e} + B_2 F_{<e}; and the reduction
dim Ann = dim { w in F^{A_1 u A_2} : T_a w in E, a >= 3 },
T_a = diag((z_a-z_2)B_a|_{A_1}, (z_a-z_1)B_a|_{A_2}),
E = evaluations of F[X]_{<e} on A_1 u A_2 (dim e).

## Pre-registered PREDICTION (sharp, falsifiable)

Naive parameter count of the solution variety (cone in w):
  params  = (V-2)t [blocks B_3..B_V] + (V-2) [slope params] + 2t [w]
  eqns    = (V-2)(2t-e)
  expected dim = (V-2)(e+1-t) + 2t
  pencil family dim = (V-2) [c_a] + 1 [Mobius param] + e [w] = V+e-1
  EXCESS  Delta := (V-2)(e+1-t) + 2t - V - e + 1.
Delta = (t-1)(4-V) at e = 1 (<= 0 for all V >= 4: C' is true).
Delta = 1 at (V,e,t) = (4,2,3);  Delta = 0 at (5,2,3);  Delta < 0 for
V >= 6 at e = 2, t = 3, and for all V >= t+2 at e = t-1.

PREDICTION P: non-pencil non-collapsing gate-clean systems EXIST
exactly where Delta > 0, i.e. at V = 4, e >= 2 — and do NOT exist for
V >= 5 at e = 2, t = 3 (and more generally where Delta <= 0).
If P holds, L-A is FALSE as stated and TRUE in the large-V regime the
band heart actually uses.

## Falsifiers (any ONE kills the corresponding claim)

* **FA (kills L-A as stated).** A gate-clean, zero-escape,
  non-collapsing (dim Ann >= 1) BLOCK system with e >= 2 whose blocks
  are not all fibres of one degree-t pencil, i.e. rank{B_1..B_V} >= 3.
  Search: (t,e,V) = (3,2,4) over F_13 (U = F_13 \ {0}, k = 5, t_0 = 0)
  by linear solve for the last block; random (3,2,4) at q = 17,19;
  (4,3,4) at q = 17,19; then the same at V = 5, 6.
* **FB (kills the V >= 5 rescue).** The same at V >= 5 with Delta <= 0.
* **FC (kills the BLOCK premise).** A gate-clean zero-escape
  non-collapsing system whose complements A_a = U \ S_a are NOT
  pairwise disjoint (overlapping-complement shape).  Search: random
  systems with prescribed overlaps, small q, all k.
* **FD (kills the consumer).** A gate-clean zero-escape non-collapsing
  system with V > |U|/2 (this, not the pencil, is what L-A is consumed
  for: V_0 <= n/2).
* **FE (kills the reduction).** Any fixture where the T_a/E reduction
  disagrees with the banked zec.ann_dim / rank_row duality.

## Pre-registered fallback statement (if FA fires)

L-A(weak): with g := the common factor of the g_a (dim G = 1 case),
Z := zeros of g in A_1 u A_2, all blocks lie in the linear system
P_1 + P_2, P_i = {B : deg B <= t, B g = 0 mod B_i}, of dimension
<= |Z| + 2 <= e + 1; a PENCIL iff Z = empty.  To be tested as stated.
