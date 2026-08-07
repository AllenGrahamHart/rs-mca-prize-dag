# WCL `(1,6)` rational unit-lift pricing report

- **date:** 2026-08-06
- **Modal app:** `ap-WuMWiEvupHO6w3aghjgG1f`
- **result:** `TIMEOUT_REMAINDER`
- **mathematical status:** no change; `(1,6)` remains `TARGET`

## Outcome

The minimal Singular deployment worked.  Installing with
`--no-install-recommends` reduced the image to 11 additional packages,
`12.8 MB` of archives and `41.8 MB` installed, so this run did not repeat the
retired `(1,5)` packaging failure.

The exact rational calculation did not reach elimination.  Singular began
the repeated-squaring construction of

```text
Y^256 mod (E(Y)^2-YB(Y)^2)-1
```

but did not finish coefficient extraction inside 60 seconds.  It emitted
only `WCL16_STAGE_REMAINDER_BEGIN`; the result packet records 60.010725
seconds and program digest
`61418dfd5a4ca40ef4d091098436110c06225f8e9a81560abcd4afee1bc988aa`.
Its SHA-256 is
`3d3d202059dccaada1f61d9584b3fe1e53896d0f02c8d0a0ff19e437826a4f03`.
No standard basis or transformation matrix was attempted.

## Route decision

The expanded six-remainder presentation is retired under the preregistered
stopping rule.  A longer retry would not address the more important route
problem: an integer Nullstellensatz certificate is insensitive to the
official `v_2(q-1)>=41` gate until its prime support is extracted.  Canonical
round-14 measurements already show that this effect makes the analogous
smallest-slot certificate an aggregate of a very large supporting-prime
population.  The exact cubic straight-line presentation remains a correct
mathematical endpoint, but there is no evidence that it yields a tractable
or gate-aware certificate.

The alternative direct `(1,6)` census has `185,569,028` affine-Galois
classes and an existing projection of at least 36,000 CPU-hours, around
`$6.6k`.  It is outside the project budget.  No additional Modal run is
authorized for this cell without a new structural reduction that is both
materially smaller and gate-aware.

This result does not refute the slot, weaken its proved divisor descent, or
support emptiness.  It only removes one computational representation from
the active roadmap.
