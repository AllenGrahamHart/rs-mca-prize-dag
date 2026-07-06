# xr_sunflower_rank_additive

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/qx13_pair_rank_ledger.md']

## Statement

If an aligned far-spread family is a sunflower (all pairwise intersections equal one common core Y, |Y| < k), every syzygy member is supported inside Y (cancellation only on shared points), and |Y| < k+1 = the MDS dual minimum weight forces all members to vanish: NO nontrivial syzygy exists, so by the alpha anatomy every member contributes its FULL t rows and the family size is <= 2n/t per pair (~630 at prize-max rate 1/4). REVERSAL NOTE: the list lane's planted-sunflower worst cases are exactly the MCA-side's provably-safe configurations — the two challenges' hard directions are disjoint here.

## Attack surface

the proof is the three sentences above (alpha's support cancellation + the dual weight); package with the exact rank bookkeeping (each member adds exactly t)

## Falsifier

a toy aligned sunflower with rank increment < t at some member (mechanical stacked-rank check)

## Ledger (migrated notes)

PROVED (552,814 checks): sunflowers never stagnate; the exact cap m <= floor(2n/t) per pair is proved, not just the shape.
