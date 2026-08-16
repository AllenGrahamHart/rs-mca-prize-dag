# Proof

At `K'=82`, `q=72`, `m=67554`, and `n=1048658`. The conservative stream has
13,101,284 leaves and 49,900 above-ceiling tuples, with canonical digest

```text
d8e7a8286cffeeb8af99e9ea283d9ff2c0cc6c86730c84062ec01ec85c6fa0c5.
```

The largest safe conservative leaf is

```text
s2=46/s3=38/U23/s4=48/s5=36/c6d3/c7d2/c8d1/c9d0/ordinary,
```

with premium `P_82` and positive margin. The exhaustive pairwise atlas
reroutes every exceptional tuple in 48,822,291 exact evaluations. Their
maximum is `39665321226453960140094333058326997487100975540`, below the ceiling by
`1675461236624987848848470187656243730027167276`.

The seven geometry lanes contain 179,887,680 evaluations. Their maximum is
the one-step value `40891353398864895345494242236029970259845626460`, below
`P_82`. Every lane used the bounded-long runner and stayed below 64 MB peak
RSS. Exact component arithmetic gives the stated positive payment gap. QED.
