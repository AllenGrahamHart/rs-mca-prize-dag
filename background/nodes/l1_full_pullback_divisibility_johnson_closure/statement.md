# L1 full-pullback divisibility/Johnson closure

- **status:** PROVED
- **role:** pay the Johnson side of fully fiberwise tame pullbacks without a
  smooth quotient-label hypothesis
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Setup

Let an official dyadic row have `n=2^m`, dimension `k>1`, and valid
source-petal size `2<=ell<=n-k+1`, with

```text
ell=sigma+1,       a_*=k+sigma=k+ell-1.               (FJ1)
```

Fix a nontrivial dyadic `s|n` with `s|ell`, and a monic degree-`s`
polynomial `P` whose complete fibers partition the evaluation domain. Put

```text
b=n/s,       K_0=ceil(k/s),       d=K_0-1,
h_0=ceil(a_*/s).                                      (FJ2)
```

Consider codewords whose complete agreement support is a union of complete
`P`-fibers.

## Divisibility exclusion

No such codeword has exact agreement `a_*`. Its agreement size is a multiple
of `s`, while `s` does not divide `a_*`. More explicitly,

```text
s<=k:       h_0=(k+ell)/s,
s>k:        h_0=ell/s+1.                              (FJ3)
```

Thus the fully fiberwise class begins strictly above the exact source shell.

## Domain-independent Johnson payment

If

```text
h_0^2>b d,                                             (FJ4)
```

then for every received word and every fixed `P`, the number of fully
fiberwise listed codewords is at most

```text
floor(b(h_0-d)/(h_0^2-bd)) <= b^2.                    (FJ5)
```

No smoothness or multiplicative structure of the label domain is required.
When `s<=k`, condition `(FJ4)` is exactly

```text
(k+ell)^2>(k-s)n.                                     (FJ6)
```

When `s>k`, one has `K_0=1`, `d=0`, so `(FJ4)` is automatic.

Combining `(FJ5)` with `l1_tame_fixed_petal_refinement_census`, all tame
fixed-source full-partition maps in this Johnson sector contribute at most

```text
n b^2 <= n^3.                                         (FJ7)
```

## Scope

This theorem itself does not cover the full-partition sub-Johnson sector
`h_0^2<=bd`, partial agreement fibers, sparse complete-fiber coverage with
`kappa>0`, wild refinement maps, or unanchored/arbitrary-locator cells. The
later `l1_full_domain_pullback_intrinsic_rigidity` retires the first of those
by proving every full-domain map intrinsic. The other residuals remain.
