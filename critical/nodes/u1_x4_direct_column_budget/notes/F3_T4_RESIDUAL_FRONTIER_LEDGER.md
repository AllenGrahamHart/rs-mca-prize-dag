# F3 T4 residual frontier ledger

Status: REPLAYED FRONTIER LEDGER, NOT A NEW GENERAL-N THEOREM.

This packet compiles the current T4 frontier for
`notes/codex_briefs/F3_FLIP_20260708.md` from existing proved nodes and
certificate audits.  It launches no search.  Its purpose is to keep the
remaining h=5 and h=8 blockers explicit, so later work does not spend cycles on
already localized strata.

## Frontier Nodes

```text
T4-H4-STRUCTURAL: PROVED
  h4_terminal_dichotomy and x83_uniform_square_shift_obstruction_gate are
  PROVED.  There is no hidden h=4 classification residual.

T4-H5-NORM-GATE: OPEN
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
  on a nonzero denominator chart propagates to every other slot.
  Residual: prove a symbolic p-specific x83 norm-gate incompatibility theorem,
  or replace the selected finite rows with a scalable certificate family.

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
  + h=5 rank-one unit propagation
  => T4-H5-NORM-GATE remains the only h=5 blocker

h6/h7 bonus sweep replay
  + h6 p4993 square-lift analysis
  => no current h=6/h=7 direct-budget blocker

h8 antipodal quotient
  + locator parity antipodal criterion
  + support-to-trade reduction
  + split rotation equivariance
  + non-antipodal aperiodicity
  + residual frontier/support-universe audits
  => T4-H8-N64-NONANTIPODAL-X83 remains the only h=8 blocker
```

Thus the T4 part of the flip should not be advanced by another broad finite
sweep unless it directly attacks one of the two open frontier nodes above.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
```

Expected digest:

```text
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
```
