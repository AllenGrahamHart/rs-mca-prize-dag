# PR body draft: Pruned-Q toy packet (Good-first-PR #1)

Title: Pruned-Q toy packet: first-match pruned prefix-fiber distributions at
exactly enumerable rows (`prob:row-sharp-q` calibration)

---

This answers Good-first-PR #1 ("Write a small exact Q toy packet that tests
`prob:row-sharp-q` on a row where the full fiber distribution can be
enumerated") and supplies what the in-tree censuses lack: the fiber
distribution AFTER first-match pruning. `rowsharp_q_external_calibration.md` /
`qsp_fiber_census.py` are raw-distribution only; `qsp_modeatnull_structure.py`
classifies the members of one fiber. This packet applies those same two
classifiers — your "obvious quotient-pullback classifiers" (C1 coset-union
S = -S, then C2 dilation-stable gS = S, first-match order) — to every member
of every fiber at four of your census rows, and prints the residual
(trivial-stabilizer) distributions with `def:q-row-atom` normalization.

**Rows** (all from `FIBER_DEFAULT`): (17,16,8) w=1-3 and (41,20,10) w=1-3 by
direct enumeration; (101,50,25) w=2 and (257,64,34) w=1 by exact stdlib
big-int DP. ((257,64,34,2) excluded by compute budget.)

**Anchors (digit-exact, fail-closed):** max / null / sum N^2 against
`rowsharp_q_external_calibration.json` on all 8 row-depths; the printed
max-to-mean ratios of `rem:capff1-collision-gap` (1.0012/1.2126/2.6722,
1.0022/1.2101/4.1034); checksums sum N_w = C(N,m); the full (41,20,10,2)
mode-at-null datum (66 / 133 at (11,0) / uniform orbit line / classifier
counts (0,0)).

**Pruned side, double-computed per fiber:** per-member classification
(enumeration) vs subgroup-lattice inclusion-exclusion of exact coset-DPs;
monotonicity and mass identities gated; hand-derived cell totals (70; 252+4;
252; C(32,17) = 565722720) gated.

**Headline results** (full table in the note):

- Row-sharp Q supported at every tested row: pruned max <= raw max everywhere,
  and every pruned overhead R = p^w max|P_Q| / C(N,m) is below the binding
  M31-list full-budget allowance 8.4152 (Poisson depth-3 rows included).
- Where the raw argmax is the null fiber, pruning usually moves the max to a
  clean fiber; at (17,16,8,1) the pruned overhead drops below 1 (0.999922).
- Mode-at-null by-catch: rung-charging the quotient-pullback classes deepens
  the (41,20,10,2) null suppression (66 -> 60; max/null 2.02 -> 2.22, max 133
  untouched) — direct input to the calibration note's open "is the (.,0) line
  rung-charged?" item, and mild support for the exchange-compression
  alternative at rows of this shape.
- Depth-3 null fibers at both enumerable rows are 100% quotient-pullback
  (pruned null = 0).
- Exact residual masses tau (the "actual residual mass" of
  `prop:q-moment-order-floor`) printed per row, e.g. 184500/184756 at
  (41,20,10).

**Verifier:** one zero-argument stdlib-only script, exact integers/Fractions
in every decision, ~2 s, `RESULT: PASS (104/104 checks; 4/4 mutation controls
caught)`, identical under `python3 -O`. Mutation controls: wrong cell
membership, off-by-one depth, wrong bound constant, wrong domain — each must
flip a named check.

**Honest scope:** the pruning ledger is exactly your two in-tree toy
classifiers applied in first-match order; the deployed-row cells with no toy
instantiation (tangent, common-support, planted, field-drop, extension, rank)
are reported as not-modeled, not silently assumed empty. Calibration only;
enters no proof; does not prove `prob:row-sharp-q`; toy rows are not deployed
rows; SS0.4/SS0.5 and the official score are untouched.

Files: `experimental/scripts/verify_rowsharp_q_pruned_toy_packet.py`,
`experimental/notes/audits/rowsharp_q_pruned_toy_packet.md`,
`experimental/data/rowsharp_q_pruned_toy_packet.json`.
