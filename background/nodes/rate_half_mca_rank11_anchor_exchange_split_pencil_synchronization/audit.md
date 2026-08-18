# Audit

- **Anchor population:** exactly 5524 slopes selected from at least 5524
  first-owned slopes.
- **Secondary types:** `1<=t<=4`, with three fixed slopes from each.
- **Anchor packet size:** `s=32-3t`, hence `20<=s<=29`.
- **One-swap overlap:** `s-1>=19`, versus two locators needed.
- **Support consistency:** exact supports are fixed globally before packet
  selection; every packet cancels the same recovered core.
- **Pencil uniqueness:** two distinct monic disjoint-root locators are
  linearly independent and determine the two-dimensional subspace.
- **Output:** high complexity in one packet, or one pencil for all anchor
  locators.
- **Nonclaim:** neither output is paid here.
- **Verdict:** GREEN.
