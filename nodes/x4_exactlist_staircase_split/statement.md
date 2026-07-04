# x4_exactlist_staircase_split

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e35_weight2_abundance.md']

## Statement

The unqualified worst-word exact-list bound is FALSE (verified counterexample: the quotient-coset staircase — locators L_B(X) G(X^M), M | n, M > t, S_Q = tail B plus h full M-cosets; top t+1 coefficients Q-independent so differences are codewords; ExactList >= C(n/M - 1, h), = 2^82.97 at the Row-C toy point vs 16n^3 = 2^34, pairwise overlaps < k throughout). THE CORRECTED STATEMENT: ExactList_C(w, A) <= QuotientStaircase(n,k,t) + DihedralStaircase-analogue + PrimitiveExactList, where QuotientStaircase = the explicit sum over M | n, M > t of coset-staircase terms (exact binomials), and the primitive target is PrimitiveExactList <= n^2 at corridor rows after stripping locators of the forms L_B(X) G(X^M) and X^e L_B(X) G(X^M + zeta X^-M). Transported quotient-row version identical (needed by TR's per-leaf term). MCA-side damage bounded: R_post counts SLOPES, and staircase supports share slopes (v8), so the compiler survives; the split is load-bearing for the LIST challenge and TR arithmetic. At prize rows M > t ~ 2^33 forces n/M <= 256, so staircase terms ~ C(128..256, 32..65) ~ 2^105-115 — under B* but far above 16n^3: QA.22 must re-run the budget with the staircase column. FOUR-COLUMN AMENDMENT (X-4b verdict, witness verified): the split gains the MomentTradeStaircase column — the primitive moment-null blocks are a THIRD cancellation mechanism outside all symmetry; see moment_trade_staircase and x4b_moment_trade_exclusion. The n^2 primitive target now applies AFTER the moment column.

## Attack surface

the staircase terms are EXACT binomials (chargeable by census); the primitive bound post-strip is the new deep target — the strip removes precisely the coefficient-cancellation mechanism, so a primitive list member's locator has full coefficient spread: quantify via the eliminant/Wronskian of the locator differences

## Falsifier

a primitive (post-strip) worst-word exact list exceeding n^2 at a toy corridor row (searchable: extend the staircase enumerator with a strip filter)

## Ledger (migrated notes)

Codex red-node pass (2026-07-04): reclassified from TARGET to CONDITIONAL.
The split is an assembly theorem: explicit quotient/dihedral staircases + the
proved moment-trade mechanism + x4b's per-row moment handling + U1's
post-dictionary primitive cap imply the corrected exact-list bound. QA.22: the
staircase columns are AFFORDABLE at every candidate — the split's arithmetic
viability is now verified, not expected.
