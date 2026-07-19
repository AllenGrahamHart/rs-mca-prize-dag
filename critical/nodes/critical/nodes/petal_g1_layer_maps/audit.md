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

## Weighted-premise weakening

The total-atlas repair was sufficient but stronger than the consumers need.
K4's proved bound for chart `chi` is the concrete quantity `m_chi+1`, not a
uniform abstract factor `n`. Thus the exact primitive union bound is

```text
sum_(chi in A_U) (m_chi+1).
```

At length `n>=256` and rate at least `1/16`, every chart satisfies
`m_chi+1<=n-k+2<=(121/128)n`. Hence the old `|A_U|<=n^5` premise implies the
new weighted bound `(121/128)n^6`. Conversely, the weighted bound can permit
more than `n^5` small charts, so it is a genuine weakening.

G3's proved first-match compiler uses only finite coverage and a total order.
The small-scale consumer uses only the weighted coefficient and quotient
closure. Therefore replacing the raw chart census by the weighted census
preserves every current consumer. G1 remains open on catalogue completion,
received-word uniformity, and the weighted payment itself.
