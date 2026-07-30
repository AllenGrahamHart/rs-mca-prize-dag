# Q(zeta_128) J_63 residue obstruction

- **status:** PROVED
- **closure:** explicit auxiliary-prime power-residue character

Let `ell=21121`, let `alpha` be the Jacobi element from
`e1_qzeta128_p257_j63_stickelberger_relation`, and put

```text
I=(q_1 q_63)/(q_127 q_65).
```

At the auxiliary prime

```text
r=5406977=256*ell+1,
```

an explicit product of 32 `ell`th-power residue characters kills every
global unit and every `ell`th power, but sends `alpha` to

```text
500235 != 1 mod r.                                  (RO1)
```

Consequently `I` and `J_63=q_1q_63` are nonprincipal.

## Falsifier

Failure of primality of `r`, a unit generator with nontrivial character, or
an exact reduction of `alpha` different from `(RO1)`.
