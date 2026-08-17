
# Cycle 366: MCA rank-11 K'=72 carrier flag and split-section wall (2026-08-16)

Cycle 365 left the first open row at `K'=72`, where the support-three
completion maximum is two above the support-two maximum.  A two-step carrier
atlas now isolates the leading nonnested geometry and replaces part of the
raw completion envelope by two unconditional charges.

## Cycle pins

```text
our start:       90178b01dba1b5fdd0c3e955e060ad41c8e7a21a
our end:         cycle commit containing this record
canonical prize: 28a62b400
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170 at 1ca90d4c570e3630b62c4cca084549282f1d7418
rich-flat stack: #1171..#1173, tip 2788d5ec3fb4b1d6f9c43a58a86ec2381e5f6804
```

## Completion-stratified fixed-union theorem

Suppose a `g`-dimensional correction subspace vanishes on a fixed `u`-point
union, and every independent support-`d` deletion has at most `M_d`
completions.  For a circuit with exactly `j` points outside the union, the
inside deletion points impose no further conditions on the vanishing
subspace.  The outside completion budget is therefore

```text
B_j=min(M_d,K'-g-u),  j<=g,
B_j=M_d,              j>g.
```

Exact outside-point exposure gives the circuit-support cap

```text
C(u,d)+sum_(j=1)^d floor(
  C(u,d-j) C(m-u,j-1) B_j / j
).
```

If the union contains a parallel class of size `b` and `d>=3`, minimality
replaces each inside binomial by

```text
I_b(u,r)=C(u-b,r)+b C(u-b,r-1),
```

because a minimal circuit cannot contain two points from one projective
parallel class.  This theorem is unconditional and reusable beyond `K'=72`.

## K'=72 carrier-flag router

At the active completion values

```text
M_2=28, M_3=30, M_4=M_5=31,
```

the maximal-overlap carriers satisfy `D_3 subset D_4,D_5`, with residual
sizes two and three beyond `D_3`.

- Residual overlap two is impossible: it would put four points of the
  support-five circuit into a rank-three proper subspace.
- With one shared residual point outside the support-three span, a
  six-dimensional space vanishes on the 36-point union.
- With one shared residual point inside that span, there is a flag
  `(33,8)<(36,5)`.
- With disjoint residuals, a five-dimensional space vanishes on a 37-point
  union; if the carriers are nested, its dimension rises to six.

The `(36,6)` and nested `(37,6)` branches pay.  The transverse `(37,5)`
branch remains slightly unsafe, and the `(33,8)<(36,5)` flag is the leading
unresolved cell.

## Exact split-section target

Let `I_4,I_5` be the first-match-deduplicated selected eleven-set incidences
of support-four and support-five circuits in the leading flag cell.  The
needed weighted census is

```text
21 I_4 + 15 I_5
 <= 20552964203529559475043545396584734873674935990.
```

Independent fixed-union caps give

```text
21 I_4 + 15 I_5
 <= 21195887396614969832992972237166204779857211620,
```

leaving the exact reduction

```text
642923193085410357949426840581469906182275630.
```

Even lowering both support-four and support-five completion budgets from 31
to 30 leaves a deficit of

```text
29448888899741560716988382745385742184901730.
```

Thus a uniform maximum drop is insufficient.  After dividing the common
36-point locator, the equality strata are two-dimensional residual pencils
with a common split degree-34 core and fully split degree-35 sections of a
five-dimensional residual polynomial space.  The next theorem must couple
these weighted strata without reusing a circuit through several owners.

## Upstream overlap

Upstream PRs `#1171` and `#1172` route rank-one pair anticodes and force a
rank-two common-factor terminal.  PR `#1173` pays an anchored transverse
rich-flat branch and emits a larger common-locator flag.  Its greedy
transversality mechanism and factor-flag language are useful candidate tools
for the K72 census, but its dimensions, ownership unit, and deployed row are
different.  It is motivation, not a logical dependency and not a proof of
the finite split-section target.

Primary and independently coded Modal replays pass for both new theorem
packets.  The full graph replay independently compiled 2,547 nodes and 7,581
edges, then passed reachability, status propagation, reference, and red-leaf
checks at 161 MB peak RSS.  Its exact generated SHA-256 is
`0a6222cd90014d82edb91940652ff3c3ed31cf51e7b51c81ac84479a2c07a60b`.

```text
result:                NARROWED K'=72 to a weighted split-section census
newly closed rows:     none
closed prefix:         10..71
remaining rank nine:  72..15528
new nodes:             2 PROVED, 1 TARGET
new premise:           K'=72 carrier-flag split-section census
critical status delta: none; exact evidence frontier refined at first wall
upstream delta:         none; #1173 recorded as a nondependency analogue
delta-star movement:   none
compute:               Modal replays, 58--60 MB peak RSS; negligible spend
next route action:     falsify or prove the weighted residual split-section census,
                       then replay the complete K'=72 carrier atlas
```
