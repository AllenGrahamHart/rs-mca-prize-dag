# `A=1` core-free cubic double-root gap-one normal forms

- **status:** PROVED
- **closure:** exact four-packet and degree-one Picard ledger
- **consumer:** `rate_half_band_crossing_location`

Retain the core-free cubic scalar branch with

```text
u=1,
R_3=(X-x_d)^2(X-x_s),                                (DGN1)
```

where both distinct roots are heavy. Write `c_s,c_d` for the simple- and
double-root row deficits, `epsilon_s,epsilon_d` for their extra excess
multiplicities, `t_s,t_d` for their new-root counts, and
`w=Delta-C_tot`. The complete packet table is

```text
I_0  c_s c_d  epsilon_s epsilon_d  w   t_s   t_d
 0    1   1       0         0      1    1    e-2
 0    1   1       1         0      0    2    e-2
 0    1   1       0         1      0    1    e-1
 1    2   1       0         0      0    2    e-2.     (DGN2)
```

There is no excess degree outside the two root rows and the possible
ordinary incidence. In the last packet the ordinary incidence has one
minimal and two excess copies, horizontal multiplicity three, and contact
multiplicity one.

Let `R_s,R_d` be the reduced distinguished divisors. There are reduced
points or divisors on their vertical fibres such that

```text
I_0=0:
  V_s=R_s+A,       V_d=R_d+P,
  div(s_F)=R_s+R_d+P;

I_0=1:
  V_s=R_s+A+B,     V_d=R_d+P,
  div(s_F)=R_s+R_d+Q+P,                              (DGN3)
```

where `Q=R_0` is the ordinary point. Consequently

```text
L_1:=O_C(rho+3,-e-1)
 =O_C(A)           if I_0=0,
 =O_C(A+B-Q)       if I_0=1.                         (DGN4)
```

The section counts are

```text
h^0(C,L_1)=1 if I_0=0,
h^0(C,L_1)=0 if I_0=1.                               (DGN5)
```

## Scope

The theorem does not exclude any of the four packets. It does not cover the
squarefree cubic branch or `u>=2`.
