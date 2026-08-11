# `A=1` core-one signed-packet exact local normal forms

- **status:** PROVED
- **closure:** exact excess-root, vertical-fibre, and contact-divisor ledger
- **consumer:** `rate_half_band_crossing_location`

Retain one of the three core-one scalar packets with ordinary heavy
incidences:

```text
(u,v,I_0,c) in {(1,1,1,4),(2,0,1,5),(2,0,2,6)}.     (SLN1)
```

Use `R_*`, `R_0`, `Z_c`, and `E_u` as in the six-packet bounded-divisor
normal form. Let `V_*` be the complete vertical fibre over the distinguished
domain point. The three packets have the following exact forms.

```text
(1,1,1,4):
  V_*=R_*+A+3B,       E_1=B,
  O_C(rho+2,-e-1)=O_C(A+2B-R_0),                    (SLN2)

(2,0,1,5):
  V_*=R_*+2A+3B,      E_2=A+B,
  O_C(rho+2,-e-1)=O_C(A+2B-R_0),                    (SLN3)

(2,0,2,6):
  V_*=R_*+3B,         E_2=B,
  O_C(rho+2,-e-1)=O_C(2B-R_0).                      (SLN4)
```

In `(SLN2)`, `A` is the unique distinguished incidence whose excess root
does not overlap the squarefree minimal recurrence locator, and
`deg A=deg B=1`. In `(SLN3)`, every excess root overlaps the minimal
locator, `A` is the unique distinguished incidence carrying a second excess
copy, and `deg A=deg B=1`. In `(SLN4)`, every distinguished incidence
carries one excess copy, every excess root overlaps the minimal locator,
and `B` is effective of degree two. The support of `B` may overlap `R_*`
or `A`.

Every ordinary incidence in all three packets has one minimal and two
excess copies, horizontal multiplicity three, and contact multiplicity one.
Thus ordinary incidences contribute exactly `R_0` and no part of `E_u`.

## Scope

The theorem does not assert that the signed degree-two classes in
`(SLN2)`--`(SLN4)` are effective, classify their pushforwards, or exclude
any of the three packets.
