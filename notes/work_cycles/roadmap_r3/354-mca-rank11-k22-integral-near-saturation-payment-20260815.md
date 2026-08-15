
# Cycle 354: MCA rank-11 K'=22 integral near-saturation payment (2026-08-15)

Cycle 353 left an exact capacity excess of
`2859529280846211417198922209345618432657212793529140162369036` at
`K'=22`.  Three independent losses were separated rather than adding a new
conditional premise.

## Cycle pins

```text
our start:       e9a8a7680
canonical prize: 6ac775504a
upstream main:   93fba1be3f
open upstream:   #1170 at 03fa65a after the K'=14..21 export
```

## Integral heavy-owner chart cap

For a clean dominant split-pencil line, a heavy owner of weight `s` uses at
least `P-s` light mass.  Its contribution is at most

```text
ell phi(s),       phi(s)=(C(P,2)+rP)/(P-s)-s.
```

The function `phi` is increasing and convex.  For fixed owner count and
heavy budget, the maximum therefore has as many weights `P-1` as possible,
at most one residual weight, and all remaining weights `floor(P/2)+1`.
On each residual interval, the objective has second derivative

```text
2-2(C(P,2)+rP)D/(ell+D)^3,
```

so it changes curvature at most once.  Exact rational endpoint/derivative
certificates check 271 segments per core offset.  On all thirteen `K'=22`
cores, the maximum has eight owners of weight `P-1`.  The uniform complete
chart cap falls from `9287934561540848` to

```text
9269974099565290.
```

The exploratory Modal runs were `ap-whhK5VCyJHo7dPVZKZbD22` and the
thirteen-core parallel replay `ap-q8qyA84WGLchLaikEneQgL`; the proof and
local verifier use exact rationals and do not depend on floating point.

## Near-saturated circuit carrier

In the no-`q`-completion branch, suppose a support-`c` deletion has `q-1`
completions.  Their private-coordinate labels span a quotient hyperplane on
a carrier of size `q+c-2`.  For `c<=4`, adjoining one outside support-`c`
label spans the full quotient, and every further representation comparison
uses at most

```text
q+3c-2<=q+10=K'
```

evaluation points.  Vandermonde independence therefore confines every
support-`c` circuit to a carrier of size at most `q+2c-2`.  Otherwise every
deletion has at most `q-2` completions.  At `K'=22`, the latter maximum is
at `b=10`, lowering the weighted sparse premium by

```text
393439020925119039272226731095485935384019750.
```

Support five deliberately retains its old eleven-completion cap.

## Complete K'=22 payment

The payment also reuses the already proved uniform corank-one
projective-pair cap `8147918`, while retaining all other coranks.  The exact
capacities are

```text
kernel =
2273421575008467450492290640797843465217921029627020608340

full rank =
901790983907425884981637631119717314733273741651299178720895580

total =
901793257329000893449088123410358112576738959572328805741503920

demand =
903025989085629081334365478664955214394150391409598064684975031

gap =
1232731756628187885277355254597101817411431837269258943471111
```

The record coefficient and full unfloored cross are positive, so the
comparison persists above the residual record floor.

```text
result:                PROVED K'=22 component-row closure
newly closed row:      22
closed prefix:         10..22
remaining rank nine:  23..15528
new nodes:             3 PROVED
new premise:           none
compute:               two cheap Modal audits, replaced by exact local checks
next route action:     specialize the same integral/near-saturation ledger
                       to K'=23 and locate its next exact wall
```
