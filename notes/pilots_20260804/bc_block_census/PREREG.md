# PREREG — bc_block_census pilot (round 15)

- **node:** `xr_band_forced_commonroot_syzygy_count` (critical, TARGET)
- **obligation of record:** `(BC)` block census, adopted by the round-14
  coordinator audit (`../fr_fiber_rigidity/FABLE_AUDIT.md`)
- **date:** 2026-08-06
- **pilot dir:** `notes/pilots_20260804/bc_block_census/`
- **status at open:** written BEFORE any code is run.

## 0. The obligation, verbatim

From the tasking brief:

```text
(BC) BLOCK CENSUS: for fixed (u, v, P, Q, D) at the tuple-incidence
boundary, |Bset| = #{(nu, tau) : |{x in D : tau(x) = W_nu(x)}| = r,
tau maximal-selected} <= X (= 118/136 at the rows).
```

From the round-14 audit (`../fr_fiber_rigidity/FABLE_AUDIT.md`, verbatim):

> - **(BC) BLOCK CENSUS** as the leaf's obligation of record
>   (|Bset| <= X for fixed (u,v); by the lens a well-posed punctured-RS
>   list count; the sharp unmeasured sub-question = block REUSE across
>   targets, since (WTB) is non-vacuous only under reuse). The
>   empirical |Bset| = 2 (8 runs, one shape) stays EMPIRICAL.

From the consumer (`../commonroot_syzygy/PREREG.md`, verbatim):

> **P1 (WTB — the shared two-block ledger).** Let `Tau` be *any* `D`-local
> target family at the boundary (arbitrary, possibly mixed, fiber profiles),
> with affine hull dimension `s >= 2`. Let `Bset(Tau)` be the set of
> *distinct* selected blocks realised anywhere in `Tau`. Then
>
> ```text
> 2 |Tau intersect plane| <= 3 |Bset(Tau)|,                      (WTB-plane)
> |Tau| * prod_(j=3)^s (w+j) <= (3/2) |Bset(Tau)| * prod_(j=0)^(s-3)(N-j).
>                                                                (WTB)
> ```

## 1. A DEFINITIONAL CATCH, recorded before computing

The brief's parenthetical formula counts **ordered pairs** `(nu, tau)`.
The consumer `(WTB)` defines `Bset(Tau)` as "the set of *distinct*
selected blocks realised anywhere in `Tau`". These are **not the same
number**. By `(TKS2)` (`sigma < r` => exactly two selected live slopes)
every maximal-selected `tau` contributes exactly two pairs, so

```text
#{(nu, tau)} = 2 |Tau|      exactly, always.
```

