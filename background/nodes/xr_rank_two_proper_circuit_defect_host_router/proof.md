# Proof

Every nonempty proper subset `J` of a minimal Maxwell core satisfies

```text
h|J|<=2|union_(i in J)A_i|-(2a+1).
```

Therefore `Delta_J>=1`. Since `h` is odd and the other two terms in
`Delta_J` are even, `Delta_J` has the parity of `t`. Hence its least possible
positive value is `delta_4=2` for four rows and `delta_5=1` for five rows.

The collision-defect identity applies to the actual compatible extension
family on `J` and gives

```text
Delta_J=D_0+2C,       C=(t-2)I+sigma+H>=0.          (1)
```

The baseline `D_0` has the same parity as `t`, so `delta_t-D_0` is even.
Rearranging `(1)` proves `(PC2)`. The full-core upper bound `(PC3)` is the
other sign of the same identity. When `D_0<=0`, its upper endpoint and the
proper lower endpoint differ by one, proving the separator. If
`D_0<delta_t`, `(PC2)` gives `C>=1`, and the nonnegative decomposition of
`C` proves `(PC4)`.

Write `|G|=t+r` and let `Delta_G=-e`. Since the host union contains the
circuit union,

```text
-e=Delta_G
   >=2|union_(i in J)A_i|-2a-h(t+r)
   =Delta_J-hr.
```

Thus `hr>=Delta_J+e`, which is `(PC5)`.

It remains to prove the shell cutoffs. The sharp pairwise zero-fiber mass
floor is

```text
M_t(D)=tD/2          for D even,
       t(D+1)/2-1   for D odd.                     (2)
```

For four rows,

```text
D_0=4h+6D-4Z.
```

Substituting `Z>=M_4(D)` and requiring `D_0>=2` gives `D<=2h-2` in the even
case and `D<=2h-3` in the odd case. For five rows,

```text
D_0=5h+12D-6Z.
```

Substitution of `(2)` and the condition `D_0>=1` give respectively
`3D<=5h-1` and `3D<=5h-10`, proving `(PC6)`. QED.
