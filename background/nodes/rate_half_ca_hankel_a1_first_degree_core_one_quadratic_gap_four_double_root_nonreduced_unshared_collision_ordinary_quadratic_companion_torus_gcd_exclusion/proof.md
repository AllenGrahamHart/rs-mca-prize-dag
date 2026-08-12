# Proof

Let `Z` be one of the dense absolutely irreducible coincidence components
from the subgroup-coincidence router, of bidegree `(d_1,d_2)`, and let
`Zbar` be its smooth projective normalization. Its coordinate functions
`x,y` have degrees at most `d_2,d_1`. The arithmetic-genus and boundary
intersection bounds in `P^1 x P^1` give

```text
genus(Zbar)<=(d_1-1)(d_2-1),
|zeros/poles of x or y|<=2(d_1+d_2),
chi<=2d_1d_2.                                      (1)
```

Suppose first that `Z` is not a translate of a one-dimensional subtorus.
Then `x,y` are multiplicatively independent modulo constants. Their
differentials are nonzero because their degrees are below `P`. Apply the
audited Corvaja--Zannier theorem to

```text
u=x^N,       v=y^N.                                (2)
```

Every point of `Z(H^2)` contributes at least one to its gcd sum, so

```text
#Z(H^2)<=max{
  3(2N^2d_1d_2 chi)^(1/3),
  12N^2d_1d_2/P
}.                                                 (3)
```

For the `S_3` component, `d_1,d_2<=4` and `(1)` gives the exact upper
comparisons

```text
[3(2N^2d_1d_2 chi)^(1/3)]^3<=27648N^2<(3F)^3,
12N^2d_1d_2/P<=192N^2/P<3F.                       (4)
```

This contradicts its `3F` points. For a cyclic component,
`d_1,d_2<=2`, and similarly

```text
[3(2N^2d_1d_2 chi)^(1/3)]^3<=1728N^2<(3F/2)^3,
12N^2d_1d_2/P<=48N^2/P<3F/2.                      (5)
```

Thus every putative component would have to be a translated subtorus.

We now exclude that alternative. An irreducible translated subtorus in
`G_m^2` has an equation

```text
X^rY^s=k,       gcd(r,s)=1,                        (6)
```

with negative exponents interpreted in the Laurent coordinate ring.

In the `S_3` case, the unique off-diagonal component is invariant under
swapping `X,Y`. Equality of the two primitive-character cosets in `(6)`
forces

```text
(s,r)=+/-(r,s).
```

Both projections are nonconstant, so this leaves only the forms `XY=k` and
`X/Y=k` up to inversion. A generic degree-three fiber has three distinct
rows `x_1,x_2,x_3`, and the unique component contains all six ordered
off-diagonal pairs. Applying either relation to `(x_1,x_2)` and
`(x_1,x_3)` gives `x_2=x_3`, a contradiction.

In the `C_3` case, let `sigma` generate the deck group and consider one
orientation image

```text
P |-> (X(P),X(sigma P)).                            (7)
```

If its generic map degree is `q`, then `(6)` and `deg X=2` give

```text
q|r|=q|s|=2.                                      (8)
```

Primitivity forces `|r|=|s|=1`. Thus `(7)` satisfies either

```text
X(sigma P)=kX(P)       or       X(sigma P)=k/X(P). (9)
```

In the first case, a subgroup point gives `k in H`, while `sigma^3=1`
gives `k^3=1`. Since `H` has order `2^41`, `k=1`. In the second case,
applying the relation twice gives `X(sigma^2P)=X(P)`. Either way `X` is
invariant under a generator of the cyclic deck group. It must then factor
through the degree-three quotient `C -> P^1_t`, forcing its nonzero degree
to be divisible by three. This contradicts `deg X=2`.

Both monodromy cases are impossible. Hence no `(2,3)` companion exists.
Shapes B and D each contain such a companion, so only A and C remain. QED.
