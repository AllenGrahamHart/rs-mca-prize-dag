# Dimension-two quotient incidence exclusion

- **status:** PROVED
- **scope:** the scalar-dimension-two output of the quotient pair-pencil
  router

Let `H_p` be the 520 or more quotient pair cores, each of size
`s=m-2=1116046`. In scalar dimension two, each coordinate is of exactly one
of the following kinds:

1. a common-gcd coordinate, lying in all 520 cores or in none; or
2. a noncommon coordinate, whose core owners lie in one affine scalar line
   and therefore number at most 15.

The all-core set has size at most `K-1=1048575`. Consequently the total core
incidence is at most

```text
520*(K-1)+15*(n-(K-1))=560987655.                   (IE1)
```

But the 520 cores require

```text
520*(m-2)=580343920,                                (IE2)
```

which exceeds `(IE1)` by `19356265`. Scalar dimension two is impossible.
Together with the previous exclusion of dimension one and the dimension cap
four, the rational pair-pencil branch now has scalar dimension three or four.

## Falsifier

A noncommon coordinate lying in cores from more than 15 scalar types; a
common-core size above `K-1`; or failure of the exact incidence contradiction.
