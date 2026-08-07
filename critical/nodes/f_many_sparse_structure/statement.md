# f_many_sparse_structure

- **status:** CONDITIONAL
- **closure:** proved implication from an explicit open higher-weight leaf
- **refs (legacy repo):** ['proof_sketch/s3b_iii_3_fibers_and_noanchor.md#1']

## Statement

RESTATED (second revision, after the verified dihedral counterexample): many-sparse flats are MULTIPLICATIVE-pullback-structured, DIHEDRAL/Chebyshev-quotient-structured (X^e g(X^M + X^{-M}) — the new class), tangent-structured, or descent-reducible. The conjecture: nothing UNPAID survives all FOUR branches. The dihedral branch is forced: reciprocal flats are gcd-trivial, multiplicatively aperiodic, and have super-poly lattices — only the enlarged quotient class pays them.

## Attack surface

coding-theory structure: codes with many minimal low-weight words are classified in known regimes; the coset-support pattern (supports = unions of coset pairs) is the signature to force; toy-enumerable falsifier at n = 16

## Falsifier

a toy flat (n = 16 exhaustive over dims 2-3) with many sparse dual words that is neither pullback- nor tangent-classified

## Ledger (migrated notes)

where ALL the residual risk of the F induction concentrates; the other three parts are elementary | E9 census (exact, codim-1 flats at j<=4): third class = support-3 words, structured not unstructured — the revision cost one statement edit because the descent node already existed. | E35 CORRECTION propagates: the multiplicative branch reads X^e g(X^M) (projective/twisted form) wherever the taxonomy lists it — matching the dihedral X^e prefix; the untwisted form is falsified as the literal clause by the {X, X^3, X^5} example.

## False-green repair (2026-08-07)

`f_sparse_rank_split` proves that the growing sparse-rank,
weight-at-least-three branch maps to the Face-4 configuration object. It does
not prove that the object is paid. The missing statement is now the separate
target `f_higher_weight_sparse_payment`; this node is conditional on it.
