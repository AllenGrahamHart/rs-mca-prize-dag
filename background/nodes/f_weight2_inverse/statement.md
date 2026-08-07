# f_weight2_inverse

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONDITIONAL]
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e30_dim3_flat_census.md']

## Statement

RESTATED ALONG E35's OBSERVED STRUCTURE (1452 flats, 28/28): if a flat (post common-root strip) carries >= 4 DISJOINT minimal weight-2 dual supports (the MATCHING count, not raw pairs — near-pencils reach raw 6 without symmetry but matching 2), then it is contained in a projective-multiplicative stratum X^e g(X^M) or a dihedral stratum. Empirical basis: the distribution has an EMPTY BAND — nonsymmetric flats have matching count 0-3, symmetric 7-8, nothing at 4-6 (threshold 4, margin 3); collapse under perturbation is all-or-nothing (7-8 -> <=2 in one cell), so the inverse theorem is sharp with no soft regime. PROOF PLAN (two steps): (i) matching composition — >= 4 disjoint two-point ratio constraints compose into a global symmetry candidate; (ii) the candidate lands in the FINITE target (f_dih_subgroup_completeness: cyclic or dihedral, nothing else). STEP (i) PROVED AT QUADRATIC THRESHOLD (Theorem 1, verifier 7/7: m > j + (j-1)^2 disjoint weight-2 supports force GLOBAL PULLBACK: Phi = nu compose psi, every psi-fiber pair a flat-wide ratio edge; engine = value rigidity + P1xP1 Bezout + Luroth; linear threshold W(d) = d+2 open with Lemma D as seed). STEP (ii) FALSIFIED AS STATED and CORRECTED: the conclusion space is NOT Dih_n — witness span{1, q, q^2}, q = X^2+3X over F_17: post-strip, w2m = 7, no Dih stratum, psi-fibers of the affine involution x -> -3-x. The TRUE conclusion space is the LUROTH/PULLBACK LATTICE (intermediate fields F(psi) of F(X)), of which the Dih_n-invariant subfields are the group special case — completeness now by LUROTH'S THEOREM (every intermediate field is F(psi)): closure by classification at the correct level. E35's empty band survives with the enlarged conclusion: abundant flats are pullback-structured (symmetric OR not); primitive stay <= 3.

## Attack surface

step (i) is the content: disjoint weight-2 words are ratio-edges on the domain; composition/transitivity across 4+ disjoint edges within a d-dim flat forces the edge map to extend (dimension count: each independent edge cuts dim by 1; 4 edges over dim <= 3 over-determine); step (ii) is the keystone; E35's all-or-nothing collapse says no stability epsilon is needed

## Falsifier

E35 (RUNNING): a toy flat with super-poly minimal weight-2 supports outside every symmetry stratum — the abundance column on E30's machinery reports it directly

## Ledger (migrated notes)

E35's two LEDGER CORRECTIONS (falsifier-grade, no S9): (1) the multiplicative clause must be PROJECTIVE — X^e g(X^M), not bare g(X^M) ({X,X^3,X^5} has 8 weight-2 supports and is a monomial-twisted pullback the literal list misses; same X^e prefix shape as the dihedral clause); (2) abundance = disjoint-support matching count. Bonus: odd-parity maximal dihedral strata carry forced weight-1 words (fixed-point ratio product -1) — they sit BEHIND the tangent strip already. | Named gaps (alpha, beta, gamma) recorded in f_matching_composition.md; sharpness data: non-Dih involutions attain at most 7 pairs at n = 16 (160 attainers), only Dih reach 8.
