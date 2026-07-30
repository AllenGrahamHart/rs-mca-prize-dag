# Proof

Let

```text
F=Q(zeta_128+zeta_128^(-1)),
E=Q(zeta_256+zeta_256^(-1)).
```

Miller's unconditional Theorem 2.1 gives `h(E)=1`. If an ideal class `y`
of `F` is extended to `E`, it is therefore principal. Norming back through
the quadratic extension `E/F` gives `y^2=1`. Weber's oddness theorem for
the plus part of a 2-power cyclotomic field then gives `y=1`. Hence

```text
h(F)=1.                                               (1)
```

For odd `a`, the quotient

```text
b_a=(1-zeta^a)/(1-zeta)=1+zeta+...+zeta^(a-1)
```

is an algebraic integer. Its numerator and denominator both have absolute
norm two, so `b_a` is a unit. Since

```text
bar(b_a)=zeta^(1-a)b_a,
```

the unit `eta_a=zeta^((1-a)/2)b_a` is real.

For prime-power conductor, the Kummer-Sinnott formula identifies the index
of the circular units in the full unit group with the plus class number.
Its standard generators are the roots of unity and the `b_a` with `a` odd.
Equation `(1)` therefore says that these circular units are all units.

Modulo roots of unity, `b_a` and `eta_a` have the same class, `b_1=1`, and
replacing `a` by `-a mod 128` changes the class only by a root of unity.
Thus the 31 units with `a=3,5,...,63` generate `R^x/mu_128`. Dirichlet's
unit theorem says that this quotient is torsion-free of rank 31. A
surjection from `Z^31` to a free abelian group of rank 31 is an isomorphism,
which proves `(C128U2)--(C128U3)`. QED.
