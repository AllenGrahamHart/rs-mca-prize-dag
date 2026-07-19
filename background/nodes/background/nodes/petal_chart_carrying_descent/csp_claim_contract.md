# Claim contract (roadmap 5.1 form) — chart-carrying descent proof packet

```text
claim id:
  ccd_m2_proof_packet (SUCCESSOR-A yields #132 + #128 + K_2-reduction/composition)

mathematical statement:
  csp_statement.md, three claims:
  CLAIM 1 (#132, structure theorem S1-S6): at a fiber-aligned sigma=1 chart
    word U on the order-n 2-group coset, L_Z(X) = L_{Z'}(X^2)(X - x_nf);
    U(X) = (X - x_nf) u1(X^2) with u1 EXACTLY the quotient concrete chart
    word with unchanged labels c_i (L_{Z'} normalization); every scale->=2
    contributor is a lift (X - x_nf) g(X^2) with g a quotient contributor;
    g(y_nf) = 0 <=> scale->=2 membership (retained-zero descends
    automatically); d = 2d', r = 1 -> r' = 0 (reading A), a' = d'+1,
    m' = m, official band <=> quotient band; image factorization
    G_P = [(Y - y_nf) g/L_W](X^2), deg(g/L_W) <= d'-1; the descended charts
    satisfy the tail-collapse chain's hypotheses verbatim.
  CLAIM 2 (#128, P3 uniqueness U0-U2): abstract two-line degree lemma
    (2A - |P| > D - |W| => at most one member); every band chart at the
    descended row (reading A) holds AT MOST ONE member; margin exactly 1.
  CLAIM 3 (L0 + C): scale-M supports (M >= 2 dyadic) are K_2-invariant
    (subgroup lattice of a cyclic 2-group); IF a set A' of descended band
    charts covers the descended top band, THEN
    #{top-band classes of U with c(S) >= 2, all dyadic scales summed} <= |A'|.

quantifiers and row scope:
  all n = 2^s (s >= 2), all EVEN k with 2 <= k <= n-2, all prime powers q
  with n | q-1 (verifier exercises primes), all label vectors c_i in F_q^*;
  fiber-aligned layout (layout pin), sigma = 1 charts, descent scale M = 2,
  reading A bookkeeping (core'' = Z' u {y_nf}, sigma' = 0, r' = 0).
  SCOPED OUT: sigma > 1 charts; odd k; direct X -> X^M descent at M > 2
  (refuted-as-mechanism, catch #130; replaced by Claim 3 L0).

consumer node and exact slot:
  petal_chart_carrying_descent (SUCCESSOR-A): obligation (i) = S3/S4,
  obligation (ii) = S5/S6, the re-posed M=2 + K_2-reduction clause = L0/C,
  the per-chart line = Claim 2 (sharpens m'+1 to 1). Downstream:
  petal_small_scale_staircase_census per-U pricing (via C).

current status:
  Claims 1, 2, and 3-L0: PROVED (complete proofs, csp_proof.md; no step
  rests on search evidence). Claim 3-C: PROVED as stated (conditional on
  its single explicit coverage hypothesis, which is G1's open content).

dependencies already proved:
  petal_top_band_tail_collapse, petal_full_touched_set_injection,
  petal_retained_zero_effective_degree (critical/nodes, PROVED);
  thm:stabilizer-partition(i) (v13; petal_g2_support_forcing PROVED) —
  also re-proved inline as L0 for self-containment;
  cyclic_fiber_interleaving_descent's M=2 component decomposition —
  re-proved inline as L2;
  def/prop:capf-concrete-sunflower, def:capf-sunflower-layer (v13) —
  consumed for bookkeeping conventions only.

new open content:
  NONE at M = 2 within scope, except Claim 3-C's coverage hypothesis:
  G1 must supply a covering band-chart atlas at the quotient row for the
  descended word u1, within budget (residual list R, csp_statement.md;
  the ~4e4 charts/word demand of catch #131 lands there).

falsifier or failure witness:
  (a) any cell where the official fiber-subset census and the quotient
      point-subset census disagree through the lift bijection;
  (b) a scale->=2 contributor not of the form (X - x_nf) g(X^2);
  (c) two distinct members in one descended band chart (would contradict
      U0's field algebra — also directly machine-checkable);
  (d) a descended member violating any of d = 2d', r = 1, a' = d'+1,
      band equivalence, or the image factorization.
  csp_verify.py checks all four on every enumerated member.

proof route being attempted:
  COMPLETED: direct algebra — antipodal locator pairing (S1), fiberwise
  2x2 Vandermonde (L2), degree/root counts (S3, U0), verbatim hypothesis
  checks against the proved tail-collapse chain (S6).

replay command, if computational:
  cd /home/u2470931/smooth-read-solomin/prize && tools/ramguard tiny -- \
    python3 <scratchpad>/csp_verify.py
  (exit 0; 15 structure cells, 13 dual-census cells incl. 9 pinned banked
  cells and 4 NEW cells — the (32,20) row shape, (16,8,577), (32,16,353) —
  332 members through the full battery, 4/4 mutation controls trip.)

upstream hard-input mapping:
  reading A pin = catch #129 (statement Section 0);
  layout pin = petal_small_scale_staircase_census fiber-aligned convention;
  band pin P1 d >= ell(m-2) = the official band, shown EQUIVALENT to the
  quotient band at m' = m (S5);
  normalization pin = catch #133 (labels c_i vs c_i/(y_i - y_nf));
  retained-zero chart constraint = catch #107 (descends as y_nf in W).
```
