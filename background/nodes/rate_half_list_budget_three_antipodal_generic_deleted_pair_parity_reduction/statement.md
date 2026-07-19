# Budget-three antipodal generic deleted-pair parity reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_two_window_square_reduction`

Retain the maximal generic floor in characteristic greater than `d`. Write

```text
d=16M,       h=2M+1,       r=4M-1.                  (DPP1)
```

Suppose the four deleted roots are two distinct antipodal pairs
`{b,-b,c,-c}`. Put `u=b^2`, `v=c^2`, `w=z^2`, and

```text
E(z)=(1-uw)(1-vw),
A(z)=E(z)^(-1/4)=sum_(j>=0)f_jw^j.                 (DPP2)
```

Every odd coefficient of `A` vanishes. Hence the second primary zero
`a_(4M+1)=0` is automatic, while the remaining primary conditions are

```text
f_(2M)=0,       f_(2M+1)!=0.                       (DPP3)
```

The two-window square is even as well. Define

```text
L_0=sum_(j=0)^M f_jw^j,
T_0=sum_(j=0)^M f_(2M+1+j)w^j.                    (DPP4)
```

Its normalized square root is the unique `C_0(0)=1` satisfying

```text
C_0^2=L_0T_0/f_(2M+1) mod w^(M+1).                (DPP5)
```

The secondary coefficient at `z^(h-2)=z^(2M-1)` is automatic. The complete
remaining secondary condition is the single scalar equation

```text
[w^M]C_0=0.                                        (DPP6)
```

Both nonautomatic equations are univariate after normalization. Set
`x=uw`, `t=v/u`, and

```text
((1-x)(1-tx))^(-1/4)=sum_(j>=0)F_j(t)x^j.          (DPP7)
```

Then `t^(8M)=1`, `t!=1`, and

```text
4jF_j=(4j-3)(1+t)F_(j-1)-(4j-6)tF_(j-2),          (DPP8)
F_(-1)=0,       F_0=1.
```

The deleted-pair stratum is therefore reduced exactly to

```text
F_(2M)(t)=0,       F_(2M+1)(t)!=0,       G_M(t)=0, (DPP9)
```

on `t in mu_(8M)\{1}`, where `G_M(t)` is the coefficient `[x^M]` of the
unique normalized square root obtained from `(DPP4)--(DPP5)` with `f_j`
replaced by `F_j(t)`.

This theorem neither proves that `(DPP9)` is empty nor addresses deleted-root
quadruples that are not two antipodal pairs.
