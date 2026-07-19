# Proof

At a selected coordinate of degree three, the pair `{i,j}` is present exactly
when the omitted label is one of the complementary labels `k,l`. A degree-two
coordinate contributes to pair `ij` exactly when its label is `ij`, and every
degree-four coordinate contributes to every pair. Therefore

```text
S_i intersect S_j = F disjoint_union T_k disjoint_union T_l disjoint_union E_ij
```

and its locator is `J A_k A_l e_ij`.

The nonzero polynomial `g_ij=f_j-f_i` has degree at most `2d-1` and vanishes
on this intersection. Polynomial division gives `(SP1)`, with

```text
deg q_ij <= (2d-1)-deg(J A_k A_l e_ij)=delta_ij.
```

For distinct `i,j,k`, let `l` be the fourth label. The polynomial cocycle
identity is

```text
g_ij+g_jk=g_ik.
```

Substituting `(SP1)` gives a common nonzero factor `J A_l`. Cancelling it in
the polynomial ring proves `(SP2)`.

For the table, put `t_i=|T_i|`, `s_i=|S intersect S_i|`, and
`p_i=sum_(j!=i)p_ij`. The individual agreement equations from the parent
reduction give

```text
t_i = T+s_i+p_i+n_4-(3d-1),
T=4d-n_1-n_2-n_4.                                   (1)
```

The pair intersections and deficits are

```text
|S_i intersect S_j|=T-t_i-t_j+p_ij+n_4,
delta_ij=2d-1-|S_i intersect S_j|.                  (2)
```

Substitution of the six canonical singleton/edge representatives from the
parent theorem into `(1)--(2)` gives exactly the printed rows. Since
`deg e_ij=p_ij`, equation `(SP1)` gives
`deg b_ij<=p_ij+delta_ij`, including the three and only three possible
quadratic slots shown in the table.

The coordinate classes `S,F,T_0,...,T_3,E_01,...,E_23` form a disjoint
partition of `D`, proving `(SP3)`. Finally each pair locator is
`J A_k A_l e_ij`. Across the product over six pairs, every `A_i` appears
three times, `J` appears six times, and every `e_ij` appears once. Cubing
`(SP3)` and cancelling the corresponding factors proves `(SP4)`. QED.
