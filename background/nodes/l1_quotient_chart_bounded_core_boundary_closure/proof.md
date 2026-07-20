# Proof - L1 quotient-chart bounded core-boundary closure

## 1. Encode every exact petal support

For each petal support `S_i`, record whether it is dense. Start from the
baseline that contains the whole petal in the dense case and none of it in
the sparse case. The symmetric difference between the exact support and this
baseline has size

```text
min(|S_i|,ell-|S_i|).
```

Across all petals its size is exactly `p`. Therefore every support pattern
with `p<=P_0` injects into:

- one dense/sparse bit for each of the `M` petals; and
- one exceptional point set of size at most `P_0`.

The number of support patterns is at most

```text
2^M sum_(e=0)^P_0 binom(n,e)
 <=2^M(P_0+1)n^P_0.                                  (1)
```

This encoding includes the canonical selected dense petals and all their
marks, so no further marked-support multiplier is needed.

## 2. Encode every exact defect locator

By the proved quotient-boundary router, the exact defect set is uniquely

```text
D=B_D disjoint_union disjoint_union_(a in A_full(D)) T_a,
```

where `B_D` contains no complete core fiber. With `beta(D)<=B_0`, the number
of possible boundaries is at most

```text
sum_(beta=0)^B_0 binom(n,beta)<=(B_0+1)n^B_0.         (2)
```

For each boundary, the full-fiber set is a subset of the `N` core fibers,
so there are at most `2^N` choices. This ambient count already bounds the
actual admissible quotient-core census; no flatness or periodic-owner theorem
is needed. Hence the number of defect locators is at most

```text
2^N(B_0+1)n^B_0.                                     (3)
```

## 3. Count numerators and reconstruct codewords

For fixed exact support, marks, and defect locator, split the strip into two
parts. If

```text
d+p<(m+1)ell,
```

the proved strict-window CRT theorem gives at most
`q^(2p)<=q^(2P_0)` numerators. On the complementary thin edge, the proved
`l1_marked_common_pencil_next_strip_boundary_fiber_bound` uses
`ell>2P_0` to force at least `m+1` dense petals and gives at most
`q^p<=q^(2P_0)` numerators. These cases exhaust `(BC3)`.

The canonical marked reduction reconstructs at most one listed codeword from
each numerator. Multiplying `(1)`, `(3)`, and the uniform numerator bound
gives the first inequality in `(BC4)`.

Finally `(BC1)--(BC2)` imply

```text
M+N<=n/ell<=log_2 n/c_0,
2^(M+N)<=n^(1/c_0),
q^(2P_0)<=n^(2 gamma P_0).
```

Substitution proves the second inequality in `(BC4)` and the claimed
uniform polynomial closure.
