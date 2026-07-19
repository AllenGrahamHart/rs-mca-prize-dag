# PMA sigma-one paired-core abundance obstruction

- **status:** PROVED
- **consumer:** `pma_wide_residual`, `petal_mixed_amplification`
- **role:** route cut for an unweighted source-layout census

## Statement

Use the setting of `pma_sigma_one_paired_core_normalization`. Let `q=|F|`,
let `n-k=2M`, and for a received word `U:H->F` write

```text
A(U)=#{(k-1)-cores C whose quotient map phi_C has signature (2,...,2,1)}.
```

Put

```text
P_M=(2M+1)!/(2^M M!),
(q)_(M+1)=q(q-1)...(q-M).
```

Then the exact first-moment identity is

```text
sum_(U in F^H) A(U)
 = binom(n,k-1) q^(k-1) P_M (q)_(M+1),                 (PA1)

E_U A(U)
 = binom(n,k-1) P_M (q)_(M+1)/q^(2M+1).               (PA2)
```

At the valid cyclic rate-half row

```text
q=65537,       n=65536,       k=32768,       M=16384,
```

the right side of `(PA2)` is strictly greater than `n^6`. Consequently some
received word over `F_65537` has more than `n^6` paired cores. The same word
and order-`65536` domain embed in every extension `F_(65537^e)`, preserving
all of its paired cores.

For `M>=2`, let `L_min(U)` be the set of planted anchors arising from paired
cores; each has exact agreement `k+1`. Two anchors determine at most one core,
so

```text
A(U) binom(M,2) <= binom(|L_min(U)|,2).                 (PA3)
```

Therefore no proof of the finite PMA inequality can bound all paired cores by
the primitive allowance `B_post<=n^6`. It must instead bound the weighted
Post-carrying sum `sum_C #E_C`, prove that almost all paired cores carry no
unowned Post codeword, replace the local summands by chart-free owners, or use
the proved first-layout domination theorem to avoid summing over cores. The
last route is the selected finite reduction.

## Scope

This is not a counterexample to `pma_wide_residual` or `imgfib`. A paired core
may carry only its planted anchors and have `E_C=empty`; `(PA1)` does not count
Post extras. The extension observation is not permission to use an ambient
extension field to pay a generated-field entropy reserve. No asymptotic lower
bound over an infinite family of official rows is claimed.
