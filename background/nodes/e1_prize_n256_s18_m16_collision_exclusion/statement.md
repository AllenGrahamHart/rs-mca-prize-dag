# E1 prize N=256 square-mass-18 cofactor-16 exclusion

- **status:** PROVED
- **closure:** dual complete census plus dual exact-resultant certificate
- **scope:** prize-envelope `N=256`, profile `(a,b,c)=(4,2,0)`, cofactor `m=16`
- **dependencies:** `e1_prize_n256_s18_m16_high_variance_exclusion`

No prize-row collision with cofactor `m=16` exists.

The parent restricts the residual variance to

```text
V in {10,18,26,34,42,50,58,66,74,82,90,98,106}.
```

After normalizing the singleton positions to `0,4`, two independent complete
engines exhaust all `320292000` signed vectors and agree on the residual
counts

| `V` | 10 | 18 | 26 | 34 | 42 | 50 | 58 | 66 | 74 | 82 | 90 | 98 | 106 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 0 | 16 | 16 | 164 | 208 | 644 | 1204 | 15628 | 3616 | 29868 | 35120 | 415944 | 37904 |

For all `540332` residual vectors, independent FLINT and PARI streams compute
the exact resultant `R=|Res(X^128+1,F)|`, check `v_2(R)=4`, and agree through
a 64-bucket multiset fingerprint. Every quotient `R/16` is outside the exact
prize interval: 308 are above and 540024 are below. The closest values are

```text
maximum below =
104797259883500113680505745049174573490076600644557179823872590464045041710081,

minimum above =
109148549668884138628080445927205579649397021264609510361461809939220006348801.
```

Hence no residual vector has `R=16p` for a prize-row prime `p`.
