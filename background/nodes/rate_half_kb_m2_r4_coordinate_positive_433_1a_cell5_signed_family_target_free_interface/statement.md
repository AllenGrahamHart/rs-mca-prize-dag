# KoalaBear positive 433-1a cell-5 signed-family target-free interface

- **status:** PROVED
- **scope:** principal cell 5, signs `(-1,-1)`, positive `433-1a -> O0b`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_universal_target_elimination_compiler`
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell5_ratio_exceptional_branch_exclusion`
- **consumer:** `rate_half_band_closure`

Use the sparse cell-5 normalization

```text
F(W)=N(W)/D(W),
S(z)=-Q(z)/(Delta D(z)),
Q(z)=z beta(z^2-1),                              (KBSF-1)
```

where `W=z^2`, `D=A_2`, `N=A_0`,
`Delta=t^2(t^2-1)`, and
`beta=-t(1+b)D(t^2)`.  Thus `F(z^2)` is the target product and `S(z)` is
the unsquared target-root sum at source root `z`.

For three proposed source roots `z_0,z_1,z_2`, put

```text
D_i=D(z_i^2),   N_i=N(z_i^2),   Q_i=Q(z_i).       (KBSF-2)
```

On the guarded stratum `Delta D_0 D_1 D_2 != 0`, the three signed records

```text
DE+ at z_0,      DE- at z_1,      BE at z_2       (KBSF-3)
```

are realizable by target roots `d,e` if and only if the following four
target-free equations hold:

```text
N_1 D_0+N_0 D_1=0,                               (KBSF-4)

Q_0^2 D_1^2-Q_1^2 D_0^2
  -4 N_0 Delta^2 D_0 D_1^2=0,                    (KBSF-5)

2 N_2 Delta D_0 D_1
  -b D_2(Q_1 D_0-Q_0 D_1)=0,                     (KBSF-6)

-2 Q_2 D_0 D_1-2b Delta D_0 D_1 D_2
  -D_2(Q_1 D_0-Q_0 D_1)=0.                       (KBSF-7)
```

The same theorem holds for `DF+`, `DF-`, `CF` after replacing `(d,e,b)`
by `(d,f,c)` and replacing `b` by `c` in `(KBSF-6)--(KBSF-7)`.

There is an additional exact simplification for the `BE` row.  Define its
endpoint polynomial

```text
E_b(z)=Delta[b^2 D(z^2)+N(z^2)]+b Q(z).          (KBSF-8)
```

In this cell it factors over the deployed field as

```text
E_b(z)=2bt(t^2-1)(z-t) R_b(z),                   (KBSF-9)
```

where `R_b` has degree three in `z`, total degree fourteen, and 120 terms.
The root `z=t` is the already-used common `AB+1` incidence.  Therefore an
outside `BE` root `z_2`, guarded distinct from `t`, satisfies its product
and unsquared-sum rows with target root `e` if and only if

```text
R_b(z_2)=0,
Q_2+(b+e) Delta D_2=0.                           (KBSF-10)
```

This removes both target variables while preserving the unsquared Vieta
signs.  It does not prove the seven-variable guarded system empty, impose
source-slot distinctness, delete cell 5 or `433-1a -> O0b`, close K3, a
Prize row, or either Prize result.

## Falsifier

An actual signed-family lift violating one of `(KBSF-4)--(KBSF-7)`, or a
guarded solution of those four equations for which the reconstruction in
the proof fails.
