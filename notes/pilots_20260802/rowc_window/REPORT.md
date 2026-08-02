# Pilot report: the RowC window adjudicated (Opus 5, 2026-08-02)

Coordinator note: condensed persistence (full detail in the JSONs);
audit in FABLE_AUDIT.md. Self-test (2772 interpolation checks) +
thresholds replayed.

## VERDICT V1 — the window is VACUOUS, killed by the row's own banked
consumption arithmetic acting as a q-FLOOR.

`B_quot_ub + B_tan_max + 16n^3 <= B* = floor(q/2^128)` (banked
verbatim) is a LOWER BOUND ON q (the left side is pure (n,k,A)
combinatorics; B* grows with q). At RowC 1/4 it forces q >=
2^229.7619 — **29.65 bits above the exposure ceiling L3 =
2^200.1130**. The exposed window lies entirely below the smallest
admissible field. Exact floors: RowC q_FLOOR = 2^128.(B_quot + 764 +
2^34) with B_quot dominated by one dyadic scale (C(128,95) etc.);
prize rows q_FLOOR = 2^255 EXACTLY (the 16n^3 = 2^127 term dominates
— independently reproducing the banked log2(29/16) = 0.9-bit pin
slack).

**The gates do NOT save P-B**: tangent holds from 2^167.0, genericity
from 2^83.3, cascade from 2^104.0 — so a BARE band of 33.11 bits
(~2^184 admissible primes) exists at RowC 1/4 where a uniformly
random pair is admissible AND super-budget by up to 2^132.46 x 8n^3
(certified: exact first+second moments, Var/mu = 1.0000 Poisson,
P[not a counterexample] <= 2^-19 at an explicit 193-bit prime). Every
row has a bare band (prize widths ~1e-8 bits, violations to 2^81.7).
**The tangent-gate floor is not the binding constraint anywhere; the
consumption gate is.**

**Consequences:** (H3) of (PB-SUPPLY) is DISCHARGED at all six rows
(implied by banked arithmetic; the F3 scope fork is NOT load-bearing
for it). The "RowC 1/16 FRAGILE 0.77 bits" flag RETIRES (that
compared against L1, not an admissibility condition; the real slack
is 110.07 bits — the tightest anywhere in the family). The
family-uniform closure is GRID-FREE: the admissible family decomposes
into (A, q-interval) cells (A derived from q by the banked candidate
rule; sup mu at each cell's left endpoint); NO admissible cell at any
row has random low-core supply above 8n^3.

**(V3) REFUTED exactly**: Var = mu (Poisson identities in the word
model — the joint probabilities are exact identities, different-slope
pairs exactly q^{-2h} via the bijection (u,v) -> (w_z, w_z')); by
Cauchy-Schwarz conditioning on admissibility moves E[N] by <= 2^-63
at the relevant scales; toy measurements (9 shapes, exhaustive gates,
conditioning ratios 0.995-1.19 across a 200:1 admissibility-pressure
range) confirm: concentration makes the count MORE certain, not
smaller.

**(V2) holds only OFF the admissible family and must be documented**:
with A pinned and only descriptor constraints, P-B is FALSE on the
bare bands with certified counterexamples (the smallest true
family-uniform constant would be 2^132.46 x 8n^3). A statement-level
obligation, not a target failure. **Recommended scope-cut wording**
(minimal): add to xr_lowcore_spread_heart the hypothesis "at any
prime field for which the row's consumption gate B_quot + B_tan +
16n^3 <= B* holds" — no new mathematics; the pins satisfy it with
20.24 (RowC) / 0.90 (prize) bits of B*-slack.

**Theorem to bank (V1)**: the consumption gate forces q >= q_FLOOR;
on every admissible cell sup C(n,A)q^{1-h} <= 2^-77.07 (>= 110 bits
below 8n^3); hence no random-supply counterexample exists at any
admissible field, and **every live slope at an admissible field is
PLANTED** — composing directly with the h4_hunt DESIGN CEILING
(<= 960 designable members; any counterexample >= 1 - 2^-23 forced).

**THE ONE ADJUDICATION LEFT (coordinator)**: the verdict rests on
reading the consumption gate as a CONDITION ON ADMISSIBLE q (B* =
floor(q/2^128) per e1_pair_feasible_prime_field_reduction:20-22)
rather than a check performed only at the pin. If ruled otherwise,
the verdict flips to V2 at RowC 1/4 (33-bit band, 2^132 violation).

**Caveats**: the counterexample certificate is probabilistic (exact
moments + union), no explicit pair constructed at RowC scale; PNT-in-
AP heuristic for the prize bands' prime counts (RowC verdicts
independent — explicit certified primes exhibited); T0/T3/T4
modelled per the bridge's definitions (gauge-invariant restatement
not re-derived); toys cannot reach the official regime (the known
FM3-caveat-4 gap); nothing proved about P-B's (H4) adversarial
content — only the random-supply component is closed.
