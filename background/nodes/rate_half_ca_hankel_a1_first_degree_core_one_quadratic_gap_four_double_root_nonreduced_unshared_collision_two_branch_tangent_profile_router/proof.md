# Proof

The four-shape classification gives the positive correction-order records

```text
A: (2),       B: (1,1),       C: (2),       D: (1,1).       (1)
```

Hence in shape B or D exactly two factor germs `f_1,f_2` vanish at the
collision. For each of them,

```text
ord_z f_i(z,0)=1.                                  (2)
```

Equation `(2)` gives the expansion `(TBP1)` with `a_i!=0`. Every other
factor has correction order zero and is therefore nonzero at `(0,0)`.
Absorbing those factors and the global scalar gives `(TBP2)` with a unit
`u`.

Differentiate `(TBP2)` in `y`:

```text
G_X=u_y f_1f_2+u(f_(1,y)f_2+f_1f_(2,y)).          (3)
```

Both `f_1` and `f_2` vanish at the origin, so `(3)` first gives
`G_X(tau,x_*)=0`. Taking the coefficient of `z` and using `(TBP1)` gives

```text
[z]G_X(t,x_*)=u_0(v_1a_2+a_1v_2).                 (4)
```

This is `(TBP3)`. Since `u_0a_1a_2` is nonzero, the right side of `(4)`
vanishes exactly when

```text
v_1/a_1+v_2/a_2=0.                                (5)
```

Rescaling either factor multiplies `a_i` and `v_i` by the same nonzero
constant, so `(5)` is independent of the chosen factor normalizations.

The proved Pade/split-jet dictionary identifies a nonzero value of
`G_X(tau,x_*)` with profile `[4]`, a simple parameter zero of `G_X` with
profile `[1,3]`, and a zero of order at least two with profile `[2,2]`.
Equations `(3)--(5)` therefore exclude `[4]` and give `(TBP5)`.

In shapes A and C the unique collision factor has correction order two.
Differentiating a unit times that single factor need not vanish at the
origin, so no analogous conclusion follows. QED.
