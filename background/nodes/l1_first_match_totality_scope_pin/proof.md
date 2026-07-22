# Proof - L1 first-match totality scope pin

Because `A_x` is finite and nonempty and the chart keys are totally ordered,
`owner(x)=min A_x` exists and is unique. Hence every `x in I` belongs to
`C_owner(x)`, so the owner cells cover `I`.

If `x` belongs to both `C_chi` and `C_psi`, then the definition gives
`owner(x)=chi` and `owner(x)=psi`; therefore `chi=psi`. The cells are pairwise
disjoint. Finite additivity of cardinality now gives `(FT2)`. Applying
`|C_chi|<=U_chi` term by term proves `(FT3)`.

For a total key map `Phi:I->K`, take `A_x={Phi(x)}`. Then `C_z` is exactly the
fiber `Phi^(-1)(z)`, proving the total-key specialization.

This matches the theorem `prefixFibreAtlas_total` on upstream main at commit
`18cfc199`: its `totalFibreAtlas` uses the realized image of a total key map,
proves that the flattened fibers contain exactly the input witnesses, proves
duplicate-freeness, and proves that first-match leaves contain exactly those
witnesses. The upstream file explicitly keeps numerical payment separate.

For L1, take `I` to be the distinct codeword-image contributors remaining
after the already-paid strata and `A_x` to be their finite carrying
chart records. The argument assigns codewords, not raw support
explanations, so multiple explanations of one codeword are not charged more
than once. The identity `(FT2)` is exact but tautological as a count; obtaining
a polynomial upper bound still requires summing valid owner-cell payments.

The later `l1_general_first_layout_domination` theorem supplies more structure
for maximal sunflower source layouts: one first layout carries every
non-anchor, so no source-layout sum is needed. The generic argument here
continues to govern internal contributor-dependent rechart keys for which no
analogous universal-carriage theorem is available.
