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
elapsed=55.63 maxrss=98688
```

No Modal job is required for the aggregate replay.

The h=3 repeat-boundary chain also has a focused replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_replay.py
```

Latest focused digest:

```text
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
elapsed=45.74 maxrss=53264
```

The h=3 proof surface now has a standalone frontier ledger:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
```

Expected digest:

```text
H3_FRONTIER_LEDGER_PASS
```

The T4 residual frontier also has a standalone ledger:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
```

Expected digest:

```text
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
```

## Confidence-ranked claims

### PROVED / replayed

1. h=2 has an optimized in-house rich-coset chain with
   `E(H) <= 22111 h^(5/2)`.  This covers official powers of two from
   `2^23` upward if used without the external Cochrane-Pinner import.  The
   same proof gives the affine coset-pair corollary used by the h=3
   repeat-boundary q0 and fixed-fiber packets.
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
7. The h=3 ordered-triple moment bookkeeping is exact:
   `M = trivial + 72 T_3 + repeat_residue`, with
   `trivial = 36 binom(n,3) + 9n(n-1) + n`; the repeat-entry residue is a real
   term that a moment proof must pay.  It now has the boundary reduction
   `repeat_residue <= 12 D_boundary + 18 Z_repeat`, where `D_boundary` counts
   distinct triples lying over repeated signatures.  The boundary further
   normalizes to `repeat_residue <= 12 n B_line + 18 n^2`, where `B_line` is
   an explicit four-affine-form line-pencil membership count.  The associated
   LP4 Stepanov compiler has reduced-condition gate `LP4-RED(5)`; the missing
   theorem is now the named `LP4-RANK/LP4-NV` line-pencil nonvanishing gate.
   Equivalently, active coordinate edges have the shifted reciprocal form
   `xy+xz+yz=0` for `x=u-1,y=v-1,z=w-1`, with
   `lambda=1+x+y+z in H`.  Equivalently, each active edge is the root set of
   `P_E(T)=T^3-(lambda+2)T^2+(2lambda+1)T-uvw`; singleton hitting is
   positive-degree gcd for these active cubics.
   The special triple-repeat cell `r^2+r+1=0` is already paid by the h=2
   coset-pair Stepanov corollary: `B_q0 <= 132 n^(2/3)`.  Every fixed
   non-q0 line fiber also has the h=2 cap `T_r <= 66 n^(2/3)`.  The LP4
   exception ledger records that `r in {0,-1,1,-1/2,-2}` is inadmissible for
   distinct triples, while q0 is the paid triple-repeat cell, reducing the
   remaining residue problem to an active-support bound for genuine line
   parameters.
   The genuine support is a union of six-element `S_3` Mobius orbits, so the
   support target should be stated on quotient line parameters.  The combined
   compiler says that `R_orb <= C n^beta` with `beta < 4/3` pays the repeat
   residue subcubically; a linear quotient-support theorem gives an
   `O_C(n^(8/3))` payment.  The exact integer-cap crossover for a linear
   support theorem is constant-sensitive: `C=1/4` covers `2^31..2^41`,
   `C=1/2` covers `2^34..2^41`, `C=1` covers `2^37..2^41`, and `C=2` covers
   `2^40..2^41`.
   Boundary-style finite evidence has tiny support but not emptiness:
   `B_line=0` at `n=16,32,64,128,512,1024` in the tested boundary rows, while
   `n=256,p=65537` has `B_line=48` and `R_orb=8`.  In that nonzero row, every
   active triple contains the forced coordinate `2`, and `B_line=3N_2=48`,
   suggesting a forced-coordinate/fiber support route.  The forced-fiber
   Stepanov compiler supplies `FF-RED(5)` for this route; the remaining theorem
   is its rank/nonvanishing gate `FF-RANK/FF-NV`.  Independently, the
   elementary degree bound `N_a <= 2n` proves that a forced-coordinate cover of
   size `F` gives `B_line <= 6Fn`; a sublinear forced cover would already pay
   the repeat residue subcubically.  The forced-cover crossover is strong:
   `F <= ceil(sqrt(n))` covers every official row, and
   `F <= ceil(n^(2/3))` covers `2^19..2^41`.  The canonical coordinate cover
   is measurable but too crude on the nonzero row: at `n=256,p=65537`,
   `C_coord=17`, giving a cover-bound above `n^3`.  The sharper invariant is
   the minimum coordinate hitting number `tau_coord`; on that row the active
   hypergraph has `tau_coord=1` with hitter `{2}`, giving
   `(72*1+18)256^2 < 256^3`.  The `2`-hit cell has the exact inverse-pair
   normal form `{2,v,v^{-1}}` with `v+v^{-1} in H`; in the same row this gives
   `N_2=16` and `B_line=3N_2=48`.  A fixed-`2` cover is false globally,
   however: boundary-style rows such as `(p,n)=(91393,256)` have active edges
   not hit by `2`, while still having `tau_coord=1`.  A bounded singleton
   stress scan over boundary-style rows through `n=256` found no
   `tau_coord>1`; if `tau_coord<=1` holds in the boundary regime, the repeat
   residue is at most `90n^2`, covering all official rows.  The star target
   is now reduced to an explicit obstruction: rule out four active coordinate
   edges with empty total intersection.  The obstruction extractor is not
   vacuous: the non-boundary contrast row `(p,n)=(97,32)` has
   `tau_coord=7` and a two-edge empty-intersection obstruction.  The obstruction
   target splits into two cases: disjoint active edge pairs, and
   pairwise-intersecting coreless obstructions on at most four edges.  The
   disjoint-pair case further splits into equal-`lambda` distinct active
   cubics and a quadratic-miss condition from subtracting the two cubics.  The
   equal-`lambda` case is exactly the fiber statistic
   `sum_lambda binom(K_lambda,2)`, so it is killed by injectivity of
   `E -> lambda(E)` on active boundary-style edges.  The lambda-distinct case
   is the scalar condition `rho=(m-n)/(lambda-mu)` with required hit
   `rho in {t(2-t): t in E}`.  Both are unified by
   `A_lambda(T)=T(T-1)^2+lambda*T(2-T)`: active edges are 3-point H-level
   fibers of `A_lambda`, and rho is a secant slope in the lambda direction.
   In reciprocal coordinates, the same branch is controlled by the cubic
   `X^3+(lambda-1)R X-R`: fixed-`lambda` injectivity is uniqueness of the
   reciprocal product `R`, and the rho-hit values are `1-r^-2` on reciprocal
   roots.  Equivalently, for fixed `lambda`, active edges are exactly the
   3-point fibers on `S={1/(u-1):u in H,u!=1}` of
   `Phi_lambda(r)=r^3/(1-(lambda-1)r)`.  The same-lambda target is now
   uniqueness of such a 3-point fiber for each `lambda`.  For
   `lambda != 1`, each fiber is parametrized by an ordered root ratio `z` via
   `r=(1+z+z^2)/((lambda-1)z(1+z))`; the `lambda=1` branch has only
   primitive-cube-root ratios `z^2+z+1=0`.  In the generic branch the original
   coordinates are the three rational functions
   `1+(lambda-1)z(1+z)/(1+z+z^2)`,
   `1+(lambda-1)(1+z)/(1+z+z^2)`, and
   `1-(lambda-1)z/(1+z+z^2)`, so this target is now a concrete
   three-membership problem on the ratio line.  The six ordered root ratios
   form one `S_3` orbit
   `z,1/z,-(1+z),-1/(1+z),-(1+z)/z,-z/(1+z)`, so the target is uniqueness
   of an admissible ratio orbit, with `lambda=1` handled by the primitive-cube
   scale branch.  That special branch is exactly the scale condition
   `{1+x,1+omega x,1+omega^2 x} subset H`, modulo `x -> omega x`; it has
   the combined count bound
   `K_1 <= min(floor((n-1)/3), floor(ceil(66 n^(2/3))/3))`; the h=2
   affine-coset cap first improves the trivial orbit count at `n=2^19`.  The
   resulting scale collision-pair payment is below `n^2` on every official
   row.  The strict value gate splits
   into `H3-VALUE-GEN-INJECTIVE` and `H3-VALUE-SCALE-INJECTIVE`; count routes
   can instead keep the generic strict gate and pay the scale branch
   quadratically.  Thus
   same-`lambda` failure is now exactly either two admissible generic ratio
   orbits for one lambda or two admissible `lambda=1` scale orbits.  The
   off-orbit condition is explicit: the generic diagonal divisors are
   `y-z`, `yz-1`, `y+z+1`, `y(1+z)+1`, `yz+z+1`, and `y(1+z)+z`; in the
   `lambda=1` scale branch, distinctness is `x^3-y^3 != 0`.  The
   lambda-distinct slope target also has a ratio form:
   `R^-1=-(lambda-1)^3 z^2(1+z)^2/(1+z+z^2)^3` and
   `rho=1+(R^-1-S^-1)/(lambda-mu)`, which must lie in the three source slope
   values.  This is now denominator-cleared as a factored equation
   `Q_0 Q_1 Q_2=0` for generic source ratios, with a separate scale-source
   product for `lambda=1`.
   The pairwise-coreless case further splits into a 3-edge coreless triangle
   or the tetrahedral four-3-subsets pattern.  The 3-edge coreless triangle
   further has only two combinatorial patterns: loose `(1,1,1)` and pinched
   `(1,1,2)` pair-intersection sizes.  But active edges are linear: a pair of
   coordinates determines the third, so pinched triangles and tetrahedra are
   impossible.  The only surviving pairwise-coreless obstruction is the loose
   triangle.  Equivalently, in the active-pair shadow graph, every shadow
   triangle must be contained in a single active edge.  A shadow triangle
   supported by three distinct active edges is exactly the loose-triangle
   obstruction; the contrast row `(p,n)=(97,32)` has two such triangles, so
   this target is real rather than a bookkeeping artifact.  In reciprocal
   coordinates `r=1/(u-1)`, active edges are zero-sum triples and an active
   pair `{r,s}` has forced third reciprocal coordinate `-(r+s)`.  The loose
   target is therefore equivalent to: every triangle in this reciprocal
   active-pair graph has `r+s+t=0`.  The active-pair graph itself is the
   explicit four-membership condition
   `1+1/r, 1+1/s, 1-1/(r+s), 1+1/r+1/s-1/(r+s) in H`.  A genuine loose
   triangle is equivalently a six-point system
   `r,s,t,-(r+s),-(r+t),-(s+t) in S`, with three lambda tests and
   `r+s+t != 0`.  Normalizing by `s=ar`, `t=br`, `X=1/r` turns this into
   six coordinate tests `1+X/q in H` for
   `q in {1,a,b,-(1+a),-(1+b),-(a+b)}` plus three explicit lambda tests and
   `1+a+b != 0`.  Equivalently, it is a nine-slope affine-line condition
   `1+c_i X in H`.  The normalized ratios are quotiented by the `S_3` orbit
   `(a,b),(b,a),(1/a,b/a),(b/a,1/a),(1/b,a/b),(a/b,1/b)`.  The effective
   condition count is the number of distinct slopes: the six coordinate slopes
   are distinct under the full normalized loose-system hypotheses, and the
   three lambda slopes are mutually distinct for the same genuine loose
   systems.  Remaining multiplicity loss comes only from lambda-coordinate
   collisions on nine explicit divisors, which quotient to two special
   normalized `S_3` branch types.  These branch types have one-parameter
   forms `b=a(a+1)/(a^2+a+1)` and
   `b=-(2a^2+2a+1)/(a^2+a+1)`.  The current loose-triangle interface is
   therefore a generic nine-slope target plus these two special branch targets.
   Secondary subcells inside the special branches are finite: after stripping
   structural non-poles, the residual degrees are `24` on branch A and `29` on
   branch B, so outside those loci the special branches have exactly eight
   distinct slopes.  The finite secondary loci are paid directly by the slope
   `1` condition, giving `53n < n^2` on every official row.
   The branch slope maps are explicit: branch A has eight slope maps of degree
   at most 4, and branch B has eight slope maps of degree at most 6.  Non-poles
   alone are not enough for the coordinate claim; the proof uses distinctness
   of the six reciprocal points.  The special-branch denominator compiler gives
   `S_a,S_total=(17,22)` for branch A and `(19,24)` for branch B; the generic
   two-parameter denominator compiler gives `S_a=7`, `S_b=7`, `S_total=15`.
   The loose Stepanov compiler packages these as three named missing gates:
   `LOOSE-GEN-RANK/NV`, `LOOSE-A-RANK/NV`, and `LOOSE-B-RANK/NV`.  The
   rank-minor compiler turns the strong rank form into bounded-degree
   bad-minor avoidance targets for those three gates.  The star conditional
   assembly shows that these three loose gates plus `H3-VALUE-INJECTIVE` and
   `H3-SLOPE-RATIO-HIT` imply `repeat_residue <= 90n^2` on every official row.
   The refined assembly expands the two disjoint-edge gates into
   `H3-VALUE-GEN-INJECTIVE`, `H3-VALUE-SCALE-INJECTIVE`, `H3-SLOPE-GG-HIT`,
   and `H3-SLOPE-MIXED-HIT`, while keeping the scale-pair and loose-secondary
   payments separate from the strict `tau_coord<=1` route.  The frontier
   ledger now replays these seven strict branch gates plus the paid ledgers as
   one consistency checkpoint.
   The same-lambda orbit-domain and degree compilers now give the
   `H3-VALUE-INJECTIVE` collision budgets: generic `S_total=14` plus
   off-orbit product total degree `10`, and lambda-one scale `S_total=6` plus
   scale exclusion `x^3-y^3 != 0`; the scale branch also has the combined
   trivial/h=2 affine count-payment route.
   The slope-miss degree compiler now gives the generic `H3-SLOPE-RATIO-HIT`
   miss budget: six membership maps with `S_total=14`, and cleared hit
   numerator factors of total degrees `15,13,13`.  The mixed generic/scale
   branch has six membership maps with `S_total=10`; orienting the generic edge
   as source gives three hit factors of total degree `9`, hence mixed
   hit-product total degree at most `27`.  Thus the slope gate splits into
   `H3-SLOPE-GG-HIT` and `H3-SLOPE-MIXED-HIT`; scale-scale is impossible for
   lambda-distinct pairs.
   A full-degree-space shortcut for LP4 affine factors is false already in a
   two-factor rational model, so the rank gate must be proved in its weaker
   threshold form or bypassed by support/incidence arguments.
