# Q(zeta_128) prime-257 class-orbit certificate

- **status:** CONDITIONAL
- **scope:** `K=Q(zeta_128)`, all degree-one primes above 257

Assume
`e1_qzeta128_p257_two_involution_nonprincipality_certificate`: for the
explicit primes

```text
q_1 =(257,zeta_128-9),
q_63=(257,zeta_128-57),
q_65=(257,zeta_128-248),
```

both `q_1 q_63` and `q_1 q_65` are nonprincipal. Then the 64 prime ideals of
`Z[zeta_128]` above 257 have pairwise distinct ideal classes.

This implication is proved in `proof.md`. It uses the unconditional facts
that the maximal real subfield has class number one and that the class number
of a 2-power cyclotomic field is odd.

An acceptable stronger certificate may prove the published class-index
description

```text
Cl(K) = Z/359057,
[q_1] = 1,
sigma_-1(e) = -e,
sigma_3(e) = 29301 e.
```

Here `q_1` is one prime above 257, `sigma_a(zeta_128)=zeta_128^a`, and the
index is chosen so that `q_1` has class one. The source evidence for these
exact integers is pinned in `source_evidence.md`, but the conditional proof
no longer requires them.

## Falsifier

An exact generator of `q_1 q_63` or `q_1 q_65`, or two distinct primes above
257 with the same certified ideal class.
