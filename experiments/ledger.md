# Amber stress-test ledger

Date: 2026-07-06.
Worktree: `/home/u2470931/smooth-read-solomin/prize-amber-stress-20260706`.
Branch: `codex-amber-stress-20260706`.
Base: `prize` master `64ae80a`.

Goal: stress-test amber nodes with numerical and algebraic falsification
attempts.  For implication nodes, attack both the premise package and the
implication where feasible.  For direct assertions, attack the assertion.
Every experiment is capped at 60 seconds and must leave checkpoint output.

Initial current-state facts:

- `dag.json` has 29 `CONDITIONAL` nodes.
- `tools/verify_prize_dag.py` still reports pre-existing reachability failures
  in archived/cut branches.
- The same validator flags three amber nodes with no `statement` field:
  `a_regular_collapse`, `free_pool_ladder`, and `m_le3_route`.
- Modal is not installed in this environment (`modal: command not found`).
  The rate-half Modal scripts request `timeout=1800`, so this pass uses a local
  60-second-safe equivalent for the same arithmetic.

## Experiment batch 1: algebraic toy attacks

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/stress_harness.py --time-limit 55
```

Checkpoint:

```text
experiments/amber_stress/results.json
```

Targets:

- `tr_perleaf_list_ident`: test quotient/lift exact-list dictionary on small
  finite fields, plus a non-stable negative control.
- `x4_exactlist_staircase_split` / `moment_trade_staircase`: recompute the
  primitive moment-null witness from the statement and test that it is not
  quotient/dihedral symmetry.
- `worst_word_planted` / `worst_word_challenger_pricing`: rerun the local E22
  challenger gate and check for unclassified third-class challengers in the toy
  cell.

Result:

- PASS in `6.15s`.
- Checkpoint: `experiments/amber_stress/results.json`.

Findings:

- `tr_perleaf_list_ident`: resisted direct falsification on small fields
  `F_97, n=12, M=3` and `F_193, n=16, M=4`.  The harness checked `886,115`
  lifted polynomial agreement comparisons and found exact quotient/upstairs
  agreement scaling in every case.  Positive controls had nonempty list counts.
- TR negative control: breaking one point in a fiber was detected in all `10`
  non-stable controls.  This is important: the dictionary is not being tested
  vacuously; stability is a load-bearing hypothesis.
- `moment_trade_staircase` / `x4_exactlist_staircase_split`: recomputed the
  statement's primitive witness
  `{11^e : e in {0,1,2,4,16,45,50,60}}` in `mu_64(F_193)`.  Power sums vanish
  for `r=1,2,3`, the `r=4` sum is `18`, the top three subleading locator
  coefficients are zero, and the only rotation stabilizer is identity with no
  reflection stabilizer.  This supports the claim that the moment column is a
  real non-quotient/non-dihedral mechanism.
- `worst_word_planted` / `worst_word_challenger_pricing`: reproduced the E15
  local challenger.  At `n=16, sigma=1`, `k=2,4,8` beat the planted count via
  mixed/full-petal challengers; `UNCLASSIFIED=0` in all gate cells.  Sigma-2
  controls had no challengers.

Verdict impact:

- No falsifier found.
- Confidence increased for `tr_perleaf_list_ident`, `x4`'s moment-column
  inclusion, and the two-class E22 challenger repair.
- The TR stress confirms that any future proof must keep the stable-support
  hypothesis explicit; dropping it is false by the negative control.

## Experiment batch 2: targeted existing verifiers

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Checkpoint:

```text
experiments/amber_stress/verifier_results.json
```

Result:

- PASS in `26.03s` total.
- Every selected command used a `60s` per-command cap; the slowest was
  `xr_ledger_qpower` at about `23.2s`.

Passed checks and covered amber surfaces:

- `list_adjacency_closing` / `list_grand`: list corridor widths and ledger
  arithmetic passed; clean-rate margins remain positive.
- `f1_classification` / `ext_lift`: minimal-field descent verifier passed,
  including concrete finite-field trichotomy partitions.
- `r2_clean_rates` / `xr_clean_residual_any_gate`: XR radius arithmetic,
  q-power ledger, and exponent reconciliation passed.
- `worst_word_planted` / `list_planted_arithmetic`: E22 two-class exhaustion
  sanity check and fixed-scale staircase injectivity passed.
- `strip`: `gap2_seam` verifier passed.
- `imgfib` / `list_safe`: `petal_fixed_excess` verifier passed, including
  top-defect controls.
- `x4_exactlist_staircase_split` / `tr_perleaf_list_ident`: dyadic profile
  evaluation passed.
- `mca_safe`: bounded-scale census verifier passed.
- `adjacency_closing` / `list_adjacency_closing`: local rate-half floor-depth
  and q-threshold arithmetic passed.  At `log2 q=256`, max floor depth is
  `2^33 = 8,589,934,592`, leaving gap `2,978,146` to `sigma*`.  Threshold
  `log2 q ~= 255.89999`, so the open slice is about `0.10001` bits.

Verdict impact:

- No falsifier found in this batch.
- The clean-rate list corridor, F1 trichotomy bookkeeping, XR arithmetic, E22
  two-class repair, strip seam, fixed-excess petal partial, dyadic profile, and
  bounded-scale census all resisted replay.
- Rate-half remains a genuine red premise: the local arithmetic confirms the
  residual top-slice gap instead of closing it.

## Current unresolved amber-stress items

- `a_regular_collapse`, `free_pool_ladder`, and `m_le3_route` are still
  unauditable as ambers because `dag.json` marks them `CONDITIONAL` but does
  not provide a statement field.
- This pass has not yet built fresh falsification harnesses for every one of
  the 29 amber nodes; it establishes a reusable checkpointed framework and
  covers the highest-leverage algebraic/numerical surfaces first.

## Premise weakening batch 1

Target:

- `list_grand`: amber implication from lower list-side predicates to the list
  grand challenge.
- `list_adjacency_closing`: amber implication from list crossing localization
  and priced columns to adjacent list crossing.
- `r2_clean_rates`: clean-rate R2 assembly at the compiled
  `R_post <= 16 n^3` target.

Weakening applied:

- Demoted `list_safe -> list_grand` and `list_unsafe -> list_grand` from
  `req` to `ev` in `dag.json`.
- Rewrote `nodes/list_grand/conditional.md` so the logical predicate set is
  exactly `s0_zero_open`, `mixed_radix_frontier`, and
  `list_adjacency_closing`.
- Demoted `worst_word_planted -> list_adjacency_closing` from `req` to `ev`.
  The transitive logical dependency remains through `list_planted_arithmetic`.
- Demoted `xr_globalness_from_ledger -> r2_clean_rates`,
  `xr_small_set_engine -> r2_clean_rates`, and
  `xr_radius_arithmetic -> r2_clean_rates` from `req` to `ev`.
  The sole logical premise of `r2_clean_rates` is now
  `xr_clean_residual_any_gate`.

Reason:

- The conclusion of `list_adjacency_closing` already contains the adjacent
  crossing inequality
  `sup_U |Lambda(U, delta - 1)| > eps*|F| >= sup_U |Lambda(U, delta)|`.
  Therefore the top-layer grand assembly does not need independent safe/unsafe
  premises.  The former children remain evidence/support edges for the
  lower-level route and for diagnostics.
- The child `list_planted_arithmetic` already consumes `worst_word_planted` and
  packages the exact planted-plus-challenger arithmetic.  A second direct
  `worst_word_planted` premise on `list_adjacency_closing` was redundant.
- The active `r2_clean_rates` statement is the compiled clean-rate residual
  bound `R_post(u,v; A) <= 16 n^3`.  The child
  `xr_clean_residual_any_gate` already includes the budget audit converting the
  safe-side obligation to that exact inequality, so the older KLLM/globalness
  route inputs are no longer direct premises of this assembly node.

Verdict impact:

- This is a genuine weakening of an amber premise package, not a proof of a red
  node.  It reduces the logical dependency surface of `list_grand` and
  `list_adjacency_closing` while preserving the same conclusions.
- For `r2_clean_rates`, this is also a route simplification, not a closure:
  `xr_clean_residual_any_gate` still needs a budget-compatible smallcore bound
  (`<= 16 n^3` scale), so the open critical premise is unchanged.

## Red-premise falsification cleanup: rate-half band

Target:

- `rate_half_band_closure`, consumed by `adjacency_closing`,
  `list_adjacency_closing`, and `mca_safe`.

Finding:

- The node folder was internally inconsistent.  `statement.md` and
  `P6_RATEHALF_SIBLING.md` say the AQB route is refuted and the band is open,
  but `conditional.md` still claimed AQB-I closes the band and `proof.md`
  claimed the P6 dihedral-sibling route gives a concrete covering mechanism.
- The repo already contains the refutation:
  `nodes/dihedral_sibling_window_certificate/proof.md` proves the P6 route
  fails the degree audit.  The proposed packet size is not a Chebyshev
  top-degree drop, true Dickson fibers are too small in the first band, and the
  endpoint fixed-point sibling also overflows.

Edit applied:

- Replaced `nodes/rate_half_band_closure/conditional.md` with the current open
  TARGET status and explicit notes that both AQB-I and P6 dihedral-sibling are
  refuted routes.
- Replaced `nodes/rate_half_band_closure/proof.md` with a proof-status notice
  rather than a stale positive proof.
- Re-posed `rate_half_band_closure` as the strong full-determination premise:
  it means "cover the band by a new priced mechanism."  A bracket-grade
  obstruction remains valuable but is a separate partial result, not a proof of
  this node as consumed by the full adjacency/safe parents.

Verdict impact:

- This does not close or repair the red node.  It prevents downstream amber
  consumers from accidentally reading a known-false route as a conditional
  proof of the rate-half premise, and prevents a bracket-grade partial from
  satisfying a full-determination premise by disjunction.

## Scope repair: aperiodic zero at crossing

Target:

- `aperiodic_zero_at_crossing`, consumed by `adjacency_closing`.

Finding:

- The node's file-level statement discussed all table rows, including the
  rate-`1/2` thin point, but its live R2 premise is `r2_clean_rates`, which is
  explicitly scoped to rates `1/4`, `1/8`, and `1/16`.
- This is a producer/consumer scope mismatch: the clean-rate R2 input cannot
  prove the rate-`1/2` margin statement.

Edit applied:

- Rewrote `nodes/aperiodic_zero_at_crossing/conditional.md` as a clean-rate
  proof packet from `fm1` and `r2_clean_rates`.
- Added the same rate-scope note to `statement.md`.
- Retitled the DAG node to "Clean-rate integrality: R2 + tiny FM pin the
  aperiodic zero threshold".
- Updated `adjacency_closing/conditional.md` so the rate-`1/2` thin point is
  explicitly supplied by `rate_half_band_closure`, not by the clean-rate
  aperiodic node.

Verdict impact:

- This weakens the assertion to the part actually supported by its premises.
  The full adjacency parent still has a route to all admissible rows only if the
  strong rate-half premise is eventually proved.

## Verification rerun after repairs

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Result:

- PASS in about `22.05s` total.
- All selected existing verifiers still pass after the premise weakenings and
  rate-scope repairs.
- The local rate-half arithmetic still reports `max_depth = 2^33` at
  `log2 q = 256`, `sigma* = 8,592,912,738`, and the residual gap
  `2,978,146`.  This supports the strong-rate-half repair: the old floor
  mechanism does not close the band.

## Assertion repair: strip

Target:

- `strip`, consumed by `mca_safe`.

Finding:

- The node files only said "Strip-periodic: aperiodic stratum exact" and did
  not state the object or inequality being consumed.  That made direct
  falsification ill-posed.

Edit applied:

- Rewrote `nodes/strip/statement.md` and `nodes/strip/conditional.md` as the
  exact decomposition implied by the wired premises:
  `rate-preserving quotient columns + O(poly(n) * FM)`.
- The proof now enumerates the roles of `periodic_strata`, `q_recursion`,
  `confinement`, `isotypic`, `gap1_noneq_mass`, and `gap2_seam`.
- Updated the DAG title to
  "Strip-periodic decomposition: quotient columns plus GAP-1 residual".

Verdict impact:

- This does not close a new node; it turns a terse amber into a falsifiable
  implication.  The only live pricing premise remains `gap1_noneq_mass`.

## Orphan amber auditability repair

Targets:

- `a_regular_collapse`
- `free_pool_ladder`
- `m_le3_route`

Finding:

- These three nodes were marked `CONDITIONAL` in `dag.json` but had no
  `statement` field, so the DAG checker reported them as unauditable
  implications.  They are historical/orphan routes with no current root-path
  consumers, but they still need a statement while their status is amber.

Edit applied:

- Added concise DAG statements for all three.
- Marked `a_regular_collapse` as orphan/historical in the notes; it is retained
  for the for-all-`m` boundary but is not active under the official
  per-constant-`m` reading.

Verdict impact:

- No proof status changed and no root path was altered.  This is an
  auditability repair.

## Packet alignment: x4 exact-list staircase split

Target:

- `x4_exactlist_staircase_split`

Finding:

- The DAG wires `moment_trade_staircase`, `xr_syzygy_support_lemma`, and
  `xr_scattered_syzygy_flattice` as required inputs of the x4 split, but
  `conditional.md` omitted them from the displayed hypothesis package.  The
  reduction packet listed `moment_trade_staircase` as a wired hypothesis but
  still omitted the two XR syzygy side inputs.

Edit applied:

- Added all three omitted required inputs to
  `nodes/x4_exactlist_staircase_split/conditional.md`.
- Added the two proved XR syzygy inputs to the packet's reattached side-input
  list.

Verdict impact:

- No status or edge changed.  This keeps the amber implication honest about
  the actual premise package consumed by the DAG.  The XR inputs look like real
  transported-residue dictionary support, not obviously removable cargo, so no
  weakening was applied here.

## Retraction cleanup: worst-word challenger pricing

Target:

- `worst_word_challenger_pricing`

Finding:

- `dag.json` and `frontier.md` correctly mark this critical node as `TARGET`
  after the 2026-07-05 E22 retraction, but `statement.md`,
  `conditional.md`, and `dependency_subdag.md` still described the retracted
  E22 staircase-pricing route as a live conditional proof.

Edit applied:

- Changed the file-level status in `statement.md` to `TARGET`.
- Replaced the stale conditional proof with an explicit proof-status note:
  there is no active conditional theorem, `e22_two_class_exhaustion` is
  evidence only, and the archived `e22_challenger_staircase_pricing` branch
  should not be used as a hidden premise.
- Rewrote `dependency_subdag.md` to show only the live evidence edge and the
  downstream consumers.
- Fixed the stale `worst_word_planted` statement header from `CONJECTURE` to
  the DAG's current `CONDITIONAL` status.

Verdict impact:

- This prevents a retracted premise package from contaminating downstream
  amber nodes.  The actual red obligation is unchanged: exact challenger
  pricing or a replacement exhaustion theorem is still needed.

## Verification rerun after x4/E22 cleanup

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Result:

- PASS in about `23.9s` total.
- The E22 two-class sanity check, fixed-scale staircase injectivity check, x4
  dyadic profile check, clean-rate XR arithmetic, list corridor checks, strip
  seam check, petal fixed-excess check, and rate-half local floor/threshold
  check all still pass.
- Structural validation still reports only the known archived/unreachable
  branches; no `CONDITIONAL` node is missing a DAG statement.

## Retraction cleanup: critical red proof-status files

Targets:

- `u1_pullback_dichotomy`
- `xr_smallcore_spread_count`
- `petal_growth`

Finding:

- All three are critical `TARGET` nodes in `dag.json` and each has a
  `RETRACTION_MANIFEST.md` explaining why its earlier conditional sub-frontier
  was cut from the trusted surface.
- Their local `conditional.md` files still read like active conditional
  proofs, and `u1_pullback_dichotomy` plus `xr_smallcore_spread_count` also
  had stale `CONDITIONAL` status headers in `statement.md`.

Edit applied:

- Updated `u1_pullback_dichotomy` and `xr_smallcore_spread_count` statement
  headers to `TARGET`.
- Rewrote the three `conditional.md` files as proof-status/advisory-route
  notes: the archived predicate routes remain useful attack structure, but are
  not live premises.

Verdict impact:

- No mathematical claim was strengthened and no edge changed.  This reduces
  the chance that an amber consumer treats a retracted red-node decomposition
  as a proved or conditionally proved input.

## Premise weakening batch 2: F1 extension-lift lane

Targets:

- `ext_lift`
- `f1_case_pole`
- `f1_classification`

Finding:

- `ext_lift` directly required `b_rational_lift`, `f1_case_pole`, and
  `f1_case_tower`, but its conclusion follows from `f1_classification` alone
  once that predicate is read as the priced B-rational / pole / tower
  trichotomy.  The case-ledger dependencies remain transitive through
  `f1_classification`.
- `f1_case_pole` directly required `ext_import`, while
  `f1_pole_list_threshold_location` already consumes `ext_import` and packages
  the imported extension-pole/list bridge plus the threshold location.
- `f1_classification/statement.md` still had a stale `CONJECTURE` status
  header despite the DAG marking it `CONDITIONAL`.

Edit applied:

- Demoted `b_rational_lift -> ext_lift`, `f1_case_pole -> ext_lift`, and
  `f1_case_tower -> ext_lift` from `req` to `ev`.
- Demoted `ext_import -> f1_case_pole` from `req` to `ev`.
- Rewrote the local proof text to make the weaker premise packages explicit.
- Updated the stale `f1_classification` statement header to `CONDITIONAL`.

Verdict impact:

- This is a genuine weakening of two amber premise packages.  No red node is
  closed, and the F1 lane still depends on `f1_case_pole`, hence on
  `list_adjacency_closing` through `f1_pole_list_threshold_location`.

## Experiment batch 3: GAP-1 telescope algebra

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/gap1_telescope_checks.py
```

