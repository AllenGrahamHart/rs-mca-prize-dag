# KoalaBear m2 r2 full-V4 source genus drop

- **status:** PROVED
- **scope:** the residual actual KoalaBear inner-degree-two type
  `(r,delta)=(2,4)`
- **dependencies:** `rate_half_kb_m2_v4_outer_recurrence_router` and the
  proved residual birational-quartic/conic exclusion
- **consumer:** `rate_half_band_closure`

Let `Gamma` be the normalization of the actual bidegree-`(2,4)` source
component, let `eta` be the involution of its degree-two projection to the
source parameter `X`, and let `a` and `c` be the lifts of

```text
tau x 1,       1 x tau
```

from the full V4 stabilizer of the `(2,4)` endpoint component. The map
`W=psi(X)` has degree four and deck group

```text
<eta,a> = V4.
```

Conjugation by `c` fixes `a` and exchanges `eta` with `eta*a`. If it fixed
`eta`, then `c` would descend to a nontrivial involution of the source
parameter line and the quartic coefficient map would factor through its
degree-two quotient, putting the coefficient image in the already-excluded
line/conic branch.

The two conjugate involutions `eta` and `eta*a` therefore have the same
number of fixed points. Tame V4 Riemann-Hurwitz, together with the
degree-two quotient `Gamma/<eta>=P1`, gives

```text
g(Gamma) in {0,1},
#Fix(a)=2-2g(Gamma).
```

Thus the full-V4 row has exactly two source-normalization regimes:

```text
g=0 and #Fix(a)=2;
g=1 and #Fix(a)=0.
```

No regime is deleted. This proves no source genus lower bound, outer
passport classification, carrier/data/slope owner, payment, `u=2` close,
adjacent certificate, or Prize row.

## Falsifier

An actual full-V4 row of source genus two or three, conjugation by `c`
fixing `eta` without forcing a line/conic coefficient image, or a failure of
the printed tame fixed-point identity.
