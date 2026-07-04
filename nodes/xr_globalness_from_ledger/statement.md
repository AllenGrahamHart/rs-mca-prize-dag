# xr_globalness_from_ledger

- **status:** PROVABLE
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_iii_2_displacement_spectral.md#3']

## Statement

THEOREM (proof written and verified; PROVED modulo the tangent-strip normal form): if every unpaid (j-1)-core has at most L_tan aligned completions (the top-core cap — which IS the tangent/moving-root ledger: completions of a core share the degree-(j-1) divisor; #152 proves the t=2 case as the residual one-exchange-edge bound), then by an exact double count, EVERY r-core link of the post-strip family has density <= L_tan/(n-j+1), uniformly in r <= j-1. Hence A_post is (a, L_tan/(n-j+1))-global in the uniform-slice KLLM sense for all a <= j-1 — a polynomial-scale link parameter, INDEPENDENT of the FM density. The KLLM loss is then poly(n), and the q-power savings remain with the pair ledger c(s,t) = min(s,t-1): the globalness branch no longer consumes the q-budget crux 1 needs. L_tan = 1 (first-unpaid-support convention) or 2 (residual-edge convention).

## Attack surface

quantify the ledger's per-cell caps as link-density bounds at each core size r; compare against KLLM's globalness threshold (the composition arithmetic); the strip handles the quotient links

## Falsifier

a post-strip alignment set with link density above the paid bound at some core size (would be an unpaid tangent leak — an R2 problem, not a route problem)

## Ledger (migrated notes)

PROVENANCE: proof by GPT Pro (relayed by project owner, 2026-07-03); VERIFIED here — algebra re-derived by hand (the binomial cancellation is exact) + 400 brute-force trials on J(10,5)/J(9,4) across all core sizes and both L_tan values. TWO FLAGS for the packet: (a) the quoted KLLM constants (delta = 10^-3 r^-1 eta^3 etc.) are [CITATION NEEDED] — verify against the actual paper in QX.12 before citing (GPT Pro hallucinated a citation once already); (b) the uniform-slice (Johnson) variant of global hypercontractivity must be cited precisely — the cube version does not transfer verbatim. FALSIFIER unchanged and sharper: an unpaid post-strip (j-1)-core with > L_tan completions = an unpaid tangent leak (E19 measures exactly this). | E19 STRESS (#209): 10 post-strip paid-tangent LINK-LEAK CANDIDATES at the exact n=16 corpus — the 'modulo strip normal form' caveat is now LOAD-BEARING: each candidate must be adjudicated (strippable under the correct L_tan convention vs a genuine unpaid tangent leak). The double-count mathematics is unaffected; the hypothesis-pinning is the open work. The #209 corpus is the adjudication test bed. | PACKET AT REPO STANDARD (Fleet A M2): G1 proved with Steiner-system tightness (Fano/SQS(8) meet the bound exactly); BONUS G2 (hereditary cap on junta cells — connects directly to the qx6_qx8 pigeonhole) and G3 (LEAK LOCALIZATION: any r-level link leak localizes upward to a top core — the #209 adjudication reduces to top-core counts only, and E19's per-r tables collapse to one level). HONEST SCOPING SHARPENED: the cap HYPOTHESIS for post-strip families at general in-band t is open — grounded only at t=2 (#152); Convention S needs an unwritten per-core stripping ledger; Convention E is #152's shape. The hypothesis at scale = exchange_ledger_gen_t territory. | C-1 ADJUDICATION (#43, replayed green, PROVED for the exact #209 corpus): all ten post-strip link-leak candidates are STRIPPABLE at L_tan = 1 — every residual support has (j-1)-core multiplicity 1 after T2-paid charging; two candidates are convention-sensitive (character pairs 9/13 and 10/14: they need the L_tan = 1 stripping convention, not L_tan = 2). The E19 leak question is CLOSED at the corpus level: the top-core cap hypothesis survives its sharpest empirical test, with the convention pinned (Convention S, L_tan = 1) as the load-bearing choice.
