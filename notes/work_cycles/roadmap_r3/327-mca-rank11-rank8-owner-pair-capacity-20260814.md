# Cycle 327: MCA rank-11 rank-eight owner-pair capacity (2026-08-14)

Two PROVED nodes retain marked extension weight in the rank-eight
affine-owner target.

The structural node
`rate_half_mca_rank11_rank8_owner_pair_weight_cap` fixes an
evaluation-rank-eight nine-set `B` and writes `U=ker(ev_B)`, `dim U=2`.
For a full-rank extension `T=B union {x,y}`, evaluation on `{x,y}` is an
isomorphism on `U`. The pair `{x,y}` therefore determines at most one owner
point in the affine `U^2` flat. Since a fixed owner owns at most `981105`
records,

```text
W_B <=981105*C(n'-9,2)
```

in the weighted concentrator's exact `(record,T)` unit.

The capacity node
`rate_half_mca_rank11_rank8_weighted_capacity_cut` compares this cap with
the retained selector demand. At the final row not closed by this method,

```text
K'=37995:
demand =579135903691691071,
cap    =579154077989218305,
method deficit =18174297527234.
```

At the first closed row,

```text
K'=37996:
demand =579191514708840299,
cap    =579155144020629315,
gap    =36370688210984.
```

The identity

```text
C(n',9)C(n'-9,2)=55C(n',11)
```

reduces the unrounded demand/cap ratio to a constant times
`C(m',11)/C(n',11)`. All eleven factors increase with `K'`, so rank eight
is impossible uniformly for `37996<=K'<=1048576`.

Focused verification:

```text
RATE_HALF_MCA_RANK11_RANK8_OWNER_PAIR_WEIGHT_CAP_PASS
  pairs=590309033203 cap=579155144020629315 controls=6/6
RATE_HALF_MCA_RANK11_RANK8_OWNER_PAIR_WEIGHT_CAP_AUDIT_PASS
  pairs=590309033203 cap=579155144020629315 proof_pins=5/5
RATE_HALF_MCA_RANK11_RANK8_WEIGHTED_CAPACITY_CUT_PASS
  last_gap=18174297527234 first_gap=36370688210984 controls=7/7
RATE_HALF_MCA_RANK11_RANK8_WEIGHTED_CAPACITY_CUT_AUDIT_PASS
  last_gap=18174297527234 first_gap=36370688210984
  monotone_factors=11/11 proof_pins=3/3
```

No Modal computation was used; all calculations are constant-memory exact
integer or rational arithmetic.

```text
DAG delta:             +2 PROVED rank-eight capacity nodes,
                       +5 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     rank eight removed for K'=37996..1048576
remaining intervals:  K'=10..4598 rank eight only;
                       K'=4599..37995 rank eight plus kernel;
                       K'=37996..1048576 kernel only
delta-star movement:   none
compute:               constant-memory boundary arithmetic
next route action:     compress rank-eight owner-core overlap below the wall
                       and kernel cross-basis overlap above K'=4598
```
