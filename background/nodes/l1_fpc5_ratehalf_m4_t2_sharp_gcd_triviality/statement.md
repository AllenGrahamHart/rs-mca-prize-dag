# Sharp rate-half FPC5 locator flat is gcd-trivial

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment`

In the official sharp rate-half guarded slice, let

```text
deg L_0=ell-3,       deg L_1=deg L_2=ell,
```

where the three locators are pairwise coprime and split on the disjoint
background and touched petals. Let `c_1,c_2` be distinct nonzero labels, and
let `V_F` be the locator flat obtained from

```text
c_2 L_1 A_1 == c_1 L_2 A_2 (mod L_0),
deg A_i<=ell-3,
F=(L_1A_1-L_2A_2)/(c_2-c_1).                         (GT1)
```

Then

```text
gcd{F:F in V_F}=1.                                   (GT2)
```

Consequently the sharp projective-flat descriptor is already in the
gcd-trivial, growing-dimensional split-locator regime. No common-locator-GCD
owner or descent remains at this endpoint.

## Scope

This is flat-wide gcd triviality. It does not say that every candidate is an
exact contributor: the pointwise primitive condition `gcd(F,W_F)=1`, the
untouched-petal nonagreements, splitness on the source core, and first
ownership remain necessary filters.
