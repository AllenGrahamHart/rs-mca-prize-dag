# `A=1` core-one exceptional-only factor descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction`

Retain the exceptional-only boundary profile from `(ACR6)`:

```text
b=0,       D_*=1,       c=z=1,       X_1=1.          (EFD1)
```

Write `E=E_Z`, `P=P_cl E`, and use the active reduced forms, so

```text
Q V+P_X W=P,
Q A+P_cl B=P_X,
W B-E=Q K.                                            (EFD2)
```

Here `e_*=e`, `r=2e+1`, and the unique zero-trace bad row `x_0` has no
exceptional incidence. If `gamma_0` is the root of `E`, then

```text
q_0=Q(gamma_0;X) | P_X,
deg q_0=r-1,
H=P_X/q_0,       deg H=D_0-r.                         (EFD3)
```

There is a unique polynomial `J(X)` satisfying

```text
B(gamma_0;X)=q_0J,       deg J=D_0-r.                 (EFD4)
```

Moreover there are biforms `B_1,A_1,K_1` such that

```text
B=QJ+E B_1,       A_1=A+P_cl J,
K-WJ=E K_1,                                            (EFD5)

Q A_1+P B_1=P_X,
W B_1-1=Q K_1,
V B_1+A_1=-P_X K_1.                                  (EFD6)
```

The exceptional specialization and exact `X`-degree are

```text
A_1(gamma_0;X)=H,       deg_X A_1=D_0-r.              (EFD7)
```

Thus the exceptional-only active system descends to a complement square
with no exceptional factor on its right side. It is not the already-excluded
trace-free square: the correction `P_clJ` raises the available `X`-degree
from `D_0-r-1` to exactly `D_0-r`. This one-degree relaxation is the complete
remaining obstruction in this profile. The theorem does not exclude the
reduced square or close the core-one face.
