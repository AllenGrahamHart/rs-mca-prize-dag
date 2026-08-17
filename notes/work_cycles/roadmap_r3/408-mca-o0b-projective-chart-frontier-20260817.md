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
- The exact remaining leaves for this representative are now `FFF` and
  `IFF`. Closing these two leaves closes the representative; no other chart
  is missing.
- In `FFI` and `FIF`, the infinity equations force `z2=z5=0`. On that
  collapsed locus, the pinned `q3` equation and `a2m != 0` guard prove
  that every finite first matching polynomial has nonzero linear
  coefficient. Thus its finite root can be eliminated exactly by a
  coefficient determinant plus the printed slope guard.
- Adjoining `k2=k5=0` to the saturated four-variable common basis produces
  a checked nonunit dimension-zero basis of size 43. Hence all admissible
  `FFI/FIF` base points lie in a finite common scheme before `d,e,f` are
  introduced.
- Reapplying all 16 route guards to that finite scheme gives a checked unit
  basis at guard index 5, `b+1`. Therefore the exact admissible
  `k2=k5=0` base locus is empty, closing both `FFI` and `FIF`.

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
- The exact 14-variable determinant chart with both proved slope guards also
  timed out without an initial transcript. Monolithic `FFI` basis runs in
  this coordinate order are now retired.

All timeouts are architectural observations only. They neither refute the
charts nor support promotion of the representative.

### Next decision gate

1. Address `IFF` by splitting its infinity consequence
   `(be-cf)z2=0` into `z2=0` and `be=cf` branches. Reuse the successful
   finite-common saturation whenever a branch also forces `z5=0`.
2. Address `FFF` through a genuine quadratic-root invariant or a finite
   common-base consequence; the linear collapsed determinant route does not
   apply.
3. Once both remaining masks close, promote the representative and transport
   it across the 1,415-representative quotient.

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
