# Cycle 148: rate-half `A=1` extremal resultant four-slack (2026-08-11)

## Nonzero resultant

Cycle 147 proves the full contracted locator `Q` and split biform `G` are
coprime. Their parameter resultant is therefore nonzero. Every classified
row supplies the full `e-2` common row roots, leaving degree

```text
d_A=0: 2e-5,
d_A=1: e-3
```

after the classified-row locator power is removed.

## Mandatory factors

Every zero-excess padded-heavy factor is common to the corresponding
vertical fibers. In the `d_A=0` profile, the exceptional row also supplies
exactly `e-3` off-line common points. Removing these factors from the
resultant leaves

```text
deg W_QG<=4+r_bad,
```

where `r_bad` is the total padding on positive-excess slopes. This formula
is identical in both `d_A` profiles.

Selected actual-support roots are transverse, so they consume exactly their
baseline intersection copy and no part of the four-slack quotient. Every
other tangency, repeated padding intersection, or unclassified common point
must fit inside `W_QG`.

## Burn-down

```text
result:                  PROVED extremal resultant four-slack
DAG delta:               +1 PROVED leaf
critical status delta:   none
compute:                 exact integer arithmetic only
new assumptions:         none
```

The extremal closing target is now concrete: eliminate positive-excess
padding or force at least `5+r_bad` additional intersection units. The
strict resultant remains larger and should be treated separately.
