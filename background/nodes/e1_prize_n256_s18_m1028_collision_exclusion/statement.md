# E1 prize N=256 square-mass-18 cofactor-1028 exclusion

- **status:** PROVED
- **closure:** exhaustive normalized census plus exact finite-field replay
- **scope:** prize-envelope `N=256`, profile `(a,b,c)=(4,2,0)`
- **dependency:** `e1_prize_n256_s18_variance_cofactor_windows`

No pair-feasible prize-envelope collision in folded profile `(4,2,0)` has
norm cofactor

```text
m=1028=4*257.
```

Indeed, the variance/cofactor theorem restricts this class to

```text
V in {10,18}.
```

After translation, odd Galois scaling, and global sign normalization, every
candidate has singleton terms at positions `0,2`, first singleton coefficient
`+1`, arbitrary second singleton sign, and four signed magnitude-two terms in
the other 126 positions. Two independent complete engines give

| quantity | exact count |
|---|---:|
| four-position choices | 10009125 |
| signed normalized vectors | 320292000 |
| `V=10` vectors | 0 |
| `V=18` vectors | 16 |
| `V in {10,18}` vectors with norm divisible by 257 | 0 |

Since `257` splits completely in `Q(zeta_256)` and divides `m`, a cofactor-1028
collision norm would be divisible by 257. The exact census rules this out.

This removes one cofactor class. It does not count the vectors in the other
five classes and does not prove the aggregate E1 collision-pair budget.
