# XR rank-two fundamental-circuit owner

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_trade_circuit_arity_segre_atlas`

Let `Lambda=(lambda_i)_(i in I)` be a rank-two uniform split-pencil trade.
Fix a total order on its active blocks and use the coefficient columns

```text
v_i=(c_i,d_i,gamma_i c_i,gamma_i d_i) in F^4
```

from the rank-two Segre atlas. Let `V:F^I -> F^4` send `alpha` to
`sum_i alpha_i v_i`, put `K=ker V`, and set `q=rank V`. Then

```text
3<=q<=4.                                                (FO1)
```

Let `B` be the lexicographically first `q`-element basis of the columns.
For every `e in I\B`, there is a unique vector `kappa^e in K` such that

```text
kappa^e_e=1,       supp(kappa^e) subset B union {e}.   (FO2)
```

Its support is the fundamental circuit of `e` over `B` and has exactly four
or five blocks. If `q=3`, every owner has four blocks and all coefficient
points lie on one nonconstant Mobius hyperplane section of the Segre quadric.
If `q=4`, an owner has four blocks exactly when one anchor coefficient in
`(FO2)` vanishes; otherwise it has five blocks.

The fundamental vectors form a basis of the complete scaling kernel:

```text
K=span{kappa^e:e in I\B},
alpha=sum_(e in I\B) alpha_e kappa^e       (alpha in K). (FO3)
```

In particular the all-one scaling vector of the original trade has the exact
star decomposition

```text
1_I=sum_(e in I\B) kappa^e.                         (FO4)
```

Thus at most four anchor blocks remain unowned, and every other block has one
canonical first-match four/five-block circuit inside its fixed rank-two
trade. This theorem does not identify the first Maxwell core containing a
block, deduplicate owners from different trades or cores, enumerate support
embeddings, or prove the aggregate `8n^3` slope payment.
