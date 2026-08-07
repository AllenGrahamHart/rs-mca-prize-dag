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

External PRs #1140, #1141, #1144, and #1149 provide the exact upstream atlas
and cell-specific closures. The local restricted inversion theorem closes
all six `F00/F01` cells, and the exact GREEN #1141 import closes all six
`F02/F03` cells. Independent replay of #1144 now proves ten moving cells.
The exact generic/rank-drop localization theorem closes all four
`F04`--`F07` cells over `R11`. Direct exhaustive compositions close
`F04-R02` and `F07-R02`; the exact complete-system inversion
`F04<->F05`, `F06<->F07` then closes the other two `R02` companions. The
four fixed `R20` cells are now also closed by exhaustive rank-drop,
cubic/full-`J`, and degree-12 compositions. Thus 34 of 36 aligned-positive
cells are PROVED. The exact residual is

```text
M01-R11, M02-R11.                                (KBCOV-1)
```

The first two cells retain a precise Sage/Singular portability review gate.
The pinned and independently replayed #1149 compression theorem is PROVED
locally. Its two balanced fingerprint orbits are now closed by direct
four-cell generic and rank-drop computations. For the four `R02/R20`
fingerprint orbits, all sixteen literal `V=0` factor branches are PROVED
empty.

On every generic fixed chart, the resultant core factors with degrees
`3,3,12`. Literal replay plus complete-system inversion closes both cubic
routes. The degree-12 branch is partitioned by `s`, its degree-6 leading
factor `L6`, and the `B0` leading factor `K10`. The `s=0` and `L6=0` leaves
were already empty. The `K10!=0` chart collapses to a forbidden transported
boundary. On `K10=0`, `B0` becomes linear; division-free evaluations of
`A1,B1` at that root give two degree-58 necessary equations, and the complete
named-open saturation is unit for the F04 and F06 representatives. Inversion
supplies F05 and F07. Hence all four fixed `R20` cells are empty and the only
aligned-positive review gate is the moving `M01/M02-R11` pair.

Closing only the aligned-positive cells is insufficient unless the same
literal-assignment audit validates the local aligned-negative and
near-aligned coverage claims.

## Falsifier

An admissible literal source assignment absent from the compiler, a cell
transport that changes a q-slice target or source divisor, an untracked
degree-drop/localizer component, or any surviving full-quotient point.
