# PRE-REGISTRATION — THE GAMMA-SHELL QUESTION: refutation or re-pose (round 20, THE PRIORITY)

Round 20, 2026-08-06. Coordinator-authored brief; the pilot appends
its own registrations BEFORE any computation. THE BOARD'S SHARPEST
QUESTION: THEOREM DSA proved accidents exist at admissible tower
rows; whether that breaks the PRIZE-LEVEL statement or merely our
intermediate runs through the gamma-shell/budget analysis left open
at the DSA bank. Two live outcomes, both wins: WITHIN-BUDGET (our
intermediate was lossy — deliverable = the re-pose guidance) or
BUDGET-BREAK (a refutation path for the grand challenge itself — a
resolution). EXTREME honesty discipline required: a budget-break
claim would be the campaign's biggest single result and gets the
strongest possible falsifier treatment.

## 0. The state (quote verbatim before working)

- background/nodes/crossing_dsa_refutation (+ its 2026-08-06
  addendum: the scope condition is SATISFIED — tower rows are
  in-family; the refutation of OUR intermediate stands
  unconditionally; THIS pilot owns the prize-level consequence).
- The object of record: the crossing count is per-gamma-shell —
  X_w(gamma) = #{S in W_w : prod T(S) = gamma} (round-15 mun
  REPORT'S row map; the DSA witness has sig(S) = 1941325217792
  computed but its SHELL POPULATION undetermined).
- The consumer chain: critical/nodes/rate_half_list_adjacent_crossing
  (its statement + its budget B* = floor(q/2^128); at the witness
  row log2 B* = 127.510) and UPWARD — trace exactly which
  prize-level statement consumes the crossing node's bound, so any
  budget-break claim names the exact statement that breaks. Do not
  stop at our node.
