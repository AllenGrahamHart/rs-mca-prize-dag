# Aligned positive unramified moving-moving/same frontier

Status: **NARROWED, not deleted**.  This is the first of the three open
moving-moving `c2(1,1,2)` source-line q-slice cells.  All calculations retain
the corrected relative `U/V` scale and use exact arithmetic over the deployed
prime `2130706433`.

## Reciprocal trace descent

After solving the linear scale normalization and removing exactly
`w^2(p-1)^2`, each of the four allocation equations is a reciprocal quartic
in `b`.  Dividing by `b^2` and setting `trace=b+b^-1` gives four quadratics
with `(total degree, terms)`

```text
(18,1181), (18,1244), (15,553), (15,574).
```

The compiler checks coefficient reciprocity before applying the descent; it
does not infer it from sampled values.  The four `3 x 3` coefficient minors
have one residual factor each, with `193,222,198,234` terms and `w`-degree
three.  Their three star projections have common support consisting only of
the already excluded factors and

```text
4*p + 5*t + 4
```

together with the reciprocal cubic

```text
8*p^3 + 37*p^2*t + 27*p^2
 + 52*p*t^2 + 89*p*t + 27*p
 + 20*t^3 + 52*t^2 + 37*t + 8.
```

Finite intersections among the noncommon projection factors are not covered
by this divisorial calculation.

## Routed components

On `4*p+5*t+4=0`, the gcd of all four residual minors, and also its gcd with
the kernel-conic polynomial, is associate to

```text
t^3 (t+1) (t+4) (w-1).
```

These factors are respectively `q(1)=0`, the endpoint discriminant, or the
excluded reciprocal fixed point `w=1`.  Thus this complete determinant
component has no admissible point.

Over the cubic function field, all four residual minors share one generic
linear root in `w`.  The root does not satisfy the kernel conic generically.
Its conic failure norm has degree `160` in `t`, factors into 15 printed
factors, and has two separately printed denominator factors.  Those finite
specializations still require classification and original-equation replay.

## Reproducibility

The trace compiler is
`kb_c2_112_aligned_positive_unramified_flint.py`, SHA-256
`988e60a010ea2793049505b5e9b0ff6d5c28b300e4a00a4b8a3724849ede09f0`.
Its generated caches are:

```text
moving_same_minors.json  f5c8285e2d93064f509ecb3ecfad98bb49eb1357777e39e968d06ce769eaba97
moving_same_conic.json   e754fecd9711b5119e4603d45848d601cb894c1c2b357b696c243b8e4439ca72
moving_swap_minors.json  cafb0e48b2be45a98e72dbe5a1689f3ffe9a6bda64e685ea152873af48ab3d86
moving_swap_conic.json   aacf8976e2fe3933055fb8e7d1a90d2b176dad8699ce37cbf2c0f7f3d6fd521e
moving_mixed_minors.json 799e8feb8f89fee7bf7dab30c3e1e4522380bb490f350a5c93f48f6ff19d3565
moving_mixed_conic.json  639a9eeacf175fbfa2e427ca8ad6c3dae1110f658bf4edbe7e3136f2c1748880
```

Replay the component checks serially under both local guards:

```bash
tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 60s \
  /home/u2470931/.venvs/prize-flint/bin/python \
  critical/nodes/rate_half_band_closure/notes/kb_c2_112_aligned_positive_unramified_moving_router.py \
  --allocation same --linear-component

tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 60s \
  /home/u2470931/.venvs/prize-flint/bin/python \
  critical/nodes/rate_half_band_closure/notes/kb_c2_112_aligned_positive_unramified_moving_router.py \
  --allocation same --component
```

## Remaining close

1. Classify every fixed and moving norm and denominator specialization,
   including rank drops and leading-coefficient exceptions.
2. Classify finite intersections among noncommon projection factors.
3. Replay every surviving determinant point in all four trace equations and
   the complete forbidden product.
4. Convert the resulting empty finite ledger into one saturated unit-ideal
   certificate before changing the DAG.

## Sibling transfer

The identical trace compiler now completes the other two moving allocations.
For `swap`, the linear component has forbidden support
`t^2(t+1)(t+4)(w-1)`.  Its only nonboundary common component is

```text
p*t + 5*p + t = 0.
```

The common determinant root on this curve misses the conic generically and
leaves a degree-`26` norm plus the denominator specialization `t=-5`.

For `mixed`, the common projection support consists of open factors, `p=0`,
`4*p+5*t+4`, and one irreducible 91-term component of bidegree `(12,12)`
with deployed-field digest
`9b318c946825ce375fc493b90aa2699b8aebf6868bf552e9a1e8419a66d134b5`.
On the linear component, a further rank curve occurs in the minors, but its
gcd with the conic is only the forbidden support
`t^4(t+1)(t+4)(w-1)`.  On the degree-12 component, the resultant of one
residual minor with the conic is not divisible by the component.  Their
finite intersection is bounded by a degree-`1224` norm in `t`, factored into
38 printed factors.

Thus all six aligned-positive unramified cells have exact finite frontiers.
The moving-moving `swap` component and off-common ledgers have since been
fully replayed: four of six component norm factors are boundary-supported,
the other two fail the original equations, and all eight off-common endpoint
candidates are boundary-supported. The corresponding PROVED node deletes
that cell. The other five cells remain narrowed but open.

The generic evidence in this note alone changes no status; the separate
moving-swap node carries the complete deletion contract.
