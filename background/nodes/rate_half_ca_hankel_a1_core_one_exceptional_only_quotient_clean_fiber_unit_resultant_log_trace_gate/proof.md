# Proof

At a clean slope, write the simple roots of `Q(t,X)` locally as `x_i(t)`.
If `m=deg_X W`, the monic-first resultant convention gives

```text
Res_X(Q,W)=a^m product_i W(t,x_i(t)).                 (1)
```

The unit-resultant theorem gives the same polynomial as

```text
c_X^(-1)E^(m+n_X+1)q_bar^(m+n_X).                   (2)
```

Take logarithmic derivatives of `(1)--(2)` and use
`a=E q_bar`. The terms containing `m` cancel, leaving

```text
sum_i dot W(t,x_i)/W(t,x_i)
 =(n_X+1)E'/E+n_X q_bar'/q_bar.                     (3)
```

Put `y_i=1/x_i`. Reversal at degree `r-1` gives

```text
W_vee(t,y_i)=y_i^(r-1)W(t,x_i).                     (4)
```

Also

```text
q_0=a(-1)^r product_i x_i,
product_i y_i=(-1)^r a/q_0.                         (5)
```

Thus the logarithmic derivative of `(4)`, summed over `i`, adds

```text
(r-1)(E'/E+q_bar'/q_bar-q_0'/q_0)                  (6)
```

to `(3)`. Since `N_sq=n_X+r-1`, the result is the right side of `(QLT2)`.

The clean first-jet theorem says `W_vee(gamma,y_i)` is nonzero at every
root, so `w` is a unit in the split quotient algebra. The quotient-ring
compiler gives `dot W_vee=j+w_Yv`; the algebra trace is the sum of its
values over the `r` simple roots. This identifies the left side and proves
`(QLT2)`. QED.
