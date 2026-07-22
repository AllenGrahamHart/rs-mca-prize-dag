# L1 official Newton cofactor-window router

- **status:** PROVED
- **role:** transport the official low-degree received-word shells from
  locator-prefix Q to power-sum Q without small-characteristic cycles
- **consumer:** `l1_mixed_petal_amplification`

## Official arithmetic

Let the generated evaluation field be `K_0=F_(p^f)` and assume

```text
n=2^m>=2^13,       n | p^f-1,       p^f<2^256,
k/n in {1/2,1/4,1/8,1/16}.                           (NW1)
```

Let `ell_0` and the canonical threshold `a_0` be

```text
ell_0=sigma_0+1,       a_0=k+ell_0-1                 (NW2)
```

from `l1_official_reserve_tame_refinement_router`. Then

```text
p>=3583,       ell_0<=p-3174.                         (NW3)
```

## Newton window

Normalize a non-codeword received polynomial `U` modulo degree-below-`k`
codewords and put `h=deg U`. If

```text
e_0=h-a_0<=p-ell_0,                                   (NW4)
```

then every nonempty exact shell of size `a>=a_0` has fixed-cofactor locator
prefix depth

```text
d=min(a,h-k)<p.                                       (NW5)
```

For an agreement root set `A`, write

```text
L_A(Z)=Z^a+l_1 Z^(a-1)+...+l_a,
S_j(A)=sum_(x in A) x^j.
```

Newton identities are triangular and invertible through depth `d<p`.
Therefore

```text
(l_1,...,l_d) <-> (S_1(A),...,S_d(A))                 (NW6)
```

is a bijective change of target coordinates. Every fixed-cofactor cell from
`l1_exact_shell_fixed_cofactor_prefix_transport` is consequently a subset of
one prescribed depth-`d` power-sum prefix fiber. At scalar cofactor it is the
same exact top-shell Q fiber in either coordinate system.

By `(NW3)`, condition `(NW4)` holds uniformly for the 3,175 threshold-excess
layers

```text
0<=e_0<=3174.                                         (NW7)
```

If `p>=n-k`, it holds for every normalized received word of degree below
`n`, so every exact shell above the canonical threshold is Newton-safe.

## Scope

This theorem removes a coordinate and small-characteristic obstruction; it
does not prove prefix flatness. Positive cofactor cells still form the Pade
graph and require collective split-divisor transversality. The special F2
growing-order Myerson target is not promoted to a general power-sum Q theorem
by this router.
