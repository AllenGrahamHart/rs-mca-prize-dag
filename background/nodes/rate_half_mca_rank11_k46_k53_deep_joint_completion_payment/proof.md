# Proof

Fix `K'` in `46..54`, put `q=K'-10`, and retain the baseline cap vector,
all kernel coranks, the all-core rank-nine chart, the full 55-shadow deficit
ledger, and sharp isolated demand from the preceding payment.

The deep defect partition supplies `(q+1)^2` exact support-four/support-five
pairs.  The remaining supports `2,3,6,7,8,9` retain respectively

```text
9,8,5,4,3,2
```

terminal/fallback alternatives, for `8640` raw vectors.  Intersect every
child with every inherited cap.  Duplicate vectors are identified.  If one
vector is componentwise below another, nonnegative deficit weights and any
later cap intersections make it no larger, so it is safely discarded.  On
each row exactly nine maximal other-support vectors remain.

For exact pair `(s_4,s_5)`, use source deletion ceilings `q-s_4,q-s_5` and
all valid terminal cross-support caps.  If `s_4+s_5<q`, intersect support
four with the joint external-carrier charge; otherwise use no joint cap.
Exhausting all exact pairs against the nine maximal vectors gives the active
branch

```text
s_4=s_5=floor((q-1)/2),       all other supports fallback.       (1)
```

The exact premiums and safe-ceiling margins at the last safe row are

```text
premium(53) =
40141995068282471040632276636969794558475239350,

ceiling(53)-premium(53) =
500709701466164598631229888808678512345658964.
```

For every row, combine the certified premium `P` with the unchanged
rank-nine marks `G` and record floor `R` as

```text
full-rank capacity=floor((G+R P)/55).
```

Adding every kernel-corank capacity and comparing with

```text
R C(m,11)-C(n,11)
```

gives positive gaps throughout `46..53`; the minimum is the printed `K'=53`
gap.  The cleared record coefficient and floor-record cross are positive on
all eight rows, so the contradiction persists above the record floor.

At `K'=54`, the same exhaustive computation again selects (1), with
`s_4=s_5=21`, but its premium exceeds the exact safe ceiling by

```text
495611154275787830253977941644262122450512788.
```

The resulting capacity excess is the wall printed in the statement.  QED.
