# Budget-three deleted-pair primary/Legendre torsion-necessity fence

- **status:** PROVED
- **closure:** exact arithmetic certificate
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_legendre_collapse`

The source-torsion condition is essential in any attempt to combine the
primary gap with the three Legendre gates. More precisely, set `M=1`, so

```text
F_2(t)=(5t^2+2t+5)/32,
H_3(t)=(5t^3+3t^2+3t+5)/16.                         (TLF1)
```

For each branch `j=0,1,2`, the following row gives a prime `p>16`, a nonzero
`r in F_p`, and `t=r^4`:

```text
j   p                           r
0   384690601                   362094250
1   114830041                   53151121
2   96186353595534244333511041  24643621616413434900523946.   (TLF2)
```

Every row satisfies

```text
F_2(t)=0,       F_3(t)!=0,                            (TLF3)
```

and its matching equation from `(LCC6)`. Thus primary nonvanishing plus one
Legendre branch is not uniformly contradictory in good characteristic.
However, the three rows respectively have

```text
r^32=15359535,
r^32=36780295,
r^32=16136690780167816062921118,                    (TLF4)
```

in their printed fields, and none is one. Since source torsion at `M=1`
requires `r^32=1`, these are route fences, not deleted-pair survivors.

Consequently a valid resultant, holonomic, or nonvanishing proof must retain
`r^(32M)=1` (equivalently `t^(8M)=1`) before claiming uniform failure. This
theorem makes no assertion about the complete three-condition system.
