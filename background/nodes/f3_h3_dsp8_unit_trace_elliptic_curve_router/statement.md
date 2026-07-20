# DSP8 unit-trace elliptic-curve router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependency:** `f3_h3_dsp8_unit_product_trace_normal_form`

In the unit-product normalization, choose one residual root from each
decorated triple. The first triple is

```text
(r,u,(ru)^(-1))
```

and has trace `sigma` exactly when `(r,u)` lies on

```text
C_sigma: r+u+(ru)^(-1)=sigma.                        (EC1)
```

Its projective closure is the plane cubic

```text
X^2Y+XY^2-sigma XYZ+Z^3=0.                           (EC2)
```

Over every field of characteristic different from `2,3`:

1. `C_sigma` is smooth, geometrically irreducible, and has genus one when
   `sigma^3!=27`;
2. when `sigma^3=27`, it has one ordinary node at
   `[sigma/3:sigma/3:1]`, no other singularity, and geometric genus zero.

Let `G_25^c` count raw normalized tuples

```text
(r,u,s,x,z,w)                                         (EC3)
```

in class `c`, with `(r,u)` and `(s,x)` on the same `C_sigma`, completed roots
`v=(ru)^(-1)`, `y=(sx)^(-1)`, all original DSP8 signed-disjointness,
nonidentity, richness, and class predicates, and

```text
t=1+rs(r+s-sigma),       1-w=t(1-z).                 (EC4)
```

Then internal residual-root ordering gives the exact ledger

```text
G_25^c=4K_25^c=J_25^c.                               (EC5)
```

Thus DSP8 is a quotient-line-weighted pair count on a one-parameter family of
mostly elliptic subgroup trace curves. The exact target remains

```text
10G_25^0+17G_25^A<=892n^2.                           (EC6)
```

This router supplies no point-pair estimate. In particular, the upstream
same-`(e1,e2)` rational-conic chart does not parameterize `(EC1)`: DSP8 fixes
`(e1,e3)=(sigma,1)`, and the generic trace fiber has genus one.
