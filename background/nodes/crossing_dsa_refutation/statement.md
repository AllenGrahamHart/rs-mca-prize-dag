# crossing_dsa_refutation

- **status:** PROVED (a refutation + a lemma kit + a scoped
  heuristic re-pricing)
- **minted:** 2026-08-06 (mint-4, round 18), coordinator-audited.
- **provenance:** notes/pilots_20260806/crossing_low_w/ (1,565,906
  checks; coordinator replayed the bijection gate 81,005/0 and the
  witness verification 2,854/0).

## Statement

THE DEEP-STRATUM STRUCTURE OF THE LOW-w CROSSING CORE, AND THEOREM
DSA: THE (ES) CROSSING INSTANCE IS FALSE AT ADMISSIBLE TOWER ROWS.

**LEMMA DS.** At n = 2^41, w = 2^v, r' = 2^40 - w, the deepest
stratum a = v-1 has n_a = 2^{42-v}, L = 2^{41-v}, r'_a = L - 2
(uniformly in v — ONE one-parameter family (2L, L-2)), a single
surviving condition p_1(S') = 0, and the stratum members biject with
reduced solutions WITH NO SIDE CONDITIONS (LEMMA FREE: zero lift
constraints — every non-structural reduced solution lifts freely).
Toy-gated exhaustively at (32,8), (64,8), (64,16): 81,005/0.

**LEMMA OE.** Odd-index conditions see only eps_j = [j in S'] -
[j+L in S'] (ternary); even-index conditions see only sigma and ARE
the next stratum's conditions. The even-condition mechanism is real
at every shallower stratum and vacuous exactly at the binding one.

**LEMMA TC (the corrected pricing).** The stratum's primitive object
is eps in {0,±1}^L — 3^L, NOT 2^{n_a} (the global functional, which
requires log2 p >= 256 = the cap) and NOT C(n_a, r'_a) (the retired
per-weight functional, 48.75 bits mis-priced). Requirement at
v = 34: 202.875 (194.875 orbit-corrected, LEMMA ROT: relations come
in orbits of size 2L; Poisson estimates over-predict by 2L).

**THEOREM DSA (unconditional pigeonhole).** If p^{delta_a} <
2^{L-2} then a nonzero ternary relation exists with even support
<= r'_a, hence W_w contains a NON-STRUCTURAL member and |W_w| >
C(n/M, r'/M): the (ES) crossing instance is FALSE at that row. No
balance functional appears. Coverage over the 19 admissible
(class, e) pairs at w = 2^34: ALL = 10, PART = 6, NONE = 3; at
2^35: 3/5; nothing at 2^36+.

**THE WITNESS (verified at n = 2^41 itself, 2,854/0):**
p = 6597069766657 = 3·2^41+1, e = 6, q = p^6 (the
triple-refutation row — also es_g_lanes' above-balance exhibit and
f2_adm's (O1) kill); an explicit eps with U = 20 gives |S'| = 126,
p_1(S') = 0, non-antipodal, lifting to S of size exactly r' with
ALL 2^34 - 1 window conditions verified (the G(s) product
factorisation cross-checked exhaustively at n = 64, 128).
|W_{2^34}| >= C(128,63) + C(108,53) > C(128,63).

**THE DICHOTOMY.** e = 1 prime rows are NEVER in the DSA regime:
B* >= 3 forces log2 p >= 129.585 > 126. The recorded prize rows are
untouched and RE-PRICED (HEURISTIC, labelled): expected relation
count 3^128/p = 2^{-53.1}, orbit-corrected 2^{-61.1} — a 53-61 bit
margin replacing the 0.089-bit global-functional cliff.

**SCOPE (load-bearing, honest):** the refutation applies under the
campaign's adopted reading that tower rows are in the crossing
lane's obligation (axis8_generating PROVED + the es_g_lanes bank +
B* >= 3). If the official family excludes towers (MAINTAINER
question), CATCH-18A shrinks to nothing and the lemma kit +
re-pricing survive.

## Falsifier

A verified failure of the witness's window conditions; a lift
constraint at the deepest stratum; an e = 1 admissible row inside
the DSA regime.

## NOT claimed

Emptiness at prime rows (heuristic only); the gamma-shell population
of the accidents (the crossing NODE's budget question at tower rows
is RE-OPENED, not decided); strata a < v-1 (LEMMA OE gives the
recursion, not carried out); w = 2^36, 2^37 deep strata.

## Addendum (2026-08-06, the scope ruling — the refutation's condition is SATISFIED)

The scope clause above ("applies under the campaign's adopted
reading that tower rows are in the crossing lane's obligation") is
RESOLVED: the frozen spec's quantifier contains no generation
restriction, so tower rows ARE in the challenge family (coordinator
ruling, CAMPAIGN_LEDGER 2026-08-06). THEOREM DSA's refutation of
the (ES) crossing instance at those rows therefore stands
unconditionally. What it refutes is OUR intermediate; the
prize-level consequence runs through the OPEN gamma-shell/budget
question (round-20 target): within-budget => the intermediate was
lossy (re-pose); budget-break => a refutation path for the grand
challenge itself.
