# Proof

The ambient lift and the cancellation used in the heavy-incidence theorem
give the exact section identity

```text
s_F^3 G_L/P_Z=R_a|_C,                                  (1)
```

where `P_Z` is the squarefree supported-slope locator.  Fix a heavy
supported incidence `(gamma,x)` with `R_a(x)!=0`.  Both `G_L` and `R_a` are
units in the local ring `O_(C,(gamma,x))`; all factors of `P_Z` other than
`L_gamma` are units.  After locally trivializing the contact line bundle,
equation `(1)` therefore says

```text
L_gamma=u s_F^3                                        (2)
```

for a unit `u`.

The reduced biform curve is Cartier in a smooth surface, hence its local
ring is one-dimensional Cohen--Macaulay.  No horizontal line contains a
component, so `L_gamma`, and therefore `s_F`, is a nonzerodivisor.  Thus

```text
length O_C/(L_gamma)=length O_C/(s_F^3)
                     =3 length O_C/(s_F).              (3)
```

The left side is the multiplicity of `x` as a root of
`Qbar_gamma(X)`. The contracted recurrence factorization is

```text
Qbar_gamma=Q_min R_gamma,       deg R_gamma=c_gamma,    (4)
```

The squarefree `Q_min` contains either one copy of `x` or none. In the first
case, the positive multiple-of-three multiplicity in `(3)` leaves at least
two copies in `R_gamma`; in the second, all copies lie in `R_gamma`, so it
contains at least three. Thus every incidence under consideration consumes
at least two excess degrees. Distinct grid incidences give disjoint
root-degree charges. At a heavy
incidence where `R_a(x)=0`, the preceding heavy-incidence theorem still
places at least one copy in `R_gamma`.  Summing proves `(CTP2)`.

Write

```text
u=Delta-I_H,       v=Delta-O.                          (5)
```

Since `2I_0+I_E=I_H+I_0`, `(CTP2)` gives

```text
I_0<=u.                                                (6)
```

### Core zero, `a=2`

The exact gap identity is `u+v=1`.  There are at most two exceptional
heavy rows, and each heavy row has at most `e-1` supported incidences.  If
`u=0`, then `(6)` gives `I_0=0` and hence

```text
I_E=I_H=Delta=2e-1>2(e-1),
```

a contradiction.  Therefore `u=1,v=0`, proving
`I_H=2e-2` and `O=Delta`.  Equation `(6)` leaves `I_0=0` or `1`, and

```text
I_E=2e-2-I_0.                                         (7)
```

One exceptional row cannot carry `(7)`, so the two roots of `R_2` are
distinct heavy rows.  Their deficit sum is

```text
c_1+c_2=2e-I_E=2+I_0.                                 (8)
```

Both deficits are positive, yielding exactly `(CTP4)`.  Finally
`O=Delta<=sum c_gamma<=Delta`, so the total excess degree is also exactly
`Delta`.

### Core one, `a=1`

Now `u+v=2`.  If the unique root of `R_1` were not a heavy row, then
`I_E=0`; equations `(CTP2)` and `(5)` would give

```text
2(Delta-u)<=Delta
```

for `u<=2`, impossible on the official row.  Hence the root `x_*` is heavy
and is the only exceptional row.  Equations `(5),(6)` give

```text
0<=I_0<=u,
d_(x_*)=I_E=Delta-u-I_0,
c_(x_*)=e-d_(x_*)=2+u+I_0.                            (9)
```

Enumerating `u=0,1,2` and `0<=I_0<=u`, with `v=2-u`, gives the six entries
of `(CTP5)`.  Since `B` already contains the heavy factor `X-x_*` and
`R_1` is its scalar multiple, `A_0` has a double root there.  The largest
printed deficit is six, and the largest `I_0` is two.  QED.
