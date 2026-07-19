# Budget-three antipodal generic Euler maximal-field character shard

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_euler_coupled_norm_gate`,
  `rate_half_list_budget_three_maximal_field_degree_collapse`

Work over the ambient admissible field `F_q` on the maximal rate-half row.
Write `q=p^e`. Every generic-floor candidate is subject to the Euler cubic
and fourth-power norm gates. Their activation is exactly:

```text
e=1: q=p,   gcd(4,q-1)=4,
               gcd(3,q-1)=3 if p=1 mod 3,
               gcd(3,q-1)=1 if p=2 mod 3;

e=2: q=p^2, gcd(4,q-1)=4, gcd(3,q-1)=3.            (MCS1)
```

There are no other ambient field-degree shards. Consequently the fourth-
power test

```text
N_Q^((q-1)/4)=1                                    (MCS2)
```

is active in every maximal-row branch. The cubic test

```text
N_T^((q-1)/3)=1                                    (MCS3)
```

is active in every quadratic-extension branch and in precisely the
`p=1 mod 3` prime-field branch. It is vacuous only in the prime-field
`p=2 mod 3` shard. The exact coupling `N_T^4N_Q^3=d^(4v)` remains mandatory
in all shards.

This table is over the ambient `F_q`. If a specialized sublane proves that
its data descend from `F_(p^2)` to `F_p`, character membership must be
recomputed in `F_p`; the ambient table must not be relabelled as a descended-
field character test. These scalar tests remain necessary, not sufficient.
