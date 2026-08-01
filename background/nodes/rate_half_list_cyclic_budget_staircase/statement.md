# Rate-half list cyclic budget staircase

- **status:** PROVED
- **closure:** proof
- **scope:** the official rate-half row `n = 2^41`, `k = 2^40`, every
  admissible field (the count is field-independent)
- **dependencies:** `rate_half_cyclic_rotated_prefix_floor` (instantiated at
  `d = 1`, `s = c-1`)
- **consumer:** `rate_half_list_adjacent_crossing` (evidence)
- **provenance:** surfaced by the Brief-6 Pro dossier
  (`notes/pro_briefs_20260801/responses/BRIEF6_PRO_DOSSIER.md`) as a direct
  consequence of the banked cyclic theorem; audited and replayed on our side
  2026-08-01.

For each dyadic quotient order `N_0` with `8 <= N_0 <= 256`, put
`c = n/N_0` and

```text
Lambda(N_0) = ceil( C(N_0 - 1, N_0/2 + 1) / N_0 ).       (LAD1)
```

Then for every admissible field, whenever the prize budget satisfies
`B* < Lambda(N_0)`, the ordinary worst-list size obeys

```text
L_1( k + 2n/N_0 - 1 )  >  B*.                             (LAD2)
```

The exact field-independent counts are

```text
N_0 =   8:  Lambda = 3
N_0 =  16:  Lambda = 313
N_0 =  32:  Lambda = 8,286,954
N_0 =  64:  Lambda = 13,449,656,337,410,111
N_0 = 128:  Lambda = 90,680,420,711,626,756,043,662,381,605,286,945
N_0 = 256:  Lambda > 2^242 > 2^128  (the banked cap-uniform tier)
```

Since `Lambda` is strictly increasing in `N_0` and the agreement
`k + 2n/N_0 - 1` is strictly decreasing, the best usable tier for a given
budget is the smallest `N_0` with `B* < Lambda(N_0)`, giving the unsafe
staircase

```text
1 <= B* <= 2                       :  L_1(3n/4 - 1)  > B*,
3 <= B* <= 312                     :  L_1(5n/8 - 1)  > B*,
313 <= B* <= 8,286,953             :  L_1(9n/16 - 1) > B*,
8,286,954 <= B* <= Lambda(64)-1    :  L_1(17n/32 - 1) > B*,
Lambda(64) <= B* <= Lambda(128)-1  :  L_1(33n/64 - 1) > B*,
Lambda(128) <= B* < 2^128          :  L_1(k + 2^34 - 1) > B*.
```

Every tier strictly raises the certified unsafe frontier `U(q)` above the
previously recorded cap-uniform value `k + 2^34 - 1` on its budget
interval; on `1 <= B* <= 312` the lower frontier reaches `5n/8 - 1` or
`3n/4 - 1`.

This theorem does not prove any safe-side bound, does not locate the
crossing, does not use the field size beyond the integer comparison
`B* < Lambda(N_0)`, and does not prove either Prize result. The `d >= 2`
fieldwise optimization of the same banked theorem is a separate
(PROVABLE) strengthening, not claimed here.

## Falsifier

A dyadic `N_0` in range whose instantiation parameters violate the parent
theorem's hypotheses (`c | n/2`, `0 < s < c`, `1 <= d <= N_0/2 - 1`); an
error in any printed `Lambda(N_0)`; or an admissible row and budget
`B* < Lambda(N_0)` with `L_1(k + 2n/N_0 - 1) <= B*`.
