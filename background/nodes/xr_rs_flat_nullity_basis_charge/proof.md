# Proof

Factor the common evaluation roots from the RS kernel slice. Since
`g=k-a-u`, division identifies `K` with an `a`-dimensional polynomial
subspace

```text
W subset F[X]_{<a+u}
```

having no common root on `D\G`.

Fix a selected error and let `M_e` be the coordinate matroid of `K` on the
nonloop part of its zero set. Let `F` be a proper flat of `M_e` with rank
`j<a`. The polynomials in `W` vanishing on `F` form a subspace of dimension
`a-j`. Every one is divisible by the product of the `|F|` distinct root
factors. Division embeds that subspace into `F[X]_{<a+u-|F|}`. Therefore

```text
a-j <= a+u-|F|,
```

which is `(FN1)`.

Count ordered bases of `M_e`. There are `m_e` choices for the first element,
because all loops were deleted. After choosing an independent ordered
`j`-set, its closure is a proper rank-`j` flat, so `(FN1)` leaves at least
`m_e-u-j` choices for the next element. Hence

```text
a! b_e
 >= m_e product_(j=1)^(a-1) (m_e-u-j)
  = m_e (a-1)! C(m_e-u-1,a-1).
```

This proves `(FN2)`.

At a global loop outside `P_0`, the affine coordinate function is nonzero
and can vanish at only one selected slope. If

```text
l_e=|Z_e intersect (G\P_0)|,
```

then `sum_e l_e<=v`. In particular at most `v` selected errors have
`l_e>0`. Every unexceptional error has

```text
m_e>=k+h-p=a+h+u+v=m_0,
```

and every error has `m_e>=m_*=a+h+u`. The function `W_u(m)` is increasing
on this range. If `|P|>v`, summing `(FN2)` therefore gives

```text
a sum_e b_e
 >= (|P|-v)W_u(m_0)+vW_u(m_*)
  = |P|W_u(m_0)-v(W_u(m_0)-W_u(m_*)).                 (1)
```

Every basis avoids `G`, and the post-strip pencil cap permits at most `L`
selected errors over each basis. Since `n-g=R+a+u`,

```text
sum_e b_e <= C(R+a+u,a)L.                              (2)
```

Combining `(1)` and `(2)` proves the floor in `(FN3)`. If `|P|<=v`, the
other term in the maximum proves the claim.

For `(FN4)`, every selected zero set contains `P_0`. After deleting `P_0`,
it has size at least `k+h-p`, while two such residual zero sets intersect in
at most `kappa-p=t-1` coordinates. Thus no `t`-subset occurs in two residual
zero sets. Counting `t`-subsets gives `(FN4)`.

The RowC residual table substitutes `a=4`, the three exact values of `h`,
and the high/low values `kappa=k,k-1`. It checks every integer
`u,v>=0`, `u+v<=k-a`, and retains a pair exactly when both `(FN3)` and
`(FN4)` exceed `8n^3`. The exact replay is in `verify.py`.
