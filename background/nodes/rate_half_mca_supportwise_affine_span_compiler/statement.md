# Support-wise affine-span MCA compiler

- **status:** REFUTED
- **refuter:** `rate_half_mca_affine_span_incidence_counterexample`

The printed claim that exact same-support pair noncontainment can replace
the direction-separation hypothesis while preserving the affine-span bound
is false.  In fact the exact `GF(1009)` counterexample also satisfies the
original direction-separation hypothesis:

```text
(n,K,m,w,s)=(100,1,21,20,1),
|Z|=31,
claimed bound=23,
max_(c in C) agr(r_1,c)=20<m.
```

Every selected explanation has maximal agreement support exactly 21, every
support is pair-noncontained, and the explanation affine span is exactly one.

The valid local conclusion is only that the incident normals on each
selected witness span the parameter space.  The rejected proof additionally
needed a uniform bound on how many incident normals can lie in each proper
subspace.  Neither pair noncontainment nor the printed direction-separation
hypothesis supplies that bound.

The former KoalaBear and Mersenne small-dimension payments are retracted.
Their numerical products remain arithmetic records, not proved slope bounds.
