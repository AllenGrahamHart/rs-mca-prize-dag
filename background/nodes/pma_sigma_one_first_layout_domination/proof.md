# Proof - PMA sigma-one first-layout domination

Fix one paired core `C`. Its quotient fibers recover a maximal sunflower word
and its planted anchor set `Anch(C)`. Lemma 2 of
`l1_core_defect_reduction`, consumed through `pma_aux_list_reduction`, is
universal in the listed codeword: every listed `P` not in `Anch(C)` has a
unique core-defect polynomial `W_P` and is a non-planted extra carried by
this layout. Deleting global owners only takes a subset and does not alter
this implication.

Assume paired cores exist and let `C_1` be first. If `P` belongs to `E_Cj`
for some `j>=2`, then `P` was not carried by `C_1`. Universal non-planted
carriage forces `P` to lie in `Anch(C_1)`. The first-match sets `E_Cj` are
disjoint, while `Anch(C_1)` has exactly `M` members. Therefore

```text
disjoint_union_(j>=2) E_Cj subset Anch(C_1)
```

and `(FL1)` follows from the exact first-match identity
`Post(U)=disjoint_union_j E_Cj`. If there is no paired core, there is no
maximal source layout representing a member of this PMA branch, so Post is
empty by its source-layout definition.

Now split the non-planted extras in the first layout into the three paid
source classes and their complement `R_first`. The proved local theorems give

```text
#(paid extras in C_1) <= B_low+B_31+B_30^full=B_paid.
```

Combining this with `(FL1)` proves `(FL2)`. Prior payment arithmetic gives
`B_paid<n^6/1024`. Also `M<=n/2`, and every official row has `n>=2^13`, so

```text
M <= n/2 < n^6/(1023*1024).
```

Adding the inequalities proves `(FL3)`. Finally, substituting `(FL2)` into
the already proved target `#Post<=B_post` shows that `(FL4)` is sufficient.
No estimate of `R_first` is used.
