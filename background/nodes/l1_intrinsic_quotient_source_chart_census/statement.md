# L1 intrinsic quotient source-chart census

- **status:** PROVED
- **role:** remove cross-chart multiplicity inside intrinsic quotient scales
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Fix a received word `U` for `RS[D,k]` and one intrinsic quotient partition

```text
D=disjoint_union_(a in A) T_a,       |T_a|=ell,
L=|A|=n/ell.                                           (IC1)
```

Consider canonical maximal-sunflower source charts whose `(k-1)`-point core
is a union of complete fibers, whose full petals are complete fibers from the
same partition, and whose remaining fibers are unused/background. Charts are
identified by their core, petal family, and source member codewords, not by a
nonunique central-polynomial/label parametrization.

For one fixed core `C` and one fixed petal `T`, there is at most one source
member polynomial `Q_T` of degree below `k` satisfying

```text
Q_T(x)=U(x)       for every x in C union T.            (IC2)
```

Consequently the complete source chart is determined by assigning every
intrinsic fiber one of the three roles

```text
core,       petal,       unused/background.            (IC3)
```

The number of such charts at this scale is at most

```text
3^L.                                                    (IC4)
```

At the L1 cutoff `ell>=c_0 n/log_2 n`,

```text
3^L<=n^(log_2(3)/c_0).                                 (IC5)
```

There are at most `log_2 n+1` intrinsic dyadic scales. Therefore any uniform
per-chart bound `n^B` over this intrinsic quotient class aggregates, under a
canonical first-match order, to at most

```text
(log_2 n+1)n^(B+log_2(3)/c_0),                         (IC6)
```

which is polynomial. In particular, composing with
`l1_quotient_chart_bipolar_entropy_closure` proves a global polynomial bound
for every fixed `(p_pet,p_core)` box across all intrinsic quotient charts.

## Scope

The theorem does not cover partial core fibers, contributor-dependent or
non-intrinsic quotient polynomials, arbitrary petal locators, or source
charts not carried by one fixed quotient partition. It counts distinct chart
families rather than redundant parameterizations of the same source members.