8. The h=3 dilation-normalized activation count lifts to at most `n` raw
   shape pairs per orbit; side-swap stabilizers only reduce the lift size.
9. Nondegenerate h=3 conic charts have no internal constant-ratio collapse
   among `U,V,W`; the remaining constant-ratio danger is confined to excluded
   or separately paid degeneracy cells.
10. The affine conic chart counts all ordered same-fiber `H`-triples except
   possibly one vertical/projective point, so local ordered fibers satisfy
   `R = T_chart + epsilon`, `epsilon in {0,1}`.
11. Changing the base point on a nondegenerate same-fiber conic changes the
    parametrization, not the geometric conic image or the recovered ordered
    `H`-triple ledger.  The bridge should count one conic fiber, not one curve
    image per ordered triple.
12. The h=3 pair-count compiler is exact locally:
    `P_z = binom(R_z/6,2) = R_z(R_z-6)/72`.  The native bridge target is the
    exact L2/level-set ledger `sum R_z(R_z-6) <= 1152 n`; the older chart
    ledger condition `(M+1)(S+Z) <= 1152 n` is only a convenient corollary
    from `sum R_z^2 <= max(R_z) sum R_z`.
13. The rich-curve denominator compiler and log-jet reduction are banked.  The
   reduced-condition side is now `RC-RED(13)`.
