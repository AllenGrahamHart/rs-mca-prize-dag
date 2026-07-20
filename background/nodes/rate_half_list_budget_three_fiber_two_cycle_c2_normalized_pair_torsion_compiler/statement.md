# Budget-three fiber-two c=2 normalized pair-torsion compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_canonical_span_criterion`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_joint_pair_torsion_selector`

Work in the official generic `c=2` canonical chamber and put

```text
N=2^40,       h=2^37+1.
```

Let `{A,B}` be a pair selected by the joint pair-torsion gate and let
`{C,D}` be the complementary denominator roots. Choose the orientation `A`
and apply the common subgroup scaling `lambda=A^(-1)`. Put

```text
t=B/A,       c=C/A,       d=D/A,
S=c+d,       P=cd,
D_A(Y)=A^(-4)D_*(AY)=(Y-1)(Y-t)(Y^2-SY+P).         (C2N1)
```

The normalized canonical outer coefficients and invariants are

```text
(alpha_A,beta_A,gamma_A)
 =(lambda^(2h)alpha,lambda^(3h)beta,lambda^(4h)gamma),
I_A=lambda^(4h)I,       J_A=lambda^(6h)J.            (C2N2)
```

For

```text
z=(1+t)^2/t=t+t^(-1)+2,
K_A(Z)=4I_A^3 Z(Z-36)^2-J_A^2(Z+12)^3,              (C2N3)
```

the selected pair has the required completion-root coupling and quotient
torsion exactly when

```text
K_A(z)=0,       t^N=1.                              (C2N4)
```

The complementary roots have an exact scalar torsion compiler. Starting
from

```text
t_0=t,       T_0=S,       P_0=P,
t_(j+1)=t_j^2,
T_(j+1)=T_j^2-2P_j,
P_(j+1)=P_j^2,             0<=j<40,                 (C2N5)
```

one has

```text
t,c,d in mu_N
  iff t_40=1,       T_40=2,       P_40=1.            (C2N6)
```

The normalized squarefree/split chamber retains

```text
tP(t-1)(1-S+P)(t^2-St+P)(S^2-4P)!=0,               (C2N7)
```

the requirement that `Y^2-SY+P` split over the base field, and that
`1,t,c,d` be base-field squares. Reversing the orientation of the selected
pair gives the exact involution

```text
(t,S,P) -> (t^(-1),S/t,P/t^2).                     (C2N8)
```

Thus every selected `c=2` survivor and only such a survivor is represented
by one role-labelled `(t,S,P)` chamber modulo `(C2N8)`, together with the
already printed primary gap, secondary gap, canonical-span identity, and
outer splitting. There is no remaining six-pair union.

This is an exact normalization and torsion compiler, not an exclusion. It
does not make the official canonical series constant-degree, eliminate the
normalized chamber, reconstruct a full cycle, or authorize a large
computation.
