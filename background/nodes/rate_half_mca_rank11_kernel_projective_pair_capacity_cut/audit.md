# Audit

The primary verifier reconstructs exact endpoint and wall primal-dual
certificates, checks every individual, shared-resource, and hierarchy
constraint, pins both replay files by SHA-256, and validates the complete
64-chunk custody ledger.  The replay script itself checks all `359516` rows
with exact integers and rationals under a 60-second, 256-MB worker policy.

The independent verifier uses direct tree-path products rather than the
primary backward dual recurrence and separately checks the endpoint signs
and replay ledger.  Floating-point optimization was used only to discover
the active tree and has no status-bearing role.
