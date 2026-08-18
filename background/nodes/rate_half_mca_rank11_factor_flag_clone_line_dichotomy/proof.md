# Proof

For every deep residual class `i`, choose a `b`-element subset `Z_i` of its
common-zero coordinates and let `mu_i` be its first-owned slope mass. Then

```text
sum_i mu_i C(|Z_i|,3) >= E C(b,3).                    (1)
```

Fix a coordinate triple `T` whose three evaluation columns on `B` have rank
three. Their common kernel in the five-space `B` has dimension two. Every
residual space `B_i` vanishing on `T` is contained in that kernel; since
`dim B_i` is two or three, it must equal the kernel and have dimension two.
All slopes counted at `T` therefore lie in the one correction space
`P ker(ev_T)`, of dimension at most four. Chronology-safe ownership bounds
their total weight by `R_4`.

There are at most `C(U,3)` rank-three triples, so subtracting their maximum
contribution from `(1)` proves `(CL1)`.

Now partition the nonzero evaluation columns of `B` by projective
proportionality. A rank-one coordinate triple lies in one clone class `D`.
All residual classes vanishing at any coordinate in `D` lie in the common
hyperplane

```text
B_D=ker(ev_x:B->F),  x in D,
```

and all their corrections lie in `P B_D`, of dimension at most eight. Let
`mu_D` be the complete first-owned slope mass of these residual classes.
Thus `mu_D<=R_8`; call `D` active when `mu_D>0`.

If every clone class has size at most `C`, convexity of `binom(c,3)` shows
that its sum over a partition of at most `U` coordinates is maximized by
as many size-`C` classes as possible and one remainder. Hence rank-one
triples contribute at most

```text
R_8 T_clone(C).                                      (2)
```

After subtracting `(2)` from `(CL1)`, every remaining low-rank weighted
incidence belongs to a rank-exactly-two triple. There are at most `C(U,3)`
such triples, proving `(CL2)` by averaging.

At `C=10000`, exact integer evaluation gives

```text
T_clone=18531303013296,
ceil((I_low-R_8 T_clone)/C(U,3))=777301822903.
```

If the clone-size hypothesis fails, one class has size at least `10001`.
This proves the one-sided displayed consequence of `(CL2)`.

It remains to retain mass on the large-clone horn. Set

```text
D_3=C(U,3),
A=I_low-R_8 T_clone(10000)
 =180088461956680275725075548840.
```

Take `L=388650911452` and suppose no genuine rank-two triple has mass at
least `L`. Since all masses are integers, the total rank-two incidence is at
most `(L-1)D_3`. Small active clone classes, those of size at most `10000`,
contribute at most `R_8 T_clone(10000)`. Therefore the incidence on active
clone classes of size at least `10001` is at least

```text
J=A-(L-1)D_3
 =90044230978447536156470456344.                       (3)
```

The clone classes partition at most `U` coordinates, so

```text
sum_D C(|D|,3) <= D_3.                                (4)
```

If every active large clone had `mu_D<=M-1`, its total rank-one incidence
would be at most `(M-1)D_3`. But exact division gives

```text
ceil(J/D_3)=388650911452=M,
```

contradicting `(3)` and `(4)`. Hence some active clone has size at least
`10001` and mass at least `M`, or the assumed rank-two bound fails and some
genuine rank-two triple has mass at least `L`. This proves `(CL3)`. QED.
