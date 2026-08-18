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
All residual classes vanishing on `D` lie in the hyperplane

```text
B_D=ker(ev_x:B->F),  x in D,
```

and all their corrections lie in `P B_D`, of dimension at most eight. Thus
the complete first-owned slope mass attached to one clone class is at most
`R_8`.

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
This proves the displayed dichotomy. QED.
