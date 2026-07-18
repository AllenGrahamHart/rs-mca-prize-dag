# Cubic block-tail energy insufficiency

- **status:** see `dag.json` (single source of truth)
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_quotient_block_identity`,
  `f3_h3_identity_deficit_energy_close`

For every official order `n=2^s` with `22<=s<=41`, there is a finite multiset
of abstract quotient-block sizes `m_B>=2` satisfying

```text
sum_B m_B(m_B-1)=(n-1)(n-2),                    (CT1)
#{B:m_B>=tau} <= 4n^2/tau^3       (tau>=2),     (CT2)
```

but whose induced quotient-energy profile obeys

```text
(n-1)^2+sum_B m_B(m_B-1)^2
  > (145/4)(n-1)^2.                              (CT3)
```

The profile is explicit. For powers `m=2^j`, `3<=j<=s`, put

```text
q_m=floor(3n^2/m^3),
```

discard zero counts, and fill the remaining mass in `(CT1)` with blocks of
size two.

Thus the exact quotient mass identity plus a cubic block-count tail with
constant four do not logically imply the clean C36' energy premise. This is
an abstract nonimplication theorem, not a subgroup-realizability claim and not
a counterexample to C36'. A successful energy proof must use additional joint
or source-specific structure.
