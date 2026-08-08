# Proof

The product-rank-drop complete exclusion proves that no deployed packet can
lie on the rank-at-most-four product branch.

On product rank five, the parallel-`DE` assembly pays
`{0,1,2} x {0,...,14}`, the xi3/xi4 assembly pays
`{3,4} x {0,...,14}`, and the endpoint theorem pays
`{5,6} x {0,...,14}`. Their missing-role sets are pairwise disjoint and cover
`{0,...,6}`. Hence the three parents form a disjoint cover of all
`7*15=105` principal labels.

Each label theorem has the same fixed role cell and covers all four
source-sign pairs and all four target lanes. Therefore the principal census
is `105*4*4=1680` empty systems, split as `720+480+480`. Together with the
rank-drop exclusion, this exhausts the deployed role-cell-4 route. QED.
