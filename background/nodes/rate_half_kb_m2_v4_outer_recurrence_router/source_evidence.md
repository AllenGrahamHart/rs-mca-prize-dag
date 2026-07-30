# Source evidence

## Primitive degree-30 catalogue

- GAP PrimGrp commit:
  `5612e113d50ac23a7d10945383936e20440b4e14`
- File: `data/gps1.g`, entry `PRIMGRP[30]` including trailing newline
- Exact extracted size: 344 bytes
- SHA-256:
  `1a923cc8f4428ec22864109cdc60d0c87326e8939cc1d72d217d22df2a4b8da0`
- Raw source:
  https://raw.githubusercontent.com/gap-packages/primgrp/5612e113d50ac23a7d10945383936e20440b4e14/data/gps1.g

The entry gives exactly four primitive groups, each with sole nontrivial
subdegree 29. The independent verifier reconstructs the PSL and PGL
projective-line actions over `F_29`; the alternating and symmetric natural
actions have the same subdegrees.

Accessed 2026-07-29. Catalogue completeness is the pinned classification
input.

## Upstream custody

The import-free export is pinned to PR `#1132` at
`d4063dcd9c56835c3916ef792e263ea720a4d397`:

```text
note blob:        41dc0c3dd72bc9bc2f7d2759ba3c6ac64491cb08
verifier blob:    774a2da946399dc28966e8f300ac9a17e6fed27b
certificate blob: 50d17f218bfa7d3acb211c946db0c025b9a98944
payload SHA-256:  fe8141810501fd7b3762a378210609177185972ec706bf9ac943fa398bd82d39
```

The certificate binds four parent terminals by exact commit, Git blob, and
canonical payload, reconstructs both degree-30 projective actions, and
rejects 21 of 21 hostile mutations.

## Imported local geometry

The source lift uses the proved actual-component facts already vendored in
the dependencies: `H_0` has bidegree `(2,4)`, maps birationally to the
bidegree-`(4,4)` component `Gamma`, its source-deck conjugate is distinct,
the twelve source locators are pairwise disjoint deck-invariant quadratics,
and the source-star defect is at most three.
