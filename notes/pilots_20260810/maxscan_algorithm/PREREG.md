# PREREG — maxscan_algorithm (round 28)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

THE ONE UNDETERMINED NUMBER on RH-AC's supply side: the scaling of
the arbitrary-word maximum. Round 27's nonpoly_flank_census left it
honestly conflicted — the delta=1 mechanism's model collapses at
prize scale (2^-500), but the maximal-slack surplus GREW over the
two measured scales (+0.74 -> +0.94/1.25 bits) — and named the
deciding computation: the EXACT n=32, t=1 whole-word-space maxscan,
priced at C(32,15) ~ 5.7e8 subset-evaluations per word class,
"Modal-class, out of stdlib reach." ROUND 25'S LESSON IS YOUR
MANDATE: the z_n32_band pilot broke an "out of reach at 1G by any
kappa" wall with an ALGORITHM (BBM: contiguous residue buckets +
bisect — memory drop at no time cost). Try to break this wall the
same way BEFORE any compute is rented. Read first:
notes/pilots_20260809/nonpoly_flank_census/{REPORT.md,
FABLE_AUDIT.md, scratch/nf_maxscan.py}; the window-shift reduction
(the flank is the width-t window [delta+1, delta+t] — a LINEAR
structure that may be exploitable algorithmically); the
antipodal-pair-locator maximizer (its exact count profile at n=16:
16 members at agreement 9, 3 at 10).

## Deliverables

**D1 — THE ALGORITHM DESIGN (registered before implementation).**
Candidate routes to price (register your own list; these are
starters, not bounds): (a) the window-shift linear-algebra route —
the admissible set at (W, delta) is an affine subspace; counting
codewords at agreement >= a in an affine subspace of locator space
may reduce to rank/kernel computations per subset CLASS rather than
per subset; (b) the closed-form route — prove the
antipodal-pair-locator family's count exactly (its profile looks
structured) and prove it is the maximizer class, replacing
enumeration by a formula plus a bounded exceptional search; (c) the
meet-in-the-middle route — split the 32 evaluation points 16/16 and
join agreement counts (the BBM shape); (d) orbit quotients — the
scan at n=16 already deduplicates by a group; how far does the
symmetry cut n=32? Price each route in operations and RAM under
the 1G wall BEFORE building.

**D2 — THE VALIDATION LADDER.** Whatever you build must reproduce
the banked ground truth EXACTLY: the n=16 two-field maxima
(MAX_F_SUBSET = 46 at q=10177 AND q=10193, argmax at W1=0), the
n=8 exhaustive stratum data, and the delta=0 plateau at matched
cells. Run the ladder BEFORE the target scale.

**D3 — THE TARGET.** If the wall breaks: the exact n=32, t=1
whole-word-space maxscan at two independent fields (the round-27
two-field standard), and THE VERDICT: does the arbitrary-word
maximum grow toward the 4.83-bit razor need or collapse with the
delta=1 model? Register outcome thresholds in advance (what
measured max at n=32 counts as "grows", what as "collapses", what
as undetermined-still). If the wall does NOT break: validate the
best algorithm at the largest reachable n (register the honest
reachable point from your D1 pricing), and EMIT THE PRICED MODAL
REQUEST as a draft entry for notes/compute_requests (the exact
app design, sharding, fail-closed manifest plan, expected cost —
the Codex Modal-app pattern from the K3 campaign is the template),
written into your own dir for the coordinator to file.

**D4 — THE CLOSED-FORM BONUS (if budget remains).** The
antipodal-pair-locator count profile: prove it. A proved maximizer
family with a closed form would decide the scaling question at
EVERY n at once — strictly stronger than any single maxscan.

## Escape tests (before the main work)

- Replay nf_maxscan.py at n=8 (SCRATCH COPY) — exact match to the
  banked s2_maxscan_n8.json.
- Reproduce the n=16 argmax cell's count profile (46/19, {9:16,
  10:3}) from the banked machinery.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4302; do not read the other round-28 pilot dirs
  (apolar_origin, ssparse_endpoints, mca_safe_rewire). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint everything; background batches with
  results files for >10-min runs. The 1G ceiling is the wall you
  are trying to beat BY DESIGN, not by relaxation.
- DRAFT-ONLY: writes only in
  notes/pilots_20260810/maxscan_algorithm/; no dag/nodes/tools
  writes; no git; NO MODAL (you design the request; the
  coordinator files and runs it); stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C).
  Two-field confirmation for any structural claim (the round-27
  standard). Own-repo grep before claiming anything is missing
  (CATCH-24A).
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)
