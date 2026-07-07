# Falsification-pruning ledger

Branch: `codex-falsification-pruning-20260705`

Ground truth: fresh worktree from `prize` `master` at `94f3c17`.

Protocol notes:
- Worktree only; no edits to `master`.
- `~/.modal.toml` exists, but neither the `modal` CLI nor the Python `modal`
  module is installed in this shell. Until Modal is available, runs are local,
  bounded by `timeout 60`, and scripts still checkpoint JSON partials.
- No status/node/edge changes have been made yet, so `tools/dag_commit.sh` has
  not been run.

## Attempt 1: sov_gridsum_residual / Bohr-pricing crux

Date: 2026-07-05

Node: `sov_gridsum_residual`

Actual open obligation attacked:
`price/rule the paid_large_power_sum/additive-Bohr class`. This is the repaired
post-T4B crux. I did not test the already-settled mechanism
`small value set => Bohr caught`.

Question:
Is the large-power-sum gate narrow enough to be plausibly priced, or does it
include a broad/high-mass class unless the Lane-1 Euler-product threshold is set
very tightly near `B=1`?

Script:
`experiments/falsification_pruning/sov_bohr_pricing_census.py`

Replay command:

```bash
timeout 60 python3 experiments/falsification_pruning/sov_bohr_pricing_census.py --seconds 55
```

Result JSON:
`experiments/falsification_pruning/results/sov_bohr_pricing_census.json`

Modal app name + wall time:
`modal_unavailable_in_shell`; local bounded run, `wall=3.60s`, `rss_kb=32820`.

What was tested:
- Exact small-prime census of `m`-point residual root cells `Gamma subset F_p^*`.
  For each cell, compute the largest additive Fourier/power-sum ratio and the
  value-set fraction of `h`-subset sums.
- Analytic interval-family frontier `Gamma={1,...,(p-1)/R}` at
  `p=65537, h=21`, recording Fourier ratio, `C(m,h)/C(p-1,h)` density, and the
  no-wrap value-set model. This parameterizes the known T4B adversarial family
  as a pricing stress curve.

Main observations:
- The interval family is exactly the pricing stressor. At `R=64`, the run
  reproduces the T4B scale: Fourier ratio `0.999598`, value-set fraction
  `0.321406`, and locator-density `log2 C(m,h)/C(p-1,h) = -126.293`.
- Collapsing interval rows only become clearly small-value-set around
  `R>=48`, with log2 densities about `-117.5, -126.3, -138.8, -147.6` for
  `R=48,64,96,128`. These are narrow but not ignorable: they sit in the same
  order as the intended `2^-128` ledger scale.
- Exact toy rows show the threshold is load-bearing. In the sampled
  `(p,m,h)=(29,7,4)` row, threshold `0.93` would leave `2163/150000` sampled
  low-value-set cells in the residual, because the worst observed residual has
  max-power ratio `0.90865` and value fraction `0.44828`. This is toy-scale
  only, but it warns against assuming a high cutoff without proving the
  Lane-1 bound below it.
- Low thresholds over-include badly. At threshold `0.70`, the sampled
  `(29,7,4)` row gates `11.55%` of cells; at threshold `0.50`, `92.88%`.
  This supports the prior note that the Bohr gate must be tight and cannot be
  a broad paid class by naive counting.

Verdict:
`NO_DELETION_SIGNAL / PRICING_CRUX_SHARPENED`.

The node is not falsified by this run, but it is not stable-frontier certified
either. The attack hit the actual crux and confirms the key pressure point:
the paid Bohr class is plausible only with a tight near-`B=1` threshold and a
matched Lane-1 theorem below that threshold. A sloppy large-power-sum gate is
too broad, while too high a gate leaves residual low-value-set cells in toys.

## Attempt 2: m720_conductor_compression / survivor field-degree calibration

Date: 2026-07-05

Node: `m720_conductor_compression`

Actual open obligation attacked:
survivor-conditioned descent / obstruction field degree. The already-confirmed
height table was not re-tested.

Important scope warning:
The local repo contains replayed non-toral calibration survivors for small
`h`, but not official `h=7..20` survivor records. This attempt therefore tests
the closest available survivor data and should be read as calibration stress,
not as an official-band counterexample.

Question:
Do known non-toral survivor/trade structures automatically lie in small
cyclotomic subfields, or can their survivor data have large/full Galois orbit
degree?

Script:
`experiments/falsification_pruning/m720_survivor_field_degree.py`

Replay command:

```bash
timeout 60 python3 experiments/falsification_pruning/m720_survivor_field_degree.py --seconds 55
```

Result JSON:
`experiments/falsification_pruning/results/m720_survivor_field_degree.json`

Modal app name + wall time:
`modal_unavailable_in_shell`; local bounded run, `wall=1.88s`, `rss_kb=162400`.

What was tested:
- Replayed the known local non-toral calibration rows:
  `(n,h,p)=(16,3,17),(16,3,97),(16,4,17),(32,5,97),(128,3,17921)`.
- For each trade pair, computed Galois orbit degrees over `Q(zeta_n)` for:
  `e_h(A)-e_h(B)`, the support union `A union B`, and the unordered pair
  `{A,B}`.

Main observations:
- Large/full degrees are common in calibration survivor data.
- At `(n,h,p)=(32,5,97)`, all `96` non-toral trades have unordered-pair field
  degree `16=phi(32)`, and `60/96` have `e_h`-difference degree `16`.
- At `(n,h,p)=(128,3,17921)`, `320/384` non-toral trades have unordered-pair
  field degree `64=phi(128)`, and `184/384` have `e_h`-difference degree `64`.
- Even at `n=16`, the unordered pair degree is full `8=phi(16)` for all
  non-toral h=3 trades in the checked rows.

Verdict:
`CALIBRATION_STRESS / NO_OFFICIAL_REFUTATION`.

This does not falsify the official `h=7..20` m720 node, because those cases need
actual official survivor records or a structural theorem. It does falsify the
naive descent shortcut "known non-toral survivor structure is automatically
low-field." Any repair must be genuinely survivor-conditioned in the official
band, or else use the D-GCD/certificate route.

## Attempt 3: e22_mixed_petal_covariance / source achievability

Date: 2026-07-05

Node: `e22_mixed_petal_covariance`

Actual open obligation attacked:
the source-achievability claim that the E22 sunflower/moment-trade construction
supplies BOTH:

- pointwise covariance `H_i(eta x)=eta^e H_i(x)` for a dyadic local modulus;
- off-tail exhaustivity `T_i \ B = {x in P_i \ B : H_i(x)=0}`;

after one bounded common tail. This does not merely test the settled fact that
those clauses would imply quotient-factor structure.

Question:
In the repo's executable local E22 sunflower cells, do actual listed
mixed/full-petal challengers admit the claimed covariance + exhaustivity
certificate, or do the cofactor equations hold without the source clauses?

Script:
`experiments/falsification_pruning/e22_source_achievability_probe.py`

Replay command:

```bash
timeout 60 python3 experiments/falsification_pruning/e22_source_achievability_probe.py --seconds 55
```

Result JSON:
`experiments/falsification_pruning/results/e22_source_achievability_probe.json`

Modal app name + wall time:
`modal_unavailable_in_shell`; local bounded run, `wall=2.14s`, `rss_kb=16836`.

What was tested:
- Used the repo's `nodes/worst_word_challenger_pricing/notes/e22_core.py`
  machinery, not a generic polynomial proxy.
- Enumerated local E22 sunflower cells
  `(n,k,sigma)=(16,2,1),(16,4,1),(16,8,1)` plus sigma-2 controls.
- For each listed structured challenger, constructed the actual cofactor
  polynomials
  `H_i = U L_{Z\C} - a_i L_{C\Z}` from the proved
  `e22_agreement_cofactor_equations` identity.
- Searched for dyadic moduli `M_i|n`, `M_i>sigma`, character residues `e_i`,
  and a common tail whose size is `< min_i M_i`, such that every touched petal
  satisfies pointwise covariance on `mu_n` and off-tail exhaustivity.

Main observations:
- Divisor/evaluation checks pass in the failures: every touched-petal agreement
  point is indeed a zero of its `H_i`. Thus this is not a broken cofactor
  equation.
- Source certificates fail for every structured sigma-1 challenger found:
  - `(16,2,1)`: `6` structured challengers, `0` certificate passes.
  - `(16,4,1)`: `23` structured challengers, `0` certificate passes.
  - `(16,8,1)`: `56` structured challengers, `0` certificate passes.
- In the first failures, off-tail exhaustivity is already exact on each touched
  toy petal (`off_tail_symdiff=[]`), but `candidate_moduli_with_covariance=[]`
  for every touched petal. The obstruction is specifically the pointwise
  covariance clause, not extra zeros.
- Sigma-2 controls have no structured challengers in scope, matching the local
  E22 gate behavior.

Verdict:
`FALSIFIER_CANDIDATE / SOURCE_SCOPE_GAP`.

This is stronger than a bare-divisibility counterexample because it uses actual
local listed challengers and actual cofactor polynomials. It suggests that
`e22_mixed_petal_covariance` is too broad if it claims all local E22 structured
challengers receive pointwise covariance from the sunflower source.

Salvage check:
This looks salvageable, not prune-worthy. The likely repair is to restrict the
source clause to a narrower square-shift / character-balanced subfamily and add
a separate statement that the local non-covariant structured challengers are
already paid, excluded, or routed by another column. Until that scope is stated
and re-attacked, the node should not be treated as a stable frontier.

## Attempt 4: petal_primitive_residue_kernel_rank / multi-character repair budget

Date: 2026-07-05

Node: `petal_primitive_residue_kernel_rank`

Actual open obligation attacked:
not the already-refuted absolute `B_pet` bound. This attacks the proposed repair:
add multi-character paid classes and prove they are chargeable.

