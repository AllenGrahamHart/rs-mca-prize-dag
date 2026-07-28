# Proof

By the square-mass reparametrization, one class is represented by a signed
singleton vector `x in {0,+/-1}^h`. If `t_x=|supp(x)|`, the class-size
condition is exactly

```text
t_x<=T,                   t_x=ell (mod 2),
```

because the number of full antipodal pairs is then uniquely
`(ell-t_x)/2`. The locations of those full pairs do not change the E1 class.

Fix an oriented difference `d=x-y` with profile `(a,b)`. At every coordinate
with `|d_i|=2`, the ordered pair `(x_i,y_i)` is forced and both supports gain
one. At each of the `b` coordinates with `|d_i|=1`, there are two choices:
the nonzero entry belongs to `x` or it belongs to `y`. If `j` of them belong
to `x`, this contributes `binom(b,j)` choices.

There are `n0=h-a-b` zero coordinates of `d`. On each such coordinate the
pair is `(0,0)`, `(1,1)`, or `(-1,-1)`. If exactly `r` common nonzero
coordinates are selected, there are `binom(n0,r)2^r` choices. The two support
sizes are consequently

```text
t_x=a+j+r,                t_y=a+b-j+r.
```

Retaining exactly the terms for which both support sizes satisfy the class
condition gives the displayed formula for `M_ell(a,b)`. Every construction
is unique coordinate by coordinate, so there is neither omission nor
overcounting.

The classes collide modulo `p` exactly when

```text
sum_i (x_i-y_i) zeta^i = sum_i d_i zeta^i = 0 (mod p).
```

Thus summing `M_ell(a(d),b(d))` over `D_p(ell)` counts all ordered low-mass
colliding class pairs. Every unordered pair occurs twice, once with `d=x-y`
and once with `-d=y-x`; also `M_ell(a,b)=M_ell(a(-d),b(-d))`. Division by two
proves the exact edge identity.

For the ledger, enumerate all integer profiles with `a,b>=0`, `a+b<=h`,
`0<4a+b<=2ell`, and positive multiplicity. The norm-radius theorem permits
only `S>=16` in the `b>0`, `N=256` branch and `S>=4` in the `b>0`, `N=512`
branch. In the all-even branch it permits only `a>=15` and `a>=4`,
respectively. Exact binomial evaluation gives the profile counts and maxima
in `statement.md`. Finally,

```text
E_low <= M_max |D_p(ell)|/2,
```

so `|D_p(ell)|<=floor(2E_max/M_max)` implies the corresponding proved edge
budget. The verifier recomputes every integer and checks the next uniform
count is no longer certified by this inequality.