Checkpoint:

```text
experiments/amber_stress/gap1_telescope_results.json
```

Targets:

- `gap1_product_model`
- `gap1_noneq_mass`
- `tr_joint_telescope`

Result:

- PASS in about `0.01s`.

Findings:

- Checked small cyclic domains over `F_97` and `F_193` with `n=24,32` and
  quotient kernels `M=6,8,16`.
- For active character sets `R`, the computed character-space rank matched
  `|R| * n/M`.
- The joint telescope landed in the `K_D` isotypic space with
  `D = gcd(M, r-r0)`, and the telescoped rank matched `n/D`.
- Equality held exactly for full congruence classes.  Non-full classes were
  strict containment controls, e.g. `M=8, R={1,3}` gave rank `6` or `8`
  inside telescoped ranks `12` or `16`.
- Bad-divisor negative controls fired in every case: using a too-large
  stabilizer failed containment.

Verdict impact:

- No falsifier found for the algebraic jointness premise behind
  `gap1_product_model`.
- The strict-containment controls confirm the test is sensitive to the exact
  closure convention rather than merely checking dimensions in easy equality
  cases.

## Experiment batch 4: MCA adjacent-delta self-consistency

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 tools/conjectural_mca_delta.py --self-test
```

Targets:

- `mca_grand`
- `mca_safe`
- `adjacency_closing`

Result:

- PASS in under one second.

Findings:

- Reproduced the banked `n=2^41, log2(q)=255.9` corridor table:
  `t* = 8592912739, 7014660390, 4722556392, 2943177800` for rates
  `1/2, 1/4, 1/8, 1/16`.
- The tool's adjacent check passed in all four rows: the computed `a*` is safe
  and `a* - 1` is unsafe in the conjectural bound model.

Verdict impact:

- This is only a self-consistency check of the arithmetic map, not an
  independent proof of the red premises.  It did not find an adjacent-index
  convention mismatch in the MCA assembly.

## Assembly clarification: MCA grand/safe nodes

Targets:

- `mca_grand`
- `mca_safe`

Edit applied:

- Rewrote `mca_grand/conditional.md` from ledger prose into an explicit
  predicate-node proof packet over `s0_zero_open`, `mca_safe`, `mca_unsafe`,
  `mixed_radix_frontier`, and `adjacency_closing`.
- Rewrote `mca_safe/conditional.md` to enumerate the live safe-side stratum
  predicates and to state explicitly that the rate-`1/2` top slice enters only
  through `rate_half_band_closure`.

Verdict impact:

- No edge changed.  The MCA top-layer ambers are now easier to falsify: a
  counterexample must attack one of the displayed stratum/corridor premises or
  the implication from those premises to the adjacent crossing.

## Verification rerun after F1/GAP-1/MCA batch

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Result:

- PASS in about `20.4s` total.
- The selected suite now includes the new GAP-1 telescope check and the
  conjectural MCA delta self-test in addition to the earlier list corridor,
  F1 descent, XR arithmetic, E22, strip seam, petal fixed-excess, dyadic
  profile, bounded-scale census, and rate-half local checks.
- `tools/verify_prize_dag.py` still reports the same known
  archived/unreachable branches.  It reports no missing `CONDITIONAL`
  statements, and the critical target set is unchanged.

## Experiment batch 5: SPI/Hankel slope-sieve mechanics

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 nodes/spi_exceptional_class/notes/verify_writeup.py
```

