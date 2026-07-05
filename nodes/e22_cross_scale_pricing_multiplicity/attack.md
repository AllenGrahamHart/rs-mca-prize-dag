# ATTACK - e22_cross_scale_pricing_multiplicity

Use the canonical support-scale object from
`e22_cross_scale_support_canonical_form`:

```text
(R, admissible moduli M, recovered tails B_M, recovered selected fibers).
```

The dyadic representative-choice part is now proved in
`e22_dyadic_minimal_scale_selector`: use the minimal admissible quotient
modulus as the canonical representative.

The compatibility node is now conditional. The remaining work is
`e22_minimal_scale_column_evaluation`: count the proved minimal-scale
partition cells in the quotient staircase arithmetic column. A proof should
specify exactly one of:

- a proof that the column counts exactly the minimal-scale representative for
  each class; or
- an explicit multiplicity factor that the column includes and the consumer
  divides by.

The result must be compatible with `dyadic_profile_evaluation`; otherwise the
E22 pricing column can still overcount cross-scale duplicates.
