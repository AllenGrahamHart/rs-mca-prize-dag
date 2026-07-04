# Proof packet: list corridor widths

Status recommendation: PROVED, by deterministic computation.

## Claim

For the three clean rates, the list-side corridor width in cap-grid units is:

| rate | W_list |
| --- | ---: |
| 1/4 | 1.612526496982 |
| 1/8 | 1.075136156735 |
| 1/16 | 1.328340157828 |

These are the grid-step gaps between the constructive list-unsafe endpoint and
the image-fiber list-safe endpoint.

## Endpoint convention

Use the same reserve coordinates as the MCA corridor packet:

```text
delta = 1 - rho - reserve
```

For the list side:

- unsafe endpoint: `reserve = H(rho) / 128`;
- safe endpoint: `reserve = tau_star(rho, log2 q = 256)`;
- grid step: `eta = 2^-9` for rates `1/4`, `1/8`, and `eta = 2^-10` for rate
  `1/16`.

Thus

```text
W_list(rho) = (H(rho) / 128 - tau_star(rho, 256)) / eta.
```

The table also prints the dyadic upper edge `H(rho) / 256`.  That column is not
the safe endpoint; it is an audit column from the constructive quotient-core
window.  It lies within `0.021` grid steps of `tau_star` at all three clean
rates, matching the `s7_list_side` observation that the list unsafe window's
upper edge nearly coincides with the entropy safe edge.

## Source formulas

The computation uses only formulas already banked in the DAG:

- `H(rho)` from the list quotient-core lower bound in `s7_list_side`;
- `tau_star(rho, q)` from the same entropy crossing used by the corridor-eater
  verifier;
- the cap-grid step convention from `corridor_eaters_computation`.

No search or large-memory experiment is involved.

## Verifier

Run:

```bash
python3 tools/verify_list_corridor_widths.py
```

The verifier recomputes `H`, `tau_star`, all reserves, all deltas, and the
three widths from first principles, then compares them against
`list_corridor_widths_table.json`.
