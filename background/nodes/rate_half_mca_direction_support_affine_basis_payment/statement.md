# Direction-support affine-basis MCA payment

- **status:** REFUTED
- **refuter:** `rate_half_mca_affine_span_incidence_counterexample`

The asserted support-sensitive bound

```text
|Z| <= floor(P(R,r,e) M(K,r))
```

is false.  On the exact counterexample

```text
(R,d,K,r,e)=(99,20,1,1,80),
|Z|=31,
floor(PM)=22.
```

Every active ordered basis does meet the direction support.  The proof still
fails because its denominator inherited the false lower bound on the number
of incident ordered bases per slope.  The former official support walls are
retracted and retained only as arithmetic evaluations of an invalid bound.
