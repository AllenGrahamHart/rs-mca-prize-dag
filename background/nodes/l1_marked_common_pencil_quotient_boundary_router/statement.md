# L1 marked common-pencil quotient-boundary router

- **status:** PROVED
- **role:** separate quotient-core locator mass from primitive core boundary
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Work in a genuine quotient/coset common-pencil chart. Thus a monic
degree-`ell` polynomial `P` partitions the chart core as

```text
C=disjoint_union_(a in A) T_a,
T_a={x:P(x)=a},       L_(T_a)=P-a,       |T_a|=ell.       (QB1)
```

For an exact missed-core set `D subset C`, put

```text
A_full(D)={a in A:T_a subset D},
B_D=D\disjoint_union_(a in A_full(D)) T_a,
beta(D)=|B_D|.                                          (QB2)
```

Then the squarefree defect locator has the unique factorization

```text
F_D=L_(B_D) product_(a in A_full(D))(P-a).              (QB3)
```

The boundary `B_D` contains no complete `P`-fiber. If `d=|D|` and
`beta=beta(D)`, then

```text
j=|A_full(D)|=(d-beta)/ell.                             (QB4)
```

Fix one marked common-pencil support/mark chart with polarized entropy
`p<=P_0`. For a fixed boundary `B` of size `beta`, let `Q(B)` be the number
of full-fiber label sets `A_0` of size `(d-beta)/ell` for which

```text
D=B disjoint_union disjoint_union_(a in A_0) T_a
```

is an admissible squarefree defect locator in the selected Forney stratum.
Then the number of corresponding listed codewords is at most

```text
q^(2p) sum_(B subset C, |B|=beta, no full fiber) Q(B)
 <=q^(2P_0) binom(|C|,beta) max_B Q(B).                 (QB5)
```

The same inequality holds after summing over `0<=beta<=B_0`. Hence, for
fixed `P_0,B_0` and generated field `q=poly(n)`, bounded partial-fiber
boundary and numerator multiplicity cost only a polynomial factor. Any
super-polynomial common-pencil family in this box must therefore produce a
super-polynomial full-fiber quotient-core census `Q(B)` for some boundary
profile, or leave every fixed boundary box with `beta(D)->infinity`.

## Scope

This is a fixed-chart router. It does not prove that `Q(B)` is paid by the
source-level exact-periodic owner: an algebraically folded locator against an
arbitrary receiver need not have a periodic agreement set. It also does not
bound first-match multiplicity across source charts, treat a core not
partitioned by the same quotient pencil, or treat arbitrary petal locators.