Question:
Is the multi-character repair a small finite-menu patch, or does it require a
large parameterized paid family with growing residual dimension and many active
character types?

Script:
`experiments/falsification_pruning/prk_multichar_chargeability_budget.py`

Replay command:

```bash
timeout 60 python3 experiments/falsification_pruning/prk_multichar_chargeability_budget.py
```

Result JSON:
`experiments/falsification_pruning/results/prk_multichar_chargeability_budget.json`

Modal app name + wall time:
`modal_unavailable_in_shell`; local bounded run, `wall=0.04s`, `rss_kb=14848`.

What was tested:
- The canonical character-block model
  `F(X)=sum_{r mod M} X^r B_r(X^M)` over degrees `0..c`.
- Single active characters are treated as the existing quotient/isotypic paid
  shape.
- Active sets with at least two characters are the proposed multi-character
  repair burden.
- For each `(M,c)`, measured:
  - number of multi-character active sets, `2^M-M-1`;
  - residual dimension after peeling the largest single character block;
  - two-character residual dimension, showing the smallest multi-character
    obstruction still grows with `c`;
  - all-character residual dimension, matching the generic all-block stress.

Main observations:
- Even two-character families have residual dimension growing linearly with
  `c/M`; e.g. for `M=3,c=23`, the two-character residual is `8`, while the
  all-character residual is `16`.
- For `M=8,c=63`, there are `247` multi-character active sets, with
  all-character residual dimension `56`.
- For `M=32,c=255`, there are `4,294,967,263` multi-character active sets
  (`log2 ~= 32`) and all-character residual dimension `248`.
- For `M=64,c=511`, there are `18,446,744,073,709,551,551` active sets and
  all-character residual dimension `504`.

Verdict:
`REPAIR_BUDGET_PRESSURE / PARAMETERIZED_PAID_FAMILY_REQUIRED`.

This does not newly falsify PRK; the node is already falsified as stated in
`statement.md`. It does rule out treating the repair as a small finite menu
uniformly in `M`. A salvage must define a uniform parameterized multi-character
paid family and prove its ledger price, or else descend to
`petal_cofactor_chargeability` with the multi-character bulk still unpaid.

## Attempt 5: dli_prime_weighted_large_block_support / U-weighted average

Date: 2026-07-05

Node: `dli_prime_weighted_large_block_support`

Actual open obligation attacked:
the corrected DLI obligation after the per-profile sup formulation was
refuted: the U-weighted average over central profiles, not the false statement
`sum_j sup_M log_q rho_j(M)=o(t)`.

Question:
Do the low-mass profiles that kill the sup formulation still create a
positive-exponent contribution after U-weighting and profile averaging, or does
the central weighted average flatten?

Script:
`experiments/falsification_pruning/dli_weighted_average_probe.py`

Replay command:

```bash
timeout 60 python3 experiments/falsification_pruning/dli_weighted_average_probe.py --seconds 55
```

Result JSON:
`experiments/falsification_pruning/results/dli_weighted_average_probe.json`

Modal app name + wall time:
`modal_unavailable_in_shell`; local bounded run, `wall=0.26s`, `rss_kb=30164`.

What was tested:
- The true U-weighted average in the canonical inactive/ternary central family.
  If a profile chooses active ternary domain `{-1,0,+1}` on `S` and inactive
  domain `{0}` off `S`, with `U(S)=3^|S|`, then
  `avg_U rho(S) = q^L Pr[A d=0]` for independent
  `Pr[d_i=0]=1/2`, `Pr[d_i=+1]=Pr[d_i=-1]=1/4`.
  This is the weighted-average object, not a per-profile sup proxy.
- Exact floating DP for the odd-eval equations on square-root sections:
  `(q,n,L,N)=(17,16,1,8),(97,32,1,16),(193,64,2,32),
  (257,256,2,32/64/128),(7681,512,1,256)`.
- A low-mass zero-skew entropy envelope at prize field size `q=2^256` for
  `N=alpha L`, `alpha in {16,32,64,128,256}`, all supports `|S|<=L`.

Main observations:
- Exact U-weighted DP rows are flat to numerical precision:
  - `q=17,n=16,L=1,N=8`: `rho=1.000244`, `log_q rho/L=8.62e-5`.
  - `q=97,n=32,L=1,N=16`: `rho=1.00000078`, `log_q rho/L=1.71e-7`.
  - `q=193,n=64,L=2,N=32`: `rho=1.00000130`,
    `log_q rho/L=1.24e-7`.
  - `q=257,n=256,L=2,N=128`, prefix and spread sections:
    `rho=1.0` to printed precision, `log_q rho/L~=2.0e-17`.
  - prize-shaped toy ratio `q=7681,n=512,L=1,N=256`:
    `rho=1.0` to printed precision.
- The low-mass zero-skew envelope is dangerous at small coordinate ratios
  (`alpha=16` has worst tested `log_q/L=0.895`) but flips sign by the
  prize-shaped seen-coordinate ratio. At `alpha=256`, the worst tested
  `L<=16` has `log_q/L=-0.9639`; for `L=16` the total contribution from all
  supports `|S|<=L` is already `q^-15.423`.

Verdict:
`NO_FALSIFIER / WEIGHTED_AVERAGE_REPAIR_SUPPORTED_IN_CANONICAL_FAMILY`.

This directly tests the repaired weighted-average object and the specific
low-mass mechanism that refuted the sup formulation. The low-mass family does
not remain a counterexample after U-weighting at the prize-shaped `N=256L`
ratio, and the exact small weighted DPs show no positive-exponent growth.

Caveat:
This is still evidence, not proof. It covers the inactive/ternary central
family and small exact odd-eval rows; it does not count every large-support
resultant-survivor family in the full tower. No DAG status change is made.

## Attempt 6: rate_half_band_closure / guardrail replay

Date: 2026-07-05

Node: `rate_half_band_closure`

Actual open obligation attacked:
the node no longer has a precise surviving positive lemma to falsify. The
current crux is: either find a genuinely new mechanism for the residual
rate-1/2 band, or prove a bracket/tightness theorem. This attempt replays and
extends the arithmetic guardrails around the known routes so we do not mistake
an already-dead route for a hidden closure.

Question:
Can the known quotient-floor / q-threshold / AQB arithmetic secretly close the
band, or does the branch really remain a new-mechanism-or-bracket problem?

Script:
`experiments/falsification_pruning/rate_half_guardrail_replay.py`

Replay command:

```bash
timeout 60 python3 experiments/falsification_pruning/rate_half_guardrail_replay.py --seconds 55
```

Result JSON:
`experiments/falsification_pruning/results/rate_half_guardrail_replay.json`

Modal app name + wall time:
`modal_unavailable_in_shell`; local bounded run, `wall=0.06s`, `rss_kb=17336`.

What was tested:
- Local replay of the quotient-remainder floor depth at `Q=log2 q=256`.
- Local binary search for the `log2 q` threshold below which the same floor
  covers `sigma*`.
- Local replay of the AQB c=2 deficit constants using Robbins/Stirling
  high-precision bounds, matching the existing AQB arithmetic verifier.

Main observations:
- The quotient-remainder floor max depth at `Q=256` is exactly
  `8,589,934,592 = 2^33`.
- The crossing is `sigma*=8,592,912,738`, so the residual gap is
  `2,978,146` radii (`2,978,147` with the ledger endpoint convention).
- The floor-depth plateau is achieved for 12 dyadic scales, `e=22..33`.
- The q-threshold replay gives `threshold_log2q=255.8999902876`; the band is
  confined to the top `0.1000097` bits of the admissible field-size range.
- AQB finite arithmetic matches the verifier:
  deficit `429,645,546.773407953684...` bits, claimed gain
  `429,645,547` bits, certified arithmetic margin `0.226592...` bits, and
  per-fiber gain `0.0003907603486` bits. This only measures the required gain;
  the convex-combination refutation still kills box-charge amortization without
  a separate heavy-fiber theorem.

Verdict:
`GUARDRAIL_REPLAY / RATE_HALF_CRUX_UNCHANGED`.

This does not close or falsify `rate_half_band_closure`. It confirms that the
known arithmetic routes leave exactly the stated narrow band and that the live
crux is genuinely one of: a new non-AQB mechanism, a B2b-style balance theorem,
a safe-side push, or a bracket/tightness theorem. No DAG status change is made.

## Attempt 7: E22 reduced common-tail payload / vacuity check

Date: 2026-07-05

Node:
`e22_tail_removed_factor_manifest_payload`, the reduced payload under
`e22_mixed_petal_covariance`.

Actual open obligation attacked:
the corrected/reduced E22 payload after the global-covariance stress test:
provide one common tail `B`, dyadic local moduli `M_i>t`, `|B|<min_i M_i`,
and kernel invariance of every `T_i\B` for actual listed mixed/full-petal
challengers. This tests the common-tail certificate itself, not global
polynomial covariance of `H_i`.

Question:
Do actual E22 local challengers admit the reduced common-tail certificate, and
if they do, is the certificate nontrivial enough to retain quotient-fiber
structure rather than deleting every touched agreement point into the tail?

Script:
`experiments/falsification_pruning/e22_common_tail_certificate_probe.py`

Replay command:

```bash
timeout 60 python3 experiments/falsification_pruning/e22_common_tail_certificate_probe.py --seconds 55
```

Result JSON:
`experiments/falsification_pruning/results/e22_common_tail_certificate_probe.json`

Modal app name + wall time:
`modal_unavailable_in_shell`; local bounded run, `wall=13.42s`,
`rss_kb=23792`.

What was tested:
- Actual listed E22 mixed/full-petal challengers from `e22_core.py`.
- Rows:
  `(16,2,1),(16,4,1),(16,8,1),(16,2,2),(16,4,2),(16,8,2),
  (32,2,1),(32,4,1),(32,2,2)`.