Targets:

- `hankel_slope_large_sieve`
- `spi_point_counting`

Result:

- PASS in about `0.16s`.

Findings:

- Checked `2500` random Hankel pencils over `F_17` on `mu_8`; the worst number
  of rational rank-drop slopes was `1`, below the generic rank bound `3`.
- Checked `1600` planted moving-kernel families in the `R(Z) == 0` branch; all
  had the fixed common `H`-root required for the tangent-paid branch.
- Checked `1000` `D_j` emptiness controls with an out-of-domain or boundary
  root; all were rejected.
- Checked `471` genuine moving-root slope-bound trials; all obeyed the
  degree-`8` supported-slope bound.

Verdict impact:

- No falsifier found for the closed mechanical subcases behind
  `hankel_slope_large_sieve`.
- This does not test the live red premise `diffuse_triple_shadow`; it narrows
  the stress evidence to the rank-drop/tangent/backbone mechanics that the
  amber implication claims are already paid before invoking that premise.

## Verification rerun after SPI/Hankel addition

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Result:

- PASS in about `23.9s` total.
- The selected verifier suite now has direct replay coverage for
  `hankel_slope_large_sieve` and `spi_point_counting`.
- The coverage snapshot leaves six amber nodes without a direct falsification
  harness: `a_regular_collapse`, `free_pool_ladder`, `m_le3_route`,
  `packaging`, `petal_mixed_amplification`, and `prize`.  The first three are
  orphan/evidence or low-level route nodes; `packaging` and `prize` are
  deliverable/root assemblies; `petal_mixed_amplification` is the remaining
  mathematical amber without a direct harness from this list.

