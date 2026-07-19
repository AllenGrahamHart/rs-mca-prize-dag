# Proof - PMA sigma-one defect-three background payment

For `d=3` and `r=1`, the background quotient in
`pma_source_paving_bridge` has

```text
kappa=d-r+1=3,
kappa+sigma=4.
```

For each fixed missed-core set `D`, the pinned interpolation-owner charge is
therefore

```text
floor(binom(L,3)/binom(4,3))=floor(binom(L,3)/4).
```

There are `binom(k-1,3)` choices of `D`, proving the first formula in `(D31)`.

Using `binom(a,3)<a^3/6` and `kL<=n^2/4`,

```text
B_31
 < k^3 L^3 / 144
 = (kL)^3/144
 <= n^6/(64*144)
 = n^6/9216.
```

The low-defect theorem gives `B_low<n^5/1024`. Since `n>=2^13`,

```text
B_low < n^6/8388608.
```

Finally

```text
1/8192-1/9216=1/73728 > 1/8388608.
```

Adding the two strict bounds proves the combined `n^6/8192` statement.
