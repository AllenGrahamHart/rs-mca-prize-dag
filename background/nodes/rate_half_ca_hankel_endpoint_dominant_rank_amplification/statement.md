# Dominant-component rank amplification at the strict endpoint

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Retain the official strict-endpoint factorization over the algebraic closure

```text
Q=product_i Q_i,       deg_(U,V) Q_i=e_i,
sum_i e_i=m,
```

and let `sr(-)` denote separation rank across the
`X | (U,V)` coefficient split.  For every component `Q_i`,

```text
sr(Q_i)>=ceil((m+1)/(m-e_i+1)).                        (DRA1)
```

In particular, let `Q_*` be the unique defect-one dominant component and put

```text
b=m-e_*.
```

The component-defect ledger and the exact full-generator rank give

```text
sr(Q_*)>=ceil((m+1)/(b+1))
        >=ceil((m+1)/(floor((O-E)/4)+1))
        >=5.                                          (DRA2)
```

Thus the live dominant component has geometric separation rank at least
five, not merely at least three.  If there is no residual component (`b=0`),
then `Q_*=Q` and its rank is exactly `m+1`.  More generally, the lower bound
in `(DRA2)` grows as the exact omission-overlap budget `O-E` shrinks.

This excludes every rank-three and rank-four mixed model for the dominant
component.  It does not classify rank-five-or-higher biforms or close the
endpoint rational-normal incidence problem.
