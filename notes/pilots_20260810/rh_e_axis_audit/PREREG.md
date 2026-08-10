# PREREG — rh_e_axis_audit (round 31)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/k3_chain_seams/REPORT.md` (round 30, F4)
2. `critical/nodes/rate_half_band_crossing_location/statement.md`
   (long file: read the pose at the top + the round-30 F4 flag
   section; use grep offsets, not a whole-file read)

## Mandate

COMMISSIONED BY THE 2026-08-10 F4 RULING: the crossing-location pose
stays q PRIME for now, blind widening to q = p^e is RULED OUT, and
this audit decides the fork. Round 30 exhibited admissible extension
rows (q = p^2 inside the razor slice, v_2(q-1) = 42, n = 2^41 | q-1)
that the item-13 family includes and no child covers. YOUR JOB: the
per-instrument primality-sensitivity audit of the rounds-27..29
stack, ending in a recommendation: WIDEN the pose to p^e (with the
instrument-by-instrument proof obligations named) or MINT a separate
extension-row child (with its pose drafted).

## Deliverables

**D1 — THE INSTRUMENT INVENTORY.** Enumerate, file:line, every
instrument the located-crossing machinery uses on 2^167 < q < 2^256:
the sub-2^167 determination, the Hankel layer (r < 2^39 scope), the
PROVED simple-pole/far-CA floors, the quotient floors (F1's
mechanism space), S_sparse and its exhausted rung lattice, the
Fisher/MDS instruments (T1-T5), the bracket theorems
([k+2^34, 3n/4]). For each: does its proof use primality of q, and
WHERE exactly (cyclotomic structure, prime-field character sums,
v_p arithmetic, prefix/charge encodings)?

**D2 — THE EXTENSION-ROW ARITHMETIC.** At the two exhibited rows
(q = p^2 ~ 2^256 razor slice; q = p^2 ~ 2^201) and at small-scale
extension analogues: compute the instrument quantities that ARE
field-agnostic (B* = floor(q/2^128), the bracket endpoints, the
budget arithmetic) and identify which change form (subfield
structure: F_p subset F_q gives new invariant subspaces — do
subfield words create supply the prime case lacks? The WP5 "31-bit
prefix charges" note says extension rows differ materially — chase
that note to its source and quantify).

**D3 — THE SUBFIELD SUPPLY QUESTION (the likely crux).** In an
extension row, words valued in the subfield F_p (or intermediate
fields) are closed under Frobenius; the locator/list machinery may
see extra structure. Determine at small scales whether subfield
words change the crossing arithmetic (exact measurements,
pre-registered expectations). This is the concrete mathematical
question behind widen-vs-child.

**D4 — THE RECOMMENDATION.** Widen (list the per-instrument proof
obligations, each with a falsifier) or child (draft the
extension-row child's pose: quantifier, bracket, falsifiers).
State which instruments transport FREE, which need work, which
BREAK. Misses first; zero-power on anything small scales cannot
see.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. Stdlib only. No
  Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json; the two
  big band statements read by grep-window only; checkpointed batches
  for long runs.
- WRITE SCOPE: ONLY inside notes/pilots_20260810/rh_e_axis_audit/.
  No dag/, nodes/, tools/ edits. No git. Never touch any path
  containing prize-codex-.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the sibling round-31 dirs (rh_overlap_cap,
  rh_type2_stratum, rh_transport_dictionary). Round-30 and earlier
  pilot dirs are readable.
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" (P(recommendation = widen), expected count of
  prime-dependent instruments, P(subfield supply changes the
  crossing)) BEFORE any further read.
- REPORT: REPORT.md in your dir; MISSES-FIRST; every quantifier
  claim quoted file:line (CATCH-24C); own-repo greps before novelty
  claims (CATCH-24A); zero-power declarations on max-quantified
  claims; banked scripts from scratch copies only.

## Pilot registrations

