# Official terminal-block attack ledger

## Exact terminal obligations

The actual schedule ends in

| `ell_j` | `N_j` | WCL weights | smallest one-orbit charge in window |
|---:|---:|---:|---:|
| 1 | 256 | 2..6 | `512*2^-6 = 8` |
| 2 | 512 | 3..7 | `1024*2^-7 = 8` |
| 4 | 1024 | 5..9 | `2048*2^-9 = 4` |
| 8 | 2048 | 9..13 | `4096*2^-13 = 1/2` |
| 16 | 4096 | 17..21 | `8192*2^-21 = 1/256` |

Thus WCL-ZONE requires **zero** primitive orbits throughout the full windows
at `ell in {1,2,4,8}`. At `ell=16`, one weight-17 orbit already
violates the bound, one weight-18 orbit saturates it, and higher-weight orbits
must be counted exactly. Deeper levels are genuinely weighted rather than
zero-event obligations.

The ledger is raw: multiplier shadows, additive clusters, and level lifts are
charged at their own level and weight. Ownership metadata cannot delete their
mass from C1'. At the four zero-event levels this repair does not change the
obligation, because any ownership class is nonempty exactly when its raw
ledger is nonempty.

## Two exact scope controls

1. `dli_wcl_scope_guardrail` proves that an isolated order-512 row can have a
   primitive weight-3 orbit of charge `64`. It fails the ambient split.
2. `dli_wcl_engineered_terminal_scope` recovers the strongest banked
   engineered weight-6 witness. Its exact norm is `2q` with a 256-bit prime
   factor satisfying `v_2(q-1)=9`, so this construction also fails the ambient
   split by 32 powers of two.

These are not evidence that official WCL is true; they prove only that both
known attacks were terminal-level constructions and cannot be transported
silently to the production tower.

## Exact weight-3 and weight-4 exclusions at `ell=1`

At `ell=1`, shift and odd Galois dilation preserve the cyclotomic norm. A
complete search quotients reduced signed supports by the
affine action

```text
e -> a e + b mod 512,  a odd,
```

before factoring norms. `dli_wcl_weight3_ambient_exclusion` certifies the
complete result:

```text
11,054,080 reduced signed supports
       254 affine-Galois norm classes
       439 distinct certified prime factors
         0 factors q<2^256 with v_2(q-1)>=41
        18 maximum v_2(q-1) below the cap
```

`dli_wcl_weight4_ambient_exclusion` applies the same norm principle through a
normalized-section compiler:

```text
1,398,341,120 reduced signed supports
    1,014,080 normalized-section keys
       24,979 affine-Galois norm classes
       44,599 distinct certified prime factors
            0 factors q<2^256 with v_2(q-1)>=41
           29 maximum v_2(q-1) below the cap
```

Therefore no official production row has a primitive weight-3 or weight-4
relation in either `ell=1` level. Weight 2 is elementary. Weights 5 and 6
remain open, so WCL-ZONE remains open.

## Bounded weight-5 falsification

`dli_wcl_weight5_first64_mitm_exclusion` checks the first 64 primes of the
form `q=k*2^41+1`, in increasing positive `k`. The exact range is

```text
3 <= k <= 996,
6,597,069,766,657 <= q <= 2,190,227,162,529,793.
```

Proper-divisor witnesses certify all 932 intervening values composite, and
direct Pocklington witnesses certify the 64 selected values prime. On every
prime row, an exact pair/triple meet-in-the-middle search checks all 130,560
legal pairs and 22,108,160 legal triples. No reduced weight-5 relation is
found. This is an exact finite no-hit theorem, not an exhaustive weight-5
exclusion.

## Exact weight-3 exclusion at `ell=2`

At `ell=2`, the first odd-index vanishing equation already forces a signed
weight-3 polynomial to vanish at an order-1024 root. The normalized-section
norm census `dli_wcl_ell2_weight3_ambient_exclusion` gives

```text
88,954,880 reduced signed supports
   521,220 normalized-section keys
       510 affine-Galois norm classes
     1,329 factor records, 1,141 distinct certified prime roots
         0 roots q<2^256 with v_2(q-1)>=41
        21 maximum v_2(q-1) below the cap
```

Thus weights 2 and 3 are absent at the official `ell=2` level. Since this is
an emptiness level, weights 4 through 7 must still be excluded before that
level is closed.

## Algebraic weight-4 exclusion at `ell=2`

The second odd-index equation removes weight 4 without a norm census. For the
four signed roots `r_i=s_i omega^e_i`, the equations are

```text
sum_i r_i = sum_i r_i^3 = 0.
```

Newton's identities make the monic root polynomial even, so its roots occur
in antipodal pairs. A reduced signed support with distinct base exponents
contains no antipodal pair. The proved node
`dli_wcl_ell2_weight4_newton_exclusion` therefore excludes every weight-4
relation over every official field. Weights 5 through 7 remain at this level.

