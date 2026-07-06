# proof: v13_base_field_normalization_guard

Convention + guard, adopted as a ledger LAW: an entropy/prefix-floor cost entry is valid only when normalized over the field that generates the construction (B), or accompanied by an explicit wired transfer theorem to a larger field. Justification: the upstream v13 margins are 3.1-22.2 bits; a |F| vs |B| normalization error is larger than the margin and would fabricate a proof. This guard is checkable per ledger entry (grep-able convention).

Source: przchojecki/rs-mca towards-prize.md (2026-07-01) + cap25 v13 raw notes; imported as the v13 adapter layer 2026-07-06.
