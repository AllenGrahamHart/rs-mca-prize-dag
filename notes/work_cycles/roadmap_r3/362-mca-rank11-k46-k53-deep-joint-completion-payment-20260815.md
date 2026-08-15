# Cycle 362: MCA rank-11 K'=46..53 deep joint completion payment (2026-08-15)

Cycle 361 closed `K'=45` but left the simultaneous support-four/support-five
fallback leaf at `K'=46`.  The fallback was too coarse: it recorded only
`s_4>=6,s_5>=5`, although the joint carrier remains valid for every exact
pair with `s_4+s_5<q`.

## Cycle pins

```text
our start:       e95151ead0a4afa7bc0cede3de887442cc2b3204
our end:         cycle commit containing this record
canonical prize: 6ac775504aa7dd6489ae5175235084e270abf6d2
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170 at f2080254b669749eb15f9fd8fec0dd5e6e915433
```

## Upstream export

The three cycle-361 nodes were exported into draft PR #1170 as commit
`f208025`.  The upstream packet now pins 82 proved public nodes, independently
replays the `K'=45,46` product, and prints the first rank-nine wall at
`K'=46`.  The only failing check is the repository's unrelated Vercel
authorization status.

## Deep exact defects

For each record, let `M_4,M_5` be the exact maximum completion counts and
write

```text
s_4=q-M_4,       s_5=q-M_5.
```

The `(q+1)^2` exact pairs are disjoint and exhaustive.  Every pair retains
all inherited deletion and cross-support caps.  If `s_4+s_5<q`, the proved
joint zero carrier and support-four external charge also apply.  This
refines the old fallback/fallback branch without introducing a premise.

The other supports contribute `9*8*5*4*3*2=8640` raw branch vectors.  After
deduplication there are 1,182 distinct vectors and exactly nine
componentwise maximal vectors on each row `K'=46..54`.  Removing a dominated
vector is exact for the premium maximum because every deficit weight is
nonnegative and all later operations are cap intersections.

## Eight-row payment

Exhausting every exact pair against the nine maximal vectors gives, on every
row `K'=46..54`, the active branch

```text
s_4=s_5=floor((q-1)/2),       every other support fallback.
```

Rows `K'=46..53` have positive premium-ceiling margins and positive exact
component gaps.  The smallest gap is at `K'=53`:

```text
2503373059664320603163477388007627909210651834842589498907998.
```

At `K'=54`, the premium exceeds its safe ceiling by

```text
495611154275787830253977941644262122450512788,
```

and complete capacity exceeds demand by

```text
2477882110233058360154706764229180240778698202487636349407165.
```

Primary and independently coded replays agree on every Pareto vector,
defect-pair maximum, fixed capacity term, safe sign, and adjacent wall.

```text
result:                PROVED K'=46..53 component-row closure
newly closed rows:     46..53
closed prefix:         10..53
remaining rank nine:  54..15528
new nodes:             2 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced eight rows
upstream delta:         cycle-361 K'=45 packet exported to #1170
delta-star movement:   none
compute:               exact local arithmetic under 1 GiB cap; no Modal spend
next route action:     attack the balanced deep joint wall at K'=54
```