- For each touched petal agreement set `T_i`, searched dyadic moduli `M_i>t`
  and a single global tail `B` such that each `T_i\B` is a union of full
  fibers of `x -> x^{M_i}`.
- Separately counted:
  - any formal common-tail certificate, allowing empty non-tail sets;
  - a nontrivial certificate retaining at least one full quotient fiber
    somewhere;
  - a stronger certificate retaining nonempty full-fiber data on every touched
    petal.

Main observations:
- Structured challengers tested: `1094`.
- Formal common-tail certificates found: `1094/1094`.
- Nontrivial retained-fiber certificates found: `0/1094`.
- Per-touched nonempty certificates found: `0/1094`.
- The row breakdown is:
  - `(16,2,1)`: `6/6` formal, `0/6` nontrivial.
  - `(16,4,1)`: `23/23` formal, `0/23` nontrivial.
  - `(16,8,1)`: `56/56` formal, `0/56` nontrivial.
  - `(32,2,1)`: `32/32` formal, `0/32` nontrivial.
  - `(32,4,1)`: `976/976` formal, `0/976` nontrivial.
  - `(32,2,2)`: `1/1` formal, `0/1` nontrivial.
- The formal certificates delete all touched agreement points into `B`; e.g.
  a typical `(16,2,1)` challenger uses `M_i=4`, tail size `3`, retained
  non-tail size `0`.

Verdict:
`SALVAGE_SURVIVES_FORMALLY / NONTRIVIALITY_GAP`.

This corrects Attempt 3: the reduced common-tail payload is not refuted by the
toy challengers if empty non-tail sets are allowed. However, in all tested
structured challengers the certificate is vacuous: it retains no full quotient
fiber. Thus E22 should not be called a stable frontier until the payload is
strengthened with a non-vacuity/pricing condition, or until the all-tail case is
shown to be paid by the existing E22 staircase arithmetic. No DAG status change
is made.

## Attempt 8: E22 all-tail pricing coverage and multiplicity stress

Date: 2026-07-05

Node:
`e22_challenger_staircase_pricing`, downstream of the reduced
`e22_tail_removed_factor_manifest_payload` salvage.

Actual open obligation attacked:
whether the all-tail common-tail certificates from Attempt 7 are covered by
the dyadic minimal-scale staircase pricing machinery, and whether the selected
support-scale representatives are injective enough for the list-side challenger
column.

Question:
If all touched petal agreement points are deleted into the common tail, are
those supports still selected by the minimal-scale pricing column, or do they
fall outside the paid E22 staircase? Separately, do distinct listed codewords
collapse to the same selected touched-support representative, creating a
possible multiplicity gap?

Script:
`experiments/falsification_pruning/e22_tail_only_pricing_coverage.py`

Replay command:

```bash
timeout 60 python3 experiments/falsification_pruning/e22_tail_only_pricing_coverage.py --seconds 55
```

Result JSON:
`experiments/falsification_pruning/results/e22_tail_only_pricing_coverage.json`

Modal app name + wall time:
`modal_unavailable_in_shell`; local bounded run, `wall=5.66s`,
`rss_kb=16128`.

What was tested:
- Actual listed E22 mixed/full-petal challengers from `e22_core.py`.
- Rows:
  `(16,2,1),(16,4,1),(16,8,1),(16,2,2),(16,4,2),(16,8,2),
  (32,2,1),(32,4,1),(32,2,2)`.
- For each structured challenger, the probe formed the touched petal agreement
  support, applied the proved dyadic tail criterion `|B_M(R)| < M`, selected
  the minimal admissible scale, and checked for missing representatives and
  collisions.

Main observations:
- Structured challengers tested: `1094`.
- Missing selected representatives: `0`.
- Representatives with at least one full quotient fiber: `39`.
- Tail-only selected representatives are common: `1055` structured challengers
  are tail-only after touched-support projection.
- Selected-representative collisions: `6`, all in the tiny
  `(n,k,sigma)=(16,8,1)` row.
- Polynomial excess over those colliding representatives: `7`.
- The first collision has selected representative
  `(M=8, tail={7,10,11,12,13}, no full fibers)` and three distinct degree-`<8`
  polynomials. They agree on the same touched petal support but have different
  full agreement supports:
  `{0,1,2,4,7,10,11,12,13}`,
  `{0,1,5,6,7,10,11,12,13}`,
  `{2,3,4,7,10,11,12,13,15}`.

Interpretation:
The all-tail salvage is not omitted by the support-scale pricing machinery:
every tested structured challenger has a selected minimal-scale representative.
However, the touched-support projection is not injective as a codeword count.
If the E22 challenger column is meant to count only selected touched-support
classes with multiplicity one, the `(16,8,1)` cell is a concrete undercount
candidate. If the declared multiplicity already includes the background/core
completion choices, this is expected and should be documented explicitly in the
consumer node.

Verdict:
`SELECTED_REPRESENTATIVE_COLLISION_CANDIDATE /
MULTIPLICITY_OBLIGATION_SHARPENED`.

No deletion or DAG status change is made. E22 remains a live frontier rather
than a falsified node: coverage survived, but the pricing proof should state
and verify the codeword-level multiplicity convention for tail-only
representatives.

## Attempt 9: Petal squarefree ledger generic-mass probe

Date: 2026-07-05

Node:
`petal_squarefree_classification_ledger_payload`, the current live descendant
of the refuted `petal_primitive_residue_kernel_rank` route.

Actual open obligation attacked:
whether squarefree realizable locator points inside the Petal residue-line
kernels contain a generic missed-core family whose count grows with the excess
`c` and therefore cannot be left as a uniformly bounded uncharged residual.

Question:
In the in-regime corridor `d = ell + c <= (t-1)ell - 1`, do random full-core
missed-core locators or capped exact-prefix pools satisfy the CRT
realizability condition `deg CRT(c_i F mod L_i) <= d` often enough to create a
raw generic-mass falsifier for the squarefree classification ledger?

Script:
`experiments/falsification_pruning/petal_squarefree_ledger_scope_probe.py`

Replay command:

```bash
timeout 60 python3 experiments/falsification_pruning/petal_squarefree_ledger_scope_probe.py --seconds 55
```

Result JSON:
`experiments/falsification_pruning/results/petal_squarefree_ledger_scope_probe.json`

Modal app name + wall time:
`modal_unavailable_in_shell`; local bounded run, `wall=33.04s`,
`rss_kb=14720`.

What was tested:
- Coset-chart petal rows over `F_1009`:
  `(ell,t)=(2,3),(2,5),(3,5),(3,6)`.
- Sequential scalars `c_i=1,...,t`.
- Only the proof's in-regime rows:
  `d=ell+c <= (t-1)ell - 1`.
- For each row:
  - exact enumeration over the prefix core pool of size `d+6`, capped at
    `20000` candidates;
  - `200` random missed-core locators from the full core pool.

Main observations:
- In-regime exact-prefix candidates evaluated: `67210`.
- In-regime exact-prefix realizable hits: `0`.
- Random full-core samples evaluated: `4000`.
- Random full-core realizable hits: `0`.
- Row details:
  - `(1009,2,3)`: no requested `c>=2` lies in regime.
  - `(1009,2,5)`: `c=2..5`, all exact and random counts `0`.
  - `(1009,3,5)`: `c=2..8`, all exact and random counts `0`.
  - `(1009,3,6)`: `c=2..8`, all exact and random counts `0`.

Scope correction:
An initial run before the in-regime guard found apparent generic mass at
endpoint rows such as `(ell,t,c,d)=(2,5,7,9)`. Those rows violate
`d <= (t-1)ell - 1`; near `d=t ell-1`, the CRT degree test becomes almost
automatic and is not the Petal ledger object. The script now enforces the
in-regime condition so this artifact is excluded.

Interpretation:
The obvious generic-missed-core falsifier did not land. In the tested
in-regime coset rows, squarefree realizability is highly nongeneric: neither
random full-core samples nor exact capped prefix pools produced a single
realizable locator. This supports the current Petal refactor's premise that
the squarefree-realizable scoping does real work. It does not construct the
ledger, classify adversarial structured families, or prove the uncharged
bound.

Verdict:
`NO_GENERIC_REALIZABLE_MASS_FOUND / SQUAREFREE_SCOPE_SUPPORTED`.

No deletion or DAG status change is made. The Petal ledger payload remains the
stable live frontier: generic mass resisted falsification, while the open work
is to classify the structured squarefree-realizable families that survive the
kernel constraints.

## Attempt 10: M720 Modal residual slice witness search

Date: 2026-07-05

Node:
`m720_official_norm_gate_case_manifest_payload`, the current live M720
h=7..20 descendant of `m720_conductor_compression`.

Actual open obligation attacked:
whether the residual h=7..20 calibration/window-slice cells contain an unpaid
non-toral anchored active core. A found witness would falsify the bounded-band
zero/exclusion strategy. Absence of a witness is evidence only because these
are window slices, not complete official manifests.

Question:
In selected residual MITM windows, do there exist disjoint anchored halves
`P={0}+...` and `Q` with equal lower elementary signatures, unequal top
coefficient, and not both toral cosets?

Script:
`experiments/falsification_pruning/m720_modal_slice_probe.py`

Replay commands:

```bash
timeout 75 ~/.venvs/modal-client/bin/python experiments/falsification_pruning/m720_modal_slice_probe.py --seconds 50 --count-ceiling 1500000
timeout 75 ~/.venvs/modal-client/bin/python experiments/falsification_pruning/m720_modal_slice_probe.py --seconds 50 --count-ceiling 500000 --output experiments/falsification_pruning/results/m720_modal_slice_probe_h8_10.json --config 128,8,2 --config 128,8,3 --config 128,9,2 --config 128,9,3 --config 256,8,2 --config 256,9,2 --config 256,10,2
```

Result JSON:
- `experiments/falsification_pruning/results/m720_modal_slice_probe.json`
- `experiments/falsification_pruning/results/m720_modal_slice_probe_h8_10.json`

