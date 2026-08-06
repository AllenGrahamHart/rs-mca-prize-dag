# K3 contributor review, 2026-07-30 — all open PRs, all authors

Reviewed: Scott Hughes's codex #1122, #1126–#1131, #1133; our Codex's #1121,
#1123–#1125, #1132. Upstream main unmoved at 93fba1be. Facts banked here are
node-local per the standing rule. Nothing below changes this node's status.

## Independent replay of the conic exclusion (#1128)

We re-ran Scott's verifier ourselves from the PR head:
`verify_kb_mca_v4_q6_u2_complete_source_conic_exclusion_v1.py
--check --tamper-selftest` → PASS, **30/30 tamper self-tests**,
`ledger_movement=0`, residual `2+2+2` frontier at **324 cases / 10 orbits**.
The saturation identity `sum div H(alpha_i,-) = 2 div B` that our wave-33
integration cites is therefore independently replayed on our side, not just
inherited from Codex's replay.

## Our degree-5 deletion is the CORRECTED argument — provenance now explicit

Upstream `dead_ends/kb_mca_v4_degree5_prime_field_pgl2_misidentification.md`
(in #1133) documents a REJECTED first draft of the fifth-power argument: it
placed the active roots in the prime-field carrier `D ⊆ F_p` and sought an
order-5 element of `PGL_2(F_p)`. The roots are parameter-line values in
`K = F_(p^6)`; the correct deletion uses `gcd(5,|K^x|)=1` after K-rational
normalizations. **Our integrated attack text is the corrected version**
(checked line-by-line against the dead end's "correct replacement").

## FENCE — the `m | 2^21` trap

From the same dead end: *"the same error also invalidates any unconditional
use of `m | |D| = 2^21` for the geometric endpoint map."* Divisibility of an
inner degree by `|D|` is a necessary condition ONLY after a separate
same-record theorem identifies the parameter-line decomposition with an
m-fold map on the carrier. #1133 states the gate conditionally (only
`m in {2,4}` would pass IF the bridge existed; the bridge is not proved).
**Checked 2026-07-30: our tree currently contains no unconditional use.**
Do not introduce one.

## #1133 — the degree-60 source-fiber adapter (content-reviewed only)

Eight exact inner-degree pole-profile rows; `m=5` empty over `K`; `m=30`
refines to inner degree 6 by exact fifth-power extraction. Its Python
verifier binds to git objects not reachable from the fetched PR ref, so we
could NOT replay it in our checkout — recorded as content-reviewed, not
replayed, matching the ledger's own provenance discipline.

## #1122 — cap-68 secant route refuted

An exact 69-record carrier family realizes constant support 981105, ranks,
exchanges, all 3280 projective ternary secants at distance >= 1052958, and
every printed circuit bound — while NOT implying cap 68. So the pairwise
ternary-secant / support-rank / circuit route to cap 68 is a proved route
cut. Any future cap-68 attempt from this node must use more than those
weakened consequences.

## Lane state

Q=6,u=2 after this review: conic-image branch EMPTY (#1128, replayed);
reciprocal P6 deleted (#1126/#1127, with one false positive caught and
documented in `dead_ends/`); residual = the `2+2+2` frontier (324/10) plus
the decomposition rows `{2,3,4,6,10,12}` under the wave-33 narrowing, with
the 26→24 transverse types at m=12. Three agents interleaved: Scott
(#1122–#1131, #1133), our Codex (#1132), this review.

## Addendum 2026-07-31 — the 112 coordination gap, surfaced and commented

Scott's #1140 compiles all 36 aligned-positive q-slice systems freshly
(`ALL_CELLS_UNCLASSIFIED`, zero citations of our lane); #1141 deletes
F02/F03 from that atlas. Our #1132 export had already excluded the
aligned-positive ramified slices (6 unit ideals) with printed residual
`remaining_unramified=6, deep_cases=17`. Neither stack consumes the other —
the first genuine coordination failure between the forks.

Maintainer approved a cross-reference comment; posted on #1140
(issuecomment-5146556389): states our coverage and residual with replay
line, explicitly does NOT assert cell-for-cell identity (the partitions
differ: his 12x3 vs our ramified/unramified/projective), proposes a mapping
row in either direction, and frames overlap as free cross-verification.
Watch: whether the atlas note gains the mapping, and whether F02/F03 land in
our printed residual (which would make #1141 a continuation, not a
re-derivation).

## Addendum 2026-08-01 — the order-two row collision (#1139/#1141)

Scott's codex has entered the `(m,r,delta)=(2,4,2)` order-two type
(`kb_mca_v4_m2_r4_order2_source_facet_interpolation_v1`, base #1139, also
carried by #1141). Established against the PR heads:

- **Diagonal-orientation duplication, second of its kind.** His split-quartic
  fiber-product + diagonal-transport + interpolation-kernel construction
  (`35 x 12` matrix, full-support kernel condition) is the same theorem as
  our `rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler`.
  Both sides built it on 2026-07-30, hours apart, independently — the same
  failure mode as the 112 atlas (#1140), caused by the same asymmetry: his
  material ships upstream immediately, our `kb_m2_r4` campaign has never
  been exported (zero such paths in #1132).
- **His coordinate-orientation fixture is complementary:** the exact facet
  census `(10,10,4)` plus a defect-zero abstract fixture proving counting
  alone cannot delete the coordinate orientation. This is a theorem we do
  not have and should consume; it also predicts his agent's next move is
  algebraic deletion — the campaign our worker has already completed for
  negative parity (two-loop, one-loop 442+433, zero-loop 8/15 as of wave 37).
- **He consumes our full-V4 export correctly** — evidence the disposition
  loop rewards whatever we actually ship.

Watch: whether his agent starts deleting coordinate-orientation cells
(= re-deriving waves 33-37); whether #1139's facet census gains a mapping to
our source-line c2 orbits; export status of `kb_m2_r4` (ours) as the fix.

## Addendum 2026-08-04 — Scott's frontier at #1149, and the export that is now overdue

External evidence, unmerged. Established read-only against PR heads
#1149 `55ac3e07477bd7a768190a3e755f22b0d44354b0` (DRAFT), #1144
`05ff2348de8f2c0f99683875ff12a9a79dcf21ec`, #1139
`8d43c6fa3a6ff04ea369ba7046fced6ae133b097`. CONTENT-REVIEWED, NOT
REPLAYED (Sage/Singular; outside our compute law). Nothing below changes
this node's status, and no upstream result is imported as a theorem.

**Two frontiers, not one.**

1. *36-cell aligned-positive (1,1,2) atlas* (#1140/#1141/#1144/#1149).
   #1141 deleted F02/F03 (6 fixed-moving), #1144 deleted M00..M03 (all 12
   moving-moving), leaving 18 = {F00,F01,F04,F05,F06,F07} x {R02,R11,R20}.
   #1149 proves named-open emptiness for F00-R11 and F01-R11 (localizer
   nilpotent of exact index three), so his frontier is now **16 open**:
   four retained two-dimensional crossed/identity schemes (F00/F01 x
   R02/R20) plus twelve F04..F07 cells compressed — a route cut, NOT an
   emptiness theorem — into six two-cell fingerprint orbits (F04=F07,
   F05=F06 at each root pattern) via
   `Res_w(Aw^2+Bw+C, Dw^2+Ew+F) = U^2 - VZ`, `U=AF-CD, V=AE-BD, Z=BF-CE`,
   generic root `w = -U/V`, with the `V=0` rank-drop branch retained.
   Certificate payload `4adc4187bb5794ed70fce122055fb94916974c1adacf9451237aff002ebfd63e`;
   `K3_closed: false`, `KoalaBear_row_closed: false`; his own scope line is
   "No owner, charge, K3 value, or KoalaBear row bound moves."

2. *Outer/transverse per-record frontier* (#1139), a different object,
   **unchanged since 2026-08-01**: `26 -> 22 -> 18 -> 12 -> 8 -> 3 -> 2`
   under `delta r = 4m`, with the only residual terminal types still
   `(m,r,delta) = (2,4,2)` and `(2,8,1)` — neither deleted (his universal
   `m=2,u=2` interface records this explicitly; the last deletion removed
   `(2,2,4)`). #1149's net commit touches no outer-frontier artifact.
   The any-69 cap-68 lemma remains conditional on resolving both types AND
   four UNPROVEN semantic gates: (i) every transverse terminal maps to the
   correct active-v4 cell; (ii) a semantic complete selector emits an
   actual record for every selected 69-class set; (iii) every strict route
   transports all 69 classes injectively and cardinality-preservingly or
   exactly reselects 69 at lower rank; (iv) every owner descent preserves
   the full eight-field same-record key. He labels it YELLOW and says the
   cap "is not bankable". The dihedral route cut stands: two fixed-point-free
   involutions preserving the deployed carrier generate a group of order
   2^21, so recurrent quadratic folds are not automatically strict progress.

**THE COORDINATION GAP HAS CLOSED — in our favour, and we have not
collected.** The 2026-07-31 addendum recorded #1140 as compiling the atlas
with "zero citations of our lane". #1149 §1 now reads: "PR #1143 now closes
the complete positive coordinate route `433-1a -> O0b` and role cell 14 of
`433-1b -> O0a`; its newest workboard instruction asks for the six
aligned-positive unramified cells. The `F00/F01` six-cell block is attacked
here literally." He is selecting his targets from our exported workboard.
The 2026-08-01 watch "export status of `kb_m2_r4` (ours) as the fix" is
therefore RESOLVED: the export worked.

But our tree closed that block completely and never shipped it. All six
`rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_*`
allocations are PROVED (moving same/swap/mixed, fixed same/swap/mixed);
`..._fixed_mixed_.../result.md` states "All six aligned-positive unramified
allocations are now closed". Upstream still sees only #1132's printed
residual `remaining_unramified=6, deep_cases=17`, which is what is
advertising the block as open. Scott has 2 of his six; we have 6 of ours.

**MAPPING STILL UNESTABLISHED — do not claim identity.** His six is
(two fixed-moving assignments F00,F01) x (three root patterns R02,R11,R20);
ours is ({fixed-moving, moving-moving}) x ({same, swap, mixed}). Ours
contains three moving-moving cells; all of his moving-moving cells (M00..M03)
were already deleted in #1144. So the two "six-cell aligned-positive
unramified blocks" are not known to be the same six objects, and the
cell-for-cell mapping row we proposed on #1140 (issuecomment-5146556389) has
still not been supplied by either side. Our 6/6 and his 2/6-plus-4-retained
are NOT in contradiction under either reading: he proved two cells empty and
left four OPEN, not nonempty.

**Pin drift.** #1139 is stacked on #1132 at head `c2edcfa5`; our #1132 has
advanced to `543db66f` ("Extend saturated 112 q-slice exclusions"). Any
repricing of the 26 -> 2 composition must be re-checked against `543db66f`.

**Watch resolutions.** RESOLVED-NO: he has not entered coordinate-orientation
deletion — #1144/#1149 stay in the *aligned*-positive orientation while our
exported lane is *coordinate*-positive; no re-derivation of waves 33-37.
RESOLVED: the kb_m2_r4 export was the fix. PARTIALLY RESOLVED: he now cites
our lane but supplied no mapping. UNRESOLVED: #1139's facet census still has
no mapping to our source-line c2 orbits.

**Watch:** whether the six-cell mapping row appears on either side; whether
#1149 leaves draft and survives its own "fresh cell-specific proof review";
whether his next cycle attacks the four F00/F01 crossed/identity survivors
(cells our tree may already have closed — see the export recommendation);
whether the resultant-hash coincidence between his R02 and R20 orbits is a
real symmetry he can exploit.
