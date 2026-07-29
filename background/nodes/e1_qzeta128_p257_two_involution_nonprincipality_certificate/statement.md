# Q(zeta_128) prime-257 two-involution nonprincipality certificate

- **status:** TARGET
- **scope:** two explicit ideals in `K=Q(zeta_128)`

Put `zeta=zeta_128`, and for odd `a mod 128` define

```text
q_a=(257,zeta-9^a),
```

where the residue is reduced modulo 257. The element `9` has order 128
modulo 257, so these are the 64 degree-one primes above 257. In particular,

```text
q_1 =(257,zeta-9),
q_63=(257,zeta-57),
q_65=(257,zeta-248).
```

Produce unconditional exact certificates that both

```text
J_63=q_1 q_63,        J_65=q_1 q_65
```

are nonprincipal ideals of `Z[zeta]`.

These two nonprincipality statements are the complete open premise in the
proved two-involution reduction to pairwise separation of all 64 prime
classes.

## Falsifier

An exact generator of either `J_63` or `J_65`.
