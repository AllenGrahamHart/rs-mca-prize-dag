# RF3-double-prime KoalaBear safe rows

- **status:** PROVED
- **consumers:** `mca_safe`, `compiler` (evidence only)
- **source:** `przchojecki/rs-mca@999b8f3a`

Let

```text
p = 2^31 - 2^24 + 1,
F = F_(p^6),
q = |F|,
n = 2^21,
```

and let `D <= F_p^*` be the subgroup of order `n`. For
`C_rho=RS[F,D,rho*n]`, with full-field challenge set `F`, the following
agreements have unconditional support-wise MCA upper numerators:

| rate | agreement `A` | radius `r=n-A` | upper numerator `R''` |
|---:|---:|---:|---:|
| `1/2` | 1,485,170 | 611,982 | 274,589,064,742,753,629 |
| `1/4` | 1,051,719 | 1,045,433 | 274,721,012,201,293,956 |
| `1/8` | 744,762 | 1,352,390 | 274,578,888,391,562,205 |
| `1/16` | 527,408 | 1,569,744 | 274,861,787,390,263,486 |

In every row,

```text
B_C^MCA(A) <= R'' <= floor(q/2^128)
                     = 274,980,728,111,395,087.
```

Hence closed radius `r` is safe at target `2^-128` in each row.

The factor-lifting input is the proved conservative RF3-double-prime theorem:
with the notation in `claim_contract.md`, more than

```text
(1 + 2 U D_Y^2) D_Z + (r+1) D_Y
```

retained slopes force one chosen agreement support on which both received
coordinates are Reed-Solomon codewords. This replaces the false weaker RF3
content ledger in the immutable Paving v9.2 release.

No adjacent unsafe agreement is proved here. In particular, this theorem does
not determine the largest safe radius of any of the four rows.