## Experiment batch 6: PMA auxiliary-list toy probe

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/pma_aux_list_probe.py
```

Checkpoint:

```text
experiments/amber_stress/pma_aux_list_results.json
```

Targets:

- `petal_mixed_amplification`
- `pma_wide_residual`

Result:

- PASS in about `16.7s`.

Findings:

- Probed the recorded PMA toy scale `F_109`, `ell=3`, `d=5`, with agreement
  threshold `8`.
- Exact `M=4` Johnson-safe row: `0` auxiliary polynomials at threshold.
- Exact wide `M=6` row: `3` auxiliary polynomials, maximum agreement `8`.
- Exact wide `M=9` row: `159` auxiliary polynomials, maximum agreement `9`.
- Sampled wide `M=12` row: checked `200,000` of `1,947,792` interpolation
  subsets, finding `1,931` distinct threshold candidates and maximum agreement
  `10`.

Verdict impact:

- No super-polynomial signal or high-agreement runaway was found in this toy
  PMA setup.
- The wide rows are nonempty, as expected; the result supports the current
  statement shape that wide sub-Johnson lists are the real residual and must be
  stripped/charged rather than ignored.

## Experiment batch 7: root/packaging and orphan amber surface

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/assembly_orphan_checks.py
```

Checkpoint:

```text
experiments/amber_stress/assembly_orphan_results.json
```

Targets:

- `prize`
- `packaging`
- `a_regular_collapse`
- `free_pool_ladder`
- `m_le3_route`

Result:

- PASS in under one second.

Findings:

- `prize` has exactly the expected required package:
  `mca_grand`, `list_grand`, and `packaging`.
- `packaging` has exactly the expected required package:
  `compiler`, `harness`, `dossier_partial`, and `bridge_ledger`; the first
  three remain `TARGET`, while `bridge_ledger` is `PROVED`.
- The three orphan/evidence amber nodes do not reach `prize` through required
  edges.  Their consumers are evidence-only:
  `a_regular_collapse -> m_handling`,
  `free_pool_ladder -> unsafe_at_crossing`, and
  `m_le3_route -> m_handling`.

Verdict impact:

- This is a logical surface check rather than a mathematical proof.  It
  confirms the remaining non-numerical amber nodes are either root/deliverable
  assemblies with the expected open package or non-required historical/evidence
  routes.

## Final selected-suite rerun for this pass

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Result:

- PASS in about `37.9s` total.
- Every command in the selected suite has its own `60s` cap.  The slowest
  commands in this run were `xr_ledger_qpower` at about `18.7s` and
  `pma_aux_list_probe` at about `16.3s`.
- The coverage snapshot now reports no amber node lacking at least one direct
  verifier, algebraic/numerical harness, or logical surface check.

## Experiment batch 8: E22 extended local third-class census

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/e22_extended_local_census.py
```

Checkpoint:

```text
experiments/amber_stress/e22_extended_local_census_results.json
```

Targets:

- `worst_word_challenger_pricing`
- `worst_word_planted`
- `list_planted_arithmetic`

Result:

- PASS in about `40.4s`.
- Exact cells checked: `77`.
- Agreement subsets checked: `1,920,836`.
- Structured-challenger cells: `36`.
- Cells with unclassified non-planted challengers: `0`.
- Deliberately skipped by local combination cap: `6` frontier cells, including
  `(n,k,sigma)=(24,8,1)`, `(32,4,2)`, `(32,8,1)`, `(48,4,1)`,
  `(64,2,2)`, and `(64,4,1)`.

Verdict impact:

- This does not close `worst_word_challenger_pricing`; it is still a top-down
  pricing/envelope theorem.
- It gives stronger falsification resistance for the premise consumed by
  `worst_word_planted` and `list_planted_arithmetic`: in the bounded exact
  sweep, all non-planted low-slack challengers remained in the mixed/full-petal
  structured classes.
- The downstream `list_planted_arithmetic` conditional was weakened: it only
  needs a rowwise certified integer envelope plus unsafe witnesses.  Exact
  two-column challenger pricing remains sufficient, but a future priceable
  third class would no longer automatically kill the arithmetic reduction.

## Amber packet cleanup: orphan/evidence conditionals

Files added:

```text
nodes/a_regular_collapse/{statement.md,conditional.md}
nodes/free_pool_ladder/{statement.md,conditional.md}
nodes/m_le3_route/{statement.md,conditional.md}
```

Reason:

- These three amber nodes had explicit `dag.json` statements and wired
  hypotheses but no node folders.
- They are not on required paths to `prize`; their consumers are evidence-only.
- Adding the packets makes the amber surface auditable without promoting the
  routes.

Coherence check:

```text
conditional coherence issues: 0
```

## Final selected-suite rerun after batch 8

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 180s python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Result:

- PASS: `19/19` selected commands.
- Sum of child wall times: about `79.8s`.
- Every child command retained its own `60s` cap.
- Slowest commands:
  - `e22_extended_local_census`: about `42.8s`.
  - `xr_ledger_qpower`: about `18.3s`.
  - `pma_aux_list_probe`: about `15.9s`.

Structural check:

- `tools/verify_prize_dag.py` still exits nonzero for the known archived
  unreachable branches.
- The critical open list is unchanged and includes
  `worst_word_challenger_pricing`, which remains a `TARGET`.

Critical orbit rebuild:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tools/build_critical_orbit.py
```

