# certified_valueset_lower conditional proof

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONDITIONAL]
- **closure:** proof from predicate nodes

## Predicate nodes

Required generator-design route:

- `graded_collision_radius`
- `far_pair_separation`
- `certifier_uniformity`

Alternative direct route:

- `lattice_cone_certificate`

## Claim

Conditional on the predicate nodes, each knife-edge row has a certified
value-set lower bound

```text
|{e1(B) mod p}| > B*.
```

## Proof

The goal is to exhibit a family of quotient classes whose `e1` values are
pairwise distinct modulo the row prime `p`, with total size exceeding `B*`.

The predicate `graded_collision_radius` supplies the local certificate rule:
within the certified small swap-radius cells, every relevant pair is
collision-free because the cyclotomic norm of the nonzero `e1` difference is
strictly below `p`.

The predicate `far_pair_separation` supplies the global family design. It
separates the cells so that every cross-cell `e1` difference is reduced to a
finite list of certified generator checks. Thus the all-pairs distinctness
obligation for a family larger than `B*` is compressed to the listed finite
checks rather than sampled.

The predicate `certifier_uniformity` supplies totality and correctness of the
per-row certificate procedure under the adopted Reading-B semantics. Therefore
the generator checks and any branch-and-bound subchecks they call produce a
proved certificate, not an empirical witness.

Combining these inputs, the exhibited family has more than `B*` classes and all
of their `e1` values are pairwise distinct modulo `p`. This proves the required
per-prime value-set lower bound.

If the lattice route is used instead, `lattice_cone_certificate` proves full
injectivity of the relevant row cell directly; the same lower bound follows
from the exact cell count being above `B*`. This is an alternative route, not an
extra requirement for the generator-design route.
