# Proof

Write `m_x=|{i:x in O_i}|` outside `X`, and put

```text
S=sum_x m_x,       Q_2=sum_x C(m_x,2),
H=sum_x C(m_x-1,2).
```

For every integer `m>=1`,

```text
m-2C(m,2)+2C(m-1,2)=2-m<=1_(m=1).                 (1)
```

Summing `(1)` gives

```text
P_1>=S-2Q_2+2H.                                    (2)
```

The extension sizes and the collision ledger give

```text
S=t(h-D)+Z-I,
Q_2=(t-1)Z-C(t,2)D-(t-1)I-sigma.                  (3)
```

Substitution into `(2)` yields

```text
P_1>=t h+t(t-2)D-(2t-3)Z
     +(2t-3)I+2sigma+2H
   =t h+t(t-2)D-(2t-3)Z+2C+I,                     (4)
```

which is `(PF2)`.

Points inside `X` occur in at least three active circuit rows, and a reused
point in `I_i subset Z_i` lies in every `S_j` for `j!=i`. Hence the points
counted by `P_1` are exactly the only circuit points relevant to block
privacy. For every block `A_i` of the host core, `(HR3)` gives

```text
p_i^G<=(h-1-e)/2.                                  (5)
```

Any circuit-private point not covered by a block in `G\J` remains private in
`G`. One additional block meets each of the `t` circuit blocks in at most
`a` points, so it covers at most `ta` of their pairwise disjoint private
point sets. With `r=|G\J|`, `(5)` gives

```text
P_1<=t(h-1-e)/2+rta,
```

and `r<=L-t` proves `(PF3)`.

The zero fibers are disjoint in `X`, so `Z<=a+D`. Dropping the nonnegative
terms `2C+I` in `(PF2)` and using `D>=3` gives

```text
P_1>=t h+(t-1)(t-3)D-(2t-3)a
   >=t h+3(t-1)(t-3)-(2t-3)a.                     (6)
```

Combine `(6)` with `(PF3)` and rearrange:

```text
[tL-t(t-2)-3]a
 >=t(h+1)/2+3(t-1)(t-3).                          (7)
```

The denominator is positive at all three prize rows. Taking the integer
ceiling proves `(PF4)` and the table.

Finally, any prize-row rank-two trade either uses every block of its minimal
core or does not. The first case obeys the much larger all-arity full-core
floor. In the second case, the Segre circuit decomposition contains a four-
or five-block row-scaling circuit properly supported in that core, so `(PF4)`
applies. Taking the smaller proper-circuit floor proves `(PF5)`. QED.
