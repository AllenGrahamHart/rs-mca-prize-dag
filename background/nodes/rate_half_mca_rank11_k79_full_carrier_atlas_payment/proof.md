# Proof

At `K'=79`, `q=69`, `m=67551`, and `n=1048655`. The conservative stream has
11,546,087 leaves and 19,406 above-ceiling tuples, with canonical digest

```text
10faebceb497f80e1a7ec6240c304ced8f7999bd15d185eb87d926df0fb6c76a.
```

The largest safe conservative leaf is

```text
s2=59/s3=43/U23/s4=41/s5=36/c6F/c7F/c8F/c9F/ordinary,
```

with premium `(P79)` and margin `(M79)`. The exhaustive pairwise atlas
reroutes every exceptional tuple in 19,114,557 exact evaluations. Their
maximum is `36806673610575733210712437632598364987616830139`, below the
ceiling by `4461997470760948156821111474256342583542475332`.

The seven geometry lanes contain 157,671,136 evaluations. Their maximum is
the one-step value `39155883271390100828809596211624350117737071281`, below
`(P79)`. Every lane used the bounded-long runner and stayed below 64 MB peak
RSS. Exact component arithmetic gives `(G79)`. QED.
