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
`F04<->F05`, `F06<->F07` then closes the other two `R02` companions. Thus 30
of 36 aligned-positive cells are PROVED. The exact residual is

```text
M01-R11, M02-R11,
{F04,F05,F06,F07} x {R20}.                       (KBCOV-1)
```

The first two cells retain a precise Sage/Singular portability review gate.
The pinned and independently replayed #1149 compression theorem is PROVED
locally. Its two balanced fingerprint orbits are now closed by direct
four-cell generic and rank-drop computations. For the four `R02/R20`
fingerprint orbits, all sixteen literal `V=0` factor branches are PROVED
empty.

On the generic fixed charts, the resultant core factors with degrees
`3,3,12`. Literal replay plus complete-system inversion now proves the first
cubic empty and closes the complementary full-`J` logarithmic route for all
eight `R02/R20` cells. All four `R02` degree-12 branches are also closed, so
every fixed `R02` cell is empty. Consequently each of the four residual
`R20` cells is reduced exactly to its degree-12 branch.

The degree-12 branch now has an exact leading-drop ledger. In `x`, its own
leading coefficient is a common nonnamed irreducible degree-6 curve; the
`E2/E3` leading coefficients add `s=0` and nonnamed irreducible curves of
degrees `22`--`24`. Naive function-field or pseudo-remainder elimination
therefore inverts real branches and grows rather than compresses. The next
valid attack needs source-level cancellation or a branchwise theorem.
The smallest leading-drop leaf, `s=0`, is PROVED empty by eight literal
localizer computations. This narrows each residual `R20` degree-12 route to
`s!=0`.
Both literal forms of the irreducible degree-6 leading curve are also PROVED
empty by eight literal localizer computations. The live `R20` degree-12
route therefore has both `s!=0` and `L6(s,p)!=0`.
Direct imposition of the degree `22`--`23` curves and a second
curve-reduced pseudo-division implementation both retain thousands of terms
and time out at the final intersection. A separate PROVED identity now
replaces every cleared row evaluation by a division-free parity-reduced
representative modulo `U^2-VZ`. Literal expansion retains `52257` and
`49848` terms, so the identity is viable only before expansion, inside a
new block-level factorization or syzygy.

Closing only the aligned-positive cells is insufficient unless the same
literal-assignment audit validates the local aligned-negative and
near-aligned coverage claims.

## Falsifier

An admissible literal source assignment absent from the compiler, a cell
transport that changes a q-slice target or source divisor, an untracked
degree-drop/localizer component, or any surviving full-quotient point.
