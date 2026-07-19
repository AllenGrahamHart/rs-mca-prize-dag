# Budget-three deleted-pair Chebyshev/Gegenbauer sign router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_legendre_collapse`

Retain a correctly posed nonharmonic deleted-pair scalar candidate. Put

```text
L=2M,       y=(r+r^(-1))/2,       x=2y^2-1,
epsilon=r^(8L),       P=P_(2L-1)(x),                    (CGR1)
```

where `P_n` is the ordinary Legendre polynomial. Then source torsion and the
primary gap are exactly

```text
epsilon^2=1,       T_(8L)(y)=epsilon,
C_L^(1/4)(x)=0.                                      (CGR2)
```

Here `T_n` is the first-kind Chebyshev polynomial and `C_n^(1/4)` is the
Gegenbauer polynomial. Moreover

```text
t H_(2L-1)(t)^2=epsilon P^2.                         (CGR3)
```

Consequently the three equations `(LCC6)` are respectively equivalent to

```text
j=0:       epsilon P^2+(2y-1)^2=0,
j=1:       epsilon P^2(y-1)^2+(y+1)^2=0,
j=2:       epsilon P^2y^2+(y-2)^2=0.                 (CGR4)
```

The official split branch contains a fourth root `iota` of `-1`. Choose
`s` from the two-element set defined by `s^2=-epsilon`; thus
`s in {1,-1}` when `epsilon=-1` and
`s in {iota,-iota}` when `epsilon=1`. The squared equations `(CGR4)` split
exactly into the six linear-sign branches

```text
j=0:       P=s(2y-1),
j=1:       P(y-1)=s(y+1),
j=2:       Py=s(y-2).                                (CGR5)
```

Thus a correctly posed elimination needs only one Chebyshev torsion sign,
one Gegenbauer primary equation, and six unsquared Legendre equations in the
single trace variable `y`. This theorem does not prove that any branch in
`(CGR5)` is empty.
