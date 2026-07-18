# XR low-core `u=1` augmented-paving scope fence

- **status:** see `dag.json` (single source of truth)
- **consumer:** `xr_lowcore_spread_heart`
- **dependencies:** `xr_rank_five_extension_list_reduction`,
  `xr_rank_five_u1_split_locator_nonbasis_bound`

In the P-B RowC rank-five branch with `(u,v)=(1,0)`, the normalized
four-dimensional kernel is only known to have the form

```text
W subset F[X]_{<=4},       dim W=4,
```

with no common evaluation root.  These hypotheses do not imply that `W` is
MDS: for any four-set `T` of evaluation points,

```text
W=span{1,X,X^2,L_T}
```

is source-compatible and has `rank(W|T)=3`.  Consequently the all-pair
weighted-RS paving-basis theorem cannot be applied to the generic `u=1`
branch through its printed `GRS_4` kernel hypothesis.

Even on the special MDS branch, grant the strongest possible ambient
specialization of that theorem: direction distance equal to the chart
redundancy and all ambient five-sets available.  At the three RowC rows its
resulting ceilings are

```text
rate 1/4:  floor(C(773,5)/C(10,5)) =   9,009,204,611,
rate 1/8:  floor(C(901,5)/C(10,5)) =  19,418,424,240,
rate 1/16: floor(C(965,5)/C( 8,5)) = 123,242,307,467.
```

All exceed `B=8*1024^3=8,589,934,592`.  On the closest rate-quarter row,
an augmented-basis argument with local charge `C(10,5)=252` can pay `B`
only if its actual numerator satisfies

```text
beta_5(A) <= 252(B+1)-1 = 2,164,663,517,435.            (AP1)
```

Thus it must prove at least

```text
C(773,5)-beta_5(A) >= 105,656,044,614,                 (AP2)
```

a `4.653796...%` source-coupled saving from the ambient numerator.  The
ambient theorem and the existing four-row nonbasis bound provide no such
statement.  This is a route-scope and arithmetic fence, not a proof that a
source-specific augmented-matroid or coherent-color argument cannot pay the
branch.  It does not promote P-B.
