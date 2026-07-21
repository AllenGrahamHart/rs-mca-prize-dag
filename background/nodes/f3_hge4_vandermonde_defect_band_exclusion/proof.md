# Proof

Choose `omega in F_p` of order `m`. Label the reciprocal root supports of a
hypothetical primitive pair by disjoint `h`-subsets `I,J` of `Z/mZ`, and put

```text
f_t=1_(t in I)-1_(t in J).                          (1)
```

Newton identities and equality of the top `h-1` locator coefficients give

```text
sum_t f_t omega^(kt)=0,       0<=k<h.               (2)
```

The case `k=0` uses `|I|=|J|`.

## Strict cyclotomic defect ceiling

Put `M=m/2` and, for `0<=t<M`, define

```text
g_t=f_t-f_(t+M),       q_t=f_t+f_(t+M),
D=sum_t g_t^2,         L=sum_t q_t^2.               (3)
```

The exact orthogonal identity gives

```text
D+L=4h=m-4d.                                      (4)
```

The cyclotomic lift `z=sum_t f_t zeta_m^t` is nonzero. Otherwise dyadic odd
Fourier inversion makes both supports invariant under the antipode, contrary
to primitivity. There are `r=floor(h/2)` odd exponents below `h`. Complete
splitting of `p`, odd-frequency Parseval, and AM--GM give

```text
p^r<=|Norm(z)|<=D^(m/4).                            (5)
```

The compatible prime is strictly greater than the composite integer `m^2`.
For both parities of `h`, equation `(5)` implies

```text
D>m^(1-4(d+1)/m).                                  (6)
```

Write

```text
x=4(d+1)R/m.
```

Taylor's theorem with positive fourth-order remainder gives

```text
exp(-x)>=1-x+x^2/2-x^3/6       for x>=0.
```

Equations `(4)--(6)` therefore yield the strict cubic defect ceiling

```text
L<4h-m(1-x+x^2/2-x^3/6)
 =4((d+1)R-d)-8(d+1)^2R^2/m
    +(32/3)(d+1)^3R^3/m^2
 =Y_3.                                               (7)
```

## Consecutive even-moment rank

Let `eta=omega^2`, which has order `M`. For

```text
0<=j<=H=floor((h-1)/2),
```

the even instances of `(2)` are exactly

```text
sum_(t=0)^(M-1) q_t eta^(jt)=0.                    (8)
```

Suppose `q` is nonzero and let its support have size `k`. If `k<=H+1`, take
the first `k` equations in `(8)`. On the distinct support points
`x_t=eta^t`, their coefficient matrix is the square Vandermonde matrix

```text
(x_t^j)_(0<=j<k,t in supp(q)),
```

whose determinant is `product_(u<v)(x_v-x_u)!=0`. It would force every
nonzero coordinate of `q` to vanish in `F_p`, a contradiction. Since
`q_t in {0,+-1,+-2}` and `p` is odd, this proves

```text
|supp(q)|>=H+2=v_h,
L=sum_t q_t^2>=|supp(q)|>=v_h.                     (9)
```

Under `(VDE2)`, equations `(7)` and `(9)` are incompatible. Hence `q=0`, or

```text
f_t+f_(t+M)=0       for every t.                   (10)
```

Thus the antipode exchanges the two supports: every hypothetical pair lies
in the primitive swap class.

## Composition with the swap norm

It remains to check that `(VDE2)` lies inside the proved swap-exclusion band.
Its guard `x<=1` gives

```text
(d+1)R<=m/4.                                       (11)
```

Because `R=s log 2` and `log 2>1/2`, equation `(11)` implies

```text
s(d+1)<m/2.                                        (12)
```

The swap-norm theorem deletes the complete swap class whenever
`s(d+1)<=m/2`. Equations `(10)--(12)` therefore exclude every primitive pair
in `(VDE2)`, proving `(VDE3)`.

Finally, on `0<=x<=1`, differentiation with respect to real `d` gives

```text
dY_3/dd=4(R(1-x+x^2/2)-1)>0,                       (13)
```

because `1-x+x^2/2>=1/2` and `R>=log 16>2`. The rank floor `v_h` is
nonincreasing, so each guarded fixed-`m` band is an initial interval and
exact adjacent endpoint certificates determine the printed ranges.

For comparison, let `Y_1=4((d+1)R-d)`. Under `x<=1`,

```text
Y_3=Y_1-8(d+1)^2R^2/m (1-x/3)<=Y_1.                (14)
```

If `Y_1<=v_h`, then `v_h<=h` also gives `(d+1)R<=m/4`, hence `x<=1`.
Therefore the former linear band is contained in `(VDE2)`. QED.
