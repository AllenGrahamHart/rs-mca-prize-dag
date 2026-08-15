# Cycle 360: MCA rank-11 K'=44 branch-lattice payment (2026-08-15)

Cycle 359 left one explicit support-five defect-two branch active at
`K'=44`, with support-five defect three only slightly below the safe premium
threshold.  This cycle refined both leaves by support-six completion maxima.

## Cycle pins

```text
our start:       9c5cf1b564c405558538a6c325a61be1fefbeba5
our end:         cycle commit containing this record
canonical prize: 6ac775504aa7dd6489ae5175235084e270abf6d2
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170 at 6e8e563dde5956320b78f8486cbe2bd958615d32
```

## Branch-lattice refinement

Any valid cap branch can be refined at another source support `c`.  Its
completion maximum lies in exactly one of

```text
M_c=q-s for 0<=s<=9-c,       or       M_c<=q-(10-c).
```

Every child inherits every parent cap.  Terminal children add the source
ceiling and valid cross-support carriers; the fallback child adds its source
ceiling.  Thus one parent is replaced by `11-c` exhaustive leaves.

At source support six there are four terminal defects and one fallback.
Replacing the two expensive support-five leaves changes the census from

```text
27-2+2*5=35 leaves.
```

## K'=44 payment

After cap intersection and full deficit weighting, the largest premium is
the nested source-five defect-two / source-six defect-two leaf:

```text
40318474413130846902399237147930487840413149400.
```

Keeping every chart, kernel, and shadow term gives

```text
demand   =914632087688377144021446114681200227193194740473705158570542108
capacity =914096453278432212124943531506920798021655606781504193772003859
gap      =   535634409944931896502583174279429171539133692200964798538249.
```

Both the record coefficient and floor-record cross are positive.  Replaying
the same 35 leaves at `K'=45` fails by capacity excess

```text
5651502053446174523626296867091469400380654135040887972894842.
```

The nested defect-two/defect-two leaf remains active at `K'=45`; simply
deepening unrelated fallback leaves cannot improve it.

```text
result:                PROVED K'=44 component-row closure
newly closed row:      44
closed prefix:         10..44
remaining rank nine:  45..15528
new nodes:             2 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced one row
upstream delta:         K'=43 and K'=44 results pending extension of #1170
delta-star movement:   none
compute:               exact local arithmetic; four guarded verifier passes
next route action:     refine the active c5-s2 / c6-s2 leaf at K'=45
```
