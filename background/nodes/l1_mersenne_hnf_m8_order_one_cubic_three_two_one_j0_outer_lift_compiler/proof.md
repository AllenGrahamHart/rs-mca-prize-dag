# Proof - J-zero outer-lift compiler

The field claim follows first. The coefficient-field dependency gives
`b in F_(p^8)`. Every official role quadratic is irreducible over `F_p`, so
its roots lie in `F_(p^2)`, and `F_(p^2)` is the unique quadratic subfield
of `F_(p^8)`. All formulas in (OLC2)--(OLC5) are rational operations on
these values. Once the displayed inherited denominators are nonzero, every
reconstructed value and polynomial coefficient lies in `K=F_(p^8)`.

In the common-quadratic compiler, `a=y-z` and

```text
G=Q(W)(W-y),       F-B=Q(W)(W-z),
aQ(y)=(lambda-1)B.                                (1)
```

The scaled compiler gives exactly the inverse changes of variables in
(OLC4): `x=dg_1`, `Y=dy`, `G_2=d^2g_2`, `V=d^2v`,
`6-2x=da`, and `S=d^3B`. Thus (OLC4) reconstructs the original monic
factors and `L=FG` without introducing a new equation.

For an actual ordered color triple, normalize its triple color to one and
write the remaining colors as `(beta,gamma)`. The role ratio is

```text
lambda=(gamma-1)/(beta-1).                         (2)
```

The role/`P_4` compiler gives `eta=S/R=1/(lambda-1)`. Equations (2) and
this identity are equivalent to the relation in (OLC3). Conversely the
official role-polynomial and Frobenius-split dependencies prove that every
official role root comes from at least one of the 42 ordered normalized
pairs. This proves the completeness of the finite role enumeration.

Set `e=(beta-1)/B`. From (OLC5),

```text
E-1=eF.                                             (3)
```

At both roots of `Q`, equations (1) give `G=0` and `F=B`, so `E=beta`.
At `W=y`, equations (1)--(2) give

```text
F(y)=B+aQ(y)=lambda B,
E(y)=1+(beta-1)lambda=gamma.                        (4)
```

More algebraically, `E-beta=e(F-B)` is divisible by `Q`, while
`E-gamma` is divisible by `W-y`. The inherited exact-fiber saturation
makes `F`, `Q`, and `W-y` pairwise coprime, and their product is `L`.
Since `1,beta,gamma` are eighth roots of unity, (3)--(4) prove

```text
L | E^8-1.                                         (5)
```

Now assume (OLC8). Because `tau^8=1`, reduction modulo `L` gives

```text
W^n-1=(W^(p+1))^8-1
       =(tau E)^8-1=E^8-1=0 mod L.                 (6)
```

Hence `L | W^n-1`. The removed root is `-1/d`. Since `p+1` is even and
`zeta=d^(p+1)` has eighth power one,

```text
(-1/d)^n=(d^(p+1))^(-8)=zeta^(-8)=1.              (7)
```

Thus `W+1/d` also divides `W^n-1`. Its inherited split-root guard says it
is coprime to `L`, so their product `P` divides `W^n-1`, proving (OLC9).

Finally `d^p=zeta/d`; therefore

```text
(d+1)^p=d^p+1=1+zeta/d,
```

which is (OLC10). The congruence in (OLC8) is the original
assignment-preserving pointwise Frobenius equation, so coefficientwise
Frobenius and the colored resultant consequences need no separate
surrogate variable. The only exponentiation is modular reduction by the
degree-six polynomial `L`; repeated squaring uses `O(log p)` products and
never constructs `W^n-1`. QED.
