# Proof - L1 Mersenne HNF order-one linear-color exclusion

Every root `x` of `L` is a root of `W^(m(p+1))-1`. Hence its color

```text
epsilon=x^(p+1)
```

lies in `mu_m`. On every official row, `p=-1 mod m`, so
`epsilon^p=epsilon^(-1)`.

Suppose for contradiction that

```text
E(W)=aW+b,       a!=0.                               (1)
```

The affine map is injective. The `H=m-2` distinct roots of `L` therefore
give `H` distinct colors. In particular there are at least three because
`H` is six or fourteen.

For any one of these colors, equation (OLC2) and (1) give

```text
x=(epsilon-b)/a,
(epsilon^(-1)-b^p)(epsilon-b)=a^(p+1)epsilon.        (2)
```

Multiply the second equation by `epsilon`. Every selected color is a root
of the quadratic

```text
-(b^p+a^(p+1))X^2+(1+b^(p+1))X-b.                  (3)
```

At least three distinct field elements satisfy (3), so the quadratic is
the zero polynomial. Its constant coefficient gives `b=0`, while its
linear coefficient then gives `1=0`, a contradiction. Thus no degree-one
interpolant exists. QED.
