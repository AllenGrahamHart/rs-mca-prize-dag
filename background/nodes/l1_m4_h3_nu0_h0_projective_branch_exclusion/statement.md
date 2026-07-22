# L1 m=4, h=3, nu=0, h=0 projective branch exclusion

- **status:** PROVED
- **dependency:** `l1_m4_h3_nu0_nonzero_b_tangent_exclusion`
- **consumer:** `l1_mixed_petal_amplification`

Assume the surviving constant-eliminant endpoint

```text
nu=0,       b!=0,       deg H=0,
r=R(0),     A=a/r^2,    B=b/r^3.                     (PBE1)
```

Then the scalar equation from the dependency factors as

```text
(3B+2A)(9B-4A^2-6A)=0.                               (PBE2)
```

The first factor is impossible. Consequently every such record satisfies

```text
9B=4A^2+6A,
9bR(0)=4a^2+6aR(0)^2.                                (PBE3)
```

Thus the constant-eliminant endpoint has only one projective outer parameter;
the tangent-at-zero component `2aR(0)+3b=0` is empty. This does not exclude
the remaining component, construct or count its solutions, treat the cubic
eliminant, zero `b`, positive valuation, wider `m`, or close L1.
