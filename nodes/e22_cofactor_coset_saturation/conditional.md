# conditional: e22_cofactor_coset_saturation

## Predicate nodes

- `e22_cofactor_petal_divisibility`
- `e22_cofactor_divisor_quotient_gluing`

## Claim

Conditional on divisor-to-quotient gluing, the E22 cofactor equations force
non-tail roots to be saturated on full quotient fibers.

## Proof

The proved predicate `e22_cofactor_petal_divisibility` translates every
touched-petal cofactor equation into the divisor condition

```text
L_{T_i}(X) | U(X)L_{Z\C}(X) - a_i L_{C\Z}(X).
```

Thus the cofactor equations lose no information when expressed as petal
locator divisibility constraints.

The predicate `e22_cofactor_divisor_quotient_gluing` now assembles the
E22-specific quotient-factor extraction, the proved fiber-locator saturation
lemma, and the proved dyadic local-to-common saturation lemma. It supplies the
remaining support-forcing theorem: any E22 mixed/full-petal challenger
satisfying those divisor constraints has all non-tail roots saturated on full
fibers of a single quotient map `x -> x^M` with `M>t`.

Combining the exact translation with this gluing theorem proves the desired
coset-saturation statement.
