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

Accessed 2026-07-29. No web claim substitutes for the exact finite
permutation replays.
