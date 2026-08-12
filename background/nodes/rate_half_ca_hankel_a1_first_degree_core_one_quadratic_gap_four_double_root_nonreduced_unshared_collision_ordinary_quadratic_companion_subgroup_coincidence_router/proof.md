# Proof

The factorwise shape classification and row-saturation theorem give, for
every `x in U_0`, exactly two distinct roots of `Q(-,x)` in `Gamma`. Hence
`Q` has at least `2R` distinct `F_P`-points.

We first prove absolute irreducibility. The chosen primitive factor is
irreducible over `F_P(X)`. If it split geometrically, its two components
would be Frobenius-conjugate and would each have parameter degree one. Their
intersection number in `P^1 x P^1` is at most three, because their two row
degrees add to at most three. Every `F_P`-point would lie on both conjugate
components, contradicting `2R>3`. Thus `Q` is absolutely irreducible.

For two quadratics, direct expansion of the Sylvester determinant gives

```text
Res_t(Q(t,X),Q(t,Y))
 =[a(X)c(Y)-a(Y)c(X)]^2
  -[a(X)b(Y)-a(Y)b(X)]
   [b(X)c(Y)-b(Y)c(X)].                            (1)
```

Each bracket is alternating in `X,Y`, so division by `X-Y` gives `(QCR3)`
and `(QCR4)`. A divided wedge of two degree-three polynomials has bidegree
at most `(2,2)`, proving the degree bounds.

Also `K_Q` is nonzero. Otherwise fix a generic `x_0` for which
`Q(t,x_0)` has two roots `alpha,beta`. The resultant identity would give

```text
Q(alpha,Y)Q(beta,Y)=0
```

identically in the integral domain over the algebraic closure. One factor
would vanish identically, making `t-alpha` or `t-beta` a constant linear
factor of `Q`, contrary to absolute irreducibility.

Now count the coincidence points forced by row saturation. There are

```text
2R=9e-7                                               (2)
```

incidences between `U_0` and `Gamma`. Since `deg_X Q<=3`, a slope has at
most three distinct incident rows. Relative to the capacity `3|Gamma|`,
the total vertical defect is therefore

```text
3(3e)-(9e-7)=7.                                      (3)
```

Consequently at least

```text
F=3e-7=2^39-6                                       (4)
```

slopes have three distinct incident rows. Every such triple supplies six
ordered off-diagonal pairs `(x,y) in U_0^2` on `K_Q=0`. A fixed ordered
pair can arise from at most two slopes, because the two nonzero row
quadratics have at most two common roots. Thus the reduced coincidence
locus contains at least

```text
3F=3(2^39-6)                                        (5)
```

distinct points of `H^2`.

Consider the separable degree-three map from the normalization of `Q=0`
to the `t`-line. Absolute irreducibility makes its geometric monodromy
transitive, so the monodromy is `S_3` or `C_3`.

In the `S_3` case, the action is transitive on ordered pairs of distinct
sheets. Hence the reduced off-diagonal fiber-product image is geometrically
irreducible. Its defining component divides `K_Q`, so it has bidegree at
most `(4,4)`, and it contains all points counted in `(5)`.

In the `C_3` case, the two ordered differences give the two orientation
images

```text
P |-> (X(P),X(sigma P)),
P |-> (X(P),X(sigma^2 P)).                          (6)
```

Each coordinate function in `(6)` has degree two. Therefore every distinct
image component has bidegree at most `(2,2)`. Each full fiber contributes
three ordered pairs to each orientation; again a pair is produced by at
most two slopes. Hence each distinct orientation component contains at
least `3F/2` points of `H^2`. If the two components were exchanged by
Frobenius, every such `F_P`-point would lie in their intersection. Bezout
limits that intersection to eight, whereas `3F/2>8`. Thus every distinct
orientation component is defined over `F_P`.

It remains to apply the published Vyugin--Makarychev subgroup-curve bound
recorded and audited in the official trigonal-subgroup dependency. For an
absolutely irreducible polynomial of bidegree `(m,n)` satisfying `(QCR5)`,
it gives

```text
#P_0(H x H)<=16mn^2(m+n)N^(2/3).                   (7)
```

The subgroup hypotheses hold throughout:

```text
100(4*4)^(3/2)<N,       N<P^(3/4)/3.               (8)
```

The second inequality follows from `P>2^167`. Swapping and inversion
preserve `H^2`, so `(7)` applies to every VM-admissible component.

For the `S_3` component, the worst bidegree-`(4,4)` constant is `8192`,
and exact cubing gives

```text
8192^3 N^2 < (3F)^3.                               (9)
```

This contradicts `(5)`. For a `C_3` orientation component, the worst
bidegree-`(2,2)` constant is `512`, and

```text
512^3 N^2 < (3F/2)^3,                              (10)
```

again a contradiction. Therefore none of the dense components just
described is VM-admissible. They all lie in the coordinate-corner
exceptional locus. QED.