Modal app name + wall time:
`rs-mca-m720-slice-probe-20260705`.
Run 1: local wall `53.51s`, remote elapsed `48.20s`.
Run 2: local wall `32.11s`, remote elapsed `26.82s`.

What was tested:
- Run 1, count ceiling `1,500,000`:
  - `(n,h,q_exp,p,W)=(64,7,2,4289,28)`;
  - `(64,7,3,262337,28)`;
  - `(128,7,2,17921,28)`;
  - `(128,7,3,2100097,28)`;
  - partial `(128,8,2,17921,25)`.
- Run 2, count ceiling `500,000`:
  - `(128,8,2,17921,22)`;
  - `(128,8,3,2100097,22)`;
  - `(128,9,2,17921,21)`;
  - `(128,9,3,2100097,21)`;
  - `(256,8,2,65537,22)`;
  - `(256,9,2,65537,21)`;
  - `(256,10,2,65537,20)`.

Main observations:
- Run 1 evaluated `1,530,144` anchored-hash subsets and `3,560,312` probe
  subsets before the time budget cut the final h=8 cell.
- Run 1 unpaid non-toral witnesses: `0`.
- Run 2 evaluated `819,128` anchored-hash subsets and `1,206,728` probe
  subsets, with no aborts.
- Run 2 unpaid non-toral witnesses: `0`.
- Across both runs: `2,349,272` hash subsets, `4,767,040` probe subsets,
  and `0` unpaid non-toral anchored active cores.

Interpretation:
Modal is now installed and authenticated, and the M720 MITM slice object can
be attacked off-laptop under the 60-second container guardrail. The tested
residual slices did not produce a non-toral active-core falsifier. This
supports the h=7..20 bounded-band exclusion strategy, but it does not close the
official manifest: all listed rows are `complete=false` window slices, and the
official theorem still needs either a uniform exclusion theorem or complete
case records.

Verdict:
`NO_NONTORAL_SLICE_WITNESS_FOUND / OFFICIAL_MANIFEST_STILL_OPEN`.

No deletion or DAG status change is made. The M720 stable frontier remains the
official case-manifest payload: falsification found no slice witness, but the
complete official coverage theorem/certificate is still absent.

## Attempt 11: SOV downstream amber-premise Bohr dilution stress test

Date: 2026-07-05

Node:
`sov_gridsum_residual`, with attention to the immediate downstream SOV amber
chain ending in `single_obstruction_valueset`.

Actual open obligation attacked:
the premise consumed by the downstream amber reductions: the Bohr /
large-power-sum exceptional class must be sufficiently narrow and paid by the
ledger budget before the residual affine/Lane-1 machinery applies. The proved
amber implications are not the target here; the target is whether their input
condition over-includes high-mass cells.

Question:
Do diluted interval cells still pass low-frequency Bohr gates while behaving
nearly randomly under h-fold sum sampling, so that a broad Bohr gate would
charge an enormous family rather than only genuinely structured exceptions?

Script:
`experiments/falsification_pruning/sov_modal_bohr_dilution_probe.py`

Replay command:

```bash
timeout 75 ~/.venvs/modal-client/bin/python experiments/falsification_pruning/sov_modal_bohr_dilution_probe.py --seconds 50
```

Result JSON:
`experiments/falsification_pruning/results/sov_modal_bohr_dilution_probe.json`

Modal app name + wall time:
`rs-mca-sov-bohr-dilution-20260705`.
Local wall `14.20s`, remote elapsed `8.63s`.

What was tested:
For `p=65537`, `m=1024`, `h=21`, start from the interval cell
`{1,...,1024}` and replace a fraction `1-beta` of the interval points with
random outside points. For each beta in
`1.00, 0.98, 0.95, 0.93, 0.90, 0.85, 0.80, 0.70, 0.50`, sample `16` cells,
measure low-frequency Fourier ratios through frequency `12`, and estimate
h-fold sum collision ratios from `6000` sampled h-subsets.

Main observations:
- Pure interval baseline: median frequency-1 ratio `0.999598`, median sampled
  h-sum collision ratio `9.301` times the uniform occupancy baseline, and
  naive locator density `log2=-126.293`.
- Beta `0.98`: median frequency-1 ratio `0.979591`, median max-small-frequency
  ratio `0.981370`, and median collision ratio `5.015`; it passes thresholds
  through `0.98`, but the naive locator-mass accounting jumps to
  `log2=270.824`.
- Beta `0.95`: median frequency-1 ratio `0.951639`, median collision ratio
  `2.170`; it passes thresholds through `0.95`, with naive locator accounting
  `log2=756.932`.
- Beta `0.93`: median frequency-1 ratio `0.928287`, median max-small-frequency
  ratio `0.932123`, median collision ratio `1.500`; it passes thresholds
  through `0.93`, with naive locator accounting `log2=1050.780`.
- Beta `0.90`: median frequency-1 ratio `0.898104`, median max-small-frequency
  ratio `0.901071`, and median collision ratio `1.149`; it still passes
  thresholds through `0.90`, while behaving close to uniform under the sampled
  h-sum statistic.
- Beta `0.85` and below are essentially uniform for the sampled h-sum
  collision statistic, while still illustrating how broad frequency gates can
  include enormous diluted families if pricing is not tied to a sharper
  structural certificate.

Interpretation:
This is pressure on the downstream amber premise, not a refutation of the
proved implications. A coarse low-frequency Bohr gate is too broad: near-pure
interval cells are structured and rare, but small random dilutions can retain
threshold-passing Fourier ratios while the combinatorial family size explodes
under naive locator accounting. The SOV frontier should therefore require a
tight paid Bohr/large-power-sum certificate, or an internal fallback showing
that diluted threshold-passers return to the residual affine/Lane-1 regime.

Verdict:
`BROAD_BOHR_GATE_OVERINCLUSION_PRESSURE / DOWNSTREAM_PREMISE_NEEDS_TIGHT_PAID_GATE`.

No deletion or DAG status change is made. The SOV chain remains live, but this
attempt rules out treating a loose Bohr-threshold exception as automatically
chargeable.

## Attempt 12: M720 downstream amber-premise manifest audit plus n=1024 slices

Date: 2026-07-05

Node:
`m720_official_norm_gate_case_manifest_payload`, with attention to the
downstream amber consumers `m720_official_h7_20_norm_gate_payload`,
`m720_official_h7_20_norm_gate_certificates`, and `m720_official_exclusion`.

Actual open obligation attacked:
the premise consumed by the downstream amber reductions: an actual complete
official primitive `h=7..20` norm-gate manifest must exist, and every primitive
case must be discharged by a uniform theorem or by a `complete=true`
zero-survivor certificate. The proved manifest-to-payload implications are not
the target; the target is whether the manifest premise is presently supported
or contradicted by an unpaid non-toral slice witness.

Questions:
- Does the worktree contain enough certificate/theorem coverage to satisfy the
  complete official manifest premise?
- In a high-gap family not previously slice-probed here (`n=1024`, `h=7..9`),
  does a bounded Modal window find an unpaid non-toral active core?

Scripts:
- `experiments/falsification_pruning/m720_manifest_gap_audit.py`
- `experiments/falsification_pruning/m720_modal_slice_probe.py`

Replay commands:

```bash
python3 experiments/falsification_pruning/m720_manifest_gap_audit.py
timeout 75 ~/.venvs/modal-client/bin/python experiments/falsification_pruning/m720_modal_slice_probe.py --seconds 50 --count-ceiling 500000 --output experiments/falsification_pruning/results/m720_modal_slice_probe_n1024_h7_9.json --config 1024,7,2 --config 1024,7,3 --config 1024,8,2 --config 1024,8,3 --config 1024,9,2 --config 1024,9,3
python3 experiments/falsification_pruning/m720_manifest_gap_audit.py --result experiments/falsification_pruning/results/m720_modal_slice_probe_n1024_h7_9.json --output experiments/falsification_pruning/results/m720_manifest_gap_audit.json
```

Result JSON:
- `experiments/falsification_pruning/results/m720_manifest_gap_audit.json`
- `experiments/falsification_pruning/results/m720_modal_slice_probe_n1024_h7_9.json`

Modal app name + wall time:
`rs-mca-m720-slice-probe-20260705`.
Local wall `29.71s`, remote elapsed `24.75s`.

What was tested:
- The audit enumerates the configured official grid
  `h=7..20`, `n in {16,32,64,128,256,1024}`, `q_exp in {2,3}`, subject to
  `n >= 2h`, and classifies each row as:
  complete under-ceiling certificate, over-ceiling algebraic certificate,
  slice-probed with no unpaid non-toral witness, slice-probed with a witness,
  or not slice-probed in this clone.
- The new Modal run checked six `n=1024` window slices:
  `(1024,7,2)`, `(1024,7,3)`, `(1024,8,2)`, `(1024,8,3)`,
  `(1024,9,2)`, `(1024,9,3)`.

Main observations:
- Official configured rows in the audit: `136`.
- Complete under-ceiling certified rows: `6`.
- Over-ceiling algebraically certified rows: `2`.
- Slice-probed rows with no unpaid non-toral witness after the new Modal run:
  `17`.
- Slice-probed rows with an unpaid non-toral witness: `0`.
- Rows not slice-probed in this clone: `111`.
- New `n=1024` Modal slices:
  - `h=7`, `q_exp=2,3`: `W=24`, `100947` hash subsets and `245157` probe
    subsets per q-exponent, zero toral and zero unpaid non-toral witnesses.
  - `h=8`, `q_exp=2,3`: `W=22`, `116280` hash subsets and `203490` probe
    subsets per q-exponent, zero toral and zero unpaid non-toral witnesses.
  - `h=9`, `q_exp=2,3`: `W=21`, `125970` hash subsets and `167960` probe
    subsets per q-exponent, zero toral and zero unpaid non-toral witnesses.