Under the pair-reading, `(BC)` is *literally equivalent* to
`|Tau| <= X/2` — i.e. to the counting statement the whole lane is trying
to prove. I therefore adopt the **distinct-block reading** (the
consumer's) as the operative one, and record

```text
reuse ratio  R := 2|Tau| / |Bset|   (>= 1),   |Bset| = 2|Tau| / R.
```

`(BC)` has content iff `R` grows with `|Tau|`. This is the crux the audit
named as unmeasured. Both numbers will be reported for every fixture.

## 2. Setting (all constants inherited, none re-derived)

Consumed read-only from the PROVED routers and from the round-14 pilot:

```text
(PP1) K_d={(SP,SQ):S in W},  gcd(P,Q)=1,  ell=max(deg P,deg Q)
(PP4) (f_tau,g_tau)=(f_*+Q tau, g_*-P tau),  deg tau<k-ell
(AD1) rho=P E_* + Q E_*',   D={x in H: rho(x)!=0},   e=|D|
(AD6) B_lambda(tau)={x in D: alpha E_tau(x)+beta E_tau'(x)=0},
      |B_lambda(tau)|=h-d;  blocks of distinct selected slopes disjoint
(TKS1) 2r<=e<=g<=2r+sigma,  r=h-d,  sigma=d-ell-1-2r
(TKS2) sigma<r => exactly two selected live slopes, disjoint r-blocks,
      |D\(B_1 u B_2)|<=sigma
(LENS) B_nu(tau) = {x in D : tau(x) = W_nu(x)},  W_nu = C_nu / L_nu,
       W_nu independent of tau;  W_1-W_2 = delta*rho/(L_1 L_2)
(GATE-r) |psi^{-1}(nu)| <= r for every nu in P^1
```

Boundary shape (tuple-incidence): `ell=floor((h-4)/7)`, `r=2ell+1`,
`d=h-r`, `sigma=h-7ell-4`. Maximality: joint core exactly `k+d`,
`A = k+h`. Write `K := k - ell` (the family's polynomial dimension) and
`Core_tau := {x in H : E_tau(x) = E_tau'(x) = 0}`.

## 3. Predictions

**P1 (the core lens — off-`D` companion of the LENS).** For every `tau`,

```text
Core_tau subset H\D,  and on H\D  (E_*,E_*')(x) = m_x (Q,-P)(x)
for a scalar word m,  so   Core_tau = {x in H\D : tau(x) = m_x}.     (CORE-LENS)
```

I predict this is exact: the maximality condition is *itself* an
agreement condition — `|Core_tau| = k+d` says `tau` agrees with the fixed
word `m` on `k+d` of the `n-e` points of `H\D`. So a target is a pair of
agreement conditions: `k+d` with `m` off `D`, and `r+r` with `W_nu, W_mu`
on `D`.

**P2 (THE ONE-TARGET THEOREM — why the round-14 census read
`|Tau| = 1` eight times out of eight).** Two distinct targets have
`|Core_tau ^ Core_tau'| <= K-1`, so

```text
2(k+d) - (n-e) <= K-1     is NECESSARY for |Tau| >= 2,
i.e.   n >= k + 2d + ell + 1 + e.                               (2-TARGET)
```

At the round-14 toy's pinning `n = 3d+k-c`, `c = sigma+1`, together with
`sigma = d-ell-1-2r` and `e >= 2r`, I predict `(2-TARGET)` **fails by
exactly one point, identically in the shape**. Hence `|Tau| <= 1` is
FORCED at every round-14 shape, `|Bset| <= 2` there is a pigeonhole
artifact, and **the empirical `|Bset| = 2` carries no information about
`(BC)`**.

**P3 (the packing bound).** `K` points determine a target, so the cores
form a constant-weight packing and

```text
|Tau| <= C(n-e, K) / C(k+d, K).                                  (PACK)
```

I predict this is exact-as-stated (a Ray-Chaudhuri--Wilson / Johnson
packing bound), that it has the *same shape* as `(P4F4)`/`(WTB)`
(`prod(N-j)/prod(w+j)`), and that at the prize rows it is astronomically
weak — so `(PACK)` is not a competitor to `(WTB)`, it is its trivial case.

**P4 (route 2 verdict — the list-count route is DEAD at the rows).**
By the LENS the per-slope census is a punctured-RS list count for
`RS_K` restricted to `D`. I predict that **at every prize row
`K = k - ell > e`**, so the restriction map `RS_K -> F_q^D` is
SURJECTIVE: every `r`-subset of `D` is the block of some `tau` at every
slope, and no list-count/Johnson/singleton bound of any strength can
bound `|Bset|`. The list-count route has content only in the toy regime
`K <= e`. There I predict the exact clean bound, per slope,

```text
#blocks at a fixed slope <= C(e, K) / C(r, K)   (~ 2^K for e = 2r),
```

from "every `K`-subset of `D` lies in at most one block".

**P5 (the reuse law — the pre-registered crux).** Because at `sigma = 0`
the two blocks of a target **partition** `D`, sharing one block forces
sharing the other. I predict:

```text
(REUSE LAW)  Bset is a disjoint union of complementary pairs {B, D\B};
  |Bset| = 2 |Pi|,  Pi = the set of realised block-PARTITIONS;
  two distinct targets share a block  <=>  they share their whole
  partition  <=>  they differ in their selected slope pair.
```

Sharp falsifier: two targets sharing **exactly one** block.

**P6 (the freedom count — my honest prior on whether `(BC)` is
provable).** At each `x in D` the received pair `(u_x, v_x)` is 2
scalars; fixing the selected slope of one target at `x` is one affine
condition, fixing a second target's slope at `x` is a second. So:

```text
with |Tau| = 2 both partitions are FREELY choosable;
with |Tau| >= 3 the third and later partitions are FORCED.
```

I therefore predict that at `|Tau| = 2` **both** a full-reuse fixture
(`|Bset| = 2`, `R = 2`) and a no-reuse fixture (`|Bset| = 4`, `R = 1`)
are constructible and pass the entire admissibility stack including the
tangent gate. If so, `R` is a free parameter at `|Tau| = 2`, and `(BC)`
is **not** derivable from the currently proved layer without an
independent bound on `|Tau|` — i.e. `(BC)` is circular as posed. This is
my honest prior and I will report it as a red-leaf negative if it fires.

**P7 (regime axis).** The FR witness sits ABOVE the Johnson radius
(`A/n > sqrt(k/n)`); the prize rows sit BELOW. I predict the *toy* max
codeword agreement is tight (`= A`) only in the above-Johnson,
`n`-pinned regime, and that below Johnson the gate is slack by a wide
margin — so the tangent gate is **weaker**, not stronger, in the prize
regime, and route 3 (a prize-regime-only rigidity mechanism from the
gate) is predicted to FAIL.

## 4. Falsifiers (pre-registered; each kills the corresponding prediction)

**BC-F1 (THE falsifier of (BC); the brief's required one).** A fully
admissible fixture (every clause of the round-14 witness stack: `(AD1)`
`D = supp(rho)`, `dim K_d = sigma+1`, joint core exactly `k+d`, exactly
two live slopes at exact `A`, disjoint `r`-blocks, leftover `<= sigma`,
and an EXHAUSTIVE tangent gate at level `A`) whose distinct-block count
exceeds the budget. At toy scale `X` is unreachable, so I pre-register
the two *scaled* forms and will report which fires:
- **BC-F1a:** any admissible fixture with `|Bset| > 2` (kills the
  round-14 empirical reading `|Bset| = 2`);
- **BC-F1b:** an admissible family with `|Bset| = 2|Tau|` and `|Tau|`
  unbounded by anything but the counting itself (kills `(BC)` at prize
  scale, since `X` is an absolute constant).

**BC-F2 (the reuse-law falsifier).** Two distinct maximal-selected
targets of the same `(u,v,P,Q,D)` sharing **exactly one** block. Firing =
`(REUSE LAW)` of P5 is wrong, `|Bset|` is not `2|Pi|`, and the whole
partition bookkeeping must be redone.

**BC-F3.** A round-14-pinned shape (`n = 3d+k-c`) carrying `|Tau| >= 2`.
(Kills P2 — the one-target theorem — and would mean the round-14
`|Bset| = 2` was informative after all.)

**BC-F4.** A realised family with `|Tau| > C(n-e,K)/C(k+d,K)`.
(Kills P3.)

**BC-F5 (the positive outcome for (BC)).** The no-reuse `|Tau| = 2`
fixture FAILS the exhaustive tangent gate (some deg-`<k` codeword beats
`A`) while the full-reuse fixture PASSES. Firing = the gate is the reuse
engine, `(BC)` has a real mechanism, and I must report the exact
functional that separates them.

**BC-F6 (the honest negative).** Both the reuse and the no-reuse
`|Tau| = 2` fixtures pass every clause including the exhaustive gate.
Firing = reuse is a FREE parameter at `|Tau| = 2`; `(BC)` is circular as
posed and cannot be closed by any argument local to `(u,v,P,Q,D)` that
does not already bound `|Tau|`.

**BC-F7 (regime split).** The reuse behaviour differs across the Johnson
radius: a configuration admissible below Johnson but not above (or vice
versa). Firing = `(BC)` may be provable in the prize regime only, which
is all the consumer needs, and I must state the exact regime predicate.

**BC-F8 (vacuity).** No admissible `|Tau| >= 2` fixture exists at any
shape I can reach. Then the reuse question is untestable at toy scale,
the run is INCONCLUSIVE on route 1, and I must report the exact
obstruction rather than claim either verdict.

**BC-F9 (surjectivity check).** `K <= e` at some prize row. (Kills P4's
"list-count route is dead" claim; the list-count route would then be
live at the rows and route 2 becomes the main attack.)

## 5. Compute discipline

- Every run under `tools/ramguard tiny -- python3 ...` or
  `tools/ramguard local -- python3 ...` from the repo root, literal `--`.
  No bare `python3`. No Modal, no network.
- Exact arithmetic only: Python ints / numpy int64 with explicit `% q`.
  No floats in any load-bearing comparison (the Johnson-radius
  comparisons are done with integer cross-multiplication:
  `A^2` vs `k*n`).
- The round-14 pilot's machinery is imported READ-ONLY via `sys.path`
  (`toy.inv`, `toy.subgroup`, `toy.rank_mod`, `toy.classify`,
  `witness.kernel_basis` where shapes permit). No file under
  `../fr_fiber_rigidity/` is modified.
- The tangent gate is made EXHAUSTIVE and cheap by two devices, both
  stated here before use:
  (a) **bucketing**: a competitor `F` with `agr > A` must agree with
      `U_nu` on `>= A+1-(k-1)` points of `T = H\Core`; splitting `T`
      into `g` buckets with `ceil((A+2-k)/g) >= k` forces some bucket to
      contain `k` agreement points, so enumerating all `k`-subsets
      *inside buckets* is exhaustive;
  (b) **slope-freeness**: `U_nu = alpha u + beta v` is linear in
      `(alpha,beta)`, so for a fixed interpolation subset `S` the
      residuals `R_u, R_v` determine the agreement set of *every* slope
      at once (`x` agrees iff `nu = [R_v(x) : -R_u(x)]`); one histogram
      replaces the loop over `P^1`. The `F = 0` competitor is checked
      separately.
- Every verdict must come from an assertion that FAILS LOUDLY.

## 6. Subtraction notice

Before claiming novelty I check against: the round-13 syzygy pilot's
`(WTB)`/`X`/no-go and its `ledger.py` row constants; the round-14 FR
pilot's LENS / two-ray syzygy / self-fiber avoidance / GATE-r and its
`|Tau| = 1` census; the 14 PROVED `xr_deficient_window_*` routers
(`(PP1-5)`, `(AD1-7)`, `(TKS1-4)`, `(FSP1-7)`, `(CRE1-4)`, `(P4F1-4)`);
`xr_window_system_descent` (W/D/R/L) and its THEOREM R (quoted verbatim
in the round-14 PREREG: "Under the tangent gate, each single-word `d`-row
Toeplitz window matrix has rank exactly `d`" — an over-agreement engine,
NOT a locator engine); `xr_window_divisor_maximality_filter`. The
`(CORE-LENS)`, `(2-TARGET)` and `(PACK)` statements are claimed as new
*only* if no upstream router already states them.

## 7. Honesty declaration

This is a RED LEAF and `(BC)` gates a status-flip chain.
**Partial-with-exact-boundary beats overclaim.** If the honest answer is
"`(BC)` is circular as posed" or "the round-14 evidence for `(BC)` was a
pigeonhole artifact", I say exactly that and give the machine-verified
reason. Every gate verification will carry its exact scope (which
competitor family, which slopes, exhaustive or sampled). No status flip
will be proposed from this pilot alone.
