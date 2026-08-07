# f_primitive_case

- **status:** CONDITIONAL
- **closure:** proved implication from `f_dim_induction`
- **refs (legacy repo):** ['proof_sketch/s3b_iii_3_fibers_and_noanchor.md#1']

## Statement

For every actual prize-consumer flat accepted by
`f_prize_consumer_flat_scope`,

```text
#{ell in P cap D_j : gcd(P cap D_j)=1,
  ell not a pullback, ell unpaid} <= n^B_F.
```

Together with `f_gcd_reduction` and `f_scale_recursion`, this supplies the
consumer-scoped Conjecture-F theorem needed by the prize proof. No theorem for
every abstract linear flat is claimed.

## Attack surface

the irreducible instance every route must face; coordinate planes first (perfiber is its coordinate case), kernel planes second

## Falsifier

toy-scale (n = 16..32) exhaustive plane searches finding super-poly primitive unpaid points

## Ledger (migrated notes)

E7 EVIDENCE (PR #183, replayed green): exact n=16 j=3 projective-plane census — the paid spike is EXACTLY the 16 common-root planes (105 = C(15,2) points each, the tangent shape as predicted); primitive max after removing them = 38 across 240 top planes, BELOW the weighted pair-bound floor 60. Hankel-kernel sample (j=5, t=3, 2048 full-rank planes — the consumer-relevant family): primitive max 13 < floor 30. No rich unpaid primitive dim-2 plane in census or sample. Prior UP. Next refinement: exhaustive j=4 Grassmannian or structured Hankel row-space enumeration.

The 2026-08-07 audit restores this node to CONDITIONAL because
`f_dim_induction` still requires the global packing and higher-weight payment
leaves, and the exact prize consumer scope is itself open. The finite censuses
remain evidence only.
