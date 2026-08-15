# Audit

The primary verifier reconstructs the exact conditional start, endpoint,
and wall
primal-dual certificates, checks every individual, shared-resource, and
hierarchy constraint, pins both replay files by SHA-256, and validates the
complete 64-chunk custody ledger.  The replay checks all `190666` rows with
exact integers and rationals under a 60-second, 256-MB worker policy.

Neither verifier proves the uniform-cap premise.  The independent verifier
uses direct tree-path products rather than the
backward dual recurrence and separately checks the endpoint signs and replay
ledger.  Floating-point optimization was used only to discover the active
tree and has no status-bearing role.
