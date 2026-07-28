# Proof

The parent leaves only `10<=V<=106`, `V=2 mod 8`, for cofactor `m=16`.
Local reciprocity gives singleton separation `4q` with `q` odd. Translation,
an odd Galois multiplier inverse to `q` modulo 32, folding, and global sign
reduce every candidate to

```text
F(X)=1+epsilon X^4+2 sum_(j=1)^4 epsilon_j X^(a_j),
epsilon,epsilon_j in {+1,-1},
{a_1,...,a_4} subset {0,...,127}\{0,4}.
```

The exact normalized search size is

```text
binom(126,4)*2^5=320292000.                            (1)
```

The primary engine folds the fifteen unordered coefficient pairs into the
positive-half negacyclic autocorrelation. The audit engine uses a full
128-slot ordered-pair convolution, lexicographic combination order, and a
different shard partition. Both complete 32/32 shards and agree on every
variance and `(E,L)` count. In particular `V=10` is empty and the other
twelve residual chambers contain exactly 540332 normalized vectors.

Each exact-norm engine regenerates its candidates inside the remote worker;
no witness packet is shared between them. The FLINT stream uses the primary
folded-pair enumerator and balanced shards. The PARI stream uses the audit
ordered-pair enumerator and lexicographic modulo shards. For every candidate
both compute

```text
R=|Res_X(X^128+1,F(X))|
```

and check `v_2(R)=4` before forming `R/16`.

For an order-independent exact audit, each engine serializes the canonical

```text
(positions,coefficients,energy,R,R/16)
```

row, hashes it with SHA-256, and assigns it to one of 64 deterministic
buckets. Each bucket records its row count, digest xor, digest sum, and digest
square-sum modulo `2^256`. The independently aggregated 64-bucket
fingerprints agree in every field, as do all variance/region counts.

The exact prize interval is

```text
[B_P 2^128,(B_P+1)2^128-1],
B_P=317494674775468773183020924238786383963.
```

The joint exact region ledger is

| `V` | below | inside | above |
|---:|---:|---:|---:|
| 10 | 0 | 0 | 0 |
| 18 | 0 | 0 | 16 |
| 26 | 0 | 0 | 16 |
| 34 | 20 | 0 | 144 |
| 42 | 132 | 0 | 76 |
| 50 | 588 | 0 | 56 |
| 58 | 1204 | 0 | 0 |
| 66 | 15628 | 0 | 0 |
| 74 | 3616 | 0 | 0 |
| 82 | 29868 | 0 | 0 |
| 90 | 35120 | 0 | 0 |
| 98 | 415944 | 0 | 0 |
| 106 | 37904 | 0 | 0 |

The maximum below and minimum above printed in `statement.md` give a strict
gap around the whole interval. Therefore no residual resultant equals `16p`
for a prize-row prime `p`, proving the claim.
