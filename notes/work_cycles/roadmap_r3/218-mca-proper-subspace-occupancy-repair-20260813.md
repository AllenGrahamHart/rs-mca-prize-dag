# Cycle 218: MCA proper-subspace occupancy repair (2026-08-13)

The Cycle 216 counterexample identifies one precise loss: local full incident
rank gives one final basis extension, not the old unconditional factor `w`.
The new field-general theorem
`rate_half_mca_proper_subspace_occupancy_compiler` proves the correct
interpolation.

For selected explanation affine rank `q`, let

```text
e=min_(b in C) wt(r_1-b),       t=N-m,
L=max(1,e-t).
```

MDS generalized weights control every incident normal subspace of dimension
below `q`.  Same-support pair noncontainment supplies one final transverse
normal, while direction-coset distance raises that final factor to `L`.
The resulting exact bound is

```text
floor(max(A_q,B_q)/L),
```

with the two zero-normal endpoint expressions printed in the node.  The old
formula is recovered only at maximum direction support, where `L=w`.

At the first KoalaBear residual dimension, ranks 1 through 9 are now paid for
every direction support.  Ranks 10 through 13 are paid respectively from

```text
e=981108, 981153, 981861, 992852.
```

Rank 14 remains on the independent gates `e<=5` or `e>=1044239`.  At the
first Mersenne residual dimension, rank 1 is fully paid and ranks 2 through 5
are paid from

```text
e=981144, 981363, 984779, 1037876.
```

Rank 6 remains on `e<=1` or `e>=1044242`.

The primary checker recomputes all exact walls and eight adjacent failures.
The independent rational checker scans 616 allowed zero-normal cases and
replays the `GF(1009)` regression at corrected bound 471.  It also exhausts
all 729 `GF(3)` rank-one received lines and 540 nontrivial selected families.

The theorem, proof, finite calibration, and combined checker were added to
draft upstream PR `#1165` at head `75c61ae4`.  PRs `#1163` and `#1164` were
given follow-up dependency comments with the repaired fixed-core walls.

```text
start:                   27be48115 plus Cycle 217 provenance edits
result:                  NARROWED + EXPORTED; one PROVED field-general
                         replacement
DAG delta:               +1 PROVED node, +1 evidence edge
critical status delta:   none; the replacement target remains TARGET
upstream terminal delta: corrected theorem and walls added to PR #1165;
                         dependent PRs #1163/#1164 notified
delta-star movement:     none
compute:                 exact bounded local arithmetic under RAMguard
next route action:       attack the explicit top-rank middle-support cells,
                         or export the corrected theorem after review
```
