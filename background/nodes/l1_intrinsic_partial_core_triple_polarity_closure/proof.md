# Proof - L1 intrinsic partial-core triple-polarity closure

## 1. Encode source charts

Orient each fiber according to whether the source core occupies more than
half of it, with ties sparse. Relative to the union of dense baseline fibers,
the symmetric-difference exception set has size exactly `p_layout`. Hence the
number of cores with `p_layout<=R_0` is at most

```text
2^L(R_0+1)n^R_0.                                      (1)
```

For a fixed core, choose any full fibers disjoint from it as source petals;
there are at most `2^L` choices. For fixed received word `U`, core `C`, and
petal `T`, the source member is unique: two degree-below-`k` candidates would
agree on `|C union T|=k-1+ell>=k` points. Therefore `(1)` times `2^L` bounds
the canonical source charts; source labels add no multiplier.

## 2. Encode contributors in one chart

Orient each selected petal support as dense or sparse. Its deviations from
the full/empty baseline total `p_petal`, so all exact petal-support patterns
with `p_petal<=P_0` number at most

```text
2^L(P_0+1)n^P_0.                                      (2)
```

For each fiber, regard `C intersect T_a` as one block and orient the defect
inside that block as dense or sparse, with ties sparse. The symmetric
difference from the corresponding full/empty core-slice baseline has size
exactly `p_defect`. Thus all exact defect sets with `p_defect<=B_0` number at
most

```text
2^L(B_0+1)n^B_0.                                      (3)
```

Empty core slices cause no ambiguity under the fixed tie convention.

For fixed source chart, exact support, marks, and defect locator, the strict
Forney-window CRT theorem gives at most `q^(2P_0)` numerators. Its thin
complement has at most `q^P_0` by the next-strip theorem because
`ell>2P_0`. Thus `q^(2P_0)` is valid throughout every strip, and every
numerator reconstructs at most one contributor.

Multiplying the four orientation factors from `(1)--(3)`, the three bounded
exception-set factors, and the numerator factor proves `(TP3)`.

## 3. Cutoff and scale aggregation

The cutoff gives

```text
L=n/ell<=log_2 n/c_0,
16^L=2^(4L)<=n^(4/c_0),
q^(2P_0)<=n^(2 gamma P_0).
```

There are at most `log_2 n+1` intrinsic dyadic scales. A canonical first-match
order makes their contributor classes disjoint. Substitution into `(TP3)`
and summation prove `(TP4)`.

