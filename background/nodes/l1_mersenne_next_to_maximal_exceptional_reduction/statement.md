# L1 Mersenne next-to-maximal exceptional reduction

- **status:** PROVED
- **dependencies:** `l1_official_max_split_value_complement_census`,
  `l1_mersenne_checkpoint_cyclotomic_normal_form`
- **consumer:** `l1_mixed_petal_amplification`

Let `m in {8,16}`, put `h=m-1`, and consider any official Mersenne row

```text
n=m(p+1),       h complete degree-p fibers.            (NMR1)
```

This covers

```text
m=8, h=7:    p=8191,131071,524287,2147483647;
m=16,h=15:   p=8191.                                  (NMR2)
```

Every such pencil, if one exists, lies in the following exceptional branch:

```text
nu=0,              H=q is a nonzero constant,          (NMR3)
T(Y)=hG(Y)-YG'(Y) has a nonzero root,
qG(y)=m alpha y for every nonzero root y of T.          (NMR4)
```

Every nonzero root of `T` is simple. For each one, `R-y` is squarefree,
all its roots are nonzero, and `gcd(R-y,D)=1`. In addition,

```text
deg T=h-2,                  deg(XR')=p-m.               (NMR5)
```

If `a=[Y^(h-2)]G` and `b=[X^(p-m)]R`, then `a,b!=0` and

```text
q=-2mab.                                                   (NMR5a)
```

Put `r=ord_0(T)` and let `S` be the monic nonzero-root factor of `T`.
Squarefreeness gives `r in {0,1}`. The polynomial

```text
B(Y)=(G(Y)-(m alpha/q)Y)/(Y^r S(Y))
```

is quadratic and satisfies

```text
B(R(0))=0.                                                (NMR5b)
```

This root of `B` is simple. Write the other root as `z`, and put

```text
a_0=deg rad(R-R(0)),       a_z=deg rad(R-z).
```

Then

```text
a_0+a_z=p+m+1.                                          (NMR5c)
```

Equivalently, the two fiber radicals consume all of `D` (after removing the
zero root from the first), while their two ramification gcds consume all of
`R'`.

After the affine target normalization

```text
F=(R-R(0))/(z-R(0)),
```

the exact residue is a degree-`p` polynomial Belyi map satisfying

```text
F(0)=0,                 deg F'=p-m-1,
D=rad(F)/X * rad(F-1),
F' proportional to gcd(F,F')gcd(F-1,F').              (NMR5d)
```

Every nonzero root of `F(F-1)` lies in the official multiplicative domain.

More precisely, for a nonzero root `y` of `T`, put

```text
kappa=m alpha y/G(y),       P_y=X^nu H-kappa.
```

If `P_y` is nonzero, then tangent multiplicity gives `p<=h^2`, contrary to
all rows in `(NMR2)`. Thus `P_y=0`, which is exactly the exceptional branch
above. If `T` has no nonzero root, squarefreeness forces

```text
G(Y)=Y^h+c,       or       G(Y)=Y^h+cY.                (NMR6)
```

The first form violates polynomial Mason--Stothers. In the second form,
Euler evaluation and an exact root-product packet leave at most one
normalized nonzero split value although `m-2` distinct values are required.
Hence both forms in `(NMR6)` are empty.

This is a reduction, not a closure of `h=m-1`. It leaves precisely the
exactly saturated Belyi branch `(NMR3)--(NMR5d)` and does not treat lower `h`,
nonembedded `m=4,h=2`, width above `p`, or full L1.
