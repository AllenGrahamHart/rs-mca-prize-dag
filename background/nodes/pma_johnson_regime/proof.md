# pma_johnson_regime proof

By `pma_aux_list_reduction`, for fixed `D` the extras inject into a list of
degree-`<=d` polynomials over the auxiliary evaluation set `T`, with agreement
`N`.

The classical Johnson/Guruswami-Sudan list-decoding criterion for
Reed-Solomon codes says that the list is polynomially bounded whenever the
agreement exceeds the Johnson threshold:

```text
N^2 > d |T|.
```

Here the auxiliary evaluation set is the union of `M` petals, each of size
`sigma + 1`, so

```text
|T| = M (sigma + 1).
```

Thus the Johnson condition is exactly

```text
N^2 > d M (sigma + 1),
```

or

```text
M < N^2 / (d (sigma + 1)).
```

With `N` in the stated `d+sigma` range, this is the recorded few-petal
condition. In that regime the per-`D` auxiliary list is polynomial, proving
the PMA stage-2 claim.
