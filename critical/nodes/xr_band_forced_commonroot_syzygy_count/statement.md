# XR primitive Pade-pencil parameter census

- **status:** TARGET
- **parent:** `xr_band_maximal_window_divisor_count`

In the setup of SL-2-RES, assume `rank J_d<2d` and that the maximal
selected family is nonempty. Let `G_d` be the set of evaluation points
at which both reversed coefficient polynomials of every left syzygy
vanish, and put `g=|G_d|`. Let `R_d^G(u,v)` be the subset of maximal
selected post-strip locators for which **every** selected ray has all
of its off-core agreement points in `G_d`. The proved rational-direction
theorem pays the complementary family with at most `n-g` locators.

In the only deficient stratum in which `R_d^G` can be nonempty, assume

```text
g >= 2(h-d).
```

The proved primitive Pade-pencil router then confines the target to

```text
ceil((2h+2)/3) <= d <= h-2,
K_d={(SP,SQ):S in W},
gcd(P,Q)=1,       ell=max(deg P,deg Q)<=3d-2h-1,
(f,g)=(f_0+Q tau,g_0-P tau),       deg tau<k-ell.
```

The full joint cores of two distinct parameters intersect in at most
`k-ell-1` points. These conditions are conclusions of the router, not
additional conjectural assumptions.

Then the `G_d`-local maximal, selected, post-strip locator set satisfies

```text
25 |R_d^G(u,v)| <= 17 n^2 - 25(n-g).               (SL2-G)
```

Together with the unconditional outside-`G_d` payment, `(SL2-G)` gives
`25|R_d(u,v)|<=17n^2` exactly. This is now an owner-aware local list
count inside one primitive polynomial direction. It is not the assertion
that one conveniently chosen syzygy has many roots, and it is not a
one-parameter locator-pencil count: the roots are forced on the entire
left kernel while maximal locators still range in the original window
slice.

## Falsifier

One official deficient high-window system in the displayed primitive
normal form with
`25|R_d^G|>17n^2-25(n-g)`. A raw `tau` family without exact maximality,
selected liveness, and the all-selected-rays-local predicate is not a
falsifier.
