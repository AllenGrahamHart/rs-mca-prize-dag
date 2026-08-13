# Proof

For every coordinate and slope,

```text
r_0+gamma(r_1-b)=c_gamma-gamma b
```

is equivalent to `r_0+gamma r_1=c_gamma`.  Thus every exact and maximal
agreement support is identical before and after gauging.

If `(p_0,p_1)` explains `(r_0,r_1)` on a support, then `(p_0,p_1-b)`
explains `(r_0,r_1-b)` there.  Adding `b` gives the inverse map, so
same-support pair containment and noncontainment are equivalent.

Fix an anchor slope `gamma_0`.  The transformed difference vectors are

```text
(c_gamma-c_gamma0)-(gamma-gamma_0)b.
```

Their span lies in the original difference span plus `<b>`.  Conversely,
each original difference lies in the transformed difference span plus
`<b>`.  The two affine dimensions therefore differ by at most one.

No incidence estimate is used.  The former rank-payment paragraph is
retracted by `rate_half_mca_affine_span_incidence_counterexample`.
