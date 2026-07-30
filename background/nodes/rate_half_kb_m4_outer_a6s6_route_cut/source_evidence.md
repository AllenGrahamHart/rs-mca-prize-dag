# Source evidence

## Primitive degree-15 catalogue

- GAP PrimGrp commit:
  `5612e113d50ac23a7d10945383936e20440b4e14`
- File: `data/gps1.g`, entry `PRIMGRP[15]` including trailing newline
- Exact extracted size: 894 bytes
- SHA-256:
  `d24658310cb386c9663e95ab9024eab9142d79f849131f499da36eeda82c003e`
- Raw source:
  https://raw.githubusercontent.com/gap-packages/primgrp/5612e113d50ac23a7d10945383936e20440b4e14/data/gps1.g

The entry gives exactly six groups. Four have nontrivial subdegree 14; the
degree-15 `A6,S6` actions have subdegrees 6 and 8.

The primary verifier checks the catalogue and route arithmetic. The
independent verifier reconstructs the `A6,S6` actions on all 15 two-subsets
and the pole-cycle type `5^3`.

Accessed 2026-07-29. The source hash pins the classification input; finite
action claims are replayed locally.

## Upstream custody

The theorem packet is exported in
[`przchojecki/rs-mca` PR #1132](https://github.com/przchojecki/rs-mca/pull/1132)
at exact head
`d7232a30a5cca4a42330422415da71f06a7c5a31`:

- note blob: `13fd38f97fb7087df88fe7c212020933b409d191`
- certificate blob: `bb130d089d1ca7c0fcab04b65f66de773952ceb2`
- verifier blob: `06854e72fe35720052505c543d86bcf587f61017`
- certificate payload SHA-256:
  `61a8db82285f22393fc2af6c1d35224d79587fa150009270d42ac33972557485`

The upstream verifier reconstructs the two degree-15 two-subset actions,
checks every imported historical object by Git blob and canonical payload,
and rejects 18 of 18 semantic mutations.
