# Proximity Prize deferred compute requests

This ledger records computations whose outputs could close or decisively
reshape a named proof branch but whose conservative cost exceeds the current
sub-`$1` Modal policy. It is suitable for contributor requests and upstream
PR notes. Entries are not theorem claims, and partial runs are evidence only.

Every request must specify the mathematical decision, completeness boundary,
certificate format, deterministic checker, resource estimate, and effect of
both outcomes on the critical DAG. Shallow sweeps without a named decision do
not belong here.

> **MAINTAINER GOVERNANCE NOTE (2026-07-20, wave-17 integration — UNRATIFIED).**
> The sub-`$1` Modal self-authorization clause remains maintainer-unratified
> (standing item w16-C5). Wave-17 is the **first wave to actually exercise it**:
> three in-tree Modal launches were imported from the resolution branch, each a
> no-hit exclusion screen whose `result.json` is now **load-bearing for a PROVED
> node's `verify.py`** (via a local coverage/hash certificate checker; no local
> re-execution of the 2–4M-modulus search):
>
> | app_id | screen | ceiling | candidates/shards | hits | consuming PROVED node |
> |---|---|---|---|---|---|
> | `ap-6KQ2mJjoE3Qkq7VaKqnxlZ` | c1-parity-antiinvariant | `$0.25` | 2,247,721 / 16 | 0 | `…c1_parity_frobenius_router` |
> | `ap-Js6Im9DeoBlc0di05YG2WE` | c1-parity-harmonic-characteristic | `$0.50` | 4,495,441 / 32 | 0 | `…c1_parity_harmonic_exclusion` |
> | `ap-PVTrzkKlh4j1B6qDmGU1Wf` | harmonic-top (order 2^41) | (none stated) | 2,247,720 / 16 | 0 | `…matched_post_field_compiler` |
>
> The three nodes are wired **ev-only** into `rate_half_list_adjacent_crossing`
> (still TARGET); no red flipped on their account. Each cert checker trips under
> a fault-injection mutation (audit control M4). **Open maintainer decision
> (w17-C1):** whether to accept remote no-hit screens under a local coverage
> certificate as PROVED evidence, and whether to ratify the sub-`$1` self-auth
> policy that permitted the launches. Recorded here; not auto-adopted.

## Request queue

| priority | request | readiness | contributor action | current authorization |
|---|---|---|---|---|
| P1 | CR-002 fiber-four rank-two classification | ready for a capped exact symbolic pilot; official scalar batch deferred pending a fast quotient-algebra evaluator | attack six trace-eliminated Gegenbauer/Chebyshev gcds, then the ODE gcd and exact fourth-power gates | external request only; cost unknown |
| P2 | CR-001 H3 high-excess certificate | blocked on an efficient official-scale template generator | derive sparse distance-six or nonzero-coupling ideal templates before benchmarking | no large run |
| P3 | CR-003 rate-half Hankel sharp-cap census | ready for an external exact pilot | run the printed small analogues through the deterministic incidence gate and price the first complete chamber | external request only; cost unknown |

Priority records expected proof value, not an instruction to spend. A request
remains unauthorized until a contributor accepts its resource cap. If a PR
cannot vendor the proved router, the checker, and the PASS/FAIL DAG contract,
it should link this ledger as future work rather than solicit the computation.
Cost estimates are conservative ceilings and must include failed shards and
retries; raw artifact storage is separate.

## Upstream handoff convention

When one of these requests is included in a PR to Przemek's repository, copy
the request as a **compute request**, not as evidence for a theorem. The PR
should also include:

1. the proved router that makes the computation complete for its stated
   scope;
2. the smallest reproducible pilot and its measured cost;
3. a resumable remote launcher with an explicit cost or resource ceiling;
4. a streaming, independently runnable certificate checker;
5. the exact DAG change authorized by PASS, FAIL, and incomplete outcomes.

Large raw artifacts should remain in contributor-controlled remote storage.
The PR should vendor compact manifests, hashes, certificates, and checkers.
An incomplete run may sharpen the request or expose a counterexample, but it
must not change a mathematical node to `PROVED`.

Requests are added only after algebraic preprocessing has made the search
space auditable. At present CR-001, CR-002, and CR-003 are the only large runs
meeting that bar; the other open critical lanes still need theorem-level
compression before a large computation would be responsible.

The XR high-core lane now has an arbitrary-rank uniform-cell Maxwell/trade
reduction, but it still has no complete finite template generator for
trade-rank-at-least-three cores and no nonuniform-cell coverage theorem.
Accordingly there is no XR large-run request yet. A raw Maxwell-core or block-
family search would not certify the aggregate slope target and should not be
sent to contributors as a compute task.

## CR-001: H3 fixed-order high-excess / double-accident certificate

- **status:** BLOCKED ON AN EFFICIENT OFFICIAL-SCALE ALGEBRAIC TEMPLATE
  GENERATOR. The complete toy-order benchmark is done; do not launch a raw
  orbit fleet.
