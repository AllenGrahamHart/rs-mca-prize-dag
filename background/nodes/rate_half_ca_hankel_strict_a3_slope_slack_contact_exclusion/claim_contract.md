# Claim contract

- **Claim:** all strict slope-slack profiles satisfying
  `floor(delta/2)+h+2<e` are impossible; only `(SSC4)` escapes officially.
- **Dependencies:** the slope-slack ledger and universal Forney contact
  section.
- **Output:** reduction of the strict `A=3` frontier to one exact profile.
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaim:** the final `delta=1,T=rho+2` corner is not excluded.
- **Falsifier:** pole colength above `delta`, failure of the contact-active
  component argument, a nonzero section of the negative line bundle in
  `(7)`, or an omitted official integer profile.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_strict_a3_slope_slack_contact_exclusion/verify.py`
  and `verify_audit.py`.
