# Proof

The reduced mixed curve has finite flat domain projection of degree `e`.
Pushing forward

```text
0 -> O(-d,-e) -> O -> O_C -> 0
```

and splitting the resulting extension gives

```text
E:=pi_*O_C=O direct_sum O(-d)^(e-1).                  (1)
```

Let `P_pos` be the positive divisor in `(SSV2)`, put `r=deg P_pos`, and let
`t=X-x_*` and `K=pi_*O_C(P_pos)`. The exact local forms show
coefficientwise that `P_pos<V_*`: at every point in its support, its
multiplicity `p` is strictly below the vertical multiplicity `n`. Locally
one may write `t=unit*s^n`. Then

```text
t O_C(pP)/O_C
```

is spanned in the fibre algebra by

```text
s^(n-p),...,s^(n-1).                                  (2)
```

These classes are nilpotent because `p<n`. The positive modification

```text
0 -> E -> K -> k_(x_*)^r -> 0                         (3)
```

is therefore killed by `t`, and its `r`-dimensional direction space

```text
W=tK/tE subset E/tE                                  (4)
```

lies in the nilpotent ideal of the vertical fibre algebra.

The fibre contains at least `e-6>0` reduced points from `R_*`. Every element
of `W` vanishes at each reduced factor outside the support of `P_pos`, while
the constant class is nonzero there. Hence

```text
W intersect Fbar*1=0.                                (5)
```

Relative to `(1)`, projection of `W` to the negative block has rank `r`.
A constant change of basis in the equal negative summands, followed by maps
`O(-d)->O` removing the `r` constant components at `x_*`, puts `(3)` in
the standard rank-`r` orbit. Thus

```text
K=O direct_sum O(1-d)^r direct_sum O(-d)^(e-1-r).     (6)
```

Since `d>1`, only the `O` summand has a global section. This proves `(SSV3)`.
Under `O_C subset O_C(P_pos)`, that section is the canonical section with
zero divisor `P_pos`.

Every point of `R_0` lies over a heavy domain row at which the residual
linear form is nonzero, whereas `P_pos` lies over its unique root `x_*`.
Thus `P_pos` and `R_0` are disjoint, and the canonical section is nonzero at
every point of `R_0`. Taking global sections in

```text
0 -> O_C(P_pos-R_0) -> O_C(P_pos) -> O_C(P_pos)|_(R_0) -> 0
```

shows that the left-hand space is zero. The exact signed normal forms
identify its line bundle with `L_2`, proving `(SSV4)`. QED.
