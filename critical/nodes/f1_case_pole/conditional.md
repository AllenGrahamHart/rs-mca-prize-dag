# conditional: f1_case_pole

One-predicate proof packet (weakening audit 2026-07-06):
- f1_pole_list_threshold_location (CONDITIONAL): carries the imported
  extension-pole/list bridge and locates the list-side threshold the import
  consumes (`N(L)` crosses the MCA gate exactly when the base list crosses
  `L ~ 2^128`).

Evidence/support edge:

- ext_import (PROVED)

Implication: every pole-type F-valued bad slope above the reserve is priced by the
imported list term at the located threshold. Consumed by ext_lift / f1_classification.

WEAKENING 2026-07-06: the direct edge `ext_import -> f1_case_pole` is evidence
rather than a logical requirement.  The transitive dependency remains through
`f1_pole_list_threshold_location`, whose statement and proof consume the
imported bridge.

Stress evidence: `experiments/amber_stress/f1_pole_threshold_probe.py` tests
the exact extension-pole floor arithmetic consumed by
`f1_pole_list_threshold_location`.  On `92` official-like non-generating rows
it found no premature or delayed threshold failure; two invalid near-`|B|=|F|`
controls were correctly rejected as non-crossing.
