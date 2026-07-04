# xr_triangle_eliminant_form

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/qx13_pair_rank_ledger.md']

## Statement

Write explicitly, in MDS coordinates, the determinantal condition for the twisted sum map on Lambda_0 + Lambda_1 + Lambda_2 to have a kernel in the light regime (sum r - trip <= 2k): the eliminant polynomial in the support coordinates and slopes. Construction only — shortening bases for each Lambda_i, the stacked matrix, the minor structure. Deliverable: the normal form + a toy evaluator (feeds E32's census directly).

## Attack surface

mechanical; generalized-Vandermonde shortening bases make the minors explicit

## Falsifier

n/a (a construction; correctness checked by the evaluator against brute rank)

## Ledger (migrated notes)

PROVED as a construction (270,536 checks): the light-triangle eliminant normal form + evaluator — E32-ext's census tool now exists.
