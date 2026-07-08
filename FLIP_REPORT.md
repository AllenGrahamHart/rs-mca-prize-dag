# F3 flip report

Status: not a flip dossier.  The branch has materially narrowed
`u1_x4_direct_column_budget`, but it has not proved enough to promote the node
from `TARGET` to `PROVED`.

The detailed node-level report is:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_FLIP_INTERIM_REPORT.md
```

## Replay

The lightweight local replay is:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected final digest:

```text
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

The latest aggregate replay was run under a 60 second wall-clock cap and
completed successfully:

```text
elapsed=56.51 maxrss=98836
```

No Modal job is required for the aggregate replay.

## Confidence-ranked claims

### PROVED / replayed

1. h=2 has an optimized in-house rich-coset chain with
   `E(H) <= 22111 h^(5/2)`.  This covers official powers of two from
   `2^23` upward if used without the external Cochrane-Pinner import.
2. The h=3 hyperbola normal form is replayed symbolically: for
   `F(T)=T^3+aT^2+bT+c`, the same-fiber equation becomes
   `XY = a^2/3 - b` after the explicit `omega` coordinate change.
3. The h=3 hyperbola-line degeneration is classified: the rational-line cell is
   exactly `b=a^2/3`; outside it the conic is irreducible over the coefficient
   field.
4. The h=3 official-row toral degeneracy is absent on the rows that matter,
   because the toral h=3 column requires `3 | n` and every official row is
   `n=2^s`.
5. The h=3 same-fiber conic has a row-field degree-2 rational chart from any
   known conic point.  This puts `U,V,W` membership conditions in the exact
   rational-map class consumed by the rich-curve compiler.
6. The h=3 local fiber-count bridge is fixed: ordered pairwise-distinct
   same-fiber triples equal six times unordered triples, and local activated
   pairs are `binom(N,2)`.
7. The h=3 dilation-normalized activation count lifts to at most `n` raw
   shape pairs per orbit; side-swap stabilizers only reduce the lift size.
8. Nondegenerate h=3 conic charts have no internal constant-ratio collapse
   among `U,V,W`; the remaining constant-ratio danger is confined to excluded
   or separately paid degeneracy cells.
9. The rich-curve denominator compiler and log-jet reduction are banked.  The
   reduced-condition side is now `RC-RED(13)`.
10. Several h=3 rank guardrails are proved or replayed:
   constant-ratio collapsed rank, small-`H` failure, one-factor private-linear
   rank, two-factor failure of naive induction, finite-row bad-prime rank drop,
   generic-open rank-minor formulation, and normalization invariance.
11. The h=3 arithmetic interfaces now cover every official row.  The current
   non-diagonal route is:
   `F3-RANK-AVOID + H3-BRIDGE-RANKCAP(Z_budget(s)) => H3-ACT(16)`.
   The private-linear alternate route is:
   `F3-PRIVATE-LINEAR-RANK-AVOID + H3-BRIDGE-PRIVATE-RANKCAP(Z_private(s)) => H3-ACT(16)`.
12. h=5 has been structurally localized.  Since `5` is not dyadic, the
   char-zero dyadic branch is excluded; every remaining survivor must be a
   p-specific x83 norm-gate event.
13. h=8 has an intrinsic antipodal split: a 16-support in `mu_64` is antipodal
   if and only if its monic locator has all odd coefficients equal to zero.
   Antipodal x83 full-zero supports route to the h=4 quotient ledger.
14. The h=8 x83 support-to-trade reduction is compatible with root-scaling
    rotations, up to swapping the two recovered sides.

### Conditional but useful

1. If `H3-ACT(16)` is proved, the existing h=3 compiler gives `T_3 < n^3` for
   every `n >= 17`.
2. If the current non-diagonal rank-minor avoidance theorem and geometric
   batching theorem are proved, the h=3 official rows close through the
   `Z_budget(s)` table, with `Z_budget(13)=16` and `Z_budget(41)=10795`.
3. If the private-linear rank-minor avoidance theorem and private-linear bridge
   assignment are proved, the alternate h=3 route closes through
   `Z_private(s)`, with `Z_private(13)=23` and `Z_private(41)=15267`.
4. If a symbolic h=5 norm-gate incompatibility is proved, the current h=5
   structural reduction should close that stratum without extending the
   certificate pile.
5. If every non-antipodal h=8 n=64 x83 support is certified nonzero, or an
   equivalent sharded signature join is supplied, the current h=8 residual
   should close.

### Evidence only

1. The n=96 h=3 all-core activation bank has raw oriented per-prime maximum
   `92 < 96`, and deduplicates to `167` affine/Galois/side-swap pair-orbits
   with per-prime maximum `27 < 96`.
2. The h=5 selected-row certificate bank verifies many zero rows, including
   complete certified rows through n=128, but it is not contiguous official-row
   coverage and not a uniform theorem.
3. The h=8 n=64 radius-three shells around paid branches at `p=4289` and
   `p=262337` have `full_zero=0`, but they cover only a tiny local slice of the
   non-antipodal support universe.

### Refuted shortcuts

1. A one-curve `C h^alpha`, `alpha < 1`, rich-curve estimate is false without
   excluding constant-ratio/multiplicative-dependence cells.
2. Rational norm-coprimality is the wrong h=3 activation object; actual
   common-root activation at primitive row roots is required.
3. Private zeros and poles do not imply full coefficient-rank injectivity.
4. The private-linear multigenerator theorem cannot be obtained by naive
   factor-by-factor induction.
5. Characteristic-zero rank fullness is not enough by itself; rank-good minors
   must remain nonzero over the actual finite row field.
6. h=8 exponent-unit maps and dihedral reflection are not x83 symmetries.

## Residual gap statement

`u1_x4_direct_column_budget` remains blocked by three concrete gaps:

1. h=3: prove `H3-ACT(16)` via a finite-row-valid rank-minor avoidance theorem
   plus the matching geometric bridge/rank-capacity assignment, or replace that
   route with complete official-row certificates.
2. h=5: prove a uniform p-specific x83 norm-gate incompatibility, or design a
   certificate family that scales beyond the current left-table format.
3. h=8: close the n=64 non-antipodal x83 support branch, either by a global
   support-level certifier or by a sharded signature join that avoids the blind
   `binom(63,7)` left table.

The best next theorem-side target is h=3 rank-minor avoidance over the actual
finite row fields.  The best certificate-engineering target is h=8
non-antipodal x83 support certification.  The h=5 path should be symbolic
unless a redesigned join replaces the current table format.
