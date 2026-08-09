# PREREG — cancellation_recon (round 27)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

Underneath the band-closure analytic half sits the campaign's oldest
wall: converting "counts are Poisson-ordinary everywhere probed" into
a PROVED lower bound is an anti-concentration statement — the
cancellation barrier both branches have historically hit. This round
has one specific new reason for hope: **THEOREM Z-FLOOR (banked
round 18, on the F2 lane) is a PROVED pointwise first-moment floor,
tight within 2x, that survived round 26's falsification event
untouched (0 violations over 292 cells while the ceiling above it
died).** Your job: a disciplined reconnaissance — can Z-FLOOR's proof
mechanism transport to band counts, and if not exactly, what is the
weakest usable BAND-AC lower bound and what would prove it?

## Deliverables

**D1 — THE NEED, STATED EXACTLY.** Read the three consumers'
contracts (adjacency_closing, list_adjacency_closing, mca_safe) and
extract what each actually needs from the band determination: which
direction (the anti-concentration direction = counts do NOT fall
below the model, i.e. the deficit side stays deficit), at what
tolerance, at which sigma. Name each bar per consumer (CATCH-24C).
The output is the exact target statement BAND-AC-LB that a proof
would have to deliver. Include the K5 witness-kernel framing
(WP5_RATEHALF_VERDICT.md) — the priced witness family covering
(R(lq), sigma*] is the constructive reading of the same need.

**D2 — THE Z-FLOOR TRANSPORT TEST.** Read THEOREM Z-FLOOR's proof
(f2_z1_mass_knife_edge lineage; the round-18 z1_ternary_mass
pilot's banked material) and extract its mechanism skeleton: what
makes the first-moment floor PROVABLE there (the structure that
yields pointwise tightness within 2x). Then map the band count into
the same shape: what plays the role of the mass, the normalizer,
the orbit structure? Registered verdict options: (a) TRANSPORTS
(state the transported theorem + verify at accessible band cells);
(b) transports PARTIALLY (a weaker floor — state it exactly and
what it buys against D1's bars); (c) STRUCTURAL MISMATCH (name the
exact clause that fails — that names the barrier sharply for the
first time). Also survey the OTHER proved in-repo floors for the
same test at lower priority: the k-local LP floors (round 22), the
E1 floors, THEOREM D / Z-3's transport law (which already moved
between lanes once — "DLI law transports, blind convergence").

**D3 — THE WEAKEST USABLE FLOOR, ATTACKED.** Whatever D2 yields,
state the weakest BAND-AC lower bound that still serves at least
one consumer bar from D1 (a partial floor serving one consumer is
a real result). Attack it falsification-first at accessible scales:
compute exact band-analogue minima across layouts (the round-19+
standard: registered grids, 2-power configs, matched controls) and
test whether the candidate floor is (i) true in vivo with margin
and (ii) tight enough to matter. The floor-campaign posture: pose
weakest-form, attack, harden or kill.

**D4 — THE BARRIER MAP (if D2 = mismatch and D3 dies).** Then the
deliverable is the sharpest statement of WHY: the exact structural
feature of band counts that blocks every in-repo floor mechanism —
with the failed transports as evidence. A named, evidenced barrier
is the honest prerequisite for deciding whether this half needs
genuinely new mathematics or an external instrument.

## Escape tests (before the main work)

- Replay Z-FLOOR at two banked cells (SCRATCH COPY of the round-24/25
  z machinery) — the floor holds and is within 2x where banked.
- Reproduce one banked band-analogue exact count from the
  window-law data before computing your own.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4062; do not read the other round-27 pilot dirs
  (pincer_formalization, nonpoly_flank_census, staircase_extension).
  Pass this clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY (the round-26 lesson).
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint long runs; background batches with results
  files for >10-min runs.
- DRAFT-ONLY: writes only in
  notes/pilots_20260809/cancellation_recon/; no dag/nodes/tools
  writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C).
  Own-repo grep gates every "no such floor exists" claim
  (CATCH-24A). The f2 calibration clause binds on anything touching
  the F2 lane's objects.
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)

### R0 — information state at registration (disclosed)

