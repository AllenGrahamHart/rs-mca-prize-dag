# XR deficient window: two-block kernel-slack router

- **status:** PROVED
- **consumer:** `xr_band_forced_commonroot_syzygy_count` (evidence)

Use the deficient primitive-Pade and active-defect notation

```text
r=h-d,       g=|G_d|,       e=|D|,
sigma=d-ell-1-2r=3d-2h-ell-1.
```

Every nonempty `D`-local target satisfies

```text
2r<=e<=g<=2r+sigma.                                  (TKS1)
```

Suppose `sigma<r`. Then every target has exactly two selected live slopes,
with disjoint active blocks `B_1,B_2` of size `r`, and

```text
|D\(B_1 union B_2)|<=sigma,
|G_d\(B_1 union B_2)|<=sigma.                        (TKS2)
```

Let `Z_G` be the monic locator of `G_d`. In the primitive kernel normal form

```text
K_d={(SP,SQ):S in W},
```

every multiplier has the sharper representation

```text
S=Z_G U,       deg U<d-ell-g<=sigma+1.               (TKS3)
```

In particular, `1<=dim K_d<=sigma+1` in this deficient branch.

At the tuple-incidence obstruction

```text
ell_0=floor((h-4)/7),       r_0=2ell_0+1,
d_0=h-r_0,
```

the official values are

```text
rates 1/4,1/8: sigma=5,  deg U<6,  1<=dim K_d<=6,
rate 1/16:     sigma=1,  deg U<2,  1<=dim K_d<=2.    (TKS4)
```

Thus the difficult deficient profile is an almost complete two-ray cover of
the whole forced-root set, with only `5,5,1` exceptional points. It is not a
generic bounded-nullity affine window and should not be merged with the
full-rank `dim K_d=0` branch before this extra structure is consumed.

## Falsifier

A nonempty `D`-local deficient target with `sigma<r` and a third selected
live slope; more than `sigma` forced-root points outside its two selected
blocks; a multiplier cofactor of degree at least `sigma+1`; or an official
boundary slack different from `5,5,1`.
