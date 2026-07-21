# XR four-anchor quadric-centroid atlas

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_rank_two_fundamental_circuit_owner`

Use the coefficient-rank-four branch of a uniform rank-two trade. Order its
canonical anchor basis as `B=(1,2,3,4)`, write

```text
v_i=(c_i,d_i,gamma_i c_i,gamma_i d_i),
M_B=(v_1 v_2 v_3 v_4),
beta_e=M_B^(-1)v_e                     for e notin B. (QC1)
```

For `1<=i<j<=4`, put

```text
p_ij=(gamma_j-gamma_i)(c_i d_j-d_i c_j)
```

and define the anchor quadric

```text
Q_B(beta)=sum_(i<j) p_ij beta_i beta_j.              (QC2)
```

Every `p_ij` is nonzero, `Q_B` is a smooth split projective quadric, and
every non-anchor coordinate satisfies

```text
Q_B(beta_e)=0,
|supp(beta_e)| in {3,4}.                             (QC3)
```

The canonical owner of `e` is

```text
kappa^e_e=1,       kappa^e_i=-beta_(e,i) for i in B,
kappa^e_f=0        for f notin B union {e}.          (QC4)
```

Thus support three in `beta_e` is exactly a four-block owner, while support
four is exactly a five-block owner. The all-one trade equation is equivalent
to the exact affine centroid identity

```text
sum_(e notin B) beta_e=(-1,-1,-1,-1).                (QC5)
```

Conversely, fix four independent anchor Segre columns. Any finite list of
vectors `beta_e` satisfying `(QC3)` and `(QC5)` yields, through
`v_e=M_B beta_e`, a coefficient-rank-four trade provided the resulting
nonzero rank-one matrices lie in the finite-slope chart and have distinct
slopes and row classes. Hence `(QC1)--(QC5)` is a complete coefficient-level
atlas for the four-anchor branch.

This theorem does not count such quadric point configurations, prove that
their rows embed in selected agreement blocks, choose a first Maxwell core,
or pay the cross-core slope aggregate.
