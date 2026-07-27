# averaged_xr

- **status:** see dag.json (single source of truth; dag status TARGET)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

AVERAGED XR (the slope-resolved second moment). Claim sought: second moments of |A_{u,v}| over pairs (u,v) (or over slopes) admit explicit Cauchy double sums over pairs (T,T') graded by intersection size, so that the Johnson-scheme decomposition applies and the lam_0 - lam_1 = n gap gives variance control; same-slope pairs carry the closed-form correlation term while distinct-slope pairs are independent. This is what `averaged_slope_conversion` consumes as its second moment. DEMOTED PROVED -> TARGET 2026-07-27 (false green, three independent reasons): (i) the node's proof.md auto-discharges 'the conditional implication (see conditional.md)' but NO conditional.md exists in the folder — there is no implication to invoke; (ii) its sole req-predicate `xr_ledger_exponent_reconciliation` RECONCILES 'averaged_xr's stated shell exponent q^{-min(s,t)} with the proved ledger's c(s,t) = min(s,t-1)' — it presupposes this claim and cannot prove it; (iii) the node's own sketch.md records status PROVABLE, and the upstream source (proof_sketch/s3b_iii_2_displacement_spectral.md#5, tagged SKETCH) says only that the averaged form 'LOOKS PROVABLE with current tools', explicitly leaving worst-case de-correlation as the wall. ATTACK: the Hooley-Katz / Scott exponential-sum lane named in that section. FALSIFIER: a shell where the reconciled exponent c(s,t) breaks the variance control the conversion needs.
