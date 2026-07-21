# Budget-three fiber-two c=2 one-antipodal product/ratio trace compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_primary_torsion_reducer`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router`

Retain the official one-antipodal normalization

```text
Omega={1,-1,c,d},       N=2^40,
S=c+d,       P=cd,       X=S^2.                         (PRT1)
```

Put

```text
t=c/d,       Z=t+t^(-1).                                (PRT2)
```

Then the sign-free primary variables satisfy

```text
X=P(Z+2).                                                (PRT3)
```

Define the product and trace towers by

```text
P_0=P,       Z_0=Z,
P_(j+1)=P_j^2,       Z_(j+1)=Z_j^2-2,       0<=j<39.   (PRT4)
```

The complementary pair lies in `mu_N` exactly when

```text
P_39^2=1,       Z_39=2P_39.                             (PRT5)
```

Consequently the exactly-one-antipodal primary/torsion circuit is
equivalently

```text
F_H(P(Z+2),P)=G_H(P(Z+2),P)=0,
P_39^2=1,       Z_39=2P_39,
(Z^2-4)(1+P^2-PZ)!=0.                                  (PRT6)
```

Every solution reconstructs one unordered complementary pair modulo the
common sign `(c,d)->(-c,-d)`. No separate square test for `X` remains.

The official field split sharpens as well. In the fixed chamber,

```text
P,Z in F_p.                                             (PRT7)
```

In the reciprocal quadratic chamber,

```text
Z in F_p,       P^p=P^(-1).                            (PRT8)
```

Thus the ratio trace always descends to the prime field, while only the
product may lie on the norm-one torus. This is an exact reconstruction and
field router. It does not prove `(PRT6)` empty, use the secondary gap, or
prove the antipodal-free part of C2-PAR.
