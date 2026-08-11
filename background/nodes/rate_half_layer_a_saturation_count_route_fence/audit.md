# Audit

1. The theorem is a family over every odd field containing `mu_32`; the
   verifier specializes only to `F_97` for a compact exact replay.
2. Saturation is checked point by point against all nine slopes, not inferred
   from the total incidence count.
3. The proof identifies the complete kernel, rather than displaying only the
   single vector represented by `Q`.
4. `verify.py` constructs all 26 rows and performs finite-field elimination.
5. `verify_audit.py` does not reuse the elimination routine. It checks the
   four symbolic kernel generators and a hard-coded nonzero `20 x 20` minor.
6. The extra slope has no incidence in `W`. This is permitted by the bare
   count-and-saturation premise and is one reason the stronger endpoint
   hypotheses remain essential.
7. No numerical survival evidence is promoted. The conclusion is an exact
   route fence with the omissions printed in the statement.
