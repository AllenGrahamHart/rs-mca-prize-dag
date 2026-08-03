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

3. If `g_d<2(h-d)`, the selected maximal occupancy obeys

   ```text
   N_d <= n < 17n^2/25.                                         (PAY)
   ```

Thus a deficient high-window system can remain unpaid only when it
has at least `2(h-d)` roots forced on every Pade syzygy. In
particular, since tangent-gated syzygies are nonproportional and hence
have common-gcd degree at most `d-2`, every deficient system in

```text
ceil(h/2) <= d <= floor((2h+1)/3)
```

is paid by this theorem.

No count is asserted for full joint rank or for the forced-common-root
remainder.

## Falsifier

A maximal exact-depth pair violating `(RD)`; failure of the exact-root
choice at `q>n`; or a high-depth selected family with `g_d<2(h-d)` and
more than `n` pairs.
