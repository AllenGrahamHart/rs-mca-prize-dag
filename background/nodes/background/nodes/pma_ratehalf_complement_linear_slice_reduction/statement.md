# PMA rate-half complement linear-slice reduction

- **status:** PROVED
- **consumer:** `petal_mixed_amplification`
- **role:** identify the guarded tail fiber as one exact split-in-subspace atom

## Statement

Use the normalized rate-half notation of
`pma_ratehalf_two_petal_support_fiber_reduction`. Put

```text
M=L_2L_3,              deg M=2ell,
d=2ell-a,              m=N-d.
```

The normalized source CRT polynomial has the factorization

```text
E_c=L_1 Etilde,
```

and, after dividing the source identity by `L_1`,

```text
L_C Etilde=F_lambda+M Y.                            (LS1)
```

Moreover `Etilde` is a unit modulo `M`; explicitly,

```text
Etilde == L_1^(-1)          mod L_2,
Etilde == lambda L_1^(-1)   mod L_3.                (LS2)
```

For an `m`-subset `S` of the core, write

```text
D_S=L_C/L_S,                deg D_S=d,
V_D=rem_M(D_S Etilde).                              (LS3)
```

Then `S` belongs to the exact guarded fiber of the predecessor if and only if

```text
deg V_D<=ell-a,
gcd(V_D,D_S)=1.                                     (LS4)
```

For such a divisor the contributor is recovered by

```text
H_D=(L_S V_D-F_lambda)/M.                           (LS5)
```

Thus the fixed-cell list is in bijection with

```text
{D monic : D|L_C, deg D=2ell-a,
            deg rem_M(D Etilde)<=ell-a,
            gcd(D,rem_M(D Etilde))=1}.              (LS6)
```

Let `K[X]_<2ell` denote polynomials of degree less than `2ell`. The unguarded
linear slice

```text
W_(lambda,a)={D in K[X]_<2ell:
               deg rem_M(D Etilde)<=ell-a}          (LS7)
```

has dimension exactly `ell-a+1` and codimension `ell+a-1`. Consequently
(LS6) is a generated-field split-in-subspace divisor atom with one exactness
guard. It is not an ordinary untwisted prefix fiber unless a further
source-to-prefix conjugacy is proved.

### Mu-basis reconciliation

Put `s=ell-a`, `d=ell+s`, and let

```text
W_(lambda,a)^<=d=W_(lambda,a) intersect K[X]_<=d.
```

The map

```text
D -> (F,W)=(D,L_1 rem_M(D Etilde))                  (LS8)
```

is a linear bijection from this truncated slice to the three-petal space
`V_s` of `pma_three_petal_mu_basis_reduction`, for labels
`(0,1,lambda)`. If its reduced syzygy degree is `mu`, then

```text
dim W_(lambda,a)^<=d
 =[ell-a-mu+1]_+ + [mu-a+1]_+.                     (LS9)
```

If the guarded fiber (LS6) is nonempty, its member is saturated, so the
mu-basis balance theorem sharpens (LS9) to

```text
a>ell/2   ==> dim W_(lambda,a)^<=d=1,
a<=ell/2  ==> dim W_(lambda,a)^<=d=ell-2a+2.        (LS10)
```

Thus, in the live upper branch, the monic ambient locus has affine dimension
`ell-2a+1`. This is exactly the earlier mu-basis freedom, now attached to the
complement-divisor atom; the linear-slice coordinate change does not itself
reduce that freedom.

## Scope

This theorem does not bound the number of split divisors in (LS6), prove a
max-to-mean estimate, or assign quotient/field-drop members to an existing
owner. It replaces the inverse-locator support map by an exact linear slice
and supplies an instance map to the BC/SCK attack surface only. Formula
(LS10) is a dimension statement, not a split-divisor count.
