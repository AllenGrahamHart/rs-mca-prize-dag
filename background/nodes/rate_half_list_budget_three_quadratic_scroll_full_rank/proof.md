# Proof

Retain the notation from the parent theorem. Write

```text
b_01=c,
b_02=a_0+a_1X,
b_03=d_0+d_1X,
b_12=e_0+e_1X,
b_13=f_0+f_1X+f_2X^2.
```

Here `c,d_1,e_1` are nonzero. The balancing polynomial is `h=sX`, with
`s=f_2/d_1` when `f_2!=0` and `s=0` otherwise. The four coefficient columns
are

```text
U_0=(c,0,-e_0,-f_0)^T,
U_1=(0,cs,-e_1+sa_0,-f_1+sd_0)^T,
V_0=(0,c,a_0,d_0)^T,
V_1=(0,0,a_1,d_1)^T.                                (1)
```

Expanding the determinant first along the first row and then along the first
row of the resulting `3x3` matrix gives

```text
det C
 =c^2[ s(a_0d_1-a_1d_0)
       -((-e_1+sa_0)d_1-a_1(-f_1+sd_0)) ]
 =c^2(e_1d_1-a_1f_1).                               (2)
```

This is `(QFR1)`.

In a pendant chamber, `a_1=L_02=0`, while
`e_1=L_12` and `d_1=L_03` are nonzero because the `12` and `03` selected
edge blocks are distinct singletons. Equation `(2)` proves `(QFR2)`,
including the chambers in which `b_13` is quadratic.

In the quadratic `K_4-e` chamber, `f_2=0` and all four displayed factors are
exactly linear. Since `c=b_01` is constant, the Plucker identity is

```text
c b_23=b_02b_13-b_03b_12.
```

Comparing quadratic coefficients gives the first equality in `(QFR3)`.
Exact quadratic degree of `b_23` makes that coefficient nonzero. Substitution
into `(2)` proves the determinant identity and nonvanishing in `(QFR3)`.

Thus `C` is invertible in all four chambers, and `(QFR4)` is the full-rank
branch already proved by the quadratic scroll atlas. QED.
