# PRE-REGISTRATION — TERNARY SMALL-SCALE LAWS: do the instances actually track each other? (round 19, ADVERSARIAL-EMPIRICAL)

Round 19, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. MANDATE: the empirical
stress test of the unification. If the three instances are one object
family, their measured laws at matched small parameters must TRACK
each other where the candidate says they should; if they scale
differently, the unification is wrong no matter how pretty the
formalism. Also: explain (or weaponize) the round-18 anomaly.

## 0. The instances at matched scale (quote the minted nodes first)

- (I1-mini) the GRS-dual ternary mass: 2-power 2N, half-system
  evaluation, R = round(S/log2 p) — the z1 pilot's valid-miniature
  protocol (CATCH-Z6: 2-POWER LENGTHS ONLY — composite lengths
  carry p-independent parasitic relations).
- (I2-mini) single-condition relations: eps in {0,±1}^L,
  sum eps_j theta^j = 0, theta of order 2L — the crossing pilot's
  toy object (its measured orbit law: LEMMA ROT, exactly-2L-orbits,
  over-dispersion).
- (I3-mini) the half-length cyclic ternary object of LEMMA AB — the
  efloor pilot's census machinery (reusable:
  notes/pilots_20260806/efloor_sparsity/sp_lib.py).

## 1. Pre-registered deliverables

- **(L1) THE MATCHED CENSUS.** One exact census framework over all
  three instance shapes at matched (effective length, p, condition
  count) grids — 2-power lengths only, all characteristics at once
  where the HNF/bad-prime method reaches. Measure per instance: the
  relation count law in p at fixed shape; the onset threshold (the
  empirical balance point); the orbit structure; the weighted mass
  vs unweighted count ratio.
