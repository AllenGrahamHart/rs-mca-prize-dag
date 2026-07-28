# Proof

For `m=256`, the parent theorem gives `v_2(m)=8` and

```text
V in {10,18,26,34,42,50,58,66,74}.
```

The singleton-separation formula makes the separation `8q` with `q` odd.
Translation, an odd Galois multiplier inverse to `q` modulo 16, folding, and a
global sign reduce every candidate to

```text
F(X)=1+epsilon X^8+2 sum_(j=1)^4 epsilon_j X^(a_j),
epsilon,epsilon_j in {+1,-1},
{a_1,...,a_4} subset {0,...,127}\{0,8}.
```

The exact normalized search size is again

```text
binom(126,4)*2^5=320292000.                           (1)
```

The primary engine folds 15 unordered coefficient pairs into positive-half
negacyclic autocorrelations. The audit engine uses a full 128-slot ordered-pair
convolution, a different combination order, and a different shard partition.
Both complete 32/32 shards and agree on every count in `statement.md`.

For each of the 20756 residual vectors, the FLINT engine computes

```text
R=|Res_X(X^128+1,F(X))|.
```

Local reciprocity gives `v_2(R)=8`, which the engine checks before forming
`R/256`. The exact prize interval is

```text
[B_P 2^128,(B_P+1)2^128-1],
B_P=317494674775468773183020924238786383963.
```

All 28 variance-18 quotients lie above the upper endpoint. Every quotient at
variance at least 26 lies below the lower endpoint; variance 10 is empty.
The extremal values printed in `statement.md` certify a strict gap around the
entire interval.

The norm ledger is split into 32 deterministic index shards. Each shard stores
a SHA-256 commitment to its ordered exact `(vector,norm,quotient)` rows. An
independent PARI engine recomputes all 20756 resultants and matches every shard
commitment and interval count. Hence no residual vector has `R=256p` for a
prize-row prime `p`.
