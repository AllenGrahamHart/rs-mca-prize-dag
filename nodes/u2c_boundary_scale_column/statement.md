# u2c_boundary_scale_column

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/u2c_giant_block_statement.md']

## Statement

(1) DICTIONARY CLAUSE: mu_t-coset unions with zero-sum value patterns (and the multi-level generalization for non-2-power t*: zero sums at each multiple of M <= t*) join the charged classes — exactly characterized, exactly countable (subset-sum collision counts, ~max(0, 2^{R/2}/q) scale). (2) QA.25 CROSSOVER ARITHMETIC: per admissible row, the boundary-column staircase mass vs B* = q/2^128 — the count GROWS as q shrinks while B* SHRINKS: locate the crossover row exactly; above it (incl. all six campaign candidates, verified nearly-empty) the column fits; below it the rows need richer per-row analysis (possibly a new determined-region-style boundary in q). (3) The residual dichotomy conjecture (U2-C'): every t-null block is a union of mu_M-cosets with M >= t... M = t INCLUDED... with zero-sum patterns — i.e., the boundary class + the old dictionary EXHAUST t-null blocks. The X-8 construction is consistent with this; its falsifier is a t-null block that is not even a boundary-scale coset union.

## Attack surface

the counting is elementary (subset-sum collision enumeration/bounds); the residual dichotomy may follow from the antipodal-descent structure one scale down; QA.25 is pure arithmetic

## Falsifier

a t-null block that is not a union of mu_M-cosets for ANY M >= t dividing n (searchable: the toy scan machinery with the fiber test at M = t added — cheap extension)

## Ledger (migrated notes)

(B) DECOMPOSED (roadmap-lane): B1 the char-0 giant coset theorem — PROVED (one-paragraph Galois/Fourier argument, exhaustively toy-verified); B2a the boundary class — exactly counted (QA.25 fits); B2b the mod-p extras bound — the residue, with the Frobenius gap explaining WHY it exists, the first-moment balance explaining why counting can't close it, and the 123-bit cushion changing its difficulty class (no-concentration, not exclusion). (B) is now structurally parallel to (A): char-0 classification proved + one mod-p gap lemma — but WITHOUT the universal-variety trick (2^41 variables), compensated by the cushion.
