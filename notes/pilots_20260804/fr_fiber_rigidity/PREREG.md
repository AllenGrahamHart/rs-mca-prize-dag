# PREREG — fr_fiber_rigidity pilot (round 14)

- **node:** `xr_band_forced_commonroot_syzygy_count` (critical, TARGET)
- **obligation of record:** `(FR)` fiber rigidity, adopted by the round-13
  coordinator audit (`../commonroot_syzygy/FABLE_AUDIT.md`)
- **date:** 2026-08-06
- **pilot dir:** `notes/pilots_20260804/fr_fiber_rigidity/`
- **status at open:** written BEFORE any code is run.

## 0. The conjecture, verbatim

```text
(FR) FIBER RIGIDITY: at the tuple-incidence boundary, every selected
block is a union of full phi-fibers of D together with at most one
further point.
```

Granting (FR), the proved (WTB) ledger gives `beta <= 6t <= 42 < X =
118/136`, closing every stratum at `s <= 11/11/10`.

## 1. Correction to the tasking brief (recorded before computing)

The brief names `xr_window_system_descent` **THEOREM R** as "rank
deficiency forces a Berlekamp-Massey error locator — the natural (FR)
engine". Reading the node, THEOREM R is the *opposite* statement:

> 3. **Single-word rank R.** Under the tangent gate, each single-word
>    `d`-row Toeplitz window matrix has rank exactly `d`.

The Berlekamp-Massey step appears only inside its proof, and it is used
**to exclude** rank deficiency (a BM locator of degree `<= d-1` would put
`u` within distance `d-1` of `RS_k`, i.e. at agreement `> A`,
contradicting the tangent gate). So BM is not an (FR) engine; it is an
**over-agreement engine**. That is the same mechanism as the L-B
DICHOTOMY (`notes/pilots_20260803/lb_escape1_overagreement/`), and this
pilot adopts the over-agreement reading as route 1. Recorded as a
brief-staleness catch, in the same class as round 13's.

## 2. Setting (all constants inherited, none re-derived)

Consumed read-only from the PROVED routers:

```text
(PP1) K_d={(SP,SQ):S in W},  gcd(P,Q)=1,  ell=max(deg P,deg Q)
(PP3) P(x)E(x)+Q(x)E'(x)=0 for x in H\G_d
(PP4) (f_tau,g_tau)=(f_*+Q tau, g_*-P tau),  deg tau<k-ell
(AD1) rho=P E_* + Q E_*',   D={x in H: rho(x)!=0},   e=|D|
(AD5) L_lambda=alpha Q-beta P,  deg L_lambda<=ell
(AD6) B_lambda(tau)={x in D: alpha E_tau(x)+beta E_tau'(x)=0},
      |B_lambda(tau)|=h-d;  blocks of distinct selected slopes disjoint
(TKS1) 2r<=e<=g<=2r+sigma,  r=h-d,  sigma=d-ell-1-2r
(TKS2) sigma<r => exactly two selected live slopes, disjoint r-blocks,
      |D\(B_1 u B_2)|<=sigma
(TKS4) official sigma = 5,5,1
```

Definition of record (`notes/BAND_LANE_DEFINITIONS.md` item 7): **live
slope** := exact-`A` max agreement over ALL of `P^1` including `(0:1)`;
selected support := the ONE first-match exact-`A` ray. Maximality
(`xr_band_maximal_window_divisor_count` clause 2): the reconstructed
pair's full joint core is exactly `H\T`, of size `k+d`. Hence
`A = k+h`, `|Core| = k+d`, and each selected ray buys exactly `r = h-d`
further agreement points, all inside `D`.

**Boundary shape** (tuple-incidence): `ell=floor((h-4)/7)`, `r=2ell+1`,
`d=h-r`, `sigma=h-7ell-4`.

## 3. Predictions

**P1 (master two-ray syzygy).** With `R_nu := C_nu - tau L_nu` the
ray-`nu` residual (`C_nu = alpha E_* + beta E_*'`), and
`delta := alpha_2 beta_1 - alpha_1 beta_2 != 0`:

```text
R_2 L_1 - R_1 L_2 = -delta * rho          identically in F[X].   (II)
```

I predict this is an exact polynomial identity (not merely a congruence
on `H`), and that it is the correct home for "forced common root".

**P2 (self-fiber avoidance).** For **every** slope `nu` in `P^1`,

```text
B_nu ^ phi^{-1}(nu) = empty.                                     (A)
```

I predict this is a two-line consequence of `rho != 0` on `D`, and in
particular that a selected block never meets the `phi`-fiber of its own
slope. Corollary: `phi^{-1}(lambda_1) ^ D subset B_2 u Leftover`.

**P3 (the selection lens / family lens).** Setting
`W_nu := C_nu / L_nu` (a function on `D` that does **not** depend on
`tau`),

```text
B_nu(tau) = {x in D : tau(x) = W_nu(x)},                         (LENS)
W_1 - W_2 = delta * rho / (L_1 L_2).
```

I predict the block census is therefore *exactly* an RS-agreement census
on `D`: blocks of slope `nu` across the family are the size-`r`
agreement sets of `RS_{k-ell}` codewords with the fixed word `W_nu`.

**P4 (gate-r).** Extending `psi(x) := [E'(x):-E(x)]` to all of
`H\Core` (it equals `phi` off `D`), the tangent gate at level `A=k+h` is
exactly

```text
|psi^{-1}(nu)| <= r  for every nu in P^1,                        (GATE-r)
```

with equality precisely at the selected slopes. I predict this is the
sharpest correct form of "no over-agreement" in this lane.

