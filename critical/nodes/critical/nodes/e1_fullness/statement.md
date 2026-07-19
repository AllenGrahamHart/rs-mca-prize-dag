# e1_fullness
- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONDITIONAL]
## Statement
The e1 non-quotient collision density estimate: for admissible prize primes,
non-quotient e_1 collisions on C(mu_N', l') are o(1)-sparse relative to the
signed-core quotient (the paid antipodal collisions). collision_norm_criterion
(PROVED) reduces every non-quotient collision to divisibility of an explicit
bounded nonzero norm by p; the ask is the density/typicality count over the
admissible prime family (routes: split-prime transfer extension,
norm_threshold_ext, or a direct bad-prime union bound). DATA (Modal, exact):
N'=16 p=60161: measured value set = signed-core prediction EXACTLY
(3281 = (3^8+1)/2); N'=32: 99.57% at p=1.5e9, 97.66% at p=7e8 (accidents
shrink with p); prize-shape birthday scans (N'=128/256, 250-bit primes,
2^22 samples): ZERO collisions.

## Conditional decomposition

The collision mechanism is reduced by `e1_exceptional_set_reduction`. The
remaining open predicate is `e1_official_prime_exception_control`: the official
row primes must avoid the explicit exceptional norm-divisor set at the needed
density, or be certified directly by the folded lattice procedure.
