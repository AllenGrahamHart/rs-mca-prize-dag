# PMA sigma-one carried-layout Top/Post allowance

- **status:** PROVED
- **consumer:** `pma_wide_residual`, `petal_mixed_amplification`
- **role:** common finite consumer ledger for the primitive top and post bands

## Statement

Fix an official finite `sigma=1` row of dyadic length `n`, dimension `k`, and
received/source word `U`. Remove every codeword already assigned to a global
profile owner. Let `X_prim(U)` be the remaining primitive maximal-sunflower
source codewords represented by at least one admissible source layout.

Fix once and for all a total order on those source layouts and assign each
codeword to the first layout that carries it. Define

- `Top(U)` to contain the codewords whose first carried layout is full-petal
  and satisfies the proved floor band `d >= ell(m-2)`;
- `Post(U)` to be the complement in `X_prim(U)`.

Then

```text
X_prim(U) = Top(U) disjoint_union Post(U).                (TP-PART)
```

Put `t_ch=(n-k)/2` and

```text
S_3(k-1) = sum_(j=0)^3 binom(k-1,j).
```

At rate `1/2`, define

```text
N_top  = 2(t_ch+1)S_3(k-1),
B_post = n^6-N_top.
```

At rates `1/4`, `1/8`, and `1/16`, define `N_top=0` and `B_post=n^6`.
Uniformly over `U`,

```text
#Top(U) <= N_top,       0 <= B_post,       N_top+B_post=n^6.   (TP-CAP)
```

Consequently any source-uniform theorem proving

```text
#Post(U) <= B_post                                           (TP-OPEN)
```

implies `#X_prim(U)<=n^6` on the same first-match ledger.

The word "first" is load-bearing. Top is not defined by the existence of a
later top-band re-layout. The layout-existential interpretation is false and
is not used here.

## Scope

This theorem supplies the finite `sigma=1` allowance only. It does not prove
`(TP-OPEN)`, compose the known per-sunflower Post payments over source charts,
or supply the separate asymptotic-reserve allowance. Global profile owners
remain charged on their own lines before this partition.

The defect-four generic-source obstruction later proves `(TP-OPEN)` false.
The partition and exact allowance identity remain valid evidence for the
corrected polynomial/profile target.
