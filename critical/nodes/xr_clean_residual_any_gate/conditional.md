# Conditional proof: clean residual any-gate

Status: CONDITIONAL on `xr_smallcore_spread_count`.

The original emptiness formulation is no longer the active requirement.  The
proved `xr_target_budget_audit` reduces the clean-rate obligation to the exact
per-pair inequality

```text
R_post(u, v; A) <= 16 n^3
```

after the quotient and tangent strips, with the dihedral and extension columns
counted inside `R_post`.

The proved `xr_pencil_cascade` classifies the large-core pencil regime
(forcing + cascade only — no payment is proved by that node; under the
ratified Route T partition the band `[k+1, A-1]`, cascade tier included,
is charged by the open third-column obligation
`xr_graded_tangent_band_charge`).  The
proved `dihedral_staircase` gives the linear dihedral cap needed by the same
budget audit.  [CORRECTION 2026-07-10 (xr amber audit, gate-side drift):
`dihedral_staircase` is honestly scoped to the deep regime 3j <= n-k and is
NOT applicable at the clean-rate candidates by its own note; the compiler
needs no dihedral cap there — the dihedral column folds into R_post (pin P3
of the xr_smallcore amber). The sentence above is retained as history.]
Therefore the remaining unproved contributions are precisely the
small-core spread remainder and the band-column charge (the latter carried
inside `xr_smallcore_spread_count`'s route of record since the 2026-08-02
Route T ratification).

Thus, assuming `xr_smallcore_spread_count` supplies the advertised polynomial
bound for that remainder (with its band column charged), the compiled
post-strip residual bound follows and this gate is closed.  No use of the
broader `rigidity_kernel` alternative is needed for this conditional route.