## Global Newton cutoff

The same argument works uniformly. If the first `ell` odd power sums vanish,
Newton's identities kill every odd elementary symmetric coefficient through
degree `2ell-1`. Therefore a relation of weight `w<=2ell` is impossible at
odd weight and antipodal at even weight. The proved node
`dli_wcl_newton_short_window_exclusion` gives the complete tower reduction

```text
ell=1:  weights 2--6; Newton excludes 2; prior norms exclude 3,4; residual 5,6
ell=2:  weights 3--7; Newton excludes 3,4; residual 5,6,7
ell=4:  weights 5--9; Newton excludes 5,6,7,8; residual 9
ell>=8: weights ell+1--ell+5; Newton excludes the entire window
```

Thus only six weight slots remain across all 34 production levels:

```text
(1,5), (1,6), (2,5), (2,6), (2,7), (4,9).
```

## Next attack

The preferred next target is `(ell,w)=(2,5)`; its two moment equations should
be used together before any norm sweep. At the terminal `ell=1` levels,
weight 5 is likewise unresolved. Directly
extending the normalized section would require choosing three free tail terms
and is much larger than the completed weight-4 computation. The pair/triple
compiler is now validated, but extending its prime range indefinitely cannot
prove the ambient theorem. The global route still needs an algebraic
obstruction from the `2^41` splitting requirement, or a rigorous orbit/norm
reduction with a feasible class and storage bound. A separately preregistered
small weight-6 round is useful as a falsification probe because a six-term
isolated-row witness is already known, but it must not be confused with
closure.

The exact Burnside sizing in `weight5_orbit_route_fence.md` now resolves the
second option negatively as a uniform continuation: weight five has
`2,296,920` affine-Galois norm classes and weight six has `185,569,028`, versus
`24,979` in the completed weight-four packet. A 256-class exact norm sample
survived, but a blind factor sweep is not a viable six-slot proof. Continue
with the simultaneous-moment sparse-divisor system, starting at `(2,5)`.

The proved `dli_wcl_ell2_weight5_pair_quadratic_router` supplies the first
structured interface. After scaling one root to `1` and choosing two others
`x,y`, it determines the sum and product of the final pair. Membership of that
pair in `mu_1024` is equivalent to two explicit Dickson-recurrence equations.
This reduces the slot from five free roots to two shape variables, but does not
yet exclude their official-characteristic solutions.

The proved `dli_wcl_ell2_weight5_pair_ideal_index_obstruction` clears those
two equations inside `Z[zeta_M]`. For every normalized pair it packages them
as an exact finite-index ideal; any split-row characteristic supporting the
pair must divide that index. Odd Galois dilation preserves the index, so one
pair per dilation orbit suffices. The complete small-order ladder has

```text
M=16,32,64,128: 14,36,82,176 pair orbits,
308/308 exact Smith indices complete,
12 distinct bad primes, maximum v_2(p-1)=8.
```

This is strong route evidence for the official split gate `v_2(q-1)>=41`, not
an extrapolated theorem. Direct integer Smith form is also fenced as the
production implementation: sampled `M=256` workers hit 600 seconds. The next
attack should preserve the ideal obstruction while replacing full integer
Smith form by a structured cyclotomic/resultant or modular determinantal
certificate at `M=1024`.

## Norm-gcd closure (2026-07-14)

The structured resultant route is now complete. It is enough to use the
weaker principal obstruction

```text
g(i,j)=gcd(|Norm(F)|,|Norm(G)|),
```

because every supporting characteristic divides both norms. Exact FLINT
resultants cover all `1,514` odd-dilation pair orbits at `M=1024`; the `507`
distinct nontrivial gcds factor over `168` Pocklington-certified primes, with
maximum `v_2(p-1)=18`. Thus `(ell,w)=(2,5)` is empty on every official row.

The current residual set is

```text
(1,5), (1,6), (2,6), (2,7), (4,9).
```

## Weight-six triple-cubic router (2026-07-14)

The simultaneous-moment route now extends to `(ell,w)=(2,6)`. Normalize a
selected triple to `{1,x,y}`, and let `d` be the product of the remaining
three roots. The paid weight-three exclusion makes `u=1+x+y` nonzero, so
the remaining cubic is determined by `x,y,d`. Two coupled power-of-two
doubling recurrences characterize whether all three cubic roots lie in
`mu_1024`.

This gives at most

```text
1514 pair orbits * 1024 products = 1,550,336 candidates,
```

