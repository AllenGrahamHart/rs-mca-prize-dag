### 2026-08-10 general-t FPC5 owner-free Cauchy divisor chart

The new PROVED node
`l1_fpc5_tpetal_owner_free_cauchy_divisor_chart` supplies the collective
object required by the ambient-owner route fence. Let `chi` be the CRT
multiplier equal to the petal label `c_i` modulo `L_i`. Every locator
reconstructs anchor-freely as

```text
B_G=rem_Lambda(chi G).
```

For a degree-`d` divisor `G` of the source-core locator, the condition
`deg B_G<=d` is exactly the `h-d-1` equations

```text
sum_(z in T) c(z) z^j G(z)/Lambda'(z)=0,
0<=j<=h-d-2.
```

Primitivity is the nonvanishing of the punctured zeroth moment at every
root of `G`, and every background zero is one explicit Cauchy-transform
equation. With `A=L_Core/G`, the same equations are reciprocal-divisor
moments in `A`. This is one owner-free simultaneous split-and-guard census;
no divisor owner is summed independently.

No critical status changes. The live bound is now precise: control this
weighted reciprocal-divisor census at the base-field-normalized scale and
then perform the chronology-valid source allocation.

The theorem is exported reciprocally in `przchojecki/rs-mca` PR #1151,
Section 8 of
`experimental/notes/l1/list_tpetal_joint_anchor_owner_v1.md`, pinned at
head `1699b933f21288ed0d72ff2b0f85b4b10277c999`. The PR was open, draft, and
mergeable at the pin; its source note points back to DAG commit
`a530e44835630165f92e01d91aa0b8e57f0ae0d7`.
