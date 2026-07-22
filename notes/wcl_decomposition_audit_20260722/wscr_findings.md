# wscr_findings.md — WCL slot-hardening item 6: powered falsifier-sampling screens

Repo: /home/u2470931/smooth-read-solomin/prize @ master 570f0067 (READ-ONLY).
Conventions: audited (notes/wcl_decomposition_audit_20260722/wcl_audit_findings.md):
cell (ell,w) = reduced signed weight-w supports (antipodal-free w-subsets of
Z_{512*ell}, signs mod global sign), omega EXACT order 512*ell, event iff the
ell odd-power vanishings P(omega^(2j-1))=0 have their obstruction integer
divisible by an official prime (q < 2^256, v_2(q-1) >= 41).
Compute law: every run `tools/ramguard local -- python3 ...` (1 GB / 5 min);
every screen designed <= 4.5 min per invocation.  NO Modal.
Script: wscr_screens.py (this directory).  Base seed: `wscr-20260722`.

## Machinery provenance

- ell=1 norms + probable-prime test: REUSED from the prior agent's audited
  wsz_weight5.py (`norm_of_set`/`norm_rec` selfchecked there against sympy
  resultants; coset-descent identity Norm_512 = Norm_256^2 proved).  Rows
  with parity-uniform support are screened at their descended (primitive)
  order — identical prime support, exact.
- (2,7) router pipeline: REIMPLEMENTED pure-Python (no flint on this host),
  formula-for-formula from the audited reference
  notes/kernel_basis/wclp_sizing_20260719/wclp_b_sample_modal.py
  (cleared cubic sigma_1=-u^2, theta_1=u*w, e3=u^3 d; ten doublings;
  F = sigma_1024 - 3u^1024, G = theta_1024 - 3u^2048; recursive power-of-two
  norms; gcd; Norm(u)-saturation).  Ring multiplication in Z[X]/(X^512+1)
  via signed Kronecker substitution + balanced-digit unpack (exact integers).
- SATURATION SOUNDNESS (wclp finding #9, adopted): for (2,7) the Norm(u)
  saturation has no paid single-equation weight-4 exclusion backing it, so
  the screen ALSO factors the u-shared part gcd(g0, Norm(u)) and screens its
  primes for admissibility (route (a), refined: only primes dividing the raw
  gcd can be event primes).
- Powered tail (all screens): boosted Pollard p-1 stage 1 with exponent
  E = (order << 260) * prod_{p<=60000} p^floor(log_p 60000): detects ANY
  prime q | n with q-1 | E — in particular every official-admissible prime
  (v_2 <= 255 < 260 covered in full) whose ODD part of q-1 is
  60000-powersmooth.  Run on every composite before rho; every unresolved
  cofactor carries a `smooth_clear` certificate bit from this detector.
- Banked catch honored: NO assumption that norm primes are == 1 mod n
  anywhere (pm1's order multiplier only enriches E; detection statement is
  purely q-1 | E).  Factor classification is probable-prime (labeled;
  Miller-Rabin, deterministic bases + 24 seeded extras above 2^81).

## Verdict semantics (uniform across screens, pre-registered)

- EVENT / EVENT_CANDIDATE: a certified/probable prime q with q < 2^256 and
  v_2(q-1) >= 41 divides the row's obstruction integer.  FATAL for the slot
  expectation — full witness written to wscr_EVENT_witness.json immediately.
  (For (2,7) an alarm is EVENT_CANDIDATE: root-legality/reducedness of the
  reconstructed triple would still need confirmation.)
- SURVIVED_CERTIFIED (incl. SURVIVED_UNIT): obstruction completely factored
  (probable-prime level), no admissible factor.  Full per-row power.
- SURVIVED_PARTIAL: unresolved composite cofactor(s) — NOT an event; caps
  the row's power at: no admissible prime among found factors, and (when
  smooth_clear) no admissible prime with 60000-powersmooth odd part hides in
  the unresolved tail.  Honest count reported per screen.
- Screens are SAMPLES: zero events moves the slot floor from untested to
  TESTED-WITH-POWER at the stated sample size/measure; it excludes nothing.

