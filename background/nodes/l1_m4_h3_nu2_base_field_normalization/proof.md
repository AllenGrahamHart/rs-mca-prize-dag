# Proof - L1 m=4, h=3, nu=2 base-field normalization

The discrete Belyi theorem gives `(BFN2)`, with

```text
y_0'=-S_e(0) in F_p^*.
```

The value-coset theorem says every positive record on either characteristic
in `(BFN1)` has depressed outer form

```text
Y^3-2s^2Y+s^3,
```

whose tangent value is `y_0=3s/4`. Therefore

```text
c=s/lambda^p=(4/3)y_0' in F_p^*.                       (1)
```

Dividing all split values by `lambda^p` proves `(BFN3)`.

Both characteristics are `2 mod 5`. Quadratic reciprocity gives

```text
(5/p)=(p/5)=-1,
```

so `Y^2+cY-c^2` has its two roots in `F_(p^2)\F_p`; Frobenius exchanges
them. The remaining root `c` is fixed.

The fiber polynomial `R_0-c` lies in `F_p[Z]`. Its complete root set `X_c`
is therefore Frobenius-stable. It is nonempty and lies in `C`, while its
Frobenius image lies in `C^p`. Two cosets of the same multiplicative subgroup
are either disjoint or equal. Since `X_c=X_c^p` meets both, `C=C^p`.

The equations `z^n=A` and `z^n=A^p` define `C` and `C^p`; equality gives
`A=A^p`, proving `(BFN4)`. Now `g_0(R_0)` and `Z^n-A` both lie in
`F_p[Z]`. Exact division in the domain identity gives `D_0 in F_p[Z]`,
proving `(BFN5)`. The fixed/conjugate fiber statement follows from their
three values and the prime-field inner polynomial.
