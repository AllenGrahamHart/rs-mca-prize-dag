# f1_pole_list_threshold_location conditional proof

## Predicate nodes

- `list_adjacency_closing`
- `ext_import`

## Claim

The pole-case list-threshold location follows from the list adjacency theorem
and the imported extension-pole/list bridge.

## Proof

The node's only quantitative assertion is that, at the non-generating rows
priced by `f1_case_pole`, the base-row list threshold lies below the corridor
crossing used by the pole ledger.

The predicate `ext_import` supplies the bridge: for the simple-pole extension
family, the extension-pole witness count `N(L)` crosses the MCA gate
`|F| 2^-128` exactly when the corresponding base list reaches the list-side
threshold `L ~ 2^128`. Therefore the pole ledger does not need a new
counting theorem; it needs the base list crossing to be localized at the
official corridor point.

That localization is precisely the content of `list_adjacency_closing`: for
each admissible row, with the official `m` quantifier, the worst-word list
count is above the epsilon gate at the unsafe radius and at most the epsilon
gate at the adjacent safe radius. Reading this statement at the base row gives
the required threshold location.

In non-generating rows the generator field satisfies `q_gen < 2^128`, so the
extra doubled-base reserve only moves the required base-side inequality in the
safe direction. Thus no additional F-lane case remains after
`list_adjacency_closing` and `ext_import`.

## Stress evidence

`experiments/amber_stress/f1_pole_threshold_probe.py` checks the exact
extension-pole floor

```text
N(L) = ceil(L(|F|-|B|) / (|F|-|B| + 2^40 L))
```

against the MCA gate on adversarial non-generating rows with `|B| < 2^128`,
`|B|^2 < |F|`, and `|F| < 2^256`.  The current run tested `92` official-like
integer rows and found no premature crossing, no missing crossing, and no row
where the crossing escaped the doubled-base reserve.  The largest additive
delay over the integer gate was exactly `2^40`, at the top field-size edge.

The same script includes invalid near-`|B|=|F|` controls; both were detected as
non-crossing because the saturation cap falls below the MCA gate.  This shows
the probe is sensitive to the separation hypothesis rather than vacuously
green.
