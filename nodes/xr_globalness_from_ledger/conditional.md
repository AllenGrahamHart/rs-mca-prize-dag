# xr_globalness_from_ledger conditional proof

## Predicate node

- `exchange_ledger_gen_t`

## Claim

Assuming the general post-strip top-core cap supplied by
`exchange_ledger_gen_t`, the post-strip family is global with link density at
most `L_tan / (n-j+1)` on every lower core.

## Proof

Assume every unpaid `(j-1)`-core has at most `L_tan` aligned completions
after the tangent strip. Let `A` be the post-strip family of aligned
`j`-supports.

Fix any `r`-core `C`, with `r <= j-1`, and let `A_C` be the link of `A`
above `C`. This is a family of `m = j-r` subsets inside a universe of size
`N = n-r`.

Count incidences

```text
(B,D),  B in A_C,  D subset B,  |D| = m-1.
```

Each `B` contributes exactly `m` such `D`. Each `D` corresponds to a
`(j-1)`-core `C union D`, and by the top-core cap it has at most `L_tan`
completions. Therefore

```text
|A_C| m <= L_tan binom(N, m-1).
```

Divide by the full slice size `binom(N,m)`. Since

```text
binom(N,m-1) / (m binom(N,m)) = 1 / (N-m+1),
```

and `N-m+1 = (n-r) - (j-r) + 1 = n-j+1`, the link density satisfies

```text
mu(A_C) <= L_tan / (n-j+1).
```

This holds uniformly for every `r <= j-1`. Thus the post-strip family is
global in the uniform-slice sense with polynomial-scale link parameter.
Composing with KLLM/global-hypercontractivity is handled by the downstream
`xr_kms_parameter_matching` node; this node proves the ledger-to-globalness
double count under the stated top-core predicate.
