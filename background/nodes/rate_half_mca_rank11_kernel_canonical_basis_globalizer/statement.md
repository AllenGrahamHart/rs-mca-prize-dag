# Rank-eleven kernel canonical-basis globalizer

- **status:** PROVED
- **scope:** the rank-deficient lane of the dense-locator component census
- **units:** `(record, eleven-subset)` incidences

Let `W=V'` be the ten-dimensional residual correction space and let `T` be
an eleven-subset with

```text
1 <= r=rank(ev_T:W->F^T) <= 9,       d=10-r.
```

Choose one canonical rank basis `B subset T`, `|B|=r`, and put
`H=ker(ev_B)`. All records assigned to this same `B` lie, after one common
affine codeword-pair translation and cancellation of `B`, in one
`d`-dimensional explanation space. Same-support pair noncontainment and all
exact supports are preserved.

The `d+1` coordinates of `T minus B` are common zeros of `H`. Generalized
MDS gives at most `K'-d` common zeros in total and therefore at most

```text
K'-d-r=K'-10
```

outside `B`. Consequently one record contributes at most

```text
C(K'-10,d+1)
```

rank-`r` eleven-subsets having canonical basis `B`. The number of records
over `B` is at most the support-local rank-`d` cap `M_d`; for `d=9` the
proved margin/interleaving cap is used.

Rank zero cannot occur because the residual correction space has empty
global common zero set. This is a rank-stratified aggregate interface, not
a payment of the complete kernel lane.

## Falsifier

A rank-zero evaluation tuple; two records over one basis requiring
different quotient solutions; loss of support or pair noncontainment under
basis cancellation; more than `K'-10` additional common zeros; or more than
`M_d C(K'-10,d+1)` incidences over one canonical basis.
