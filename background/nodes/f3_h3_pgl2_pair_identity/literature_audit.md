# Literature scope audit for the constant-39 route

Date: 2026-07-12.

The paired identity asks for a simultaneous, pointwise bound on two PGL2
intersections at the same parameter. The following primary results are nearby
but do not supply the required finite constant.

1. Shkredov--Vyugin, *On additive shifts of multiplicative subgroups*
   (arXiv:1102.1172), proves power-law bounds for intersections of several
   additive shifts. The output grows with `|H|`; it does not imply a uniform
   bound of 39.
2. Shkredov, *On tripling constant of multiplicative subgroups*
   (arXiv:1504.04522), proves `E^*(H+x) << |H|^2 log |H|` for
   `|H|<sqrt(p)`. The logarithmic loss is already known to be the wrong
   endpoint for C36's printed constant.
3. Kim--Yip--Yoo, *Multiplicative structure of shifted multiplicative
   subgroups and its applications to Diophantine tuples*
   (arXiv:2309.09124, Theorem 1.1), gives a sharp Stepanov bound when a full
   Cartesian product `AB+lambda` lies in a multiplicative subgroup. A rich
   `P(t)` or `R(t)` fiber is the graph of a Mobius map: every first coordinate
   determines one second coordinate. It does not furnish a Cartesian product
   with both factors of size at least two, so Theorem 1.1 cannot be applied
   directly.
4. Kim--Yip--Yoo, *Shifted multiplicative subgroups are not ratio sets*
   (arXiv:2602.20919), rules out equality of an entire shifted subgroup with a
   ratio set. It does not bound the representation multiplicity of one
   parameter in `(1-H)/(1-H)` or `(1-H)(1-H)`.

Conclusion: no audited result above closes `I_inv+2I_aff<=39`. A successful
citation route needs a theorem on simultaneous rational-map intersections or
matching-graph fibers, not a marginal energy estimate or a product-set
containment theorem. This is a route cut, not evidence against the bound.

The subsequent 7,090-row bounded sweep is recorded in
`smallrow_sweep_result.md`. It found no counterexample, but its global
extremizer did not reduce to the previously observed single telescoping
pattern. The pointwise route remains background; the aggregate non-swap
moment is the preferred target.
