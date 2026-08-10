# Proof

The pinned cell-4 pairing-3 elimination is imported by AST at its
`evaluate_case` boundary and supplied with the exact cell-11 tower and kernel.
All 32 sign/lane/`xi` rows terminate with no witness and no unresolved exit.
The exact totals are 192 target roots, 336 candidate roots, 224 guarded source
points, and 128 compatible `(u,v)` lifts.

Independent Frobenius-gcd reconstruction recovers every base-field root from
the printed profiles. Direct audit then rebuilds each root union, candidate
partition, quadratic-pair equation, missing-sum equation, `f` recovery, and
colored-pair cut. All 256 final `f` rows have nonzero colored-pair cuts. The
universal quotient computes the two claimed label orbits exactly.
