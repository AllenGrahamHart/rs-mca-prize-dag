
# Cycle 357: MCA rank-11 K'=41 sharp isolated-incidence payment (2026-08-15)

Cycle 356 left an exact capacity excess at `K'=41`.  The first attack on
completion saturation exposed a stronger loss earlier in the route: the
dense-locator component theorem still used generic bidegree Bezout to allow
198 isolated records on every eleven-set.

## Cycle pins

```text
our start:       ffb120ecd3200489fd6e6464ce0e916dad04596a
our end:         cycle commit containing this record
canonical prize: 6ac775504aa7dd6489ae5175235084e270abf6d2
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170 at 768e95bb74fec99e40cad8144ac8ce4568263f9f
critical census: 167 PROVED / 37 CONDITIONAL / 27 TARGET
```

## Rank-stratified isolated cap

For one eleven-set, evaluation rank at most nine leaves a nonzero correction
kernel, so every compatible record point lies on a positive-dimensional
affine fiber.  At rank ten, ten coordinate equations give

```text
q(Z)R=U_0+Z U_1.
```

After substitution, the eleventh equation is linear in `Z`.  It is either
identically zero, producing the affine-owner component, or has at most one
retained slope root.  Since retained slopes are distinct and avoid `Z(q)`,
actual isolated incidence is at most

```text
C(n',11),
```

not `198 C(n',11)`.  Thus exact component demand is

```text
R C(m',11)-C(n',11).
```

## K'=41 payment

Every capacity term from Cycle 356 is retained unchanged.  At the residual
record floor, the sharpened demand and complete capacity are

```text
demand   =914185087092839732068202094579173634339667328332842235009045152
capacity =910225257243846741169120022645139013735502214295549192982298326
gap      =  3959829848992990899082071934034620604165114037293042026746826.
```

The cleared record coefficient and floor-record cross are positive, so the
contradiction persists above the record floor.  The same exact payment first
fails at `K'=42` by capacity excess

```text
2710771376158610722953158157862051010402433288229120154217278.
```

The discarded shortcut was to treat pairing a circuit label with received
values as a support-independent quotient functional.  Different sparse
representations of one polynomial functional need not agree on arbitrary
received words, so no `q-2` completion cap was claimed.

```text
result:                PROVED K'=41 component-row closure
newly closed row:      41
closed prefix:         10..41
remaining rank nine:  42..15528
new nodes:             2 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced one row
upstream delta:         not yet exported; #1170 is the natural packet
delta-star movement:   none
compute:               exact local arithmetic and a tiny finite-field audit
next route action:     attack the exact K'=42 deficit through the weighted
                       completion vector or another genuinely shared resource
```
