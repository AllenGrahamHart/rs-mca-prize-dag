# Audit

Date: 2026-07-27.

The candidate table is pinned to
`critical/nodes/xr_smallcore_spread_count/notes/audit_consumption_replay_20260710.py`
with SHA-256
`c39442d16fcbe86bbfd97f245de970dc729d0e257514c6d4f9f74c9a8c7fac56`.
The parent theorem is independently reconstructed from upstream `prop:floor`
at commit `b13de8113a03f06b6fc22bbd2f289a8abcdf7e95`.

The verifier recomputes all six error counts and cutoffs, tests the cutoff on
both sides, checks the named budgets, and enforces the DAG status and edges.
The high-budget negative result is deliberately typed as route failure rather
than as evidence for safety.
