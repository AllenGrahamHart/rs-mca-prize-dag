# Proof

Let `m_x` be the number of selected active blocks in `J` containing `x`.
The total active-block incidence and pair incidence are

```text
S=sum_x m_x=t(a+h),
Q=sum_x C(m_x,2)=sum_(i<j)|A_i intersect A_j|
 <=C(t,2)a.                                         (1)
```

For every `m>=1`, `m-2C(m,2)<=1_(m=1)`. Summing and using `(1)` gives

```text
P_J>=S-2Q
   >=t(a+h)-t(t-1)a
   =t h-t(t-2)a,                                    (2)
```

which is `(UF2)`.

Now view the same points inside the complete host core `G`. Any point counted
by `P_J` that is not covered by a block in `G\J` remains private to its
unique block in `G`. The minimal-core private-point bound gives at most
`(h-1-e)/2` such surviving points per active block. Each additional block
meets each active block in at most `a` points and therefore covers at most
`ta` points from the `t` disjoint private sets. Hence

```text
P_J<=t(h-1-e)/2+(|G|-t)ta.                          (3)
```

The exact core-size bound `|G|<=L` and `e>=0` prove `(UF3)`.

Combining `(UF2)` and `(UF3)` and dividing by `t>0` gives

```text
h-(t-2)a<=(h-1)/2+(L-t)a,
(h+1)/2<=(L-2)a.                                   (4)
```

Taking the integer ceiling proves `(UF4)`. The official values of `h,L`
give the table.

Finally, for an XR uniform counterexample the Maxwell density threshold is
automatic. The uniform split-pencil reduction supplies a minimal core `G`,
and its stacked parity matrix has a nonzero left-kernel trade. Thus `(UF4)`
contradicts every counterexample with `a<A_unif`. Since selector affine rank
is `s=a+1`, ranks through `A_unif` are paid, proving `(UF5)`. QED.
