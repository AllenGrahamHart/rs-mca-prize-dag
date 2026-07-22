# Audit

## Checked axes

1. `phi` is monic and selected fibers are complete, so `V_E(phi)` is the
   exact full-fiber locator.
2. The partial template is fixed before coefficient bucketing.
3. The denominator in `(MP2)` is the field size to power `t`.
4. The strict degree gate is checked after the first `t` coefficients cancel.
5. Distinct quotient sets give distinct monic locators and codewords.
6. Monicity of the center proves boundary-only behavior.
7. The extension-field conclusion uses all `A` roots in the base domain.
8. The `F_17` agreement and error sets are exact, not subsets.
9. Both agreement and error prefixes differ while the partial remainders
   agree.
10. The consequence is a target-count requirement, not a refutation of
    every possible prefix adapter.

## Route effect

Upstream PR `#1041` cannot be consumed as a payment. Its portable theorem
instead sharpens the L1 target: common-template quotient families are real,
and the arbitrary-word residual is a fixed-syndrome multiprefix incidence.
The next positive theorem must bound the complete attained-image sum or give
a chronology-valid owner decomposition.
