# sketch: e22_two_class_exhaustion

This is not a proof of the node. It records the first structural reduction of
the no-third-class problem.

## Setup

Use the notation of `e22_core.py`.

- `C` is the core, `|C| = k - 1`.
- Petals `P_i` have size `ell = sigma + 1`.
- The received word is zero on `C` and on the background, and equals
  `a_i L_C(x)` on petal `P_i`.
- A listed codeword is a polynomial `f` of degree `< k` agreeing with the
  received word on at least

```text
s = k + sigma = k - 1 + ell
```

coordinates.

## Lemma 1: root-count localization

Let `f` be a nonzero listed codeword that touches at most one petal. Let `z`
be its number of agreements on zero-valued coordinates (`C` plus background),
and let `t` be its number of agreements on the one touched petal. Then

```text
z + t >= k - 1 + ell.
```

Since `deg f < k`, if `z >= k` then `f` has at least `k` roots and hence
`f = 0`. But the zero polynomial cannot reach the threshold: it agrees on at
most `|C| + |background|`, and the background size is strictly less than
`ell`, so this is at most `k - 1 + (ell - 1) < s`.

Therefore `z <= k - 1`, and the threshold inequality forces

```text
z = k - 1,   t = ell.
```

Thus every third-class counterexample is already extremely rigid: it has
exactly `k-1` zero agreements and agrees on one full petal.

## Lemma 2: ratio-flat reformulation

Let `Z` be the `k-1` zero-agreement coordinates of such an `f`. Then

```text
f = b L_Z
```

for some nonzero scalar `b`. If the full touched petal is `P_i`, agreement on
that petal is equivalent to

```text
b L_Z(x) = a_i L_C(x)  for every x in P_i.
```

Equivalently the rational function `L_Z / L_C` is constant on `P_i`.

The no-third-class statement therefore reduces to:

> There is no `Z != C` of size `k-1`, drawn from zero-valued coordinates in
> the planted layout, for which `L_Z / L_C` is constant on a full petal.

If `Z = C`, the word is the planted codeword for that petal.

## Remaining subclaim

`E22-RF`: the ratio-flat condition above has no non-core solutions in the
low-slack cells relevant to E22, or every solution is quotient-equivalent to a
declared mixed/full-petal staircase class rather than a third class.

This is the smallest current algebraic target for a direct proof of
`e22_two_class_exhaustion`.
