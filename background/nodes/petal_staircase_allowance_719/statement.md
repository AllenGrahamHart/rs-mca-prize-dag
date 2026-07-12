# Exact petal staircase multiplicity allowance

- **status:** PROVED
- **scope:** the four official maximal petal rows

For `n in {2^41,2^42,2^43,2^44}`, the exact residual multiplicity that the
`n^6` petal allocation can place on the planted staircase column is

```text
floor(n^6 / C(n+6,6)) = 719.
```

Equivalently,

```text
719 C(n+6,6) <= n^6 < 720 C(n+6,6).
```

Thus the staircase branch cannot consume an unspecified `n^b` chart or
codeword multiplicity. Its complete joint inflation allowance is 719.

