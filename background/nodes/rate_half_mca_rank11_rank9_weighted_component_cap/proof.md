# Proof

Let `u` span the evaluation kernel on `B`. The owners agreeing with the
received pair on `B` form the affine plane from the nine-cell predecessor.
Let `J` be the coordinates where every plane owner agrees with the received
pair. Every owner core has the disjoint decomposition

```text
C_p=J disjoint_union P_p,
```

and the petals `P_p` are pairwise disjoint. In particular,

```text
sum_p |P_p|<=n'-|J|<=n'.                            (1)
```

Fix a component incidence `(gamma,T)` containing `B`. Since the lane has
rank ten on `T`, the two added coordinates raise the evaluation rank from
nine. They determine the unique owner point `p` of this component on the
record line. Both added coordinates lie in `C_p`, and at least one lies
outside `Z(u)`, hence in `P_p`.

For a fixed point `p`, the number of unordered two-coordinate extensions is
therefore at most

```text
|P_p|*|C_p minus B|<=|P_p|(m'-10).                  (2)
```

The last inequality uses support-wise pair noncontainment: any owner of an
assigned record has `|C_p|<m'`, so `|C_p minus B|<=m'-10`.

If `t_p` record lines pass through `p`, fixed-owner exception disjointness
gives

```text
t_p<=n'-m'+1=981105.                                (3)
```

Charge every component incidence to its unique point and combine
(1)--(3):

```text
W_B
 <=sum_p t_p |P_p|(m'-10)
 <=981105*(m'-10)*sum_p |P_p|
 <=981105*(m'-10)n'.
```

All inequalities count `(record,T)` incidences, so no extension weight is
discarded.
