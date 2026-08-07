# Proof

The parent reduction is uniform in the four `R02` source assignments. It
proves that every point of each source chart maps into `V(I_F)` and that `V`
and `K8` are units there. The original named-open chart also inverts
`s^2-4pvar`. Thus every admissible point lies in the corresponding
Rabinowitsch chart.

Exact Groebner computation over `F_p0` gives saturated bases of sizes
`25,25,26,26`, all of dimension zero. In each finite quotient, repeated
squaring and reduction computes

```text
x^(p0^6)-x, s^(p0^6)-s, pvar^(p0^6)-pvar.
```

Adjoin these three exact remainders. Sequential reduction of `s`, the
degree-six leading factor, `K8`, and all transported named-open factors
reaches zero at factor 18 in every cell. Therefore every degree-six rational
point of each saturated core ideal lies on an excluded boundary, and no
complete named-open point survives.

There is a second certificate for `F04-R02`. Exact Groebner elimination gives
one degree-30 polynomial `h(s)` in its Rabinowitsch ideal. Its irreducible
factor degrees over `F_p0` are five linear factors, two quartics, and one
quintic. An element of `F_(p0^6)` has minimal-polynomial degree dividing six,
so neither an irreducible quartic nor an irreducible quintic can vanish at
its `s` coordinate.

At each of the five linear roots, specialize `I_F04`, reduce
`x^(p0^6)-x` and `pvar^(p0^6)-pvar` modulo the exact fiber basis, and adjoin
the two remainders. Sequential reduction of the complete required
open-factor product reaches zero in all five resulting ideals. Hence every
degree-six rational point at a linear root lies on an excluded boundary.

This independently exhausts `F04-R02` and cross-checks the direct quotient
certificate. The direct quotient argument proves all four `R02` cells. QED.
