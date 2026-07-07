# OVERNIGHT GOAL (2026-07-08, for Codex): close the shallow kernel at h = 3
# — unconditional theorems toward the F3 floor and the two prize problems

## 0. Mission context (read first, 5 minutes)

The Proximity Prize's two grand challenges are, in this repo's DAG
(~/smooth-read-solomin/prize/dag.json), PROVED conditional on exactly
SEVEN battle-hardened floor conjectures. Four of them (F1 dli, F2 u2c,
F3 u1_x4, F5 xr_smallcore) are proved or shape-level instances of ONE
shared object: anti-concentration censuses at sub-balance rows (the
"shared census kernel", node shared_census_kernel). The most attackable
isolated instance is the SHALLOW one behind F3: counts of constant-shift
divisor pairs of X^n - 1 (h-subsets of mu_n with equal e_1..e_{h-1}) at
rows q >= n^2. Current state (ALL of this is banked, machine-checked,
replayable — read before working):

- h = 2 stratum CLOSED (T_2 <= C n^{5/2} via Heath-Brown--Konyagin
  import; truth measured ~ n^2). Node f3_h2_stratum_theorem.
- h = 4, 5: primitive residue EMPTY at q >= n^2 in all data; the
  structured tail = X -> X^2 pullbacks of h=2 trades (decoded exactly).
- h = 3: T_3 = C(n/3,2)*[3|n] (toral) + n * #activated(q) (interior
  norm-gate families) + Poisson accidents. PROVED: the hyperbola normal
  form (same-fiber pairs satisfy X*Y = Delta; machine-verified
  2816/2816); the fiber cap max-fiber <= n/3 (moving-root). VERIFIED:
  interior families are NORM-GATE ACCIDENTS — rigid shapes sigma with
  obstruction elements E1(sigma), E2(sigma) in Z[zeta_n] that are
  NONZERO in char 0 but vanish mod p at the single activating prime;
  shape sets pairwise disjoint across 7 tested primes; 4/7 rows have
  EMPTY interiors.

READ (in order): 
  prize/critical/nodes/u1_x4_direct_column_budget/notes/F3_SHALLOW_LADDER.md
  prize/critical/nodes/u1_x4_direct_column_budget/notes/F3_IDENTIFICATION.md
  the scripts f3_*.py in the same directory (conventions + instruments)
  prize/critical/nodes/xr_smallcore_spread_count/notes/F5_SKELETON.md
  (P5-P7: the sunflower/pencil/moving-root lemma family)

## 1. THE TERMINAL GOALS (in priority order; ONE of A or B completed =
##    success; partial progress banked per the workflow = also success)

### TERMINAL A (primary): the char-0 classification theorem for h = 3

PROVE UNCONDITIONALLY: classify ALL pairs of disjoint 3-element subsets
{x1,x2,x3}, {y1,y2,y3} of roots of unity (any order n) in CHARACTERISTIC
ZERO satisfying x1+x2+x3 = y1+y2+y3 AND e_2 equal. Conjecture from data:
the only families are the toral ones (two mu_3-cosets, both signatures
zero) — but exotic families involving 5th/7th/9th roots of unity may
exist at special n; finding them is EQUALLY valuable (they predict new
paid columns at 5|n, 7|n rows — immediately testable!).

ROUTE (decomposed; bank each stage separately):
A1. E1 = x1+x2+x3-y1-y2-y3 = 0 is a vanishing sum of 6 roots of unity
    (with signs; absorb signs as -1 = zeta_2). The Conway--Jones
    classification of primitive vanishing sums of weight <= 9 applies:
    every solution decomposes into primitive sums of weights 2, 3, 5
    (R(2): 1+(-1); R(3): 1+w+w^2; R(5)-type with 5th roots; the known
    weight-6/7 primitives). ENUMERATE the finitely many decomposition
    TYPES of a 6-term signed vanishing sum. (Known result; reconstruct
    the type list and machine-verify each type numerically in C to 50
    digits before using it. If reconstruction of CJ stalls, prove the
    weaker Mann bound version: every solution has all ratios x_i/x_j,
    y_i/y_j etc. of order dividing an absolute constant M — Mann's
    theorem gives M effectively for 6 terms — and enumerate orders <= M
    by machine.)