- Rebuilt `orbit/critical_dag.json`, `orbit/critical_orbit.html`, and the SVGs.
- Projected critical view: `189` nodes, `246` edges, with `7` `UNPROVED`
  mathematical nodes:
  `dli_prime_weighted_large_block_support`, `petal_growth`,
  `rate_half_band_closure`, `u1_pullback_dichotomy`,
  `u2c_giant_tnull_dichotomy`, `worst_word_challenger_pricing`, and
  `xr_smallcore_spread_count`.
- The full validator also reports the packaging artifact targets
  `compiler`, `harness`, and `dossier_partial` as root-critical open nodes.

## Experiment batch 9: petal-growth local excess scan

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/petal_excess_local_scan.py --time-limit 55
```

Checkpoint:

```text
experiments/amber_stress/petal_excess_local_scan_results.json
```

Targets:

- `imgfib`
- `petal_growth`

Result:

- PASS in about `39.5s`.
- Coset-chart configurations checked: `16`.
- Total rows checked: `76`.
- Below-top rows checked: `48`.
- Below-top Lemma-13 violations: `0`.
- Configurations with below-top ambient `dim K` growth: `8`.
- Configurations with below-top exact realizable count growth: `1`.
- Maximum exact realizable count below top: `1`.
- Maximum exact realizable count at/top beyond the top-defect band: `5005`.

Interpretation:

- This does not close `petal_growth`.
- It falsifies the old flat-kernel intuition as a route: ambient `dim K` grows
  with `c` even below top, though still within the Lemma-13 ceiling.
- The exact realizable counts stayed essentially absent below top in this local
  sweep, but grew sharply at or beyond top defect.  This supports the current
  retraction note: the live obstruction is the top-band paid-family
  classification, not the fixed-excess/below-top kernel floor.

## Selected-suite rerun after batch 9

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 220s python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Result:

- PASS: `20/20` selected commands.
- Sum of child wall times: about `122.7s`.
- Every child command retained its own `60s` cap.
- Slowest commands:
  - `e22_extended_local_census`: about `43.0s`.
  - `petal_excess_local_scan`: about `42.6s`.
  - `xr_ledger_qpower`: about `18.5s`.
  - `pma_aux_list_probe`: about `15.9s`.

## Experiment batch 10: XR small-core/light-triangle rank scan

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/xr_smallcore_triangle_scan.py --time-limit 55
```

Checkpoint:

```text
experiments/amber_stress/xr_smallcore_triangle_scan_results.json
```

Targets:

- `xr_clean_residual_any_gate`
- `xr_smallcore_spread_count`

Result:

- PASS in under `60s`.
- Finite rows checked: `3`.
- Deterministic slope tests checked: about `1.4M`
  (`1,407,204` in the selected-suite rerun).
- Rank-drop tests: `0`.
- Severe rank-drop tests: `0`.
- Profiles with no full-rank probe: `0`.

Interpretation:

- This does not close `xr_smallcore_spread_count`.
- It directly attacks the E32-style small-core/light-triangle stagnation
  surface using the archived normal-form rank test.  At the tested toy scales,
  the post-cascade small-core profiles all had full-rank witnesses under the
  deterministic slope probes.
- The node wording was aligned to the consumer: `xr_clean_residual_any_gate`
  needs the explicit `16 n^3`-compatible spread count, not a generic
  `poly(n)` statement.

## Selected-suite rerun after batch 10

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 360s python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Result:

- PASS: `21/21` selected commands.
- Sum of child wall times: about `178.1s`.
- Every child command retained its own `60s` cap.
- Slowest commands:
  - `xr_smallcore_triangle_scan`: about `55.0s`.
  - `petal_excess_local_scan`: about `43.8s`.
  - `e22_extended_local_census`: about `43.3s`.
  - `xr_ledger_qpower`: about `17.4s`.
  - `pma_aux_list_probe`: about `15.9s`.

## Experiment batch 11: diffuse triple-shadow circuit scan

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/diffuse_shadow_circuit_scan.py --time-limit 55
```

Checkpoint:

```text
experiments/amber_stress/diffuse_shadow_circuit_results.json
```

Targets:

- `diffuse_triple_shadow`
- `hankel_slope_large_sieve`

Result:

- PASS in about `13.9s`.
- Finite rows checked:
  - `F_13`, `mu_12`, `t=3`, `j=4`, `k+1=6`.
  - `F_17`, `mu_8`, `t=2`, `j=3`, `k+1=4`.
  - `F_17`, `mu_16`, `t=3`, `j=5`, `k+1=9`.
- Minimal dependent locator/slope circuits found: `11,785`.
- Tangent-core circuits: `1,094`.
- Diffuse `m >= 4` circuits: `10,691`.
- Triple-shadow violations: `0`.

Interpretation:

- This directly stress-tests the reduction surface in
  `hankel_slope_large_sieve`: a non-fresh/minimal stagnating certificate should
  have at least `k+1` triple-covered agreement positions; `m=3` such
  certificates should be tangent-core, and the non-tangent residue should
  begin at diffuse `m >= 4`.
- The small models behaved exactly that way.  Planted common-core controls
  triggered the tangent branch, random minimal `m=3` dependencies were
  tangent-core, and random non-tangent `m>=4` dependencies landed in the
  diffuse residue.
- This does not close `diffuse_triple_shadow`: it supplies falsification
  evidence for the structural reduction, not a polynomial counting theorem for
  the diffuse residue.

## Selected-suite rerun after batch 11

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 420s python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Result:

- PASS: `22/22` selected commands.
- Sum of child wall times: about `192.2s`.
- Every child command retained its own `60s` cap.
- Slowest commands:
  - `xr_smallcore_triangle_scan`: about `55.0s`.
  - `petal_excess_local_scan`: about `42.5s`.
  - `e22_extended_local_census`: about `42.4s`.
  - `xr_ledger_qpower`: about `19.1s`.
  - `pma_aux_list_probe`: about `15.7s`.
  - `diffuse_shadow_circuit_scan`: about `14.7s`.

Critical orbit rebuild:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tools/build_critical_orbit.py
```

- Rebuilt the generated orbit files after the DAG note update.
- Projected critical view remains `189` nodes and `246` edges.
- Status counts remain `162` `PROVED`, `20` `CONDITIONAL`, and `7`
  `UNPROVED` mathematical nodes.

