# gap1_noneq_mass

- **status:** CONJECTURE
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_ii_strip_periodic.md#3']

## Statement

#{aligned (l, Z): root set K_M-stable but (u,v) multi-isotypic (non-equivariant) on the stratum} <= poly(n) * FM — the isotypic escape stratum carries no super-poly alignment mass.

## Attack surface

bound the multi-isotypic stratum via the isotypic decomposition + FM; the stratum is thin (non-equivariant data on stable supports)

## Falsifier

toy enumeration (gap1_toy_test) showing non-equivariant periodic alignments outgrowing poly

## Ledger (migrated notes)

E6 (PR #187): NO amplification signal in any tested periodic model (exact F_13/F_97 all-support + F_257 to n=256); packet PROVES the local isotypic base-line rank lemma (alpha^M in base field => each character maps into one line alpha^r B => cosets cannot add slope exponent) — the per-character product model looks like the MECHANISM, not just a bound. Prior UP strongly. | With #212's product mechanism, GAP-1 = one remaining counting step (terminal reserve estimate). | Reduced to Conjecture TR (joint quotient-row FM bound) — see gap1_product_model. The convergence deepens: GAP-1, F, spread, and the clean-rate exclusion all funnel toward the same rigidity/counting core at quotient scales. | FACE 1 SIMPLIFIED (E34): Conjecture TR's jointness is STRUCTURAL — exact telescoping to a single instance at the joint-stabilizer scale (class-closure form). Remaining: (i) lift the identity from linear-model counts to aligned A_r sets; (ii) the per-leaf bound = the list-lane identification (tr_perleaf_list_ident). The q^{M-1} over-aggregation M4 flagged is gone by construction. | FACE 1 STATUS after the lifting lemma: jointness fully closed (structural + lifted); the ENTIRE remaining face-1 content = the per-leaf bound in its corrected split form (x4_exactlist_staircase_split at quotient rows) + the degenerate-tower bookkeeping (count transfer conditional there — charge degenerate towers separately or exclude by row arithmetic). | QA.24: the degenerate-tower correction column exists and is universal (all consumer triples) — face 1's arithmetic uses corrected counts; no route change.
