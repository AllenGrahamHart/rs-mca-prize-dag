# h_window_derivation

- **status:** PROVED
- **closure:** proof
- **refs (legacy):** ['experimental/notes/roadmaps/a_closure_assembly.md']

## Statement

The 2 log2 n / (log2 n)^2 cap on trade sizes has NO in-repo derivation (proof-agent flag; assembly arithmetic verified at both 20 and 100). Trades can a priori have h up to A (~67 at Row C). RESOLUTIONS (any one): (i) extend (C1) certificates to h <= A (same machinery — x83/A3 apply at every h); (ii) a large-h emptiness lemma (first moment empty by hundreds of bits at h > 20; obstruction count grows with h); (iii) derive the true consumer cap from the list accounting. Must close before the assembly is complete. AUDIT VERDICT (Opus agent, 13/13 replayed): NO banked step caps the consumer at 2 log2 n — that number maps to no repo object. The only banked window is the frozen W3 v1 grammar (log2 n)^2 = 100, which is DEFINITIONAL (an uncharged exclusion, not an emptiness theorem) and sits BELOW the Row-C agreements A = 67/133/261 (rates 1/16, 1/8, 1/4). RESOLUTION ADOPTED: H_max := A — trades with h up to A enter the accounting; A3+X24 apply verbatim at every h; prize-max rows have empty windows and need nothing. PROVED EN ROUTE (all h, verified numerically): <= floor(n/h) partners per anchored core (value-set argument: L_Q = L_P - c with c in the value set of L_P on mu_n, Q -> c injective) — sharpens the h=3 cubic-cap argument uniformly. NEW FLAG: the exact star-PTE support bound (h <= A vs 2h <= A) is unpinned in-repo and changes the gap size — micro-lemma needed.

## Attack surface

route (iii) first (cheap accounting audit); (i) priced by the pilot's feasibility curve; (ii) if the curve is bad

## Falsifier

a consumer trace with h > 2 log2 n trades entering R_PTE at super-absorbable weight

## Ledger

Micro-lemma resolved (star_pte_support_bound PROVED): h <= A, extremes realized explicitly at F_101. The audit's tighter 2h <= A hope is dead.
