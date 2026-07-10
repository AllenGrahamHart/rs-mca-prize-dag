# e1_folded_certificate_cell_128_payload

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONDITIONAL]
- **closure:** conditional on no-vector certificate

## Statement

The `N'=128` E1 folded-certificate cell is reduced to the proved common field
choice plus the remaining no-vector certificate.

The named field is

```text
p = 904625697166646869347790708689937759412227977745095982970820953353127723009,
rho_128 = 440266185830122294862552098878717819794821358702875176198798016633729926114.
```

The field and primitive root are proved by
`e1_pocklington_250bit_exhibit_field`; the schema assembly is proved by
`e1_named_field_folded_cell_certificate_soundness`. The remaining predicate is
`e1_folded_no_vector_certificate_128_payload`, which must provide a complete
folded kernel certificate proving that no nonzero non-cyclotomic

```text
w in {-2,-1,0,1,2}^{64}
```

satisfies the `N'=128` folded kernel equation over the displayed field/root.

## Falsifier

A failed field/root check, a nonzero non-cyclotomic folded vector in the
displayed `N'=128` field/root, or an incomplete certificate transcript.
