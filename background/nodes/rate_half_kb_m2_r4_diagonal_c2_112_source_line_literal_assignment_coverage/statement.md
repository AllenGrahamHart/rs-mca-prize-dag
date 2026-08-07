# KoalaBear source-line literal-assignment coverage

- **status:** TARGET
- **scope:** every literal internal source-star assignment in the saturated
  diagonal `c2(1,1,2)` source-line branch
- **evidence:**
  `rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_literal_cell_crosswalk`
- **consumer:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_complete_exclusion`

Prove complete source-bound coverage without using generic endpoint-only
Möbius covariance. It is enough to provide either:

1. a literal compiler and first-match classification for every assignment,
   target, sign, ramification, and boundary cell; or
2. a restricted symmetry theorem proved for the complete source form,
   q-slice targets, localizers, and both full quotient identities.

For the aligned-positive unramified branch, the literal source registry has
eight fixed-moving and four moving-moving assignments, each with three root
distributions, hence 36 semantic cells. The proved crosswalk identifies the
six local canonical systems. The restricted literal inversion theorem then
transports the three `F00` exclusions to all three `F01` companions, closing
the six-cell `{F00,F01} x {R02,R11,R20}` block without generic covariance.

External PRs #1140, #1141, #1144, and #1149 provide an exact upstream atlas
and substantial cell-specific closures. They are integration candidates,
not theorem dependencies of this local TARGET until imported and replayed.
The currently advertised upstream branch after #1149 retains 16 fixed-moving
cells because its stack does not import all three representative
full-quotient packets. The local restricted inversion theorem reconciles
that six-cell block. The residual aligned-positive literal assignments are
`F02`--`F07` and `M00`--`M03` until upstream closures are imported.

Closing only the aligned-positive cells is insufficient unless the same
literal-assignment audit validates the local aligned-negative and
near-aligned coverage claims.

## Falsifier

An admissible literal source assignment absent from the compiler, a cell
transport that changes a q-slice target or source divisor, an untracked
degree-drop/localizer component, or any surviving full-quotient point.
