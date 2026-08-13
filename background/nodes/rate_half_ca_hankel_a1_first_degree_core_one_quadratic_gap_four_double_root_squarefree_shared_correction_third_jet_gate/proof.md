# Proof

At a common simple root of the squarefree forms `g_*` and `S_B`, the exact
row and determinant factorizations give

```text
Q(t,x_*)=a_Q g_*S_B^3,       D_1=a_D g_*S_B^2,     (1)
```

so their base valuations are four and three.

Let `B` be the correction divisor on the normalized curve. Along its point
over `tau`,

```text
ord_B(X-x_*)=3,       ord_B(P_F|_C)=2.              (2)
```

Replacing the moving curve coordinate by the fixed value `x_*` changes
`P_F` only by a multiple of `X-x_*`. Therefore `(2)` gives

```text
z^2 divides P_F(t,x_*)=F_0(t).                     (3)
```

This conclusion is deliberately only order two. The supported contact and
the correction contact may be distinct normalized branches above `tau`, so
their orders cannot be added in a base polynomial without an extra jet.
Equation `(3)` makes `(HSJ4)` well-defined, and since `D_1` has exact order
three,

```text
kappa_tau=0 iff D_1 divides F_0 locally.            (4)
```

The kernel equation gives the formal recurrence

```text
F_(i+1)=x_*F_i-Q(t,x_*)h_i.                         (5)
```

The last term has order four by `(1)`. Divide `(5)` by `z^2` and reduce
modulo `z`; induction proves `(HSJ5)`. In particular, if `kappa_tau` is
nonzero, every component has exact order two and the leading vector is
`kappa_tau(1,x_*,...,x_*^d)`.

If `kappa_tau=0`, equation `(4)` gives `D_1|F_0`. Since

```text
Q(t,x_*)/D_1=(a_Q/a_D)S_B                          (6)
```

is polynomial even at a shared root, recurrence `(5)` propagates
`D_1|F_i` to every `i`. The converse follows by taking `i=0`, proving
`(HSJ6)`. Division by `D_1` then gives the same degree-at-most-three vector
and cubic recurrence as in the separated theorem.

Finally, at `tau`,

```text
Q_tau=(X-x_*)U_tau,                                (7)
```

and the class of `U_tau` in the regular quotient is nonzero. On the
vanishing branch its image is divisible by `z^3`, while the determinant
valuation is exactly three. Hence one positive Smith exponent is at least
three and their sum is three, so the type is `[3]`. QED.
