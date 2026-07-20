# Proof - L1 quotient-chart bipolar entropy closure

## 1. Petal support encoding

Orient each petal as dense or sparse. Use the whole petal as the dense
baseline and the empty set as the sparse baseline. The symmetric difference
between the exact support and its baseline has size

```text
min(|S_i|,ell-|S_i|).
```

Consequently all petal supports with `p_pet<=P_0` inject into `M` orientation
bits and an exceptional point set of size at most `P_0`. Their number is at
most

```text
2^M(P_0+1)n^P_0.                                      (1)
```

## 2. Core defect encoding

Orient each core fiber according to whether `D` occupies more than half of
it. Use the whole fiber as the dense baseline and the empty set as the sparse
baseline; ties use the sparse orientation. The symmetric difference between
`D` and the union of dense core baselines has size exactly `p_core`.

Thus every exact defect set with `p_core<=B_0` injects into `N` orientation
bits and one exceptional core-point set of size at most `B_0`. The number of
defect locators is at most

```text
2^N(B_0+1)n^B_0.                                      (2)
```

This direct encoding includes both sparse partial fibers and almost-full
partial fibers. It does not infer periodicity of the resulting locator or
agreement set.

## 3. Numerators and the cutoff

For each fixed support pattern and defect locator, the strict-window marked
CRT theorem gives at most `q^(2p_pet)` numerators when
`d+p_pet<(m+1)ell`. On the complementary edge, the proved next-strip theorem
uses `ell>2P_0` and gives at most `q^p_pet`. Hence `q^(2P_0)` is a uniform
numerator bound in every degree strip. Each numerator reconstructs at most one
listed codeword in the fixed chart.

Multiplying `(1)`, `(2)`, and the numerator bound proves the first inequality
in `(BE4)`. Finally

```text
M+N<=n/ell<=log_2 n/c_0,
2^(M+N)<=n^(1/c_0),
q^(2P_0)<=n^(2 gamma P_0),
```

which proves the second inequality and the claimed bipolar escape condition.

