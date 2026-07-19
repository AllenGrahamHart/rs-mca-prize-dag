# Audit

The proof separates received pairs by the same column-distance predicate used
in the CA definition. In the close case it translates by an actual code pair,
not by independently selected per-slope codewords. Linearity preserves both
agreement and mutual-extension failure, so no slopes are lost and no union
bound is introduced.

The verifier independently exhausts every received pair and finite slope for
two tiny Reed-Solomon codes, at every agreement level. It computes MCA-bad,
far-CA-bad, and sparse-layer slope sets directly from the witness definitions.
