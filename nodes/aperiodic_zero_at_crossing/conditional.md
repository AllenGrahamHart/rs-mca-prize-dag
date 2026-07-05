# conditional proof: aperiodic_zero_at_crossing

- **status:** CONDITIONAL
- **closure:** proof

## Predicate nodes

- `fm1`
- `r2_clean_rates`

## Claim

At the clean-rate decision candidates (`rho` in `{1/4, 1/8, 1/16}`), the
aperiodic contribution is not killed by integrality at `A*` or `A*+1`; the
exactly-zero range begins at `A*+2`, with the live `A*+1` term decided using
the compiled clean-rate R2 bound.

This node makes no rate-`1/2` claim.  The rate-`1/2` thin point and residual
band are routed through `rate_half_band_closure`.

## Proof

The predicate `fm1` supplies the exact first-moment normalization on the
aperiodic stratum.  The predicate `r2_clean_rates` supplies the clean-rate
compiled bound

```text
R_post(u, v; A) <= 16 n^3.
```

Substituting that bound into the audited margin table gives positive
`log2(n^3 FM)` margins at `A*` and `A*+1`, so integrality cannot set the
aperiodic contribution to zero there.  The same table is monotone from
`A*+2`, where the clean-rate margins are negative, so the contribution is
zero from that radius onward.

Therefore the clean-rate adjacency machinery must explicitly decide `A*+1`
with the R2 constant, and may use exact zero only from `A*+2`.

## Ledger

RATE-SCOPE REPAIR 2026-07-06: the old all-row wording over-claimed because
`r2_clean_rates` is clean-rate scoped.  The rate-`1/2` instance remains outside
this node and is carried by `rate_half_band_closure`.
