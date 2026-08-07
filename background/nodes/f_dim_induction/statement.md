# f_dim_induction

- **status:** CONDITIONAL
- **closure:** proved implication from explicit open packing and sparse-payment leaves
- **refs (legacy repo):** ['proof_sketch/s3b_iii_3_fibers_and_noanchor.md#1']

## Statement

F_r for gcd-trivial r-flats by induction: at each point of multiplicity >= j, either the hyperplanes through it are SPREAD in the flat (local pair-type counting binds) or coincidences abound (twin-type structure) — forcing a shared divisor factor and descent to F_{r-1} of the reduced instance. Each dimension of excess buys one unit of divisor depth, matching Conjecture F's j - dim P threshold shape. Base case r = 2 = f_dim2_skeleton.

## Attack surface

the open quantification: the spread-vs-coincidence dichotomy at dim r (how much coincidence forces a factor); naive slicing degrades by q^{r-2} so the divisor structure MUST compound — high plane dimensions merge into the fiber/petal machinery already mapped (perfiber, imgfib)

## Falsifier

toy r = 3 census (extend E7) exceeding the compounding-depth prediction

## False-green repair (2026-08-07)

The local spread/rank-defect dichotomy and strict descent are proved. The
uniform absolute-exponent packing step is not: the raw spread numerator grows
like `n^r`, and the higher-weight sparse branch was only routed to Face 4.
Those obligations are now explicit in `f_global_packing_step` and
`f_higher_weight_sparse_payment`.
