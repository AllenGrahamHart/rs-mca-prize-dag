# Proof packet: list corridor ledger

Status recommendation: PROVED, by deterministic assembly.

## Claim

The list-side clean-rate corridor closes at all three clean rates.  The required
ledger inequality is

```text
available_gain(rate) >= W_list(rate) - 1.
```

Using the list-width packet and the proved scale-free floor sweep:

| rate | W_list - 1 | scale-free floor gain | margin |
| --- | ---: | ---: | ---: |
| 1/4 | 0.612526496982 | 0.6328125 | 0.020286003018 |
| 1/8 | 0.075136156735 | 0.09912109375 | 0.023984937015 |
| 1/16 | 0.328340157828 | 0.375 | 0.046659842172 |

All rows pass.

## Applicability of the scale-free floor

The sweep packet proves that the quotient-remainder floor is scale-free: the
lemma hypotheses depend on `(c, m, s, A0)` and not on the printed convenience
scale `N_rho = 1024`.  The floor is a list-size lower bound from the
quotient-remainder prefix/heaviest-prefix locator floor.  Therefore it is a
valid list-side eater, not only an MCA-side accounting device.

The sweep already verifies the relevant best scales:

- rate `1/4`: `(c, d) = (2^25, 209)`, gain `81/128`;
- rate `1/8`: `(c, d) = (2^21, 2251)`, gain `203/2048`;
- rate `1/16`: `(c, d) = (2^28, 11)`, gain `3/8`.

These gains are measured in the same cap-grid units as `W_list`.

## Consequence

The clean-rate list corridor has no remaining width deficit once
`list_corridor_widths` is admitted.  This packet is the list-side mirror of the
proved MCA `corridor_ledger`: exact widths plus a verified scale-free floor
eater collapse the bracket to adjacency at rates `1/4`, `1/8`, and `1/16`.

The rate-`1/2` band is outside this clean-rate packet and remains governed by
`rate_half_band_closure`, as already wired in `list_adjacency_closing`.

## Verifier

Run:

```bash
python3 tools/verify_list_corridor_ledger.py
```

The verifier loads `list_corridor_widths_table.json`, checks
`required = W_list - 1`, checks the exact sweep fractions, verifies every
margin is positive, and runs the underlying cap-envelope sweep verifier.
