# Budget-three antipodal generic deleted-pair fourth-root gcd gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_ode`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_fourth_power_router`

Retain the official nonharmonic fourth-power-router data. Thus `N=8M`,

```text
Q=(x^N-1)/D_0,       A=xU_0^2,       R=Q-A^2=AS+T,   (FGG1)
```

and the constant ODE has scalar `kappa!=0`. Define

```text
P=2N+kappa x^2U_0^3.                                 (FGG2)
```

Then the following exact differential identity holds:

```text
2xD_0R'=P+2(ND_0-xD_0')R.                           (FGG3)
```

If one of the three nonharmonic scalar branches passes and

```text
T=W^4,       deg W=M-1,                              (FGG4)
```

then

```text
W divides P,
S divides P^2,
deg gcd(S,P)>=M-1.                                   (FGG5)
```

Thus every complete deleted-pair survivor must pass a deterministic
half-degree gcd gate before a fourth root or outer ratio is constructed. A
classifier may compute `P mod S`, and then `(P mod S)^2 mod S`, instead of
forming `P^2`.

This theorem is a necessary gate, not a converse. It does not prove the gcd
bound fails uniformly, and it does not provide a compressed official-degree
representation of `S`.