Interpretation:
The downstream M720 amber chain is sound as an implication, but its manifest
premise is not satisfied by the current worktree evidence: most official rows
still lack even slice evidence here, and none of the slice rows are complete
official certificates. The new n=1024 slices add resistance evidence against a
cheap unpaid non-toral witness, but they do not repair the premise because
`W<n` in every new row.

Verdict:
`OFFICIAL_MANIFEST_PREMISE_UNSATISFIED_IN_WORKTREE / NO_N1024_SLICE_WITNESS_FOUND`.

No deletion or DAG status change is made. The M720 stable frontier remains the
actual official norm-gate manifest or a uniform nonvanishing theorem; slice
evidence is useful falsification pressure but not a certificate payload.

## Attempt 13: E22 downstream amber-premise vacuity audit

Date: 2026-07-05

Node:
`e22_tail_removed_factor_manifest_payload`, with attention to the downstream
amber consumers `e22_common_tail_invariance_payload` and
`e22_cofactor_common_tail_kernel_invariance`.

Actual open obligation attacked:
the premise `A` consumed by the downstream amber implications: the actual E22
cofactor equations must supply a common-tail / kernel-saturation or
tail-removed quotient-factor certificate. The implication from such a
certificate to kernel invariance is not the main target here. The target is
whether the certificate premise is true in a meaningful, pricing-useful form,
or whether it is satisfied only by a vacuous all-tail choice.

Question:
For adversarial E22 mixed/full-petal challengers, is the literal common-tail
premise merely automatic by taking `M_i=n` and deleting every touched point into
`B`, or does it leave retained quotient fibers at a proper local scale
`M_i<n`?

Script:
`experiments/falsification_pruning/e22_premise_vacuity_audit.py`

Replay command:

```bash
timeout 60 python3 experiments/falsification_pruning/e22_premise_vacuity_audit.py --seconds 55
```

Result JSON:
`experiments/falsification_pruning/results/e22_premise_vacuity_audit.json`

Wall time:
Local wall `51.67s`, RSS `17116 KB`. No Modal was used.

What was tested:
The audit enumerated `72` light E22 toy cells: rows
`(16,2,1)`, `(16,4,1)`, `(16,8,1)`, `(16,2,2)`, `(16,4,2)`,
`(16,8,2)`, `(32,2,1)`, `(32,4,1)`, `(32,2,2)`, crossed with the first
four coprime cyclic layouts per `n` and scalar modes `linear` and
`geometric`. For each structured mixed/full-petal challenger it checked:

- whether the literal all-tail certificate is available by taking `M=n`;
- whether any retained full quotient fiber exists at any dyadic scale; and
- whether any retained full quotient fiber exists at a proper local scale
  `M<n`.

Main observations:
- Structured challengers tested: `8393`.
- Literal all-tail certificate available: `8393 / 8393`.
- Challengers with a retained full quotient fiber at a proper scale: `1866`.
- Challengers with no retained proper-scale full quotient fiber: `6527`.
- The `n=16,k=8,sigma=1` family is especially stark: across the tested layouts
  and scalar modes, every structured challenger is all-tail-only (`439 / 439`)
  with no retained proper-scale quotient fiber.
- The `n=32,k=4,sigma=1` family has many retained fibers but is still mostly
  all-tail-only: `5795 / 7558` structured challengers have no retained
  proper-scale full quotient fiber.

Interpretation:
This is a premise-level warning, not an implication refutation. As currently
written, the literal E22 common-tail/kernel-saturation premise is too easy to
satisfy: if `M_i=n` is admissible, then any non-full touched support can be
made kernel-invariant by deleting the entire touched support into the common
tail. That proves the formal tail-removed identity only vacuously. The
downstream chain therefore needs either:

- an explicit pricing theorem for all-tail certificates; or
- a strengthened premise requiring a proper local scale and retained
  quotient-fiber mass, plus separate handling of all-tail-only challengers.

Verdict:
`LITERAL_PREMISE_ALWAYS_AVAILABLE_BUT_OFTEN_VACUOUS / PRICING_USEFUL_PREMISE_FAILS_ON_6527_OF_8393`.

No deletion or DAG status change is made yet. This does not kill the E22 chain,
because all-tail cases may be chargeable by the staircase pricing machinery,
but it identifies the undertested premise that must be stated and paid
explicitly.

## Attempt 14: PRK downstream amber-premise multi-character budget extension

Date: 2026-07-05

Node:
`petal_primitive_residue_kernel_rank`, with attention to the downstream amber
consumer `petal_cofactor_chargeability` and the live ledger premise
`petal_squarefree_classification_ledger_payload`.

Actual open obligation attacked:
the premise `A` consumed downstream: after the old PRK absolute-rank statement
was falsified, the repair must provide a real squarefree classification ledger.
Multi-character residue-kernel families must either be paid by cited charged
records, or the uncharged residue must have a polynomial bound whose exponent
is independent of the excess `c`. The conditional implication from such a
ledger to cofactor chargeability is not the target here.

Question:
How hostile is the multi-character repair premise as `M` and `c` grow? In
particular, can multi-character active sets be left uncharged while retaining a
`c`-independent residual dimension, or does the premise force a parameterized
paid family?

Script:
`experiments/falsification_pruning/prk_multichar_chargeability_budget.py`

Replay command:

```bash
python3 experiments/falsification_pruning/prk_multichar_chargeability_budget.py --M 3 5 7 8 16 32 64 128 256 --c-multiple 2 4 8 16 --enumerate-limit 10 --output experiments/falsification_pruning/results/prk_multichar_chargeability_budget_extended.json
```

Result JSON:
`experiments/falsification_pruning/results/prk_multichar_chargeability_budget_extended.json`

Wall time:
Local wall `0.05s`, RSS `14952 KB`. No Modal was used.

What was tested:
The model decomposes a cofactor polynomial of excess degree `c` into
`mu_M` character blocks

```text
F(X)=sum_{r mod M} X^r B_r(X^M).
```

Single active characters are the old quotient/isotypic paid shape. Active sets
with at least two characters are the proposed repair burden. For each
`M in {3,5,7,8,16,32,64,128,256}` and `c in {2M-1,4M-1,8M-1,16M-1}`, the script
computes the number of multi-character active-set types and the residual
dimension after peeling the largest single character.

Main observations:
- For `M=16`, the multi-character type count has `log2 ~= 16`; at `c=255`,
  even the smallest two-character residual has dimension `16`, while the
  all-character residual has dimension `240`.
- For `M=64`, type-count `log2 ~= 64`; at `c=1023`, smallest two-character
  residual dimension `16`, all-character residual `1008`.
- For `M=128`, type-count `log2 ~= 128`; at `c=2047`, smallest
  two-character residual dimension `16`, all-character residual `2032`.
- For `M=256`, type-count `log2 ~= 256`; at `c=4095`, smallest
  two-character residual dimension `16`, all-character residual `4080`.
- At fixed `M`, the two-character residual grows linearly with `c/M`; the
  all-character residual grows essentially like `c`.

Interpretation:
This does not newly refute the already-demoted old PRK statement; it attacks
the repair premise consumed by the downstream amber chain. A ledger that leaves
multi-character families uncharged cannot satisfy the `c`-independent exponent
condition. A ledger that charges them cannot be a small finite menu of
single-character or low-defect records: it needs a parameterized multi-character
paid family with an explicit budget/citation. Therefore the actual premise `A`
for `petal_cofactor_chargeability` remains unverified and very sharp.

Verdict:
`PARAMETERIZED_MULTICHAR_PAID_FAMILY_REQUIRED / UNCHARGED_C_INDEPENDENT_BOUND_REFUTED_IN_MODEL`.

No deletion or DAG status change is made. The PRK branch remains salvageable
only if the squarefree classification ledger explicitly pays these
multi-character active-set families or proves that they do not occur in the
actual squarefree-realizable locus.

## Attempt 15: DLI downstream amber-premise large-block threshold scan

Date: 2026-07-05

Node:
`dli_prime_weighted_large_block_support`, with attention to the downstream
amber consumer `dli_prime_block_conductor_mass`.

Actual open obligation attacked:
the premise `A` consumed downstream: under the actual DLI map-determined
central measure, the U-weighted mass of small/exceptional support must be
negligible, so the conductor-mass argument can ignore bounded-size block mass.
The conditional implication from large-block support to conductor mass is not
the target here.

Question:
Does the U-weighted entropy side of the premise suppress low-support profiles
at the prize-shaped seen-coordinate expansion `N=256L`, or is there a
low-support mass route that could keep conductor mass linear in `L`?

Script:
`experiments/falsification_pruning/dli_large_block_threshold_scan.py`

Replay command:

```bash
python3 experiments/falsification_pruning/dli_large_block_threshold_scan.py
```

Result JSON:
`experiments/falsification_pruning/results/dli_large_block_threshold_scan.json`

Wall time:
Local wall `0.03s`, RSS `14208 KB`. No Modal was used.

What was tested:
For inactive-or-ternary profiles on `N=alpha L` seen coordinates, the script
computes the U-weighted low-support contribution

```text
q^L * sum_{k <= beta L} binom(alpha L,k) / 4^(alpha L)
```

for `q_bits=256`, `alpha in {64,96,128,160,192,224,240,256,288,320}`,
`L in {1,2,4,8,16,32}`, and `beta in {1,2,4}`. The prize-shaped seen-coordinate
lever is `alpha=256`.

Main observations:
- For every tested `L` and `beta`, the first listed `alpha` with negative
  exponent is `160`.
- At prize `alpha=256`, the low-support exponent is strongly negative:
  - `beta=1`: about `-0.964` to `-0.969` in `log_q_per_L`;
  - `beta=2`: about `-0.935` to `-0.941`;
  - `beta=4`: about `-0.884` to `-0.893`.
