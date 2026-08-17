# Proof

At `K'=77`, `q=67`, `m=67549`, and `n=1048653`. The conservative stream has
10,475,101 leaves and 7,657 above-ceiling tuples. Their canonical digest is

```text
f2bac3ee68fdc243f1a7ed7101dcaa72ba7ecd4c278ce4cb4d7b0a4466e774a9.
```

The largest safe conservative leaf is

```text
s2=42/s3=37/s4=34/s5=35/c6d3/c7d2/c8d1/c9d0/carrier32_plain,
```

with premium `(P77)` and margin `(M77)`. The exhaustive pairwise atlas
reroutes all 7,657 exceptional tuples in 6,623,568 exact evaluations. Their
maximum is `35026060643237953572770728698158639005273906176`, below the
ceiling by `6194522850075411977316893801271216001945342098`.

The seven geometry lanes contain 143,928,183 evaluations. Their maximum is
the one-step value `37927152249618150254202496789638286615058058210`,
strictly below `(P77)`. The five-step lane required the bounded 10-minute
runner after the default 270-second runner timed out; it completed at 60 MB
peak RSS and was safe. Exact component arithmetic gives `(G77)`. QED.
