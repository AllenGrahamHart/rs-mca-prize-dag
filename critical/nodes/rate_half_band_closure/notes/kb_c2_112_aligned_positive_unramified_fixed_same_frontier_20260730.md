# Aligned positive unramified fixed-moving/same frontier

Status: **NARROWED, not deleted**.  The primary calculation below concerns
the fixed-moving `same` cell; the sibling section records the transfer to all
three fixed-moving allocations among the six open aligned-positive
unramified `c2(1,1,2)` q-slice cells.  Every calculation uses the corrected
relative `U/V` scale from `kb_c2_112_positive_qslice_symmetric.py`.

## Exact reduction

After solving the linear scale normalization and removing the exact open
factor `w^2(p-1)^2`, the four allocation equations are quadratic in `b` and
have `(total degree, terms)`

```text
(16,870), (16,900), (13,396), (13,405).
```

Python-FLINT 0.9.0 computes all three star resultants in about 21 seconds
under `ramguard tiny`; the former SymPy route timed out.  More usefully, a
common `b` root forces the `4 x 3` coefficient matrix to have rank at most
two.  The four `3 x 3` minors factor into explicit open/boundary factors and
one residual polynomial each, with residual shapes

```text
terms:   300, 341, 302, 348
degrees: (p,t,w)=(8,10,4), (8,11,4), (8,10,4), (9,11,4).
```

Eliminating `w` from the first residual minor against the other three gives
three projections in `(p,t)`.  Their common divisorial support consists of

```text
4*p + 5*t + 4 = 0
```

and the reciprocal quartic

```text
16*p^4 + 220*p^3*t - 20*p^3
 + 579*p^2*t^2 + 684*p^2*t - 72*p^2
 + 503*p*t^3 + 1218*p*t^2 + 684*p*t - 20*p
 + 140*t^4 + 503*t^3 + 579*t^2 + 220*t + 16 = 0.
```

This does not cover finite intersections between noncommon projection
factors.

## Routed components

The linear component is completely excluded at the determinantal level.
After `p=-(5*t+4)/4`, the common minor factor is associate to

```text
t^3 (t+1) (t+4) (w-1),
```

and the gcd of the three reduced `w`-projections is associate to

```text
t^5 (t+1) (t+4) (5*t+8)^4.
```

These are respectively supported on `q(1)=0`, repeated endpoint fibers,
`w=1`, or `p=1`.  The helper checks the identities rather than matching only
hashes.

On the quartic, the first two residual minors have a monic linear gcd in
`w`; its root also kills the other two residual minors identically.  Thus the
quartic is a genuine generic rank-two component.  The kernel nevertheless
misses the Veronese condition `[b^2:b:1]` generically.  The kernel-conic
residual has `712` terms and degrees `(p,t,w)=(12,12,7)`.  Its value at the
quartic root has a nonzero norm of degree `496` in `t`.  The norm factors into
22 printed factors; four denominator factors are printed separately.  These
finite specializations are not yet classified.

## Sibling transfer

The same quadratic/minor compiler completes for fixed-moving `swap` and
`mixed` within 22 seconds under the same guard.

For `swap`, the common linear component `4*p+5*t+4=0` has exactly the same
forbidden-support proof as `same`.  The second common component is the
reciprocal cubic

```text
16*p^3 + 204*p^2*t + 804*p^2
 + 165*p*t^2 + 948*p*t + 804*p
 + 20*t^3 + 165*t^2 + 204*t + 16 = 0.
```

All four minors share a linear `w` root on this cubic, but its kernel misses
the `b`-conic generically.  The exceptional support is a degree-`225` norm
in `t` with two separately printed denominator factors.

For `mixed`, one common component is `t^2-4*p=0`, hence a repeated endpoint
fiber.  The nontrivial common component is a 21-term reciprocal degree-five
polynomial.  Again all four minors share its `w` root, while the kernel-conic
test fails generically; its exceptional support is a degree-`48` norm with
no denominator.  On the additional common linear component
`4*p+5*t+4=0`, the residual rank curve is quadratic in `w`; it also misses
the kernel conic generically and leaves a degree-`116` norm in `t`.

Thus all three fixed-moving cells have been reduced to finite specialization
support plus finite intersections among noncommon projection factors.  The
separate moving trace router now narrows all three moving-moving cells as
well.

## Replay

All commands are serial and must retain both resource guards.

```bash
tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 60s \
  /home/u2470931/.venvs/prize-flint/bin/python \
  critical/nodes/rate_half_band_closure/notes/kb_c2_112_aligned_positive_unramified_flint.py \
  fixed-moving --allocation same --linear-component

tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 60s \
  /home/u2470931/.venvs/prize-flint/bin/python \
  critical/nodes/rate_half_band_closure/notes/kb_c2_112_aligned_positive_unramified_quartic_router.py \
  --test-pair-cache \
  critical/nodes/rate_half_band_closure/notes/kb_c2_112_aligned_positive_unramified_quartic_pair01.json
```

The generated input caches are independently reproducible with the
compiler's `--dump-minor-cache` and `--dump-conic-cache` modes.  The quartic
or cubic pair caches are produced by the router's `--pair 01 --dump-gcd`
mode; mixed uses the cheaper `--pair 23`.  Every cache and decoded polynomial
is hash-pinned.

## Remaining close

1. Classify every fixed-cell kernel-conic norm and denominator
   specialization, retaining rank-drop and leading-coefficient exceptions.
2. Classify finite intersections among the noncommon factors of each cell's
   three `(p,t)` projections.
3. Replay every surviving determinant point in all four original quadratic
   equations and the full forbidden product.
4. Compile and route the three moving-moving cells after transporting the
   normalization through the reciprocal trace descent.

No DAG node or status changes on the evidence in this note.