- The existing weighted-average DP probe remains consistent with this: its
  exact DP rows had maximum `log_q_per_L = 8.62e-05`, with prize-shaped rows
  essentially `1.0` for the weighted average `rho`.

Interpretation:
This did not falsify the corrected DLI premise. It does falsify weaker
seen-coordinate margins: at `alpha=128`, low-support mass can still have
positive exponent, so the premise genuinely depends on the strong
`255L+1`/`256L` seen-coordinate lever. At the actual prize-shaped margin,
however, this low-support route is exponentially suppressed in the U-weighted
object. The remaining possible falsifiers would have to exploit the actual
map-partition geometry or exceptional block definitions, not merely sparse
support entropy.

Verdict:
`NO_LOW_SUPPORT_WEIGHTED_FALSIFIER_AT_ALPHA_256 / SEEN_COORDINATE_MARGIN_IS_LOAD_BEARING`.

No deletion or DAG status change is made. The DLI weighted large-block premise
survives this adversarial entropy scan, but it remains an open structural
statement about the actual map-determined residue blocks.

## Attempt 16: Rate-half downstream premise audit

Date: 2026-07-05

Node:
`rate_half_band_closure`, with attention to downstream consumers
`adjacency_closing` and `list_adjacency_closing`.

Actual open obligation attacked:
the premise `A` consumed downstream is not the arithmetic replay itself. The
downstream closing nodes need a real certificate that covers the rate-`1/2`
band. The previously proposed concrete premises were:

- AQB averaged quotient-box gain at `sigma*`; and
- the dihedral/Chebyshev fixed-point sibling window certificate.

The task is to determine whether either premise is true, or whether the node is
still only bracket-grade/new-mechanism.

Scripts and local files:
- `experiments/falsification_pruning/rate_half_guardrail_replay.py`
- `nodes/aqb_coupled_family_entropy_manifest_payload/refutation.md`
- `nodes/dihedral_sibling_window_certificate/proof.md`

Replay command:

```bash
python3 experiments/falsification_pruning/rate_half_guardrail_replay.py
```

Result JSON:
`experiments/falsification_pruning/results/rate_half_guardrail_replay.json`

Wall time:
Local wall `0.06s`, RSS `17336 KB`. No Modal was used.

Main observations:
- Floor-depth route at `Q=256` reaches `2^33 = 8,589,934,592`.
- `sigma* = 8,592,912,738`, so the arithmetic gap is `2,978,146` grid radii.
- The floor closes only below threshold
  `log2(q) = 255.89999028758754`; the open slice has width about
  `0.1000097124` bits near the top of the admissible field range.
- AQB deficit arithmetic is tight but only quantitative:
  required gain `429,645,546.773...` bits, claimed `429,645,547`, margin
  `0.226592...` bits.
- The AQB premise is structurally refuted in
  `aqb_coupled_family_entropy_manifest_payload/refutation.md`: the family
  average is a convex combination of single-box counts, so box-sharing gain is
  cancelled by the averaging normalization unless a separate heavy-fiber
  theorem is supplied.
- The dihedral sibling premise is refuted in
  `dihedral_sibling_window_certificate/proof.md`: the advertised packet size
  is not the Chebyshev top-degree drop; the first band overflows degree by
  `2^32`, and true Dickson fibers collapse to old quotient-core scale.

Interpretation:
This is a direct premise audit. The downstream implication “if the rate-half
band is closed, then adjacency/list adjacency can consume it” is not the target.
The target premises currently available to close the band are false or
unsatisfied. Thus `rate_half_band_closure` should be treated as bracket-grade
or new-mechanism, not as an amber node waiting on a small numerical detail.
The stale local `conditional.md` still describes the refuted AQB premise, while
`dag.json` correctly records AQB and dihedral as refuted evidence.

Verdict:
`KNOWN_CONCRETE_PREMISES_REFUTED / RATE_HALF_REQUIRES_NEW_MECHANISM_OR_BRACKET_GRADE`.

No DAG edit is made in this clone. A canonical cleanup should eventually align
`nodes/rate_half_band_closure/conditional.md` with the DAG statement, replacing
the stale AQB conditional proof with the current bracket-grade/new-mechanism
premise.

## Attempt 17: Petal/PRK multi-character premise on actual split-squarefree locus

Date: 2026-07-05

Node:
`petal_squarefree_classification_ledger_payload`, as the premise provider for
downstream amber consumers including
`petal_squarefree_kernel_classification_payload` and
`petal_cofactor_chargeability`.

Actual open obligation attacked:
the premise `A` consumed downstream is not merely that abstract
multi-character residue-kernel families are large.  Attempt 14 already showed
the abstract character-block budget is too large to leave uncharged.  The live
premise is whether those multi-character families actually occur inside the
actual split-squarefree CRT-realizable locator locus, or whether the
squarefree-realizability condition excludes them before the chargeability node
needs to pay them.

Question:
Can a simple two-character coefficient support produce a split-squarefree
missed-core locator satisfying the CRT degree condition in the executable
Petal chart?

Script:
`experiments/falsification_pruning/petal_multichar_realizability_probe.py`

Replay command:

```bash
/usr/bin/time -f 'wall=%e rss_kb=%M' timeout 60 \
  python3 experiments/falsification_pruning/petal_multichar_realizability_probe.py \
    --seconds 55 \
  > /tmp/petal_multichar_realizability_probe.out
```

Result JSON:
`experiments/falsification_pruning/results/petal_multichar_realizability_probe.json`

Wall time:
Local wall `5.86s`, RSS `14328 KB`. No Modal was used because this was a
small p=127, 50k-sample, single-process premise audit.

Parameters:
`p=127`, `M=ell=3`, `t=6`, `d=(t-1)M-1=14`, `c=11`,
`seed=7205`, `random_samples=50000`, active coefficient residues
`{0,M-1}`.

Main observations:
- Exhaustive narrow family `X^d + a X^(d-M) + b`:
  `9` split-squarefree rows were found, but `0` CRT-realizable hits in the
  tested petal/scalar charts.
- Random two-character family on active degrees
  `{0,2,3,5,6,8,9,11,12,14}`:
  `50000` rows evaluated, `16` split-squarefree rows found, and `0`
  CRT-realizable hits.
- Five split examples without CRT hits were retained for replay.  The first
  was the binomial support `[0,14]`, which split completely but failed all
  tested CRT charts.

Interpretation:
This is a premise audit, not a proof.  It does not repair the abstract PRK
budget problem: uncharged multi-character families are still too large in the
model.  It also does not refute the Pro-style cofactor obstruction by itself,
because that obstruction may live before or outside this particular
split-locator realization.  What it does show is that, in the tested executable
actual-locus chart, the obvious two-character obstruction families do not
automatically produce squarefree CRT-realizable locators.

Verdict:
`NO_SPLIT_MULTICHAR_CRT_HIT_IN_TESTED_CHARTS / ACTUAL_LOCUS_EXCLUSION_REMAINS_PLAUSIBLE_BUT_UNPROVED`.

No deletion, DAG status change, or premise promotion is made.  The stable
frontier remains the squarefree classification ledger: either explicitly pay a
parameterized multi-character family or prove that the actual
squarefree-realizable locator locus excludes the modeled bulk.

## Attempt 18: E22 all-tail pricing premise across layouts/scalars

Date: 2026-07-05

Node:
`e22_challenger_staircase_pricing`, as the all-tail pricing route needed by
the downstream amber chain under `e22_common_tail_invariance_payload` and
`e22_cofactor_common_tail_kernel_invariance`.

Actual open obligation attacked:
Attempts 7 and 13 showed that the literal common-tail premise can be satisfied
vacuously by deleting all touched points into the tail.  The premise `A`
actually needed downstream is therefore stronger: all-tail certificates must
still be selected and paid by the dyadic minimal-scale staircase machinery,
with no omitted class and no unaccounted multiplicity/injectivity defect.

Question:
Under alternate sunflower layouts and scalar choices, do all-tail mixed/full
petal challengers fall outside the selected pricing column, or do several
structured codewords collapse to the same selected representative in a way that
would require an explicit multiplicity convention?

Script:
`experiments/falsification_pruning/e22_all_tail_mode_sweep.py`

Replay commands:

```bash
/usr/bin/time -f 'wall=%e rss_kb=%M' timeout 60 \
  env PYTHONDONTWRITEBYTECODE=1 \
  python3 experiments/falsification_pruning/e22_all_tail_mode_sweep.py \
    --seconds 55 \
  > /tmp/e22_all_tail_mode_sweep.out

/usr/bin/time -f 'wall=%e rss_kb=%M' timeout 60 \
  env PYTHONDONTWRITEBYTECODE=1 \
  python3 experiments/falsification_pruning/e22_all_tail_mode_sweep.py \
    --seconds 55 \
    --row 32,2,2 \
    --layout shuffle_17 \
    --scalar-mode geometric \
    --output experiments/falsification_pruning/results/e22_all_tail_mode_sweep_missing.json \
  > /tmp/e22_all_tail_mode_sweep_missing.out
```

Result JSONs:
- `experiments/falsification_pruning/results/e22_all_tail_mode_sweep.json`
- `experiments/falsification_pruning/results/e22_all_tail_mode_sweep_missing.json`

Wall time:
The main sweep stopped by its internal deadline at local wall `55.26s`, RSS
`18696 KB`, after `71/72` cells.  The single missed cell completed separately
in local wall `0.23s`, RSS `15048 KB`.  No Modal was used.

Scope:
Rows
`(16,2,1)`, `(16,4,1)`, `(16,8,1)`, `(16,2,2)`, `(16,4,2)`,
`(16,8,2)`, `(32,2,1)`, `(32,4,1)`, `(32,2,2)`;
layouts `cyclic_step_1`, `cyclic_step_3`, `cyclic_step_5`, `shuffle_17`;
scalar modes `linear`, `geometric`.

