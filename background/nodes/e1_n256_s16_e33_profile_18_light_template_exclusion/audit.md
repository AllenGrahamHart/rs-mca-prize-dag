# Audit

- The first six-template draft was rejected by the independent orbit checker,
  which returned the missing support `{0,1,63,64}`. No claim uses that draft.
- Repaired production app `ap-TbM5Ao0mujKzSnl3E7cFL5` completed all 88 cells.
- Eight shards per template cover `310,124=binom(124,3)` heavy supports and
  `19,847,936` sign-normalized vectors per template.
- The source packet records all shard rows, source hash, witnesses, totals,
  and maxima; the verifier replays the production source with a different
  one-shard partition.
- A second C++ implementation forms the ordered negacyclic product rather
  than accumulating unordered signed chords. It reproduces the six profile
  counts and maxima.
- The Python verifier independently enumerates all 132 normalized four-light
  supports and checks that the eleven affine-unit orbit representatives are
  exhaustive.
- Every retained witness is reconstructed independently from its positions
  and coefficients, including profile, conductor, and exact `M_3`.
- Three hostile controls are rejected: omitting the second reflection family,
  omitting one shard, and replacing the exact maximum 1356 by 1355.
- The discarded bare quotient routes are recorded in the route report; no
  quotient upper bound is load-bearing in this proof.
