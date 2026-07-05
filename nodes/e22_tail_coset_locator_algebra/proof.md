# proof: e22_tail_coset_locator_algebra

Let `D` be the multiplicative subgroup domain and let `M | n`. The quotient
map

```text
pi_M: x -> x^M
```

has fibers of size `M` on `D`. For a selected quotient value `z`, the full
fiber is exactly the set of roots in `D` satisfying

```text
X^M - z = 0.
```

Let `B` be a disjoint tail with `|B| = b < M`, and let
`H = {z_1, ..., z_h}` be the selected quotient values. The locator of the
union of `B` and the full fibers over `H` is therefore

```text
L_B(X) prod_{z in H} (X^M - z).
```

Writing

```text
G(Y) = prod_{z in H} (Y - z)
```

gives the claimed locator form

```text
L_B(X) G(X^M).
```

It remains to check the top-coefficient statement. Since `G` is monic of
degree `h`,

```text
G(X^M) = X^{hM} + g_1 X^{(h-1)M} + ...
```

and `L_B` has degree `b < M`. Thus the leading block of
`L_B(X)G(X^M)` is

```text
X^{hM} L_B(X),
```

while every term involving `g_1, g_2, ...` has degree at most

```text
(h-1)M + b = hM + b - M.
```

There is an `M`-coefficient gap below the leading block. If `M > t`, none of
those lower quotient terms can contribute to the top `t` subleading
coefficients. Those coefficients are exactly the corresponding coefficients
of `L_B`, shifted by the leading power `X^{hM}`, and hence depend only on
`B` and on the degree `h`, not on the selected quotient values in `H`.

This proves both the locator identity and the `M > t` coefficient invariance.
