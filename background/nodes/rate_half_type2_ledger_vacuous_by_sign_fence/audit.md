# Audit

1. The fence is exact integer arithmetic — no sampling, no field choice, no
   asymptotics — so PROVED is the honest status.
2. The equivalence `2r <= R <=> a >= 3n/4` is specific to rate one half
   (`k = n/2`); both verifiers state and use that hypothesis.
3. `verify.py` checks the equivalence with rationals and samples the
   bracket; `verify_audit.py` shares no code path — integers only, the
   floor derived through the rho-decomposition `1 - 62*rho`, and the
   bracket covered by monotonicity plus one endpoint rather than samples.
4. The adversary's `w* = 2r` is the DISJOINT-support end of the admissible
   range; the fence needs no claim that disjointness is attained, only
   that nothing excludes it (adversary-free direction).
5. The source's `w*` measurements sat under a 24-locator cap; the cap's
   direction favours vacuity, and the fence does not rely on them.
6. Statement U, referenced by the draft as the value question, was refuted
   in round 37; the wiring updates those references. The refutation
   changes the bracket's expected value, not the ledger's sign.
7. Edge character: evidence/route-restriction only. No requirement of
   `rate_half_band_crossing_location` is discharged.
