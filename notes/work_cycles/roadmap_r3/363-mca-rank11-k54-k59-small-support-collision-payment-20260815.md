# Cycle 363: MCA rank-11 K'=54..59 small-support collision payment (2026-08-15)

Cycle 362 closed `K'=46..53` but left the balanced exact pair
`s_4=s_5=21` at `K'=54`.  A support-five charge derived only from the
joint zero closure fails on the legal `t=4` branch.  The useful resource is
instead the attaining completion carrier at each individual support.

## Cycle pins

```text
our start:       8c3a30f9a0d2a29289226431c810a5a74cd200c6
our end:         cycle commit containing this record
canonical prize: 6ac775504aa7dd6489ae5175235084e270abf6d2
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170 at c8b610fa48fda07c961d1b04cb20e3f87f910838
```

## Same-source collision theorem

At support `c<=5`, let an independent source deletion attain `q-s`
completions and let `B` be its carrier.  For any other independent deletion,
the two vanishing spaces have dimension `11-c`, hence intersection dimension
at least

```text
12-2c>0.
```

The common-root bound implies that the second carrier has at most `s+c-1`
points outside `B`.  Splitting a circuit by its exact number `j` of outside
points and deleting each outside point gives the circuit-support cap

```text
C(b,c)+sum_(j=1)^c floor(
  C(b,c-j) C(m-b,j-1) (s+c-j) / j
),
```

for `0<s<q`, with separate exact branches `C(b,c)` at `s=0` and zero
circuits at `s=q`.  This is unconditional for supports `2,3,4,5`.

## Six-row payment

Refine supports `2..5` to every exact defect.  Pareto-compress the groups
`(2,3)`, `(4,5)`, and `(6,7,8,9)` separately.  On every row `K'=54..60`,
their maximal-vector counts are `1,1,7`; thus all
`3,693,717,480` represented raw leaves on the six safe rows reduce to 42
exact frontier evaluations.

The active branch is

```text
s_2=s_3=s_4=s_5=floor(q/2),       c6F/c7F/c8F/c9F.
```

Rows `K'=54..59` have positive premium margins and exact component gaps.
The smallest gap is at `K'=59`:

```text
2662571195028360324230500777441238424043251068116179184680206.
```

At `K'=60`, complete capacity exceeds demand by

```text
3672733965923291717387950853821894967875078243379846951201638.
```

Primary and independently coded replays agree on every group frontier,
premium, fixed capacity term, safe sign, and adjacent wall.

```text
result:                PROVED K'=54..59 component-row closure
newly closed rows:     54..59
closed prefix:         10..59
remaining rank nine:  60..15528
new nodes:             2 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced six rows
upstream delta:         cycle-362 K'=46..53 packet exported to #1170
delta-star movement:   none
compute:               exact local arithmetic under 1 GiB cap; no Modal spend
next route action:     attack the all-fallback support-6..9 wall at K'=60
```
