# Source evidence

## Primitive degree-six catalogue

- GAP PrimGrp commit:
  `5612e113d50ac23a7d10945383936e20440b4e14`
- File: `data/gps1.g`, entry `PRIMGRP[6]` including its trailing newline
- Exact extracted size: 321 bytes
- SHA-256:
  `00bc5cdf6d0d833236953b9462c7c595a28960407ab2ee89e1b44ae11c16f5b7`
- Raw source:
  https://raw.githubusercontent.com/gap-packages/primgrp/5612e113d50ac23a7d10945383936e20440b4e14/data/gps1.g

The entry gives exactly `PSL(2,5),PGL(2,5),A6,S6`, their orders, and the
single nontrivial subdegree five.

## Transitive degree-ten catalogue

- GAP TransGrp commit:
  `165fc21ff497b24b7a5975582b331e6692ba04f1`
- File: `data/trans10.grp`
- Exact file size: 7059 bytes
- SHA-256:
  `e7d8189cac31fa4f5a0f830234080fbddf0d741ca27921ffc7946c24b22f51d0`
- Raw source:
  https://raw.githubusercontent.com/hulpke/transgrp/165fc21ff497b24b7a5975582b331e6692ba04f1/data/trans10.grp

The order field leaves exactly catalogue entries 40--45 after imposing
divisibility by 600. Entries 40--43 are the four printed wreath forms;
entries 44--45 are the natural `A10,S10` actions.

## Subdirect products

Leonard L. Scott, "Representations in characteristic p", Proceedings of
Symposia in Pure Mathematics 37 (1980), 319--331, lemma on page 328,
DOI `10.1090/pspum/037/604599`.

The primary verifier replays the catalogue arithmetic and route logic.
The independent verifier reconstructs entries 40--43 as explicit
permutation groups of orders 7200, 14400, 14400, and 28800, then checks
the endpoint, degree-six, and intermediate degree-five subgroup indices.

Accessed 2026-07-29. No network access is required by either verifier.
