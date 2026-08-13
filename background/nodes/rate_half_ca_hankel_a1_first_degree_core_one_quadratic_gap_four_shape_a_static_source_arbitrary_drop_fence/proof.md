# Proof

Choose distinct elements

```text
r_1,...,r_d,a in F\U
```

and put

```text
Q(X)=product_(i=1)^d(X-r_i),
G(X)=(X-a)^(n-q).                                   (1)
```

The field-size assumption permits this choice. Both polynomials are
nonzero on `U), `Q` is squarefree, and `G(r_i)!=0`. Thus every
weight in `(SDF2)` is nonzero.

For every polynomial `A` of degree at most `R-1), Lagrange
interpolation gives

```text
sum_(x in U) A(x)/L'(x)=[X^(R-1)]A(X).              (2)
```

For `0<=j<=d`,

```text
R_j=sum_x omega_xQ(x)x^j
   =sum_x G(x)x^j/L'(x)=0,                          (3)
```

because

```text
deg(GX^j)<=n-q+d=R-2-q<=R-2.
```

Equation `(3)` proves that the coefficient vector of `Q` lies in
`ker M`.

We next prove that this is the complete kernel. On polynomials of degree
less than `d`, consider

```text
beta(P,S)=sum_(x in U)omega_xP(x)S(x).              (4)
```

Apply the residue theorem to

```text
G(X)P(X)S(X)/(Q(X)L(X)).
```

There is no residue at infinity: its denominator degree exceeds its
numerator degree by at least `q+4`. Therefore

```text
beta(P,S)
 =-sum_(i=1)^d
    G(r_i)P(r_i)S(r_i)/(Q'(r_i)L(r_i)).             (5)
```

Every diagonal coefficient on the right of `(5)` is nonzero.
Evaluation of degree-less-than-`d` polynomials at the `d` distinct
points `r_i` is an isomorphism. Hence `beta` is nondegenerate on that
space.

Every polynomial of degree at most `d` has a unique expression

```text
cQ+P_0,       deg P_0<d.                            (6)
```

Equation `(3)` puts `Q` in the radical, while `(5)` makes the
restriction to the complementary space nondegenerate. Thus the radical
is exactly `span{Q}`, proving `(SDF3)`.

Finally, for `s>=0`,

```text
R_(d+1+s)
 =sum_x G(x)x^(d+1+s)/L'(x).                       (7)
```

If `s<q`, the polynomial in `(7)` has degree at most `R-2`, so
`(2)` makes the sum zero. At `s=q`, its degree is exactly `R-1`
and its leading coefficient is `lc(G)`. Equation `(2)` gives the
last assertion in `(SDF4)`. QED.
