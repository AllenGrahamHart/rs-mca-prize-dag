# Proof: FPC5 shifted-Johnson first-layout payment

Choose the first admissible maximal source layout in the canonical order
after all earlier global owners. By `l1_general_first_layout_domination`,
every selected codeword not among this layout's `M` planted anchors is
carried as a non-planted contributor in this same layout. Every later
first-carried member is one of those first `M` anchors. It is therefore
enough to count the selected non-planted profiles in the first layout and add
`M`.

For fixed `(M,t,d)`, the exact touched set is reconstructed from the
contributor. There are

```text
binom(M,t)
```

possible touched sets, and these cells are disjoint. For each touched set,
`l1_fpc5_shifted_johnson_grs_shell_cap` bounds the complete fixed cell by
`W L_m(q)`, retaining the exact required-background incidence factor.
Summing over touched sets and adding the planted anchors proves `(FL1)`.

Exact defect degree is also reconstructed from the contributor. Therefore
distinct degrees in `Delta` are disjoint, and summing their individual
bounds before adding the anchors once proves `(FL2)`. Equation `(FL3)` is the
prize-budget comparison. QED.
