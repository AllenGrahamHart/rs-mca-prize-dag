# Audit

The endpoint verifier checks that the reduction's eight-profile set and the
joint exclusion's eight-profile set are identical. It pins both statements,
checks both dependencies are `PROVED`, and requires exactly those incoming
requirement edges.

The mutation audit rejects a dropped or invented profile and a frontier that
fails to advance by one even-variance step.
