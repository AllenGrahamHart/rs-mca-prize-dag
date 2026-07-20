# Budget-three fiber-two c=2 normalized gap-span compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_maximal_field_degree_collapse`,
  `rate_half_list_budget_three_fiber_two_cycle_boundary_transfer`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_normalized_pair_torsion_compiler`

Retain the normalized generic `c=2` chamber and put

```text
N=2^40,       H=2^37+1,       r=2H-3=2^38-1,
E(z)=(1-z)(1-tz)(1-Sz+Pz^2)=sum_(j=0)^4 E_jz^j.
                                                               (C2G1)
```

Thus

```text
E_0=1,
E_1=-(1+t+S),
E_2=t+(1+t)S+P,
E_3=-(tS+(1+t)P),
E_4=tP.                                                 (C2G2)
```

Let `A=E^(-1/4)=sum_(n>=0)a_nz^n`, with `a_0=1`. Every coefficient needed by
the canonical certifier is generated without a formal radical by

```text
4n a_n=-sum_(j=1)^min(4,n)(4n-3j)E_j a_(n-j).          (C2G3)
```

All denominators in this recurrence are nonzero at the official row. The
primary gap is exactly

```text
a_(2H-2)=a_(2H-1)=0,       c=a_(2H)!=0.                (C2G4)
```

Put

```text
L=sum_(m=0)^(H-1)a_mz^m,
T=sum_(m=0)^(H-1)a_(2H+m)z^m.                          (C2G5)
```

The secondary gap is exactly the existence of the unique polynomial `C`
with

```text
C(0)=1,       deg C<=H-3,
LT=cC^2 mod z^H.                                      (C2G6)
```

There are no free canonical outer coefficients. Define

```text
B=sum_(m=0)^r a_mz^m,
Q=(1-z^N)/E,
R=Q-B^4,       Rbar=z^(-2H)R,
alpha=Rbar(0)=4c,
Sigma=Rbar-alpha B^2C^2,
X=z^HBC^3,       Y=z^(2H)C^4,
beta=[z^H]Sigma,
gamma=[z^(2H)](Sigma-beta X).                         (C2G7)
```

The canonical-span condition is the exact polynomial identity

```text
Sigma=beta X+gamma Y.                                 (C2G8)
```

Finally set

```text
I=alpha^2+12gamma,
J=72alpha gamma-27beta^2-2alpha^3,
z_t=(1+t)^2/t.                                        (C2G9)
```

The completion-root coupling of the selected `c=2` pair is the one scalar
equation

```text
4I^3 z_t(z_t-36)^2-J^2(z_t+12)^3=0.                  (C2G10)
```

Together with the torsion recurrences, distinctness, splitting, and square
conditions in the normalized-pair compiler, `(C2G3)--(C2G10)` are an exact
single-chamber decision interface. Every original generic `c=2` mismatch
survivor enters it, and every passing normalized packet reconstructs through
the existing canonical and completion-root converses. Pair reversal remains
the printed involution `(t,S,P)->(t^(-1),S/t,P/t^2)`.

This compiler does not prove the interface empty or make its official-order
evaluation cheap. It does not authorize `CR-002-C2N`; a compressed algorithm,
pilot, checker, resource ceiling, and complete official-field ledger are
still required.
