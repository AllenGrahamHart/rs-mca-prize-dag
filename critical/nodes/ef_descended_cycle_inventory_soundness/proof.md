# proof: ef_descended_cycle_inventory_soundness

Let `C` be the set of `B`-defined pole-free horizontal cycles produced after
full-orbit descent.

The inventory covers `C`, so every cycle appears in exactly one entry or in a
declared disjoint entry class. Each entry carries one of the accepted labels:
base-descended, proper-subfield/tower-confined, or noncontainment-degenerate.
The certificate attached to the entry verifies the asserted label.

Therefore every cycle in `C` is classified into one of the three cases named
by `ef_descended_cycle_classification_payload`. This is exactly the payload's
classification statement.
