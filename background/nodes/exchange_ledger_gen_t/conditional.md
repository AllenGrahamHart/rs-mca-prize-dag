# exchange_ledger_gen_t conditional proof

## Predicate node

- `xr_ledger_qpower`

## Claim

The exchange ledger has reach `s_L = t - 1` for general `t`.

## Proof

The predicate `xr_ledger_qpower` gives the closed-form pair ledger

```text
c(s,t) = min(s, t - 1).
```

It also identifies the two regimes: linear q-factor suppression for each
exchange step while `s < t`, and saturation at the distinct-slope independence
plateau. The base case `c(1,2) = 1` is exactly the `#152` one-exchange ledger.

Therefore the general-`t` exchange ledger is obtained by reading the same
closed-form formula at arbitrary `t`: each step up to `t - 1` contributes one
fresh q-factor, and no further q-power can be forced beyond the plateau. This
is precisely the requested generalization.

