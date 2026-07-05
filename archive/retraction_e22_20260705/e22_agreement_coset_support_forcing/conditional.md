# conditional: e22_agreement_coset_support_forcing

## Predicate nodes

- `e22_agreement_cofactor_equations`
- `e22_cofactor_coset_saturation`

## Claim

Conditional on coset saturation for the cofactor equations, the E22 agreement
equations force tail-plus-coset support.

## Proof

The proved cofactor-equation predicate takes an arbitrary listed E22
sunflower codeword, factors its zero agreements, and rewrites every petal
agreement as

```text
U(x) L_{Z\C}(x) = a_i L_{C\Z}(x).
```

Thus no information is lost by studying the cofactor equations on the touched
petals.

The remaining coset-saturation predicate has now been reduced to divisor
gluing. The pointwise equations are first translated into petal-locator
divisibility constraints. The active open component is local quotient-factor
extraction; once that is supplied, the proved fiber-locator lemma gives local
full-fiber blocks and the proved dyadic gluing lemma turns those blocks into
saturation on full fibers of one quotient map `x -> x^M` with `M > t`. That
is exactly the advertised fixed-tail plus full-quotient-fibers support form.

Therefore the support-forcing statement follows from these two predicates.
