# Q(zeta_128) prime-257 two-involution nonprincipality certificate

- **status:** CONDITIONAL
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

Then both

```text
J_63=q_1 q_63,        J_65=q_1 q_65
```

are nonprincipal ideals of `Z[zeta]`, conditional only on
`e1_qzeta128_p257_j63_fixed_field_nonprincipality_certificate`.

The `J_65` assertion is proved unconditionally by
`e1_qzeta128_p257_j65_harbater_nonprincipality`. The remaining premise asks
whether the single prime

```text
(257,zeta_128-zeta_128^(-1)-66)
```

is nonprincipal in its degree-32 fixed field. The proved quadratic transfer
identifies this with nonprincipality of `J_63`.

The conjunction is the complete premise in the proved two-involution
reduction to pairwise separation of all 64 prime classes. Only its `J_63`
half remains open.

## Falsifier of the remaining premise

An exact generator of `J_63`, equivalently of the fixed-field prime above.
