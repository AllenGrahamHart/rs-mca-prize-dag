# Budget-three fiber-two c=1 normalized torsion compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_fiber_two_cycle_c1_coefficient_resultant_elimination`

Work in the official generic `c=1` canonical chamber and put

```text
N=2^40,       h=2^37+1.
```

Index a passing packet by repeated square `A`, unused residual square
`C`, and complementary unpaired squares `{B,D}`. Common subgroup
scaling gives an equivalent packet with

```text
lambda=A^(-1),
b=B/A,       d=D/A,       c=C/A,
D_A(Y)=A^(-4)D_*(AY)=(Y-1)(Y-c)(Y^2-SY+P),
S=b+d,       P=bd.                                   (C1N1)
```

The normalized canonical outer coefficients and invariants are

```text
(alpha_A,beta_A,gamma_A)
 =(lambda^(2h)alpha,lambda^(3h)beta,lambda^(4h)gamma),
I_A=lambda^(4h)I,       J_A=lambda^(6h)J.            (C1N2)
```

Define

```text
X=1+P+3S,                    Y=1+P-9S,
E=Y-16P,                     F=16-Y,
J_even=4(E^2+PF^2),          J_odd=8EF,
I_even=X^3+192XP,            I_odd=-24X^2-512P,
K_0=I_A^3J_even-J_A^2I_even,
K_1=I_A^3J_odd-J_A^2I_odd,
N_1(S,P)=K_0^2-PK_1^2.                               (C1N3)
```

The old indexed norm and the normalized norm obey

```text
N_1(S,P)=A^(-(24h+12)) N_(A;B,D).                    (C1N4)
```

In particular, passage is exactly `N_1(S,P)=0`.

The three normalized quotient roots have a succinct exact torsion compiler.
Starting from

```text
T_0=S,       P_0=P,       c_0=c,
T_(j+1)=T_j^2-2P_j,
P_(j+1)=P_j^2,
c_(j+1)=c_j^2,             0<=j<40,                 (C1N5)
```

one has

```text
b,d,c in mu_N
  iff T_40=2,       P_40=1,       c_40=1.            (C1N6)
```

The normalized squarefree/split chamber retains

```text
P c(c-1)(1-S+P)(c^2-Sc+P)(S^2-4P)!=0,               (C1N7)
```

the requirement that `Y^2-SY+P` split over the base field, and that
`1,b,d,c` be base-field squares.

Thus, modulo the proved canonical covariance, every `c=1` survivor and
only such a survivor is represented by one role-labelled triple `(S,P,c)`
satisfying `(C1N3)--(C1N7)` together with the already printed primary gap,
secondary gap, canonical-span identity, and outer splitting. There is no
remaining union over a repeated root or unused root.

This is an exact normalization and torsion compiler, not an exclusion. It
does not make the official canonical series constant-degree, prove
`N_1!=0`, or authorize a large computation.

