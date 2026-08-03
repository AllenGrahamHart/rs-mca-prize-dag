# XR band windowed-projection reduction

- **status:** PROVED
- **closure:** proof
- **scope:** every Reed-Solomon pencil satisfying the tangent gate and
  the banked `k`-packing property; the final arithmetic is instantiated at
  the three prize rows
- **consumer:** `xr_band_high_window_exclusion`

Let `C = RS_k` on `n` distinct evaluation points, let
`w_z = u + z v` for `z in P^1(F_q)`, and put `A = k+h`. A depth-`d`
joint-explanation pair `P=(f,g)` has full joint-agreement core `Z_P` of
size `k+d`. Write

```text
a_P(z)  = agr(f+zg, w_z),          a_P(infinity) = agr(g,v),
W_d(z)  = #{c in C : k+d <= agr(c,w_z) <= A-2},
beta_d  = floor((n-k-d)/(h-d-1)).
```

For `ceil(h/2) <= d <= h-2`, let `N_d^raw` be the number of all
depth-`d` joint-explanation pairs, before selected-support filtering.
Then

```text
N_d^raw <= ((1/(q+1)) sum_z W_d(z)) / (1-beta_d/(q+1)).       (WPR)
```

Equivalently,

```text
(q+1-beta_d) N_d^raw <= sum_z W_d(z).                         (WPR')
```

The selected occupancy `N_d` is at most `N_d^raw`, so either formula
also bounds `N_d`. In particular, the exact integer inequality

```text
25 sum_z W_d(z) <= 17 n^2 (q+1-beta_d)                        (W17)
```

implies `N_d <= 17n^2/25` at that depth.

At each of the three prize rows, `h=2^s+1`, the band-proper high range
is `[ceil(h/2),h-2]`, `beta_d<n<=q`, and the correction denominator in
`(WPR)` is positive. At the pinned `q>=2^250`, even a family at the
`17n^2/25` target leaves more than 127 bits of margin in the optional
simultaneously-clean-member union bound.

This theorem is a reduction, not the high-window estimate `(W17)`.
It does not assert a Reed-Solomon list-size bound.

## Falsifier

A depth-`d` pair for which the projection multiplicities do not sum to
`n-k-d`; two distinct high-depth pairs with the same projection at one
pencil member; or a tangent-gate pencil violating `(WPR')`.
