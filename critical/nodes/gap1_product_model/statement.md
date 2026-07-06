# gap1_product_model

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/evidence_plan_codex.md']

## Statement

Conditional reduction: the tower product bound is already proved, removing
cross-character amplification; the remaining terminal reserve is exactly the
TR chain, namely joint-stabilizer telescoping plus the quotient-row per-leaf
exact-list supply. Under tr_joint_telescope and tr_perleaf_list_ident, the
non-equivariant periodic mass is bounded by the per-character product with
poly(n) x FM reserve.

## Attack surface

extend the PROVED base-case lemma (alpha^M in base field) to intermediate fields — the repo's most-repeated recursion pattern, fourth appearance; then sum over characters

## Falsifier

a periodic model exceeding the per-character product rank (E6 found none across F_13/F_97 exact + F_257 to n=256)

## Ledger (migrated notes)

Codex red-node pass (2026-07-04): reclassified from CONJECTURE to
CONDITIONAL. The product theorem half is banked; the open terminal reserve is
now wired to tr_joint_telescope and tr_perleaf_list_ident rather than left as
prose. Provenance: Codex (#212), the third handoff item; verified by replay +
structural check. GAP-1 now reduces to a counting step (the terminal
per-character reserve estimate). | TERMINAL STEP VERDICT (Fleet A M4-retry,
verifier 9/9): the crude |K|-line count is INSUFFICIENT — short by 119.96 bits
(pinned row) to 951.5 bits (Row C corridor candidate); the dominating factor is
|K| >= q vs a <= +49-bit budget. The precise remaining statement is CONJECTURE
TR: the JOINT product over active characters of per-character sets — each a
same-rate quotient-row instance at scale n/M — is <= n^B x max(1, FM).
Per-leaf FM bounds over-aggregate by q^{M-1} when M > t: the bound must be
joint. The multi-scale recursion's FIFTH appearance: GAP-1's closure is
R2/FM-flavored at the quotient rows.
