# ATTACK — e1_fullness (medium; strongest fresh scaffolding)

## The object is the folded kernel, uniformly over all admissible rows

The proved `kernel_lattice_reframing` reduces an `e_1` collision to a nonzero
folded vector `w in {-2..2}^{N'/2}` with
`sum_x w_x zeta^x == 0 mod p`. The historical certifier experiments are not a
complete shortest-vector proof, and `integer_code_distance_cert` remains a
`TARGET`. `e1_fullness` asks for control of the same kernel object uniformly
over admissible rows.

## Proved inputs to build on
- collision_norm_criterion (PROVED): every non-quotient collision => p divides
  an explicit bounded nonzero norm Res/Norm(w).
- kernel_lattice_reframing (PROVED): the folded short-vector reduction.
- DATA: value set = signed-core quotient exactly at one `N'=16` exhibit;
  smaller-prime collisions occur at `N'=16,32`; prize-shape searches found no
  witnesses in their tested boxes. These are evidence only.

## The residue = a bad-prime DENSITY count (this is the proof)
For each bounded folded pattern w, the "bad primes" are those dividing the
fixed nonzero norm N(w) (finitely many per w: <= log2 N(w)/log2 p). Sum over
the patterns w of support <= 2l': #bad primes <= sum_w omega(N(w)). Bound this
against the admissible-prime count in the window. Routes (node attack surface):
split-prime transfer range; norm_threshold_ext; or the direct union bound.
That average-prime argument cannot by itself prove a statement for every
admissible field. First try to construct exact exceptional rows at prize scale.
If they exist above the budget, reroute the downstream theorem to price their
input-dependent contribution. Otherwise prove a pointwise family bound, or a
complete per-input certifier theorem, at the required scale.