## Experiment batch 12: F1 pole/list threshold exact arithmetic probe

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/f1_pole_threshold_probe.py --time-limit 55
```

Checkpoint:

```text
experiments/amber_stress/f1_pole_threshold_results.json
```

Targets:

- `f1_pole_list_threshold_location`
- `f1_case_pole`
- `f1_classification`

Result:

- PASS in under `1s`.
- Official-like non-generating integer rows checked: `92`.
- Threshold failures: `0`.
- Invalid near-`|B|=|F|` controls checked: `2`.
- Invalid controls detected as non-crossing: `2`.
- Maximum additive delay of the pole-floor crossing over the integer MCA gate:
  `2^40`.

Interpretation:

- This attacks the arithmetic seam in the implication
  `f1_pole_list_threshold_location => f1_case_pole`: the exact formula

  ```text
  N(L) = ceil(L(|F|-|B|) / (|F|-|B| + 2^40 L))
  ```

  should not cross the MCA gate before the base list gate, fail to cross on
  official non-generating rows, or require more than the doubled-base reserve.
- Across rows with `|B| < 2^128`, `|B|^2 < |F|`, and `|F| < 2^256`, no such
  falsifier appeared.
- The invalid controls show the hypothesis is load-bearing: if `|B|` is
  adversarially too close to `|F|`, the saturation cap drops below the MCA gate
  and the probe correctly reports no crossing.
- This does not close `f1_pole_list_threshold_location`; the list adjacency
  premise is still the live mathematical input.  It does stress-test the
  extension-pole/list bridge arithmetic and the non-generating reserve
  monotonicity consumed by the F1 pole lane.

## Selected-suite rerun after batch 12

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 450s python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Result:

- PASS: `23/23` selected commands.
- Sum of child wall times: about `190.9s`.
- Every child command retained its own `60s` cap.
- Slowest commands:
  - `xr_smallcore_triangle_scan`: about `55.0s`.
  - `e22_extended_local_census`: about `42.5s`.
  - `petal_excess_local_scan`: about `42.3s`.
  - `xr_ledger_qpower`: about `17.3s`.
  - `pma_aux_list_probe`: about `15.9s`.
  - `diffuse_shadow_circuit_scan`: about `15.0s`.

Critical orbit rebuild:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tools/build_critical_orbit.py
```

- Rebuilt the generated orbit files after the F1 DAG note update.
- Projected critical view remains `189` nodes and `246` edges.
- Status counts remain `162` `PROVED`, `20` `CONDITIONAL`, and `7`
  `UNPROVED` mathematical nodes.

