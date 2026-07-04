# ATTACK — e1_fullness (medium; strongest fresh scaffolding)

## The object is IDENTICAL to the certifier lattice (just all-primes)
The proved-and-computed certifier work reduces an e1 collision to a nonzero
folded vector w in {-2..2}^{N'/2} with sum_x w_x zeta^x == 0 mod p (see
nodes/integer_code_distance_cert/notes/folded_certificate.md, PROVED +
machine-certified). e1_fullness is the SAME object quantified over admissible
primes: "non-quotient collisions are o(1)-sparse."

## Proved inputs to build on
- collision_norm_criterion (PROVED): every non-quotient collision => p divides
  an explicit bounded nonzero norm Res/Norm(w).
- kernel_lattice_reframing (PROVED): the folded short-vector reduction.
- DATA: value set = signed-core quotient EXACTLY at N'=16 (3281=3281); 99.6% at
  N'=32 (accidents shrink in p); the dim-64 Row-C cell CERTIFIED (0 vectors
  below threshold, 449s) — so a good prime has NO short folded vector.

## The residue = a bad-prime DENSITY count (this is the proof)
For each bounded folded pattern w, the "bad primes" are those dividing the
fixed nonzero norm N(w) (finitely many per w: <= log2 N(w)/log2 p). Sum over
the patterns w of support <= 2l': #bad primes <= sum_w omega(N(w)). Bound this
against the admissible-prime count in the window. Routes (node attack surface):
split-prime transfer range; norm_threshold_ext; or the direct union bound.
GOAL: show #{patterns} x max omega(N(w)) = o(#admissible primes) => o(1)-sparse.
The certifier's Gaussian-heuristic "~2^-50 bad at N'=128" is the target scale.
