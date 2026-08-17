## Preregistered cell-3 cached common-input compilation

- **decision:** remove duplicated symbolic compilation from the O0b
  cells-3/6 outside workers and pin one reusable packet per source-sign row
- **scope:** exactly four source-sign rows; no outside labels and no Singular
  solve
- **launcher SHA-256:**
  `d9cb5dd8f5c66c69f9c5ed79f7d1b2b965ce306feddd0db865146d82c2bfbeba`
- **checker SHA-256:**
  `99e6f05bd9e97ffa091b3f9e347765cbb0b864ff61f56a567206a4aed6e36ae3`
- **product-rank certificate SHA-256:**
  `ee4dcb25877e9101a544ee5896b9bf6890059d6398c78d7562127b0d1c53c293`
- **compact-structure certificate SHA-256:**
  `2f8712f2a942bb46f153d5204c4f4c8f9bff08336c295db4f31aef10fb5d22b7`
- **compact-kernel certificate SHA-256:**
  `e20ccb714b252f00ee3ce877ee68eff032f43deb877e2097919151436ddcf789`
- **envelope:** four one-CPU workers, 3 GiB each, 180-second container
  wall; projected cost below `$0.10`
- **local safety:** one RAM-guarded Modal client under a 240-second external
  hard stop; no local symbolic algebra

Each row must reproduce the three compact-equation hashes already recorded
in the six-chart structure certificate and the eight kernel-entry hashes in
the global kernel certificate. The output packet stores Singular-ready text
for three equations, eight kernel entries, sixteen route guards, and six
rank cofactors. The checker requires all four ordered sign rows, exact source
custody, exact packet shape, and four distinct packet hashes.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 240s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_cached_common_input_modal.py
```

A complete checked result certifies only reusable representation of already
proved common algebra. It authorizes construction and preregistration of the
repaired 24-representative outside pilot; it excludes no outside system.
