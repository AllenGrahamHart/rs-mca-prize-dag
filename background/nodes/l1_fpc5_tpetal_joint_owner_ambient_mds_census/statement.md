# Joint-owner ambient MDS census

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Fix one nonempty full-petal cell and one exact primitive squarefree anchor.
Use

```text
P_0=F L_(R_0),       p=deg P_0=d+|R_0|,
r=2d-deg Lambda,     Q_f=|mathbb F|.                 (MC1)
```

The saturated-cell inequality `deg Lambda>d` gives `r<d<=p`.

The complete monic pair chart is in affine bijection with

```text
H in mathbb F[X]_(<=r).                               (MC2)
```

For `H!=0`, its exact joint owner is `gcd(H,P_0)`. Equivalently, after
nonzero diagonal rescaling on the `p` roots of `P_0`, the vector of joint
anchor defect/background failure values is the evaluation vector of `H`.
Thus the complete unguarded joint-owner chart has exactly the support
strata of the length-`p`, dimension-`r+1` Reed-Solomon code.

Fix a monic divisor `Q|P_0` of degree `q<=r`, and put

```text
s=r-q,       m=p-q.
```

The number of nonzero chart points with exact owner `Q` is

```text
N_Q(m,s)
 =sum_(j=0)^s (-1)^j binom(m,j)(Q_f^(s+1-j)-1).      (MC3)
```

Consequently the number whose exact owner has degree `q` is

```text
binom(p,q) N_Q(p-q,r-q).                              (MC4)
```

At top ownership `q=r`,

```text
N_Q=Q_f-1,                                            (MC5)
```

for every degree-`r` divisor `Q|P_0`. Hence the complete top-owner ambient
chart has exactly

```text
binom(p,r)(Q_f-1)                                     (MC6)
```

non-anchor points and realizes every possible top owner.

## Scope

This is an exact census of the complete monic pair chart before requiring
the reconstructed locator to split on the source core, primitivity, exact
background agreement, or first ownership. It proves that owner-coordinate
dimension and linear algebra alone cannot coalesce the owner strata: all
top divisors already occur in the ambient chart. It does not count guarded
FPC5 contributors or pay any source cell.
