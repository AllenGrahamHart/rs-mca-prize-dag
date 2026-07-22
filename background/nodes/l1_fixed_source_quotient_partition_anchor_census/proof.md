# Proof - L1 fixed-source quotient-partition anchor census

## 1. One full petal determines the partition

Let `P` be monic of degree `ell` and suppose `T_i` is one of its complete
level fibers with value `a_i`. The polynomial `P-a_i` is monic of degree
`ell` and vanishes at every point of the `ell`-element set `T_i`. Its complete
factorization is therefore the monic locator of that set, proving `(FQ4)`.

If `P'` is another monic degree-`ell` quotient polynomial carrying the same
petal at value `a_i'`, then

```text
P-P'=a_i-a_i'.
```

Thus `P` and `P'` differ by an additive constant and have exactly the same
level-fiber partition. Assign each partition class to the least indexed
source petal it carries. Two classes with the same owner carry the same
petal, so the preceding identity makes them equal. This proves `(FQ3)`.

## 2. Count complete-fiber role keys

Distinct nonempty complete level fibers are disjoint and each has `ell`
points. Hence there are at most `L=floor(n/ell)` of them. Three independent
roles on those fibers give at most `3^L` structural keys for one partition.
Multiplication by `(FQ3)` proves `(FQ6)`.

The cutoff `(FQ7)` gives

```text
L<=log_2 n/c_0,
3^L<=n^(log_2(3)/c_0),
M_src<=log_2 n/c_0.
```

This proves `(FQ8)`. First-match deletion can only reduce the number of keys
or contributors, so any uniform polynomial per-key payment remains
polynomial after this aggregation.

## 3. L1 application

For every internal rechart already known to satisfy `(FQ2)`, the per-key
fixed-polarity payment from `l1_quotient_chart_bipolar_entropy_closure` may be
summed over at most `(FQ6)` structural keys. This removes the quotient-
polynomial supply axis in that anchored scope.

No implication from dense source-petal support to `(FQ2)` is used or proved.
The additive shift changes fiber labels but not the structural partition;
this census passes label-sensitive numerator data to the downstream whole-
strip CRT payment. `l1_fixed_source_anchored_triple_polarity_closure` performs
that payment at fixed triple polarity. Internal maps for which no whole source
petal is a complete fiber remain in the refinement or arbitrary-locator
branches.
