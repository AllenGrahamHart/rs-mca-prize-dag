# Upstream import ledger (2026-07-08, per Codex's alignment recommendation)

Format per Codex's ask: payload | status | upstream source | local node(s) |
claim imported | explicit nonclaim. LAW APPLIED (this is where we depart from
Codex's draft): v13-raw material enters as PROVED only when OUR verification
earned it (upstream's own promotion rule forbids citing v13-raw as theorem
rows); otherwise it enters at TARGET/quarantine with a replay plan (standing
order 12 precedent, already encoded in v13_prefix_collision_ledger).

| payload | status | upstream source | local node(s) | claim | nonclaim |
|---|---|---|---|---|---|
| four adjacent-pair replay | PROVED-AUDIT (ours: exact integers, all margins) | prop:capg-moved-frontier / cor:capg-adjacent-pairs | NEW v13_adjacent_rows_replay_audit -> v13_frontier_row_packets, adjacency_closing | unsafe side + pair locations verified independently | does NOT prove safe side at a0+1 |
| second-moment shift-pair identity | PROVED (upstream 3-line proof READ + our m=h instance machine-replay, 5 rows) | thm:capg-second-moment | NEW v13_second_moment_shift_pair_identity (split from collision ledger) | Sum N^2 = C(n,m) + Sum P_e; sp strata definitions | full-strata replay at general m RUN 2026-07-10 (PASS, digit-exact, 40+ rows — see v13_prefix_collision_ledger notes) |
| trade = shift-pair dictionary | PROVED (f3_shiftpair_weld, machine-checked) | (ours + their def) | ev-fan EXTENDED to u2c, xr_smallcore, x4 | F3 trades = sp top stratum | does not amber anything (max-form lossy; see weld node) |
| beta-normalization guard | PROVED (guard existed; catches #11-13 = its predictions confirmed) | towards-prize.md ledger law | v13_base_field_normalization_guard: ev edges ADDED into dli, u2c, worst_word | base objects spend |B| not |F| | not a census bound |
| prefix rigidity | PROVED (2026-07-10 independent replay: 109,200 colliding pairs, 46 configs, chars 2/3/5/13/17, zero violations; verifier in node notes) | v13 raw lem:capg-prefix-rigidity | v13_prefix_collision_ledger PROMOTED | colliding fibers differ in >= w+1 points/side; e=w+1 pairs are constant shifts; second-moment stratification exact at general m | primitive sp_w part stays open; no max-fiber control |
| L4 interior chart -> Q | TARGET pending our proof-read | cap25_v13_bc_l4_interior_chart_to_q | ledger only (no node yet) | -- | NOT imported as proved; verify then wire to v13_bc_split_pencil_normal_form as child |
| Veronese z*=0 top-stratum emptiness (char 0) | PROVED (2026-07-10 independent replay: iff-2-power law exact at 7 n-rows, 3248 pairs, Lemma A on all 1124, L4 pins; upstream verifier green + tamper-covered) | e83962ae note cap25_v13_bc_l4_veronese_top_stratum.md (SOURCE CORRECTED from 'v13 raw') | NEW v13_veronese_top_stratum_char0 -> v13_bc_split_pencil_normal_form | char-0 top stratum empty at L4 | char-p conjectural (degenerate primes exist, e.g. 32 at p=97 n=16); deeper strata + M2 bound + z*!=0 branch open |
| BC curve second moment (#395 Thm C1) | PROVED (2026-07-10 independent replay: identity exact at 10 rows, 2 RHS methods, per-stratum; proof-read sound at general parameters incl. L4) | #395 (branch bc-l4-curve-second-moment, closed unmerged 2026-07-08) | NEW v13_bc_curve_second_moment_identity -> v13_bc_split_pencil_normal_form | exact M2 stratification; e >= w+2 floor; top stratum = constant shifts | NO magnitude bounds; C2/dichotomy/ceilings unverified; distinct from Veronese emptiness (do not conflate) |
| row-sharp Q atom target w/ margins | NOTE-LEVEL (statement bridge to F6) | grande_finale def:q-row-atom | rate_half_band_closure notes (upstream_determination_datum.md already carries the data) | their frontier form named at our F6 | floors stay frozen; no re-pose |
| Q route-cuts / no-shortcut audits | queued as PROVED-ROUTE-CUT background nodes after listing | v13 raw + grande finale | ledger only | -- | route-cuts prove nothing positive |
| image-fiber list-side correction | PROVED core (2026-07-10 replay of thm:capf-planted: 6 instances, 4 characteristics, brute-force cross-check, tamper control; dyadic table exact; proof-read sound) | v13 raw sec:capf-l1 (identification inferential, flagged) | NEW v13_capf_planted_lower_count -> imgfib | planted binomial sublists, no pigeonhole loss; full-ImgFib poly bound FALSE in reserve regimes; imgfib quotient-budget clause confirmed consistent | corrected L1 problem (stabilizer-primitive poly bound) stays OPEN; no upper bounds |
| entropy-subfield envelope | stays CONJECTURE (agree with Codex) | def:capff1-gstar | v13_entropy_envelope_conjecture (unchanged) | -- | never a proof parent |
| Lean packages | statement-discipline reference only (agree) | experimental/lean | none | -- | not proof |
| line-ray saturation identity | PROVED (2026-07-08: proof read + independent Modal replay, 14 pairs, per-word + line + W-scan forms all exact) | grande_finale thm:saturation + prop:line-ray-saturation | f5_lineray_saturation_instrument (NEW, ev -> xr_smallcore_spread_count); F5_SKELETON P8 | support censuses factor through rays with exact fiber C(s,m); F5's per-W scan overcounts each ray by exactly C(s,k) | NOT an anti-concentration bound; the W-collision moment stays open |

Codex's "7 not 8" caveat: resolved — the critical surface has exactly 7 reds
(correct as rendered); the shared_census_kernel red is off-critical by design.