- **consumer:** `f3_h3_mobius_excess_half` (C36').
- **proved router:** `f3_h3_low_distance_ideal_star_router`, strengthening
  `f3_h3_low_distance_exceptional_prime_router`; the proved
  `f3_h3_ideal_star_prime_alignment_criterion` supplies the exact fixed-root
  sieve once candidate primes are available. The stronger proved
  `f3_h3_weighted_multistar_router` is the selected final sieve: a candidate
  fiber must contain a center of distance-deficit weight at least four. The
  proved `f3_h3_excess_multistar_degree_ladder` raises this threshold with
  `e=P-18`; degree four is confined to the boundary profiles
  `(P,D)=(19,1),(20,2)`. The proved
  `f3_h3_excess_budget_degree_tradeoff` pays `P<=32` analytically and forces
  center weight at least twelve on the selected residual. The proved
  `f3_h3_high_excess_low_distance_moment_reduction` and
  `f3_h3_low_distance_quotient_incidence_router` identify the exact
  certificate currency as a low-distance edge–quotient moment. The proved
  `f3_h3_distance_four_fiber_degree_cap` and
  `f3_h3_high_excess_distance_six_moment_reduction` then remove the
  distance-four term completely. The cap now canonically orients the generic
  graph with indegree at most one, so the generic distance-four graph is a
  pseudoforest rather than merely maximum-degree three. The proved
  `f3_h3_distance_six_support_overlap_payment` also removes every
  support-overlapping distance-six stratum from the direct analytic route.
  The proved `f3_h3_disjoint_distance_six_split_pencil_router` then rewrites
  the residue as a quadratic split-pencil / affine subgroup-line
  correlation with an exact integral certificate target.
- **proved double-accident alternative:** the joint-ideal router targets
  `Y_18` rather than all rich product fibers. Its nonzero-coupling refinement
  removes the second quotient lift from coarse template generation. Each
  positive summand supplies one quotient anchor with nonzero `lambda` and the
  normalized ideal

  ```text
  K^NZ=( (beta_F-beta_E)/pi^2,
         (beta_G-beta_E)/pi^2,
         (beta_EC-D)/pi ).
  ```

  For fixed product center, at most one quotient lift has zero coupling;
  `R(t)>=2` therefore supplies at least `R(t)-1` nonzero generators. The zero
  locus is exactly `{x,y,z}={q,-q,-q^2}`, `w=q^4`, so it is removed by an
  exponent-pattern test. The official row prime divides `N(K^NZ)`. Every
  prime outside the finite nonzero-coupling candidate set has `Y_18=0`, hence
  satisfies C36'. On survivors, reconstruct the complete quotient fiber and
  enlarge the ideal by all nonzero couplings. The proved odd-saturation
  syzygy shows this symmetric batch is exact at every odd row-prime ideal;
  separate quotient-collision generators are redundant. The product-direction
  identity similarly removes the product-collision generator type: after
  inverting two, one coupling row and column generate the complete
  product-by-quotient rectangle. Intersecting
  unrelated product-prime and quotient-prime unions does not certify common
  target or common prime-ideal alignment.
- **first official order:** `n=8192`; later orders only after a symbolic
  template or candidate-prime generator makes this first order credible.
- **decision:** determine every official row that can support `P(t)>=33` by
  generating the relevant weight-twelve multistar prime union, then prove

  ```text
  17 sum_(t!=1,P(t)>=33)(P(t)-18)R(t)
    <=300n^2-238(n-1)(n-2).
  ```

  The proved low-tail payment then gives C36' for the complete fixed-`n`
  scope. A violation refutes C36'; positive but safe rows identify the actual
  high-excess geometry.
- **exact moment interface:** it is enough to certify only

  ```text
  M_6,33=sum_(P(t)>=33)N_6(t)R(t),
  136M_6,33<=21(300n^2-238(n-1)(n-2)).
  ```

  This is conservatively `M_6,33<(651/68)n^2<9.574n^2`. A certificate may
  prove this moment without enumerating every candidate prime if it uses the
  exact canonical incidence router.
- **raw single-norm route fence:** a proved restricted-family count gives
  `2,173,296,943,108` unordered low-distance pair-pairs and at least
  `530,590,075` Galois/exchange orbits at `n=8192`. Distance six is generic for
  disjoint norm-three supports. The principal-prime union remains a complete
  outer envelope, but enumerating and factoring those raw orbits is not the
  requested implementation.
- **proved algebraic filter:** distance-two collision norms are powers of two
  and cannot contribute an odd candidate prime. Candidate generation is
  restricted to squared distances four and six; the rich seven-vector graph
  has at least six such low edges.
- **distance-class pilot:** Modal app `ap-nFVftE3yG19HwOwPvjIehP` completed
  both toy orders below `$0.001` in requested-resource function time.
  Distance-four relevant factors number `4` and `67`, while distance-six
  factors number `103` and `2,127`. A larger raw census is not requested;
  distance four should be classified as a four-term sublane and distance six
  remains the generic algebraic generator problem.
- **proved distance-four router:** the generic lane is already reduced to
  `uv=-y` and `x=(u^2-y)/(u(1-y))`; the antipodal lane is
  `x^2=u+v-uv`. Any contributor implementation must use these two-variable
  forms rather than enumerate four exponents. Their proved global ledger is
  `N_4<=(3n^2+n)/2`. Fiberwise, choose one valid cross-overlap orientation
  per generic edge: the head determines the tail uniquely, giving at most
  `g` generic edges and `N_4(t)<=g+ag<=2(m-1)` including the unique possible
  antipodal representation. On antipodal-free fibers `N_4(t)<=m`.
- **required preprocessing:** derive the complete relevant prime union for
  multistars of incident weight at least twelve without enumerating raw
  collision orbits. A complete principal collision-prime list is a valid but
  deliberately overbroad fallback. Distance four must use its two-variable
  routers; distance six needs a sparse cyclotomic norm-template, resultant,
  or equivalent algebraic generator with a proved coverage map under odd
  Galois dilation and pair exchanges. The selected final sieve is weighted
  common-prime alignment, not rational gcd or ideal normal form.
  For the double-accident alternative, derive orbit-complete templates for
  the three-generator `K^NZ` ideals under odd Galois dilation, internal
  product-pair exchange, and leaf exchange. Retain one distinguished quotient
  anchor and exclude zero coupling by the proved telescoping exponent test.
  The template manifest must retain `(beta_EC-D)/pi`; deleting it admits
  unrelated product and quotient targets and invalidates coverage of `Y_18`.
  The exact survivor checker must then reconstruct `R(t)` and the complete
  `R(t)-1`-or-larger nonzero coupling batch. No second quotient coordinate is
  needed in the coarse symbolic template, and no separate quotient-collision
  template family is needed in the exact batch. Replay
  `c_(u_0)lambda_1-c_(u_1)lambda_0=-theta_01` and
  `lambda_(i,j)-lambda_(0,j)=pi^2c_(u_j)alpha_i` as cross-checks. On an exact
  survivor, store and factor one coupling cross; reconstruct but do not factor
  the full rectangle.
- **analytic alternative:** the canonical edge–quotient router writes the
  remaining distance-six records as four free subgroup variables with two
  rational subgroup-membership tests. A constants-explicit point-count proof
  of the exact moment interface is a complete substitute for the prime-union
  generator; no distance-four incidence bound is required. The sharper split
  target is

  ```text
  136(42M_6,33^0+53M_6,33^A)
    <=1113(300n^2-238(n-1)(n-2)),
  ```

  or conservatively
  `M_6,33^0+(53/42)M_6,33^A<(1643/136)n^2<12.081n^2`.
  Here the antipodal-free lane has two membership tests and the relatively
  weighted antipodal lane has three. This is the preferred analytic target.
  A contributor proving a direct incidence theorem may instead target either

  ```text
  4(10M_6,25^0+17M_6,25^A)<=5B_(n,6),
  17(8M_6,29^0+11M_6,29^A)<=22B_(n,10).
  ```

  Their conservative allowances are `24.75n^2` and `(715/34)n^2`, but their
  filters are only `P>=25` and `P>=29`. These are analytic alternatives, not
  authorization to weaken the fixed-order request: its `P>=33` threshold
  forces the degree-twelve weighted screen that makes candidate generation
  credible.

  The preferred direct-incidence request is sharper still. On the `E=6`
  interface, exact quotient mass pays both cubic overlapping generic families
  and the two antipodal-edge families. It is enough to prove

  ```text
  D_6,25^0+(17/10)D_6,25^A <=(223/20)n^2,
  ```

  where every retained edge has six disjoint signed atoms. A contributor
  point-count argument should impose this disjointness from the outset. The
  exact normalized implementation is as follows. For each target `t`, split

  ```text
  Q_(t,r)(X)=X^2-(1+r-t)X+r
  ```

  over `H` as `r` varies in `H`; pairs of generic split members with disjoint
  signed supports are precisely the retained distance-six edges. The quotient
  weight is the affine line fiber
  `#{z in H\{1}:1-t(1-z) in H\{1}}`. If `J_25^0,J_25^A` are the raw ordered
  record totals before canonical orientation, the requested inequality is

  ```text
  10J_25^0+17J_25^A <=892n^2.
  ```

  The factor eight is exact. As an algebraic cross-check, every split-member
  pair `r!=s` must satisfy
  `(X-r)Q_(t,s)-(X-s)Q_(t,r)=t(s-r)X`. This is a `cX` shift, not a
  constant-shift top-stratum test.
- **bounded pilot:** Modal app `ap-J4kT8st6P45yWvWZtc2Xgi` completed the full
  `n=32` orbit/norm census and an `n=64` scaling sample for below `$0.001` of
  requested-resource function time. Exact-norm equality compressed `5,216`
  orbits to `227` norms at `n=32`, but the first `5,000` `n=64` orbits already
  yielded `2,567` norms. Therefore simple norm deduplication does not satisfy
  the preprocessing gate. It predates the ideal-star selector and should not
  be extended.
- **bounded ideal-star pilots:** Modal app `ap-yiFl4ymMCORN2txyqtXONi`
  completed the normalized principal-gcd screen. It removed no relevant
  primes (`103 -> 103` at `n=32`, `2,127 -> 2,127` at `n=64`) and counted
  `24,407,583` and `2,569,691,591` raw rooted stars. Modal app
  `ap-InR5xZAak4rOrjhrEUWIIZ` then tested exact common-prime-ideal alignment
  without star enumeration. It compressed `103 -> 18` and `2,127 -> 162`.
  Both complete campaigns cost below `$0.001` in requested-resource function
  time. This selects prime-ideal alignment and rejects rational gcd screening.
- **bounded weighted-multistar pilot:** Modal app
  `ap-jU9q1eWAaOiRkg3sqZForL` applied the stronger exact sieve to those
  aligned lists. It compressed `18 -> 4` at `n=32` and `162 -> 67` at
  `n=64`, or `103 -> 4` and `2,127 -> 67` from the principal-prime lists.
  The two functions used `0.289` and `5.825` seconds and cost below `$0.001`
  in requested-resource time. Future contributor implementations should test
  weighted degree, not merely two incident low-distance edges. Both toy orders
  have empty `P>=19` loci, so they also have empty selected `P>=33` tails; the
  pilot measures implementation compression rather than degree-twelve scale.
- **known rich-fiber check:** on both exact rich fibers at
  `(n,p)=(8192,67657729)`, one center has nine distance-six leaves and the
  first two normalized collisions generate the prime ideal itself. This
  demonstrates the intended ideal compression on known positives. These
  fibers have `P=20`, so the `E=14` theorem pays them before the requested
  high-excess computation; they are not positive degree-twelve examples.
- **screen after preprocessing:** for each candidate prime, fix one primitive
  `n`th root and enumerate each squared-norm-at-most-three unordered shifted
  pair once. Group products by value and retain the prime only if some fiber
  has `P>=33` and meets its excess-dependent incident-distance threshold
  `L(7+ceil((P-18)/2))`, with distance four weighted two and distance six
  weighted one. The minimum threshold is twelve. Galois invariance makes one
  root complete; no rooted-star enumeration is required.
  On the double-accident alternative, retain a candidate only when the exact
  row has a target with `P>=19`, `R>=2`, an admissible low-distance star, and
  a nonzero coupling anchor. Reconstruct every quotient lift on that target
  and verify that at least `R-1` couplings are nonzero and lie in the same
  degree-one prime ideal as the star. Across all `U(t)` unordered products,
  verify the coupling rectangle has at least
  `U(t)R(t)-min(U(t),R(t))` nonzero entries and is reconstructed from its
  stored row/column cross.
- **arithmetic:** certify every odd generated factor with `p=1 mod n` and
  `p>=n^2`, run the weighted screen, and compute exact
  `P(t),R(t),N_6(t)` and high-tail moment totals for each survivor. For an
  analytic-route census, stream the split parameters and line fibers per
  target and return `J_25^0,J_25^A` separately; do not retain all raw tuples.
- **required certificate:** algebraic template manifest and coverage count;
  normalized principal-norm hashes; complete relevant-factor and primality
  certificates; fixed-root subgroup certificates; compact weighted-screen
  summaries; per-prime histogram summaries; and a product/remainder witness
  proving that no relevant factor was omitted. A double-accident certificate
  must also include the zero-coupling exponent-pattern exclusions, nonzero
  coupling-norm hashes, target-local `R-1` batch counts, and odd-saturation
  syzygy hashes. Exact survivors must include coupling-cross hashes, matrix
  dimensions, partial-matching zero locations, and a reconstruction hash for
  the full rectangle.
- **checker:** a small streaming verifier must validate template coverage,
  normalized principal norms, factor certificates, subgroup order, the
  excess-dependent weighted-degree screen, histogram totals, the exact
  edge–quotient moment and high-tail inequalities above, the factor-eight
  orientation identity, the `cX` cubic cross-check, and their composition with
  the proved low-tail payment without retaining the full data set in RAM. On
  the double-accident route it must independently replay the telescoping zero
  test, nonzero anchor congruence, complete quotient batch, normalized-factor
  2-power norms, both coupling syzygies, partial-matching zero bound, and
  cross-to-rectangle reconstruction before applying the `Y_18` reduction.
- **execution shape:** benchmark a tiny order first; shard orbit classes;
  checkpoint completed classes and factors; store large artifacts remotely;
  return only manifests and compact certificates. Do not materialize all raw
  pair-pairs or return them to WSL. Do not factor every coupling-rectangle
  entry: `(CM5)` proves that the stored cross has the same odd-local ideal.
- **stop conditions:** do not enumerate rooted stars. Stop if the algebraic
  candidate generator, unfactored cofactors, or measured cost makes a complete
  fixed-order certificate implausible. Bank the partial template/factor
  manifest, but do not describe it as fixed-order coverage.
- **estimated resources:** deliberately unpriced pending a contributor
  benchmark. It is expected to exceed the local `<$1` allowance and must not
  be launched here without a new explicit budget.

This request is stronger than extending the existing first-prime or raw-norm
sweeps and narrower than certifying every `P>=19` candidate. Its eventual
completeness follows from the proved low-distance, weighted-multistar, and
excess-budget routers, but it is not yet an executable official-order job.

## CR-002: Fiber-four `K_4` rank-two component classification

- **status:** READY FOR EXACT SYMBOLIC CONTRIBUTOR COMPUTE; do not replace it
  with an official-field point sweep.
- **consumer:** `rate_half_list_adjacent_crossing`.
- **proved router:** `rate_half_list_budget_three_fiber_four_rank_gate`.
  The known antipodal component is already descended and welded by
  `rate_half_list_budget_three_fiber_four_antipodal_descent` and
  `rate_half_list_budget_three_antipodal_mobius_weld`. The follow-on
  `rate_half_list_budget_three_antipodal_primitive_quotient_gate` proves that
  its official residual is neither a dyadic cyclic/dihedral pullback nor the
  direct four-coset deletion partition. The reverse-contact theorem
  `rate_half_list_budget_three_antipodal_pencil_degree_floor` further proves
  that the monic pencil's degree-drop direction has degree at least
  `2^36-2`. On the centered pure-quartic stratum `e_2=e_3=0`, the Wronskian
  refinement `rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity`
  proves the exact degree `v=2^37-2`. The differential refinement
  `rate_half_list_budget_three_antipodal_reverse_residual_stratification`
  proves that `T=dDU-Y(D'U+4DU')` has exact degree
  `r+4-q(r-v)`, where `q` is the first nonzero centered coefficient.
- **deleted-pair final router:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_scalar_router`.
  After the constant ODE, Mobius router, Euclidean reconstruction, and
  harmonic exclusion, it removes `q_out` from the search. For the three
  printed pairs `(a_j,b_j)`, completion is exactly

  ```text
  4b_jT=a_jS^2,
  y=4b_j/a_j-2,       y notin {2,-2},
  y_(m+1)=y_m^2-2,       y_38=2,
  S/(1+q_out) is a nonzero square,       X^2-yX+1=0.
  ```

  The final square verdict is invariant under
  `q_out<->q_out^(-1)`. A contributor should implement three one-variable
  certifiers in `r`, not a two-variable torsion search.

  The stronger proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_fourth_power_router`
  removes even that root-independent `q_out` square verdict. With
  `chi=r+r^(-1)`, the three multipliers are the explicit squares

  ```text
  h_0^2=1/(4(chi-1)^2),
  h_1^2=(chi-2)^2/(4(chi+2)^2),
  h_2^2=chi^2/(4(chi-4)^2).
  ```

  Conditional on `T=(h_jS)^2`, the final square-pencil condition is exactly
  that `T` is a nonzero fourth power. This is the implementation endpoint.

  The first implementation stage begins with the proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_gate`,
  but its terminal quotient has now been eliminated by the stronger proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_legendre_collapse`.
  Define

  ```text
  H_n(t)=[z^n]((1-z)(1-tz))^(-1/2),       H=H_(4M-1)(t).
  ```

  Then `sigma=S(0)=2H`, and the three first-rejection gates are exactly

  ```text
  t H^2+(chi-1)^2=0,
  t(chi-2)^2H^2+(chi+2)^2=0,
  t chi^2H^2+(chi-4)^2=0.
  ```

  The sequence has the width-two recurrence

  ```text
  2(n+1)H_(n+1)=(2n+1)(1+t)H_n-2ntH_(n-1)
  ```

  and, for `t=r^4`, the Legendre form
  `H_n(r^4)=r^(2n)P_n((r^2+r^(-2))/2)`. A contributor should attack uniform
  torsion nonvanishing or provide a coverage-proved fast holonomic,
  diagonal, or cyclotomic-resultant evaluator. Do not reconstruct `R,S,T`,
  and do not iterate `2^37-1` recurrence steps for each torsion point.

  **Deferred large run CR-002-L (recorded for contributor compute).** Put
  `n=4M-1=2^37-1` and

  ```text
  K_n(t)=4^nH_n(t)
        =sum_(j=0)^n binom(2j,j)binom(2n-2j,n-j)t^j.
  ```

  After clearing the `r` and power-of-four denominators, the three branch
  polynomials are

  ```text
  B_0(r)=r^6K_n(r^4)^2+4^(2n)(r^2-r+1)^2,
  B_1(r)=r^4(r-1)^4K_n(r^4)^2+4^(2n)(r+1)^4,
  B_2(r)=r^4(r^2+1)^2K_n(r^4)^2
         +4^(2n)(r^2-4r+1)^2.
  ```

  The exact decision is whether any admissible official split-quadratic
  characteristic `p`, source order `ord(r)|2^40`, and branch `j` has
  `B_j(r)=0`, after applying the already proved distinctness, primary-gap,
  and characteristic filters. A negative result closes the scalar-gate
  portion of the generic deleted-pair sublane. A positive result must emit
  `(p,ord(r),j)` and the minimal common factor, then pass the existing full
  scalar, trace, gcd, and fourth-power checkers before it counts as a
  survivor.

  Source torsion must be inside the elimination ideal, not applied as an
  informal post-filter. The proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_primary_legendre_torsion_necessity_fence`
  gives one exact good-characteristic `M=1` primary-gap solution for each
  `B_j`; every row retains the required nonzero next coefficient, and every
  row fails `r^32=1`. Thus the pairwise primary/`B_j` resultant has genuine
  large-prime false-route hits. A contributor output that omits
  `r^(32M)-1` does not answer CR-002-L.

  The preferred lower-degree implementation is the proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_chebyshev_gegenbauer_sign_router`.
  Put `L=2M`, `y=(r+r^(-1))/2`, `x=2y^2-1`, and
  `epsilon=r^(8L)`. The coverage-equivalent system is

  ```text
  T_(8L)(y)=epsilon,       epsilon^2=1,
  C_L^(1/4)(x)=0,
  ```

  followed by one of

  ```text
  P_(2L-1)(x)=s(2y-1),
  P_(2L-1)(x)(y-1)=s(y+1),
  P_(2L-1)(x)y=s(y-2),       s^2=-epsilon.
  ```

  There are two sign choices in each line. These six unsquared systems are
  an exact intermediate endpoint; they retain source torsion and reduce the
  branch degree relative to `B_j(r)`.

  Apply the stronger proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_trace_gcd_router`
  before an official computation. Since `t!=1` forces `x^2!=1`, replace the
  torsion equation by

  ```text
  epsilon=-1: G_epsilon=T_(2L),
  epsilon= 1: G_epsilon=U_(2L-1).
  ```

  Put `C=C_L^(1/4)` and `R=P_(2L-1) mod C`. For each `s^2=-epsilon`, the
  three branch polynomials are

  ```text
  E_(0,s)=(R+s)^2-2s^2(x+1),
  E_(1,s)=2(R+s)^2-(x+1)(R-s)^2,
  E_(2,s)=(x+1)(R-s)^2-8s^2.
  ```

  Reduce `G_epsilon` and `E_(j,s)` modulo `C`. The exact official decision
  is now whether any of the six gcds

  ```text
  gcd(C, G_epsilon mod C, E_(j,s) mod C)
  ```

  is nontrivial in an admissible characteristic. Every representative has
  degree at most `L=2^36`. A PASS must provide compact Bezout or subresultant
  certificates for all six signs and every official characteristic class. A
  FAIL must print the common factor, reconstruct `y` using `(TGR6)`, and then
  replay the retained next-coefficient and downstream filters. A contributor
  may use the larger cleared `r`-polynomials as an independent checker, but
  should not make them the primary official-scale representation without a
  measured reason.

  A responsible implementation should work by power-of-two cyclotomic
  norms/subresultants or a comparably coverage-proved batch algorithm. It
  must emit compact Bezout, subresultant, or product-tree certificates with
  an independent streaming checker. An exhaustive root-by-characteristic
  sweep is specifically out of scope: the existing interval ledger contains
  `4,495,441` congruence moduli before primality, and each field can contain
  up to `2^40` source roots. Their Cartesian product has no reasonable cost
  envelope. The official batch is unauthorized here and likely well above
  the current sub-`$1` budget. Before requesting it, contributors must publish
  a small-order benchmark, a total CPU/RAM/storage estimate, a resumable
  shard plan, and a hard spending cap. Until then this item is a
  theorem/algorithm request, not a request to start containers.

  Apply the proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_fourth_root_gcd_gate`
  before extracting that fourth root. With

  ```text
  P=2N+kappa x^2U_0^3,
  ```

  every survivor satisfies `S|P^2` and `deg gcd(S,P)>=M-1`. A contributor
  should compute `P mod S`, its square modulo `S`, and a compact gcd-degree
  certificate. A proof that the gcd degree is always smaller than `M-1`
  closes this deleted-pair sublane without a fourth-power extraction.
- **decision:** classify the saturated algebraic locus on which four
  pairwise-coprime monic quadratics `P_i=X^2+u_iX+v_i` satisfy

  ```text
  dim_(F(X^4)) span {1/P_0,1/P_1,1/P_2,1/P_3}=2.
  ```

  Determine whether the nondegenerate locus consists only of the antipodal
  component `u_0=u_1=u_2=u_3=0`, up to the exact scaling and permutation
  symmetries that preserve `F(X^4)`, or print every additional component.
- **algebraic input:** form `P=product_i P_i`, decompose each `P/P_i` in the
  basis `1,X,X^2,X^3` over `Z[u_i,v_i,Y]`, and impose every coefficient in
  `Y` of every `3 x 3` minor. Saturate by `2`, the four constant terms, the
  four discriminants, and all pairwise resultants. Any further normalization
  must come with a proved coverage map.
- **bounded pilot:** the complete pairing census over `F_13` has `50,856`
  rank-four, `1,104` rank-three, and `15` rank-two cases; all rank-two cases
  are antipodal. It runs in a few seconds with negligible memory and is
  vendored as an audit, but it is not a characteristic-free classification.
- **downstream posedness:** the antipodal component is already nonempty at the
  first nonconstant quotient boundary (`d=8` over `F_97`): an exact
  `26,880`-assignment census finds `192` algebraically valid Möbius-graph
  pencils.
  At arbitrary scale the proved descent and weld reduce it to

  ```text
  product_i(R+a_iS)=kappa (Y^d-1)/product_i(Y-a_i^2).
  ```

  Therefore an antipodal-only component classification does not close the
  rate-half node; it identifies this quartic norm equation as the remaining
  official-scale rigidity problem. Any follow-on symbolic attack on that
  equation must retain the odd-degree primitive condition and may discard
  quotient-pullback and four-coset components by theorem, with the discarded
  ideal factors named explicitly in its certificate. It must also parameterize
  only degree-drop directions in `2^36-2<=v<=2^37-2`; constant and low-degree
  translation components have already been excluded analytically. Split the
  outer-parameter ideal by `e_2`, then `e_3`: every `e_2=0` component must
  impose `v>=(2^38-4)/3`, and the `e_2=e_3=0` component must impose
  `v=2^37-2` together with the exact linear-residual Wronskian identity from
  the outset. In that pure component, require `U,V` squarefree and saturate
  away every branch with two roots of `UV` in `Z(D) union {0}`. None of the
  `192` exact `d=8` positives even has centered `e_2=0`.

  At the generic floor `v=2^36-2`, impose the exact linear identity

  ```text
  dDU-Y(D'U+4DU')=t_0+t_1Y
  ```

  and saturate away branches where `U` has two repeated, deleted-divisor, or
  zero roots. At the intermediate floor `v=(2^38-4)/3`, impose the analogous
  quadratic identity and saturate away branches with three such roots. Above
  either floor, separate components by the exact residual degree
  `r+4-q(r-v)`, which rises by `q` per added degree of `V`. A contributor run
  that omits these identities is not solving the posed downstream problem.

  The boundary identities now admit a stronger elimination and this should be
  used before introducing any coefficients of the official-degree `U`. Put

  ```text
  E(z)=product_(i=0)^3(1-b_i z),
  E(z)^(-1/4)=sum_(m>=0)a_mz^m,       b_i^d=1,
  s=2^37,       d=2^39.
  ```

  The monic `U` is uniquely the reverse of the truncation through `a_(s-1)`.
  A generic-boundary solution requires `a_s=a_(s+1)=0` and
  `a_(s+2)!=0`; an intermediate-boundary solution requires `a_s=0` and
  `a_(s+1)!=0`. The coefficients obey

  ```text
  4m a_m=-sum_(j=1)^4(4m-3j)eta_j a_(m-j),
  E=1+eta_1z+eta_2z^2+eta_3z^3+eta_4z^4.
  ```

  A valuable contributor-scale follow-on is an exact compressed
  nonvanishing/component certificate for these gaps on four distinct
  order-`d` roots, modulo common scaling and permutation, with the centered
  outer `q=2` and `q=3` conditions retained through the `a_i^2=b_i` lift and
  Möbius weld. PASS excludes the corresponding boundary; FAIL must print an
  admissible finite field, four roots, square-root lift, outer parameters, and
  replayable recurrence values. A point sample or a linear scan through
  `2^37` recurrence steps has no completeness claim. Use a compressed
  algebraic-series, diagonal, resultant, or cyclotomic representation and
  provide its coverage proof before a large run.

  In the generic `q=2` branch, the primary gap is only half of the posed
  certificate. Set `B=sum_(m=0)^(s-1)a_mz^m`, `h=2^36+1`, and

  ```text
  J=z^(-2h)(E^(-1)(1-z^d)-B^4)/B^2,
  P=(J/J(0))^(1/2),       P(0)=1.
  ```

  The normalized reverse of `V` is fixed by `P mod z^h`, and its degree
  `h-3` forces `[z^(h-2)]P=[z^(h-1)]P=0`. A generic-boundary PASS must exclude
  the simultaneous four vanishings

  ```text
  a_s=a_(s+1)=[z^(h-2)]P=[z^(h-1)]P=0,
  ```

  not merely the primary pair. A FAIL certificate must replay both nested
  series and then reconstruct the remaining outer-coefficient identities.

  The secondary series now has a cheaper exact interface. Write

  ```text
  d=8h-8,       r=2h-3,
  L=sum_(m<h)a_mz^m,       T=sum_(m<h)a_(2h+m)z^m.
  ```

  After `a_(2h-2)=a_(2h-1)=0` and `c=a_(2h)!=0`, the two secondary
  vanishings are equivalent to

  ```text
  L T=c C^2 mod z^h,       C(0)=1,       deg C<=h-3.
  ```

  The full shifted tail also satisfies the proved first-order equation

  ```text
  E'B+4EB'
    =-z^(2h-1)((zE'+8hE)T_hat+4zE T_hat'),
  ```

  whose parenthesized forcing has degree at most one. A contributor
  implementation should use this square-plus-differential gate before the
  canonical span test; it should not build the nested square root or either
  official-degree polynomial. A rejected packet may print the first failed
  square coefficient. A survivor must print the two coefficient windows,
  `c`, the normalized square root, and the two linear-forcing coefficients.

  Before the canonical span, apply the generic Euler divisor gate. Reverse
  the canonical truncations to monic `U,V`, form the linear residual

  ```text
  T=dDU-Y(D'U+4DU'),
  ```

  write `T=t_1(Y-tau)`, and first apply the scalar norm gate

  ```text
  t_1^2V(tau) in (F^*)^3.
  ```

  For a base field of order `q=1 mod 3`, certify this by exponentiation to
  `(q-1)/3`; when `q=2 mod 3`, skip it because cubing is bijective. A scalar
  rejection certificate needs only the canonical field, `t_1,tau,V(tau)`,
  and the cubic-character value.

  Next compute

  ```text
  N_T=Res(V,T),       N_Q=Res(V,(Y^d-1)/D).
  ```

  Require `N_Q` to be a fourth power and require the exact coupling

  ```text
  N_T^4N_Q^3=d^(4v).
  ```

  Use subgroup products or compressed resultants; do not expand the
  degree-`d-4` quotient. The certificate prints both norms, their character
  values, and the coupling residual. A coupled scalar survivor must then
  certify

  ```text
  (TU^3+d) mod V=0.
  ```

  Evaluate `U^3 mod V` in a compressed quotient-algebra representation and
  multiply by the linear `T`; do not materialize `TU^3+d`, whose degree is
  `6*2^36-2`. A remainder rejection certificate prints a hash-pinned nonzero
  remainder. Passing either gate is only a necessary-condition hit and
  continues to the span and split/Mobius stages.

  Shard any contributor implementation by the proved maximal-field character
  table. Over the ambient field, the fourth-power test is active in every
  branch. The cubic test is active in every quadratic-extension branch and in
  the prime-field `p=1 mod 3` branch; only prime-field `p=2 mod 3` packets
  skip it. A specialized packet whose data have been proved to descend from
  `F_(p^2)` to `F_p` must recompute both characters over `F_p`. The shard
  manifest must name the field in which each character was evaluated.

  There is now an exact deterministic reconstruction for that last step. Put

  ```text
  Q=(1-z^d)/E,                 Rbar=z^(-2h)(Q-B^4),
  alpha=Rbar(0),               Cbar=P mod z^h,
  S=Rbar-alpha B^2Cbar^2,
  X=z^hBCbar^3,                Y=z^(2h)Cbar^4.
  ```

  A complete generic candidate must satisfy `S=beta X+gamma Y`, where
  `beta=[z^h]S` and `gamma=[z^(2h)](S-beta X)`, and the centered quartic
  `W^4+alpha W^2+beta W+gamma` must split into four distinct parameters with
  the Möbius matching to square-root lifts of the `b_i`. The contributor run
  should therefore stream-reject in this order: primary gaps, secondary gaps,
  Euler cubic norm, Euler fourth norm, norm coupling, Euler remainder, full
  span equality, quartic splitting, Möbius matching. It must use compressed
  reversals and never materialize or retain official-degree `U,V` coefficient
  arrays.

  Common subgroup scaling preserves the certifier, so normalize one `b_i=1`;
  quotient by permutations as well. The certificate must include the inverse
  orbit-coverage counts. PASS means every normalized orbit rejects at one
  named stage. FAIL prints the first complete passing orbit and all compact
  canonical data. Prefix agreement in the span test is not a PASS.

  A bounded order-64 pilot (`ap-wLXZpGxaBiBlZ1NZ3MP14e`) exhausts all
  `C(64,4)=635376` quadruples over each of the first eight primes above the
  deliberately strong threshold `p>=64^2`, `p=1 mod 64`. It finds no primary
  double gap, although six fields contain between `64` and `192` single gaps.
  The `p=193` positive control reproduces all `64` members of the known
  double-gap scaling orbit and already has `p>d`. The square threshold is not
  a uniform official hypothesis: the maximal-row quadratic field branch has
  only `p>2^64` at `d=2^39`. The
  hash-pinned result and checker are
  `experiments/prize_resolution/rate_half_list_order64_primary_gap_result.*`.
  Do not turn this into a large fixed-order prime sweep: no proved transport
  makes additional order-64 fields complete for the official growing-order
  question. The valuable large request is the compressed, coverage-proved
  simultaneous-gap/span certificate above.

  A final bounded order-128 route pilot
  (`ap-K60XbR1aXkETENbT2n7A4b`, with orbit classifier
  `ap-CxjRuOXnLkrszE6llB1U4m`) exhausts all `C(128,4)=10668000`
  quadruples in each of the first eight split prime fields. Only `p=257` and
  `p=641` contain primary double gaps, with `192` packets apiece, and no
  packet passes the secondary two-window gate. Modulo common subgroup scaling,
  each positive field has one orbit of size `128` and one orbit of size `64`;
  the size-`64` orbit is two deleted antipodal pairs. The hash-pinned evidence
  packet is `experiments/prize_resolution/rate_half_list_order128_two_window_result.*`.
  This is the last justified raw fixed-order sweep. It selects a parity-
  reduced one-parameter sublane for algebraic treatment but supplies no
  transport to official order. Contributors should spend additional compute
  only on the coverage-proved symbolic request above, not on more primes or
  larger fixed orders.

  That sublane now has a proved exact router. If the deleted roots are two
  antipodal pairs and `d=16M`, normalize their squared ratio to
  `t in mu_(8M)\{1}`. One primary and one secondary zero are automatic; the
  remaining gate is `F_(2M)(t)=G_M(t)=0` with `F_(2M+1)(t)!=0`, where the
  `F_j` obey a second-order recurrence and `G_M` is one terminal coefficient
  of a length-`M+1` square root. A useful symbolic contributor subtask is a
  characteristic-explicit Bezout, resultant-factor, or torsion-nonvanishing
  certificate for this pair at symbolic `M`. A table of fixed `M` gcds is not
  the requested output and does not authorize a large recurrence campaign.

  The complete canonical survivor has a still stronger exact interface.
  Parity forces `beta=0` and gives

  ```text
  (1-w^(8M))/((1-w)(1-tw))
   =(B_0^2+lambda w^(2M+1)C_0^2)
    (B_0^2+mu     w^(2M+1)C_0^2),
  ```

  with two coprime degree-`4M-1` factors partitioning the undeleted torsion
  roots. This two-cell primitive square-pencil classification is the preferred
  contributor subtask: determine every possible root-cell partition under
  the displayed form, then impose the existing nonperiodic and Möbius-matching
  gates. The inverse-root cells have identical Fourier moments through
  frequency `2M`, and their first difference at `2M+1` is exactly
  `-(2M+1)(lambda-mu)`. A symbolic classification or prefix-flatness
  transcript has a DAG outcome; enumerating the `8M` roots or constructing
  official-degree factors does not.

  A proved primitive-resultant bound now removes the prime-field and nonsplit
  quadratic branches from this deleted-pair subtask. Any contributor
  classification should therefore work only in the split quadratic branch
  `q=p^2`, `p=1 mod 2^40`. A campaign covering either eliminated branch is
  obsolete. All quotient-pencil factors, outer parameters, and Möbius data in
  the surviving branch descend to `F_p`; an implementation should use
  `F_{p^2}` only for the full evaluation-domain check. The ordinary four-root
  orbit and the non-generic boundary strata remain separate CR-002 work.

  On the deleted-pair generic sublane, eliminate the generic direction before
  any CAS component calculation. In original half-degree coordinates every
  complete packet has

  ```text
  D=D_0(Y^2),       U=YU_0(Y^2),       V=V_0(Y^2),
  (16M-4)D_0U_0-2xD_0'U_0-8xD_0U_0'=kappa.
  ```

  For fixed monic quadratic `D_0`, the displayed constant-forcing ODE has at
  most one monic polynomial solution `U_0`; its coefficient recurrence has
  one terminal equation. Generate `U_0` from that recurrence and reject at
  the terminal equation before introducing `V_0,lambda,mu`. Preserve the
  forced simple root `U(0)=0`, but saturate away every second repeated,
  deleted-divisor, or zero root. A contributor transcript that allocates an
  independent official-degree `U`, or saturates away the zero root, does not
  cover the proved sublane.

  The outer ratio is no longer a free scalar either. Normalize the four
  deleted-root lifts to `(1,iota,r,iota r)`, put `q_out=mu/lambda`, and split
  the classifier into exactly the three reciprocal branches

  ```text
  r^2(1+q_out)^2=4q_out(r^2-r+1)^2,
  (r-1)^4(1+q_out)^2=4q_out(r+1)^4,
  (r^2+1)^2(1+q_out)^2=4q_out(r^2-4r+1)^2.
  ```

  For fixed `r`, each branch determines at most one unordered
  `{q_out,q_out^(-1)}`. Do not enumerate 24 point matchings and do not divide
  by `1+q_out`: the harmonic `q_out=-1` cases are retained by the cleared
  router equations. The official harmonic-exclusion theorem then removes
  all of them: app `ap-YVKd2kCRyMVnpUDLR9id5x` checked every one of the
  `4,495,441` exact characteristic congruence classes with no trace-recurrence
  hit. Allocate no `q_out=-1` shard. Impose `q_out^N=1` before any remaining
  polynomial solve; the two monic root-cell factors prove this from their
  constant terms.
  A complete contributor certificate should identify the selected pairing
  branch before applying the remainder-square router.

  In fact, do not solve for either of those objects. Once the ODE has produced
  `U_0`, form

  ```text
  Q=(x^N-1)/D_0,       A=xU_0^2,       R=Q-A^2.
  ```

  For `q_out!=-1`, Euclidean division `R=AS+T` is a complete router. Do not
  retain `q_out` as a variable. For pairing `j`, impose the exact identity
  `4b_jT=a_jS^2`, recover `y=q_out+q_out^(-1)=4b_j/a_j-2`, and apply the
  38-step trace gate above. The valuable contributor task is a compressed,
  coverage-proved uniform rejection of these three one-variable tests,
  followed by one exact fourth-power certificate for `T`. Allocating
  coefficients of `V_0`, sampling square prefixes, materializing `x^N-1`,
  sharding harmonic data, constructing `q_out`, duplicating reciprocal roots,
  or running the old polynomial-square test is obsolete.
  Before allocating full Euclidean data, reject at `(CCG3)` using the one
  terminal reversed-quotient coefficient. Only then reject unless `S|P^2` and
  `deg gcd(S,P)>=M-1`; compute these through modular remainders rather than a
  dense square. A PASS certificate for uniform nonexistence may consist of a
  coverage-proved strict gcd upper bound on all three scalar branches.

  The intermediate `q=3` floor now has a root-free preferred endpoint. In
  original coordinates form the canonical `U`, the exact quadratic residual

  ```text
  T=dDU-Y(D'U+4DU'),
  P=TU^3+d,       W=T'U+3TU'.
  ```

  **CR-002-I: RESOLVED ANALYTICALLY; DO NOT RUN.** Define

  ```text
  A=4YDT'+3T(dD-YD'),       J=dA^3+27T^7.
  ```

  The exact identity `4YDW=UA-3T^2` proves

  ```text
  gcd(P,W)|J,       deg J=18.
  ```

  But a survivor would force `deg gcd(P,W)>=(2^38-4)/3`. Hence the maximal
  intermediate boundary is empty. No holonomic, subresultant, modular, dense,
  or official-field run is needed; contributors should spend no compute on
  CR-002-I.

  The same annihilator closes the first higher-degree band. If
  `t=deg T=3v-2r+4>=5`, then `deg J=7t`, so a survivor requires

  ```text
  10v>=7r-14,       v>=96,207,267,429.
  ```

  Do not run any intermediate experiment for
  `v<=96,207,267,428`; all `4,581,298,449` degrees from the official floor
  through that endpoint are proved empty. The interval above
  `96,207,267,429` is not yet a ready large-compute request: first derive a
  new compression or annihilator that can decide degrees where `7 deg T`
  reaches `v`.

  The compact Hensel certifier remains below only as an audit trail and small
  analogue decoder. With `h=(2^37+1)/3`, form

  ```text
  Rbar=z^(-3h)(Q-B^4),       theta=Rbar(0),
  H=Rbar/(theta B),          C_*=H^(1/3),
  Delta=[z^(h-1)]C_*^2/B,   kappa=[z^(2h-1)]C_*,
  Delta_1=[z^h]C_*^2/B,     kappa_1=[z^(2h)]C_*,
  Delta_2=[z^(2h)]C_*^2/B,  Gamma_1=[z^h]C_*^3/B^2,
  kappa_2=[z^(3h)]C_*,       Delta_3=[z^(3h)]C_*^2/B,
  Gamma_2=[z^(2h)]C_*^3/B^2, Xi_1=[z^h]C_*^4/B^3,
  kappa_3=[z^(4h)]C_*.
  ```

  Stream-reject `Delta=0,kappa!=0`. If `Delta!=0`, test only the unique
  `u=3kappa/Delta` and require
  `u^2-uDelta_1+3kappa_1=0`. If `Delta=kappa=0`, test only the at-most-two
  base-field roots of `X^2-Delta_1 X+3kappa_1`; there is no longer a
  parameterized scalar branch. Reduce

  ```text
  81kappa_2-27uDelta_2+27u^2Gamma_1-35u^3
  ```

  modulo that monic quadratic and apply the printed linear gate `A u+B=0`.
  If `A!=0`, test only `u=-B/A`; if `A=0,B!=0`, reject. Only `A=B=0`
  reaches the next gate. Reduce

  ```text
  243kappa_3-81uDelta_3+81u^2Gamma_2-105u^3Xi_1+154u^4
  ```

  by the same quadratic and apply `C u+D=0`. On `A=B=0`, if `C!=0` test
  only `u=-D/C`; if `C=0,D!=0`, reject. Two roots remain only on
  `A=B=C=D=0`. A survivor must make the unique solution of

  ```text
  H=C_u^3(1+u z^h C_u/B)
  ```

  a polynomial of degree at most `2h-2`. The exact cube-part form is likewise
  retained for audit and reuse outside the now-closed maximal boundary:

  ```text
  Rbar=theta C_u^3(B+u z^hC_u),
  C_u^2 | gcd(Rbar,Rbar'),
  C_u | gcd(Rbar,Rbar',Rbar'').
  ```

  For each normalized cube divisor `C`, the exact cofactor test is

  ```text
  Rbar/(theta C^3)-B=u z^hC.
  ```

  Do not materialize dense official-degree polynomials or extend the Hensel
  coefficient hierarchy one term at a time. The degree-eighteen annihilator
  has already rejected every official maximal-intermediate candidate before
  this cofactor or its split/Mobius matching can arise.

  The pure `q=4` floor must use the harmonic-Fermat router. Choose lift signs
  `a_i^2=b_i`, quotient by common scaling and relabel to a harmonic ordering,
  then normalize `a_0=1` and generate

  ```text
  w=(2x-y(1+x))/(1+x-2y),       x^(2d)=y^(2d)=w^(2d)=1.
  ```

  Reject equality or antipodality among the four lifts. For every surviving
  orbit, test the exact coprime decomposition

  ```text
  Q=(1-z^d)/E=B^4+Z^4,
  B(0)=1,       ord_0Z=1,       deg B,deg Z<=2^37-1,
  ```

  together with the proved squarefree and linear-Wronskian constraints.
  Harmonicity itself is not a rejection stage: complete lift-subgroup scans at
  orders `16,32,64,128` already contain `4,40,500,3660` normalized harmonic
  sets. PASS must exclude the matched Fermat decomposition for every harmonic
  orbit; FAIL prints the lift orbit, `B,Z`, factor assignment, and Wronskian
  replay. Do not launch a raw harmonic-pair enumeration at official order
  without a compressed subgroup router and an orbit-coverage certificate.
- **required certificate:** a Groebner/regular-chain/primary-decomposition
  transcript over `Z[1/2]` or a justified characteristic-zero base; explicit
  saturated component ideals; nondegeneracy witnesses; and, for each claimed
  symmetry reduction, a machine-checkable inverse coverage map.
- **checker:** an independent exact script must verify ideal containment in
  both directions after saturation, replay every component parametrization,
  and check that discarded components lie in a named discriminant or
  resultant divisor. Probabilistic modular reconstruction alone is
  insufficient.
- **DAG outcome:** an antipodal-only result proves that the welded quartic norm
  equation is the complete direct fiber-four residual. Additional components
  become a finite, printed list of separate algebraic subcases and must each
  be transported to its own subgroup-product equation. A counterexample to
  the proposed component list repairs the classification target but does not
  affect the already-proved rank-three and rank-four exclusions. On the
  antipodal component, a useful next certificate must address the primitive,
  nonperiodic high-degree locus; a quotient-periodic or low-degree-translation
  census has no remaining DAG outcome. A pure-quartic certificate with
  `v<2^37-2` is likewise incompatible with the proved Wronskian theorem.
  Generic- or intermediate-boundary output with residual degree other than
  one or two, respectively, is incompatible with the proved reverse-residual
  theorem and must be treated as a generator or normalization error.
- **execution shape:** use a contributor machine or capped remote CAS job;
  checkpoint elimination stages and export compact bases plus hashes. Do not
  materialize large artifacts in WSL.
- **estimated resources:** unknown until a modular pilot; potentially
  multi-gigabyte and therefore outside the current laptop and sub-`$1` Modal
  policy.

A raw `d=16` or larger antipodal point census is not a third compute request.
The `d=8` positives already defeat scale-free emptiness, while a finite larger
negative cannot certify the official `d=2^39` quartic norm equation. Such a
run becomes responsible only after a proved lifting/classification theorem
makes a bounded range complete.

## CR-003: Rate-half Hankel sharp-cap component existence census

- **status:** EXTERNAL EXACT PILOT REQUEST. Do not run on the current laptop or
  the remaining low-credit Modal account.
- **consumer:** `rate_half_band_closure`, at strict budget `B=2^39` and
  half-distance budget `B=2^39+1`.
- **proved routers:**
  `rate_half_ca_hankel_strict_a3_slope_slack_ledger` and
  `rate_half_ca_hankel_half_distance_a3_slope_slack_ledger`, together with
  `rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger`. At the
  official scale the counterexample families are indexed by

  ```text
  strict:         m<=e<=floor((4m-1)/3),  0<=h<=4(e-m),
  half-distance A=3:  m+1<=e<=floor((4m-1)/3),
                                            0<=h<=4(e-m)-1.
  half-distance A=1:  s in {0,1,2},
                      m+1<=e<=floor((4m-s)/(1+s)).
  ```

  This request concerns only `h=0` for `A=3` and `ell=0` for `A=1`. In both
  `A=3` shapes the generator is a degree-`e` rational normal kernel curve of
  exact separation rank `e+1`, its norm residual has degree at most `e`, at
  least `N-e` domain rows are saturated, and every geometric component degree
  is forced by a unique possible integer chamber. The strict matrix is
  `(4m+1) x 4m` with a unique right singular block and locator degree `rho`;
  the half-distance matrix is `4m x (4m+1)` with a unique left singular block
  and locator degree `rho+1`. In the latter case the degree-`rho` split
  `Q_gamma` is a factor of the locator with one additional distinct domain
  root. The `A=1` matrix has the same dimensions but full row rank `4m`, one
  right singular block, and a fixed core `s in {0,1,2}`. Its residual
  sharp-cap and norm degree are the exact `T_max,eta` of `(A1L4)--(A1L5)`.
- **decision:** for the complete analogues

  ```text
  m in {2,4,8,16},       N=16m,
  A=3: rho=4m-1, strict m<=e<=floor(rho/3),
       half-distance m+1<=e<=floor(rho/3), T=4e+1;
  A=1: rho=4m, s in {0,1,2}, d=rho-s,
       m+1<=e<=floor(d/(1+s)), T=T_max(s,e),
  ```

  and, for each `m`, the first three prime fields in increasing order with
  `N|(q-1)` and `q>N`, decide separately for each shape whether a syndrome
  Hankel pencil exists with the designated generic rank, minimal index `e`,
  no common degree-`r` domain-split locator, exactly `T` supported finite
  slopes, and exactly the designated fixed core (`s=0` for `A=3`). The solver
  must impose the appropriate Hankel coefficient chain, not merely search
  arbitrary biforms satisfying the norm identity.
- **preprocessing contract:** enumerate only component degree packets allowed
  by `(SSL19)--(SSL20)` or `(A1L14)--(A1L15)` and summing to the corresponding
  residual bidegree. Use the exact norm residual, complementary factorization,
  and clean-column count as early rejection constraints. Quotient by
  parameter `PGL_2`, common polynomial scaling, and cyclic domain
  automorphisms only with an inverse coverage map.
  On the `A=1,s=1,e=2m-1` sharp-cap face, impose the stronger proved packet:
  exactly one component has `(r_*,e_*)=(2e_*+1,e_*)`, every residual
  component has `(r_i,e_i)=(2e_i,e_i)`, their total parameter degree is at
  most `floor(e/5)`, and the dominant component has separation rank at least
  `ceil((e+1)/(b+1))`. Do not allocate shards to rank-at-most-four models on
  this face. Its contracted middle-Hankel matrix also satisfies the proved
  exact identity `adj M=lambda*q*q^T`, with one common linear factor and no
  other projective rank drop. A shard must divide the nonzero maximal minors
  by that same `lambda` and verify every quotient `q_iq_j`; do not treat the
  cofactors as independent elimination variables. For a surviving dominant
  component, impose its exact component norm identity with residual degree
  `e-5b-1+D_*`, `D_* in {0,1}`, and its complementary factorization over at
  least `14m+5b` residual domain rows. Output that component certificate
  separately from the balanced residual components, whose norm residual
  degrees are exactly `5e_i+D_i`. Finally impose the proved two-sided weld

  ```text
  W B-B_X E_Z=Q_* K,       V B+A E_Z=-P_X K,
  ```

  with the printed degree boxes. The external decision is now classification
  of this coupled matrix factorization together with
  `adj M=lambda*q*q^T`; independent searches for cofactors, norm factors, and
  complements are obsolete on this face. The current live handoff is:

  ```text
  B_X=X_0X_1,
  QV_a+P_XW_a=P,

  D_*=0:
    QA_a+P B_a=P_XX_1,
    W_aB_a-X_1=QK_a;

  D_*=1:
    QA_a+P_cl B_a=P_XX_1,
    W_aB_a-X_1E_Z=QK_a,
    K_a(gamma_0;X)!=0.
  ```

  Every root of `X_1` has a nonzero domain trace. Either `X_0=1`, or exactly
  one of the following boundary normalizations applies:

  ```text
  b=0,D_*=1,c=1: X_1=1 and the exceptional trace is active;
  b=0,D_*=1,c=2: X_1 has one active root with delta=1.
  ```

  The `c=1` exceptional-only boundary has a stronger proved endpoint and must
  not be sent as the generic active system above. Put `E=E_Z` and
  `q_0=Q(gamma_0;X)`. Then `q_0|P_X`, and the unique polynomial

  ```text
  J=B(gamma_0;X)/q_0,       deg J=D_0-r,
  ```

  gives the exact descended system

  ```text
  B=QJ+E B_1,       A_1=A+P_clJ,
  QA_1+PB_1=P_X,
  WB_1-1=QK_1,
  VB_1+A_1=-P_XK_1,
  deg_X A_1=D_0-r.
  ```

  A contributor shard should classify this corrected complement square
  directly. It must retain the final equality: the one-degree relaxation
  from `D_0-r-1` to `D_0-r` is why the trace-free exclusion does not close
  the profile. Do not allocate the old exceptional-only active-trace system
  or claim the trace-free contradiction after silently dropping `P_clJ`.

  Normalize the infinity block before allocating any remaining coefficients.
  With `q_inf=[X^r]Q=E q_bar`, `j_inf=[X^(D_0-r)]J`, and
  `v_inf=[X^(D_0-2)]V`, impose

  ```text
  [X^(D_0-r)]A_1=P_cl j_inf,
  [X^D_0]B_1=-j_inf q_bar,
  [X^(r-1)]W=-E q_bar v_inf,
  [X^(D_0-1)]K_1=j_inf q_bar v_inf.
  ```

  Hence `A_1` and `B_1` have exact corners `(D_0-r,T-1)` and
  `(D_0,e-1)`. Eliminate those four leading coefficients from the solver.
  Do not retain the old `deg_X B<=D_0-1` box after descent: the corrected
  `B_1` has exact `X`-degree `D_0`. The optional `v_inf` may be zero.

  Before any Hankel elimination, also require the compact two-sided
  resultant certificate. With `n_X=D_0-1`, print nonzero `c_t,c_X` and check

  ```text
  Res_t(P,Q)=c_tP_X^e,
  Res_t(P,A_1)=c_t^(-1)P_X^(T-e),
  Res_X(P_X,Q)=c_XP_cl^rE^(r-1),
  Res_X(P_X,V)=c_X^(-1)P_cl^(n_X-r)E^(n_X-r+1).
  ```

  Use product trees or subresultant certificates; do not materialize all
  official fibers merely to multiply them. A failed identity rejects the
  shard. Passing all four remains only preprocessing and does not certify the
  Hankel chain or irreducibility.

  Reduce the unit-intersection calculation further. Reuse the same `c_X`,
  put `[X^r]Q=E q_bar`, and let `m=deg_XW` after checking whether the optional
  infinity coefficient vanishes. Require

  ```text
  Res_X(Q,B_1)=c_X q_bar,
  Res_X(Q,W)=c_X^(-1)E^(m+n_X+1)q_bar^(m+n_X).
  ```

  The first resultant has degree only `e-1` in the parameter and is the
  preferred common-fiber certificate. A shard with any other irreducible
  resultant factor is invalid. Do not force `m=r-1` when `v_inf=0`, and do
  not infer that `q_bar` is root-free from this identity.

  Apply one reciprocal Euclidean step before allocating any lower
  coefficients. At the proved fixed degrees put

  ```text
  F(t,Y)=Y^rQ(t,1/Y),       G(t,Y)=Y^D_0B_1(t,1/Y),
  j_infF+EG=YL,
  Delta_inf=L(t,0)=j_inf[X^(r-1)]Q+E[X^(D_0-1)]B_1.
  ```

  Require the exact compact certificate

  ```text
  Res_Y(F,L)=c_XE^(r-1),       gcd(q_bar,Delta_inf)=1.
  ```

  The complete `q_bar` factor is thereby removed before the classifier:
  any nonexceptional irreducible factor in `Res_Y(F,L)`, or any common
  factor of `q_bar,Delta_inf`, rejects the shard. Use a subresultant or
  product-tree certificate; do not enumerate official fibers. Retain the
  exceptional `E`-supported contact and continue with the Hankel and
  splitting gates, since this reciprocal descent is necessary but not an
  exclusion.

  Do not allocate `Delta_inf` as a free coefficient. With

  ```text
  a_minus=[X^(D_0-r-1)]A_1,
  ```

  impose the proved leading Bezout ledger

  ```text
  P_clDelta_inf+E q_bar a_minus=1.
  ```

  Equivalently, compute `Delta_inf=P_cl^(-1) mod (E q_bar)` and retain
  `a_minus` as the quotient certificate. Reject immediately if either gcd
  with `E q_bar` is nontrivial or the exact polynomial identity fails. This
  modular inversion is preferred to adding coefficient variables or
  evaluating every official fiber.

  Use the full reciprocal complement rather than continuing coefficient by
  coefficient. Define

  ```text
  A_vee=Y^(D_0-r)A_1(t,1/Y)=P_clj_inf+YU,
  R_X=Y^(D_0-1)P_X(1/Y),
  ```

  and require

  ```text
  FU+P_clL=R_X.
  ```

  A shard should allocate `F,U`, test the coefficientwise divisibility
  `P_cl | (R_X-FU)`, and recover `L=(R_X-FU)/P_cl`. Do not allocate the
  lower coefficients of `L` independently. Then enforce
  `E | (YL-j_infF)` to reconstruct `G`; a packet passing only the first
  divisibility is incomplete. This replacement converts the lower
  reciprocal block into interpolation and two exact divisibility checks.

  Reduce the remaining unit square before allocating any companion forms.
  With `N=D_0+r-2` and the fixed-degree reciprocals of `V,W,K_1`, introduce

  ```text
  S=(j_infW_vee+EK_vee)/Y
  ```

  and require

  ```text
  LW_vee-FS=EY^N,
  V_vee=-UW_vee-P_clS,
  K_vee=(YS-j_infW_vee)/E.
  ```

  Thus a shard allocates only `F,U,W_vee,S`, then recovers
  `L,G,K_vee,V_vee` through the triangular ledger. Reject on any of the one
  `P_cl` or two `E` divisions, on the reduced unit identity, or on a
  recovered degree-box violation. Do not create independent coefficient
  blocks for the four recovered forms. Hankel and splitting tests still
  follow this preprocessing.

  Pin the middle-Hankel factor before checking any cofactor equations. On
  this exceptional-only shard the unique omission is at `E=0`, so print one
  nonzero base-field scalar `c_H` and require

  ```text
  adj M=c_HEqq^T,
  gcd(nonzero maximal minors)=E       up to scalar,
  (adj M/E)|_(E=0)=c_Hq(gamma_0)q(gamma_0)^T.
  ```

  The final matrix must be nonzero of rank one. With `q_r=E q_bar`, its top
  row and column are zero, while globally the top-top cofactor is
  `c_HE^3q_bar^2`. Reject a different common linear factor, a zero divided
  specialization, or any additional common cofactor factor. Do not absorb
  `c_H` into `q` unless a base-field square root is supplied explicitly.
  This pinned cofactor check is the first actual Hankel gate after the
  reciprocal reconstruction.

  At each active domain root impose the exact gcd factorization

  ```text
  K_x=-H_xJ_x,       deg Qhat_x=delta_x+epsilon_x,
  N_x=Qhat_x/E_Z^epsilon_x,
  S_*=product_x N_x,       sum_x delta_x=C_*.
  ```

  When `D_*=1`, also impose the exceptional saturated gcd degree at least
  `e+3b` and complementary quotient degree at most `c+1`. Allocate no shards
  for `K=0`, the quartic boundary, a trace-free weld, arbitrary prime-factor
  allocations, a `Z_W` exceptional allocation, or a zero exceptional trace;
  all are proved impossible. Do not run the unreduced weld as one monolithic
  elimination. Each live shard must additionally certify the exact two-sided
  partitions

  ```text
  Q_gamma A_gamma=G_X/X_0       for every clean gamma,
  Q_x V_x=P                     for every saturated x,
  ```

  with squarefree disjoint factors of exact degrees
  `(r,D_0-deg(X_0)-r)` and `(e_*,T-e_*)`. Check the active bad-row clean
  incidence total `c e_*-C_*-E_bad` before attempting elimination. Do not
  introduce independent biform coefficients for a proposed partition packet.
  First build its saturated-row by clean-slope nonincidence graph, check the
  incidence relation in both directions, and label every edge by

  ```text
  theta_(x,gamma)=F_gamma(x)/G_x(gamma).
  ```

  The graph is proved connected. Recover its row/column potentials by one
  spanning-tree pass and reject on the first inconsistent cycle. With the
  recovered clean-fiber scalars `a_gamma`, test all `r+1` vectors

  ```text
  (a_gamma [X^j]F_gamma)_(gamma in Z_cl)
      in RS[Z_cl,e_*+1].
  ```

  These tests are necessary and sufficient to reconstruct the unique
  partition-compatible biform up to scalar, and they automatically verify
  every saturated fiber. Compute the ranks of the scaled clean-locator
  coefficient matrix, scaled saturated-locator coefficient matrix, and core
  value matrix; they must agree with `sr(Q)`, be at least
  `ceil((e+1)/(b+1))>=5`, and equal `e+1` when `b=0`. Only a packet passing
  this gate should acquire Hankel-chain, adjugate, irreducibility, or
  active-trace variables.

  The bounded prime-field reference prefilter and schema are

  ```text
  background/nodes/rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction/check_packet.py
  background/nodes/rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction/packet_schema.md
  ```

  It emits a canonical packet hash and all three ranks. It deliberately
  materializes the small-analogue core matrix and does not certify primality,
  the ambient domain/support, or any post-partition Hankel condition. Use it
  for bounded pilot shards only; a positive final certificate still needs the
  complete independent checker specified below.
- **positive certificate:** print the shape, field, domain generator, endpoint
  syndrome vectors `y_0,y_1`, the primitive `Q(U,V;X)`, its left or right
  KCF/minimal-index certificate, all `T` slopes and split locators, the
  column-far no-common-locator check, component factorization, incidence
  matrix, the corresponding norm identity, and the complementary
  factorization. For a
  half-distance `A=3` certificate, print and verify the extra locator root at
  every clean slope. For `A=1`, print the fixed core, residual generator,
  Euclidean remainder, and residual norm identity separately. The independent
  checker must rebuild every Hankel matrix and verify all ranks, roots,
  weights, and degree ledgers. For an `A=1,s=1` active partition packet it
  must also print the nonincidence graph, locator hashes, recovered potentials,
  zero Reed--Solomon parity syndromes, and the three matching rank
  certificates. A rejected packet should retain a compact inconsistent-cycle
  witness, a nonzero parity syndrome, or a rank mismatch.
- **negative certificate:** an exhaustive Groebner/regular-chain or finite
  enumeration transcript for every registered field and allowed component
  packet, including saturated ideals, symmetry coverage, and independently
  checkable inconsistency witnesses. Random sampling or a solver's bare
  `UNSAT` line is insufficient.
- **interpretation:** one positive small analogue is a route fence and a
  construction template, not an official counterexample. Complete negative
  small analogues are also evidence only, but can reveal which component
  chamber or Hankel-chain identity should be promoted into a uniform theorem.
  Neither outcome changes the critical status without a proved transport.
- **execution shape:** checkpoint by
  `(family,shape,core,m,e,q,component packet)`, omitting `core` only for
  `A=3`; stream compact certificates and hashes; stop a shard before memory
  pressure rather than materializing all split locators. Contributors may
  parallelize independent shards, but each shard must have a declared wall,
  RAM, and dollar ceiling.
- **estimated resources:** unknown until `m=2,4` pilots; likely unsuitable for
  the current sub-`$1` policy and potentially multi-gigabyte at `m=16`.
