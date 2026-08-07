# Proof

The parent reduction proves that every point of the source chart maps into
`V(I)` and that `V` and `K8` are units there. The original named-open chart
also inverts `s^2-4pvar`. Thus every admissible point lies in the
Rabinowitsch chart `zB=1`.

Exact Groebner elimination gives one degree-30 polynomial `h(s)` in the
Rabinowitsch ideal. Its irreducible factor degrees over `F_p0` are five
linear factors, two quartics, and one quintic. An element of `F_(p0^6)` has
minimal-polynomial degree dividing six. Therefore neither irreducible
quartic nor the irreducible quintic can vanish at its `s` coordinate.

It remains to test the five linear roots. At each root, specialize `I`,
reduce `x^(p0^6)-x` and `pvar^(p0^6)-pvar` modulo the exact fiber basis, and
adjoin the two remainders. Sequential reduction of the complete required
open-factor product reaches zero in all five resulting ideals. Hence every
degree-six rational point at a linear root lies on an excluded boundary.

The nonlinear factors and all linear factors are exhausted, so no
admissible `F_(p0^6)` point exists. QED.
