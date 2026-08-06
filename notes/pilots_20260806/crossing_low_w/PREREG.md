# PRE-REGISTRATION — the LOW-w CROSSING CORE (generative): the deep stratum and the w = 2 principal question

Round 18, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. GENERATIVE lens: prove
suppression on (part of) the uncovered low-w crossing region, or
characterize exactly what is true there.

## 0. The target (the round-17 convergent frontier)

THEOREM CS (banked, notes/pilots_20260806/es_coprimality/) proves the
(ES) crossing instance unconditionally wherever
ceil((w-1)/2)·log2 p > (n/4)·log2 r'; at 256-bit p that is every
w > w* = 2^37.3131. The UNCOVERED region is w in [2^34, ~2^37.31] —
and three blind round-17 pilots converged on its structure:
- es_g_lanes §3: the binding obstruction is the DEEPEST stratum
  a = v-1, where exactly ONE condition survives; at w = 2^34 the
  instance is n_a = 256, |Z^(a)| in {1,2}, and no admissible row
  clears the balance requirement (log2 p >= 256 = the rules cap).
- es_coprimality LEMMA STRAT + CATCH-17C: the deep exceptional
  witnesses reduce to w' = 2 PRINCIPAL instances — the reduced ideal
  is principal and non-coprimality is generic there.
- CS2 is SHARP (AM-GM equality attained), so the gap CANNOT be closed
  by sharpening the archimedean side. A different idea is required.

## 1. Source surfaces (read ALL first; quote verbatim)

- notes/pilots_20260806/es_coprimality/{REPORT.md, PROOFS.md} —
  THEOREM CS, LEMMA STRAT, LEMMA TWO (N_odd is the invariant; r'
  even forces 2 | N), the E_floor definition, the residual bad-prime
  list {3,7,17,47,97,193,257,353,449}, COROLLARY CS-TOWER.
- notes/pilots_20260806/es_g_lanes/{REPORT.md, PROOFS.md} — the
  stratum table (§3), the |Z_w| closed forms per admissible p-class,
  the 19 admissible (p-class, e) pairs, the w = 2^34 exhibit row.
- notes/pilots_20260806/es_boundary_adversary/REPORT.md — the five
  witnesses and the census method (ground truth machinery).
- critical/nodes/b1_char0_giant_coset_theorem — LEMMA Z (cited).

## 2. Pre-registered deliverables

- **(G1) THE w = 2 PRINCIPAL QUESTION, stated exactly.** At a w' = 2
  instance the ideal is (x_1), principal, and non-coprimality is
  "generic" — but the OBLIGATION is not coprimality, it is the
  original count statement transported down the stratum. State
  exactly what the crossing lane needs at the reduced instance
  (n' = n/2^a, one condition, weight r'/2^a): which S' are
  admissible members, what the structural family is there, and what
  "no accidents" means. Do NOT inherit the balance frame — it is
  provably unavailable here.
