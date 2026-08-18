## Rank-eleven shifted-inversion intersection probe

- **status:** `COMPLETE`, heuristic evidence only
- **canonical Modal app:** `ap-CiORfCwgZcjfdftPZfgEg2`
- **question:** attempt to falsify the necessary quadratic-survivor condition
  `I(tau,kappa)>=8740` outside the antipodal and constant-product classes
- **coverage:** 96 shift cosets, 64 parameters each, 6144 total; half random
  and half conditioned to contain a planted domain pair
- **resource envelope:** 96 one-CPU containers, 768 MiB, 60-second hard
  timeout; observed maximum RSS 300048 KiB; no failed shard
- **result:** maximum nonfixed intersection 2336; q50/q90/q99
  `2066/2150/2218`; no falsification; threshold gap 6404
- **artifacts:** compact summary JSON, 6144-line JSONL row ledger, pinned C++
  source and dispatcher, preregistration, and outcome-neutral checker

The run gives positive evidence for a uniform shifted-inversion bound but
cannot prove one. A larger blind sample has low present value: the gap is
already wide, while a proof must find and exclude structured exceptional
parameters. Future compute should target an algebraically defined candidate
family or an exact complete reduction, not merely increase random volume.
