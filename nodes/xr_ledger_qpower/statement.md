# xr_ledger_qpower

- **status:** PROVABLE
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_iii_2_displacement_spectral.md#2']

## Statement

RESOLVED IN CLOSED FORM: c(s,t) = min(s, t-1). Theorem (proof written, verified): for agreement supports S,T of size k+t at exchange distance s, codim(K_S cap K_T) = t + min(s,t) — Case r >= k: the two degree-<k explanations are FORCED EQUAL by interpolation on the overlap, giving q^{-(t+s)}; Case r < k: the pair count q^{2k-r} gives exactly q^{-2t} (statistical independence — the plateau). All-slope accounting: same-slope branch q^{1-t-min(s,t)} (union over q slopes), distinct-slope branch q^{2-2t} (the change of variables (u,v) -> (U_z, U_z') is invertible, so distinct-slope words are independent). Net suppression relative to FM: q^{-min(s,t-1)}. LINEAR GROWTH, NO RANK COLLAPSE; saturation at t-1 is the unavoidable distinct-slope independence, not a degeneration. Base case c(1,2)=1 = #152.

## Ledger (migrated notes)

PROVENANCE: derived externally (GPT Pro, relayed by project owner 2026-07-03); INDEPENDENTLY VERIFIED by the roadmap lane — both codim cases re-derived by hand, Monte Carlo at q=5,k=2,t=2 matches (s=1: ratio 0.98 vs q^-3; plateau: 1.07-1.11 vs q^-4). CAVEATS for the packet write-up: (a) this is the exact PAIR-CORRELATION (moment-level) ledger — the fixed-word worst-case conversion remains with the KMS/globalness branch, as the derivation itself states; (b) stated in the plain support-collinearity model — the bridge to LD_sw split-locator conventions needs its ledger row; (c) the cited 'average-support-collinearity packet' does not exist under that name — cite m1_support_coefficient_test.md and the actual #152/#193 anchors. | Fleet A M1: c(s,t) = min(s,t-1) now at repo standard — 164 exact checks over six fields incl. full word enumeration; bridge row written (forward-only per the LD_sw separation); a task-spec arithmetic bug caught and proven as a PASS check.
