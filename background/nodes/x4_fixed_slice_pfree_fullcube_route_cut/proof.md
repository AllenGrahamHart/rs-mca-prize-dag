# Proof

For an `A`-subset `S`, write its reversed locator as

```text
ell_S^*(T)=prod_(x in S)(1-xT)=1+c_1T+...+c_A T^A.
```

The identity

```text
(ell_S^*)'/ell_S^*=-sum_(j>=0) p_(j+1)(S)T^j
```

shows recursively that the full coefficient prefix `(c_1,...,c_t)`
determines every power sum `p_j(S)` for `j<=t`, and hence determines the
subvector indexed by `J`. Thus a full-prefix fiber is contained in one
`Psi_J` fiber. The coordinates of `Psi_J` are sums of fixed field elements
against the `0/1` incidence vector, so `Psi_J` is `F_p`-linear on the Boolean
cube. Removing the condition `|S|=A` only enlarges its fibers.

By `x4_exact_slice_f2_guard_route_cut`, the official depth satisfies

```text
t_XR log2|B0|<=N-129.
```

The codomain of the full-cube map has cardinality at most
`|B0|^|J|<=|B0|^t_XR`. Its domain has `2^N` points. Pigeonhole therefore gives

```text
max_y #{S subset D:Psi_J(S)=y}
 >=2^N/|B0|^t_XR
 >=2^129.
```

Since `N^3=(2^41)^3=2^123`, the full-cube maximum is necessarily larger than
the target budget. Therefore the valid containment cannot be closed by an
upper estimate on the unweighted maximum at scale `N^3`; the fixed slice or an
equivalent owner refinement is load-bearing. QED.