A2. For each E1-type, impose E2 = 0 (the e_2 difference) and solve the
    resulting cyclotomic constraints exactly (sympy; minimal
    polynomials; NO floating point in final claims — numerics only as a
    screen). Output: the complete list of char-0 trade families.
A3. Machine-check the classification against the data: at every banked
    row, every persistent (cross-q) family must be in the list; the
    norm-gate families must NOT be (their E1, E2 are nonzero — already
    certified at 9601).
A4. COROLLARY (write it): every interior h=3 family at every row is
    p-selected: activation <=> p | gcd(N(E1), N(E2)) with E1, E2 != 0.
    Combined with |E_i| <= 6 (unit summands) and deg Q(zeta_n) = phi(n):
    log_2 |N(E_i)| <= phi(n) * log_2 6, so EACH SHAPE ACTIVATES AT AT
    MOST phi(n)*log_2(6)/log_2(n^2) PRIMES q >= n^2 — the
    AVERAGE-ACTIVATION THEOREM. State constants explicitly; verify
    against the 7-prime persistence data.
A5. TERMINAL STATEMENT (the node candidate, write as a formal theorem
    with proof): "h=3 interior classification: char-0 families = [the
    A2 list]; all other interior trades are norm-gate accidents with
    explicit activation bounds [A4]." If A1-A4 complete, draft the node
    statement + proof file (do NOT edit dag.json — see repo rules).

### TERMINAL B (secondary; independent of A): in-house explicit h=2

Upgrade f3_h2_stratum_theorem from an external import to a
self-contained theorem with EXPLICIT constants: reconstruct the
Stepanov-method proof that the additive energy of a multiplicative
subgroup H (|H| = n <= q^{2/3}) satisfies E(H) <= C n^{5/2} with an
explicit C (target C <= 100; any explicit C is a win). Machine-verify
every lemma of the reconstruction numerically at n <= 512 rows, and
verify the final constant against the banked ladder data (measured
truth ~ n^2, so generous constants still close the stratum:
T_2 <= E/8 <= (C/8) n^{5/2} < n^3 for n > (C/8)^2). If the full
reconstruction stalls, bank the partial: the auxiliary-polynomial
construction with its parameter arithmetic, and the exact statement of
the missing step.

### TERMINAL C (stretch, only after A or B): pair-coprimality on average

For random rigid shapes sigma, the norms N(E1(sigma)), N(E2(sigma))
generically share NO prime = 1 mod n. Any of: (i) a proof for a
positive-density subset of shapes; (ii) an exact computational census
of gcd(N(E1),N(E2)) over ALL shapes at n = 96 (Modal, shard it) giving
the empirical coprimality rate + the exceptional list; (iii) the
structural characterization of exceptional shapes. This lemma is shared
VERBATIM with F2's engineered-accident obstruction (F2-A2) — progress
here counts on two floors.

## 2. THE WORKFLOW LAWS (non-negotiable; these made tonight's results)

1. POSE PRECISELY BEFORE COMPUTING: every hunt/experiment gets a
   written statement of what would count as success/failure BEFORE the
   run (pre-registration). Bank the pose in your notes file first.
2. FALSIFICATION-FIRST: when you form a hypothesis, design the
   experiment that would REFUTE it, not confirm it. A refuted hypothesis
   is banked progress (tonight's affine-line refutation directly led to
   the hyperbola lemma).
3. MACHINE-CHECK EVERY IDENTITY: any algebraic identity you derive must
   be verified exactly (mod-p integers or exact cyclotomics) at multiple
   rows before you build on it. Tonight an alpha-sign error was caught
   ONLY because the identity was tested at scale. If a check fails,
   fix and re-run; never proceed on a failed check.
4. EXACT ARITHMETIC in all final claims. Floats only as screens, and
   any float screen must be followed by an exact confirmation.
5. HONEST LABELS: every banked claim is tagged PROVED (with proof) /
   MACHINE-VERIFIED (exact, finitely many cases) / VERIFIED-AT-ROWS
   (evidence, not proof) / HEURISTIC / REFUTED / OPEN. Never upgrade a
   label without the corresponding artifact. Catches (your own errors,
   found and fixed) are banked explicitly with what fired them.
6. BANK AS YOU GO, node-locally: everything goes in your notes file(s)
   under the relevant node's notes/ directory in YOUR worktree (see
   repo rules), with replay commands. A result that isn't banked with a
   replayable script does not exist.
