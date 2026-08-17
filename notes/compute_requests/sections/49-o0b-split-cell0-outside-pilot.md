## Preregistered O0b split cell-0 component outside pilot

- **decision:** test the changed O0b outside ideal on a complete stratum
  subcover before authorizing the 708-representative campaign
- **scope:** 24 canonical representatives covering all 56
  `component/lane-orbit/outside-sign/missing-record` strata
- **launcher SHA-256:**
  `04ae51440703ad0116e33ce6a4c7f3312eff748cd8c3fa1a1d326c4d465f5d48`
- **checker SHA-256:**
  `74770cfadbfa1275fe58fbee187b40e00cea8e8526ff3dc07347a8011c8046b5`
- **outside-core SHA-256:**
  `5cd86020b601b68e9a4295d55d057ec0e029dede334397e6bc51f9d840e5561f`
- **representative manifest SHA-256:**
  `658ae5f1f3c0667df2cece818e0c89a752ce9cdf7c4f6f421fc4a721134b8fa4`
- **pilot representative-list SHA-256:**
  `47ef7c3a9a92ac2bcb08462377195c0576c2495b0ff1f7c0948103d10e02bc27`
- **component certificate SHA-256:**
  `2fd2d65ebd033d8cd784f428d31d9b49eb66c4b6a059326ed7efcd60d53ed100`
- **envelope:** at most 24 one-CPU workers, 2 GiB each, 180-second
  Singular child wall and 210-second container wall; conservative campaign
  wall below five minutes and projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client under a 300-second external
  hard stop; exact CAS work is remote and each returned row is checkpointed

The PROVED component router reduces the complete equal-sign ledger from
2,520 component cases to 708 representatives. Its pilot subcover contains
one orbit representative whose orbit meets each of the 56 coarse strata.
Each worker imposes the exact component relation, missing-product equation,
three paired-product resultants, missing squared-sum equation, and all source,
denominator, leading-support, and target-distinctness guards. The pure outside
core fixes the O0b record order `BE,CF,DE+,DE-,DF+,DF-,EF` and the two
repeated-lane variants.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 300s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_modal.py \
  --scope pilot
```

`PILOT_ALL_UNIT` requires 24/24 `COMPLETE` rows, unit saturated ideals, exact
case hashes, and checker acceptance; it authorizes preregistration of the full
708-case campaign but has no theorem or DAG-status effect. Any complete
nonunit row is retained with its six generators and complete guard list for
route analysis. `TIMEOUT`, `ERROR`, `REMOTE_ERROR`, client interruption, or
an incomplete checkpoint is `INCOMPLETE` and authorizes only a bounded repair
or resumption. No pilot outcome closes cell `0`.

The first deployment smoke, Modal app `ap-6GEKxb3H9szvhPpQ0AyIIo`, is
`INCOMPLETE`: all 24 rows returned `REMOTE_ERROR` before CAS startup because
the validated pure outside core was not mounted into the remote image. The
checkpoint SHA-256 is
`a68188167e669240aff40d5df0cfc389eee8c2459d8438922ba6163b48f97c61`.
No row reached Singular and the run has no mathematical status. Launcher
`04ae5144...` adds the missing immutable core mount; all case, solver, wall,
and outcome contracts are unchanged for the bounded rerun.