- The accident family: DSA gives >= C(108,53) = 2^103.6 accidents
  at the witness row (one epsilon's fibre); the FULL family is
  larger (all epsilon in the pigeonhole class; LEMMA ROT orbits).

## 1. Pre-registered deliverables

- **(G1) THE SHELL MAP OF THE ACCIDENT FAMILY.** For the DSA
  accidents at the witness row: how do their sigs/gammas distribute
  over shells? Structure available: the accidents are lifts of
  reduced solutions (LEMMA DS bijection); sig behaves how under the
  2^33-periodic lift and the ROT orbit action? Derive the exact
  sig-arithmetic of the lift (a lifted S' has sig = f(sig'(S'),
  structure) — work it out), then the shell distribution law.
  Toy-verify the sig-arithmetic exhaustively at the three DSA gate
  shapes before any prize-row claim.
- **(G2) THE BUDGET COMPARISON.** Per-shell: structural population
  ~ 2^117.15 per sig class (round-15 [B3]) vs B* = 2^127.51 at the
  witness row — the structural margin is ~ 2^10.4. The accidents
  add HOW MUCH to the MAXIMAL shell? Three regimes to decide:
  (i) accidents spread ~uniformly over 2^41 shells (adds ~2^62.6
  per shell from the single-epsilon fibre — negligible vs 2^117);
  (ii) accidents concentrate on FEW shells (the periodic lift may
  force sig into a small coset! — check this FIRST, it is the
  danger case); (iii) intermediate. The full-family count (all
  epsilons, orbit-corrected per LEMMA ROT + the ssl CATCH-19A
  scope note: the crossing instance IS all-odd so the 2N constant
  applies) must be estimated with stated error bars, worst case
  first.
- **(G3) THE VERDICT, with the refutation protocol.** If the
  maximal-shell total exceeds B* at ANY admissible row: STOP,
  pre-registered-falsifier-check everything, produce a
  self-contained reproduction script computing the exact per-shell
  count and the exact budget at that row, trace the consumer chain
  to the prize-level statement, and report which statement breaks
  — clearly labelled as a CANDIDATE refutation for coordinator
  replay, NOT a claimed resolution. If within budget at all
  admissible rows: state the margin law and the RE-POSE guidance
  (what the crossing intermediate should claim instead — e.g. a
  per-shell bound with the accident term priced in).
- **(G4) THE PT-2 INTERACTION.** The bracket endpoint clears the
  ternary threshold by 0.336 bits (tern_master_threshold watch
  line). Does the shell analysis change at w just above 2^34 vs at
  the endpoint? State whether the re-pose (if that is the verdict)
  is stable across the bracket.

## 2. Pre-registered falsifiers / honesty clauses

- The sig-arithmetic toy gate is MANDATORY before prize claims.
- A budget-break claim requires: exact arithmetic (no floats at the
  comparison), BOTH the count lower bound and the budget upper
  bound derived with citations, the consumer chain traced to the
  prize statement, and the CANDIDATE label. Overclaim on this
  question is the worst failure mode available to this campaign.
- A within-budget verdict must state the margin at the WORST
  admissible row, not a favourable one.
- Concentration (regime ii) must be decided by proof or exhaustive
  toy census, never assumed away.

## 3. Rules of engagement

- DRAFT ONLY: write only inside notes/pilots_20260806/gamma_shell/.
  Never edit dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/crossing_gap/ (sibling this round). Do NOT
  read CAMPAIGN_LEDGER entries appended after the "ROUND 20
  LAUNCHED" marker (the round-19 quarantine rule).
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

---

# PILOT PRE-REGISTRATIONS (appended BEFORE any computation)

Opus pilot, round 20, 2026-08-06. Everything below is registered
before a single line of arithmetic is run. Machine checks land in
`toy_shell.py` (toy stages) and `shell_exhibit.py` (prize-row stages),
both fail-closed (a permanent `failclosed` stage exits 1).

## P0. The objects, as I will use them (all quoted in PROOFS.md)

`sig(S) := sum_{i in S} i mod n`;
`prod T(S) = x_0^{r'} zeta^{sig(S)}`; so the gamma-SHELL is exactly a
`sig` class mod `n = 2^41` and `X_w(gamma) = #{S in W_w : sig(S) = t(gamma)}`.
`gamma = (-1)^{r'+1} c` with `c` a FREE parameter of the received word
`u = X^{n-1} + c X^{k+w-1}`, so every shell is realisable by an actual
received word: the max-shell count is a genuine lower bound on `L_1(k+w)`.

## P1 (G1). THE SIG-ARITHMETIC OF THE PERIODIC LIFT — registered claim

Let `a = v-1`, `n_a = 2^{42-v}`, `L = 2^{41-v}`, and let `S` be the lift of
`S' <= Z/n_a`, i.e. `S = {j + n_a t : j in S', 0 <= t < 2^a}`. Registered:

```text
(SIG-LIFT)   sig(S)  ==  2^a * sigma'(S')  +  |S'| * n_a * 2^{a-1} * (2^a - 1)   (mod n)
```

with `sigma'(S') = sum_{j in S'} j` as an INTEGER, and at the prize shape
(`v = 34`, `|S'| = 126`, `a = 33`, `n_a = 256`) the second term is
**identically 0 mod 2^41**, so `sig(S) = 2^33 * sigma'(S') mod 2^41`, which
depends on `S'` only through `sigma'(S') mod n_a`.

**Falsifier F1 (MANDATORY GATE):** (SIG-LIFT) fails for a single `(S', shape)`
at any of the three DSA gate shapes `(n,w) = (32,8), (64,8), (64,16)`,
exhaustively over every `S'`. If F1 fires I abandon every prize-row claim.

## P2 (G1/G2). THE SHELL MAP — registered claim, and THE DANGER CASE FIRST

Registered predictions, in the order the brief demands (concentration first):

- **(SHELL-CONC)** Every deep-stratum member (structural or accidental) has
  `sig(S) in 2^a * Z/n`, a subgroup of order `n_a = 2L`. So the whole deep
  stratum lives in **`2L` shells out of `n`** — at the prize row **256 of
  `2^41`**, a concentration factor `2^33`. **Regime (ii) is the truth, not
  regime (i).** I register this BEFORE computing.
- **(SHELL-STRUCT)** Structural members have `sigma'` EVEN, so they occupy
  exactly the `L` shells `2^{a+1} Z/n` (128 shells at the prize row), with
  EXACTLY `C(2L, ...)`-equidistribution: `C(128,63)/128 = 2^117.149`, which
  must reproduce the banked `[B4]` figure `2^117.1491` EXACTLY. If it does
  not, my shell dictionary is wrong and I stop.
- **(SHELL-ACC)** An accident with `sigma'` even lands in a STRUCTURAL shell;
  with `sigma'` odd it lands in one of `L` shells disjoint from the structural
  ones. Within one `eps`-fibre the shell is `const + 2*(sum of the chosen
  zero-pair indices)`, so a fibre spreads over at most `L` shells of ONE
  parity class.

**Falsifier F2:** at any toy shape the deep-stratum members occupy more than
`2L` distinct `sig` values, or the structural per-shell count is not
`|W^struct|/L`.

## P3 (G2). THE PROVED ACCIDENT-COUNT LOWER BOUND (new; the load-bearing step)

Registered new argument (Cauchy-Schwarz + LEMMA TC fibre weight):

Let `D = {x in {0,1}^L : x_{L-1} = 0, |x| even}`, `|D| = 2^{L-2}`, and
`phi(x) = sum_j x_j theta^j in F_{p^{delta_a}}`. Put `Q = p^{delta_a}`.

1. **(MULT)** For each nonzero relation `eps` with `eps_{L-1} = 0` and `U`
   even, `#{(x,y) in D^2 : x - y = eps} = 2^{L-2-U}` EXACTLY.
2. **(PAIRS)** `P := #{(x,y) in D^2, x != y, phi(x) = phi(y)} >= |D|^2/Q - |D|`
   (Cauchy-Schwarz), and `P = sum_{eps} 2^{L-2-U(eps)}` over those relations.
3. **(RATIO)** `rho(U) := C(L-U, (r'_a-U)/2) / 2^{L-2-U} >= rho_min :=
   min over even U in [2, r'_a]`, attained at `U = 2`.
4. **(COUNT)** Hence the number of NON-STRUCTURAL deep-stratum reduced
   solutions obeys `N_acc >= rho_min * (|D|^2/Q - |D|)`, PROVED, no heuristic.

**Falsifier F3:** at any toy shape, exhaustively, either (MULT) fails, or the
exact `N_acc` is smaller than the bound of (COUNT). Either kills the argument.

## P4 (G2/G3). THE COMPARISON — exact integers only

`Xmax := ceil(N_acc_lower / 2L) + structural-per-shell-if-same-parity` vs
`B* = floor(q/2^128)`, at the witness row `p = 3*2^41+1, e = 6`. All integer
arithmetic (`math.comb`, `Fraction`); floats only for display `log2`.
Registered prediction: **the comparison BREAKS the budget** — I predict
`log2 Xmax` in `[195, 205]` against `log2 B* = 127.510`. I register the
predicted interval so a miss is visible.

**Falsifier F4:** `Xmax <= B*` at the witness row => verdict is WITHIN-BUDGET
and I deliver the re-pose guidance instead.

## P5 (G3). WHAT ACTUALLY BREAKS — registered honesty clause

I register IN ADVANCE that I will check the LOGICAL FORM of every consumer
statement before calling anything a refutation. In particular `(RHL-ADJ)`
("there is an agreement index `a_L(C)` such that ...") is an EXISTENCE
statement and a larger `L_1` at one agreement CANNOT refute it — it relocates
`a_L`. If the budget breaks I must therefore report precisely which claim
dies (safe-side at `w = 2^34`) and which does NOT (the node's own (RHL-ADJ),
the grand challenges as determinations), and label the result a CANDIDATE
for coordinator replay. Overclaiming the grand-challenge consequence is the
failure mode I am most exposed to and I pre-commit against it.

**Falsifier F5:** if the consumer chain shows no statement of record asserts
safety at `a = k+2^34`, the correct verdict is THRESHOLD RELOCATION, not
refutation, and I will say so.

## P6 (G4). PT-2 STABILITY — registered claim

The shell divisor is `2L = 2^{42-v}` and the structural shell count is
`S(v) = C(2^{41-v}, 2^{40-v}-1)/2^{41-v}`; both are `w`-dependent. Registered
prediction: the accident term is decisive ONLY at `v = 34` and dies at
`v >= 35` (proved-existence needs `log2 p < L-2`), so the verdict is NOT
uniform across the bracket. I will state the whole `v` profile.

**Falsifier F6:** the break survives at `v >= 36` (would contradict THEOREM
DSA's own coverage table) — that would indicate an error in my count.

## P7. Row scope — the WORST admissible row, not a favourable one

I must report the comparison at the worst row for my claim, and separately
identify the row set on which the break holds. Registered: the break needs
BOTH (i) `w = 2^34` live at the row (`log2 B* >= 117.149`, i.e.
`log2 q >= 245.149`) and (ii) the DSA regime `p^{delta_a} < 2^{L-2}`. I will
enumerate the admissible `(class, e)` pairs meeting both and report the
MINIMUM margin over them.
