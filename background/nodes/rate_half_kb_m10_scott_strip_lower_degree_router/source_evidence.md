# Source evidence

## Primitive degree-10 catalogue

- GAP PrimGrp commit:
  5612e113d50ac23a7d10945383936e20440b4e14
- File: data/gps1.g, entry PRIMGRP[10]
- Raw source:
  https://raw.githubusercontent.com/gap-packages/primgrp/5612e113d50ac23a7d10945383936e20440b4e14/data/gps1.g
- Exact extracted entry size: 1272 bytes
- Extracted entry SHA-256:
  9cf136ffbea68f3156bc2ff386b5aec7b510a77e13e77ad6a09904b02382a69e

The entry gives exactly the nine groups, orders, and subdegree rows used in
the proof. It also exhibits S5, PGammaL(2,9), and S10 on the same ten-point
actions as the simple socles.

## A6 automorphisms and degree-10 action

The online ATLAS page

  https://brauer.maths.qmul.ac.uk/Atlas/alt/A6/

identifies Aut(A6)=A6.2^2 and supplies its ten-point permutation
representation. The representation page

  https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/A6V4G1-p10B0

records degree 10, primitivity, rank two, and suborbits 1,9. Thus all four
outer-automorphism twists are realized in the same ten-point action.

## Subdirect products

Leonard L. Scott, "Representations in characteristic p", Proceedings of
Symposia in Pure Mathematics 37 (1980), 319-331, lemma on page 328,
DOI 10.1090/pspum/037/604599.

The kernel-free flag actions and their complete subdegrees are reconstructed
directly by verify.py and independently from explicit flag stabilizer
generators by verify_audit.py.

## Upstream review custody

The reviewer-facing packet is pinned in draft PR #1132:

- PR: https://github.com/przchojecki/rs-mca/pull/1132
- Commit: 412bc68f1dcb6ac3924d6445146417f3c713ef89
- Theorem-note blob: 13645fac5d116ec90ebbd5f1254d74b9715f83be
- Certificate blob: 6e49093fdb9d9e55b45c55265eb3cc0c0e65e8c9
- Verifier blob: 9f12c4e749b3ab147b2374943c3d9b56c2c90697
- Certificate payload SHA-256:
  66117d7ba207a66606fc4ae4770a2b314b3510066be7af734b4e579d028ce1d1

The upstream theorem has the same scope as this node: strict routing from
inner degree ten to degrees 2, 3, or 6, with no destination-row deletion,
payment, or K3/KoalaBear closure.

Accessed 2026-07-29. No web claim substitutes for the exact finite
permutation replays.