Registered 2026-08-09 by pilot `cancellation_recon`, BEFORE any
interpreter run. Documents read before registering (reading is not
computation; disclosing the state so the priors are auditable):
`critical/nodes/{adjacency_closing,mca_safe,list_adjacency_closing}/conditional.md`,
`critical/nodes/rate_half_band_closure/{statement.md,node.json}`,
`background/nodes/rate_half_cyclic_simple_pole_mca_floor/statement.md`,
`notes/kernel_basis/WP5_RATEHALF_VERDICT.md`,
`notes/pilots_20260806/z1_ternary_mass/PROOFS.md:110-310` (THEOREM
Z-FLOOR + Z-2 + Z-3), `notes/pilots_20260808/z_ceiling_assault/zcore.py`
(API only). NOT yet read: the D3 data, any floor-campaign in-vivo
numbers, any other round-27 pilot dir (quarantined), CAMPAIGN_LEDGER
at/below line 4062 (quarantined).

### R1 — named functionals (CATCH-19C)

All in-vivo work below is on the **band analogue**: `q` prime,
`n | q-1`, `D` = the order-`n` multiplicative subgroup (or a coset),
`C = RS[F_q, D, k]` with `k = n/2`, a **line** `(u,v)` with `v` nowhere
zero, `a = k + sigma` the agreement, `r = n - a` the radius.

- `Bline(u,v,a)` := `#{ z in F_q : agr(u + z v, C) >= a }`. The band-count
  analogue. **NOT** claimed equal to `B_mca(a)`, which is a max over
  admissible rows under the support-wise convention; every claim below is
  about `Bline` and its max over the sampled line family, named
  `Bmax(a) := max over sampled lines of Bline`.
- `Ninc(u,v,a)` := `#{ c in C : max_z mult_c(z) >= a }` where
  `mult_c(z) := #{ i : (c_i - u_i)/v_i = z }`. (For `sigma >= 1` and
  `k = n/2`, `a > n/2`, so each codeword has at most one heavy slope;
  `Ninc` = the (codeword, slope) incidence count.)
- `fz(a)` := `#{ c in C : mult_c(z) >= a }` (the fiber = list size of
  `u+zv` at radius `r`). `S2(a) := sum_z fz^2`, `Lmax(a) := max_z fz`.
- `Dcl(a) := Bline * S2 / Ninc^2 >= 1` — the **Cauchy-Schwarz clustering
  defect** (=1 iff all nonempty fibers equal).
- `Rpg(a) := Bline * Lmax / Ninc >= 1` — the **pigeonhole defect**.
- `FMinc(a) := q^{k+1} * P_a`, `P_a := sum_{j>=a} C(n,j) q^{-j} (1-1/q)^{n-j}`
  — the random-line first-moment incidence model.
  `FMB(a) := q * (1 - (1-P_a)^{q^k})` — the first-moment slope-count model.
- `Vol(n,r) := sum_{j<=r} C(n,j)(q-1)^j`; `PGL(a) := Vol(n,r)/q^{n-k}` —
  the pigeonhole list floor (guaranteed max list size).
