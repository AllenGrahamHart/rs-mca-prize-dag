# Claim contract

## Direct claim

In `Q(zeta_128)`, the ideal

```text
(257,zeta_128-9)(257,zeta_128-248)
```

is nonprincipal.

## Imported theorem

Dembele identifies the degree-16 CM field
`E=Q(i(zeta_64+zeta_64^(-1)))`, proves that it has class number 17, relates
its Hilbert class field to the Harbater field, and records Elkies's defining
degree-17 polynomial for that field.

## Replayed finite claim

The published polynomial is irreducible modulo 257. The repository verifier
checks this with the exact finite-field irreducibility criterion, without a
CAS or a probabilistic primality/factorization routine.

## Consumer

`e1_qzeta128_p257_two_involution_nonprincipality_certificate`.
