# Mersenne checkpoint analogue result

- **status:** COMPLETE evidence; no theorem or official-row certificate
- **script:** `l1_mersenne_checkpoint_analog_modal.py`
- **Modal apps:** initial census `ap-X9B0VIv80tdRxDSfYnkG9o`; embedded-family
  classification `ap-mLyev4aS4qOOhZhKqcpK5i`
- **row:** `(n,p,m)=(32,7,4)` over `F_(7^4)`
- **coverage:** all `binom(32,7)=3,365,856` seven-subsets of the order-32
  subgroup

## Exact output

```text
COMPLETE records=3365856/3365856 primitive=12 zeta=936
groups_ge_2=16 max_h=2 max_depth_at_max=8 embedded_m2_h2=16
group_size_histogram 1:3365824 2:16
max_group_masks 0x105445 0x54450010
MODAL_EXIT=0
```

Two subsets were grouped exactly when their monic degree-seven locators had
the same coefficients in degrees one through six. Distinct locators in one
group differ by a nonzero constant, so their root sets are automatically
disjoint and the group size is the exact split-value degree `h`. The worker
also checked disjointness directly.

The complete analogue contains 16 pencils with `h=2`, all with maximum
first-checkpoint depth eight, and no pencil with `h>=3`. All 16 two-fiber
pencils lie in one order-16 coset and omit an antipodal pair, exactly matching
the proved `m=2` construction embedded in the order-32 domain. Thus a blanket
emptiness conjecture is false even in the first genuine Mersenne analogue,
but the proposed `m=4,h=3` exclusion survives this exhaustive test. This is
only route evidence: `p=7` is below the official characteristic floor and no
official row or uniform theorem follows from the census.
