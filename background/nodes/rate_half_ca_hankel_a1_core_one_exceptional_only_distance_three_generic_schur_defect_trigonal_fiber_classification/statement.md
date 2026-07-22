# `A=1` distance-three generic Schur-defect trigonal-fiber classification

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quadratic_locator_rank_gate`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_locator_mobius_dichotomy`

Let `e>=3`. Retain pairwise coprime monic quadratic pair locators `D_i`
that are also coprime to the monic cubic `B`, and assume the generic branch

```text
dim span{D_1,...,D_e}=3.                              (GSDFC1)
```

Put

```text
A=product_i D_i,       U_0=A,       U_i=B A/D_i,
V=span{U_0,...,U_e}.                                  (GSDFC2)
```

Define the linear solution space

```text
K={(R,y_1,...,y_e):deg R<=2 and D_i | R-y_iB for all i}.
                                                               (GSDFC3)
```

Then the exact Schur-defect identity is

```text
(3e+1)-dim(VV)=dim K.                                (GSDFC4)
```

Moreover,

```text
dim K<=1.                                            (GSDFC4a)
```

Consequently exactly one of the following holds.

1. **Saturated generic branch:** `dim(VV)=3e+1` and `K=0`.
2. **Trigonal-fiber branch:** `dim(VV)=3e` and `K` is one-dimensional. Its
   unique projective nonzero solution recovers `R`. For every `i` with
   `y_i!=0`, the two roots of `D_i` lie in the level set

   ```text
   B/R=1/y_i.                                         (GSDFC5)
   ```

   The nonzero `y_i` are pairwise distinct. At most one `y_i` is zero, in
   which case `D_i | R`.

On the external-design row set, evaluation is injective on `VV`, so
`dim(VV)` is exactly the rank of the quadratic locator matrix from the first
dependency. Thus every generic rank drop is detected and its rational map
`B/R` is reconstructed by one linear system. This theorem classifies the
drop; it does not exclude either resulting branch.
