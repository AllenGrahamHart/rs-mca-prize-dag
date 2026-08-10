# Active balanced-core source-witness compiler

- **status:** PROVED
- **row:** deployed KoalaBear MCA at agreement `1116048`
- **unit:** source-bound certificates projecting to distinct affine slopes

For every admissible received line, instantiate the named
`HAS_ACTIVE_V4_BALANCED_CORE_CERTIFICATE` predicate by the explicit decidable
certificate relation in `certificate_schema.json`. Its data include:

```text
received-line id; affine slope; explaining data;
active shifted interpolation lattice and canonical reduced basis;
degree-981104 split locator and selected support;
earlier-owner exclusions; balanced-core depth w=67471;
first-match chronology and selector labels.
```

After the tangent and Q cells, `Z_BC` is exactly the slope projection of
valid certificates. The certificate universe is finite. Selecting its
lexicographically first member for each slope gives exactly one selected
certificate per `Z_BC` slope, and the certificate stores the slope itself.
Thus selected certificates and `Z_BC` are in bijection and every selector
fiber has multiplicity one. The original line, slope, and support are fields,
not reconstructed labels.

This node gives semantic content to the previously symbolic `bcCertified`
predicate. It does not prove that a certificate satisfies the legacy
`Q=6,s=6,u=2` equality-wall hypotheses, construct an endpoint component,
bound the number of `Z_BC` slopes, or pay a slope.

## Falsifier

A mismatch between the instantiated predicate and schema validity, failure
of finite canonical selection, two selected certificates for one slope, or
loss of any stored datum.
