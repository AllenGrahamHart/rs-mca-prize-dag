# L1 m=4, h=3, nu=0 zero-b value-coset certificate

- **status:** PROVED
- **dependency:** `l1_m4_h3_mason_defect_budget`
- **consumer:** `l1_mixed_petal_amplification`

Assume `nu=0` and `b=0`. Choose `s!=0` with `s^2=-a`, so the three split
values are `0,s,-s`. Put

```text
r=R(0),       z=s/r,
u=1-z,        v=1+z.                                  (ZVC1)
```

The products of the three complete fibers show that

```text
u,v in K,       u+v=2,       u,v not in {0,1},       u!=v,   (ZVC2)
```

where `K` is the order-`n=4(p+1)` subgroup. Put

```text
epsilon=u^(p+1),       eta=v^(p+1) in mu_4.
```

Every valid pair is a common root of

```text
2U^2+(eta-epsilon-4)U+2epsilon=0,
U^(p+1)=epsilon,
(2-U)^(p+1)=eta.                                      (ZVC3)
```

Exact quotient-ring certificates for all 16 quarter pairs give

```text
p=8191,131071:      only (1,1), whose root u=1 is degenerate;
p=524287,2147483647: valid (1,-1),(-1,1), with both
                      quadratic roots in each case.   (ZVC4)
```

Consequently

```text
p in {8191,131071}: no nu=0,b=0 record;
p in {524287,2147483647}: every nu=0,b=0 record obeys
                          a^2+3aR(0)^2+R(0)^4=0.       (ZVC5)
```

This does not exclude the latter zero-`b` arm, treat either nonzero-`b`
endpoint, classify positive valuation or wider `m`, or close L1.
