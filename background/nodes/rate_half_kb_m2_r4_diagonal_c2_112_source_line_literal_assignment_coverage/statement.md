# KoalaBear source-line literal-assignment coverage

- **status:** TARGET
- **scope:** every literal internal source-star assignment in the saturated
  diagonal `c2(1,1,2)` source-line branch
- **evidence:**
  `rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_literal_cell_crosswalk`
- **affine near-positive transport:**
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_literal_inversion_transport`
- **pair-swap route cut:**
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_pair_swap_covariance_refutation`
- **direct residual registry:**
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_direct_residual_registry`
- **first direct exclusions:**
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_f02_square_orbit_exclusions`
- **F02 mixed collision exclusions:**
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_f02_mixed_collision_exclusions`
- **F04 complete-chart exclusions:**
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_f04_complete_chart_classification`
- **F06 complete-chart exclusions:**
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_f06_complete_chart_classification`
- **M01 chart and quotient exclusions:**
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_m01_complete_chart_classification`
- **M03 chart and quotient exclusions:**
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_m03_complete_chart_classification`
- **projective-boundary literal coverage:**
  `rate_half_kb_m2_r4_diagonal_c2_112_near_positive_projective_boundary_literal_coverage`
- **aligned-negative literal coverage:**
  `rate_half_kb_m2_r4_diagonal_c2_112_aligned_negative_literal_assignment_coverage`
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
cubic/full-`J`, and degree-12 compositions. Finally, direct Singular with an
interreduced same-ideal `J` generating set completes the exact full-quotient
certificate for `M01-R11`; the checked complete-source inversion supplies
`M02-R11`. Thus all 36 aligned-positive cells are PROVED:

```text
aligned-positive residual = empty.                 (KBCOV-1)
```

The 36-cell aggregate checks a disjoint seven-packet census rather than
inferring coverage from an orbit count.
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
supplies F05 and F07. Hence all four fixed `R20` cells are empty. Together
with the exact moving-pair certificate, the aligned-positive registry has no
remaining cell.

For the separate affine near-positive literal audit, the proved restricted
inversion transport acts on the reconstructed q-slice residuals, targets,
and radical localizers. It reduces `108` semantic cells to `42` exact
transport orbits. The canonical `F00/M00` leaves represent `12`; the
remaining affine frontier is the explicit 30-cell product

```text
{F02/F03,F04/F05,F06/F07,M01/M02,M03}
    x {{A,TA},other} x {RX,RL,RM}.                 (KBCOV-2)
```

This reduction does not supply a full-quotient transport and does not cover
the near-positive projective boundary or either negative-sign literal audit.

The remaining matching-centralizer generator cannot enlarge this quotient.
For the normalized reciprocal-pair swap, all target quadratics transform
exactly, but both reconstructed residuals fail for every induced assignment;
an exact search finds no alternative literal destination in either root
order. Thus the 30 cells in `(KBCOV-2)` are direct classification tasks, not
unclaimed centralizer images.

The exact direct compiler records all 30 representatives and its
reconstruction-generated nonmonomial factors. Sequential saturation and an
independent Rabinowitsch audit prove the
four `F02` square-allocation representatives empty:

```text
F02-A-RX, F02-A-RL, F02-OB-RX, F02-OB-RL.        (KBCOV-3)
```

For both mixed cells, localization by the ten recorded factors and the torus
units leaves a zero-dimensional scheme on which `c-d` vanishes identically.
Because `c,d` are distinct `J_1` labels, `c-d` is an inherited chart unit.
Direct collision saturation and independent complete-localizer
Rabinowitsch ideals close both mixed representatives. The post-`F02` affine
near-positive residual is exactly 24 representatives:

```text
{F04,F06,M01,M03} x {A,other} x {RX,RL,RM}.      (KBCOV-4)
```

For every one of the six `F04` representatives, sequential saturation by
the twelve reconstruction factors and the inherited units `b,c,d,c-d`
returns the unit ideal. Independent one-step Rabinowitsch ideals with the
complete sixteen-factor product also return `[1]`. The `F04/F05` direct
orbit block is therefore closed. The current affine residual is exactly

```text
{F06,M01,M03} x {A,other} x {RX,RL,RM},           (KBCOV-5)
```

consisting of `18` representatives.

The same dual exact calculation closes all six `F06` representatives:
sequential complete-chart saturation is unit, and independent one-step
Rabinowitsch ideals with all sixteen factors are `[1]`. Thus the represented
`F06/F07` direct block is also empty. The current affine residual is

```text
{M01,M03} x {A,other} x {RX,RL,RM},               (KBCOV-6)
```

consisting of `12` representatives.

Five `M01` representatives have unit complete-chart q-slice ideals in both
sequential and one-step formulations. The sole survivor, `M01-A-RL`, has an
exact two-point base-field chart. Because full quotient transport is not
licensed, all eight `M01/M02`, `A/TA` literal companions are reconstructed
separately. Every point passes its q-slice and localizer controls and fails
the first necessary colored quotient norm. Hence the current affine residual
is exactly

```text
{M03} x {A,other} x {RX,RL,RM},                   (KBCOV-7)
```

consisting of `6` representatives.

Five of those six `M03` representatives also have unit complete-chart ideals
under both exact formulations. The sole survivor, `M03-OB-RL`, has a
zero-dimensional lex basis whose `c`-eliminant is the product of two distinct
irreducible quadratics. It therefore has exactly four `F_(p^2)` points, all
present over `F_(p^6)`. The inversion closure of those points is checked
directly, but full quotient covariance is not assumed: all four `OB` points
and all four `OI` companions are reconstructed independently. Each passes
its endpoint, q-slice, and localizer controls and fails the first colored
quotient norm. Consequently

```text
affine near-positive direct residual = empty.      (KBCOV-8)
```

The positive projective boundary is also literal rather than normalized.
The twelve source-star assignments and four target roots give 48 cells.
Direct homogeneous reconstruction and complete named-open localization prove
all 48 q-slice ideals unit under both Rabinowitsch and sequential saturation:

```text
positive projective-boundary literal residual = empty. (KBCOV-9)
```

The aligned-negative branch is now literal as well. Direct reconstruction on
the complementary charts `c+d!=0` and `c+d=0` covers all twelve assignments.
After selected-minor factors are inverted, its 24 chart cells contain exactly
32 genuine consistency components; the two normalized mismatch identities
hold on every component and exclude all of them:

```text
aligned-negative literal residual = empty.         (KBCOV-10)
```

The sole remaining obligation is literal coverage for the 48 near-negative
assignment/root cells.

## Falsifier

An admissible literal source assignment absent from the compiler, a cell
transport that changes a q-slice target or source divisor, an untracked
degree-drop/localizer component, or any surviving full-quotient point.
