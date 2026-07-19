# Budget-three multifiber Vandermonde exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:** `rate_half_list_budget_three_linear_grassmann_atlas`

Let `F` be a field, let `s>=1`, and take distinct elements
`r_1,...,r_t in F` with `t<=m`. For each `i`, let `C_i subset F` have size
`s` and contain `r_i^m`. Define

```text
B_i(X)=product_(c in C_i)(X^m-c),
A_i(X)=B_i(X)/(X-r_i).                                (MVE1)
```

Then

```text
A_1,...,A_t are linearly independent over F.          (MVE2)
```

This applies to direct quotient-periodic budget-three constructions. Suppose
a size-`d` omitted block is completed to a union of `s` full fibers of one
map `X^m`, where `d=sm`, and its locator `A_i` is obtained by deleting one
exceptional root `r_i` from the completed block.

1. In any 4-cycle chamber, the four locators have this form. If `m>=4`,
   `(MVE2)` contradicts the nondegenerate four-term relation required by the
   linear Grassmann atlas.
2. In either path-plus-singleton chamber, the three locators in the tight
   triangle have this form. If `m>=3`, `(MVE2)` contradicts the required
   three-term relation.

At the prize-max value `d=2^39`, every power-of-two quotient-fiber size
`m>=4` is therefore excluded from all six cycle/path chambers, regardless of
how many equal fibers are grouped into each completed block. A surviving
construction must use fiber size `1` or `2`, different quotient maps between
blocks, incomplete/mixed fibers, or a primitive non-quotient locator. The
theorem does not exclude those residuals or any of the other seven bounded
chambers.
