# F3 T4 residual frontier ledger

Status: REPLAYED FRONTIER LEDGER; h=5 PAID, h=8 STILL OPEN.

This packet compiles the current T4 frontier for
`notes/codex_briefs/F3_FLIP_20260708.md` from existing proved nodes and
certificate audits.  It launches no search.  Its purpose is to keep the T4
frontier explicit, so later work does not spend cycles on already localized or
paid strata.

## Frontier Nodes

```text
T4-H4-STRUCTURAL: PROVED
  h4_terminal_dichotomy and x83_uniform_square_shift_obstruction_gate are
  PROVED.  There is no hidden h=4 classification residual.

T4-H5-NORM-GATE: REPLAYED/PAID
  The current bank has 589 complete h=5 zero rows and 3,164,030,779 audited
  right-side probes.  This includes all admissible n=32 primes through 65537,
  179 n=64 certified primes with 515 admissible primes still missing up to the
  largest certified n=64 prime, one n=96 row, and seven n=128 rows.
  The h=5 x83 compiler also triangularizes the low obstruction keys as
  D_j E_j = -D_j l_j + P_j(l5,...,l9), with max low-key conjugate bound
  1,104,676,577,280.  The reciprocal compatibility compiler eliminates the
  shared support product delta to give four delta-free compatibility
  equations of max total degree 10; the base-free reciprocal system records
  all ten pairwise rank-one equations, also of max total degree 10.  The
  reciprocal open-cover packet excludes the all-zero high-coefficient chart on
  official rows because x -> x^10 has fibers of size at most 2 in mu_{2^s}.
  The unit-norm reciprocal gate adds four Hermitian equations using
  delta*bar_delta=1, with max total degree 18.  The chart-local recovery
  compiler sharpens this to five chart obligations: four incident rank-one
  minors plus `N_i` on charts `1..4`, and four incident minors with automatic
  unit norm on the central `bar_l5 != 0` chart.  The central automatic-unit
  claim is verified by four saturated syzygies
  `l5*N_i in <C_i5,conjugate(C_i5)>`.  More generally, the rank-one unit
  propagation packet verifies 20 abstract syzygies showing that one unit row
  on a nonzero denominator chart propagates to every other slot.  The
  rank-one minor propagation packet verifies 30 abstract syzygies showing that
  the four incident minors on a chart imply the six nonincident minors after
  saturating by that chart denominator.  The chart-local profiles range from
  `67` total terms on the central chart to `615` terms on chart `1`; the
  central chart has max degree `10` and no Hermitian equation.  The central
  chart graph compiler sharpens this further: after saturating by `l5*bar_l5`,
  the four central equations solve `bar_l9,bar_l8,bar_l7,bar_l6` explicitly.
  The fixed-point skeleton shows why this graph structure should be preserved:
  fully expanded fixed-point numerators have pre-cancellation term bounds up to
  `1,255,488,415,957`.  The weighted-homogeneity packet verifies the natural
  root-scaling grading: all ten pairwise minors are homogeneous and all four
  unit rows have weight zero, so the next central-chart attack should preserve
  this weighted quotient.  The central weighted-slice packet verifies that
  algebraic emptiness proofs may work on the slice `l5=bar_l5=1`, where the
  four central graph equations still have `67` terms but max degree drops from
  `10` to `9`; this is not an official row orbit quotient.  The sliced
  fixed-point skeleton shows the corresponding compatibility degree bounds
  drop from `91,81,71,61` to `81,72,63,54`, but the pre-cancellation term
  bounds remain prohibitive, so direct expansion is still the wrong primitive.
  The central slice quadratic normal-form packet composes the graph only
  through degree two and verifies that the relaxed fixed equations are a
  triangular four-row system to quadratic order, with the same linear
  determinant `81/256`.  The central slice cubic normal-form packet extends
  this to degree three without expanding the global fixed numerators; the
  four cubic fixed equations have only `4..7` terms and retain the same
  linear determinant.  The central slice formal-isolation packet records the
  all-orders local consequence: since this determinant is a unit in every
  official row characteristic, the completed local fixed-point quotient at
  the normalized central origin is just the residue field.
  The official scaling packet verifies that the
  finite `mu_n` action is free on the central chart for all official rows
  because `gcd(5,2^s)=1`; arbitrary ambient scaling is not allowed.
  The central finite-scheme payment compiler records a weaker sufficient
  target than emptiness: if the saturated row-wise central slice is
  zero-dimensional, the Bezout bound `81*72*63*54=19840464` gives at most
  `19840464 n < n^3` central points on every official row.
  The central infinity-flag packet verifies a sparse eight-equation graph
  formulation and a dominant boundary flag
  `l9=0`, then `l7=0` or `l8=0`, terminating on coordinate branches.
  The central projective-infinity exclusion upgrades this flag into the needed
  finiteness proof: all projective-infinity branches terminate at
  `l6=l7=l8=l9=0`, and the largest leading-coefficient prime is `19`, below
  the official characteristic range.  Combined with the finite-scheme payment,
  this gives the h=5 contribution `< n^3` on all official rows.
  Residual: no h=5 residual for the direct `n^3` budget.  Stronger
  norm-gate emptiness remains optional and is not needed here.

T4-H6-H7-BUDGET: REPLAYED/PAID
  The local replay verifies 11 n=32 h=6/h=7 full zero rows, seven complete h=6
  n=64 rows, and one complete h=7 n=64 row.  The h=6 p=4993 row has six
  nontoral witnesses, far below n^3, and the square-lift packet routes them to
  paid h=3 quotient trades.

T4-H8-N64-NONANTIPODAL-X83: OPEN
  The current bank has six complete h=8 n=32 rows and two explicitly partial
  h=8 n=64 rows.  The p=4289 and p=262337 x83 radius-three shell certificates
  are complete with full_zero=0, but they only cover local shells around the
  paid antipodal branch.  The non-antipodal aperiodicity packet proves there
  is no separate periodic non-antipodal branch.
  The x83 parity-reduction packet proves that any non-antipodal x83 full-zero
  support must have a nonzero high odd locator coefficient among
  `c15,c13,c11,c9`; if those four coefficients vanish, full-zero forces the
  locator even and hence the support is antipodal.
  The x83 triangular obstruction compiler proves that the seven low
  obstruction equations have the form
  `D_j E_j = -D_j c_j + P_j(c8,...,c15)`.  Thus any primitive full-zero
  support lies on an explicit graph over the high locator half, with
  first obstruction `E7` having denominator `32768`, `30` terms, and total
  degree `9`.
  The h=8 reciprocal compatibility compiler combines this triangular graph
  with the unit-root coefficient identities and eliminates the shared support
  product `delta`, giving seven delta-free reciprocal compatibility equations.
  These are linear in the reciprocal bar variables, with maximum total degree
  `16`.
  Residual: certify 122,131,731,640,320 anchored non-antipodal 16-supports
  (7,633,233,227,520 aperiodic rotation orbits), or build a sharded signature
  join avoiding the blind left table.
```

