# Cycle 487: cross-type pole-simple atom identity

## Result: PROVED identity threshold 16

Two pole-simple scalar-locator certificates sharing `r>=16` supports are
projectively identical whenever at least three shared supports come from
each of two distinct saturated pair types.

For independent scalar coefficient pairs, denominator-root incidence gives

```text
|G\H|>=ceil((rm'-n')/(r-1)).
```

Near-sunflower incidence puts this set in both pair cores. The official
margin is `-2605` at `r=15` and `+2067` at `r=16`, so 16 is the exact first
threshold for this argument.

For proportional scalar pairs, normalize the pairs to equality. Subtraction
cancels the locator term. A nonzero denominator difference puts all shared
explanations on one global affine codeword line, contradicting the presence
of two distinct pair types with two slopes each. A zero difference forces
the remaining coefficients to agree.

## Burn-down

```text
starting local pin:       dbb221f8a
canonical prize pin:      0dd5b3244
upstream frontier pin:    PR #1173 at 2788d5ec3
DAG delta:                +1 PROVED identity node, +4 edges
critical status delta:    none
closed interface:         compatibility of sufficiently overlapping atoms
compute spend:            none
next action:              construct cross-type decks with at least 16 supports
```

## Nonclaims

- no shared-deck construction;
- no canonical atom over a complete family;
- no quotient owner payment, high-complexity payment, or MCA closure.
