# proof: e22_two_class_exhaustion

We use the notation of
`nodes/worst_word_challenger_pricing/notes/e22_core.py`.

Let:

- `C` be the core, with `|C| = k - 1`;
- `P_i` be the petals, each of size `ell = sigma + 1`;
- `B_0` be the background, with `|B_0| < ell`;
- `L_C` be the core locator;
- the received word be zero on `C union B_0` and equal to `a_i L_C`
  on petal `P_i`, with `a_i != 0`.

The list threshold is

```text
s = k + sigma = k - 1 + ell.
```

We prove that no non-planted listed codeword can be classified as
`one_petal_nonplanted` or `background_or_core_only`.

## Root-count localization

Let `f` be a degree-`< k` listed codeword touching at most one petal. Let
`z` be the number of agreements on the zero-valued coordinates `C union B_0`,
and let `t` be the number of agreements on the one touched petal, with
`t = 0` in the background/core-only case. Since `f` is listed,

```text
z + t >= k - 1 + ell.
```

If `z >= k`, then `f` has at least `k` roots while `deg f < k`, so `f = 0`.
The zero polynomial agrees only on the zero-valued coordinates, whose number is

```text
|C| + |B_0| = k - 1 + |B_0| < k - 1 + ell = s,
```

so `f = 0` is not listed. Hence `z <= k - 1`. Also `t <= ell`, so the
threshold inequality forces

```text
z = k - 1,    t = ell.
```

Thus every possible third-class counterexample must vanish on exactly
`k - 1` zero-valued coordinates and agree on one whole petal.

## Ratio-flat obstruction

Let `Z` be the `k - 1` zero-valued coordinates on which `f` vanishes. Since
`f` is nonzero, `deg f < k`, and `f` has `k - 1` distinct roots,

```text
f = b L_Z
```

for some `b != 0`.

Assume the full touched petal is `P_i`. Agreement on `P_i` gives

```text
b L_Z(x) = a_i L_C(x)   for every x in P_i.
```

Write

```text
A = C \ Z,
B = Z \ C,
r = |A| = |B|.
```

Here `B subset B_0`, so `r <= |B_0| < ell`. Also `A` is contained in the core
and `B` is contained in the background, hence both are disjoint from the petal
`P_i`. Cancelling the common locator factor for `C cap Z`, the petal agreement
becomes

```text
b L_B(x) = a_i L_A(x)   for every x in P_i.
```

Equivalently, with `lambda = a_i / b`,

```text
H(x) := L_B(x) - lambda L_A(x)
```

vanishes on every point of `P_i`. But `deg H <= r < ell`, while `P_i` contains
`ell` distinct field points. Therefore `H` is the zero polynomial.

Since `L_A` and `L_B` are monic of degree `r`, `H = 0` forces
`lambda = 1` and `L_A = L_B`. Locators over distinct field points determine
their root sets, so `A = B`. The sets `A` and `B` lie respectively in the
disjoint core and background, hence this is possible only when

```text
r = 0.
```

Therefore `Z = C`. The petal agreement then gives `b = a_i`, so

```text
f = a_i L_C,
```

which is one of the planted codewords. This contradicts the assumption that
`f` is non-planted.

## Conclusion

No non-planted listed codeword can touch at most one petal. Every non-planted
listed codeword therefore touches at least two petals. By the classification
used in `e22_core.py`, such a word is either:

- `full_petal`, if every touched petal is full; or
- `mixed_petal`, otherwise.

Thus the planted sunflower receiver has no
`one_petal_nonplanted` or `background_or_core_only` third class. This proves
`e22_two_class_exhaustion`.
