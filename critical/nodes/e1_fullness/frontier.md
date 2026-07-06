# frontier: e1_fullness

The collision mechanism is now a wired proved reduction:
`e1_exceptional_set_reduction`.

## Proved inputs

- `collision_norm_criterion`: every non-quotient collision forces the row
  prime to divide an explicit nonzero cyclotomic norm.
- `kernel_lattice_reframing`: per-prime collisions are exactly sparse ternary
  kernel vectors; after antipodal folding this is a short vector
  `w in {-2..2}^{N'/2}`.
- `graded_collision_radius`: small swap-distance pairs are unconditionally
  collision-free by the height threshold.
- `are_exceptional_density`: an almost-all-primes Markov statement from
  summing norm prime divisors.

## Evidence

The folded-certificate note records exact toy behavior:

- `N'=16, p=60161`: certified full, matching the signed-core quotient count;
- `N'=16, p=10177`: bad-prime collisions exist;
- `N'=32`: collisions exist at smaller primes and support grows.

The statement also records prize-shape birthday scans with zero collisions,
but those are evidence only.

## Remaining theorem

The open content is:

> For admissible prize-scale primes in the open cells `N' in {128,256}`,
> non-quotient folded short-vector collisions are `o(1)`-sparse relative to
> the signed-core quotient.

This is now the node `e1_official_prime_exception_control`: the admissible
row-prime family must avoid almost all of the norm-divisor exceptional set, or
the pinned rows must be certified directly.

## Routes

- direct bad-prime union bound over folded patterns;
- extend the split-prime transfer range (`amplification_range_ext`);
- prove a norm-threshold extension that reaches the prize-scale cells;
- certify the specific exhibit primes by exact lattice enumeration, if the
  row instances are pinned.

## Falsifier

A prize-scale admissible prime with a nonzero folded vector
`w in {-2..2}^{N'/2}` at the relevant support threshold, producing a
non-quotient `e_1` collision density above the allowed budget.
