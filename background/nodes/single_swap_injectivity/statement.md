# single_swap_injectivity

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

For classes differing in one element, e1(B) - e1(B') = zeta^i - zeta^j has all archimedean conjugates <= 2, so its norm is <= 2^{phi(N')} ~ 2^{N'/2} << p ~ 2^250. Nonzero (thm:upstairs) and of height below p => p cannot divide it => single-swap pairs NEVER collide at prize scale. Unconditional, for every prime in the admissible range.

## Ledger (migrated notes)

the base case of certified distinctness: the swap-metric graph's edges are all collision-free; the open problem is composing this into large all-pairs-distinct families | Subsumed as the s=1 case of graded_collision_radius; kept as the write-up's base case. | PROVED 2026-07-04 as the s=1 norm-radius case.
