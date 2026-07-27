# E1 N=256 square-mass-16 E=34 three-profile reduction

- **status:** PROVED
- **closure:** proof plus two complete finite censuses

Let `F` have folded profile `(3,4,0)` in the `N=256,s=5` band and suppose
its positive-half autocorrelation variance is `V=68`. Put

```text
E=V/2=34,
L=sum_(d=1)^63 |A_d|,
n_j=#{d: |A_d|=j}.
```

Then every pair-feasible collision satisfies

```text
(n_1,...,n_6) in {
  (6,7,0,0,0,0),
  (9,4,1,0,0,0),
  (12,1,2,0,0,0)
}.                                                       (1)
```

In particular every residual profile has `L=20`.

The exact slack recurrence gives `L<=20` and 24 integer magnitude profiles.
Eighteen have the abstract nested-layer cap at most 1940. Of the six larger
profiles, complete nested quotient censuses give

```text
(5,5,1):       1880 / 1828,
(14,1,0,1):    1922 / 1922
```

in the odd order-128 / divided order-64 chambers. For `(2,8)`, the refined
order-64 and order-128 outside-inner-`4Z` caps are both 1942, while an exact
7,927,920-support census gives maximum 1536 in the inner-`4Z` chamber.
The remaining outer-`4Z` case has small-field norm below `2^250`.

Thus every profile outside (1) has `M_3<=1942<1947`. The exact rational
cubic-Hermite certificate at contacts 14 and 57 puts its collision norm below
`2^250`, contradicting pair feasibility.

This theorem does not exclude the three profiles in (1), any lower positive
variance, or profile `(4,2,0)`.
