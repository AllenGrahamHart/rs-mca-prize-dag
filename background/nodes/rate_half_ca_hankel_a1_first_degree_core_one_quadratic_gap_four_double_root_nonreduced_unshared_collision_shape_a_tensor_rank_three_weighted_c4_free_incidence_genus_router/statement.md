# `A=1` shape-A rank-three weighted incidence/genus router

- **status:** PROVED
- **closure:** rank three reduces to a weighted `C_4`-free incidence graph
  with two exact plane-genus budgets
- **consumer:** `rate_half_band_crossing_location`

Retain an official Shape-A all-excess survivor of tensor separation rank
three. Put

```text
m=e-2,
n=(3e-7)/2,
T=3e,
R=3n+7=(9e-7)/2.                                  (WIG1)
```

The two coefficient maps are the normalizations of nondegenerate rational
plane curves `C_t,C_X` of degrees `m,n`. Group the `T` marked parameter
points by their common image on `C_t`, and give a resulting vertex `P`
weight

```text
s_P=#{delta in Gamma:a(delta)=P}.                  (WIG2)
```

Likewise group the `R` marked domain points by their common image on `C_X`
and give a resulting vertex `Q` weight

```text
l_Q=#{x in U_0:b(x)=Q}.                            (WIG3)
```

Join `P` and `Q` exactly when their coefficient pairing vanishes. The
resulting simple bipartite graph is `C_4`-free and satisfies

```text
sum_P s_P=T,                 sum_Q l_Q=R,
sum_(P~Q)s_P=m                 for every Q,         (WIG4)
sum_(Q~P)l_Q=n-w_P             for every P,
sum_P s_P w_P=2e-7.                                (WIG5)
```

Here `w_P` is a nonnegative integer. For a slope in the group `P`, it is
the sum of its union-excess and padded-heavy degree.

The singular-branch weights obey the exact plane-genus budgets

```text
sum_P binom(s_P,2)<=binom(m-1,2),
sum_Q binom(l_Q,2)<=binom(n-1,2).                  (WIG6)
```

Consequently

```text
s_P<=m-1,                  l_Q<=n-1,               (WIG7)
# {P}>=10,                 # {Q}>=10.              (WIG8)
```

Every domain vertex has at least two parameter neighbours. Parameter
vertices carrying total weight at least `e+7` have `w_P=0`; there are at
least two such zero-deficit vertices, and each has at least two domain
neighbours.

## Scope

This is an exact finite compression of the rank-three branch, not its
exclusion. A closing argument may now rule out the weighted `C_4`-free
graph, strengthen either genus budget using source singularities, or show
that the coefficient curves cannot realize its prescribed split-line
sections.