each with two explicit cyclotomic norm obstructions. It is substantially
smaller than the fenced `185,569,028` blind weight-six norm classes and
uses only ten recurrence doublings per candidate before norm evaluation.
The next exact step is to classify algebraically zero obstruction pairs,
benchmark sampled norm gcds, and only then decide whether a complete
parallel certificate is feasible. No emptiness or WCL promotion occurs yet.

The first deterministic norm benchmark completed on Modal
(`ap-CQbBz0ysQOhbfp2z51zewT`). Four candidates at each order
`64,128,256,512,1024` had no identically zero obstruction pair. Raw gcds
reached `183,078` bits. Removing all factors shared with `Norm(u)` is
rigorous by the paid weight-three exclusion and reduced the sampled maximum
to `11,367` bits. A separate factor run
(`ap-4XmwufmOFrKTfwDNWEtyiS`) completely factored all `19` nonunit
saturated gcds over `16` primes, with maximum `v_2(p-1)=10`.

The route survives, but a blind production sweep is not selected: sampled
order-`1024` norm pairs took `28.2--44.7` seconds. The next theorem should
batch candidates, exploit the small-prime support, or quotient the
pair-product space further before dispatching `1.55` million norm pairs.

---

## WEIGHT-6 RECURSIVE-NORM CLOSURE + FOUR-SLOT RESIDUAL (wave-9 audited, 2026-07-17; appended — v4's two in-place tense edits of history text above are NOT taken, w9-C6)

Slot (2,6) is CLOSED on every official row: the recursive-norm certificate covers all 404,740 quotient orbits (404,230 nonzero saturated norm gcds — 443 certified prime roots, max v_2(p-1) = 18 < 41; 510 structural double-zero cases = exactly the antipodal-mirror family c = 512+a+b; 3,163 complete batches; zero worker errors). Independently reproduced at the wave-9 audit (census, digests on Modal, Pocklington graph, valuation spot checks).

THE RESIDUAL OF RECORD IS NOW FOUR SLOTS: (1,5), (1,6), (2,7), (4,9).
(1,5): the streaming terminal weight-five norm sweep is in flight (no claims yet; pilot max_v2 = 21).

## Extended-window residual of record (2026-07-22 forced correction)

The four-slot residual above is the PRE-EXTENSION (w <= L+5) bookkeeping.
Under the ratified C1'-r3 extended ledger (w <= L+7, L = dimension ell) the
residual of record is TEN zero-event cells:

| ell | window [ell+1, ell+7] | Newton floor 2*ell+1 | closed | OPEN |
|---:|---|---|---|---|
| 1 | [2,8] | 3 (then (1,3),(1,4) by ambient census) | — | (1,5)(1,6)(1,7)(1,8) |
| 2 | [3,9] | 5 | (2,5),(2,6) certs | (2,7)(2,8)(2,9) |
| 4 | [5,11] | 9 | — | (4,9)(4,10)(4,11) |
| >=8 | [ell+1, ell+7] | 2*ell+1 > ell+7 | Newton empties all | — |

One-orbit masses: 512*ell*2^-w; minimum breach 32x the 1/32 threshold at
(4,11) — every open cell is a genuine zero-event obligation, none is
mass-safe. Machine certificate: ../dli_wcl_zone_coverage/
verify_slot_decomposition.py (both ell=1 levels share the (1,w) cells).

## Exact sizing ledger (2026-07-22, Burnside — 3/3 calibration anchors exact)

Ambient affine-Galois orbit counts (exact) and census projections:
(1,5) 2,296,920 [445 CPU-h total; 46.44% banked]; (1,6) 185,569,028
[>=36k CPU-h ~ $6.6k]; (1,7) 1.30e10 [289 CPU-y]; (1,8) 8.06e11 [hopeless];
(2,7) ambient 4.35e11 / router 94,652,815 [33k CPU-h — reproduces Pilot B
exactly; the router is a constraint-first presentation, 4,600x smaller];
(2,8) router 1.86e10 [6.4M CPU-h]; (2,9) router 3.08e12 [1.07e9 CPU-h];
(4,9)/(4,10)/(4,11) 8.07e17/1.64e20/3.01e22 [census infeasible at any rate].
CONSEQUENCE: censuses are live only at (1,5) [finish], (2,7) [after the
GMP-gcd swap + router-soundness for k=5], and marginally (1,6); the ell=4
cells are DESCENT-ONLY (the quartic-divisor (4,9) + straight-line-lift
nodes are proved; (4,10)/(4,11) descent statements + Delta certificates are
the open work); (1,7)/(1,8)/(2,8)/(2,9) need new algebra, not compute.

CENSUS-SOUNDNESS CATCH (mandatory for any future sweep implementation):
prime factors of these cyclotomic norms are NOT all == 1 mod n (roots may
live in extensions; witnessed: 31 divides an order-64 norm). Any
progression-based trial-division shortcut is UNSOUND. Full factoring or
certified partial factoring only.
