# XR higher-rank minimal-face syzygy dichotomy

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_higher_rank_uniform_split_pencil_reduction`

Use the uniform high-core split-pencil notation from the dependency. Thus the
kernel is normalized `GRS_a`, selected blocks have size `a+h` and pairwise
intersection at most `a`, and the selector has affine rank `s=a+1`.

Let `Lambda` be a rank-two dual-product-code trade whose active-coordinate
union `X` has the minimum possible size

```text
|X|=a+2.                                             (MF1)
```

If `t` is the number of active rows, then `4<=t<=a+2`. Every active row has
support exactly one facet

```text
S_i=X\{x_i},                                         (MF2)
```

and the omitted points `x_i` are distinct.

For a function `f` on `X`, write `[S]f` for its order-`a` divided difference
on an `(a+1)`-set. Put

```text
D_i=[S_i]q,       N_i=[S_i]U,
```

where `(U,q)` is the split-pencil pair. Exactly one of the following two
branches holds.

## Regular face-syzygy branch

Every selected `D_i` is nonzero. The colors satisfy

```text
gamma_i=N_i/D_i=(alpha+beta x_i)/(chi+delta x_i),
beta chi-alpha delta !=0.                            (MF3)
```

Let

```text
mu_i(y)=(y-x_i)/Lambda'_X(y),       y in X.          (MF4)
```

Then `mu_i` is the canonical dual-`GRS_a` word supported on `S_i`, and the
complete trade-coefficient space on these facets is

```text
ker (1; x_i; gamma_i; x_i gamma_i)_(i=1,...,t),
dim=t-3.                                             (MF5)
```

These are the arbitrary-rank Plucker face syzygies. They may be quotiented as
a known local relation space.

## Collapsed near-tangent branch

The unique degree-at-most-`a+1` interpolants to both `q|X` and `U|X` have
degree less than `a`. Equivalently,

```text
[X\{x}]q=[X\{x}]U=0       for every x in X.         (MF6)
```

After undoing the common-root normalization, the two received directions are
jointly `k+2` close to a codeword pair on the common support

```text
P_0 union X,       |P_0 union X|=k+2.               (MF7)
```

Thus this branch is tangent-paid when `h<=2`, and is an explicit
near-tangent defect of exactly `h-2` agreements when `h>=3`.

For the six current P-A rows, `h=n/scale_denominator+1`, so none is paid by
this observation alone:

```text
row                         h             h-2
RowC 1/4                    5               3
RowC 1/8                    5               3
RowC 1/16                   3               1
prize 1/4              2^33+1          2^33-1
prize 1/8              2^33+1          2^33-1
prize 1/16             2^32+1          2^32-1
```

There is no mixed branch with one or some, but not all, selected denominators
zero. Consequently, after quotienting the regular face-syzygy spaces, every
surviving rank-two uniform trade either has at least `a+3` active coordinates
or carries the common `k+2` near-tangent core `(MF7)`. This is a structural
dichotomy, not an aggregate slope payment.
