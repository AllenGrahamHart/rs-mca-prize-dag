### 2026-08-10 general-t FPC5 joint-owner ambient MDS census

The new PROVED node
`l1_fpc5_tpetal_joint_owner_ambient_mds_census` turns the empirical owner
coalescence warning into an exact ambient route fence. On the roots of

```text
P_0=F L_(R_0),       p=deg P_0,
```

the determinant coordinate `H` is a length-`p`, dimension-`r+1`
Reed-Solomon evaluation word up to nonzero diagonal scaling. For any fixed
exact owner `Q` of degree `q`, the complete monic chart has the exact MDS
inclusion-exclusion count

```text
sum_(j=0)^(r-q) (-1)^j binom(p-q,j)
  (|mathbb F|^(r-q+1-j)-1).
```

In particular, every degree-`r` divisor of `P_0` occurs with exactly
`|mathbb F|-1` chart points, so the ambient top-owner census is

```text
binom(p,r)(|mathbb F|-1).
```

No critical status changes. These ambient points need not reconstruct split
primitive guarded locators. The exact conclusion is a no-go: owner
coordinates, MDS support counting, and unguarded linear algebra cannot
coalesce the residual. The live theorem must count simultaneous splitting
and guards across the full coordinate body.

The theorem is exported reciprocally in `przchojecki/rs-mca` PR #1151,
Section 7 of
`experimental/notes/l1/list_tpetal_joint_anchor_owner_v1.md`, pinned at
head `ca93321887b47b0f3323c24ecd4427df2c8dad47`. The PR was open, draft, and
mergeable at the pin; its source note points back to DAG commit
`058febd07e71302be851d2f13e62cc55a8e689ba`.
