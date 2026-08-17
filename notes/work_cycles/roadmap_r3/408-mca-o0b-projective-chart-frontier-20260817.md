## MCA O0b projective-chart frontier (2026-08-17)

### Exact progress

- The cells-3/6 matching equations `q4,q5,q6` are proved to be quadratic
  resultants. Their simultaneous vanishing is exactly the union of the eight
  finite/infinity projective common-root charts; degree drops and the common
  root at infinity are included.
- For representative
  `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`, chart `III` and
  the three one-finite masks `FII`, `IFI`, `IIF` are proved empty. Every one
  becomes unit at the forbidden boundary guard `b+1`.
- The exact remaining leaves for this representative are `FFF`, `FFI`, `FIF`,
  and `IFF`. Closing these four leaves closes the representative; no other
  chart is missing.

### Retired endpoints

- The direct high-degree resultant initial ideal timed out.
- Raw multi-finite chart ideals timed out before an initial basis.
- Direct Rabinowitsch inversion of `b+1` timed out on all four multi-finite
  masks.
- An exact eight-variable sparse kernel graph lift timed out on `FFI` and must
  not be expanded to the other masks.

All timeouts are architectural observations only. They neither refute the
charts nor support promotion of the representative.

### Next decision gate

1. Prefer a structural common-root reduction. In a finite chart, the two
   equations are `A0(u)=record_y*A2(u)` and
   `A0(-u)=record_z*A2(-u)`. Use the concrete pairing-0 record products to
   eliminate outside variables or derive a lower-dimensional syzygy before
   another Groebner computation.
2. A different algebra engine may be compared on one pinned mask only if the
   exact input and outcome-neutral checker remain reproducible. Cap the pilot
   below `$0.10`; do not launch a four-mask campaign from an unvalidated
   engine.
3. On a successful one-mask architecture, finish the other three masks for
   this representative before transporting across the 1,415-representative
   quotient.

### Integration posture

The generic projective-resultant decomposition is already a portable proved
result for the upstream shift-pair/exact-second-moment lane. The partial chart
closures should remain local evidence until the representative is complete.
Fable's prize tree remains at `c31605f55`; no concurrent result currently
supersedes this frontier.

### Resource discipline

All local commands remain RAM-guarded. Algebra runs stay on Modal. Broad
Singular campaigns are prohibited on this frontier; only preregistered,
single-architecture pilots with retained partial output are authorized.
