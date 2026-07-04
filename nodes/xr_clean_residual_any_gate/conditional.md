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

The proved `xr_pencil_cascade` removes the large-core pencil regime.  The
proved `dihedral_staircase` gives the linear dihedral cap needed by the same
budget audit.  Therefore the remaining unproved contribution is precisely the
small-core spread remainder.

Thus, assuming `xr_smallcore_spread_count` supplies the advertised polynomial
bound for that remainder, the compiled post-strip residual bound follows and
this gate is closed.  No use of the broader `rigidity_kernel` alternative is
needed for this conditional route.
