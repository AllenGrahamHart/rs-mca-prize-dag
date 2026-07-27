# Audit

The endpoint verifier checks that the reduction's six-profile set and the
joint exclusion's six-profile set are identical. It pins both statements,
checks that both dependencies are `PROVED`, and requires exactly those two
incoming requirement edges.

The mutation audit rejects a dropped, duplicated, or invented profile and a
frontier that fails to advance by one even-variance step.
