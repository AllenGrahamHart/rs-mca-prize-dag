# Source evidence

## Primitive degree-12 catalogue

- GAP PrimGrp commit:
  `5612e113d50ac23a7d10945383936e20440b4e14`
- File: `data/gps1.g`, entry `PRIMGRP[12]`
- Raw source:
  `https://raw.githubusercontent.com/gap-packages/primgrp/5612e113d50ac23a7d10945383936e20440b4e14/data/gps1.g`
- Extracted entry SHA-256:
  `9165e7e00ecebd79aaa1272ac83747529839a86191c859b56d49c01d88d12166`

The entry gives exactly `M11`, `M12`, `PSL(2,11)`, `PGL(2,11)`, `A12`, and
`S12`, each with nontrivial subdegree `11`.

## Subdirect products

Leonard L. Scott, "Representations in characteristic p", Proceedings of
Symposia in Pure Mathematics 37 (1980), 319-331, lemma on page 328,
DOI `10.1090/pspum/037/604599`. The proof is the full-diagonal-strip
decomposition used here.

## Exceptional M12 cross-action

- `https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/M11/` records `Out=1` and
  one index-12 maximal subgroup `PSL(2,11)`.
- `https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/M12/` records `Out=2`, two
  index-12 maximal subgroups `M11`, and the two degree-12 representations.
- `https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/M12G1-p12aB0`
- `https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/M12G1-p12bB0`
- GAP generator files `M12G1-p12aB0.g1/.g2` and
  `M12G1-p12bB0.g1/.g2`
- Concatenated four-file SHA-256:
  `55af41251add2886aedb2ebf04dfb522776768a245dd9e6cd8369094cf84aa38`

Both pages identify their permutations as standard generators. The exact
paired-generator replay in `verify_audit.py` reconstructs order `95040`, an
order-`7920` point stabilizer, same-action orbits `1,11`, and cross-action
orbit `12`.

For the remaining socles, the GAP rows themselves exhibit the full outer
extensions `PSL(2,11) < PGL(2,11)` and `A12 < S12` in the same natural
degree-12 action. Thus those outer automorphisms preserve the action class.

Accessed 2026-07-29. No web claim is used in place of the checked finite
permutation calculation.

## Upstream export

This theorem and its secondary degree-five consumer are exported together in
draft upstream PR `#1132`:

- PR: `https://github.com/przchojecki/rs-mca/pull/1132`
- head commit: `c23eb801af8853d0369a72ea8834c84e7a3242f6`
- theorem-note blob: `cd29c893dceb63283c7a731c9a3c4280fa665c5c`
- certificate blob: `9e1bd3d89dac6409f148dc134fda46d3bf644c11`
- verifier blob: `989e6780f29c22acaa5d231ef9f1e54b47255138`
- certificate payload SHA-256:
  `456b51c78e837c8a27ffda0b43409c63c88128b254be320723728868db096e6f`

The upstream verifier reconstructs the paired `M12` group of order `95040`
and rejects `22/22` semantic mutations. The PR is mergeable; its only
reported status failure at this head is unrelated Vercel authorization.
