# Budget-three antipodal generic deleted-pair harmonic exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_mobius_ratio_router`,
  `rate_half_list_budget_three_maximal_field_degree_collapse`

On the maximal generic deleted-pair stratum, retain the only arithmetic branch
left by the Fourier-resultant theorem:

```text
N=2^38,       q_field=p^2,       p=1 mod 2^40,
3*2^128<=p^2<4*2^128.                                (HDE1)
```

Then the harmonic outer ratio is impossible:

```text
q=mu/lambda!=-1.                                      (HDE2)
```

Equivalently, the harmonic fourth-power alternative `(RSR5)` has no official
input. Every remaining deleted-pair candidate lies on a nonharmonic branch
and must pass the Euclidean quotient-square criterion `(RSR4)`.

The exhaustive arithmetic step in the proof is hash-pinned at

```text
experiments/prize_resolution/
  rate_half_list_deleted_pair_harmonic_characteristic_result.json
```

and covers all `4,495,441` congruence classes in the exact interval, including composite moduli.
This theorem does not exclude any nonharmonic ratio branch
or prove the full adjacent crossing.
