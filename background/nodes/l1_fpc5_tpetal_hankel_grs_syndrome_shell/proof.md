# Proof: FPC5 Hankel charts are exact GRS syndrome shells

Let `G=X^d+sum_(a<d)g_aX^a` have support `S`. The incoming support theorem
gives unique amplitudes `w_x`, `x in S`, such that

```text
mu_a=sum_(x in S) w_x x^a,       0<=a<d.             (1)
```

Put `nu_a=sum_x w_xx^a`. Since `G(x)=0` on `S`, the sequence `nu` obeys

```text
nu_(r+d)+sum_(a<d)g_a nu_(r+a)=0                     (2)
```

for every `r>=0`. Membership in the FPC5 Hankel chart says that `mu` obeys
the same recurrence for `0<=r<c`. Starting from the `d` equalities in `(1)`,
induction in `r` therefore gives

```text
mu_a=nu_a,       0<=a<D=d+c.                         (3)
```

With `e_x=w_x/v_x`, equation `(3)` is exactly `H_D e=mu`. The incoming
primitive identity says that every `w_x` is nonzero, so `wt(e)=d`.

Conversely, let `e` have weight `d` and syndrome `mu`. Put
`S=supp(e)`, `w_x=v_xe_x`, and `G=product_(x in S)(X-x)`. The moment
representation `mu_a=sum_xw_xx^a` makes every one of the `c` locator
recurrences vanish. Every `w_x` is nonzero, so the incoming Cramer-amplitude
criterion makes `G` primitive. The degree-`d` Vandermonde system makes the
amplitudes unique for a fixed support, proving the bijection `(GS4)`.

Suppose `D<N`. The weighted Vandermonde matrix `H_D` has rank `D`. For every
polynomial `P` of degree below `N-D`, the Lagrange leading-coefficient
identity gives

```text
sum_(x in C) P(x)x^a/L_C'(x)=0,       0<=a<D.
```

Thus `RS[F,C,N-D]` lies in `ker H_D`; both spaces have dimension `N-D`, so
they are equal. Surjectivity supplies a word `y` with syndrome `mu`, and
`H_De=mu` is equivalent to `y-e` belonging to that code. This proves
`(GS5)--(GS6)`.

If `D>=N`, the first `N` rows of `H_D` form an invertible diagonally weighted
Vandermonde matrix. Hence a syndrome has at most one preimage `e`, and the
fixed chart has at most one primitive locator.

Finally, for two distinct shell errors `e,e'` in the `D<N` case, their
difference is a nonzero word of the `[N,N-D,D+1]` GRS code. Therefore

```text
D+1 <= wt(e-e') <= |supp(e) union supp(e')|
    =2d-|supp(e) intersect supp(e')|,
```

which is `(GS7)`. QED.
