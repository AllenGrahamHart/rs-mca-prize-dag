# Budget-three fiber-two c=1 parity Frobenius router

- **status:** PROVED
- **closure:** proof plus exact arithmetic certificate
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_mobius_router`,
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_nonharmonic_scalar_compiler`

Retain the official nonharmonic `c=1` parity compiler. Thus

```text
M=2^36,       L=2^39,       q_field=p^2,
p=1 mod 2L,       r^(4L)=1,       r^4!=1,            (CFR1)
```

and an accepted source branch has base-field outer trace
`y_Xj=tau(z_Xj) in F_p`.

For all five source branches

```text
R1, R2, P0, P1, P2,                                  (CFR2)
```

every accepted lift lies in `F_p`. The `R0` trace is identically invariant
under `r -> -r`, so `R0` is the sole branch on which an anti-invariant top
lift can remain.

More precisely, in the nonsplit congruence shard write `r^p=-r`. Equality of
the source trace with its Frobenius conjugate has the following complete
zero loci, after removing nonzero denominators and scalars:

```text
R1,R2: (r^2+iota)(r^4+8iota r^2-1)=0,
P0:    r^2+1=0,
P1:    5r^2-3-4iota=0,
P2:    5r^2-3+4iota=0.                              (CFR3)
```

The first `R1,R2` factor forces `r^4=-1` and is excluded by the primary gap;
`P0` contradicts `r^4!=1`. For the remaining factors put

```text
v=-iota r^2 on R1,R2,       u=r^2 on P1,P2.
```

They force the fixed reciprocal traces

```text
v+v^(-1)=-8,       u+u^(-1)=6/5,                    (CFR4)
```

with `u,v in mu_(2L)`. A preregistered 16-shard Modal campaign checked both
40-step trace terminals over every odd `k` in

```text
p=1+k*2^40,       29058991<=k<33554432.              (CFR5)
```

All `2,247,721` nonsplit candidate moduli were covered, including composites;
`449,544` multiples of five were rejected as composite before division. All
shards completed, the longest took 2.957014 seconds, and neither trace had a
hit.

The launcher, compact result, human-readable result, and independent checker
are

```text
experiments/prize_resolution/
  rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_modal.py
  rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_result.json
  rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_result.md
  rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_check.py
```

This theorem removes the top-lift extension from five branches only. It does
not exclude any Frobenius-invariant branch, the anti-invariant `R0` branch,
or any official polynomial packet.

