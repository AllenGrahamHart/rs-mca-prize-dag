# Budget-three antipodal generic deleted-pair constant-coefficient gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_fourth_power_router`

Retain the official nonharmonic deleted-pair normalization. Thus

```text
t=r^4,       D_0=(x-1)(x-t),       Q=(x^N-1)/D_0,
A=xU_0^2,       R=Q-A^2=AS+T,       N=8M.            (CCG1)
```

Put `a=4M-1`, `s=2M-2`, and assume the required `deg S=s` gate. In a new
reversal variable `z`, define

```text
A_rev=z^aA(z^(-1)),       R_rev=z^(a+s)R(z^(-1)),
sigma=[z^s](R_rev/A_rev mod z^(s+1)).                 (CCG2)
```

Then `sigma=S(0)`. Put `chi=r+r^(-1)`. A complete deleted-pair survivor on
pairing branch `j` must satisfy the corresponding single scalar equation

```text
j=0:       t sigma^2+4(chi-1)^2=0,
j=1:       t(chi-2)^2 sigma^2+4(chi+2)^2=0,
j=2:       t chi^2 sigma^2+4(chi-4)^2=0.             (CCG3)
```

Thus the constant term of the scalar polynomial identity is an exact first
rejection gate. It requires one terminal coefficient of a length-`s+1`
reversed quotient, not the full Euclidean remainder, a polynomial gcd, or a
fourth root.

This theorem does not prove that `(CCG3)` fails uniformly. It also does not
compress the coefficient extraction in `(CCG2)` below its printed truncated-
series length.
