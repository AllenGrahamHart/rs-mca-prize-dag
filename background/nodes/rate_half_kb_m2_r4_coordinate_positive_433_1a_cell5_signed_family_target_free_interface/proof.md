# Proof

Write

```text
P_i=N_i/D_i,       T_i=-Q_i/(Delta D_i).
```

For the three records in `(KBSF-3)`, target realizability means

```text
P_0=de,    T_0=d+e,
P_1=-de,   T_1=d-e,
P_2=be,    T_2=b+e.                              (1)
```

The first two sum equations reconstruct

```text
d=(T_0+T_1)/2,       e=(T_0-T_1)/2.              (2)
```

Hence `(1)` is equivalent to

```text
P_1+P_0=0,
T_0^2-T_1^2-4P_0=0,
2P_2-b(T_0-T_1)=0,
2(T_2-b)-(T_0-T_1)=0.                            (3)
```

Clearing the nonzero denominators in the four rows of `(3)` gives,
respectively, `(KBSF-4)--(KBSF-7)`.  This proves necessity.

Conversely, assume the guards and the four cleared equations.  Define
`d,e` by `(2)`.  Dividing `(KBSF-4)--(KBSF-7)` by their guarded clearing
factors recovers `(3)`.  Its rows give `P_0=de`, `P_1=-de`, `P_2=be`, and
`T_2=b+e`, so all six unsquared product/sum equations in `(1)` hold.

The `DF+/DF-/CF` family is the identical calculation with `e,b` replaced
by `f,c`.

For the endpoint corollary, the target polynomial at source root `z` is

```text
Y^2-S(z)Y+F(z^2).
```

Multiplying its value at `Y=b` by `Delta D(z^2)` gives exactly `(KBSF-8)`.
Direct substitution of the sparse cell-5 coefficients and exact polynomial
division gives `(KBSF-9)`; the independent checker verifies zero remainder
and the printed degree/term ledger.

All scalar factors in `(KBSF-9)` are guarded units, and an outside source is
not `z=t`.  Hence its endpoint row is equivalent to `R_b(z)=0`.  If the
unsquared sum is `b+e`, the other root of the target quadratic is `e`, so
the product is automatically `be`.  Conversely the `BE` product and sum
make `b` a target root and imply both equations in `(KBSF-10)`. QED.
