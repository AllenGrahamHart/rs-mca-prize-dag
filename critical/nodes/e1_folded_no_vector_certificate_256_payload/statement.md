# e1_folded_no_vector_certificate_256_payload

- **status:** TARGET
- **closure:** proof or certificate

## Statement

Over the named field from `e1_pocklington_250bit_exhibit_field`, using the
displayed primitive `256`th root, construct a complete machine-checkable
folded-kernel certificate proving that no nonzero non-cyclotomic vector

```text
w in {-2,-1,0,1,2}^128
```

satisfies the `N'=256` folded kernel equation.

The certificate must be tied to the exact field/root constants and must
include a proof log, exact checker, or imported off-laptop certificate whose
local replay is light.

## Falsifier

A nonzero non-cyclotomic folded vector in the displayed `N'=256` field/root,
or an incomplete/noisy transcript that does not certify all of
`{-2,-1,0,1,2}^128`.
