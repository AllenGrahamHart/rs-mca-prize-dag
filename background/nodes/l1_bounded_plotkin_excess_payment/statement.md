# L1 bounded Plotkin-excess payment

- **status:** PROVED
- **role:** pay every bounded layer above the joint Plotkin boundary
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Use the combined constant-weight sets from
`l1_joint_plotkin_boundary_payment`. Put

```text
V=N+b,       E=V-4ell.                                  (PX1)
```

If `E>=0`, every exact petal-support/defect-degree cell has at most

```text
2^(E+1)(V-E)=2^(E+3)ell                                (PX2)
```

compatible contributors.

Consequently, for every fixed petal-polarity cap `p<=P` and Plotkin-excess
cap `E<=E_0`, the aggregate is polynomial per source chart. An explicit
bound at the L1 lower cutoff is

```text
2^(E_0+1)(P+1)n^(1/c_0+P+2).                           (PX3)
```

The region `E<0` is already paid by the Plotkin-boundary theorem. Therefore
a bounded-polarity per-chart counterfamily must satisfy

```text
N+b-4ell -> infinity.                                  (PX4)
```

For an official rate-`1/r` source, the exact numerator identity is

```text
(r-1)E
 =(M-3(r-1)+1)ell-r(g+1),       g=ell-b.                (PX5)
```

Thus future source-scale work must have this slack escape every fixed cap;
mere strictness in the Plotkin gate is insufficient.

## Scope

This is a per-source-chart fixed-support payment. It does not count
unbounded Plotkin excess, growing petal polarity, or non-intrinsic
first-match chart multiplicity.
