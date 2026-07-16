# Proof - PMA sigma-one paired-core abundance obstruction

Fix a core `C`. Restriction to `C` supplies `q^(k-1)` possible value vectors,
and each vector has a unique degree-at-most-`k-2` interpolant `Q_C`. Once
those core values are fixed, the map

```text
U|_(H\C) -> phi_C,       phi_C(x)=(U(x)-Q_C(x))/L_C(x),
```

is a bijection from `F^(H\C)` to itself because every `L_C(x)` is nonzero.

There are `2M+1` choices for the singleton point. The remaining points have

```text
(2M)!/(2^M M!)
```

partitions into `M` unordered pairs. After the singleton and pair blocks are
fixed, an injective assignment of field values to the `M+1` blocks has
`(q)_(M+1)` choices. Hence exactly

```text
q^(k-1) (2M+1)!/(2^M M!) (q)_(M+1)
```

received words make this fixed core paired. Summing over the
`binom(n,k-1)` cores proves `(PA1)`. Since `|F^H|=q^n` and
`n=(k-1)+(2M+1)`, division proves `(PA2)`.

For the displayed finite row, `65537` is prime and
`65537-1=65536`, so `F_65537^*` contains an order-`65536` cyclic domain. The
exact integer certificate multiplies the factors in `(PA2)` and compares its
numerator with `n^6 q^(2M+1)`, without logarithmic approximation. The strict
inequality forces at least one word above `n^6` by averaging.

For `(PA3)`, a paired core supplies `M` distinct planted anchors. By the
two-anchor part of paired-core normalization, no unordered pair of anchors
can occur in two distinct layouts. Double counting `(core, anchor pair)`
incidences proves the inequality.

Finally, field embeddings preserve interpolation, locators, quotient values,
and their equality pattern, so any finite-field witness persists in every
extension field. This proves only persistence of paired cores, not an entropy
transfer.
