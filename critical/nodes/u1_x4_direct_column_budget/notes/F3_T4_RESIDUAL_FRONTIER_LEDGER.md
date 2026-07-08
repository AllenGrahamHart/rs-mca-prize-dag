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
  paid antipodal branch.
  Residual: certify 122,131,731,640,320 anchored non-antipodal 16-supports, or
  build a sharded signature join avoiding the blind left table.
```

## Dependency Shape

The T4 closure shape is now:

```text
h4_terminal_dichotomy
  + x83_uniform_square_shift_obstruction_gate
  => h=4 structurally localized

h5_structural_reduction
  + h=5 certificate coverage/scaling audits
  => T4-H5-NORM-GATE remains the only h=5 blocker

h6/h7 bonus sweep replay
  + h6 p4993 square-lift analysis
  => no current h=6/h=7 direct-budget blocker

h8 antipodal quotient
  + locator parity antipodal criterion
  + support-to-trade reduction
  + split rotation equivariance
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
