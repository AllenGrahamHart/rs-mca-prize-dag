# Proof

Let `Xbar` be the smooth projective normalization of `(QLG1)` over the
algebraic closure of the official base field, and retain `x,y` as its two
coordinate functions. The curve has bidegree `(3,3)`, so

```text
deg x=deg y=3,       genus(Xbar)<=4.                 (1)
```

Let `S` be the union of the zeros and poles of `x` and `y`. Each degree-three
function has at most three distinct zeros and three distinct poles. Hence

```text
|S|<=12,       chi=|S|+2 genus(Xbar)-2<=18.          (2)
```

The coordinate functions are multiplicatively independent modulo
constants. Otherwise `x^r y^s=q` for nonzero `(r,s)`, so the irreducible
curve would be a toral binomial. This contradicts the two-dimensional
Newton support of `(QLG1)`, which always contains

```text
(3,1), (2,2), (1,3), (0,0).                         (3)
```

Put

```text
u=x^N,       v=y^N.                                  (4)
```

Then `u,v` remain multiplicatively independent. Their degrees are `3N`.
Their differentials are nonzero: `p` does not divide `N`, and the
degree-three coordinate maps are separable because `p>3`.

Corvaja and Zannier's positive-characteristic gcd theorem, quoted in
`source.md`, gives

```text
sum_(z outside S) min{ord_z(1-u),ord_z(1-v)}
 <=max{
   3(2 deg(u)deg(v)chi)^(1/3),
   12 deg(u)deg(v)/p
 }.                                                   (5)
```

Every affine point of `(QLG1)` in `mu_N x mu_N` lifts to a point outside
`S` and contributes at least one to the left side. By `(1)--(4)`, the two
terms on the right are at most

```text
3(2*(3N)^2*18)^(1/3)=3*324^(1/3)N^(2/3),            (6)
108N^2/p.                                            (7)
```

Both are strictly smaller than `2(e-148)`. For `(6)`, cube the positive
quantities to obtain the exact integer comparison

```text
27*324*N^2 < [2(e-148)]^3.                           (8)
```

For `(7)`, use `p>2^167` and verify

```text
108N^2 < 2^167*2(e-148).                             (9)
```

Thus `(QLG1)` has fewer than `2(e-148)` ordered subgroup points. The
degree-four router requires both orientations of `e-148` distinct matched
pairs, a contradiction. The final alternatives follow from the
antiweight, degree-two/three, irreducible, and reducible routers. QED.
