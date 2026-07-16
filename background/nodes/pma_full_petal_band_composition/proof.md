# Proof - PMA full-petal band/root composition

## 1. The two petal counts

The exact agreement set contains `k-1-d` core points, `t ell` petal points,
and `r` background points. The list threshold is `k+ell-1`, hence

```text
(k-1-d)+t ell+r >= k+ell-1,
t ell+r >= d+ell.                                  (1)
```

Maximality gives `r<=b<ell`. The planted-receiver two-class exhaustion
theorem proves that a non-planted listed word touches at least two petals, so
`2<=t<=M`. This proves `(FPC1)`.

The maximal source layout has all `M` petals available. The G1 chart carried
by that layout therefore has `m_chi=M`; `t` records only the subset actually
touched by this codeword. These are different definitions.

Assume the top-band inequality `d>=ell(M-2)`. From (1) and `r<=ell-1`,

```text
t ell
 >= d+ell-r
 >= ell(M-2)+ell-(ell-1)
 = ell(M-2)+1.
```

Thus `t>=M-1`. Since `t<=M`, this proves `(FPC3)`. The banked G1
clause-(P) audit realizes both `M-1` and `M` touched-petal strata, so replacing
this conclusion by `t=M` would be false.

## 2. Composition with root pinning

The green `petal_growth` theorem pays every layout-anchored full-petal class
with `d>=ell(M-2)`. Consider the complement. Since all quantities are
integral,

```text
d<=ell(M-2)-1.                                      (2)
```

If also `t>=2M-4`, then

```text
2d+1-t ell
 <= 2ell(M-2)-1-t ell
 = ell(2M-4-t)-1
 <= -1.
```

Hence the root-pinning excess is `e=0`. The pattern is full-petal, so its
petal deficit `u=t ell-h` is also zero. The `E=0` aggregate in
`pma_petal_pattern_root_pinning_ledger` pays this whole branch at the L1 lower
cutoff. Together with the top band this proves `(FPC4)`.

For `M=2`, the top-band threshold is zero, so every class is already paid.
For `M=3`, non-plantedness gives `t>=2=2M-4`, so `(FPC4)` pays every class.
For `M=4`, the second branch pays `t=4`, while the top band pays every `t` at
`d>=2ell`; only `t=2,3` below the band can remain. For `M>=5`, retaining only
the complement of both proved payments gives the first three conditions in
`(FPC5)`. The existing root-pinning theorem already pays every fixed `e`
region, so a family still present in the direct PMA target must have
`e->infinity`. This proves `(FPC5)`.

## 3. Deficit coordinates

On the below-band branch define

```text
a=M-t,       v=ell(M-2)-d.
```

Equation (2) gives `v>=1`. Substitute `t=M-a` and
`d=ell(M-2)-v` into (1):

```text
(M-a)ell+r >= ell(M-2)-v+ell=ell(M-1)-v,
(a-1)ell <= r+v.
```

The root-pinning excess becomes

```text
e
 = max(0,2d+1-t ell)
 = max(0,2ell(M-2)-2v+1-(M-a)ell)
 = max(0,ell(M+a-4)-2v+1).
```

This proves `(FPC6)` and completes the composition theorem.
