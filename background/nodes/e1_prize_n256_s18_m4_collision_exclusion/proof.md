# Proof

The parent theorem leaves exactly the nine variance chambers

```text
V=10,18,26,34,42,50,58,66,74.
```

For cofactor `m=4`, local reciprocity fixes the singleton separation at two.
Translate and apply the established sign normalization so their positions are
`0,2`; choose the four doubleton positions from the other 126 slots and their
32 normalized sign patterns. The complete normalized universe has

```text
32 binom(126,4)=320292000
```

vectors.

The primary residual stream uses a folded-pair autocorrelation engine with
balanced shards. The audit uses lexicographic modulo shards and a direct full
128-slot convolution. Restricting to the parent chambers gives

| `V` | 10 | 18 | 26 | 34 | 42 | 50 | 58 | 66 | 74 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vectors | 0 | 16 | 16 | 100 | 144 | 420 | 820 | 17084 | 2776 |

The total is `21376`.

For each streamed vector, the primary worker computes

```text
R=|Res(F,Phi_256)|
```

in exact FLINT arithmetic, verifies `4|R`, and compares `R/4` with the exact
integer prize interval

```text
[108037839417390090843359763492907651257884484313348964300411102808750191280128,
 108037839417390090843359763492907651258224766680269902763874477416181959491583].
```

The audit independently regenerates the residual in a different order and
computes the resultants in PARI. Both engines aggregate the candidate
multiset into the same 64 buckets, retaining in each bucket the exact count,
XOR, sum, and sum of squares of a SHA-256 commitment. Every field in every
bucket agrees. Their common region ledger is

| `V` | below | inside | above |
|---:|---:|---:|---:|
| 10 | 0 | 0 | 0 |
| 18 | 0 | 0 | 16 |
| 26 | 0 | 0 | 16 |
| 34 | 0 | 0 | 100 |
| 42 | 44 | 0 | 100 |
| 50 | 208 | 0 | 212 |
| 58 | 648 | 0 | 172 |
| 66 | 16936 | 0 | 148 |
| 74 | 2768 | 0 | 8 |

The exact extrema around the interval are

```text
maximum below =
107716387476569755844902778849041509815310757677547440774146432592221447900929,

minimum above =
110553665570163478885905819698234426068541015284212878175575978480389082393089.
```

Thus no residual vector has `R/4` in the prize interval. Combined with the
parent exclusion of every higher admissible variance, cofactor `m=4` is
impossible.
