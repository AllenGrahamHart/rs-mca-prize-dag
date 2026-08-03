# XR deficient-window mixed core/block payment

- **status:** PROVED
- **closure:** proof plus exact official arithmetic
- **consumer:** `xr_band_forced_commonroot_syzygy_count`

Use the active-defect punctured-list router.  Put

```text
N=n-e,  K=k-ell,  w=d+ell,  r=h-d,
```

and let `Tau` have affine dimension `s`.  If `d_j` are the generalized
weights of its direction code on `H\D`, then every target member has at
least

```text
product_(j=2)^s (d_j-(N-K-w)+b)/(s-1)!
```

independent `(s-1)`-tuples of core-agreement hyperplanes.  Each tuple cuts
the affine hull to a line.

For `x in D`, let `phi(x)=[P(x):Q(x)]`.  Every fiber of `phi` has at most
`ell` points.  Consequently each selected `r`-point active block contains at
least

```text
r(r-ell)/2
```

unordered pairs `{x,y}` with `phi(x)!=phi(y)`.  Along any core-cut line, at
most two target members can have one selected block containing a fixed such
pair.  Double counting gives, whenever `ell<r`,

```text
|Tau| <= floor(
  (N)_(s-1) e(e-1)
  / (r(r-ell) product_(j=2)^s(w+j))
).                                                        (MCB1)
```

Here `(N)_(s-1)` is a falling factorial.  This is an upper bound for the
actual selected parameter set, not for every word in its affine hull.

Combine `(MCB1)` with the affine-span list bound.  Over the complete official
active-defect range, the two bounds pay `(SL2-D)` at affine dimensions

```text
rate 1/4:  s=10,
rate 1/8:  s=10,
rate 1/16: s=9.
```

Together with the preceding low-span payment, `(SL2-D)` is proved through
dimensions `10,10,9`.  Any counterexample has affine dimension at least
`11,11,10` on the three rows.

## Falsifier

A target family at one displayed dimension violating `(MCB1)`, a
`phi`-fiber larger than `ell`, more than two same-witness members on a
core-cut line, or an official arithmetic tuple where both the affine and
mixed bounds exceed the local budget.
