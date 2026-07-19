# conj_f

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONDITIONAL]
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_iii_3_fibers_and_noanchor.md#1']

## Statement

For every linear P <= P^j and pair (u,v): the D_j-points of P are, up to n^{B_F} exceptions, covered by a shared divisor of degree >= j - dim P - O(log_n) (tangent shape) or a proper quotient-pullback stratum (periodic shape).

## Attack surface

prove coordinate planes first (= prob:perfiber, minimal instance), then kernel planes; the crux is classifying exceptional planes (ES-type)

## Falsifier

a toy-scale plane family (n = 16..32, enumerable) with super-poly D_j points, no deep shared divisor, no pullback symmetry

## Ledger (migrated notes)

CONDITIONAL (Codex critical pass): full Conjecture F follows from the
primitive case via the proved gcd reduction and proved multiplicative scale
recursion. The frontier is now isolated in `f_primitive_case`.
