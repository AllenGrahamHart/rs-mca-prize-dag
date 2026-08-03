# XR deficient window: affine-plane triple router

- **status:** PROVED
- **consumer:** `xr_band_forced_commonroot_syzygy_count` (evidence)

Use the active-defect notation

```text
N=n-e,       K=k-ell,       w=d+ell,       r=h-d,
```

and let `Tau` have affine dimension `s>=2`.  Choose `s-2` independent
punctured-core agreement hyperplanes through a target parameter.  Their
intersection with the affine hull is a plane with two-dimensional direction
space `U_C=<delta_1,delta_2>`.  On `D`, put

```text
psi_C(x)=[delta_1(x):delta_2(x)]
```

when the two evaluations do not both vanish.

A **triple flag** consists of this core cut, one selected `r`-point defect
block, and three points of the block with pairwise distinct values of
`phi=[P:Q]`.  It is restriction-degenerate when one of the three `psi_C`
values is undefined or two are equal.  Let `I_deg` be the number of
restriction-degenerate flags, counted with their target parameters.

If `r>2ell`, then

```text
B_(s-2)=product_(j=3)^s(w+j)/(s-2)!,

2 |Tau| B_(s-2) r(r-ell)(r-2ell)/6
 <= I_deg + 3 binom(N,s-2) binom(e,3).              (APT1)
```

In particular, a family with no restriction-degenerate flag satisfies

```text
|Tau| <= 9 binom(N,s-2)binom(e,3)
             /(B_(s-2)r(r-ell)(r-2ell))

      <= 3 N^(s-2)e(e-1)(e-2)
             /(2r(r-ell)(r-2ell)product_(j=3)^s(w+j)).  (APT2)
```

For `ell=1`, `(APT2)` is below the smallest official SL2-D local budget at
the next currently unpaid affine dimensions throughout

```text
rate 1/4:   s=11, d+1<=6,840,580,025,
rate 1/8:   s=11, d+1<=6,840,580,025,
rate 1/16:  s=10, d+1<=3,523,371,941.               (APT3)
```

Consequently a counterexample in one of these slices must contain a
restriction-degenerate triple flag.  This is a structural reduction, not a
bound on `I_deg`; no critical status changes.
