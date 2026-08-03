# XR deficient-window primitive Pade-pencil router

- **status:** PROVED
- **consumer:** `xr_band_forced_commonroot_syzygy_count`
- **scope:** official prize rows, high band, nonempty maximal selected family

Fix `ceil(h/2)<=d<=h-2`, put `R=n-k`, `r'=R-d`, and let
`K_d` be the left kernel of the stacked window matrix. Assume
`rank J_d<2d` and that at least one maximal depth-`d` pair exists. Let
`G_d` be the common `H`-root set of all syzygies and put `g=|G_d|`.

Then there are coprime, nonproportional, nonzero polynomials `P,Q` and a
nonzero linear space `W` of multiplier polynomials such that, with

```text
ell=max(deg P,deg Q),
```

the complete kernel is

```text
K_d={(SP,SQ):S in W},        W subset F[X]_{<d-ell}.      (PP1)
```

Moreover:

1. `G_d` is exactly the set on which every `S in W` vanishes, and

   ```text
   1<=ell,       ell+g<=d-1,       dim K_d<=d-ell-g.       (PP2)
   ```

2. For every counted pair `(f,g_0)`, with errors `E=u-f` and
   `E'=v-g_0`,

   ```text
   P(x)E(x)+Q(x)E'(x)=0        for every x in H\G_d.       (PP3)
   ```

3. If the counted family is nonempty and `(f_0,g_0)` is one member,
   every member has the unique form

   ```text
   (f,g_0')=(f_0+Q tau, g_0-P tau),   deg tau<k-ell.       (PP4)
   ```

   In particular, full joint cores of two distinct members intersect in
   at most `k-ell-1` points.

4. In the forced-root residual `g>=2(h-d)`, necessarily

   ```text
   d>=ceil((2h+2)/3),       ell<=3d-2h-1.                 (PP5)
   ```

Thus the deficient red leaf is not a general common-factor census. It is
an upper-third-depth count inside one primitive polynomial-direction
affine family, with a stronger pairwise core cap.

This is not the upstream one-parameter moving-root theorem: the locators
still range in a high-dimensional window slice. No occupancy estimate is
asserted.

## Falsifier

A nonempty official deficient system with `r'>2d-2` whose kernel contains
two syzygies with nonzero polynomial determinant; failure of `(PP2)` or
`(PP3)`; or two counted pairs not related by the unique shift `(PP4)`.
