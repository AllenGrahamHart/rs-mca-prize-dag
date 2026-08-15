# Cycle 361: MCA rank-11 K'=45 full completion-product payment (2026-08-15)

Cycle 360 left the nested support-five/support-six defect-two leaf above the
`K'=45` premium ceiling.  Refining only higher supports did not close it.
This cycle coupled the terminal support-four and support-five carriers, then
replayed the complete Cartesian product of all completion maxima.

## Cycle pins

```text
our start:       ba9dc04e52505f6c42639f8692ab1abcf78b9b77
our end:         cycle commit containing this record
canonical prize: 6ac775504aa7dd6489ae5175235084e270abf6d2
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170 at 62b63a52a3e01d6086ba3e2333d4fdb21350a180
```

## Joint zero carrier

For terminal support-four/support-five defects `s_4,s_5`, their vanishing
spaces have dimensions seven and six.  If their intersection had the
Grassmann-minimal dimension three, the two spaces would sum to all of `V`.
The common-root bound and `q>s_4+s_5` force their source carriers to overlap,
contradicting the no-common-zero hypothesis.  Hence the intersection has
dimension at least four and the carrier union has size at most `q+6`.

Closing this intersection under all common zeros gives a carrier `B` with

```text
4<=t=dim H_B<=6,
delta=K-t-|B| in [0,min(s_4,s_5)].
```

For every independent support-four deletion, Grassmann and the root bound
then leave at most `delta+3` points of its whole completion carrier outside
`B`.

## External support-four charge

If a support-four circuit has exactly `j` points outside `B`, deleting one
of those points leaves `j-1` external deletion points and at most
`delta+4-j` external completions.  Each such circuit is charged exactly `j`
times.  This proves the four-stratum cap

```text
C(b,4)+sum_(j=1)^4 floor(
  C(b,4-j) C(m-b,j-1) (delta+4-j)/j
),
```

with the stronger `C(b,4)` cap at `delta=0`.  At the formerly active
`s_4=3,s_5=2` leaf, the selected incidence cap is

```text
32578977236967057729773689331510654377703052,
```

versus the previous independent cap

```text
518691078344615652006898851983705727784314240.
```

## Full completion product

The support `c` completion maximum has `11-c` disjoint alternatives.  Their
full product over `c=2..9` has `9!=362880` leaves.  Of these, `259200` have
both support-four and support-five terminal and are eligible for the joint
cap; the cap actually tightens `48384` leaves.

Without the joint cap, the maximum premium remains unsafe at

```text
41119280132819537082584175767452500583010727727.
```

With it, the terminal-pair maximum falls to

```text
30915047166299259953679561401812508774596279777,
```

and the global maximum moves to the all-fallback branch:

```text
40126324034612056409620566967689123241580103372.
```

The exact safe ceiling is

```text
40449741059808005650840187255316169911744988527.
```

Complete demand therefore exceeds capacity by

```text
1616971801308361526826641488053709685917408248376428345137933.
```

An independent implementation replayed all `725760` leaves across `K'=45`
and the negative-control row `K'=46`.  At `K'=46`, the all-fallback branch
exceeds the ceiling and capacity exceeds demand by

```text
5057508862309072579343840146913199075599800084788396842011438.
```

```text
result:                PROVED K'=45 component-row closure
newly closed row:      45
closed prefix:         10..45
remaining rank nine:  46..15528
new nodes:             3 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced one row
upstream delta:         K'=45 structural and payment packet pending #1170 extension
delta-star movement:   none
compute:               exact local streaming arithmetic under tiny RAM guard
next route action:     attack the all-fallback completion branch at K'=46
```