## Sampling measures (honest limitation, applies to all four screens)

Draws are uniform over the natural presentation spaces (reduced signed
supports; legal normalized router presentations), i.e. orbit-size-weighted
over orbits — exact orbit-uniform sampling is infeasible without full orbit
enumeration.  Per-index deterministic seeding (`wscr-20260722:<tag>:<i>`),
reproducible; duplicates rejected by canonical orbit key.  Calibration
pilots use disjoint `:pilot*` seed streams — pilot rows are NOT part of any
registered sample.

---

## Selfcheck + calibration (before any registered run)

SELFCHECK (ramguard local): 6/6 PASS —
SC1 Kronecker mul vs schoolbook (incl. 512x512, coefficients to 2^999);
SC2 recursive_norm vs the audited wsz norm_rec at width 512 + sympy
resultant at width 16; SC3 EXACT mod-q (q=12289, 1024 | q-1) validation of
the (2,7) chain: split-cubic doubling recurrence vs scalar root arithmetic
at every level k=1..10 AND recursive_norm(F/G/u) vs the direct 512-conjugate
product mod q at full production size (no tolerances); SC4 orbit-invariance
of both canonicalizations under 15 random group elements each; SC5 powered
pm1 detector positive control (pulls q0 = 3*2^41+1 = the smallest official-
admissible prime out of q0*p100) + classifier gate control (12289 flagged at
gate 10, not at gate 41); SC6 factor-screen reassembly on a real (1,5) norm.
(First SC3 draft used mpmath polyroots and FAILED on numerics; replaced by
the exact mod-q check — stronger, and it passes.  No production code path
was affected.)

CALIBRATION pilots (disjoint :pilot* seeds, ramguard local):
- ell=1 rows: typical (1,5) norms ~190-213 bits, (1,6) ~227-247, (1,7)
  ~238-294 (the 594/661/718-bit figures in the sizing note are worst-case
  BOUNDS, not typical values).  Easy rows certify in 0.01-0.1 s; hard rows
  leave ONE ~170-250-bit semiprime-ish cofactor that local rho cannot crack
  at any lawful budget (production used gp ECM/MPQS on Modal for these) —
  they burn the full rho budget and land SURVIVED_PARTIAL with smooth_clear.
  Pilot certified fractions at 3 s/row: (1,5) 3/8, (1,6) 4/6, (1,7) 3/4.