- **(L2) THE TRACKING TEST (the adversarial core).** The
  unification predicts: (a) the single-condition instances (I2, I3
  at w' = 2) obey the SAME law after the exact dictionary
  (coordinator's expectation from LEMMA STRAT: I3's binding stratum
  IS an I2 instance — verify the dictionary numerically, exactly);
  (b) I1 at R conditions behaves as R "independent" I2-layers to
  first order (the product/syndrome heuristic — the z1 pilot's
  first-moment-restricted-to->2R law). MEASURE both. A significant,
  structured deviation that the dictionaries cannot absorb is a
  REFUTATION of the unification's quantitative content — report it
  as such with the exact deviation law.
- **(L3) THE ANOMALY.** Round-18 efloor residual 4: at n = 32,
  p = 5, w = 2 the flat model predicts ~110 nonzero ternary
  codewords; the exact count is 0. Explain it: is it the
  SP-TERNARY mechanism, a Gauss-sum exactness effect (2-power
  conductor), the orbit over-dispersion, or something new? Whatever
  the mechanism, test whether it appears in the OTHER instances at
  matched parameters — a shared anomaly is the best possible
  positive evidence for the unification; an instance-local one is a
  disanalogy datum.
- **(L4) THE SCALING VERDICT.** For each measured law: does it
  extrapolate consistently ACROSS instances toward their respective
  prize regimes (I1 at p ~ 2^64, I2 at p ~ 2^129, I3 at the
  official q), or do the instances leave the shared regime at
  different rates? No prize-row claims — the deliverable is the
  small-scale consistency verdict with honest scale caveats.

## 2. Pre-registered falsifiers / honesty clauses

- A structured tracking deviation (L2) that survives the exact
  dictionaries = the unification's quantitative refutation. Do not
  absorb deviations into free parameters post hoc — dictionaries
  must be stated BEFORE measuring.
- The composite-length rule is absolute except in one labelled
  control cell (deliberately composite, to reproduce CATCH-Z6's
  parasitic relations as the negative control).
- Nulls from unreached grid cells are reported as unreached.

## 3. Rules of engagement

- DRAFT ONLY: write only inside
  notes/pilots_20260806/tern_small_scale_laws/. Never edit dag.json,
  node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/tern_route_b/ (sibling independence). You
  MAY reuse banked machinery: efloor_sparsity/sp_lib.py,
  es_coprimality/cop_lib.py, crossing_low_w/low_w_lib.py,
  z1_ternary_mass artifacts — all banked, not sibling-active.
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

---

# APPENDED BY THE PILOT — 2026-08-06, BEFORE ANY COMPUTATION

Everything below was written before a single census was run. Nothing in
this section is edited afterwards; corrections, if any, are recorded in
`PROOFS.md` as self-catches with the original text left standing.

## A. The one framework (registered shape)

All three instance miniatures are censused by ONE routine

```text
CT(N, p, T) := { v in {0,+-1}^N  :  sum_{i<N} v_i * omega^{s i} = 0
                                    in F_{p^delta}, for every s in T }
```

with `M := 2N`, `omega` a fixed primitive `M`-th root of unity in char `p`
(concretely `omega = X mod g`, `g` the first — sorted — irreducible factor
of `X^N + 1` over `F_p`, the SAME convention as the banked
`efloor_sparsity/verify_sp.py:467`, `SP.syndrome_columns(n,p,w,[fs[0]],reps)`),
and `T <= Z/M` any set closed under multiplication by `p`.

Registered instance dictionary (the shapes, not yet the laws):

- **I3**`(n, p, w)`   = `CT(N = n/2, p, T = <p>-closure of {odd s in [1,w-1]})`.
- **I2**`(L, p)`      = `CT(N = L,   p, T = <p>-closure of {1})`.
- **I1**`(2N, p, R, a)` = `CT(N, p, T = <p>-closure of {a, a+1, ..., a+R-1})`,
  with `p = 1 mod 2N` (structurally forced: the evaluation points are the
  half-system of `mu_{2N} <= F_p^*`, `f2_adm/PROOFS.md:232-235`), so
  `<p> = {1}` and `T = {a,...,a+R-1}` exactly.

Note the registered ASYMMETRY: `I3` and `I2` have all-ODD `T`; `I1`'s `T`
is a consecutive window and for `R >= 2` contains BOTH parities. This is
registered now because prediction P2 turns on it.

## B. Registered grids

- **G-A (2-power, the only valid miniatures — CATCH-Z6).**
  `M = 2N in {8, 16, 32, 64}`, i.e. `N in {4, 8, 16, 32}`.
  `N = 32` is attempted; if it exceeds the COMPUTE LAW it is reported
  UNREACHED, never estimated.
- **G-B (the ONE labelled composite negative control).** `M in {12, 24}`
  (`N in {6, 12}`), deliberately composite, to reproduce CATCH-Z6's
  `p`-independent parasitic relations. Results from G-B are never mixed
  into any G-A law.
- **primes.** I3 grid: every odd prime `p <= 61`. I1/I2 grid: the primes
  `p = 1 mod 2N` (I1's structural constraint), smallest six per `N`.
- **windows.** I3: `w in {2,4,6,8}`. I2: the single condition. I1:
  `R in {1,2,3,4}`, shifts `a in {0,1,2,3}`.

## C. Registered dictionaries (stated BEFORE measuring)

- **(D1) the LEMMA STRAT dictionary, I2 <-> I3.** For every `L, p`:
  the I2 relation set `{eps in {0,+-1}^L : sum_j eps_j theta^j = 0,
  ord(theta) = 2L}` equals, **as a set of vectors under the identity map
  `eps_j = v_j`, `theta = xi`**, the I3 ternary code at `n = 2L`, `w = 2`.
  FALSIFIER: any cell where the two vector sets differ.
- **(D2) I1 <-> I2 at one condition.** `I1(2N, p, R=1, a=1)` ternary
  kernel `=` `I2(L=N, p)` relation set, identity map, for `p = 1 mod 2N`.
  FALSIFIER: any cell where they differ.
- **(D3) the multiplicity dictionary (weighted mass <-> unweighted count).**
  Put `Z(N,p,T) := sum over ALL v in CT (including v=0) of 2^{-wt(v)}`
  (the z1 mass, `z1_ternary_mass/PROOFS.md:19`) and
  `Sct(N,p,T) := sum over NONZERO v in CT of 2^{z(v)}`, `z(v) = #{i: v_i=0}`
  (the efloor S-count, `efloor_sparsity/PROOFS.md:308-309`).
  REGISTERED IDENTITY:
  ```text
  Sct  =  2^N * (Z - 1).
  ```
  FALSIFIER: any cell where it fails. (This is the registered claim that
  the efloor S-count and the z1 weighted mass are the SAME functional.)

## D. Registered predictions (the tracking test, L2)

- **(P1) independent layers, I1 at R conditions.** Registered null law:
  `#{v != 0} ~ (3^N - 1) / p^{rk}`, `rk` = the exact `F_p`-rank of the
  condition system. Reported as the ratio measured/predicted; a ratio
  that is structured in `R` (not noise) is the deviation L2 asks for.
- **(P2) orbit quantization and its registered BREAK.** The kernel is
  closed under `v -> -v` always; under the negacyclic twisted rotation
  `R_neg` (`crossing_low_w/PROOFS.md:330-332`, order `2N`) **iff every
  `s in T` is odd**; under the plain cyclic rotation (order `N`) **iff
  every `s in T` is even**. REGISTERED CONSEQUENCE: `I1` at `R >= 2` has a
  mixed-parity window, so NEITHER survives, and `I1` at `R >= 2` **loses
  the `2N`-orbit quantization that I2 and I3 always have**. FALSIFIER
  both ways: `2N`-orbits observed at I1 `R >= 2` refutes P2; orbit sizes
  not dividing `2N` at I2/I3 refutes LEMMA ROT's transport.
- **(P3) THE ANOMALY MECHANISM — registered before measuring.**
  Registered hypothesis **SELF-ORTH**`(N,p,T)`: `T u (-T)` contains every
  odd residue mod `2N`. Registered claim:
  ```text
  LEMMA TWT (ternary weight theorem).  If SELF-ORTH holds, then every
  nonzero v in CT(N,p,T) has  p | wt(v).
  ```
  Registered consequence at the round-18 anomaly cell `(n=32, p=5, w=2)`:
  SELF-ORTH holds, `5 | wt` forces `wt in {5,10,15}`, the admissible
  ternary population drops from `3^16 = 43046721` to
  `C(16,5)2^5 + C(16,10)2^10 + C(16,15)2^15 = 8864256`, and the corrected
  flat prediction is `8864256 / 5^8 = 22.69` vectors `= 0.709` orbits
  after the `2N = 32` orbit correction — so an exact count of **0** is
  UNREMARKABLE (`P(0) ~ e^{-0.709} = 0.49`), not an anomaly.
  FALSIFIERS: (i) any ternary kernel vector with `p` not dividing `wt` in
  a SELF-ORTH cell REFUTES LEMMA TWT and voids this explanation;
  (ii) if weights are ALSO `p`-divisible in non-SELF-ORTH cells, the
  mechanism is misidentified and must be re-derived.
- **(P4) anomaly transport — the shared-vs-local test (L3's real question).**
  SELF-ORTH is a property of `(2N, p, T)` alone, hence in principle
  shared. But I1 structurally forces `p = 1 mod 2N`, so `<p> = {1}` and
  `|T| = R`; SELF-ORTH then needs `R >= N/2`. REGISTERED PREDICTION: **no
  I1 miniature at `R <= 4` with `N >= 8` satisfies SELF-ORTH, so the
  anomaly is INSTANCE-LOCAL to I3/I2 at non-split primes — a DISANALOGY
  datum, not shared positive evidence.** FALSIFIER: an I1 cell at
  `R <= 4`, `N >= 8`, with SELF-ORTH true.
- **(P5) the composite negative control.** At `M in {12,24}` there exist
  `p`-INDEPENDENT ternary kernel vectors (the same vector for every
  admissible `p`); at 2-power `M` there are none. FALSIFIER: either
  direction failing.
- **(P6) the onset threshold.** Registered empirical balance point: a
  nonzero ternary kernel exists iff
  `N*log2(3) - rk*log2(p) - log2(2N) >~ 0`, the orbit-corrected
  functional of `crossing_low_w/PROOFS.md:196`. Measure the crossing
  and its width; report the observed threshold constant.

## E. Registered controls (fail-closed; a failure VOIDS the pilot)

- **(C1) replication of the banked table.** My framework must reproduce
  `efloor_sparsity/PROOFS.md:320-326` EXACTLY: at `n=32`, `w=2`, the
  nonzero ternary counts `6560 / 0 / 16640 / 148224` for
  `p = 3 / 5 / 7 / 17`, and the `w=4,6,8` rows. A mismatch voids
  everything downstream.
- **(C2) factor-independence.** The ternary count must not depend on
  which irreducible factor of `X^N+1` is chosen (the choice is a
  monomial change of coordinates). Verified, not assumed.
- **(C3) two disjoint code paths.** Every count small enough is verified
  by BOTH brute-force enumeration over `3^N` and the meet-in-the-middle
  census; disagreement is a hard failure.
- **(C4) nulls from unreached cells are reported UNREACHED.**