- Z-lane replay functionals are zcore's: `TMASS`, `ZFRATIO = TMASS*p^kappa/2^N`
  (= Z-FLOOR's ratio; Z-FLOOR asserts `ZFRATIO >= 1`), `CRATIO`.

### R2 — predictions (numeric windows, registered before computing)

- **P1 (D1 / CATCH-24C).** Of the three consumers, the number whose OPEN
  residual actually contains a band **lower-bound** clause is **1**
  (adjacency_closing, via rate_half_band_closure's (RH-ADJ) unsafe half).
  Predicted: mca_safe = upper-only (0 LB clauses);
  list_adjacency_closing's rate-half LB = already discharged by a PROVED
  node. Window: integer in {0,1,2,3}; point prediction 1. Conf 0.75.
- **P2 (live band width).** The band on which an LB is still needed is
  NOT `(2^33, sigma*]` (width 2,978,146) but `(2^34-1, sigma_safe]` with
  `sigma_safe = 2^39`. Predicted live width `>= 2^38 = 2.75e11`, i.e.
  `>= 10^4 x` the nominal band width. Conf 0.70.
- **P3 (D2 verdict prior).** (a) TRANSPORTS 0.20 / (b) PARTIAL 0.45 /
  (c) STRUCTURAL MISMATCH 0.35.
  - **P3a (named failing clause, registered in advance).** If (c) fires,
    the failing clause is: *Z-FLOOR's Cauchy-Schwarz needs the counted
    functional to be the SECOND moment `sum_s |F_s|^2` of the fibers of a
    GROUP HOMOMORPHISM with a fixed known total mass `sum_s |F_s| = 2^m`
    and a free codomain ceiling `p^d`; the band count `Bline` is instead
    the SUPPORT size `#{z : f_z > 0}` of a non-homomorphic incidence map
    whose total mass `Ninc` is itself unknown.* Conf that this is the
    named clause if (c) fires: 0.60.
  - **P3b (self-subtraction, hard law 5).** Probability that the
    transported theorem, once written, is equivalent up to constants to
    the already-PROVED `rate_half_cyclic_simple_pole_mca_floor` (i.e. the
    transport re-derives our own banked theorem and buys no new reach):
    **0.55**.
- **P4 (the cap arithmetic).** The volume/pigeonhole exhaustion line is
  `sigma_pg = n / log2(q)`; at the cap row (`n = 2^41`, `log2 q = 256`)
  this is `2^41/256 = 2^33` exactly, reproducing the banked
  "floor family caps at n/256 = 2^33 exactly" line. Conf 0.80 that the
  arithmetic reproduces it to within 1%.
- **P5 (in-vivo CS/pigeonhole defects).** Over the ladder, at
  band-analogue radii with `Bline >= 10`: median `Dcl` in **[1.0, 3.0]**,
  max `Dcl < 20`; median `Rpg` in **[1.5, 8]**. Conf 0.55.
- **P6 (exhaustion in vivo).** At radii ABOVE the exhaustion line
  (`Vol(n,r) < q^{n-k}`), random lines give `Bline = 0` in `>= 90%` of
  cells; at least one structured/planted line per scale still gives
  `Bline > 0`. Conf 0.55.
- **P7 (structural surplus of the max).** At the band-analogue radius
  where the random-line mean of `Bline` lies in `(0.5, 5)`,
  `Bmax / mean(Bline) >= 3` on at least 2 of the >= 3 scales tested.
  Conf 0.50. (This is the floor conjecture's own pre-registered
  falsifier direction: a structural surplus of the max over the
  first-moment model.)
- **P8 (escape tests).** Z-FLOOR replays at 2 banked cells with
  `ZFRATIO >= 1` and `ZFRATIO <= 2` (the Corollary Z-FLOOR.1 tightness).
  Conf 0.85 on `>= 1`, 0.65 on `<= 2`.

### R3 — D3 attack design (falsification-first, registered)

**Candidate weakest usable floor, posed weakest-form:**

> **FLOOR-PG-BAND (candidate).** For every admissible row and every
> agreement `a` with `PGL(a) = Vol(n,n-a)/q^{n-k} >= 2`, the max over
> lines satisfies `Bmax(a) >= PGL(a) / Lmax(a)`-style pigeonhole, and in
> the usable form: `Bmax(a) >= FMB(a)/2`.

Attack families (all exact, stdlib, matched controls):

- **F-A (ladder scan).** Scales `(n,k,q)`: `(4,2,q)` for q in a long
  1-mod-4 ladder; `(6,3,q)` q in 1-mod-6 up to 103; `(8,4,17)`,
  `(8,4,41)`; `(10,5,11)`; `(12,6,13)`. `>= 3` scales as the campaign
  standard demands. For each: exhaustive over all `q^k` codewords, exact
  integer arithmetic, all R1 functionals at every `sigma >= 1`.
- **F-B (line families = matched controls).** (i) uniform random `(u,v)`;
  (ii) `v = 1`, `u` random (the "constant-direction" control);
  (iii) planted: `u = c0 + e` for a codeword `c0` and a sparse `e`
  (forces one heavy fiber); (iv) coset/cyclic-structured `u,v` built from
  multiplicative-subgroup indicators — the small-scale analogue of the
  cyclic simple-pole construction. Controls are matched by `(n,q,a)`.
- **F-C (falsifier for FLOOR-PG-BAND).** A cell where the exhaustive
  max over the whole line family (or over ALL lines when `q^{2n}` is too
  big, over `>= 10^3` sampled lines + all structured ones) has
  `Bmax(a) < FMB(a)/2` while `FMB(a) >= 4`. Registered kill rule: `>= 3`
  such cells at `>= 2` scales kills the usable form.
- **F-D (tightness of the reduction).** Report `Dcl`, `Rpg` distributions
  — if `Dcl` is bounded the CS reduction is usable, if it grows with
  scale the barrier is named as clustering.

### R4 — addendum registered AFTER the escape tests, BEFORE the D3 runs

Escape tests done (E1 Z-FLOOR replay 3 cells, E2 three banked F7-A2
ladder points reproduced exactly). Then read
`background/nodes/rate_half_cyclic_simple_pole_mca_floor/proof.md`.
That proof turns out to contain a Cauchy-Schwarz-on-fiber-multiplicities
step, so the D2 mapping is now concrete and the D3 attack is re-aimed at
the two lossy steps of the in-repo conversion. Registered BEFORE running:

- **P9 (self-subtraction confirmed / P3b resolution).** I now expect the
  D2 verdict to be (a) TRANSPORTS-BUT-ALREADY-BANKED. Registered before
  the arithmetic: the transported Z-FLOOR = the proved simple-pole
  conversion; new reach bought = **0**.
- **P10 (cap law, exact).** The whole in-repo LB family is
  `sigma_reach(c,d) = c(d+1)-1` with supply `L = C(N-1, N/2+d)/(N q^{d-1})`,
  `N = n/c`, and admissibility `1/E = N q^d / B + k q/(q-n) < 2^128`.
  Predicted: maximizing over `c | n` (2-powers) and `d >= 1` at
  `q = 2^256` returns `sigma_max = 2^34 - 1` at `(c,d) = (2^33, 1)`,
  reproducing the banked optimized floor; and the binding rung is the
  2-power quantization `N = 256` vs `N = 128`. Conf 0.65.
- **P11 (the 4.8-bit deficit).** `log2 C(127,64) = 123.1714 +- 0.001`
  and `log2(q/2^128)` over the razor slice = `127.90..128.00`, giving a
  deficit `4.73..4.83` bits = a factor `28.4`. Conf 0.80 that the exact
  arithmetic reproduces both numbers.
- **P12 (in-vivo loss of the simple-pole conversion — the new attack).**
  At band-analogue cells I will measure the two lossy sub-steps of the
  conversion separately, on the exact list of a banked sunflower word:
  `LOSS_avg := M(best pole) / M(pole guaranteed by averaging)` and
  `LOSS_CS := M(actual) / (L^2 / sum_j r_j^2)`, plus the end-to-end
  `LOSS_tot := M(best pole) / [L(q-n)/(q-n+k(L-1))]`.
  Registered prediction: `LOSS_tot` in **[3, 12]** at (n,k,sigma,q) =
  (16,8,1,97) and **increasing with q** across the banked ladder;
  `LOSS_CS` in **[1.0, 2.0]** (Cauchy-Schwarz nearly tight because
  multiplicities are near-equal) and `LOSS_avg` in **[2, 10]**. Conf 0.45.
  **Why it matters (registered):** the band's banked deficit is
  `x28.4 = 4.83` bits; if the end-to-end conversion loss exceeds `28.4x`
  and is provable, the next 2-power rung (`N = 128`, reach `2^35 - 1`)
  becomes admissible and the proved unsafe reach doubles. Registered kill
  line: `LOSS_tot < 28.4` sustained across `>= 3` ladder points and `>= 2`
  scales makes this route dead-as-measured (not proof-dead).
- **P13.** Registered before running: at the banked cell the pole-averaged
  collision bound is loose because collisions are Poisson-distributed over
  poles; predicted `M(best pole) >= 0.9 L` at `q = 97, n = 16` (i.e. the
  actual distinct-slope count is nearly the full list). Conf 0.5.

**Registered honesty rules for this pilot.** (i) Every "no such floor
exists" claim is gated by an own-repo grep (CATCH-24A) reported inline.
(ii) The f2 calibration clause binds on the Z-lane replay: I will state
Z-FLOOR's scope (`F_p`-subspace, ternary difference set, shift-0
hypotheses where relevant) before transporting anything. (iii) Misses
first in the final report.
