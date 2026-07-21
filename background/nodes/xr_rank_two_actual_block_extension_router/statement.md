# XR rank-two actual-block extension router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rank_two_dual_support_extension_factorization`,
  `xr_rank_two_received_pair_alternating_router`

Use one row of a uniform rank-two trade. Retain the notation

```text
X=S_i disjoint_union Z_i,       z_i=|Z_i|,
A_i=S_i disjoint_union T_i,     tau_i=|T_i|=h-d-1+z_i,
f_i=b+gamma_i q.                                      (AR1)
```

Every polynomial `J` of degree below `h` has the unique division

```text
J=Lambda_(T_i) U+V,
deg U<d+1-z_i,       deg V<tau_i.                    (AR2)
```

The corresponding block parity functional splits exactly as

```text
sum_(x in A_i) J(x)f_i(x)/Lambda'_(A_i)(x)
 =sum_(x in S_i) U(x)f_i(x)/Lambda'_(S_i)(x)
  +sum_(x in A_i) V(x)f_i(x)/Lambda'_(A_i)(x).       (AR3)
```

Thus the `h` block checks decompose into

```text
d+1-z_i       support-local checks,
tau_i         extension-sensitive checks.            (AR4)
```

The selected trade row has numerator `R_i Lambda_(T_i)` and occupies one
nonzero support-local check. The remaining ledger is therefore exactly

```text
(d-z_i)+tau_i=h-1.                                   (AR5)
```

There is also an exact realization and count. The support-local checks hold
if and only if there is a unique polynomial `w_i` of degree below `a` such
that

```text
w_i(x)=-f_i(x)                    for every x in S_i. (AR6)
```

In that case define the external zero set in the punctured ambient domain
`Omega` by

```text
E_i={x in Omega\S_i:f_i(x)+w_i(x)=0}.                (AR7)
```

Then `A_i=S_i union T_i` is an actual selected agreement block of size
`a+h` if and only if

```text
T_i subset E_i,       |T_i|=tau_i.                   (AR8)
```

Consequently the exact number of block extensions of the fixed
`(S_i,gamma_i)` support is

```text
C(|E_i|,tau_i),                                       (AR9)
```

interpreted as zero when `|E_i|<tau_i`.

This theorem closes per-row agreement-block extension counting. It does not
count possible supports `S_i`, enforce compatibility and pairwise-intersection
conditions among several extensions, choose the first Maxwell core, classify
higher trade rank or nonuniform cells, or pay the cross-core slope aggregate.
