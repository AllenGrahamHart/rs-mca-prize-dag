# XR deficient-window rational-direction payment

- **status:** PROVED
- **consumer:** `xr_band_maximal_window_divisor_count`
- **scope:** tangent-gated high band, with `q>n`

Fix `ceil(h/2)<=d<=h-2`, put `r'=n-k-d`, and let `K_d` be the
left kernel of the stacked window matrix `J_d=[R_u;R_v]`. Write a
kernel vector `(a,b)` as the reversed polynomials

```text
A(X)=sum_{s=0}^{d-1} a_s X^(d-1-s),
B(X)=sum_{s=0}^{d-1} b_s X^(d-1-s).
```

When `K_d` is nonzero define its forced common-root set

```text
G_d={x in H : A(x)=B(x)=0 for every (A,B) in K_d}.
```

Then:

1. For every maximal depth-`d` pair `(f,g)`, with errors
   `e=u-f`, `e'=v-g`, every `(A,B) in K_d` satisfies

   ```text
   A(x)e(x)+B(x)e'(x)=0                 for every x in H.       (RD)
   ```

2. If `q>n`, some nonzero syzygy has common `H`-root set exactly
   `G_d`. Every syzygy is divisible componentwise by the locator of
   `G_d`; consequently, for `g_d=|G_d|`,

   ```text
   dim K_d <= 2(d-g_d),       rank J_d >= 2g_d.                 (FR)
   ```

3. Partition the selected maximal occupancy as

   ```text
   N_d = N_d^out + N_d^G,
   ```

   where a pair is counted by `N_d^out` when at least one of its
   selected rays has an off-core agreement point in `H\G_d`, and it is
   counted by `N_d^G` otherwise. Then, without any size assumption on
   `G_d`,

   ```text
   N_d^out <= n-g_d.                                           (PAY)
   ```

   Every selected ray of a pair counted by `N_d^G` has all `h-d` of
   its off-core agreement points in `G_d`. Since each counted pair has
   at least two selected slopes and their off-core blocks are disjoint,

   ```text
   N_d^G>0  implies  g_d>=2(h-d).                              (LOC)
   ```

Thus the only unpaid pairs are those whose complete selected off-core
geometry is local to a forced set of at least `2(h-d)` points. In
particular, since tangent-gated syzygies are nonproportional and hence
have common-gcd degree at most `d-2`, every deficient system in

```text
ceil(h/2) <= d <= floor((2h+1)/3)
```

has `N_d^G=0` and is paid by this theorem with `N_d<=n-g_d`.

No count is asserted for full joint rank or for the forced-common-root
remainder.

## Falsifier

A maximal exact-depth pair violating `(RD)`; failure of the exact-root
choice at `q>n`; more than `n-g_d` pairs carrying a selected off-core
point outside `G_d`; or a `G_d`-local pair when
`g_d<2(h-d)`.
