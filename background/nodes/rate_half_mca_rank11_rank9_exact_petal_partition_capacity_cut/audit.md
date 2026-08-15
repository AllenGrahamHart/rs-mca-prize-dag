# Audit

The primary verifier checks the source hash, exact line formula, four
quotient blocks, eight endpoint gaps, adjacent raw signs, persistence
quadratic, every row `10..15634`, and hostile contract mutations.

The independent audit does not use the endpoint reduction as its numerical
oracle. It scans every admissible `a` at `K'=15634`, confirms the unique
maximum, replays all row comparisons against the proved baseline line, and
checks the convex transfer identities on representative boundary data.

All checks use constant-memory exact Python integers and fit the `tiny`
RAMguard profile. Modal is unnecessary for certificate replay.
