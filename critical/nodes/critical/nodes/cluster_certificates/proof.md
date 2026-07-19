# cluster_certificates proof

First, let a cluster have swap diameter at most `d*`. Every pair inside the
cluster has swap distance at most `d*`, so `graded_collision_radius` certifies
every internal pair as collision-free. Such clusters are free cliques.

Second, consider two clusters with center difference `Delta`. Write any
cross-pair difference as

```text
Delta + eta = Delta (1 + Delta^(-1) eta),
```

where `eta` is the perturbation caused by moving from the centers to the two
chosen cluster elements. The everywhere-big hypothesis says that each
archimedean conjugate of `Delta` dominates the corresponding perturbation by
the printed spread/budget margin. Hence every conjugate of
`1 + Delta^(-1) eta` lies in the precomputed small disk used by the cluster
rule, and its quotient norm is below the remaining budget after the single
center norm check on `Delta`.

Thus one check that `p` does not divide the center norm, together with the
uniform quotient-norm bound, certifies all cross-pairs between the two
clusters.

Finally, if a certified difference is multiplied by a nonzero integer
`m < p`, then divisibility by `p` is unchanged: `p` cannot divide the integer
factor. These integer multiples are therefore self-certified freebies.

The three clauses give the stated cluster-certificate compression.
