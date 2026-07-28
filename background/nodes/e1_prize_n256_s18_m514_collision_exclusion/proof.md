# Proof

The parent theorem gives the six displayed variances and says that
`v_2(m)=1`. Its singleton-separation formula therefore makes the separation
odd. Translation moves the first singleton to zero; multiplication by the
inverse odd separation is a cyclotomic Galois automorphism that moves the
second to one. Folding into the degree-128 basis changes only signs, and a
global sign fixes the first singleton coefficient. Every candidate maps to

```text
F(X)=1+epsilon X+2 sum_(j=1)^4 epsilon_j X^(a_j),
epsilon,epsilon_j in {+1,-1},
{a_1,...,a_4} subset {0,...,127}\{0,1}.
```

The normalized search space has exact size

```text
binom(126,4)*2^5=320292000.                           (1)
```

The primary engine forms the positive-half negacyclic autocorrelation by
folding the 15 unordered coefficient pairs. The audit engine independently
forms the full 128-slot ordered-pair convolution and checks
`A_(128-d)=-A_d` and `A_64=0`. They use different enumeration orders and shard
partitions. Both complete all 32 shards and agree exactly on every count in
`statement.md`.

Since `3` has order 256 modulo 257,

```text
257|Norm(F(zeta)) iff F(3^u)=0 mod 257 for some odd u.
```

Testing all 128 odd exponents leaves the 184 candidates in the final column of
the table. For each, the primary norm engine computes the exact integer
resultant

```text
R=|Res_X(X^128+1,F(X))|
```

with FLINT. An independent PARI engine recomputes all 184 resultants and agrees
entry by entry. There are 46 distinct values. Every `R` is divisible by 514,
but exact integer comparison gives

```text
R/514 <=
66082262884856162162140234757894655654959953149381163882659090799481192796929
< B_P 2^128,

B_P=317494674775468773183020924238786383963.          (2)
```

A prize-row collision with cofactor 514 would have `R=514p` for a row prime
`p>=B_P 2^128`, contradicting (2).
