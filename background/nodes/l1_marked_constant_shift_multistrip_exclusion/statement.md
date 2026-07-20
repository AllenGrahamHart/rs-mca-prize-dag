# L1 marked constant-shift multistrip exclusion

- **status:** PROVED
- **role:** uniform common-pencil marked stability across all degree strips
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Let `K` be a field, let `P in K[X]` be monic of degree `ell`, and let
`a_1,...,a_t` be distinct elements of `K`. For each `i`, choose

```text
V_i | P-a_i,       S_i=(P-a_i)/V_i,
J=product_i V_i,       v=deg J.
```

Suppose

```text
deg F=d,       deg W<=d,       gcd(F,W)=1,
S_i | W-c_iF                                      (MT1)
```

for scalars `c_i`. For every integer `m>=1`, no such data exist when

```text
t>=2m+1,       m ell<d,       d+v<(m+1)ell.       (MT2)
```

Thus the marked common-pencil residual in degree strip `m` can retain at
most `2m` selected dense petals unless its marked degree reaches the next
strip boundary. On the L1 bounded-polarity branch, `v<=p`, so the sufficient
exclusion conditions are

```text
t_dense>=2m+1,       m ell<d,       d+p<(m+1)ell.  (MT3)
```

If all dense petals of one L1 contributor belong to that pencil, write their
number as `T`. The list threshold, `r<ell`, and `p<ell` then combine with the
exclusion to give the exact survivor window

```text
ceil((d-p+1)/ell) <= T <= 2m.                      (MT4)
```

In particular `m<=T<=2m`, improving to `m+1<=T<=2m` when
`d>m ell+p-1`.

The case `m=1` recovers
`l1_marked_constant_shift_subtwoell_exclusion`.

## Scope

The theorem does not cover arbitrary petal locators, `t<=2m`, or
`d+v>=(m+1)ell`. It is a uniform exclusion of high-petal common-pencil cells,
not a count of the surviving low-petal cells.
