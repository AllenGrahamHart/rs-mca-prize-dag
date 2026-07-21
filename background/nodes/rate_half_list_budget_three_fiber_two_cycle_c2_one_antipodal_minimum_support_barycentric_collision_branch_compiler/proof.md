# Proof

Direct expansion gives

```text
32z(z-36)^2-(3y-4)^2(3y+2)(z+12)^3
 =-27[y(z+12)-2z+8]
       ([y(z+12)-16]^2-64z),                         (1)
```

which is `(BCB2)`.  The official characteristic exceeds three, so the
collision-router equation is equivalent to `(BCB3)`.  At `z=-12`, the two
factors on the right of `(1)` are respectively `32` and `1024`, both
nonzero.  Hence `z!=-12` on either branch.

On `L=0`, substitution of `y(z+12)=2z-8` into `Q` gives

```text
Q=4(z-4)(z-36).
```

The corresponding `L` values are `y=0` and `y=4/3`.  This proves `(BCB3')`
and the stated disjoint first-match convention.

The torsion-field dependency says that the selected roots `1,t` are squares
in the base field.  Choose `rho^2=t`.  Then

```text
z=(1+t)^2/t=(rho+rho^(-1))^2=x^2,
rho^(2N)=t^N=1.                                      (2)
```

Substitution of `(2)` in `(BCB3)` gives the two equations in `x`; the
quadratic equation factors as

```text
[y(x^2+12)-16-8x][y(x^2+12)-16+8x]=0.
```

Replacing `rho` by `-rho` exchanges these two factors.  Multiplying the
`z`-equations by the required powers of `t` and using

```text
t(z+12)=t^2+14t+1,       t(z-4)=(t-1)^2
```

proves `(BCB5)`.

It remains to compile outer splitting.  From `(BCR4)`, the discriminants of
the collided and complementary outer pairs are

```text
Delta_1=-alpha(3y+2),       Delta_2=alpha(y-2).       (3)
```

They are nonzero on the retained separable locus.  On the `L` branch,

```text
3y+2=8x^2/(x^2+12),       y-2=-32/(x^2+12),
Delta_1=4kappa x^2,       Delta_2=16kappa.            (4)
```

On the `Q` branch with sign `epsilon`,

```text
3y+2=2(x+6epsilon)^2/(x^2+12),
y-2=-2(x-2epsilon)^2/(x^2+12),
Delta_1=kappa(x+6epsilon)^2,
Delta_2=kappa(x-2epsilon)^2.                         (5)
```

Equations `(4)--(5)`, together with nonvanishing of the discriminants, prove
that both quadratics split if and only if `kappa` is a nonzero square.

Finally suppose the selected denominator pair is antipodal.  Then `t=-1`
and `z=0`.  The `L` branch gives `y=-2/3`, contradicting the separability
condition `3y+2!=0`.  The `Q` branch gives `(12y-16)^2=0`, hence `y=4/3`.
The collision-router formula

```text
J=-alpha^3(3y-4)(3y+2)^2
```

then gives `J=0`, while `(BCB6)` becomes `kappa=-alpha/6`.  The
collision-router identities

```text
s^2=alpha y,
beta=-s^3,
gamma=alpha^2/4+alpha s^2/2
```

at `y=4/3` give the remaining equations in `(BCB7)`.  Finally
`alpha/3=(s/2)^2` and `-alpha/6` are both squares, so their quotient `-2`
is a square.  This proves all claims. QED.