- **(G2) THE n_a = 256 INSTANCE, attacked directly.** At w = 2^34,
  the binding stratum is n_a = 256, ONE surviving condition
  (x_1' = 0 or the single closure orbit), weight r'_a = r'/2^a.
  This is small enough for exact structure: the solutions of
  p_1(S') = 0 with S' <= mu_256, |S'| = r'_a mod p — LEMMA Z
  characterizes char-0; what survives mod p is a vanishing-sum
  question at n' = 256. Enumerate/characterize EXACTLY which
  reduced-instance solutions LIFT to admissible members of the
  original crossing window system (the lift constraint is the
  un-collapsed even-index conditions — they are not free; LEMMA
  STRAT tells you which survive). The conjecture to test: the lift
  constraints kill every non-structural reduced solution — i.e. the
  deep stratum is EMPTY of accidents for a reason invisible to
  balance. Toy-verify the lift mechanism exhaustively at
  (n, n_a) = (32, 8), (64, 8), (64, 16) before claiming anything.
- **(G3) The covered/uncovered split refined.** With (G2)'s lift
  constraints priced, recompute which part of [2^34, 2^37.31]
  becomes covered by CS + stratum-emptiness. State the exact
  remaining set.
- **(G4) If the lift conjecture FAILS** (a reduced solution lifts):
  that is a constructive path toward a crossing accident — follow it
  UP: does it lift all the way to a genuine accident at a scaled
  row? That would be a campaign-critical catch on the crossing lane
  (report witness + reproduction script, stop).

## 3. Pre-registered falsifiers / honesty clauses

- The toy lift-mechanism verification is a GATE: no claim about the
  prize rows unless the mechanism is exhaustively correct at all
  three toy shapes.
- If the deep stratum is empty for balance-invisible reasons, the
  proof must not smuggle balance back in — self-check the argument
  against the es_g_lanes verdict that no admissible row clears it.
- AK-UNIT check as in round 17: no congruence conclusions about
  counts.

## 4. Rules of engagement

- DRAFT ONLY: write only inside notes/pilots_20260806/crossing_low_w/.
  Never edit dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/efloor_sparsity/ (sibling this round).
- COMPUTE LAW: never bare python3 — tools/ramguard tiny|local --
  python3 ..., literal --, from repo root
  /home/u2470931/smooth-read-solomin/prize. This includes file
  patching and JSON peeking (three round-17 pilots breached exactly
  there; use Edit-style heredocs under ramguard).
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report;
  the coordinator persists it verbatim.

---

# PILOT PRE-REGISTRATIONS (appended by the Opus pilot BEFORE any computation)

Round 18, 2026-08-06. Nothing below has been computed at the time of
writing; the only actions taken so far are reads of the four source
surfaces named in §1. Registrations are numbered **X0-X9**.

## X0. The reduced instance, exactly (this is my G1 answer, registered)

Sources, verbatim:

- `notes/pilots_20260806/es_coprimality/PROOFS.md:143-151` (LEMMA STRAT):
  > `strat(S) >= a >= 1`, i.e. `S` is `(n/2^a)`-periodic. Put
  > `n_a = n/2^a`, let `S' <= Z/n_a` be the reduced set (`|S'| = r'/2^a`)
  > ... 1. `x_s = 0` whenever `2^a` does not divide `s`;
  > 2. `x_{2^a t} = 2^a * iota(p_t(S'))` ...
  > 3. `I_S = 2^a * iota(I_{S'})O_K` with `w' = floor((w-1)/2^a) + 1`;
- `notes/pilots_20260806/es_g_lanes/PROOFS.md:201-202`:
  > `n_a = 2^{41-a},   W_a = floor((w-1)/2^a) = 2^{v-a} - 1,   r'_a = r'/2^a,`
- `notes/pilots_20260806/es_g_lanes/PROOFS.md:221-223`:
  > At `a = v-1`: `n_a = 2^{42-v}`, exactly ONE condition survives
  > (`s = 2^{v-1}`, since `2*2^{v-1} = 2^v > w-1`), so `|Z^{(a)}| in {1,2}`

I register the following closed form, to be machine-checked: with
`n = 2^41`, `w = 2^v`, `r' = 2^40 - w`, `a = v-1`,

```
n_a = 2^{42-v},   L := n_a/2 = 2^{41-v},   r'_a = r'/2^{v-1} = L - 2,
one condition:  p_1(S') = sum_{j in S'} theta^j = 0,   theta = zeta_{n_a}.
```

So the deep-stratum family is UNIFORM in `v`: `(n_a, r'_a) = (2L, L-2)`,
`L = 2^{41-v}`; at `v = 34`, `(256, 126)` and `L = 128`.
**Prediction X0:** `r'_a = L - 2` exactly, for every `v = 34..39`.

## X1. THE LIFT IS FREE — I register the NEGATION of the brief's conjecture

The brief (§2 G2) conjectures *"the lift constraints kill every
non-structural reduced solution"*, the lift constraint being *"the
un-collapsed even-index conditions"*. **I register, before computing,
that I expect this to be FALSE because the constraint set is EMPTY.**
By LEMMA STRAT (1) every condition `x_s` with `2^a \nmid s` vanishes
IDENTICALLY on a `mu_{2^a}`-coset union; at `a = v-1` the only `s` in
`[1, w-1]` divisible by `2^a` is `s = 2^{v-1}`. Therefore

```
{ S in W_w : strat(S) >= v-1 }  <->  { S' <= Z/n_a : |S'| = L-2, p_1(S') = 0 }
```

is a BIJECTION with no side conditions, and it carries
structural <-> structural (`strat(S) >= v  <->  S' a union of antipodal
pairs). **Prediction X1:** every reduced solution lifts; the number of
surviving lift constraints is exactly 0.

## X2. THE TERNARY COLLAPSE — the new pricing functional

Since `theta^L = -1` in any field where `theta` has order `2L`, the single
condition depends on `S'` only through

```
eps_j := [j in S'] - [j + L in S']  in {0,+1,-1},   j = 0..L-1,
p_1(S') = sum_j eps_j theta^j.
```

With `U(eps) = #{j : eps_j != 0}` and `B = (r'_a - U)/2`, the fibre over
`eps` has size `C(L-U, (r'_a-U)/2)` and is nonempty iff `U ≡ r'_a mod 2`
and `U <= r'_a`. **Registered identity, to be machine-checked exhaustively
at `L = 4, 8` and by count at `L = 16`:**

```
sum_{eps in {0,±1}^L, U ≡ r'_a (2), U <= r'_a} C(L-U, (r'_a-U)/2) = C(2L, r'_a).
```

**Prediction X2:** the correct primitive object of the deep stratum is
`eps`, of which there are `3^L`, NOT the `2^{n_a} = 4^L` of the global
functional and NOT the `C(2L, L-2)` of the per-weight functional. At
`v = 34`: `log2 3^128 = 202.875` vs global `256` and per-weight
`log2 C(256,126) = 251.628` (`es_g_lanes/REPORT.md:105`). I predict the
per-weight functional MIS-PRICES this stratum by ~48.75 bits because its
solutions are fibred, not independent.

## X3. EXISTENCE THEOREM (pigeonhole) — registered as the G4 branch

**Registered claim.** Let `delta_a = ord_{n_a}(p)`. If

```
p^{delta_a} < 2^{L-2}
```

then there EXISTS `eps in {0,±1}^L`, `eps != 0`, with
`sum_j eps_j theta^j = 0` in `F_{p^{delta_a}}`, `U(eps)` even and
`2 <= U(eps) <= L-2`. Proof to be written: pigeonhole the `2^{L-2}` vectors
`a in {0,1}^L` with `a_{L-1} = 0` and `|a|` even into `F_{p^{delta_a}}`;
a collision `a != b` gives `eps = a-b`, whose support is the symmetric
difference, hence even, hence `<= L-2`.

**Prediction X3:** combined with X1 this makes (ES) FALSE at every
admissible crossing row with `w = 2^34` and `p^{delta_a} < 2^126`. Since
`|F| < 2^256` (`critical/nodes/rules_freeze/statement.md:9`, quoted at
`es_g_lanes/PROOFS.md:86`) forces `p < 2^{256/e}`, every tower row with
`e >= 3` has `p < 2^{85.34}`. Extension rows are admissible per
`critical/nodes/axis8_generating/proof.md:13-14` (quoted at
`es_g_lanes/PROOFS.md:79-82`). **I predict G4 FIRES on tower rows and
does NOT fire on the recorded prime rows `q = p ~ 2^256`.**

## X4. The prime-row verdict (registered as a HEURISTIC, not a theorem)

At the recorded crossing rows (`q = p` prime, `log2 p ~ 256`, `delta = 1`)
the expected number of nonzero ternary relations is `3^128/p = 2^{-53.1}`.
**Prediction X4:** the deep stratum at prime rows is empty, with a
**53.1-bit** margin — a margin invisible to both balance functionals
(global fails by ~0.09 bits; per-weight passes by only 4.37 bits). This is
registered explicitly as a counting heuristic; I will NOT call it proved.

## X5. The unresolved band, registered in advance

Between `p^{delta_a} = 2^{L-2}` (provable existence) and `3^L` (heuristic
emptiness) there is a band where I expect to prove NOTHING. At `v = 34`
that is `log2 p in [126, 202.875]`. I register this gap now so that a
later claim of full coverage is checkable against it.

## X6. Toy gate (the brief's mandatory gate) — exact shapes

`(n, n_a) = (32,8), (64,8), (64,16)`, which in my parametrisation are

```
(32, 8):  a=2, v=3, w=8,  r'=8,  L=4, r'_a=2
(64, 8):  a=3, v=4, w=16, r'=16, L=4, r'_a=2
(64,16):  a=2, v=3, w=8,  r'=24, L=8, r'_a=6
```

At each: (i) verify LEMMA STRAT (1)+(2) exhaustively; (ii) verify the X1
bijection exhaustively over ALL `S'`; (iii) verify the X2 fibre identity;
(iv) at `(64,16)` with small `p ≡ 1 mod 16`, exhibit a non-structural
reduced solution and verify its lift `S <= Z/64`, `|S| = 24`, against ALL
`w-1 = 7` conditions by direct evaluation.

**Extra ground truth I register now:** a FULL brute-force census of
`W_8` at `n = 32, r' = 8` over all `C(32,8) = 10,518,300` subsets, for
several `p ≡ 1 mod 32`, decomposed by `strat`. This is the only place
where "are there OTHER accidents (at `a < v-1`)?" is answered honestly.

## X7. Prize-scale exhibit (if X3 fires)

Construct an explicit admissible row and an explicit `eps` by
meet-in-the-middle (support exactly 8: `k=4` on `{0..63}` and `k=4` on
`{64..127}`, giving `U = 8`, even). Then verify at `n = 2^41` itself:
`|S| = r'`, `p_1(S') = 0`, `S` not a `mu_{2^34}`-coset union, and
`x_s(S) = 0` for `s` in `[1,2^34-1]` — the `2^33 \nmid s` cases by the
exact geometric-sum identity evaluated in `F_p` on a random sample plus
the proof, the `s = 2^33` case directly.

## X8. FALSIFIERS

- **F1.** If any reduced solution fails a full-system condition, X1 is
  refuted and I report it as such (the brief's conjecture would then be
  live).
- **F2.** If the `(64,16)` toy produces a reduced non-structural solution
  that does NOT lift, the whole G4 branch dies and I report it.
- **F3.** If the X2 fibre identity fails at any toy, X2 is refuted.
- **F4.** If the `n=32` full census finds non-structural members of `W_8`
  whose `strat` is NOT `>= v-1`, then the deep stratum is not the whole
  story and I must say so rather than presenting it as complete.
- **F5 (no balance smuggling).** X3 is pure pigeonhole and uses no balance
  functional; X4 is labelled heuristic. I will self-check the final
  argument line-by-line against `es_g_lanes/REPORT.md:103` (*"no
  admissible row reaches either"*) and report any place a balance
  inequality re-enters.
- **F6 (AK-UNIT).** No conclusion of mine may be a congruence on a count.
  My conclusions are (i) existence of an individual `S`, and (ii) the
  inequality `|W_w| > C(n/M, r'/M)`. Neither is a congruence.
- **F7.** If the prize-scale MITM finds no `eps`, I report the search as
  failed rather than asserting existence from the pigeonhole alone —
  though the pigeonhole, if proved, stands on its own.

## X9. What I will NOT claim

I will not claim the low-`w` crossing core is CLOSED. The best available
outcome is: a proved dichotomy (tower rows refuted / prime rows re-priced
with a 53-bit heuristic margin) plus an exactly stated residual (X5).
