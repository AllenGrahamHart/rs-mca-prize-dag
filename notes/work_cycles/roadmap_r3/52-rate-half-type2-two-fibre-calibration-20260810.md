# Cycle 52: rate-half type-2 two-fibre calibration (2026-08-10)

## Coordination snapshot

Canonical `prize` was inspected read-only at committed head `45cf661a6`.
Four Round-32 pilots were active in a dirty worktree, so none of their
uncommitted statements was imported. Przemek's upstream main remained
`93fba1be`; 11 open PRs were inspected. PRs `#1151`, `#1152`, and `#1156`
contain relevant LIST, K3, and MCA exception-routing progress, but none
closes an endpoint or supplies this rate-half calibration.

## Proved result

The node `rate_half_type2_fr_two_type1_fibre_spend_calibration` proves the
projective-fibre mechanism and composes it with cycle 51's corrected spend.
For two type-1 slopes at `a=7m-1`, each named fibre has size at least `3m`.
Every type-2 slope therefore spends at least

```text
2m+1
```

roots outside `W`. This improves the minimum-distance-only floor, but its
exact capacity payoff is

```text
T<=2+floor(((9m+1)m)/(2m+1))=9m/2,
```

an exact factor `9/8` above `4m`.

## Corrected frontier

For the same fibre inequality to reach the calibrated spend `9m/4+1`, the
two fibres must total at least

```text
25m/4.
```

Their automatic lower bound is `6m`, so the missing theorem must provide
exactly `m/4` additional fibre mass. Equivalently, the two type-1 root sets
must have total deficit at least `m/4` below `2rho`, leaving at most
`3m/4-1` points in all other fibres.

At the official `m=2^37`, baseline spend is `274877906945`, required spend
is `309237645313`, and the exact shortfall is `34359738368`. The resulting
total cap is `618475290624`, exceeding the target by `68719476736`.

## Route decision

Do not treat the two-type-1 argument as closure and do not optimize the old
`~2m` target. The next positive theorem must force the `25m/4`
concentration, recover the missing `m/4` from strict overlap slack, or use a
collective inequality outside the uniform-spend ledger. No critical status
or crossing bracket changes.
