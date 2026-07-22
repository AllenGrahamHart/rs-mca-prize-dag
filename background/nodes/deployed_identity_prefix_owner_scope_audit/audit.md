# Audit

The upstream compiler at commit `32a41660` still prints architecture ID
`GRANDE_FINALE_V3_EXACT_COMPLETION` while `agents.md` declares Grande Finale
v4. This metadata drift is recorded but does not affect the row arithmetic or
owner classification.

The exact source hashes are pinned in `deployed_rows.json`. The verifier does
not fetch upstream or recompute million-scale binomial coefficients. Those
arithmetic calculations are already independently replayed by
`v13_2_discrete_subfield_census_guard`; this audit checks the new ownership
and row-contract conclusion.

The phrase “attack below budget at `a+`” is never used as a safety claim. All
four upstream rows remain open.
