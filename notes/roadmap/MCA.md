# MCA Resolution Lane

This is a navigation view.  Node-local manifests and the generated DAG are
the status source of truth.

## Terminal

The lane terminates only when `mca_grand` is unconditionally `PROVED`,
including the finite adjacent rows and maximal-safe/adjacent-unsafe
certificates required by the challenge.

## Current critical families

- `(Q)`: growing-order quotient/prefix flatness.
- Primitive shift-pair control and the DSP8 correlation bound.
- The `h>=4` norm-gate count.
- Mixed-petal amplification.
- Split-pencil high-core, low-core, and graded tangent charges.
- The deployed rate-half band closure.
- The `c2(1,1,2)` source-line literal-assignment coverage repair: the local
  six-cell ledger is exactly `{F00,M00} x {R02,R11,R20}`, not an exhaustive
  source-assignment atlas. The former branch-level PROVED promotion is now
  CONDITIONAL pending literal coverage or a complete-system restricted
  symmetry theorem.
- The first restricted symmetry is now PROVED: literal reparameterization
  `b -> b^-1` identifies every complete `F01-Rxx` system with
  `F00-Rxx`. All six `F00/F01` cells are therefore closed locally; this does
  not transport to `F02`--`F07`.
- Upstream PR #1141 is imported as a pinned PROVED exact theorem after its
  local Python replay and recorded independent Sage review: all six
  `F02/F03` cells are closed. A fresh sharded review of PR #1144 proves ten
  moving cells. The balanced `M01-R11` cell and its literal `M02-R11`
  companion remain PROVABLE: parity and certificate checks pass, but three
  Sage environments fail at the external Singular basis-conversion bridge.
  The direct generic/rank-drop localization now also closes all four
  `F04`--`F07-R11` cells. Current aligned-positive coverage is therefore
  `26/36`, with those two moving cells and the eight `F04`--`F07` cells over
  `R02/R20` remaining. PR #1149's exact quadratic compatibility theorem and
  six-orbit compression are pinned PROVED; its two balanced fixed orbits are
  fully closed. All sixteen rank-drop factor branches in the four remaining
  fixed orbits are now PROVED empty, leaving only generic `V != 0` charts.
  Their representative resultant cores split with degrees `3,3,12`; one
  cubic closes, while the complementary cubic and the degree-12 factor remain
  route-level obstructions. On `F04`, full-`J` coefficient zero further
  reduces the surviving cubic to one degree-11 factor. No additional literal
  cell is yet closed by these generic cuts. The degree-12 branch has now been
  decomposed at its `x`-leading boundary: all leading factors are nonnamed,
  including `s`, one common irreducible degree-6 curve, and target-specific
  irreducibles of degrees `22`--`24`. Direct function-field division and a
  three-step pseudo-remainder prefix are exact no-go fences; the latter grows
  to 149340 terms while lowering `x`-degree only to 34.
  The smallest explicit leaf, `s=0`, is now PROVED empty in all eight
  literal fixed cells: each specialized ideal has a two-element basis and
  the complete transported localizer vanishes at factor 14. This is a
  branch close only; aligned-positive coverage remains `26/36`.
  Both literal forms of the irreducible degree-6 leading curve are likewise
  PROVED empty in all eight cells: `F04/F07` share a 15-term form,
  `F05/F06` a distinct 17-term form, the full ideals have basis size `43` or
  `46`, and the localizer vanishes at factor 17. The live branch has `s!=0`
  and `L6!=0`; coverage still remains `26/36`.
  Direct degree `22`/`23` curve intersections have exact dimension-one seed
  bases but retain roughly 6000-term rows and time out. Curve-reduced
  pseudo-division reaches `deg_x=5` but grows to roughly 23500 terms per
  row. Both expanded endpoints are fenced. The new PROVED parity-reduced
  evaluation identity replaces powers `U^(2j)` by `(VZ)^j` modulo
  `R=U^2-VZ` before expansion and supplies a possible block-level route.
  Its metrics-only literal replay shows that expansion retains `52257` and
  `49848` terms, almost the entire direct rows. The expanded parity endpoint
  is therefore also fenced; only a block-level factorization or syzygy is
  authorized next.

These labels are route families rather than substitute hypotheses.  A
supplier enters a consumer as `req` only after an exact transport theorem;
otherwise it remains `ev`.

## Upstream alignment

Use Przemek's terminology in outbound packets.  The local-to-upstream scope,
pins, and two-axis status are maintained in
`notes/correspondence/JOINT_CROSSWALK.json` and summarized in
[SHARED_UPSTREAM.md](SHARED_UPSTREAM.md).

- [Added 2026-08-07, CATCH-P3 filing correction] Universal
  unsafe-crossing family instantiation
  (unsafe_crossing_family_instantiation) — MCA-lane: sole out-edge
  to unsafe_at_crossing; formerly filed under LIST.md in error.
