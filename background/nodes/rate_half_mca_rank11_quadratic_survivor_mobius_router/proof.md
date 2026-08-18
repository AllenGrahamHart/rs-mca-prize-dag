# Proof

The mass router already gives the high-complexity output or one synchronized
pair type with `r>=4370` pairwise-disjoint split exception locators of one
degree `e in {1,...,11}`. There is nothing to prove when `e!=2`, so assume
`e=2` and write

```text
D_i(X)=(X-x_i)(X-y_i)=X^2-s_i X+p_i.
```

The fixed pencil is two-dimensional. Its locators are distinct monic
quadratics, and at least two occur, so their span is exactly two-dimensional.
The proved pair-locator Mobius dichotomy applies. Hence there are base-field
scalars `a,b,c` satisfying

```text
b*x_i*y_i+a*(x_i+y_i)=c,       Delta=a^2+b*c!=0,     (1)
```

and one nonidentity involution

```text
phi(x)=(c-a*x)/(a+b*x)                              (2)
```

interchanges `x_i,y_i` for every `i`. The coefficient points `(s_i,p_i)`
and their affine line are base-field rational, so `(1)` can be chosen over
the base field; no closure-field descent is required.
The involution is unique: two disjoint pairs prescribe the images of four
distinct points, while a projective linear transformation is determined by
its action on any three.

Suppose first that `b=0`. Then `a!=0`, and `(2)` becomes

```text
phi(x)=c/a-x=s-x.
```

Equation `(1)` says every locator is `X^2-sX+p_i`, the normalized affine
reflection pencil. The mass router selected a pencil outside the nonzero
affine class, hence `s=0`. This is the antipodal class.

Now suppose `b!=0`. Put

```text
tau=a/b,       kappa=Delta/b^2.
```

The determinant condition gives `kappa!=0`. Directly from `(2)`,

```text
phi(x)+tau
 = [b(c-a*x)+a(a+b*x)]/[b(a+b*x)]
 = (a^2+b*c)/[b^2(x+tau)]
 = kappa/(x+tau).                                   (3)
```

If `a=0`, then `tau=0` and `phi(x)=kappa/x`. One selected pair lies in the
official multiplicative subgroup `H`, so `kappa=x_i y_i` lies in `H`.
This is the constant-product quotient class.

If `a!=0`, then `tau!=0` and `(3)` is the shifted-inversion class. Every
selected pair contributes its two distinct roots to

```text
{x in H: x!=-tau, phi(x) in H, phi(x)!=x}.
```

The `r` pairs are disjoint, so these contributions are distinct. Their
number is at least `2r>=8740`. The three coefficient cases are exhaustive,
and all unpriced outputs have been retained. QED.
