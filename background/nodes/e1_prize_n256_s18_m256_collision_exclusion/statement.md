# E1 prize N=256 square-mass-18 cofactor-256 exclusion

- **status:** PROVED
- **closure:** dual exhaustive census plus committed dual exact resultants
- **scope:** prize-envelope `N=256`, profile `(a,b,c)=(4,2,0)`
- **dependency:** `e1_prize_n256_s18_variance_cofactor_windows`

No pair-feasible prize-envelope collision in folded profile `(4,2,0)` has
norm cofactor `m=256`.

The variance/cofactor theorem restricts this class to nine variances. After
normalizing singleton positions to `0,8`, two independent complete engines
exhaust all `320292000` signed vectors and agree on:

| `V` | vectors | quotient `Norm/256` position |
|---:|---:|---|
| 10 | 0 | empty |
| 18 | 28 | all above prize interval |
| 26 | 52 | all below prize interval |
| 34 | 204 | all below prize interval |
| 42 | 212 | all below prize interval |
| 50 | 864 | all below prize interval |
| 58 | 956 | all below prize interval |
| 66 | 15364 | all below prize interval |
| 74 | 3076 | all below prize interval |

FLINT computes exact whole norms for all 20756 residual vectors. PARI
independently reproduces all 32 shard commitments. No quotient lies in the
prize interval. The exact gap is witnessed by

```text
maximum below =
79966870433624456578392518772995331447805526474703846245310288507286369992961,

minimum above =
127117908459354031873489386413391045324297956117263458825602208201263580806401.
```

This removes cofactor `256` and leaves the three prize cofactors `{2,4,16}` in
the leading profile. Their residual vectors remain open.