**P5 (the (FR) verdict — my honest prior).** I predict **(FR) is NOT
forced by the currently proved layer**: a realised admissible pair whose
selected block splits a `phi`-fiber by `>= 2` points EXISTS at the
smallest tuple-incidence boundary shape that can pose the question. My
reason, recorded now: in the per-pair construction every constraint I can
identify — `(AD1)`-`(AD7)`, `(TKS1)`-`(TKS4)`, ray exactness, the
deficiency/primitivity of `(P,Q)` — is satisfiable by free choice of the
pointwise scalars `c_x` (on `D`) and `m_x` (off `D`), because the
received words `u,v` are unconstrained. If so, **(FR) is a
FAMILY-level statement or it is false**, and route 3 returns a
refutation rather than a theorem.

**P6 (smallest decisive shapes).** I predict:
- `h=18` gives `ell=2, r=5, d=13, sigma=0, e=10` — the smallest boundary
  shape, but it **cannot** pose the strong falsifier (a fiber cannot be
  split by `>= 2` points when fibers have size `<= ell = 2`), and it
  violates the load-bearing `ell > sigma+2`.
- `h=25` gives `ell=3, r=7, d=18, sigma=0, e=14, t=2` — the smallest
  shape with `ell > sigma+2` **and** room to split a fiber by `>= 2`
  points. This is the decisive shape.
- The ambient `n` is pinned by `dim K_d = 1`: `n = 3d + k - 1`.

## 4. Falsifiers (pre-registered; each kills the corresponding prediction)

**FR-F1 (THE falsifier of (FR); the brief's required one).** A realised
admissible pair whose selected block splits a `phi`-fiber by `>= 2`
points — i.e. some fiber `F` with `2 <= |B ^ F| < |F|`. Firing = (FR)
REFUTED at that shape, and the syzygy leaf's obligation of record must be
re-posed.

**FR-F2 (weak violation).** A realised admissible pair whose selected
block splits two distinct `phi`-fibers by one point each (no fiber split
by `>= 2`, but more than "one further point"). Firing = (FR) as literally
worded is refuted; the `6t` count may still survive under a repaired
wording, which I will then state exactly.

**FR-F3.** Identity `(II)` failing on any instance. (Kills P1 — my
algebra is wrong; everything downstream is void.)

**FR-F4.** A point `x in D` with `psi(x) = phi(x)`, or a selected block
meeting its own slope's fiber. (Kills P2.)

**FR-F5.** `B_nu(tau)` depending on `tau` other than through
`tau(x) = W_nu(x)`, or `W_nu` depending on the base pair `(f_*,g_*)`.
(Kills P3/LENS.)

**FR-F6.** `|psi^{-1}(nu)| > r` for some `nu` in a configuration that
otherwise passes every admissibility check. (Kills P4; would mean the
gate is not the binding constraint.)

**FR-F7 (the positive outcome).** The exhaustive search at the decisive
shape finds **zero** realised admissible pairs with a fiber-splitting
selected block, while finding at least one `(FR)`-compliant realised
pair. Firing = **(FR) PROVED for that shape by exhaustion** (0-liveness),
P5 refuted, and route 3 delivers a theorem.

**FR-F8 (empty-shape failure).** No realised admissible configuration at
all at the decisive shape, `(FR)`-compliant or not. Then the toy is
vacuous, the run is INCONCLUSIVE, and I must move up a shape rather than
claim either verdict.

**FR-F9 (the exchange signal).** Fiber-splitting configurations exist but
every one of them fails the tangent gate (some codeword beats `A`), while
fiber-completing ones pass. Firing = route 2 (first-match exchange /
forced over-agreement) is the real (FR) engine, and I must report the
exact functional that fires.

## 5. Compute discipline

- Every run under `tools/ramguard tiny -- python3 ...` or
  `tools/ramguard local -- python3 ...` from the repo root, literal `--`.
  No bare `python3`. No Modal, no network.
- Exact arithmetic only: integers and `F_q` with `q` prime, via Python
  ints / numpy int64 with explicit `% q`. No floats in any load-bearing
  comparison.
- Enumerated spaces kept below `10^8` elementary operations per run; if a
  run needs more, redesign rather than raise the profile.
- Every verdict must come from an assertion that FAILS LOUDLY, not from a
  printed number I eyeball.

## 6. Subtraction notice

Before claiming novelty I check against: the 14 PROVED
`xr_deficient_window_*` routers (label families `(RD)(FR-of-RD)(PAY)(LOC)`,
`(PP1-5)`, `(AD1-7)`, `(LA1-3)`, `(MCB1)`, `(APT1-3)`, `(ACP1-3)`,
`(FSP1-7)`, `(FAT1-4)`, `(CRE1-4)`, `(UE1-3)`, `(ABN1-2)`, `(TKS1-4)`,
`(P4F1-4)`), `xr_window_system_descent` (W/D/R/L),
`xr_window_divisor_maximality_filter` (F/PF/INV/S/BON), the round-13
syzygy pilot's `(WTB)`/`X`/no-go, and the L-B pilot's LEMMA P / THEOREM F
/ DICHOTOMY. Note that `xr_deficient_window_rational_direction_payment`
already uses the label `(FR)` for a *different* statement (forced-root);
this pilot's `(FR)` is the coordinator's fiber-rigidity conjecture, and I
will flag the collision.

## 7. Honesty declaration

This is a RED LEAF and (FR) feeds a status-flip chain.
**Partial-with-exact-boundary beats overclaim.** If the answer is
"(FR) is false as worded", I say so and give the explicit counterexample
with every admissibility check listed and its verification scope stated.
If the tangent gate is verified only on a restricted codeword family, I
say exactly which. No status flip will be proposed from this pilot alone.