## Dependency Shape

The T4 closure shape is now:

```text
h4_terminal_dichotomy
  + x83_uniform_square_shift_obstruction_gate
  => h=4 structurally localized

h5_structural_reduction
  + h=5 certificate coverage/scaling audits
  + h=5 x83 triangular norm-gate compiler
  + h=5 reciprocal compatibility compiler
  + h=5 base-free reciprocal system
  + h=5 reciprocal open-cover exclusion
  + h=5 unit-norm reciprocal gate
  + h=5 chart-local reciprocal recovery
  + h=5 central chart graph
  + h=5 central fixed-point skeleton
  + h=5 weighted homogeneity
  + h=5 central weighted slice
  + h=5 central slice formal isolation
  + h=5 central finite-scheme payment
  + h=5 central infinity flag
  + h=5 central projective-infinity exclusion
  + h=5 central slice quadratic normal form
  + h=5 central slice fixed-point skeleton
  + h=5 official scaling action
  + h=5 rank-one minor propagation
  + h=5 rank-one unit propagation
  => T4-H5-NORM-GATE is paid for the direct n^3 budget

h6/h7 bonus sweep replay
  + h6 p4993 square-lift analysis
  => no current h=6/h=7 direct-budget blocker

h8 antipodal quotient
  + locator parity antipodal criterion
  + support-to-trade reduction
  + split rotation equivariance
  + non-antipodal aperiodicity
  + x83 parity reduction
  + x83 triangular obstruction compiler
  + h8 reciprocal compatibility compiler
  + residual frontier/support-universe audits
  => T4-H8-N64-NONANTIPODAL-X83 remains the only h=8 blocker
```

Thus the T4 part of the flip should not be advanced by another broad finite
sweep unless it directly attacks the h=8 open frontier node above.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
```

Expected digest:

```text
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
```
