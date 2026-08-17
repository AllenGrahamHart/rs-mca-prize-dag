# Proof

At `K'=81`, `q=71`, `m=67553`, and `n=1048657`. The conservative stream has
12,695,949 leaves and 39,570 above-ceiling tuples, with canonical digest

```text
5e8c37955cd9842170149c8021e77d6072be9a769df01e8d82bd11d4caaa5c20.
```

The largest safe conservative leaf is

```text
s2=55/s3=41/s4=44/s5=35/c6d3/c7d2/c8d1/c9d0/carrier32_plain,
```

with premium `P_81` and positive margin. The exhaustive pairwise atlas
reroutes every exceptional tuple in 40,569,326 exact evaluations. Their
maximum is `38588134569160005322410296957739069270917018036`, below the ceiling by
`2728613435299985889292059999502528621810771313`.

The seven geometry lanes contain 172,265,121 evaluations. Their maximum is
the one-step value `40287409045971746658167168137122038667039311900`, below
`P_81`. Every lane used the bounded-long runner and stayed below 64 MB peak
RSS. Exact component arithmetic gives the stated positive payment gap. QED.