## Experiment batch 13: subgroup exponential-sum import probe

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/subgroup_expsum_probe.py --time-limit 55
```

Checkpoint:

```text
experiments/amber_stress/subgroup_expsum_results.json
```

Targets:

- `free_pool_ladder`
- `subgroup_expsum_input`

Result:

- PASS in about `8.2s`.
- Multiplicative subgroup rows checked: `749`.
- Prime range: `p <= 2800`.
- Rows searched in and above the advertised `N >= p^(3/7)` range.
- Near-linear failures at threshold `0.72`: `0`.
- Worst relative additive Fourier mass:
  `max_a |sum_{x in H} exp(2*pi*i*a*x/p)| / |H| ~= 0.6553`.
- Smallest observed saving exponent in the scanned rows: `eta ~= 0.068`.
- Negative/sanity controls detected: `9/9`.

Interpretation:

- This directly stress-tests the premise of the orphan/evidence amber
  `free_pool_ladder`: the named subgroup exponential-sum import.
- The probe does not know the exact exponent required by the historical
  `slackMCA_v4` route, so it is intentionally framed as a falsifier for gross
  no-cancellation behavior rather than as a proof.
- The interval and singleton controls are near-linear and are detected; full
  multiplicative groups show the expected cancellation.  Thus a similar
  no-cancellation subgroup row would have been flagged.
- No such subgroup row appeared in the tested range.  The analytic import
  remains open and non-critical to the current root path.
- Selected-suite rerun after batch 13: `run_selected_verifiers.py 60` PASS 24/24; child wall sum 201.4s. Slowest children: `xr_smallcore_triangle_scan` 55.0s, `petal_excess_local_scan` 43.1s, `e22_extended_local_census` 42.9s, `xr_qpower_experiment` 17.7s, `pma_structural_search` 15.8s, `diffuse_shadow_circuit_scan` 15.1s, `subgroup_expsum_probe` 9.0s. `tools/build_critical_orbit.py` stayed at 189 critical nodes, 246 critical edges, status counts PROVED 162 / CONDITIONAL 20 / UNPROVED 7 / PROVABLE 0.

## Experiment batch 14: XR small-core quadrilateral rank scan

Targeted nodes:

- `xr_smallcore_spread_count`
- amber consumer: `xr_clean_residual_any_gate`

Command:

```text
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/xr_smallcore_quad_scan.py --time-limit 55
```

Result file:

```text
experiments/amber_stress/xr_smallcore_quad_scan_results.json
```

Result:

- PASS under the selected-suite default in about `55.0s`.
- Checked `4` roomy small rows: `(p,n,k,A) = (17,12,2,4), (19,13,2,4), (23,14,3,5), (29,15,3,5)`.
- Tested `848301` deterministic slope probes over `69` small-core/light quadrilateral profile shapes.
- Found `0` rank drops, `0` severe rank drops, and `0` profiles without a full-rank probe.

Interpretation:

- This extends the previous triangle-surface falsification attempt to the first
  `m = 4` small-core/light stagnation probe.
- No counterexample to the `xr_smallcore_spread_count` premise was found.
- The result is still evidence only.  It does not prove the `16 n^3`
  post-strip bound consumed by `xr_clean_residual_any_gate`.

- Selected-suite rerun after batch 14: `run_selected_verifiers.py 60` PASS
  25/25; child wall sum about `256.2s`. Slowest children:
  `xr_smallcore_triangle_scan` 55.0s, `xr_smallcore_quad_scan` 55.0s,
  `e22_extended_local_census` 43.3s, `petal_excess_local_scan` 43.1s,
  `xr_ledger_qpower` 17.5s, `pma_aux_list_probe` 15.9s,
  `diffuse_shadow_circuit_scan` 14.8s, and `subgroup_expsum_probe` 8.6s.
  `tools/build_critical_orbit.py` stayed at 189 critical nodes, 246 critical
  edges, status counts PROVED 162 / CONDITIONAL 20 / UNPROVED 7 / PROVABLE 0.

## Experiment batch 15: E22 shuffled-layout challenger census

Targeted nodes:

- `worst_word_challenger_pricing`
- amber consumers: `worst_word_planted`, `list_planted_arithmetic`

Command:

```text
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/e22_random_layout_census.py --time-limit 55
```

Result file:

```text
experiments/amber_stress/e22_random_layout_census_results.json
```

Result:

- PASS under the selected-suite default in about `51.0s`.
- Checked `219` exact cells and `1,427,408` agreement subsets.
- Scope: `144` shuffled toy cells, `64` shuffled medium cells, `8` larger
  low-k cells, plus `3` positive-control cells.
- The positive controls all detected the known structured challenger.
- Found `0` cells with an unclassified non-planted challenger.

Interpretation:

- This attacks the two-column E22 premise away from the mostly cyclic petal
  layouts in the extended local census.
- No third challenger class was found.
- This remains evidence only: it does not prove the top-down rowwise
  challenger pricing/envelope theorem consumed by the amber arithmetic nodes.

- Selected-suite rerun after batch 15: `run_selected_verifiers.py 60` PASS
  26/26; child wall sum about `307.4s` on that run. Slowest children:
  `xr_smallcore_triangle_scan` 55.0s, `xr_smallcore_quad_scan` 55.0s,
  `e22_random_layout_census` 51.0s, `petal_excess_local_scan` 42.9s,
  `e22_extended_local_census` 42.7s, `xr_ledger_qpower` 18.2s,
  `pma_aux_list_probe` 16.1s, `diffuse_shadow_circuit_scan` 14.8s, and
  `subgroup_expsum_probe` 8.7s.
  `tools/build_critical_orbit.py` stayed at 189 critical nodes, 246 critical
  edges, status counts PROVED 162 / CONDITIONAL 20 / UNPROVED 7 / PROVABLE 0.

## Experiment batch 16: U2-C t-null boundary transition scan

Targeted nodes:

- `u2c_giant_tnull_dichotomy`
- amber consumer: `x4_exactlist_staircase_split`

Command:

```text
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/u2c_tnull_boundary_scan.py --time-limit 55
```

Result file:

```text
experiments/amber_stress/u2c_tnull_boundary_scan_results.json
```

Result:

- PASS in about `11.2s`.
- Checked `7` exact local cells.
- Positive controls detected: `2/2`.
- Clean controls with primitive non-boundary blocks: `0/2`.
- Known `N=64,t=3,b=8` transition reproduced:
  - `p=257`: `192` primitive non-boundary blocks.
  - `p=577`: `64` primitive non-boundary blocks.
  - `p=641`: `0` primitive non-boundary blocks.
  - `p=769`: `0` primitive non-boundary blocks.
- Three nearby exploratory cells also had `0` primitive non-boundary blocks.

Interpretation:

- This directly attacks the surfaced U2-C premise behind the `x4` exact-list
  split: if primitive non-boundary `t`-null blocks persisted on the clean side,
  the boundary/dictionary dichotomy would be in trouble.
- The positive controls show the detector sees the known obstruction.
- The clean controls support the certifier transition recorded in
  `u2_per_row_certifier`.
- This is evidence only; it does not prove the giant/boundary-scale U2-C
  dichotomy.

- Selected-suite rerun after batch 16: `run_selected_verifiers.py 60` PASS
  27/27; child wall sum about `318.4s`. Slowest children:
  `xr_smallcore_triangle_scan` 55.0s, `xr_smallcore_quad_scan` 55.0s,
  `e22_random_layout_census` 51.1s, `e22_extended_local_census` 42.8s,
  `petal_excess_local_scan` 42.8s, `xr_ledger_qpower` 17.4s,
  `pma_aux_list_probe` 15.9s, `diffuse_shadow_circuit_scan` 14.9s,
  `u2c_tnull_boundary_scan` 11.9s, and `subgroup_expsum_probe` 8.7s.
  `tools/build_critical_orbit.py` stayed at 189 critical nodes, 246 critical
  edges, status counts PROVED 162 / CONDITIONAL 20 / UNPROVED 7 / PROVABLE 0.

## Experiment batch 17: DLI weighted/RES low-mass falsifier and repair probe

Targeted nodes:

- `dli_prime_weighted_large_block_support`
- amber consumer: `x4_exactlist_staircase_split`

Command:

```text
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/dli_weighted_res_probe.py --time-limit 55
```

Result file:

```text
experiments/amber_stress/dli_weighted_res_probe_results.json
```

Result:

- PASS in about `17.8s` under the hard `60s` cap.
- Checked `13` exact cells.
- Reproduced `2/2` expected low-mass ternary refutations of the old
  pointwise/sup DLI-flatness premise.
- Found `0` unexpected alarms after classifying those known sup refutations.
- Zero-atom rank-charge control had charged exponent `0.0`.

Exact findings:

- `n=16,L=4`, eight ternary active coordinates:
  `rho = 211475.08017070568`, `eta = 2.3299609146907123`.
- `n=32,L=4`, twelve ternary active coordinates:
  `rho = 2610.803458897601`, `eta = 1.4949413720360685`.
- Exact meet-in-the-middle larger-active ternary cells then flattened:
  `eta = 0.6599218293814246` at `m=16`,
  `eta = -0.1750977132732192` at `m=20`, and
  `rho = 1.0365770232770783`, `eta = 0.006826159202134505`,
  zero-fiber count `211` at `m=24`.

Interpretation:

- This kills the stronger pointwise/sup DLI premise in a way that active
  full-rank scoping cannot repair: the obstruction is mass-forced, not a rank
  defect.
- The amber implication into `x4_exactlist_staircase_split` was therefore
  weakened explicitly: it may consume only the U-weighted/RES aggregate
  statement actually needed by the primitive-core ledger.
- The weakened weighted/large-active premise survived this bounded exact probe.
  This remains evidence only; `dli_prime_weighted_large_block_support` is still
  a red `TARGET`.

- Selected-suite rerun after batch 17: `run_selected_verifiers.py 60` PASS
  28/28; child wall sum about `337.4s`. The suite now includes
  `dli_weighted_res_probe`. Slowest children:
  `xr_smallcore_quad_scan` 55.0s, `xr_smallcore_triangle_scan` 55.0s,
  `e22_random_layout_census` 51.1s, `e22_extended_local_census` 43.1s,
  `petal_excess_local_scan` 42.8s, `dli_weighted_res_probe` 18.5s,
  `xr_ledger_qpower` 17.9s, `pma_aux_list_probe` 15.8s,
  `diffuse_shadow_circuit_scan` 15.1s, `u2c_tnull_boundary_scan` 11.5s,
  and `subgroup_expsum_probe` 8.6s.

## Experiment batch 18: TR quotient-row dictionary support probe

Targeted nodes:

- `tr_perleaf_list_ident`
- amber consumer: `gap1_product_model`

Command:

```text
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/tr_quotient_dictionary_probe.py --time-limit 55
```

Result file:

```text
experiments/amber_stress/tr_quotient_dictionary_probe_results.json
```

Result:

- PASS in about `1.9s`.
- Checked `4` exact quotient rows with `M=3,4,6,8`.
- Enumerated `2,002,569` quotient polynomials across linear, quadratic, and
  random received words.
- Performed `3,846` direct upstairs fiber-support checks over all characters.
- Detected `8/8` negative controls: single-point fiber breaks and
  wrong-character twists.
- Found `0` stable-support transport mismatches.

Interpretation:

- This directly attacks the dictionary premise in `tr_perleaf_list_ident`:
  stable per-character agreement upstairs should be exactly quotient-row
  agreement downstairs, with exact-support and threshold counts transported
  fiber-by-fiber.
- The negative controls show that both hypotheses are load-bearing. If fiber
  stability or fixed-character form is removed, the probe detects mixed fibers.
- No falsifier was found. The node remains conditional because the transported
  quotient-row exact-list supply still depends on `x4_exactlist_staircase_split`.

- Selected-suite rerun after batch 18: `run_selected_verifiers.py 60` PASS
  29/29; child wall sum about `340.0s`. The suite now includes
  `tr_quotient_dictionary_probe`. Slowest children:
  `xr_smallcore_quad_scan` 55.0s, `xr_smallcore_triangle_scan` 55.0s,
  `e22_random_layout_census` 51.1s, `petal_excess_local_scan` 43.0s,
  `e22_extended_local_census` 42.7s, `dli_weighted_res_probe` 18.9s,
  `xr_ledger_qpower` 18.1s, `pma_aux_list_probe` 15.9s,
  `diffuse_shadow_circuit_scan` 14.8s, `u2c_tnull_boundary_scan` 11.9s,
  `subgroup_expsum_probe` 8.7s, and `tr_quotient_dictionary_probe` 2.1s.
  `tools/build_critical_orbit.py` stayed at 189 critical nodes, 246 critical
  edges, status counts PROVED 162 / CONDITIONAL 20 / UNPROVED 7 / PROVABLE 0.
  `tools/verify_prize_dag.py` still reports the known open targets and
  archived/unreachable side branches.

## Experiment batch 19: PMA correlated-target adversarial search

Targeted nodes:

- `pma_wide_residual`
- amber consumer: `petal_mixed_amplification`

Command:

```text
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/pma_correlated_target_search.py --time-limit 55
```

Result file:

```text
experiments/amber_stress/pma_correlated_target_search_results.json
```

Result:

- PASS in about `36.5s`.
- Completed `13` correlated-target profiles: `10` exact profiles and `3`
  sampled `M=12` profiles.
- Exact `M=6` profiles checked `18,564` interpolation subsets each.
- Exact `M=9` profiles checked `296,010` interpolation subsets each.
- Sampled `M=12` profiles checked `60,000` interpolation subsets each.
- No timeout/partial profile and no large exact spread-residual alarm.

Findings:

- Constant scalar controls produce the expected structured full-agreement
  locator target: one candidate at `M=6` and `M=9`, with agreement `18` and
  `27` respectively.
- Nonconstant exact `M=9` profiles remained small: threshold candidate counts
  `159` and `176`, both spread/non-twist by the probe's simple classifier.
- Sampled `M=12` profiles were larger but not runaway: `1,013` to `1,212`
  sampled threshold candidates, with estimated total threshold counts about
  `3.3e4` to `3.9e4`, max agreement `18`, and no large exact alarm.

Interpretation:

- This directly attacks the correlated-target strengthening in
  `pma_wide_residual` by varying both the common defect locator and the scalar
  pattern across petals.
- The wide sub-Johnson lists are visibly nonempty, so the residual remains real.
  The probe did not find a super-polynomial signal or high-agreement runaway in
  the checked toy window.
  Evidence only; `pma_wide_residual` remains a red `TARGET`.

- Selected-suite rerun after batch 19: `run_selected_verifiers.py 60` PASS
  30/30; child wall sum about `379.1s`. The suite now includes
  `pma_correlated_target_search`. Slowest children:
  `xr_smallcore_quad_scan` 55.0s, `xr_smallcore_triangle_scan` 55.0s,
  `e22_random_layout_census` 51.1s, `e22_extended_local_census` 43.2s,
  `petal_excess_local_scan` 43.2s, `pma_correlated_target_search` 38.0s,
  `dli_weighted_res_probe` 18.9s, `xr_ledger_qpower` 18.6s,
  `pma_aux_list_probe` 15.8s, `diffuse_shadow_circuit_scan` 14.8s,
  `u2c_tnull_boundary_scan` 11.5s, and `subgroup_expsum_probe` 8.9s.

## Experiment batch 20: U1-for-X4 direct-column weakening and active-core probe

Targeted nodes:

- `x4_exactlist_staircase_split`
- new red premise: `u1_x4_direct_column_budget`
- broader source route kept separate: `u1_pullback_dichotomy`

Weakening:

- The X4 amber no longer consumes the full U1 pullback-compression theorem.
- Its live U1-style input is the strictly weaker direct-column premise:
  after quotient, dihedral, moment-trade, U2 boundary, and DLI/skew strips, the
  remaining primitive exact-list active-core residue must fit the direct row
  column.  A concrete sufficient target is `<= n^3` at the official rows.
- Full U1 remains red and useful for XR/route material; this is not a closure of
  `u1_pullback_dichotomy`.

Command:

```text
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/u1_x4_active_core_budget_probe.py --time-limit 55
```

Result file:

```text
experiments/amber_stress/u1_x4_active_core_budget_results.json
```

Result:

- PASS in about `28.5s`.
- Exact gate replay passed:
  `n=16,h=3,p=17` has `352` trades;
  `n=16,h=3,p=97` has `16` trades;
  `n=16,h=4,p=17` has `120` non-toral and `6` toral trades;
  `n=32,h=5,p=97` has `96` trades.
- Checked `9` active-core rows: `5` complete rows and `4` capped window slices.
- Positive control detected: `n=16,h=4,p=17` produced `60` anchored non-toral
  trades and `48` anchored non-toral cores.
- No direct `n^3` alarms.  The maximum observed non-toral/direct-budget ratio
  was `60/4096`.
- The checked `q >= n^2` complete rows and boundary slices produced no
  non-toral active-core hits.

Interpretation:

- This is evidence for the weakened X4 premise, not a proof.  Complete small
  rows are exact; capped windows can only find falsifiers.
- The test deliberately compares against the direct `n^3` column, not the older
  stronger `h n` or `n^2` trophies.  Boundary-zone failures of those stronger
  trophies would not by themselves kill X4 under this weakened routing.

- Selected-suite rerun after batch 20: `run_selected_verifiers.py 60` PASS
  31/31; child wall sum about `405.9s`. The suite now includes
  `u1_x4_active_core_budget_probe`. Slowest children:
  `xr_smallcore_quad_scan` 55.0s, `xr_smallcore_triangle_scan` 55.0s,
  `e22_random_layout_census` 51.1s, `e22_extended_local_census` 43.0s,
  `petal_excess_local_scan` 42.7s, `pma_correlated_target_search` 37.4s,
  `u1_x4_active_core_budget_probe` 29.0s, `dli_weighted_res_probe` 18.6s,
  `xr_ledger_qpower` 17.5s, `pma_aux_list_probe` 16.0s,
  `diffuse_shadow_circuit_scan` 15.1s, `u2c_tnull_boundary_scan` 11.6s,
  `subgroup_expsum_probe` 8.7s, and `tr_quotient_dictionary_probe` 2.1s.
