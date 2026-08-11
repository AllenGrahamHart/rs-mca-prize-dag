# `A=1` core-one signed packets have no degree-two section

- **status:** PROVED
- **closure:** length-three nilpotent modification and ordinary-point removal
- **consumer:** `rate_half_band_crossing_location`

Retain any signed tangent packet and write its exact local normal form as

```text
L_2=O_C(rho+2,-e-1)=O_C(P_3-R_0),                    (SSV1)
```

where

```text
P_3=A+2B for (u,v,I_0,c)=(1,1,1,4),(2,0,1,5),
P_3=2B   for (u,v,I_0,c)=(2,0,2,6).                  (SSV2)
```

In every case `P_3` is an effective degree-three proper subdivisor of the
vertical fibre over `x_*`, while `R_0` is a nonempty reduced divisor on
other domain fibres. For the domain projection `pi:C->P^1_X`,

```text
pi_*O_C(P_3)
 =O direct_sum O(1-d)^3 direct_sum O(-d)^(e-4),
h^0(C,O_C(P_3))=1.                                   (SSV3)
```

Its unique section is the canonical section cutting out `P_3`. It is
nonzero on `R_0`, and therefore

```text
h^0(C,L_2)=h^0(C,O_C(P_3-R_0))=0.                    (SSV4)
```

## Scope

The theorem classifies the section count of all three signed packets. It
does not exclude them: no prior input requires `L_2` to have a nonzero
section.
