# Audit

- **Anchor:** arbitrary triple-owner pair type with `r>=29`.
- **Secondary types:** `1<=t<=4`; each has at least three records.
- **Anchor packet sizes:** 29, 26, 23, or 20.
- **Minimum one-swap overlap:** 19 locators.
- **Core:** fixed supports make every packet cancel the same `J_3`.
- **Output:** one high-complexity packet or one rational pencil for all `r`
  locators of the selected type.
- **Ownership:** first-owned pair types remain disjoint; no cross-type pencil
  identity is asserted.
- **Verdict:** GREEN.
