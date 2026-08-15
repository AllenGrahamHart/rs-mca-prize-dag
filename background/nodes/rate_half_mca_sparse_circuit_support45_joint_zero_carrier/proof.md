# Proof

Let `A_c` be the independent `(c-1)`-deletion at source support `c`, and
let `Z_c` be its `q-s_c` completions.  Put `U_c=A_c union Z_c`.  The private
completion coordinates give a `(q-s_c)`-dimensional label space supported
on `U_c`, and

```text
|U_4|=q+3-s_4,       |U_5|=q+4-s_5.               (1)
```

The vanishing spaces

```text
H_c={f in V:f|_(A_c)=0}
```

also vanish on every completion, and have dimensions

```text
dim H_4=7,       dim H_5=6.                        (2)
```

Grassmann gives `dim(H_4 intersect H_5)>=3`.  If equality held, then
`H_4+H_5=V`.  The three-dimensional intersection vanishes on
`U_4 union U_5`, so the polynomial common-root bound gives

```text
|U_4 union U_5|<=K-3=q+7.
```

Together with (1), this forces

```text
|U_4 intersect U_5|>=q-s_4-s_5>0.
```

Every polynomial in `H_4+H_5=V` would vanish at a point of this overlap,
contrary to the assumption that `V` has no common zero on the evaluation
set.  Hence the intersection has dimension at least four.  Applying the
root bound again proves `(JZ1)`.

Let `B` be the complete common-zero set of `H_4 intersect H_5`, and let
`H_B` and `t` be as in the statement.  Then `B` contains both carriers.
Moreover `H_4 intersect H_5` is contained in `H_B`, while `H_B` is
contained in `H_5` because it vanishes on `U_5`.  Therefore

```text
4<=t<=6.                                               (3)
```

The same root bound gives `|B|<=K-t`, so `delta>=0`.  Evaluation
functionals on `B` are independent in `P_K^*`, and their rank on `V` is
`10-t`.  Consequently

```text
dim(Lambda intersect E_B)=|B|-(10-t)=q-delta.       (4)
```

The private-coordinate label spaces of dimensions `q-s_4` and `q-s_5`
are both contained in the space in (4).  Thus

```text
delta<=min(s_4,s_5),
```

which proves `(JZ2)`.

Finally fix any independent three-set `A`, let `Z_A` be all of its
support-four circuit completions, and put `U_A=A union Z_A`.  Its vanishing
space `H_A` has dimension seven.  By (3),

```text
dim(H_A intersect H_B)>=7+t-10=t-3>=1.
```

This intersection vanishes on `U_A union B`, so

```text
|U_A union B|<=K-(t-3)=K-t+3.
```

Since `|B|=K-t-delta`, subtraction gives

```text
|U_A setminus B|<=delta+3.
```

This is the asserted outside-completion bound.  QED.
