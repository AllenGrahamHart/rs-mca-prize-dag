# F3 h=3 frontier ledger

Status: REPLAYED FRONTIER LEDGER, NOT `H3-ACT`, NOT `RC-RANK`.

This packet compiles the current h=3 proof surface for the F3 flip brief.  It
imports the activation-bound compiler, official bridge-budget tables, the
rank-effective bridge repair, the conic bridge accounting ledger, the
L2/level-set bridge compiler, the exact-profile bridge contract, and the h=3
repeat-boundary frontier ledger.  It does not prove a new rank theorem or a new
geometric batching theorem.

## Frontier Gates

```text
H3-ACT-COMPILER: REPLAYED/CONDITIONAL
  C=16 would imply T3<n^3 from n>=17.  The n=96 all-core evidence has
  720 oriented activation records over 82 threshold primes, with maximum
  92 oriented activations at p=37633.  The activation orbit-dedup replay
  reduces the same list to 167 affine/Galois pair-orbits, with maximum
  27 deduped orbits at one prime and no repeated canonical orbit across
  threshold primes.
  Residual: prove H3-ACT(16), or replace it with official-row activation
  certificates.

F3-RANK-AVOID / RC-NV: OPEN
  The non-diagonal official-row arithmetic covers s=13..41 with
  Z_budget=16..10795.  The older diagonal bridge-budget table is only
  11..7420 and is retained as a legacy lower bound.
  The exact rich-curve reduced-condition profile now records
  `DA+6D(D-1)` conditions per repaired curve, about `7.84%..8.77%`
  of the legacy `13D(A+D)` count on the sample boxes.
  Feeding this exact profile into the bridge-budget optimizer gives the
  alternate conditional budget `Z_exact=33..21421`, with total gain `51451`
  over the active non-diagonal table.
  The exact-profile rank-capacity guard verifies that, on these official
  boxes, a degree-space-full repaired image has capacity exactly `1` and the
  constant-ratio collapsed model has capacity `0`; the larger budget therefore
  buys more distinct rank-effective images, not duplicate-image reuse.
  The exact-profile rank-deficit budget shows that a bounded-deficit theorem
  with `rank >= (L+1)-Delta` and `Delta <= 1847` would already suffice for all
  official exact-profile boxes.
  The conic-chart large-gap pilot checks the same actual same-fiber conic chart
  in three larger-gap boxes `H=20,24,32`; its deficits are `27,1,0`, far below
  the official exact-profile tolerance `1847`, while official rows have
  minimum `H/A = 4096/681`.
  The conic binary-form target reduction restates the exact-profile conic rank
  theorem as codimension `<=1847` inside binary forms of degree
  `(A-1)+6H(B-1)`; the pinned chart quadratics have span rank `3`.
  The six-A guardrail records that all official exact-profile rows have
  `H-6A >= 20`, but it also refutes the unrestricted claim that `H>=6A` alone
  implies full conic rank outside the official dense-box regime.
  The conic rational-curve interface restates the map as
  `H0(O(A-1))` times boxed degree-`3(B-1)` monomials in four sections of
  `O(2H)`; official rows have positive column-supply margin, but the four
  generators are not a complete linear series.
  The conic-chart linear-relation guard verifies `P_U+P_V+P_W+aQ=0` on the
  same-fiber conic chart despite pairwise coprime chart polynomials, so
  separated-divisor arguments alone cannot prove full rank.
  The rank-good open set is now witnessed inside the actual same-fiber conic
  chart family in the toy row: the conic chart
  `p=769,a=37,b=706,base=(101,333)` has rank `320=A B^3`, certified by a
  concrete minor with determinant `514 mod 769`.
  Residual: prove finite-row rank-good minor nonvanishing on repaired
  degree-2 signature-curve images.

H3-BRIDGE-RANKCAP: OPEN
  The bridge must count rank-effective capacity units, not raw duplicate
  curves.  Pinned toy capacities are collapsed=0, private=3, random=4.  The
  conic bridge accounting ledger proves that different base points in the same
  same-(e1,e2) fiber are not new conic images; the exact local L2 target is
  sum_z R_z(R_z-6) <= 1152 n, equivalently P_total <= 16 n.
  The exact-profile bridge contract records that Z_exact=33..21421 is a
  distinct-rank-effective-image budget and not an L2 pair-count bound.
  Residual: assign activated non-toral shape pairs to repaired chart images
  within the official rank-capacity budget.

F3-PRIVATE-LINEAR-RANK-AVOID: OPEN/ALTERNATE
  The retuned private-linear arithmetic covers s=13..41 with
  Z_private=23..15267.  Every official private-linear passing witness has
  max(A,D,B-1)<H with margin at least 7904.  The private-linear rank-deficit
  budget shows that a bounded-deficit theorem with
  `rank >= A+3H(B-1)-Delta` and `Delta <= 25` would already suffice for all
  official private-linear boxes; the tight row is `s=16`.
  Residual: prove finite-row minor nonvanishing on the private-linear
  three-parameter normal-form image, plus the matching private-linear bridge.

H3-REPEAT-BOUNDARY-STAR: OPEN FRONTIER
  The repeat-boundary frontier ledger replays seven strict branch gates:
  H3-VALUE-GEN-INJECTIVE, H3-VALUE-SCALE-INJECTIVE, H3-SLOPE-GG-HIT,
  H3-SLOPE-MIXED-HIT, LOOSE-GEN-RANK/NV, LOOSE-A-RANK/NV, and LOOSE-B-RANK/NV.
  On the count route, H3-VALUE-SCALE-INJECTIVE is replaced by the paid
  scale-collision ledger, leaving six still-open strict gates.  The scale
  ledger now uses the minimum of the trivial orbit bound and the h=2
  affine-coset cap; the h=2 cap first improves the bound at `n=2^19`.
  The same-lambda J-invariant compiler identifies the generic off-orbit
  degree-10 product as `-numerator(J(z)-J(y))`, where
  `J(z)=(1+z+z^2)^3/(z^2(1+z)^2)`.
  The slope equality-factorization compiler verifies that the generic and
  mixed slope gates are exactly coordinate-intersection targets after
  denominator clearing, with product totals 41 and 27 respectively.
  The loose branch-geometry compiler verifies that branch B is the
  fixed-parameter complement of branch A, `b_B(a)=-1-b_A(a)`, that finite
  branch-map ramification is killed by reciprocal-multiplier distinctness, and
  that the clean branches share six of their eight unique slope maps.
  The shared-core degree split records this common six-map target with
  `S_total=14`, leaving private two-map tails with `S_total=8` on branch A and
  `S_total=10` on branch B; the full clean branch totals remain `22` and `24`.
  The shared-core rank-target compiler gives a sample-box count-route target
  with rank target `1049`, entry degree `1359`, minor degree at most
  `1425591`, point bound `1087/2`, and rank-capacity slack `40`.
  Residual: prove or replace the strict same-lambda, slope, and loose-triangle
  branch gates needed by the star route.
```

