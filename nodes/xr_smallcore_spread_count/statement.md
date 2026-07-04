# xr_smallcore_spread_count

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e27_exceptional_pair_census.md']

## Statement

For every pair (u,v): the number of aligned aperiodic supports whose agreement sets pairwise share cores < k+t-1 (the post-cascade remainder — a SPREAD family in the face-3 sense) is <= poly(n). E27's toy data: this remainder sits exactly in the FM band (unstructured mult->=2 events at FM-normalized rates, all classification tests at chance) — clause (ii) of the rigidity kernel holds empirically for the remainder. This is face 4's residual content after the cascade lemma — and it is a SPREAD-FAMILY count: face 3's machinery (design bounds, syzygy circuits, the exception classes) is the natural instrument. The convergence: face 4 decomposes into a provable forcing lemma + a face-3-type bound + the dihedral staircase.

## Attack surface

pairwise-small-core aligned families are sunflower-free configurations of size-A sets; design/anticode bounds at intersection threshold k+t-1; the eliminant route counts them as bounded-deficiency solutions; E27's spectrum calibrates constants

## Falsifier

a toy pair with super-poly many pairwise-small-core aligned supports (searchable with E27's pencil machinery)

## Ledger (migrated notes)

DECOMPOSED (close-look pass, conventions pinned against qx13): the split is FORCED by proved machinery — (2a) same-slope families are automatically far-spread and equal the LIST challenge's worst-word object (the two grand challenges meet); (2b) the partial-forcing band r in [k+1, A-2] reduces to a graded tangent ledger via one-line two-slope forcing; (2c) the far-spread core = the fresh-codimension-or-structure dichotomy — the face's single irreducible statement. Pairwise additivity at distinct slopes is rank-level PROVED (qx13 2b); only the m >= 3 stagnation dichotomy is genuinely open.
