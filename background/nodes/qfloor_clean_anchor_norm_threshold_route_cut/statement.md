# Qfloor clean-anchor norm-threshold route cut

- **status:** PROVED
- **closure:** proof plus exact arithmetic

At the six clean candidate predecessors, the canonical quotient parameters
required by `qfloor_exact` are

| rate | `N'` | `ell'=rho N'+1` | bit length of `(2ell')^(N'/2)` |
|---:|---:|---:|---:|
| `1/4` | `256` | `65` | `899` |
| `1/8` | `256` | `33` | `774` |
| `1/16` | `512` | `33` | `1548` |

The table is identical at RowC and prize scale. Every threshold exceeds
`2^256`, whereas every official row has characteristic
`p<=q<2^256`. Consequently no clean candidate predecessor can satisfy the
strict norm hypothesis

```text
p > (2ell')^(N'/2)
```

of `qfloor_exact`.

The raw counts `binom(N',ell')=binom(N',N'-ell')` exceed the corresponding
RowC and prize budgets on all six rows. They remain quotient-multiplicity
evidence, but this proved theorem cannot turn them into distinct ambient MCA
slopes. A different injectivity/value-set theorem, such as the open direct-E1
route, is required.

This is a route cut. It is not a safety certificate and does not upper-bound
the true quotient value set.