7. NO OVERCLAIMING: distinguish "the data shows" from "we proved".
   The morning integration will replay everything; claims that don't
   replay are discarded and cost trust.

## 3. COMPUTE RULES

- Modal creds: ~/.modal.toml. CLI: ~/.venvs/modal/bin/modal run <script>.
- PREFER MODAL for anything beyond trivial arithmetic. Target < 60s per
  Modal task; shard larger work into < 60s pieces (map over shards).
  A task may exceed 60s ONLY if you are confident it is sensible and
  worthwhile (cap 240-280s; set the timeout explicitly).
- LOCAL RAM IS LIMITED: single process < 1.5 GB, prefer << 1 GB. Big
  arrays (q^2-cell DPs etc.) go to Modal with memory=4096-8192 and
  slice-wise updates (see f3_h3_program_modal.py for the pattern).
- int64 overflow guards + checksums on every DP (sum of fibers must
  equal C(n,h) — assert it; the guard caught a real overflow tonight).
- sympy is available in Modal images via .pip_install("sympy"); exact
  cyclotomic work (minimal polynomials, norms) belongs there. For norms
  in Z[zeta_n]: compute via resultants with the cyclotomic polynomial
  or by the product over Galois conjugates mod many primes + CRT —
  verify both routes agree on small cases first.

## 4. REPO RULES (one-writer discipline — violating these poisons the night)

- Work in a FRESH worktree: 
    cd ~/smooth-read-solomin/prize
    git worktree add ../prize-codex-overnight-20260708 -b codex/overnight-20260708
  and do ALL your work there. Commit early and often on that branch
  (one commit per completed stage, honest messages).
- DO NOT touch: prize/master (any file), dag.json (even in your
  worktree — node statements are maintainer-integrated after replay),
  the orbit/ artifacts, tools/publish_site.sh, anything under
  ~/smooth-read-solomin/rs-mca* (the upstream fork + three open PRs
  live there), the Claude artifacts, any remote (NO pushes, NO PRs,
  NO gh commands).
- Your deliverables are FILES in your worktree + commits on your branch.
  The maintainer replays and integrates in the morning.

## 5. THE OVERNIGHT LOOP

Repeat until MORNING (never stop early — completing a terminal advances
you to the next queue item, it does not end the night):
1. Pick the highest-priority open stage (A1 -> A2 -> A3 -> A4 -> A5,
   with B stages interleaved if A blocks).
2. Pose it precisely in the notes file (pre-register).
3. Attempt proof OR design the decisive experiment; run on Modal.
4. Machine-check; bank with label; commit.
   On completing a TERMINAL: write its node-candidate statement + proof
   file, mark it TERMINAL-COMPLETE in OVERNIGHT_LOG.md, then MOVE ON:
   A complete -> start B; B complete -> start C; all three complete ->
   the BONUS QUEUE, in order: (i) prove the h=4/5 emptiness (the
   pullback classification + no-primitive theorem the data supports);
   (ii) sweep h = 6, 7, 8 with the ladder machinery (new censuses,
   pullback decode, norm-gate certificates); (iii) POSE the h=3 per-row
   accident bound precisely (the Stepanov target: the h=3 analogue of
   HBK) with the auxiliary-polynomial ansatz written out — this is the
   final missing piece of the F3-green path and even a clean POSE is
   valuable.
5. Every ~2 hours, append a timestamped progress entry to
   OVERNIGHT_LOG.md in the worktree root: current stage, what is
   banked, what is blocked, next step. If genuinely blocked on a stage
   > 90 minutes, bank the precise blocker statement and move to the
   next stage or terminal.

## 6. MORNING HANDOFF (required)

Write OVERNIGHT_REPORT.md in the worktree root:
- Claims ranked by confidence, each with label, file, and REPLAY
  COMMAND (script + expected output digest).
- The catches of the night (errors caught + what fired them).
- Terminal status: which goal(s) reached; if none, the exact frontier
  (sharpest open statement + best attack).
- A <= 10-line executive summary at the top.

Success mode (A): the two prize problems get, through F3's floor, their
first fully-classified kernel stratum with unconditional activation
bounds. Success mode (B): the h=2 node becomes self-contained with
explicit constants (their finite-form discipline, our first in-house
Stepanov). Either is a substantial night. Both plus C is a jackpot.
