# RS common-root weighted basis charge

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependency:** `xr_poststrip_affine_pencil_charge`

Let `H:F^D->Y` be a parity check of an `[n,k]` Reed-Solomon code. Fix
`1<=h<=R=n-k`, put `r=R-h`, and let `P` contain one pair `(gamma,e)` at
each of a finite set of distinct slopes. Assume

```text
e in A,       He=y_0+gamma y_1,       wt(e)<=r,
```

where `A` is an affine space above the nonconstant syndrome line, has affine
dimension `s`, and satisfies the genericity hypothesis of the affine-core
charge. Put `a=s-1>=1`. Suppose also that distinct selected errors satisfy

```text
|Z_e intersect Z_f| <= kappa <= k,
L=floor((n-kappa)/(k+h-kappa)).
```

Let `K=(A-A) intersect ker H`. Let `G` be the set of coordinates on which
every word of `K` vanishes, write `g=|G|`, and let `P_0 subset G` be the
coordinates on which every member of `A` vanishes, with `p=|P_0|`. Then

```text
g <= k-a,

C(a+h-1,a-1) ( |P|(k+h-p) - (g-p) )
 <= a C(n-g,a) L.                                      (CRB1)
```

In particular, put `Q=C(a+h-1,a-1)`. Then

```text
|P| <= floor(
  max{
    aL C(R+a,a)/(Q(a+h)),
    aL C(n,a)/(Q(k+h)),
    (aL C(R+a,a)+Q(k-a))/(Q(k+h))
  }
).                                                       (CRB2)
```

At the six XR rows, both the high-core application `kappa=k` and the
low-core application `kappa=k-1` pay selector ranks

```text
4,4,4,16,16,14.
```

Thus the first open prize selector ranks improve from `16,16,15` to
`17,17,15`. The theorem does not improve the RowC or prize-rate-`1/16`
frontiers and does not close either XR target.
