# Shifted-inversion falsification record

The preregistered Modal probe completed all `96` shift shards and all `6144`
parameter rows. The canonical replay is app
`ap-CiORfCwgZcjfdftPZfgEg2`.

```text
maximum nonfixed graph points = 2336
threshold                     = 8740
gap                           = 6404
q50 / q90 / q99               = 2066 / 2150 / 2218
maximizer                     = tau index 13, tau=1594323,
                                kappa=1810701059, planted pair
```

Every shard recounted its maximizing parameter with exponent membership in
place of the production bitset lookup. No shard failed or timed out. The
candidate cap survived this attack with a wide empirical margin.

This is not a proof. Only 96 of 1016 shift cosets and 64 parameters per shift
were sampled. Structured exceptional parameters can be invisible to this
design, and the global quotient limit at `tau=0` is deliberately outside the
tested shifted class. The experiment supports pursuing a uniform
shifted-inversion bound; it does not authorize one in the DAG.
