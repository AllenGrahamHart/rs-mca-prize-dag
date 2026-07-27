# Audit

The endpoint verifier checks that the reduction's ten-profile set is the
disjoint union of the six-profile two-odd exclusion and the four-profile
six-odd exclusion. It pins all three statements, checks that every dependency
is `PROVED`, and requires exactly those three incoming requirement edges.

The mutation audit rejects a dropped, duplicated, or invented profile, an
overlap between branches, and a frontier that fails to advance by one
even-variance step.
