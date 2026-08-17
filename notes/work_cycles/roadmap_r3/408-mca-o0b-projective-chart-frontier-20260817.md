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
- In `FFI` and `FIF`, the infinity equations force `z2=z5=0`. On that
  collapsed locus, the pinned `q3` equation and `a2m != 0` guard prove
  that every finite first matching polynomial has nonzero linear
  coefficient. Thus its finite root can be eliminated exactly by a
  coefficient determinant plus the printed slope guard.

### Retired endpoints

- The direct high-degree resultant initial ideal timed out.
- Raw multi-finite chart ideals timed out before an initial basis.
- Direct Rabinowitsch inversion of `b+1` timed out on all four multi-finite
  masks.
- An exact eight-variable sparse kernel graph lift timed out on `FFI` and must
  not be expanded to the other masks.
- Both the 16-variable leading-collapsed `FFI` ideal and its 14-variable
  unguarded determinant superset timed out. The latter included slope-zero
  components that the new finite-slope theorem excludes from the exact chart.

All timeouts are architectural observations only. They neither refute the
charts nor support promotion of the representative.

### Next decision gate

1. Run one exact 14-variable `FFI` determinant presentation with the proved
   `m4p1*m5p1 != 0` slope guards. A unit closes `FFI`; any other outcome
   retires broad basis computation on this mask.
2. If the exact pilot does not close, branch or factor the two explicit
   determinants under `q3`; retain the exact slope guards in every branch.
3. Transport the successful collapsed architecture to `FIF`, then address
   the structurally different `FFF` and `IFF` leaves before quotient
   transport.

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
