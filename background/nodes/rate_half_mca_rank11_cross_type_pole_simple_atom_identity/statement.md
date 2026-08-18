# Cross-type pole-simple atom identity

- **status:** PROVED
- **scope:** two pole-simple scalar-locator certificates on a shared deck of
  official KoalaBear exact supports

Let two scalar-locator certificates share `r>=16` distinct supports after a
common shortening by `c`. Suppose the shared deck contains at least three
records from each of two distinct saturated pair types. Then the two
certificates are projectively identical.

The threshold is exact for the incidence argument. If the scalar coefficient
pairs are independent, pole-simplicity forces

```text
|G\H| >= ceil((rm'-n')/(r-1)) = Z_r-c.
```

Every point of `G\H` belongs to both pair cores, while distinct-pair
uniqueness gives `|G\H|<=K'-1`. At the threshold,

```text
Z_15-(K-1) = -2605,
Z_16-(K-1) =  2067.                                  (AI1)
```

For the cross-packet deck sizes used downstream:

```text
r       19       22       25       28
margin  12968    20754    26594    31136.             (AI2)
```

If the scalar pairs are proportional, normalize them to equality. The
locator terms cancel. A nonzero denominator difference would put every
shared explanation on one global affine codeword line, and two records from
each pair type would identify both distinct pair types with that line. Hence
the denominator difference is zero, and two slopes force the remaining
certificate coefficients to agree.

This theorem does not produce a shared deck or pay a family of identical
atoms.

## Falsifier

An independent-scalar survivor at `r>=16`; failure of the threshold or
shortening arithmetic; a proportional-scalar nonidentical pair whose shared
explanations do not lie on one affine line; or two distinct saturated pair
types identified by two slopes on the same parameterized codeword line.
