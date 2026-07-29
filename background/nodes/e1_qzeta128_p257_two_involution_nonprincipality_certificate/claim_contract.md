# Claim contract

## Exact objects

In `K=Q[x]/(x^64+1)`, with `zeta=x mod (x^64+1)`, set

```text
q_1 =(257,zeta-9),
q_63=(257,zeta-57),
q_65=(257,zeta-248),
J_63=q_1 q_63,
J_65=q_1 q_65.
```

## Direct claim

`J_63` and `J_65` are both nonprincipal.

## Required certificate

An acceptable packet supplies, for each ideal, an unconditional exact class
coordinate, an explicit nonzero image under a certified ideal-class
character, or another proof-producing nonprincipality obstruction. The
primary computation and an independently implemented exact audit must agree.

It is not necessary to determine the complete class group, its complete
Galois action, or all 64 prime coordinates. A complete certified class-group
calculation remains an acceptable stronger packet.

## Nonclaims

- A GRH-only class coordinate is insufficient.
- `bnfcertify(B,1)` alone is insufficient: it certifies only that the true
  class group is a quotient of the computed group, so a computed nonzero
  coordinate may disappear in that quotient.
- The published `359057,29301` ledger is evidence, not this certificate.
- Nonprincipality of only one of the two ideals is insufficient for the
  two-involution reduction.

## Consumer

`e1_qzeta128_p257_class_orbit_certificate`.
