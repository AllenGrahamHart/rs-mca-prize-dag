# Proof

On the selected-antipodal shard, the collision-branch dependency gives

```text
s^2=4alpha/3,
Phi(W)=(W^2-sW+s^2+alpha/2)(W^2+sW+alpha/2),
q^2=-alpha/6.                                          (1)
```

Here `alpha,s,q` are nonzero.  Define `a=s/(2q)`.  Then

```text
a^2=s^2/(4q^2)=(4alpha/3)/(4(-alpha/6))=-2.           (2)
```

The discriminants of the two quadratics in `(1)` are respectively

```text
-6alpha=(6q)^2,       -2alpha/3=(2q)^2.               (3)
```

Their roots can therefore be ordered as

```text
q(a+3), q(a-3), q(-a+1), q(-a-1).                    (4)
```

The infinity dependency sends an outer root `w` to `b_r+c_mw`.  With
`d=c_mq` and `u=b_r/d`, substitution of `(4)` gives `(SAI2)`.

All four infinity roots lie in `mu_N`, hence are nonzero.  Their distinctness
gives `ell_3!=ell_4`, so `y!=1`.  Put `v=u-a`.  From

`y=(v+1)/(v-1)` one obtains

```text
v=(y+1)/(y-1),       v-1=2/(y-1).                    (5)
```

Dividing the first two formulas in `(SAI2)` by the fourth and using `(5)`
gives

```text
(v+2a+3)/(v-1)=(a+2)y-(a+1),
(v+2a-3)/(v-1)=(a-1)y+(2-a).                         (6)
```

This proves `(SAI3)--(SAI4)`.  Since each `ell_i` is `tau` times one of
`A_a(y),B_a(y),y,1`, all four lie in `mu_N` if and only if the four scalars
in `(SAI5)` do.  Multiplying `(SAI4)` and using the infinity gate's
`product_i ell_i=P_src^(-1)` proves `(SAI6)`.

Rearranging `(SAI6)` gives

```text
P_src y A_a(y)B_a(y)=tau^(-4).                        (7)
```

The fourth powers in the cyclic group `mu_N` form exactly its subgroup
`mu_(N/4)`.  Since `N=2^40`, equation `(7)` proves `(SAI6')` with
`N/4=2^38`.

Conversely `(5)` gives the formula for `u`, while
`tau=ell_4=d(v-1)` gives `d=tau(y-1)/2`.  The definitions of `u,d` then
recover `b_r,c_m`, proving `(SAI7)` at the top-coefficient interface.

Finally replace `q` by `-q`.  Then `(a,d,u)` becomes `(-a,-d,-u)`, and
`(SAI2)` swaps `ell_1` with `ell_2` and `ell_3` with `ell_4`.  Therefore
`tau` becomes `ell_3=tau y` and `y` becomes `y^(-1)`, which is `(SAI8)`.
QED.