## Use In The F3 Brief

This ledger keeps T1/T2 honest.  The strongest current degree-2 route is the
exact-profile route:

```text
RC-RED-PROFILE + F3-RANK-AVOID-EXACT
  + H3-BRIDGE-RANKCAP-EXACT(Z_exact)
  => H3-ACT(16)
  => T3 < n^3 on all official rows.
```

Here `Z_exact=33..21421`, and the bridge must spend those units on distinct
rank-effective repaired images because the official exact-profile boxes have
one-image degree-space capacity `1`.

The companion exact-profile bridge contract also keeps this rank-family route
separate from the L2/level-set route: the L2 target remains
`sum_z R_z(R_z-6) <= 1152n`, not a consequence of `Z_exact` alone.

The legacy degree-2 route remains valid but weaker:

```text
RC-RED(13) + F3-RANK-AVOID + H3-BRIDGE-RANKCAP
  => H3-ACT(16)
  => T3 < n^3 on all official rows.
```

The private-linear route is a separate alternate:

```text
F3-PRIVATE-LINEAR-RANK-AVOID + H3-BRIDGE-PRIVATE-RANKCAP
  => H3-ACT(16),
```

but it must use the private-linear degree cap and `Z_private` table.  It cannot
be mixed with the degree-2 non-diagonal compiler.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
```

Expected digest:

```text
H3_FRONTIER_LEDGER_PASS
```
