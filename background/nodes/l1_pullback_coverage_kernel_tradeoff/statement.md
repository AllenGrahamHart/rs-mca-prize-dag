# L1 pullback coverage/kernel tradeoff

- **status:** PROVED
- **role:** identify the sparse-coverage kernel with complete-fiber coverage
  deficit and couple it to partial agreement loss
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Exact kernel formula

Use the setup of `l1_general_pullback_interleaving_descent`. A monic
degree-`s` map has `b` complete domain-fiber labels, and

```text
k_j=max(0,ceil((k-j)/s)),
kappa=sum_(j=0)^(s-1) max(0,k_j-b).                   (CK1)
```

Then

```text
kappa=max(0,k-sb).                                     (CK2)
```

Thus the evaluation kernel is exactly the shortfall between the code
dimension and the number `sb` of domain points covered by complete fibers.

## Coupling to partial agreement

At source threshold `a_*=k+ell-1`, let `z(f)` be the partial loss from
`l1_partial_pullback_johnson_router`: agreement points not contained in a
fully agreed complete fiber. Every listed codeword satisfies

```text
z(f)>=max(0,k+ell-1-sb),                               (CK3)
kappa<=max(0,z(f)-ell+1).                              (CK4)
```

Consequently

```text
z(f)<=ell-1       ==> kappa=0,
z(f)<=ell-1+K     ==> kappa<=K.                       (CK5)
```

## L1 consequence

In the strict Johnson gate of `l1_partial_pullback_johnson_router`, the
separate fixed-`kappa` hypothesis is automatic on every box
`z<=Z<=ell-1+K`. Under a tame whole-petal anchor and `q<=n^gamma`, that box
costs at most

```text
n^(3+gamma K).                                         (CK6)
```

The pullback residual is therefore the nonpositive Johnson gate, wild or
unanchored map supply, or partial-loss excess `z-ell+1` escaping every fixed
cap. An unbounded sparse-coverage kernel is not an independent mechanism.
