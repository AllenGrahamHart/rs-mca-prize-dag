# acl_count

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

EXACT SLOPE COUNT (thm:exactcount, Paper B / slackMCA). With N' = n/sigma, n_1 = N'/2, l' = rho N' + 1, let A(N',l') = sum over u >= 0, t = l' - 2u >= 0, u <= n_1 - t of binom(n_1,t) 2^t be the number of antipodal-rearrangement classes of l'-subsets of mu_{N'} (class invariant: the signed set of singleton antipodal pairs together with the number of full pairs). Then for every prime IN THE STABLE RANGE the canonical line's bad-slope count is exactly B(p) = A(N',l'), and at rho = 1/2, B(p) = (3^{n/(2 sigma)} - 1)/2. Consequently at safe slack B(p) = n^{beta(rho)/c_eff + o(1)} with beta(rho) = (1/2) max over 0 <= theta <= 2 min(rho,1-rho) of (H(theta) + theta). SCOPE FENCE (load-bearing): exactness holds only ABOVE THE QUOTIENT NORM THRESHOLD p > (2 l')^{N'/2}. At log2 q = 256 and rho = 1/2 that means N' <= 80 — zone (a) of proof_sketch/s2_paid_ledger.md#3, which is the PROVED-exact zone. The range 80 < N' < ~512 is zone (b), explicitly CONJECTURAL in that source and carried by the separate node `zone_b` (CONDITIONAL). This node claims only the zone-(a) exact count. REF CORRECTED 2026-07-27: the previous ref pointed at proof_sketch/s3b_iii_3_fibers_and_noanchor.md#2 (tagged SKETCH, on Conjecture F unification), which does not state this theorem; the real source is thm:exactcount in archived/slackMCA_v3.tex upstream.
