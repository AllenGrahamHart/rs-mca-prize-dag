# e22_residual_profile_generating_function

- **status:** PROVED
- **closure:** proof

## Statement

Fix dyadic scales `M_i<M_j` in a domain of size `n`. Put

```text
P = n/M_j,          q = M_j/M_i,
```

so there are `P` coarse `M_j`-parents, each containing `q` fine `M_i`-fibers.
Before imposing the lower-scale minimality conditions, canonical scale-`M_i`
data that are also raw-admissible at `M_j` are counted by the following
finite product formula.

Let

```text
G_q(u,z) = u + sum_{s=0}^{q-1} binom(q,s) z^s,
H_i(x)  = sum_{a=0}^{M_i-1} binom(M_i,a) x^a.
```

Here `u` marks a complete `M_j`-parent, and `z` marks a selected `M_i`-fiber
inside an incomplete `M_j`-parent. For fixed `c,r,b`, the number of
canonical scale-`M_i` data with:

- `c` complete coarse parents;
- `r` selected fine fibers in incomplete coarse parents; and
- scale-`M_i` tail size `b`;

is

```text
[u^c z^r] G_q(u,z)^P
*
[x^b] H_i(x)^(Pq - cq - r).
```

The raw scale-`M_j` admissible part is obtained by summing this expression
over

```text
0 <= b < M_i,
b + M_i*r < M_j.
```

## Falsifier

A canonical scale-`M_i` support raw-admissible at `M_j` whose selected-fiber
profile or tail choices are counted with the wrong coefficient.
