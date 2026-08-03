# Proof

Use target variables

```text
a=de,  u=df,  v=ef,  f=f,       a f^2 = u v.      (KBP1B14-LP-3)
```

The cell-14 structure theorem gives a global guarded common model
`F(r,b)=0`, quadratic in `b`, together with rational `t(r)`, `c(r,b)`, and a
globally normalized common kernel.  Every denominator inverted by the
outside compiler is a denominator already proved nonzero on this guarded
curve.

Let `m(r,b)` be the common-kernel ratio at the missing source label.  If the
missing outside record is `y_0`, `y_1`, or `y_2`, its product equation sets
`a=m`, `a=m`, or `a=-m`, respectively.  Hence all three `de` records become
fixed common-curve functions.  In each of the first three enumerated perfect
matchings, the two residual `de` records are paired.  Their exact Vieta
compatibility determinant reduces modulo `F` to

```text
E(r,b) = L_0(r) + b L_1(r).                        (KBP1B14-LP-4)
```

No target variable remains in this equation.

Write `F=A b^2+B b+C`.  Away from the common zero locus of `L_0,L_1`, a
solution of `F=E=0` requires

```text
R(r) = A L_0^2 - B L_0 L_1 + C L_1^2 = 0.         (KBP1B14-LP-5)
```

The compiler removes from `R` only factors supported on the common
`gcd(L_0,L_1)` boundary and the already excluded route guards
`r,t,r^2+/-1,t^2+/-1,t^2+/-r^2`.  In all 144 cases the residual open cut is a
nonzero constant.  Thus no guarded solution exists off the boundary.

The remaining boundary polynomial is factored exactly over the deployed
field.  For missing records `y_0,y_1` it has degree 60 and twelve distinct
irreducible factors of degrees

```text
1,1,2,2,4,4,4,4,6,6,13,13.
```

For `y_2` it has degree 82 and ten distinct factors, with degree/multiplicity
profile

```text
(1,1),(1,1),(5,1),(5,1),(7,1),(7,1),
(8,1),(8,1),(8,2),(12,2).
```

Multiplicity does not change the zero set.  On each factor, `L_0=L_1=0`,
so `(KBP1B14-LP-4)` is automatic.  The compiler adds the curve equation, all
remaining outside equations, and that factor to a deployed-field Singular
ideal.  Every such ideal is the unit ideal.

The exact ledger contains 144 open ideals and 1632 boundary-factor ideals,
all unit.  It covers the full Cartesian product in `(KBP1B14-LP-2)`.  One
boundary process timed out in the large parallel launch; its isolated replay
used byte-identical definitions and a byte-identical Singular program and
returned the unit ideal.  The aggregate checker verifies that replacement by
both hashes.  Therefore all 144 systems are empty. QED.
