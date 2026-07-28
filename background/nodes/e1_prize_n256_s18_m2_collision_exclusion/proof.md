# Proof

The parent theorem leaves exactly

```text
V=10,18,26,34,42,50,58,66,74,82,90,98.
```

Since `v_2(m)=1`, the singleton separation is odd. Translation and an odd
cyclotomic Galois automorphism normalize the singleton positions to `0,1`,
and a global sign fixes the first coefficient. Choosing the four doubleton
positions and 32 sign patterns gives

```text
32 binom(126,4)=320292000
```

normalized vectors.

The primary residual stream uses folded-pair autocorrelation and balanced
shards. The audit uses lexicographic modulo shards and a direct full 128-slot
convolution. Their residual counts are

| `V` | 10 | 18 | 26 | 34 | 42 | 50 | 58 | 66 | 74 | 82 | 90 | 98 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vectors | 0 | 16 | 8 | 88 | 88 | 232 | 460 | 15292 | 2160 | 16188 | 30552 | 446188 |

The total is `511272`.

For each vector, the primary computes

```text
R=|Res(F,Phi_256)|
```

in exact FLINT arithmetic, verifies `2|R`, and compares `R/2` with the exact
integer prize interval

```text
[108037839417390090843359763492907651257884484313348964300411102808750191280128,
 108037839417390090843359763492907651258224766680269902763874477416181959491583].
```

The audit independently regenerates the residual and computes all resultants
with PARI. Both implementations are prepared to certify the primality status
of an in-interval quotient, including candidates with extra 2-adic valuation;
in fact no quotient is in the interval. They aggregate the exact row multiset
into 64 buckets retaining count, XOR, sum, and sum of squares of SHA-256 row
commitments. Every field in every bucket agrees. Their common region ledger is

| `V` | below | inside | above |
|---:|---:|---:|---:|
| 10 | 0 | 0 | 0 |
| 18 | 0 | 0 | 16 |
| 26 | 0 | 0 | 8 |
| 34 | 0 | 0 | 88 |
| 42 | 20 | 0 | 68 |
| 50 | 56 | 0 | 176 |
| 58 | 316 | 0 | 144 |
| 66 | 14924 | 0 | 368 |
| 74 | 2152 | 0 | 8 |
| 82 | 16188 | 0 | 0 |
| 90 | 30552 | 0 | 0 |
| 98 | 446188 | 0 | 0 |

The exact extrema around the interval are

```text
maximum below =
107768200285002421852540903242682983183211082719077647662104106067449092858113,

minimum above =
108175736216610979727225685018558899952758788007302660274771396038641324156161.
```

Thus no residual vector has `R/2` in the prize interval. Combined with the
parent exclusion of all higher admissible variances, cofactor `m=2` is
impossible.