Appended by the round-31 pilot `rh_e_axis_audit` after reading ONLY
the two named anchors (`notes/pilots_20260810/k3_chain_seams/REPORT.md`
in full; `critical/nodes/rate_half_band_crossing_location/statement.md`
lines 1-64 and 492-512 by bounded windows) and BEFORE any other read
or any computation.

### R1 — headline prior

**P(recommendation = WIDEN the pose to q = p^e) = 0.55.**
P(MINT a separate extension-row child) = 0.35. P(neither clean —
recommendation is a third shape, e.g. widen-with-an-e-cap or
"widen the pose, child the residue") = 0.10.

Reasoning I am committing to in advance: the item-13 family is
`q = p^e`; the sub-2^167 determination is claimed for *every*
admissible q; and `official_row_primes_pinning` (PROVED) forbids a
certificate that is neither family-uniform nor exhibit-scoped. Those
three push toward widening. The counterweight is that a widened pose
that no instrument actually supports is worse than an honest child.

### R2 — expected count of prime-dependent instruments

Against the eight instrument families the brief names (sub-2^167
determination; Hankel layer; PROVED simple-pole floor; far-CA floor;
quotient floors / F1 mechanism space; S_sparse + rung lattice;
Fisher/MDS T1-T5; bracket theorems), I register:

**Expected count that genuinely use primality of q: 2.** 80% interval
[0, 4]. Median guess for *which*: (i) something in the S_sparse /
rung-lattice layer that uses a prime-field character-sum or a
`v_p`-style arithmetic step; (ii) an encoding-level dependence
inherited from the WP5 "31-bit prefix charges" note. I predict the
MDS/Fisher instruments (T1-T5) and the bracket theorems are
**field-agnostic** (Reed-Solomon and Singleton/Johnson-type counting
work over any finite field) at ~0.8 each, and that the Hankel layer
is field-agnostic at ~0.75 (rank of a Hankel/Toeplitz matrix is a
linear-algebra fact over any field).

I further register the *shape* of the answer I expect: most
instruments will transport because they depend on `q` only through
`|F| = q`, `n | q-1`, and `B* = floor(q/2^128)`; the risk is
concentrated not in "primality is used in a proof step" but in
"extension fields have MORE structure, so a *supply upper bound*
proved for prime fields may simply be false for `p^e`". Upper bounds
are the fragile direction; lower bounds/floors transport.

### R3 — the subfield supply question

**P(subfield structure changes the crossing arithmetic materially,
i.e. moves `a_RH` or breaks a floor) = 0.35.**
P(it changes some measurable supply count but not the located
crossing) = 0.30. P(no measurable difference at all) = 0.35.

Pre-registered mechanism guesses, in order:
1. (~0.45) The evaluation domain is the `n`-th roots of unity, and
   Frobenius `x -> x^p` permutes it (index multiplication by `p mod n`).
   Frobenius-stable subsets of the domain give `F_p`-rational
   locator polynomials, so the *symmetric-function* conditions that
   the agreement counting solves can have a different solution count
   over `p^e` than over a prime field. This is the mechanism I think
   is real if any is.
2. (~0.25) Subspace/linearized-polynomial supply (the classical
   extension-field-only list-decoding lower bounds). I predict this
   one does **NOT** apply here because the domain is multiplicative
   (a group of roots of unity), not an additive `F_p`-subspace.
3. (~0.15) Intermediate fields / norm-and-trace structured received
   words creating supply the prime case lacks.

**Specific falsifiable side-prediction (registered because it is
cheap and would be a real finding either way): for the exhibited
`e = 2` rows, the `2^41`-torsion does NOT lie in `F_p`.** Since
`q - 1 = (p-1)(p+1)` and `gcd(p-1, p+1) = 2`, essentially all of the
2-power torsion sits in one factor; if it sits in `p+1` the domain
lies in the norm-one ("circle") subgroup, which is exactly the
structure the repo elsewhere marks **extra-official**. **P(the
exhibited razor-slice row has its `2^41`-torsion in the norm-one
subgroup rather than in `F_p^*`) = 0.70.** If true this is a
material input to widen-vs-child that round 30 did not compute.