14. Several h=3 rank guardrails are proved or replayed:
   constant-ratio collapsed rank, small-`H` failure, one-factor private-linear
   rank, two-factor failure of naive induction, finite-row bad-prime rank drop,
   generic-open rank-minor formulation, and normalization invariance including
   source Mobius reparametrizations.  The private-linear route can now be
   posed in the three-parameter PGL2 normal form
   `Y, (Y-1)/(Y-lambda), (Y-eta)/(Y-theta)`, with the repaired open set given
   by `lambda,eta,theta notin {0,1}` and pairwise distinct.  In this chart,
   every `r x r` rank minor has total parameter degree at most
   `2rH(B-1)`.
15. The h=3 arithmetic interfaces now cover every official row.  The current
   non-diagonal route is:
   `F3-RANK-AVOID + H3-BRIDGE-RANKCAP(Z_budget(s)) => H3-ACT(16)`.
   The active `Z_budget` table is the non-diagonal one, with range
   `16..10795`; the older diagonal bridge-budget table is only a legacy lower
   bound with range `11..7420`.
   The private-linear alternate route is:
   `F3-PRIVATE-LINEAR-RANK-AVOID + H3-BRIDGE-PRIVATE-RANKCAP(Z_private(s)) => H3-ACT(16)`.
16. h=5 has been structurally localized.  Since `5` is not dyadic, the
   char-zero dyadic branch is excluded; every remaining survivor must be a
   p-specific x83 norm-gate event.  The h=5 x83 low obstruction keys are now
   compiled into a triangular system
   `D_j E_j = -D_j l_j + P_j(l5,...,l9)`, giving exact per-key
   norm-divisor bounds and reciprocal high-coefficient equations for the
   remaining branch.  Eliminating the shared support product `delta` now gives
   three pairwise delta-free compatibility equations plus the central
   `l5=delta*bar_l5` compatibility row, four equations total with max total
   degree `10`.  The base-free version is the full rank-one compatibility
   system: ten pairwise equations among `E1,E2,E3,E4` and the central row,
   again with max total degree `10`.  The all-zero high-coefficient chart is
   excluded on official rows: it would force a locator `X^10+l0`, impossible
   for a 10-support in `mu_{2^s}` because `x -> x^10` has fibers of size at
   most `2`.  Since the support product has unit norm, four additional
   Hermitian equations `P_j conjugate(P_j)=D_j^2 l(10-j)bar_l(10-j)` are now
   compiled, with max total degree `18`.  Chart-local recovery reduces the
   target to four incident rank-one minors plus one matching Hermitian equation
   on charts `1..4`, and only four incident minors on the central chart because
   `l5/bar_l5` has unit norm identically.  The central claim is verified by
   saturated identities `l5*N_i in <C_i5,conjugate(C_i5)>`; an abstract
   rank-one identity gives 20 unit-propagation syzygies across all charts, and
   a second identity gives 30 minor-propagation syzygies showing that four
   incident minors imply all ten pairwise minors after chart saturation.  The
   central chart is the smallest local target: four equations, 67 total terms,
   and max degree `10`.  On that chart the four equations are linear in
   `bar_l9,bar_l8,bar_l7,bar_l6` respectively, giving an explicit rational
   graph after saturation by `l5*bar_l5`.  The fixed-point skeleton shows that
   direct expanded conjugation is too large: the pre-cancellation term bound is
   up to `1,255,488,415,957`.  The reciprocal system is homogeneous for the
   natural root-scaling weights; all unit rows have weight zero.  The central
   weighted-slice compiler now permits the algebraic emptiness slice
   `l5=bar_l5=1`, reducing the central graph max degree from `10` to `9`
   without treating it as an official row quotient.  On that slice the
   fixed-point degree bounds drop from `91,81,71,61` to `81,72,63,54`, but the
   expansion-size bounds remain prohibitive.  The slice tangent compiler adds
   a local normal form: the graph tangent is the `1/2` anti-diagonal map, so
   the relaxed fixed-point equations have linear part `3/4 I` and determinant
   `81/256`.  This proves only that the normalized origin is a simple local
   fixed point away from characteristics `2,3`; it is not a global h=5 closure.
   On official rows the central chart has a free finite `mu_n` scaling action
   because `bar_l5` has weight `-5` and `gcd(5,2^s)=1`.