- (2,7) rows (3 pilot orbits, all SURVIVED_CERTIFIED): pure-Python
  ~7.8-8.8 s/orbit.  Bit profile matches the banked Modal pilot EXACTLY:
  n1 610-626k bits (banked ~632k), n2 1,095-1,131k (banked ~1,140k),
  Norm(u) 293-316 (banked ~318), raw gcd 151-162k (banked ~164k),
  saturated gcd 66-282 bits (banked deciles 1-199).  Phase split local:
  recurrence 2.3-2.7 s, Norm(F) 1.1-1.3 s, Norm(G) 2.8-3.7 s, gcd
  0.77-0.99 s (banked flint-container gcd 1.095 s — same CPython math.gcd),
  saturate 0.07-0.08 s, factor 0.1-0.95 s.
  => (2,7) screen rate is ~6.8x the banked flint rate; per the compute law
  the sample SHRINKS to the sanctioned fallback 150 orbits, run as 6
  ramguard shards x 25 orbits (~220 s each; sharding precedent: the prior
  agent's 8-shard coset census, same law).

---

## PRE-REGISTRATION — screen 1: (1,5) irreducible-core sample

- Population: the 2,265,060-orbit irreducible core = all (1,5) orbits MINUS
  the proved subfamilies (coset-of-4Z tower = primitive order <= 128,
  31,578 orbits; symmetric R = c-R, 360 orbits; overlap 78).  Membership is
  orbit-invariant and tested directly on the drawn support: reject iff all
  residues mod 4 equal, or exists c with R = c-R.  The OPEN order-256 coset
  layer (parity-uniform, mixed mod 4) stays IN and is screened at its
  descended order (exact by the proved descent identity).
- Sample: N = 400, seeds `wscr-20260722:15core:i`, i = 0..399; uniform over
  reduced signed supports restricted to the core (orbit-size-weighted);
  duplicate canonical keys rejected.
- Pipeline: exact integer Norm at primitive order; timed factor screen
  (small primes <= 1e6, perfect powers, boosted pm1 with
  E = (order<<260)*smooth(60000), Brent rho to row deadline 0.45 s);
  global soft deadline 250 s (honest early stop if hit).
- Falsifiable expectation: ZERO events.  One admissible prime factor
  (q < 2^256, v_2(q-1) >= 41) of any sampled norm = EVENT = the (1,5) slot
  conjecture is FALSE — fatal, full witness reported immediately.
- SURVIVED verdicts and the power cap: as in the semantics block above;
  the screen's power = certified fraction at full strength + powered-pm1
  smooth-tail strength on partial rows.  Also recorded: max v_2(q-1) over
  ALL certified/probable prime factors, per-row timing med/p95.

### RESULT — screen 1 (wscr_screen_15core.json)

**400/400 rows, ZERO EVENTS.**  max v_2(q-1) over every certified/probable
prime factor: **17** (gate 41).  Verdicts: 201 SURVIVED_CERTIFIED (complete
probable-prime factorization), 199 SURVIVED_PARTIAL (one-or-two unresolved
~150-250-bit composite cofactors each; **187/199 smooth-clear** — the
boosted-pm1 detector certifies no admissible prime with 60000-powersmooth
odd part hides in them; the other 12 hit the pm1 all-factors-clump case
g == n and carry only the certified-factor guarantee).  0 unit-norm rows.
Rejections during draw: 4 coset-of-4Z, 0 symmetric, 0 duplicate (matches
expected support-measure fractions).  Wall 106.6 s; row med 0.44 s /
p95 0.55 s (med is budget-dominated: partial rows burn the full 0.45 s rho
deadline; certified rows finish in 0.01-0.1 s).
Certified power: 50.3% of rows at full strength, 97.0% at
full-or-smooth-tail strength, 3.0% capped at certified-factor strength.

---

## PRE-REGISTRATION — screen 2: (2,7) router sample + gcd-stage timing pilot

- Population: the 94,652,815-orbit router space (audited presentation:
  selected quadruple {1, z^a, z^b, z^e} normalized + complement triple with
  free product d = z^c; orbits = quotient by odd dilation x rebasing).
  Reconstructed formula-for-formula from the audited (2,6)-certificate
  machinery / wclp_b_sample_modal.py reference; validated by selfcheck SC3
  (exact mod-q) and by reproducing the banked bit profile (calibration).
- Sample: N = 150 (the pre-sanctioned fallback from 200 — pure-Python rate
  is ~8.5 s/orbit vs the banked 1.25 s flint rate; the compute law says
  SHRINK, never raise the profile).  Seeds `wscr-20260722:27:i`, i = 0..149;
  uniform over legal normalized presentations (orbit-size-weighted);
  duplicate canonical orbit keys assert-checked at merge.  6 ramguard
  shards x 25 orbits (i mod 6 == shard), soft deadline 245 s per shard.
- Pipeline (per orbit): cleared cubic + ten doublings; F, G; exact
  recursive norms; g0 = gcd(Norm F, Norm G); Norm(u)-saturation PLUS the
  route-(a) u-shared part gcd(g0, Norm u) (wclp finding #9 soundness fix);
  timed factor screen (2.0 s cap) on both; admissibility gate on all found
  primes.
- Falsifiable expectation: ZERO event-candidates; secondary expectations
  from the banked Modal pilot: zero-branch count 0 (finding #10: vacuous at
  weight 7), saturated gcds mostly < ~300 bits, nontrivial-gsat fraction
  ~90%+.
- EVENT_CANDIDATE = admissible prime divides the obstruction (fatal-class,
  witness written; root-legality confirmation would follow).  SURVIVED as
  in the semantics block.
- Timing-pilot deliverable (for the projection ledger): per-phase med/p95
  over the sample — recurrence, Norm(F), Norm(G), Norm(u), gcd, saturate,
  factor — plus whole-row med/p95, explicitly labeled pure-Python-local
  (the gcd/saturate phases are CPython math.gcd in BOTH stacks and are the
  transferable numbers; the banked flint container did recurrence+norms
  ~24x faster).

### RESULT — screen 2 (wscr_screen_27router.json, 6 shards merged)

**150/150 orbits, ZERO EVENT-CANDIDATES.  Zero-branch rows: 0** (secondary
expectation confirmed — finding #10's weight-7 vacuity).  max v_2(q-1)
over all certified/probable primes: **16** (gate 41).  No duplicate orbits.
Bit profile vs the banked Modal pilot (validation of the reconstruction):
n1 med 630,660 (banked ~632k), n2 med 1,137,702 (banked ~1,140k), raw gcd
med 162,711 (banked ~164k), saturated gcd med 83 bits / max 1,706 (banked
deciles 1-199, max 1,625).
Verdicts: 34 SURVIVED_CERTIFIED, 116 SURVIVED_PARTIAL (101 smooth-clear,
15 clumped).  HONEST NOTE: the partial fraction is dominated by the
route-(a) u-shared part (gcd(g0, Norm u), ~300-bit composites) — wclp #9's
"factor Norm(u), cheap" holds for gp/ECM on Modal but NOT for local rho;
the saturated gcds themselves (med 83 bits) factor fine.  Census designers
should keep gp/ECM in the loop for route (a).
**Timing pilot (pure-Python local, med/p95 s):** recurrence 2.470/3.092,
Norm(F) 1.098/1.426, Norm(G) 3.031/3.622, Norm(u) 0.001/0.001,
**gcd 0.767/0.993** (transferable: CPython math.gcd in both stacks; banked
flint-container gcd 1.095 s), saturate 0.068/0.088, factor 2.000/2.203
(budget-saturated at the 2.0 s cap), row 9.347/10.986, max 12.300.
Wall: 6 shards x 229-232 s.
Certified power: 22.7% full strength, 90.0% full-or-smooth-tail, 10.0%
capped at certified-factor strength.

---

## PRE-REGISTRATION — screen 3: (1,6) uniform sample

- Population: the full 185,569,028-orbit (1,6) affine-Galois orbit space
  (no exclusions — no proved subfamilies are banked at (1,6)).
- Sample: N = 256, seeds `wscr-20260722:16:i`, i = 0..255; uniform over
  reduced signed supports C(256,6)*2^5 (orbit-size-weighted); duplicate
  canonical keys rejected; parity-uniform supports screened at their
  descended order (exact).
- Pipeline: as screen 1 with row rho deadline 0.75 s; global soft deadline
  250 s.  Even weight => Norm may be even; powers of 2 stripped (2 is not
  admissible); Norm != 0 still guaranteed (Lam-Leung + antipodal-free).
- Falsifiable expectation: ZERO events.  Secondary purpose: factor-stage
  cost growth vs (1,5) for the projection ledger (typical-norm bits and
  certified fraction at the bigger weight; the sizing table's 661-bit
  figure is the worst-case bound, calibration says typical ~230-250 bits).

### RESULT — screen 3 (wscr_screen_16.json)

**256/256 rows, ZERO EVENTS.**  max v_2(q-1): **17** (gate 41).
Verdicts: 96 SURVIVED_CERTIFIED, 160 SURVIVED_PARTIAL (144 smooth-clear,
16 clumped), 0 unit rows, 0 duplicates/rejections.  Wall 129.1 s; row med
0.750 s (budget-dominated) / p95 0.831 s.
Factor-stage growth vs (1,5): certified fraction 37.5% (vs 50.3%) at a
1.67x row budget — typical norms grow ~200 -> ~235 bits and the unresolved
cofactors grow correspondingly; the growth is in the HARD-cofactor
fraction, not in the norm computation (still < 1 ms/row).  Power: 37.5%
full strength, 93.8% full-or-smooth-tail, 6.3% certified-factor only.

---

## PRE-REGISTRATION — screen 4: (1,7) uniform sample

- Population: the full 13,043,008,668-orbit (1,7) affine-Galois orbit
  space (no proved subfamilies banked).
- Sample: N = 128, seeds `wscr-20260722:17:i`, i = 0..127; uniform over
  reduced signed supports C(256,7)*2^6 (orbit-size-weighted); duplicate
  canonical keys rejected; parity-uniform supports descended (exact).
- Pipeline: as screens 1/3 with row rho deadline 1.5 s; global soft
  deadline 250 s.  Odd weight => Norm odd and != 0.
- Falsifiable expectation: ZERO events.  Secondary purpose: rate
  degradation for the go/no-go ledger on ever attacking (1,7) by census
  ((1,7) has NO banked descent; 289 CPU-y floor at the banked rate) —
  recorded as certified fraction + row med/p95 at the 2x screen-1 budget,
  plus max v_2 statistics.

### RESULT — screen 4 (wscr_screen_17.json)

**128/128 rows, ZERO EVENTS.**  max v_2(q-1): **24** — the highest across
all four screens, still 17 doublings below the 41 gate.  Verdicts: 51
SURVIVED_CERTIFIED, 77 SURVIVED_PARTIAL (74 smooth-clear, 3 clumped), 0
unit rows, 0 rejections/duplicates.  Wall 122.1 s; row med 1.500 s
(budget-dominated) / p95 1.667 s.  Rate truth for the go/no-go ledger:
typical norms ~240-300 bits; certified fraction 39.8% at 3.3x the
screen-1 row budget — the (1,7) factor stage is not qualitatively harder
than (1,6) at sample scale; the census blocker remains the 13.0e9 orbit
count (289 CPU-y floor), not per-row hardness.

---

## POST-HOC declump pass (labeled; registered JSONs untouched)

The 46 clumped cofactors across the four screens (pm1 g == n: every prime
factor has 60000-powersmooth odd part — the ONE corner where an admissible
smooth prime could have hidden from the powered detector) were re-attacked
with staged p-1 (stepped 2-part, per-prime-power odd stage, 7 bases;
wscr_declump.json): **46/46 FULLY RESOLVED in 0.69 s; ZERO alarms; max
v_2 among the newly certified primes = 14.**  Post-declump power tally
(wscr_power_tally.py): every screen now stands at **100% full-or-
smooth-tail strength, 0 rows capped at certified-factor-only**:
15core 202 full + 198 smooth-tail; 27router 34 + 116; 16 96 + 160;
17 51 + 77.

---

## FINAL VERDICT TABLE

| screen | cell | population (orbits) | sampled N | events | max v_2 (gate 41) | rows w/ unresolved tail | wall | certified power (post-declump) |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 15core | (1,5) core | 2,265,060 | 400 | **0** | 17 | 198 (all smooth-clear) | 106.6 s | 50.5% complete-factorization; 100% smooth-tail |
| 27router | (2,7) router | 94,652,815 | 150 | **0** (+0 zero-branch) | 16 | 116 (all smooth-clear) | 6 x ~230 s | 22.7% complete; 100% smooth-tail |
| 16 | (1,6) | 185,569,028 | 256 | **0** | 17 | 160 (all smooth-clear) | 129.1 s | 37.5% complete; 100% smooth-tail |
| 17 | (1,7) | 13,043,008,668 | 128 | **0** | 24 | 77 (all smooth-clear) | 122.1 s | 39.8% complete; 100% smooth-tail |

Power statement (uniform): on every sampled orbit, either the obstruction
integer is COMPLETELY factored (probable-prime level) with no admissible
factor, or its unresolved composite tail (one-two ~150-450-bit cofactors)
is certified by the boosted p-1 detector to contain NO prime q with
q-1 | (order << 260) * smooth(60000) — i.e. no official-admissible prime
whose odd part of q-1 is 60000-powersmooth.  Residual blind spot, stated
honestly: an admissible prime with ROUGH odd part inside an unresolved
tail would be invisible; closing it needs gp/ECM-class factoring (the
production Modal stack does this routinely).

## Surprises / findings for the controller

1. **Typical norms are ~200-300 bits, not the 594/661/718-bit worst-case
   bounds** quoted in the sizing table.  Norm computation is < 1 ms/row
   locally; the whole factor-stage cost profile is governed by the ~50-60%
   of rows that end in one hard semiprime-ish cofactor.
2. **The pure-Python (2,7) reconstruction reproduces the banked Modal
   pilot's bit profile within ~0.3-1%** (n1 630,660 vs ~632k; n2 1,137,702
   vs ~1,140k; raw gcd 162,711 vs ~164k; gsat med 83 bits) — an
   independent full-stack confirmation of the audited router pipeline AND
   of the wclp sizing pilot, from scratch, on different hardware.
3. **Zero-branch 0/150** — consistent with wclp finding #10 (weight-7
   zero branch is vacuous).
4. **Route (a) cost truth**: the (2,7) saturation-soundness fix (screen
   the u-shared part gcd(g0, Norm u)) is what generates most (2,7)
   partial rows locally — those ~300-bit composites need gp/ECM, exactly
   as wclp #9 priced it.  Keep gp in the production loop for route (a).
5. **max v_2 grows mildly with weight** (17/16/17 at w=5,6 vs 24 at w=7,
   more prime factors per norm) — nowhere near the 41 gate.
6. **pm1 clumping is benign**: all 46 clumped cofactors split by staged
   p-1 in < 1 s total and were smooth-composite as predicted, none hiding
   an admissible prime.
7. Timing pilot for the (2,7) projection ledger (task deliverable):
   per-orbit med 9.35 s / p95 10.99 s pure-Python local, phase split
   recurrence 2.47 / Norm(F) 1.10 / Norm(G) 3.03 / gcd 0.77 / saturate
   0.07 / factor 2.00 (capped).  The transferable number is the gcd stage
   (CPython math.gcd in both stacks): 0.767 med / 0.993 p95 s — the banked
   1.095 s Modal figure is confirmed as gcd-bound; a GMP/flint gcd remains
   the top optimization lever for the 33k CPU-h (2,7) census projection.

## TESTED-WITH-POWER summary (for the slot nodes' notes)

Powered falsifier-sampling screens (2026-07-22, wscr_*, seeds
`wscr-20260722:*`, fully reproducible): deterministic seeded samples of
the four cheapest open WCL slot spaces — 400 orbits of the (1,5)
irreducible core (proved subfamilies excluded), 150 router orbits of
(2,7) via the audited cleared-cubic pipeline (independently reconstructed
and validated exactly mod q and against the banked bit profile), 256
supports of (1,6), 128 supports of (1,7) — produced **ZERO events and
zero event-candidates in 934 sampled orbits**; max v_2(q-1) over every
certified/probable prime factor of every obstruction integer is 24,
versus the official gate of 41.  Every sampled obstruction is either
completely factored or carries a staged-p-1 certificate that no
official-admissible prime with 60000-powersmooth odd part hides in its
unresolved tail (the only blind spot: admissible primes with rough odd
part inside ~150-450-bit unresolved cofactors).  The four slots move from
UNTESTED to TESTED-WITH-POWER at sample scale: survival evidence, not
exclusion — the samples cover 1.8e-4 of the (1,5) core down to 1e-8 of
(1,7) and remove nothing from any census obligation.

## Deliverables

- wscr_screens.py — all machinery + subcommands (selfcheck, pilots,
  screens, merge, declump); every run under ramguard local. The imported
  canonical packet omitted its `wsz_weight5` helper; the vendored
  `wsz_weight5.py` restores the exact norm and probable-prime contracts, and
  the full selfcheck passes in this worktree.
- wscr_screen_15core.json, wscr_screen_27router.json (+ 6 shard files),
  wscr_screen_16.json, wscr_screen_17.json — sample spec, seeds, per-item
  outcomes (factors, unresolved, verdicts), timings, max v_2.
- wscr_declump.json — post-hoc clump resolution. The original shard files and
  `wscr_power_tally.py` named by the canonical report were not committed;
  the merged JSON files retain all per-row records but are not a substitute
  for those missing provenance artifacts.
- This file.
