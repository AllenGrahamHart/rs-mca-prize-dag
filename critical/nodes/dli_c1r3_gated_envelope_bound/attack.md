# Attack routes (round-3 escalation targets, from the r3b report sec. 6)

1. Octave-31 census completion (199 rows; 4 rows need a compute-law
   amendment or contributor run — >16GiB / longer ceiling at q > 4.05e9).
2. The full-ledger lever (drop w_max entirely) if any extended zone slot
   resists.
3. A quantitative iid-approximation theorem under v_2(q-1) large — the bulk
   proof lead; 918552577 is the worked example of accident-vs-ledger
   cancellation.
4. Gated L=2: a proof-side level-uniformity argument is the only route
   (exact reach is impossible).

## [2026-08-01] The 256-basis factorisation is banked as evidence

`dli_c1_256_block_basis_factorization` (PROVED, background, ev into this
node) establishes: every official level's odd-moment matrix is 256
invertible blocks `A_a = D_a F`; each block Fourier marginal is EXACTLY
iid; all spectral excess is cross-block dependence along the single
companion orbit `C_a = M^a C_0`, `M = F^T D_1 F^(-T)`. Consequence for
this node's attack language: "iid saturation" is now a theorem-shaped
statement — the open question is the dependence structure of one
deterministic 256-step orbit, with short signed relations as its
low-complexity resonance certificates. The proposed successor
architecture (C1-ZERO / SWIF-4 + ten WCL slots + Newton => consumer) and
its gates are recorded in
`notes/pro_briefs_20260801/responses/BRIEF1_PRO_DOSSIER.md` and
`.../BRIEF1_DOSSIER_AUDIT.md`. No status change here; the route fences
(no prime census, no q-sized DP, no v2-surplus argument at the top level)
are binding on future attacks.
