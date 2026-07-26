# e1_folded_certificate_cell_256_payload

- **status:** CONDITIONAL
- **closure:** conditional on no-vector certificate

## Statement

The `N'=256` E1 folded-certificate cell is reduced to the proved common field
choice plus the remaining no-vector certificate.

The named field is

```text
p = 904625697166646869347790708689937759412227977745095982970820953353127723009,
rho_256 = 368095729527972287347366462180303065908636718991804826343652948937354262881.
```

The field and primitive root are proved by
`e1_pocklington_250bit_exhibit_field`; the schema assembly is proved by
`e1_named_field_folded_cell_certificate_soundness`. The remaining predicate is
`e1_folded_no_vector_certificate_256_payload`, which must provide a complete
folded kernel certificate proving that no nonzero non-cyclotomic

```text
w in {-2,-1,0,1,2}^{128}
```

satisfies the `N'=256` folded kernel equation over the displayed field/root.

## Falsifier

A failed field/root check, a nonzero non-cyclotomic folded vector in the
displayed `N'=256` field/root, or an incomplete certificate transcript.
