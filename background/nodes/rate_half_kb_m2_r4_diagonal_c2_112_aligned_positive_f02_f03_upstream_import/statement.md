# KoalaBear aligned-positive F02/F03 upstream import

- **status:** PROVED
- **scope:** all six literal
  `{F02,F03} x {R02,R11,R20}` aligned-positive unramified cells over
  `F_(2130706433^6)`
- **provenance:** Przemek repository PR #1141, exact commit
  `826c0e7610604d550b8dd9b772c197a4e660e525`
- **consumer:** source-line literal-assignment coverage

For

```text
F02={E01,E12},       F03={E01,E13},
```

the exact factor-first localized q-slice calculation proves

```text
F02-R11 = empty.                                     (KBF2-1)
```

The `R02` and `R20` q-slices have finite schemes of dimensions four and
eight. Their points all lie over the recorded irreducible quadratics in
`F_(p^2)`, hence in `F_(p^6)`. At every point the coefficient-one mismatch
in each full `J/I` quotient identity has a nonzero quadratic norm. Therefore

```text
F02-R02 = empty,       F02-R20 = empty.             (KBF2-2)
```

The upstream compiler proves the literal complete-source identity
`F03(b)=F02(b^-1)`, including `U,V,z`, the named open, and all `J/I/K/R`
factor multisets. Inversion is bijective on `b!=0`, so `(KBF2-1)--(KBF2-2)`
also exclude all three `F03` cells.

```text
F03-R02 = empty,       F03-R11 = empty,
F03-R20 = empty.                                     (KBF2-3)
```

The load-bearing Sage certificate is pinned by raw SHA-256 and payload hash.
Its fail-closed Python verifier was independently replayed in a detached
checkout of the exact commit on 2026-08-07 and passed all 26 semantic mutation
tests. The upstream theorem records a prior independent Sage and Python
review returning GREEN.

## Falsifier

A missing factor branch, a point outside the finite survivor census, a zero
recorded mismatch norm, failure of literal `F02 -> F03` transport, or a hash
mismatch against the pinned upstream proof objects.
