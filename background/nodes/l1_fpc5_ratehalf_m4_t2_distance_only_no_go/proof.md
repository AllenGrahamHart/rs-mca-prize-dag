# Proof: sharp FPC5 distance-only no-go fence

Consider the graph whose vertices are all `(2L+1)`-subsets of a fixed
`(5L+5)`-point core. Join two vertices when their intersection has size at
least `L`. If `D'` differs from a fixed `D` in exactly `i` deleted and `i`
inserted points, then

```text
|D intersect D'|=2L+1-i.
```

The closed forbidden neighborhood therefore has size at most

```text
V_L=sum_(i=0)^(L+1) binom(2L+1,i)binom(3L+4,i).      (1)
```

A greedy independent-set algorithm repeatedly selects one remaining vertex
and deletes its closed forbidden neighborhood. It selects at least

```text
binom(5L+5,2L+1)/V_L
```

vertices. Distinct selected sets are nonadjacent, so their intersections have
size at most `L-1`. This proves (NG2)--(NG3).

For the asymptotic estimate, the numerator has binary logarithm

```text
(5H(2/5)+o(1))L.
```

The summands in (1) increase through the relevant endpoint asymptotically,
and the polynomial number of summands is absorbed by `o(L)`. At `i=L+O(1)`,
their maximum logarithm is

```text
(2H(1/2)+3H(1/3)+o(1))L.
```

Subtracting gives (NG4); direct evaluation of binary entropy gives
`0.0998654701...>0`.

Finally the sharp background is the fixed full block `R=B` of size `L-1`.
For two selected defects,

```text
|(D union B) intersect (D' union B)|
 =|D intersect D'|+|B|
 <=2L-2=2s,
```

because core and background are disjoint. This proves (NG5) and the claimed
distance-only fence. QED.
