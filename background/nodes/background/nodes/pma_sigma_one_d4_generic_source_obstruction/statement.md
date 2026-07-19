# PMA sigma-one generic defect-four source obstruction

- **status:** PROVED
- **role:** counterexample to the finite `n^6` PMA Post allocation
- **consumer:** `pma_wide_residual`, `petal_mixed_amplification`, `imgfib`

## Statement

There is a valid official rate-half row and a maximal `sigma=1` source word
for which more than `n^6` primitive, post-owner, non-planted source codewords
have exact defect four, no background agreement, exactly six singleton petal
agreements, and total agreement exactly `k+1`.

Use

```text
n=65536,                 k=n/2,
q=65537^2,               n | (q-1),
L=n-k,                   M=L/2,
s_n=floor(n/(32 log_2 n))=128.
```

There is a fixed `(k-1)`-core `C`, background point, pairing of the remaining
`L` points, and an injection of distinct nonzero labels `c_1,...,c_M` such
that the resulting maximal-sunflower word `U` has more than `n^6` distinct
codewords of the displayed type.

Every one of these codewords survives the three finite global owners:

1. its exact agreement set has odd size `k+1`, so it has trivial stabilizer;
2. the balanced core is farther than `s_n+6` from every eligible dyadic
   `k`-coset, so its agreement set is outside `QOWN_cosgrow`;
3. the source word equals `1` on one pair `{x,-x}` and therefore is not an
   odd lift `U(y)=(y-a)V(y^2)`.

Consequently the source-level primitive class `Top disjoint_union Post`
contains more than `n^6` members. Since the proved common ledger gives
`#Top<=N_top` and `B_post=n^6-N_top`, necessarily

```text
#Post>B_post.
```

Thus the finite assertion in `pma_wide_residual` is false as posed. This does
not by itself refute a larger polynomial `n^B` image-fiber theorem.

## Falsifier boundary

An error in the exact first-moment inequality, a hidden identification between
different exact defect sets, or membership of the constructed exact-support
class in one of the three global owners.