Aggregate observations over all `72` cells:
- Structured mixed/full-petal challengers: `8386`.
- Missing selected representatives: `0`.
- Tail-only selected representatives: `8174`.
- Representatives with full fibers: `212`.
- Selected-representative collisions: `34`, with polynomial excess `37`.
- Support collisions match the representative collisions: `34`, with
  polynomial excess `37`.
- Collisions are concentrated in small rows:
  `(16,8,1)` for every tested layout/scalar mode, and one `(32,4,1)` row
  for `cyclic_step_3|linear`.

Interpretation:
This is a premise-first audit.  It did not falsify the coverage part of the
all-tail pricing premise: every tested structured all-tail challenger had a
selected dyadic representative.  It did, however, reinforce that the live
premise is multiplicity/injectivity, not mere coverage.  The repeated small-row
collisions are compatible with a correct pricing column only if the proved
cross-scale/support multiplicity convention is exactly the one consumed by the
staircase arithmetic.

Verdict:
`ALL_TAIL_COVERAGE_RESISTS_ACROSS_MODES / MULTIPLICITY_PREMISE_REMAINS_LOAD_BEARING`.

No deletion or DAG status change is made.  The E22 frontier remains an explicit
all-tail pricing/multiplicity theorem or a strengthened nonvacuous retained
fiber premise with separate all-tail handling.

## Attempt 19: SOV Bohr-gate threshold refinement

Date: 2026-07-05

Node:
`sov_gridsum_residual`, with attention to the downstream amber consumer
`sov_affine_piece_partition_payload`.

Actual open obligation attacked:
the premise `A` consumed downstream is not just that small value-set cells are
detectable by a large additive power sum.  The premise needed for the partition
is that the detected Bohr/large-power-sum exceptional class is narrow enough to
be paid, or else internally routed back to Lane-1 cancellation.  A broad gate
that accepts near-random diluted cells would make the paid class far too large.

Question:
Near the transition from interval-like to random-like cells, what Bohr
threshold still admits diluted interval families whose sampled h-sum
distribution is nearly uniform, and how large is the naive family mass?

Script:
`experiments/falsification_pruning/sov_modal_bohr_dilution_probe.py`

Replay command:

```bash
/usr/bin/time -f 'wall=%e rss_kb=%M' timeout 60 \
  ~/.venvs/modal-client/bin/python \
  experiments/falsification_pruning/sov_modal_bohr_dilution_probe.py \
    --seconds 50 \
    --betas 0.97,0.95,0.93,0.91,0.90,0.89,0.87,0.85 \
    --thresholds 0.88,0.90,0.92,0.94,0.96 \
    --cells-per-beta 32 \
    --sum-samples 8000 \
    --max-frequency 24 \
    --seed 7206 \
    --output experiments/falsification_pruning/results/sov_modal_bohr_dilution_refined.json \
  > /tmp/sov_modal_bohr_dilution_refined.out
```

Modal app:
`rs-mca-sov-bohr-dilution-20260705`

Wall time:
Local wall `29.31s`, RSS `48192 KB`; remote elapsed `24.19s`.

Parameters:
`p=65537`, `m=1024`, `h=21`, `32` cells per beta, `8000`
sampled h-sums per cell, frequencies `1..24`.

Main observations:
- Pure interval baseline: frequency-1 ratio `0.999598`, no-wrap value-set
  fraction `0.321406`.
- `beta=0.93`: median max small-frequency ratio `0.933014`, median
  collision ratio vs uniform `1.4821`, naive locator-density log2 `1050.78`.
- `beta=0.91`: median max ratio `0.913596`, median collision ratio
  `1.1920`, naive locator-density log2 `1313.38`.
- `beta=0.90`: median max ratio `0.902398`, median collision ratio
  `1.1003`, naive locator-density log2 `1439.57`.
- `beta=0.89`: median max ratio `0.893657`, median collision ratio
  `1.0673`, naive locator-density log2 `1574.95`.
- `beta=0.87` and below no longer pass the tested `0.88` threshold, and
  sampled collisions are essentially uniform.

Interpretation:
This directly attacks the downstream premise.  A Bohr gate at threshold
`0.90` is too broad as a paid class: it accepts diluted interval families with
near-uniform sampled h-sum behavior and enormous naive family mass.  The SOV
node is not deleted, because this does not refute the Lane-1 mechanism and does
not prove that no tighter paid class exists.  It does force the premise to be
one of:

- a near-pure Bohr/large-power-sum class with a much tighter pricing theorem;
- a mixed gate that routes diluted threshold-passers back into Lane-1; or
- an explicit parameterized paid family for diluted Bohr cells.

Verdict:
`BROAD_BOHR_GATE_OVERINCLUSION_CONFIRMED / TIGHT_PAID_GATE_OR_INTERNAL_LANE1_FALLBACK_REQUIRED`.

No DAG edit is made.  The stable SOV frontier remains the paid
Bohr/large-power-sum certificate, but a loose Fourier-threshold premise should
be treated as false for downstream use.

## Attempt 20: M720 suggested official-manifest slice extension

Date: 2026-07-05

Node:
`m720_official_norm_gate_case_manifest_payload`, the premise provider for the
downstream M720 norm-gate amber chain.

Actual open obligation attacked:
the downstream implication consumes an actual complete official norm-gate
manifest.  More slice evidence is not itself the premise, but a non-toral slice
witness would falsify the manifest strategy, and additional no-witness slices
measure how far the worktree remains from a real manifest certificate.

Question:
For the next official rows suggested by the manifest-gap audit, does a bounded
MITM slice find an unpaid non-toral anchored active-core witness?

Scripts:
- `experiments/falsification_pruning/m720_manifest_gap_audit.py`
- `experiments/falsification_pruning/m720_modal_slice_probe.py`

Replay commands:

```bash
python3 experiments/falsification_pruning/m720_manifest_gap_audit.py \
  --result experiments/falsification_pruning/results/m720_modal_slice_probe.json \
  --result experiments/falsification_pruning/results/m720_modal_slice_probe_h8_10.json \
  --result experiments/falsification_pruning/results/m720_modal_slice_probe_n1024_h7_9.json \
  --output experiments/falsification_pruning/results/m720_manifest_gap_audit_all_slices.json

/usr/bin/time -f 'wall=%e rss_kb=%M' timeout 60 \
  ~/.venvs/modal-client/bin/python \
  experiments/falsification_pruning/m720_modal_slice_probe.py \
    --seconds 50 \
    --count-ceiling 6000000 \
    --config 64,8,2 \
    --config 64,8,3 \
    --config 256,8,3 \
    --config 64,9,2 \
    --config 64,9,3 \
    --config 256,9,3 \
    --output experiments/falsification_pruning/results/m720_modal_slice_probe_suggested_next.json \
  > /tmp/m720_modal_slice_probe_suggested_next.out

python3 experiments/falsification_pruning/m720_manifest_gap_audit.py \
  --result experiments/falsification_pruning/results/m720_modal_slice_probe.json \
  --result experiments/falsification_pruning/results/m720_modal_slice_probe_h8_10.json \
  --result experiments/falsification_pruning/results/m720_modal_slice_probe_n1024_h7_9.json \
  --result experiments/falsification_pruning/results/m720_modal_slice_probe_suggested_next.json \
  --output experiments/falsification_pruning/results/m720_manifest_gap_audit_all_slices_plus_suggested.json
```

Modal app:
`rs-mca-m720-slice-probe-20260705`

Wall time:
Local wall `52.98s`, RSS `48008 KB`; remote elapsed `48.21s`.

Main observations:
- Pre-run audit with all existing slice files:
  `136` official rows, `6` complete-under-ceiling, `2` over-ceiling algebraic,
  `17` slice-probed with no nontoral witness, `0` with nontoral witness,
  `111` not slice-probed.
- New suggested run requested six configs but processed two before the time
  budget:
  - `(n=64,h=8,q_exp=2)`: `p=4289`, `W=29`, `1,184,040` hash subsets,
    `3,108,105` probe subsets, `0` anchored toral, `0` anchored nontoral,
    not complete because `W<n`, not aborted.
  - `(n=64,h=8,q_exp=3)`: `p=262337`, `W=29`, aborted during hash table
    construction after `557,056` hash subsets, `0` probes, `0` nontoral.
- Post-run audit:
  `19` slice-probed no-nontoral rows, `0` slice-probed with nontoral rows,
  `109` not slice-probed.

Interpretation:
No falsifying non-toral slice witness was found.  The result is still a
premise failure for downstream use: the official complete manifest does not
exist in this worktree, and slice evidence covers only a small fraction of the
official rows.  The correct stable frontier remains a complete official
manifest or a uniform theorem; additional bounded slices are evidence, not a
certificate.

Verdict:
`NO_NONTORAL_SUGGESTED_SLICE_WITNESS / OFFICIAL_MANIFEST_PREMISE_STILL_UNSATISFIED`.

No DAG edit is made.

## Attempt 21: Petal/PRK multi-character actual-locus parameter sweep

Date: 2026-07-05

Node:
`petal_squarefree_classification_ledger_payload`, as the premise provider for
`petal_squarefree_kernel_classification_payload` and
`petal_cofactor_chargeability`.

Actual open obligation attacked:
the premise `A` consumed downstream is that after the old PRK absolute-rank
route is repaired, the growing multi-character cofactor directions are either
explicitly paid or absent/bounded on the actual split-squarefree
CRT-realizable locator locus.  This attack looks for actual-locus witnesses,
then separates obvious charged-like binomial/coset locators from unclassified
multi-character candidates.

Question:
Across several small in-regime rows and many sampled petal/scalar charts, do
two-character coefficient supports produce an unclassified split-squarefree
CRT-realizable locator?

Script:
`experiments/falsification_pruning/petal_multichar_modal_sweep.py`

Replay commands:

