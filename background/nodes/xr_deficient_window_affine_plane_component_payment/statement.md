# XR deficient window: affine-plane component payment

- **status:** PROVED
- **consumer:** `xr_band_forced_commonroot_syzygy_count` (evidence)

In the setup of the affine-plane triple router, fix an independent
`(s-2)`-core cut and three points `x,y,z` in one selected defect block with
pairwise distinct values of `phi=[P:Q]`.  The two block equations

```text
det(V_x,V_y)=det(V_x,V_z)=0
```

have at most three target parameters on the residual affine plane, with no
hypothesis on the projective evaluations of its two-dimensional direction
code.

Consequently, whenever `r>2ell`, the restriction-degeneracy term in `(APT1)`
is unnecessary and

```text
2 |Tau| B_(s-2) r(r-ell)(r-2ell)/6
 <=3 binom(N,s-2)binom(e,3),                       (ACP1)

|Tau| <=3N^(s-2)e(e-1)(e-2)
          /(2r(r-ell)(r-2ell)product_(j=3)^s(w+j)). (ACP2)
```

For `x=d+ell<=4h/5`, the right side of `(ACP2)` is maximized at `ell=1`.
Therefore the following larger next-dimension slices are paid:

```text
rate 1/4:   s=11, r>2ell, d+ell<=6,840,580,025,
rate 1/8:   s=11, r>2ell, d+ell<=6,840,580,025,
rate 1/16:  s=10, r>2ell, d+ell<=3,435,973,837.    (ACP3)
```

At rate `1/16`, the separate `ell=1` payment extends further to
`d+1<=3,523,371,941`.  This does not pay the upper tails, widths with
`r<=2ell`, or every higher-`ell` tuple.  The critical node remains `TARGET`.
