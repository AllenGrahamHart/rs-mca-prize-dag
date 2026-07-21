# Proof

The Euler divisor dependency proves that minimum support forces
`deg C=m=H-3`; in particular `c_m!=0`.  Recall

```text
Theta=HBC+z(BC'-B'C),
J_supp=Q_-C^2Theta+Q_+C(-z)^2Theta(-z),              (1)
```

where `Q_+=Q_-(-z)`.  The coefficient of `b_ic_jz^(i+j)` in `Theta` is

```text
H+j-i.                                               (2)
```

At degree `3H-7=r+m-1`, only `(i,j)=(r,m-1)` and
`(r-1,m)` can occur.  Their coefficients in `(2)` are respectively `-1`
and `+1`.  Hence

```text
[z^(3H-7)]Theta=Delta_inf.                           (3)
```

Both `m=H-3` and `3H-7` are even.  Since `Q_-` and `Q_+` have common leading
coefficient `P`, equation `(1)` gives

```text
[z^(5H-11)]J_supp=2P c_m^2 Delta_inf.                (4)
```

Minimum support requires `deg J_supp=5H-11`, so `(4)` also proves
`Delta_inf!=0`.  At zero, `B(0)=C(0)=Q_-(0)=Q_+(0)=1` and
`Theta(0)=H`; thus

```text
J_supp(0)=2H.                                        (5)
```

Equations `(4)--(5)` prove `(ETG2)`.

The degree `5H-11` is even.  For an even-degree polynomial with nonzero
constant and leading coefficients, the product of its roots is their ratio
`J_supp(0)/lc(J_supp)`.  Equations `(4)--(5)` identify that ratio with `Xi`
in `(ETG3)`.

Finally `(BSP5)` says that these roots are distinct elements of `mu_N`, and
evenness makes the root set stable under `a -> -a`.  The characteristic is
odd, so there are no fixed points.  For each pair `{a,-a}`, its product is

```text
-a^2=(iota a)^2
```

for an element `iota in mu_N` of order four.  Thus every pair product lies
in the square subgroup `mu_(N/2)`, and so does their total product `Xi`.
This proves `(ETG4)`. QED.
