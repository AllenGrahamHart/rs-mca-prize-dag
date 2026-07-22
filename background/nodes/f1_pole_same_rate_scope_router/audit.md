# Audit

The proof uses the exact objects in the proved interleaved import:
`C_K=RS[K,D,kappa]` and `Phi(C_K)=C_B^e`.  It does not infer rate
preservation merely from an informal phrase such as "corresponding base
row".

The current DAG uses the all-rate node `list_adjacency_closing` inside the
all-rate F1 chain.  That is sound for the full prize but overstates the
dependency of the clean-rate subproblem.  This router records the valid
per-rate projection without weakening the full-prize claim.

The upstream Grande Finale v4 moving-root theorem was also checked during
this audit.  It pays a chart only after all selected residual locators are
proved to lie in one projective pencil.  No such coverage theorem exists for
the XR canonical mismatch charts, so it does not close
`xr_tangent_support_mismatch_bridge`.
