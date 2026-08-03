# Proof

## A fixed tuple on the full affine hull

Choose affine coordinates `c=(c_1,...,c_s)` on `A`. At a point `x in D`,
the error vector has the form

```text
V_x(c)=E_x+lambda_x(c)W_x,       W_x=(-Q(x),P(x)),  (1)
```

where `lambda_x` is affine linear. The invariant active residual gives
`det(E_x,W_x)!=0`, so `V_x(c)` never vanishes.

Fix points `x_0,...,x_s` with distinct `phi` values. Membership in one
selected block implies

```text
F_i(c)=det(V_(x_0)(c),V_(x_i)(c))=0,
1<=i<=s.                                             (2)
```

These are `s` polynomials of degree at most two on affine `s`-space. The
affine Bezout inequality bounds the sum of the degrees of all irreducible
components of their common zero set by `2^s`. One can see this directly by
intersecting successively: a component contained in the next quadric keeps
its degree, while every other component produces intersections of total
degree at most twice its degree. Thus there are at most `2^s` irreducible
components, including isolated points.

Let `C` be a positive-dimensional component and let `rho` be the common ray
of the vectors in `(2)`. If `rho` were nonconstant, then on the projective
normalization of `C` each `lambda_(x_i)` would be a Mobius function of
`rho`, with its unique pole at `[W_(x_i)]`. The `s+2` affine functions

```text
1,lambda_(x_0),...,lambda_(x_s)
```

belong to the `(s+1)`-dimensional space of affine-linear functions on `A`,
so they have a nontrivial linear dependence. Pulling it back to `C` and
looking successively at the `s+1` distinct poles kills every nonconstant
coefficient, then the constant coefficient. This is a contradiction.

Hence `rho` is constant on every positive-dimensional component. The
high-depth same-ray interaction strip permits at most one target parameter
on such a component. Isolated target parameters are already isolated
components. The component-degree bound therefore proves `(FAT1)`.

## Tuple incidence

For one `r`-point selected block, choose points in order while avoiding the
at most `ell` points in each previously used `phi` fiber. The number of
unordered `(s+1)`-tuples with distinct `phi` values is at least

```text
product_(j=0)^s(r-j ell)/(s+1)!.                    (3)
```

Every target has at least two disjoint selected blocks. A fixed tuple belongs
to at most one block of a fixed target, and `(FAT1)` caps its target owners by
`2^s`. Double counting gives

```text
2|Tau| product_(j=0)^s(r-j ell)/(s+1)!
 <=2^s binom(e,s+1),                                (4)
```

which is `(FAT2)`. If `ell=1`, every fiber has size at most one, so the block
count is exactly `binom(r,s+1)` and `(FAT3)` follows.

## Official arithmetic

Put `x=d+1`. Then `e<=x-3` and `r=h-x+1`. The right side of `(FAT3)` is at
most

```text
C_s(x)=2^(s-1) product_(j=0)^s(x-3-j)
                    /product_(j=0)^s(h-x+1-j).      (5)
```

It is strictly increasing wherever the factors are positive because

```text
C_s(x+1)/C_s(x)
 =((x-2)/(x-s-3))*((h-x+1)/(h-x-s))>1.             (6)
```

The verifier evaluates `(5)` by exact integer cross multiplication at the
two last-paid values in the statement and at their successors. The former
are below `B_0` and the latter above it. Monotonicity proves the two claimed
intervals. QED.
