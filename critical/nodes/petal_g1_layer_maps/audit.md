# G1 sufficiency audit

Date: 2026-07-12.

The previous clause (iii) bounded the number of charts charging each listed
codeword by `n^b1`. The primitive consumer then asserted a total bound
`n^(b1+b4)` from the per-chart K4 bound `n^b4`. This implication is invalid.

Indeed, take `N` pairwise disjoint nonempty charts, each containing one
different codeword and satisfying its K4 bound. Every codeword has chart
multiplicity one, but the total primitive count is `N`; no bound on `N`
follows from per-codeword multiplicity. First-match selection removes overlap
for staircase charging, but it also does not bound the number of selected
primitive charts.

The binding repair is a total atlas-size bound `|A_U|<=n^b1`, or an equally
strong direct aggregate primitive estimate. With the atlas-size form,
summing the per-chart K4 bound gives `n^(b1+b4)` exactly. The existing
union-injective distinct-label propositions are useful local inputs, but they
do not supply the arbitrary-word atlas or its total census.

No mathematical closure is claimed by this repair. G1 remains a critical red
leaf with a now-valid consumer interface.
