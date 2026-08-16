# Proof

At `K'=78`, `q=68`, `m=67550`, and `n=1048654`. The conservative stream has
10,837,645 leaves and 11,552 above-ceiling tuples, with canonical digest

```text
bce3cdddfa5da0272f099e17bcb671876f9092e103b51ffa04b9aa7919d49cd7.
```

The largest safe conservative leaf is

```text
s2=50/s3=38/s4=36/s5=37/c6d2/c7d1/c8d1/c9d0/carrier32_plain,
```

with premium `(P78)` and margin `(M78)`. The exhaustive pairwise atlas
reroutes every exceptional tuple in 10,115,441 exact evaluations. Their
maximum is `36102481454819719165765129089266727844130971230`, below the
ceiling by `5142147164896874728877642736062155222476971859`.

The seven geometry lanes contain 150,693,396 evaluations. Their maximum is
the one-step value `38552393090078383126619984181387841064702317594`, below
`(P78)`. Every lane used the bounded-long runner and stayed below 62 MB peak
RSS. Exact component arithmetic gives `(G78)`. QED.
