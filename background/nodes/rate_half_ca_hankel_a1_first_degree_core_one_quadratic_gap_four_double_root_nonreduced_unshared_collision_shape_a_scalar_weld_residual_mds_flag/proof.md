# Proof

The row factorization `(RWF1)` is the coefficient-MDS normalization. The
connected scalar-weld dichotomy shows that a passing common biform has only
one projective row-scalar vector.

Fix `delta`. The all-excess factorization gives

```text
lambda_xP_x(delta)
 =G(delta,x)
 =zeta_delta A_delta(x)H_delta(x)R_delta(x)         (1)
```

for every `x in X_delta`. The actual-support factor is nonzero there, and
every padded-heavy root lies outside `U_0`. Division in `(1)` is therefore
legal and yields

```text
u_(delta,x)(lambda)=zeta_delta H_delta(x).          (2)
```

Let `s_delta=|X_delta|`. From

```text
|I_delta|=n-a_delta-r_delta
```

and `(RWF5)`,

```text
s_delta
 =R-n+a_delta+r_delta
 =3e+a_delta+r_delta.                               (3)
```

For every polynomial `B` of degree at most `s_delta-1`, Lagrange
interpolation on `X_delta` gives

```text
sum_(x in X_delta)B(x)/L_delta'(x)
 =[X^(s_delta-1)]B(X).                              (4)
```

Apply `(4)` to

```text
B(X)=zeta_delta H_delta(X)X^j.
```

Since `deg H_delta=a_delta-q_delta`, the right side is zero precisely
through

```text
j<=s_delta-(a_delta-q_delta)-2
  =3e+r_delta+q_delta-2,                            (5)
```

and at the next index it is

```text
zeta_delta lc(H_delta)!=0.                          (6)
```

Equations `(2)`, `(5)`, and `(6)` prove `(RWF7)--(RWF8)`. Expanding
`E_(delta,j_delta+s)` in the coordinates of `lambda` gives `(RWF9)` and
`(RWF10)`.

Finally, the proved shape-A norm concentration theorem gives

```text
deg T=e-sum_delta q_delta.
```

Substituting the exact parity-run characterization proves `(RWF11)`. QED.