### R4 — power

**P(small-scale exhaustive computation has power to discriminate
prime vs extension supply at matched `(n, k)`) = 0.50.** The
honest obstruction is that exhaustive `max_y` costs `q^(n+k)`, so
matched prime/extension pairs are only reachable at `q <= ~17`,
`n = 4`. I pre-commit: if the reachable window cannot separate the
hypotheses, I will declare **ZERO POWER** rather than report a null
as evidence of transport.

### R5 — misses discipline

I pre-commit to a MISSES-FIRST section scoring R1-R4 explicitly,
including direction of error, and to naming any instrument I could
not locate in-repo as an inventory **gap** rather than silently
omitting it from D1.

### R6 — D3 experiment pre-registration (written after D1/D2 reading and
### after the D2 arithmetic ran, but BEFORE any D3 measurement)

Instrument: `F_LMAX(n_s, K, q, a) = max_U #{c in C : agreement(U,c) >= a}`
— the exact max list profile at the scaled rate-1/2 RS row, the same
object the round-29 `list_profile_bound` pilot measured at
`q = 17 / 41 / 97` and found to be the **q-independent absolute
constant 7** at the cell `(n_s, K, a) = (8, 4, 5)`. Every field ever
used in that measurement (and in every other rounds-27..29 experiment
I could find) is PRIME.

Design: matched `(n_s, K) = (8, 4)`, `a = 5, 6, 7`, over
- primes `q = 17, 41, 73, 89, 97, 113`;
- extensions `q = 9 (3^2), 25 (5^2), 49 (7^2), 81 (3^4), 121 (11^2),
  169 (13^2), 289 (17^2), 361 (19^2)`.

`q = 289 = 17^2` is the designed analogue of the round-30 razor
exhibit: there `8 | p-1`, so the order-8 domain lies **inside the prime
subfield** `F_17` — exactly the branch the exhibited razor row is in
(measured in D2: `v_2(p-1) = 41`, so `D` is inside `F_p`). `q = 9, 25,
49, 121, 169, 361` are the other branch (`D` not inside `F_p`), and
`q = 81 = 3^4` puts `D` inside the intermediate field `F_9`.

Pre-registered expectations, committed before running:

- **E1.** `F_LMAX(8,4,5) = 7` at every extension field too — i.e. the
  constant is field-TYPE-independent, not merely q-independent.
  **P = 0.60.** If it exceeds 7 anywhere, that is a supply excess the
  prime-field evidence base cannot see, and it flips me toward CHILD.
- **E2.** If any field type shows excess, it is the `D` inside `F_p`
  branch (`q = 289`), not the `D` outside branch. **P = 0.55**
  conditional on any excess existing.
- **E3.** The maximizing key at an extension field is NOT
  `F_p`-rational (a rational key forces the whole agreement list to be
  rational, by the splitting argument, so rational keys can only
  reproduce the prime-field value). **P = 0.7.**
- **E4.** The scaled crossing `sigma_L(q) = max{sigma : F_LMAX(K+sigma)
  > isqrt(q)}` is a function of `q` alone, identical between prime and
  extension fields of the same size when both exist — untestable
  directly (no `q` is both), so the honest test is monotone
  consistency along the merged ladder. **P(consistent) = 0.75.**
- **E5 (ZERO-POWER pre-commitment).** `n_s = 8` cannot see the razor
  row's mechanism (round-29 already declared the scaled-cell program
  STRUCTURALLY INCAPABLE of resolving `c`); a null here is evidence
  about *supply parity*, never about the located crossing itself. I
  pre-commit to saying so in the report whatever the outcome.
