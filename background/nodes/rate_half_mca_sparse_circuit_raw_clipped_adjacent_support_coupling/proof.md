# Proof

The parent fixed-union theorem gives, for each `0<=i<=d-2`,

```text
b_i C_(d,i)+a_i C_(d+1,i)<=A_i,
C_(d,i)<=L_i.
```

Its direct completion exposure gives the two sums in `(RCA4)` for the
remaining strata. Every support-`e` circuit contributes exactly
`s_e=C(m-e,11-e)` selected eleven-set incidences. Therefore the independent
incidence caps imply `(RCA1)`, and the actual integer stratum vector is a
feasible point of `(RCA3)--(RCA5)`. Relaxing integrality can only increase a
maximum, so the floor of the rational optimum in `(RCA6)` is a valid integer
upper bound.

It remains to justify the printed evaluation rule. Fix the total support-`d`
count. Uncoupled support-`d` mass consumes no support-`(d+1)` capacity and is
therefore assigned first. In coupled stratum `i`, increasing `x_i` by one
reduces the available `y_i` by `b_i/a_i`. Thus the exchange argument for
fractional knapsack assigns the remaining support-`d` mass in increasing
order of `b_i/a_i`. The resulting maximum support-`(d+1)` count is a
continuous piecewise-linear function. On each segment the weighted objective
is linear, hence its maximum occurs at a segment endpoint or where the raw
cap `Y` becomes active.

The reverse argument fixes support `d+1`. At full `x_i=L_i`, stratum `i`
has free support-`(d+1)` capacity `(A_i-b_iL_i)/a_i`. Beyond those free
capacities, one more unit of support `d+1` costs `a_i/b_i` units of support
`d`, so the reverse allocation order is increasing `a_i/b_i`. This describes
the same polytope and gives the same optimum.

Finally, pairwise replacement concerns only the two census terms displayed
in `(RCA6)`. Replacements on disjoint support pairs concern disjoint terms
and may be summed, exactly as in the parent theorem. Overlapping pairs are
not composed. QED.
