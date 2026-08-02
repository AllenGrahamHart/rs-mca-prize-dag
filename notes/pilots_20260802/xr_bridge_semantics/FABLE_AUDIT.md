# Fable audit of the xr bridge adjudication pilot — 2026-08-02

**Verdict: ACCEPTED.** Classification (b) confirmed — a genuine inherited
gap, not the prose-only defect my leading hypothesis predicted. The
repair R2 (`Gamma_hi = {core >= K}`) is forced, jointly with widening
P-A1's predicate to "core of size >= k"; R1 is unsafe (it routes the band
into P-A2, whose only removal step provably requires `|T| <= n-A`, and
that exact widening is already REFUTED in
`background/nodes/xr_nondeep_tangent_supportwise_payment`). The bridge's
PROVED status is repairable at statement level; the flag also surfaced an
unsupported removal claim inside `xr_strip_classification_rungs` item 3.

## Independent verification record (spot-checks by me, this session)

Re-read and confirmed verbatim every load-bearing citation:

1. `xr_tangent_support_mismatch_bridge/proof.md:3,6-9` — the case split
   IS on A-supports, and the generic branch imports "all distinct
   selected support intersections at most `K`" from "the proved strip
   rung". The conflation is in the proof, not only the statement.
2. `xr_strip_classification_rungs/proof.md:18-22` — the forcing algebra
   (g=(c1-c2)/(z1-z2), f=c1-z1·g, |R|>=k+1 forces a codeword pair on >k
   points) is proved; the next sentence "This is exactly the
   tangent/classified event removed before the generic remainder" is
   asserted with no derivation. Confirmed: nothing in the node derives
   the removal.
3. `xr_smallcore_spread_count/notes/audit_p8p9_local_20260710.py:221-226`
   — the machine-checked high-core class is `if J >= k` (R2 semantics);
   line 192: F1 verifies the forcing identity on core>=k+1 cross pairs
   and counts them (4,662 in the cited fixture) — verifies, does not
   remove; line 214: the tangent event fires at `t-d_ <= 0`, i.e.
   pair-agreement >= k+t = A — the A-support trigger.
4. `xr_pencil_cascade/statement.md:9` — the only proved core-based
   payment fires at core >= k+t-1 = A-1.
5. `xr_highcore_collision_count/statement.md:7-9` — P-A1's predicate is
   exact-size-k ("shares a size-`k` core"), so the R2 bridge edit forces
   the paired P-A1 widening.
6. `xr_true_tangent_coordinate_injection/statement.md:9-19` — hypothesis
   `|T| <= n-A`, conclusion `# slopes <= |T| <= n-A`. Under R1 a band
   pair with only a (K+1)-point explanation has `|T|` up to `n-K-1`,
   far outside the printed slot. R1-unsafe confirmed.

## The gap, re-derived (scale-free)

Take a distinct-slope pair with core `r in [k+1, A-2]` (band non-empty on
all six official rows; astronomically wide on the prize rows). The strip
algebra forces a codeword pair `(f,g)` agreeing on `r > k` points —
proved. But: the tangent strip's trigger P2/T2 needs single-slope
agreement > A (does not fire — every slope still agrees on exactly A);
the pencil cascade needs `r >= A-1` (does not fire); and the bridge's
nongeneric branch needs a joint explanation on an A-SUPPORT, which the
forced pair need not provide (it agrees on only `r < A` points). Nothing
banked removes or pays the band pair, so the bridge's imported premise
`cores <= K` is unsupported, and under the current wording
`Gamma_hi = {core = K}` a band slope sits in neither class. The
dichotomy is non-exhaustive as written: genuine gap.

## Adopted posture

1. **Evidence banked, no statement edits yet.** The R2 + P-A1 joint edit
   is a coordinated change to two critical nodes (one PROVED). I am
   treating R2 as forced (per the pilot's four-way convergence: pinned
   verifier, F5_SKELETON conventions, pilot instrument, Pro brief) but
   the P-A1 widening changes a proof obligation, and the pilot's open
   question 2 — whether P-A1's banked partial payments (sunflower cap,
   rank-two ledgers, Maxwell deficits) survive `{core in [k, A-2]}` —
   gates the edit. A dedicated cost-pass pilot has been launched
   (notes/pilots_20260802/p_a1_widening_cost/). The edit lands after
   that pass, as ONE change touching bridge + P-A1 (+ the strip node's
   item-3 rewording), surfaced to the maintainer.
2. **Strip node over-claim surfaced.** `xr_strip_classification_rungs`
   item 3 ("hence the post-strip generic remainder has pairwise cores at
   most k") is unsupported. My recommendation: scope-narrow, not status
   flip — restate item 3 as: forcing PROVED for all cores >= k+1;
   removal/charge PROVED only at r >= A-1 (pencil cascade); the band
   [k+1, A-2] is classified, not charged, and is carried by the R2
   bridge partition into P-A1. The node's six-row arithmetic and the
   88-check replay are untouched by this. Decision recorded as SURFACED
   (status wording on a PROVED node).
3. **FM3 unblocked by R2 only.** Under R2, FM3's prefix-concentration
   mechanism (cores >= K) lands every slope in Gamma_hi and
   `Gamma_lo = EMPTY` is directly statable. Under the current wording
   FM3's conclusion is literally false. FM3 wording stays blocked until
   the joint edit lands.
4. **Notation pin.** The repair edit must pin one symbol for K/k (same
   object, two spellings across .md vs dag statements) — the flag was
   partly a transcription failure across that boundary. Follows the
   naming-convention rule: dag statements are normative; `k`.
5. **Honest caveats kept.** The (K+1)-core exhibits are pilot-scale;
   band realization by received pairs at official A is not established
   anywhere. The gap argument (steps 3-6) is scale-free and does not
   need it; the "concrete counterexample" framing does. Recorded as-is.

## Catches

- Catch: the pinned verifier `audit_p8p9_local_20260710.py` had the
  correct (R2) semantics all along; the bridge's `= K` is a
  mis-transcription of its own machine check. Genre: false-green wording
  over a green computation — same family as the averaged_xr catch from
  the 2026-07-27 honesty audit.
- Catch: `xr_quotient_global_core_collision_router`'s routing sentence
  is already wrong under the current wording whenever a full core
  exceeds k; R2 repairs it as a side effect. To be folded into the same
  change.
- Catch: the archived `xr_partial_tangent_band` node (cut 2026-07-05)
  was the honest record of exactly this open work; the cut orphaned the
  obligation while the strip prose silently absorbed it as if proved.
  Process lesson for future retractions: grep consumers for claims that
  cite the cut node's mission before deleting it.