17. h=8 has an intrinsic antipodal split: a 16-support in `mu_64` is antipodal
   if and only if its monic locator has all odd coefficients equal to zero.
   Antipodal x83 full-zero supports route to the h=4 quotient ledger.
18. The h=8 x83 support-to-trade reduction is compatible with root-scaling
    rotations, up to swapping the two recovered sides.  The non-antipodal
    residual has no periodic rotation subcase: every non-antipodal orbit is
    aperiodic, and the anchored count is exactly `16` times the orbit count.
    The residual is therefore `7,633,233,227,520` aperiodic support orbits.
    Exponent-unit maps and reflection remain refuted as x83 symmetries.

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
   should close.  With only proved rotation canonicalization, the support-first
   target is `7,633,233,227,520` aperiodic non-antipodal orbits.

### Evidence only

1. The n=96 h=3 all-core activation bank has raw oriented per-prime maximum
   `92 < 96`, and deduplicates to `167` affine/Galois/side-swap pair-orbits
   with per-prime maximum `27 < 96`.
2. The h=5 selected-row certificate bank verifies `589` complete zero rows and
   `3,164,030,779` audited right-side probes.  It is contiguous for n=32
   through `p=65537`, but the n=64 bank still misses `515` admissible primes up
   to its largest certified prime, so it is not official-row coverage and not a
   uniform theorem.
