# Proof

It is enough to check `(FPA3)` over each supported fibre. Work in one local
ring `A` of `C` over a supported slope `gamma`, write `h=L_gamma`, and put

```text
B=A/(h),       g=G|_C.
```

Because `h` is a nonzerodivisor on the reduced mixed curve, the standard
colon calculation gives

```text
J/(h)=ann_B(g).                                        (1)
```

We prove that the specialization of `N_F` annihilates `g` in `B`.

The contracted exceptional-root theorem supplies a squarefree split
residual recurrence factor `Q_min(X)` at `gamma`. It divides both the
specialized generic generator and the residual domain locator:

```text
Qbar_gamma=Q_min R,       G=Q_min G_1.                 (2)
```

The factor `Q_min` belongs to the specialized contracted apolar ideal. Let
`N_min` be its recurrence numerator. Multiplying a recurrence polynomial by
`R` multiplies its reciprocal generating numerator by the reversed factor.
Thus, in either affine domain chart and hence homogeneously,

```text
N_F(gamma;X)=R(X)N_min(X).                             (3)
```

Equations `(2),(3)` give

```text
N_F(gamma;X)G(X)
 =R N_min Q_min G_1
 =Qbar_gamma N_min G_1.                               (4)
```

Therefore the product is zero in
`B=O_{C,gamma}=Fbar[X]/(Qbar_gamma)` with its full local scheme structure.
By `(1)`, `N_F` belongs to `J` at every point over `gamma`.

Away from the supported fibres, `H` is a unit and `J=O_C`. The local
memberships therefore glue and prove `(FPA3)`. The polynomial quotient
`N_FG/H` is regular. Interpreting the forced domain-infinity contact of
`N_F` as the line bundle `(FPA2)` gives `(FPA4)`. QED.
