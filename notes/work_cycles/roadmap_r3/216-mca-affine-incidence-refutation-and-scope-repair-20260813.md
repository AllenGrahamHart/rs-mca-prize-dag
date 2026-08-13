# Cycle 216: MCA affine-incidence refutation and scope repair (2026-08-13)

## Trigger

An attempted rank-preserving recursive-shortening compiler forced a check of
the rank-one base case.  The printed common-zero bound became zero for a
nonempty singleton family, exposing a missing affine-rank-zero branch.  A
direct construction then showed that the defect is more fundamental: the
underlying MCA affine-incidence denominator is false.

## Exact counterexample

Over `GF(1009)` in

```text
RS[F,{0,...,99},1],       (n,K,m,w,s)=(100,1,21,20,1),
```

one received line has 31 selected slopes with exact maximal agreement
supports of size 21, same-support pair noncontainment, and explanations in
one affine codeword line.  The direction is separated:

```text
max_(c in C) agr(r_1,c)=20<21=m.
```

Nevertheless,

```text
affine-span compiler:          claimed 23 < 31,
direction-support refinements: claimed 22 < 31.
```

The primary and independent verifiers reconstruct all 100 coordinates and
all 31 maximal supports.  No search or probabilistic computation is used.

## Proof gap

Same-support pair noncontainment correctly forces the normals incident with
each selected support to span the full parameter space.  It does not bound
the multiplicity of normals in a proper subspace.  Each zero-explanation
witness in the counterexample contains 20 normals on one line and one
transverse normal: 40 ordered bases, against the proof's charge of
`m*w=420`.

This also refutes upstream `thm:affine-span-mca` at its printed
direction-separated scope.  It is an upstream-grade correctness report for
PR `#1163`, not merely a local no-separation issue.

## DAG repair

The following nodes are now `REFUTED`:

- `rate_half_mca_supportwise_affine_span_compiler`;
- `rate_half_mca_direction_support_affine_basis_payment`;
- `rate_half_mca_direction_support_common_zero_envelope`.

The combined `rate_half_mca_global_core_rank_support_distance_router` returns
to `TARGET`.  Its former rank and middle-support payments are withdrawn.
At the first residual dimensions, only the independent extremal gates remain:

```text
KoalaBear s=14:  e<=5 or e>=1044239,
Mersenne s=6:    e<=1 or e>=1044242.
```

## Surviving theorems

The codeword-direction gauge identity and rank shift at most one were split
from the invalid incidence add-on and reverified.  Ordinary punctured-list
decoding, sparse-direction affine-rank/heavy-fiber bounds, the directional
Johnson theorem, and recursive shortening remain proved.

The direction-distance gate now starts honestly at `s=1`.  Recursive
shortening is initialized separately from that direct gate, with no false
all-defect base.  Exact repaired checkpoints include

```text
KoalaBear:   j<=4337 at s=14, j<=4330 at s=22, j=0 through s=4992;
Mersenne:    j<=4334 at s=6,  j<=4330 at s=10, j=0 through s=4979.
```

## Replacement target

The valid next MCA theorem must control proper-subspace occupancy of incident
normals, not merely local full rank.  Any replacement also needs whole-line
first-match ownership.  Historical rank/support products remain arithmetic
records only.

```text
start:                   e4073ebba
result:                  one PROVED exact counterexample;
                         three incidence nodes REFUTED;
                         one combined router PROVED -> TARGET;
                         gauge/direction/shortening packages scope-repaired
DAG delta:               +1 node, +3 edges net after rewiring
critical status delta:   none; corrected evidence under rate-half MCA target
upstream terminal delta: printed affine-span MCA compiler and PR #1163
                         small-dimension use require correction
delta-star movement:     none
compute:                 exact bounded local arithmetic under RAMguard;
                         no Modal spend
next route action:       export the counterexample/correction upstream, then
                         seek a proper-subspace occupancy replacement
```
