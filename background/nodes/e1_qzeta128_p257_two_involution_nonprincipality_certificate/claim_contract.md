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

## Conditional claim

`J_63` and `J_65` are both nonprincipal.

## Proved input

`e1_qzeta128_p257_j65_harbater_nonprincipality` proves `J_65`
nonprincipal by an exact Hilbert-class-field Artin symbol.

## Exact open premise

`e1_qzeta128_p257_j63_fixed_field_nonprincipality_certificate` asks for
nonprincipality of the prime

```text
p_66=(257,zeta_128-zeta_128^(-1)-66)
```

in the degree-32 fixed field of `sigma_63`. The proof in `proof.md` transfers
that certificate to `J_63`.

It is not necessary to determine the complete class group, its complete
Galois action, all 64 prime coordinates, or to test `J_65` again. A complete
certified class-group calculation remains an acceptable stronger packet.

## Nonclaims

- A GRH-only class coordinate is insufficient.
- `bnfcertify(B,1)` alone is insufficient: it certifies only that the true
  class group is a quotient of the computed group, so a computed nonzero
  coordinate may disappear in that quotient.
- The published `359057,29301` ledger is evidence, not the remaining
  certificate.
- `J_65` alone is insufficient for the two-involution reduction; `J_63`
  remains required.

## Consumer

`e1_qzeta128_p257_class_orbit_certificate`.