3. The h=8 n=64 radius-three shells around paid branches at `p=4289` and
   `p=262337` have `full_zero=0`, but they cover only a tiny local slice of the
   non-antipodal support universe.
4. The h=3 repeat-boundary support is tiny on tested boundary-style rows:
   `B_line=0` for `n=16,32,64,128,512,1024`, and `B_line=48` at the nonzero
   guardrail row `n=256,p=65537`; the nonzero row is fully explained by the
   forced coordinate `2`.

### Refuted shortcuts

1. A one-curve `C h^alpha`, `alpha < 1`, rich-curve estimate is false without
   excluding constant-ratio/multiplicative-dependence cells.
2. Rational norm-coprimality is the wrong h=3 activation object; actual
   common-root activation at primitive row roots is required.
3. Private zeros and poles do not imply full coefficient-rank injectivity.
4. The private-linear multigenerator theorem cannot be obtained by naive
   factor-by-factor induction.  The first two-factor loss is structural: a
   bidegree `(2,2)` resultant relation explains the exact rational rank drop
   from `9` to `8` at `A=1,B=3,H=2`.  The same resultant obstruction is outside
   every official private-linear box because all those boxes have `B-1 < H`;
   in fact the passing boxes satisfy `max(A,D,B-1)<H` with margin at least
   `7904`.
5. Characteristic-zero rank fullness is not enough by itself; rank-good minors
   must remain nonzero over the actual finite row field.
6. h=8 exponent-unit maps and dihedral reflection are not x83 symmetries.
7. The h=3 repeat-boundary support is not identically zero on boundary-style
   rows: `n=256,p=65537` has `B_line=48`.

## Residual gap statement

`u1_x4_direct_column_budget` remains blocked by three concrete gaps:

1. h=3: prove `H3-ACT(16)` via a finite-row-valid rank-minor avoidance theorem
   plus the matching geometric bridge/rank-capacity assignment, including the
   exact L2 or level-set control needed by the pair-count compiler; or replace
   that route with complete official-row certificates.
2. h=5: prove a uniform p-specific x83 norm-gate incompatibility, or design a
   certificate family that scales beyond the current left-table format.
3. h=8: close the n=64 non-antipodal x83 support branch, either by a global
   support-level certifier or by a sharded signature join that avoids the blind
   `binom(63,7)` left table.

The best next theorem-side target is h=3 rank-minor avoidance over the actual
finite row fields.  The best certificate-engineering target is h=8
non-antipodal x83 support certification.  The h=5 path should be symbolic
unless a redesigned join replaces the current table format.
