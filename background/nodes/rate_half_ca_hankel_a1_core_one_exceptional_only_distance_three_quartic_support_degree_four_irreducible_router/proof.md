# Proof

Put `G=mu_N`, where `N=2^41`, and normalize any degree-four rational map by
a target Mobius transformation as

```text
psi=S/R,       deg S=4,       S(0)!=0,       deg R<=3.   (1)
```

The same two-dimensional linear-algebra argument as in the degree-three
reduction supplies this form: take `R` in the kernel of the leading
coefficient functional and choose `S` outside that line and the kernel of
evaluation at zero. Scale `S` to be monic. Write

```text
S=X^4+s_3X^3+s_2X^2+s_1X+s_0,
R=r_3X^3+r_2X^2+r_1X+r_0,       s_0!=0.             (2)
```

The off-diagonal coincidence polynomial

```text
C(X,Y)=[S(X)R(Y)-S(Y)R(X)]/(X-Y)                    (3)
```

has bidegree at most `(3,3)`. Its two boundary rows are

```text
[Y^0]C=(s_1r_0-s_0r_1)+(s_2r_0-s_0r_2)X
       +(s_3r_0-s_0r_3)X^2+r_0X^3,                 (4)

[Y^3]C=r_0+r_1X+r_2X^2+r_3X^3.                    (5)
```

Suppose `C` is absolutely irreducible. If `r_0!=0`, independent inversion
of `X` and `Y` gives the published estimate's nonzero corner and nonconstant
boundary unless `R` is constant and `s_1=s_2=s_3=0`. In that exception

```text
C=r_0(X^3+X^2Y+XY^2+Y^3),                           (6)
```

which is geometrically reducible, contrary to the assumption.

If `r_0=0` and at least two of `r_1,r_2,r_3` are nonzero, one of `(4)--(5)`
again has an endpoint and another nonzero coefficient after independent
coordinate inversion. Thus the published estimate applies directly with
bidegree at most `(3,3)`:

```text
#C(G x G)<=16*3*3^2*(3+3)N^(2/3)=2592N^(2/3).      (7)
```

The exact official margin is

```text
2592N^(2/3)<2(e-148),                               (8)
```

contradicting the captured ordered pair count.

It remains to consider a monomial denominator `R=r_jX^j`, with
`j in {1,2,3}`. Scaling removes `r_j`. For `j=2`, equation `(3)` is

```text
X^3Y^2+X^2Y^3+s_3X^2Y^2-s_1XY-s_0(X+Y).            (9)
```

The determinant-minus-one subgroup automorphism

```text
X=U^(-1)V^(-1),       Y=V
```

followed by multiplication by `U^3V` turns `(9)` into

```text
1-s_0U^2-s_1U^2V+s_3UV+UV^2-s_0U^3V^2.            (10)
```

This has bidegree `(3,2)`, nonzero constant term, and nonconstant
restriction `1-s_0U^2` at `V=0`. The published bound is therefore

```text
960N^(2/3)<2(e-148),                                (11)
```

again impossible.

For `j=1`, division by `X` gives exactly `(Q4R1)` with
`a=s_3`, `b=s_2`, `c=s_1`, and `d=s_0`. Direct division in `(3)` gives
`(Q4R2)`. For `j=3`, precomposition by `X |-> X^(-1)`, which preserves
`G`, gives the same Laurent exponent interval from `-1` through `3`, with
nonzero end coefficient; a target scaling and relabeling gives `(Q4R1)`.
The additive constant cancels from the coincidence equation.

These Laurent-end cases are not covered by `(7)`: the smallest audited
unimodular corner transform has bidegree `(3,4)` and explicit constant
`5376`, which is larger than the official margin. They must be retained.
Together with the geometrically reducible case separated at the start, they
exhaust the degree-four branch. QED.
