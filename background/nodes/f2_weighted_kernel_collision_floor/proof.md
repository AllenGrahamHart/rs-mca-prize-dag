# Proof

Every ordered subset pair `(S,T)` has a unique disjoint difference and
common intersection:

```text
eps=1_(S\T)-1_(T\S),  U=S intersect T.
```

The pair is a syndrome collision exactly when `eps in K`. For a fixed
ternary kernel word, the common intersection is arbitrary on its
`m-wt(eps)` zero coordinates. Therefore

```text
sum_v N(v)^2
 = sum_(eps in K intersect {-1,0,1}^m) 2^(m-wt(eps))
 = 2^m Z(A),
```

proving `(FLOOR-1)`. The diagonal pairs `S=T` give
`sum_v N(v)^2>=2^m`, hence `Z(A)>=1`. The image of `A` has `p^d` points,
so Cauchy--Schwarz and `sum_v N(v)=2^m` give

```text
sum_v N(v)^2 >= 4^m/p^d.
```

Division by `2^m` proves `(FLOOR-2)`.

For `(FLOOR-3)`, insert additive-character orthogonality for `A eps=0`:

```text
Z(A)=p^-d sum_u prod_s
  [1 + (1/2)chi(<u,a_s>) + (1/2)chi(-<u,a_s>)]
    =p^-d sum_u prod_s (1+cos(2 pi <u,a_s>/p)).
```

The identity `1+cos(2x)=2cos^2(x)` gives the second form.

Finally fix a fiber representative `x_0 in {0,1}^m`. Its other incidence
vectors are exactly `x=x_0+c` with `c in K` and
`c_i in {-x_0(i),1-x_0(i)}` coordinatewise. This is the asserted
full-agreement two-list recovery bijection. QED.
