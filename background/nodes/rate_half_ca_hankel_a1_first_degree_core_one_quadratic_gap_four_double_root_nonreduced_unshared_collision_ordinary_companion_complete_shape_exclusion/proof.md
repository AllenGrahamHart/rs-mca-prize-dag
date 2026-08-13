# Proof

Shapes B and D contain `(2,3)` companions and are already excluded by the
quadratic-companion torus-gcd theorem. It remains to remove shape C.

Let `C` be the normalization of `Q=0`. The deck-involution router supplies
a nonidentity involution `sigma` of `C -> P^1_t`, acting on the row
coordinate as `X |-> -X` or `X |-> k/X`, with `k in H`. Its graph is one
geometric off-diagonal component of `C times_(P^1_t) C`.

There are at least `F_6=3e-14` slopes for which `Q(delta,X)` has six
distinct roots in `U_0`. A deck transformation acts freely on such an
unramified fiber. Thus `sigma` partitions its six roots into three pairs,
and exactly six of the thirty ordered off-diagonal pairs have second
coordinate `sigma(x)`. The remaining twenty-four ordered pairs do not lie
on the graph of `sigma`.

For a fixed ordered row pair `(x,y)`, the two nonzero quartics
`Q(t,x),Q(t,y)` have at most four common roots. Hence the residual
fiber-product components contain at least

```text
24F_6/4=6F_6=P_res                                  (1)
```

distinct points of `H^2`. A connected separable degree-six cover has at
most five geometric off-diagonal components, so after deleting the graph
of `sigma` there are at most four.

Every row-coordinate image is contained in the divided resultant locus
of bidegree at most `(20,20)`. Suppose that no residual component carrying
one of the points counted in `(1)` has translated-subtorus image. On the
normalization of each such image, the Euler-characteristic bound is at
most `800`. The Corvaja--Zannier theorem bounds its `H^2` points by the
maximum of the same cube-root and characteristic terms used in the
deck-involution router. Each term is strictly below `P_res/4`, because

```text
64*17280000*N^2 < P_res^3,
4*4800*N^2 < 2^167 P_res.                           (2)
```

The union of at most four components would then contain fewer than
`P_res` counted points, contradicting `(1)`. Therefore a residual
component carrying an actual `H^2` point has image

```text
X^aY^b=c,       gcd(a,b)=1.                         (3)
```

Let `W` be its normalization, let `h_1,h_2` be the degrees of the two
projections `W -> C`, and let `q` be the degree to the image `(3)`. The
common parameter function has degree `6h_i`, so `h_1=h_2=:h`. The row
coordinate has degree four on `C`; comparison of the two coordinate maps
in `(3)` gives

```text
q|a|=q|b|=4h.                                       (4)
```

Primitivity forces `|a|=|b|=1`. Relation `(3)` then assigns a unique
second row to a generic first row, so `h=1`. The component is the graph of
a nonidentity deck transformation

```text
eta(X)=cX       or       eta(X)=c/X.                (5)
```

Its counted `H^2` point gives `c in H`. It is distinct from `sigma`, since
the graph of `sigma` was removed, and distinct from the identity, since
the diagonal was removed in the divided resultant.

Let `D` be the deck group of `C -> P^1_t`. It acts freely on a generic
six-point fiber, so `|D|` divides six. A scaling `X |-> cX` in `D` has
order dividing both `|H|=2^41` and `|D|`, hence a nonidentity scaling is
`X |-> -X`.

If `sigma(X)=-X`, a scaling eta either is the identity or equals sigma,
both excluded. A reciprocal eta commutes with sigma, and the two distinct
involutions generate a subgroup of order four.

If `sigma(X)=k/X`, a nonidentity scaling eta is `X |-> -X`, commutes with
sigma, and again generates a subgroup of order four. If eta is reciprocal,
say `eta(X)=c/X`, then `c!=k` and `eta sigma` is the nonidentity scaling
`X |-> (c/k)X`. Its order divides both a power of two and `|D|`, so it has
order two. The two distinct involutions therefore commute and generate a
subgroup of order four.

Every case contradicts `|D|` dividing six. Shape C is impossible. Combining
this with the quadratic-companion exclusions for B and D leaves exactly
shape A in the four-shape classification, with the record `(OCX5)`. QED.
