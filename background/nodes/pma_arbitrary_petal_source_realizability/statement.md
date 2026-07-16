# PMA arbitrary-petal maximal-source realizability

- **status:** PROVED
- **role:** source-only common-pencil route cut
- **consumer:** `petal_mixed_amplification`

## Statement

Let `L` be an `n`-point subset of a field `K`. Fix a core `C subset L` with
`|C|=k-1` and a partition

```text
L\C = B disjoint_union T_1 disjoint_union ... disjoint_union T_M,
|T_i|=ell,       |B|=b<ell.
```

Assume `K^*` contains `M` distinct scalars `c_1,...,c_M`, and put

```text
L_C(X)=product_(x in C)(X-x).
```

Define a received word `U:L->K` by

```text
U(x)=0                    for x in C union B,
U(x)=c_i L_C(x)           for x in T_i.
```

Then the Reed-Solomon codewords

```text
f_i(X)=c_i L_C(X),       deg f_i=k-1<k,
```

have exact agreement sets

```text
Agr(U,f_i)=C union T_i.
```

Thus they form an exact sunflower with arbitrary prescribed disjoint petals
and agreement `k-1+ell`. When `ell=sigma+1`, every `f_i` is listed at the PMA
threshold `k+sigma`. If

```text
M=floor((n-k+1)/ell),       b=(n-k+1)-M ell,
```

the source is maximal by petal packing.

In particular, maximal-source structure alone does not force the petal
locators into a common constant-shift pencil `P-a_i`. Such a conclusion needs
a contributor-dependent rechart theorem or additional first-match structure.

## Smooth-Domain Witness

Over `F_17`, take `L=F_17^*`, `n=16`, `k=8`, `ell=2`, core
`C={1,...,7}`, background `{16}`, and petals

```text
{8,9}, {10,11}, {12,13}, {14,15}.
```

Their monic quadratic locators have four different linear coefficients, so
they cannot be shifts `P-a_i` of one quadratic `P`. With values `1,2,3,4`,
the construction gives a maximal four-petal sunflower whose four codewords
each have exact agreement `9=k+1`.

## Scope

This theorem constructs the maximal source, not a surviving post-owner
`M=4,t=3` residual codeword. It refutes only a source-only common-pencil
inference. A theorem may still rechart each particular residual contributor
into a common pencil, and the arbitrary-locator residual may still admit a
direct polynomial count.
