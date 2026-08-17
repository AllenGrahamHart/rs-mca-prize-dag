## Preregistered O0b cells-3/6 initial-prefix diagnostic

- **decision:** locate the first hard outside equation in one representative
  whose full initial ideal timed out in the six-case cross pilot
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  independently test the common basis plus the first `1,2,3,4,5` outside
  equations in the compiler's pinned order
- **launcher SHA-256:**
  `19845e2caf2a57e54bb4c72572b0392f5a0ba1cbe10f81b1b80dc4a9b4509dff`
- **outcome-neutral checker SHA-256:**
  `917d3f9479ba981532ca4f339898aa927c9076847036c32a00b01e7b555e63d5`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** at most five one-CPU workers, 4 GiB each, 180-second
  Singular child wall and 230-second container wall; projected cost below
  `$0.25`
- **local safety:** unordered result streaming with immediate checkpoints
  under one RAM-guarded Modal client and a 300-second external hard stop

Every complete worker retains the exact reduced basis and its hash. Comparing
independent prefixes avoids making a long stage chain disappear behind one
timeout. The result is diagnostic only: completion of a prefix proves no
emptiness statement, and a timeout has no mathematical status. The maximal
completed prefix may be reused as a certified computational input for a
single-equation extension. This run does not authorize any multi-case or full
1,416-case campaign.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 300s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_initial_prefix_modal.py
```
