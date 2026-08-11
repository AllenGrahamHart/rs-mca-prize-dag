# Proof

At `j=0`, every row outside the heavy factor is saturated. Cancel the common
factor `B` from the ambient identity and from the residual domain locator:

```text
G=B G_L,       s_F^3G_L/H=A_0^res|_C.                 (1)
```

Fix a supported incidence `(gamma,x)` on a heavy row. Since `G_L(x)` is
nonzero and `H` vanishes at `gamma`, regularity of `(1)` forces the Forney
numerator to vanish at that point.

At the same supported fibre, use the contracted recurrence factorization

```text
Qbar_gamma=Q_min R_gamma,
N_F(gamma;X)=R_gamma N_min,
deg R_gamma=c_gamma.                                  (2)
```

The split minimal recurrence has nonzero Forney value at each of its simple
roots. Therefore a root of `Qbar_gamma` at which `N_F` vanishes belongs to
`R_gamma` (including a repeated minimal root, which contributes its extra
copy to `R_gamma`). There are at most `c_gamma` distinct heavy incidences in
that fibre. Summing proves `(CHI2)`.

Let `I_L` be the supported incidence count on light rows. Saturation and
`rho=3e-1` give

```text
I_L=(N-s-h)e=(3rho+3+a)e=(9e+a)e.                     (3)
```

The total residual incidence identity is

```text
I_L+I_H=T d-O.                                        (4)
```

Both parameter-constant profiles have `T=rho+4=3e+3`.

For `s=0`, `d=3e-1`, so subtracting `(3)` from `(4)` gives

```text
I_H+O=(3e+3)(3e-1)-(9e+a)e=(6-a)e-3.                 (5)
```

For `s=1`, `d=3e-2`, and the same calculation gives

```text
I_H+O=(3-a)e-6.                                       (6)
```

This proves `(CHI3)`. Both `I_H` and `O` are at most `Delta`. In core zero,
`a<=1` would make the right side of `(5)` exceed `2Delta=4e-2`; hence
`a>=2`. In core one, `a=0` makes `(6)` exceed
`2Delta=2e-4`; hence `a>=1`. Combining these lower bounds with the bounded
residual table proves `(CHI4)`.

Finally, at `s=0,a=2`, equation `(5)` is

```text
I_H+O=4e-3=2Delta-1,
```

which is the first identity in `(CHI5)`. At `s=1,a=1`, equation `(6)` is
`2e-6=2Delta-2`, proving the second. QED.