```bash
/usr/bin/time -f 'wall=%e rss_kb=%M' timeout 60 \
  ~/.venvs/modal-client/bin/python \
  experiments/falsification_pruning/petal_multichar_modal_sweep.py \
    --seconds 50 \
    --output experiments/falsification_pruning/results/petal_multichar_modal_sweep_classified.json \
  > /tmp/petal_multichar_modal_sweep_classified.out

/usr/bin/time -f 'wall=%e rss_kb=%M' timeout 60 \
  ~/.venvs/modal-client/bin/python \
  experiments/falsification_pruning/petal_multichar_modal_sweep.py \
    --seconds 50 \
    --config 101,5,5 \
    --random-samples-per-config 20000 \
    --chart-samples 64 \
    --random-scalar-modes 2 \
    --seed 7206 \
    --output experiments/falsification_pruning/results/petal_multichar_modal_sweep_final_row.json \
  > /tmp/petal_multichar_modal_sweep_final_row.out
```

Modal app:
`rs-mca-petal-multichar-sweep-20260705`

Wall time:
Main classified sweep: local wall `54.47s`, RSS `48756 KB`, remote elapsed
`49.00s`.  Final row completion: local wall `11.65s`, RSS `48764 KB`, remote
elapsed `5.83s`.

Scope:
Rows `(p,M,t)`:
`(127,3,5)`, `(127,3,6)`, `(127,3,7)`, `(97,4,5)`,
`(193,4,5)`, `(101,5,5)`.  For each row the sweep tests the narrow family
`X^d + aX^(d-M)+b`, random active coefficient degrees in residues `{0,M-1}`,
`64` sampled disjoint petal charts, and `5` scalar modes
(`linear`, two geometric modes, two random modes).

Main observations:
- Total CRT-realizable hits found: `1`.
- Charged-like CRT hits: `1`.
- Unclassified CRT hits: `0`.
- The single hit occurs at `(p=127,M=3,t=6,d=14,c=11)` in the narrow family:
  `X^14 + 105`, support `[0,14]`, roots
  `[3,6,12,24,31,48,62,65,79,96,103,115,121,124]`.
- Independent local replay verified root count `14`, roots disjoint from the
  chosen petals, and CRT degree `14 <= d` for scalar row
  `[116,120,35,50,112,8]`.
- The hit is classified as `binomial_coset_locator`, because support `[0,d]`
  is an obvious quotient/coset-style paid shape, not the unclassified
  multi-character bulk that would falsify the repair premise.
- Split rows without unclassified CRT hits:
  `(127,3,6)` had `9` narrow split rows and `9` random split rows; all
  non-hit or charged-like.  The other completed rows had no split rows in the
  tested families.
- The main sweep reached the final `(101,5,5)` row near the deadline; that row
  was rerun separately and completed with `0` split rows and `0` CRT hits.

Interpretation:
This strengthens Attempt 17.  The actual locus is not empty: a binomial/coset
locator can satisfy the CRT degree condition.  But the only actual-locus hit
found is already in a paid-looking quotient/coset class.  No unclassified
two-character CRT-realizable family was found in the tested parameter sweep,
so this did not falsify the current salvage premise.  It does sharpen the
ledger requirement: the classification proof must explicitly route binomial
coset locators to the paid ledger and then prove that the remaining
multi-character bulk is paid or excluded.

Verdict:
`ONLY_CHARGED_LIKE_SPLIT_MULTICHAR_CRT_HITS / NO_UNCLASSIFIED_MULTICHAR_ACTUAL_LOCUS_WITNESS_FOUND`.

No DAG edit is made.  `petal_squarefree_classification_ledger_payload` remains
the stable frontier for the Petal/PRK chain.

## Attempt 22: Petal/PRK deep split-row stress at `(p=127,M=3,t=6)`

Date: 2026-07-05

Node:
`petal_squarefree_classification_ledger_payload`, again as the premise provider
for the downstream Petal/PRK amber chain.

Actual open obligation attacked:
Attempt 21 showed that the row `(p=127,M=3,t=6,d=14,c=11)` is the only tested
row that naturally produces split two-character examples.  This follow-up
concentrates the search budget there and asks whether the split examples hide
an unclassified CRT-realizable multi-character witness.

Question:
If the random two-character sample on `(127,3,6)` is enlarged by an order of
magnitude, do any split rows satisfy the CRT degree condition in the sampled
petal/scalar charts?

Script:
`experiments/falsification_pruning/petal_multichar_modal_sweep.py`

Replay command:

```bash
/usr/bin/time -f 'wall=%e rss_kb=%M' timeout 60 \
  ~/.venvs/modal-client/bin/python \
  experiments/falsification_pruning/petal_multichar_modal_sweep.py \
    --seconds 50 \
    --config 127,3,6 \
    --random-samples-per-config 250000 \
    --chart-samples 64 \
    --random-scalar-modes 2 \
    --seed 7207 \
    --output experiments/falsification_pruning/results/petal_multichar_modal_sweep_p127_m3_t6_deep.json \
  > /tmp/petal_multichar_modal_sweep_p127_m3_t6_deep.out
```

Modal app:
`rs-mca-petal-multichar-sweep-20260705`

Wall time:
Local wall `55.07s`, RSS `48760 KB`; remote elapsed `49.06s`.

Main observations:
- Narrow family: `16002` rows evaluated, `9` split rows, `0` CRT hits.
- Random active-residue family: `245441 / 250000` rows evaluated before the
  deadline, `77` split rows, `0` CRT hits.
- Total CRT hits: `0`; charged-like hits: `0`; unclassified hits: `0`.
- The retained split-without-CRT examples again include binomial/coset support
  `[0,14]`, but under this seed's scalar/chart sample they did not satisfy the
  CRT degree condition.

Interpretation:
This does not prove actual-locus exclusion, but it materially strengthens the
negative evidence on the only row where split two-character examples are
common enough to stress.  The earlier Attempt 21 binomial/coset CRT hit is
real but paid-looking and scalar/chart-sensitive.  The dangerous unclassified
multi-character bulk still did not appear.

Verdict:
`DEEP_ROW_NO_UNCLASSIFIED_MULTICHAR_CRT_HIT / ACTUAL_LOCUS_EXCLUSION_STILL_RESISTS`.

No DAG edit is made.

## Attempt 23: SOV near-pure Bohr paid-mass sign scan

Date: 2026-07-05

Node:
`sov_gridsum_residual`, with attention to the downstream premise used by
`sov_affine_piece_partition_payload`.

Actual open obligation attacked:
the SOV downstream chain cannot merely assume that a high additive
large-power-sum threshold defines a payable exceptional class.  Attempt 19
showed that loose gates around `0.90` over-include near-uniform diluted
families.  This attempt attacks the opposite edge: even very near-pure Bohr
families may be too numerous to pay if the gate allows a handful of random
substitutions.

Question:
For the interval cell of size `m=1024`, how many random substitutions are
needed before the naive cell-locator mass becomes positive, and what
large-power-sum thresholds would still accept those families?

Script:
`experiments/falsification_pruning/sov_modal_bohr_dilution_probe.py`

Replay command:

```bash
/usr/bin/time -f 'wall=%e rss_kb=%M' timeout 60 \
  ~/.venvs/modal-client/bin/python \
  experiments/falsification_pruning/sov_modal_bohr_dilution_probe.py \
    --seconds 50 \
    --betas 1.000000000000,0.999023437500,0.998046875000,0.996093750000,0.994140625000,0.992187500000,0.990234375000,0.988281250000,0.984375000000,0.980468750000 \
    --thresholds 0.98,0.985,0.99,0.995 \
    --cells-per-beta 32 \
    --sum-samples 8000 \
    --max-frequency 24 \
    --seed 7208 \
    --output experiments/falsification_pruning/results/sov_modal_bohr_nearpure_scan.json \
  > /tmp/sov_modal_bohr_nearpure_scan.out
```

Modal app:
`rs-mca-sov-bohr-dilution-20260705`

Wall time:
Local wall `30.62s`, RSS `48448 KB`; remote elapsed `25.34s`.

Main observations:
- `0` substitutions: median max small-frequency ratio `0.999598`,
  median collision ratio vs uniform `8.3613`, naive locator-density log2
  `-126.293`.
- `1` substitution: ratio `0.998661`, collision ratio `8.1396`,
  density log2 `-100.316`.
- `2` substitutions: ratio `0.997878`, collision ratio `7.9114`,
  density log2 `-76.340`.
- `4` substitutions: ratio `0.995862`, collision ratio `7.4455`,
  density log2 `-31.563`.
- `6` substitutions: ratio `0.994069`, collision ratio `6.9891`,
  density log2 `+10.565`.  This is the first tested positive-mass row.
- `8` substitutions: ratio `0.991904`, collision ratio `6.5786`,
  density log2 `+50.886`.
- `20` substitutions: ratio `0.980708`, collision ratio `4.5986`,
  density log2 `+270.824`.

Interpretation:
This is a premise falsification for threshold-only paid classes.  A threshold
as high as `0.99` still admits 6- and 8-substitution diluted intervals, whose
naive locator mass is already positive.  A threshold near `0.995` cuts before
the first tested positive-mass row in this model, but that is a very tight
near-pure requirement and still needs a real structural/paid proof, not just a
Fourier threshold.

This does not refute SOV itself.  The sampled h-sum distribution remains
strongly nonuniform in the near-pure rows, so these are not Lane-1 fallback
candidates in the same way as the `beta=0.90` rows.  Instead, they show that
the paid Bohr premise must be extremely tight or parameterized by the number of
off-interval substitutions; a broad high-threshold gate is still false as a
payable class.

Verdict:
`NEAR_PURE_BOHR_MASS_SIGN_FLIPS_AT_6_SUBSTITUTIONS / THRESHOLD_ONLY_PAID_GATE_REQUIRES_~0_995_OR_STRUCTURE`.

No DAG edit is made.
