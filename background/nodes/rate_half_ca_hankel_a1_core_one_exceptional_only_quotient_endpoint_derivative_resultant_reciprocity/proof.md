# Proof

For every root `a` of `A`, exact row saturation says that `Q(z;a)` has
degree `e` and exactly `e` distinct supported roots. One is the simple root
`z=0`. Therefore

```text
Q(z;a)=z q_1(a)+O(z^2),       [z^e]Q(z;a)=q_e(a),
q_1(a)q_e(a)!=0.                                      (1)
```

Because `A` is monic,

```text
R_A(z)=Res_X(A,Q)=product_(A(a)=0) Q(z;a).            (2)
```

The coefficient of `z^(2e)` at the bottom of `(2)` and its leading
coefficient are respectively

```text
[z^(2e)]R_A=Res(A,q_1),       lc_z(R_A)=Res(A,q_e).   (3)
```

In the flat profile, compare `(3)` with

```text
R_A= kappa z^(2e)P_ord^k_0.
```

Since `P_ord` is monic, the leading coefficient gives
`kappa=Res(A,q_e)`. The coefficient of `z^(2e)` then gives `(QDR1)`.

In the swapped profile, use the cleared identity

```text
(z-z_max)R_A
 =kappa z^(2e)(z-z_min)P_ord^k_0.                    (4)
```

Leading coefficients in `(4)` again give `kappa=Res(A,q_e)`. Comparing the
coefficients of `z^(2e)` gives

```text
-z_max Res(A,q_1)
 =-z_min Res(A,q_e)P_ord(0)^k_0,
```

which is `(QDR2)`. Finally `k_0=2^37-1` is odd, and inversion does not change
a square class, proving `(QDR3)`. QED.
