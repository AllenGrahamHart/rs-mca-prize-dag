# FPC5 `M=4,t=2` official codimension sieve

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment` after the rate-quarter close

On every official row `k=2^40`. For an `M=4,t=2` full-petal cell write

```text
d=ell+s,       c_slice=ell-s-1.
```

Then

```text
rate 1/2:   c_slice>=2,
rate 1/4:   c_slice>=(k+4)/5.
```

In particular the codimension-zero endpoint `s=ell-1` is impossible at both
surviving rates.

This does not count split locators in the positive-codimension slice. At
rate `1/2`, petal-equation codimension two remains possible. The separate
guarded-slice theorem proves that its forced full-background agreement raises
the actual guarded locator codimension to `ell-1`.
