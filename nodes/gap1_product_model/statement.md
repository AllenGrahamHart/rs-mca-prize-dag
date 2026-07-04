# gap1_product_model

- **status:** CONJECTURE
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/evidence_plan_codex.md']

## Statement

HALF PROVED (in flight, #212 — verified here: three verifiers replayed green, Theorems 1-3 structure checked): the tower product bound — each character maps into one intermediate-field line (P_r(alpha) = alpha^r G_r(beta) in alpha^r K), multi-character mass <= the per-character product, and the recursion runs down any tower B = K_0 <= ... <= K_s. CROSS-CHARACTER AMPLIFICATION IS REMOVED. The OPEN half: the terminal reserve estimate — per-character counts summed against poly(n) x FM (the note keeps this explicitly open).

## Attack surface

extend the PROVED base-case lemma (alpha^M in base field) to intermediate fields — the repo's most-repeated recursion pattern, fourth appearance; then sum over characters

## Falsifier

a periodic model exceeding the per-character product rank (E6 found none across F_13/F_97 exact + F_257 to n=256)

## Ledger (migrated notes)

Provenance: Codex (#212), the third handoff item; verified by replay + structural check. GAP-1 now reduces to a counting step (the terminal per-character reserve estimate). | TERMINAL STEP VERDICT (Fleet A M4-retry, verifier 9/9): the crude |K|-line count is INSUFFICIENT — short by 119.96 bits (pinned row) to 951.5 bits (Row C corridor candidate); the dominating factor is |K| >= q vs a <= +49-bit budget. The precise remaining statement is CONJECTURE TR: the JOINT product over active characters of per-character sets — each a same-rate quotient-row instance at scale n/M — is <= n^B x max(1, FM). Per-leaf FM bounds over-aggregate by q^{M-1} when M > t: the bound must be joint. The multi-scale recursion's FIFTH appearance: GAP-1's closure is R2/FM-flavored at the quotient rows.
