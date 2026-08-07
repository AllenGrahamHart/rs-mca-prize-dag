# Proof

Fix one of the four cells and a point on its selected degree-12 branch.
Split first on `s`. The `s=0` leaf is empty by the literal specialization
theorem. On `s!=0`, split on the degree-6 leading factor `L6`; its zero leaf
is empty by the literal leading-curve theorem.

It remains to consider `s*L6!=0`. The `B0` leading coefficient has one
transported named-unit factor and one nonnamed factor `K10`. If `K10!=0`,
the generic-boundary theorem proves the complete chart empty. If `K10=0`,
the linear-source leading-drop theorem proves the complement empty. The
four cases are exhaustive, so no admissible point remains on the selected
degree-12 branch. QED.
