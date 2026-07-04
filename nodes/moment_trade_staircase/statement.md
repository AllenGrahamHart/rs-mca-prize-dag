# moment_trade_staircase

- **status:** PROVABLE
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e35_weight2_abundance.md']

## Statement

Cancellation is NOT symmetry: any disjoint family of t-moment-null blocks (e_1(B) = ... = e_t(B) = 0, |B| > t) generates exact-list staircases exactly as the quotient/dihedral ones do — the block locators have zero top-t sub-leading coefficients, so unions share top coefficients and differences drop to degree < k. VERIFIED PRIMITIVE WITNESS: B = {11^e : e in {0,1,2,4,16,45,50,60}} in mu_64 over F_193 — power sums vanish for r = 1,2,3 (r = 4 gives 18), locator top-3 sub-leading coefficients literally zero, NO rotation or reflection stabilizer (all independently recomputed). Replicated across cosets: post-strip exact lists >= C(R, R/2), exponential in n — the quotient/dihedral strip provably misses it. CODING IDENTITY: t-moment-null blocks are 0/1-coefficient dual codewords with t leading zero syndromes — sparse dual words at weights ABOVE every census we ran (E9/E30/E35 covered weight <= 4; structural blindness, honest lesson). The symmetry classes are the special case where invariance forces moment-nullity; the general class is Prouhet-Tarry-Escott-flavored and p-SPECIFIC.

## Attack surface

existence per (n, p, t, b) is a classical-flavored finite-field question (0/1 words in cyclic-code duals with prescribed leading zeros) — CHECKABLE per official row (the Reading-B certification engine hook); E37 censuses toy and official-like rows

## Falsifier

n/a for the class (witness verified); the per-row EXCLUSION statements are the falsifiable targets

## Ledger (migrated notes)

THE UNIFICATION (matching-composition witness + fiber arithmetic, verified): t-moment-null blocks of size b ARE fibers of polynomials with zero top-t coefficients (elementary symmetric functions of a fiber = the map's coefficients, invariant in the fiber value below e_b), and the matching-composition counterexample's psi-fiber pairs are the same class at b = 2. The fifth mechanism = PULLBACK ALONG RATIONAL MAPS with coefficient constraints; the symmetry quotients are its invertible/group special cases. Trade FAMILIES mix maps across blocks (each block a fiber of its own map) — the family class is the mixed-pullback closure.
