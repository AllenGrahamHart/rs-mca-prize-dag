# L1 m=4, h=3, nu=0 zero-b Euler exclusion

- **status:** PROVED
- **dependencies:** `l1_m4_h3_nu0_zero_b_value_coset_certificate`,
  `l1_m4_h3_euler_quotient_factorization`
- **consumer:** `l1_mixed_petal_amplification`

Assume `nu=0` and `b=0`. The value-coset certificate already excludes
`p=8191,131071`. On either remaining characteristic, put `r=R(0)`. Then

```text
a^2+3ar^2+r^4=0.                                      (ZBE1)
```

The Euler quotient identity cancels its factor `R` to give

```text
2aDXR'=H(R^2+a)-4alpha.                               (ZBE2)
```

At each of the `p` simple roots of the split fiber `R`, differentiation of
the domain identity and `(ZBE2)` imply

```text
H=12alpha/a.                                          (ZBE3)
```

Evaluating `(ZBE2)` at zero then forces

```text
a/r^2=-3/2.                                           (ZBE4)
```

Substitution in `(ZBE1)` gives `-5/4=0`, impossible on the official
characteristics. Thus the entire `nu=0,b=0` endpoint is empty. Together with
the nonzero-`b` and positive-valuation exclusions, the official
`m=4,h=3` branch is empty on all four rows.

This does not classify nonembedded `h=2`, treat `m=8,16`, wider exchanges,
or close the full L1 node.
