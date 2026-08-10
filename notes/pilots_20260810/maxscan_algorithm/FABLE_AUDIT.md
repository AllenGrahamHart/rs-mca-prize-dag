# FABLE_AUDIT — maxscan_algorithm (round 28)

Coordinator: Fable. Date: 2026-08-10. Pilot: Opus (task adc1a5646e15df795,
~44 min, 65 tool uses). Quarantine marker: ledger line 4302, observed
(one incidental ps-listing filename exposure disclosed, not read).

## Verdict

**BANKED. The BBM pattern struck twice: a computation priced
"Modal-class, out of stdlib reach" fell to two algorithmic ideas
(signal separation collapsing the field size; the antipodal identity
collapsing the subset space) in 4 minutes and 130 MB — and a theorem
proved mid-run (the PARITY THEOREM) then reached n=64, a scale nobody
had costed. The verdict on RH-AC's supply side: the delta=1 flank
maximum COLLAPSES at four scales, monotonically and accelerating,
~12 bits short of the razor need. The round-27 conflict is resolved
on this branch; the maximal-slack curve is the named residual, with
the parity recursion as the route to it. No compute was rented, and
the Modal request that remains is optional, <$5, and gates only the
argmax-by-exhaustion upgrade.**

## Replays (mine)

| what | result |
|---|---|
| ms_exact.py at n=8,16,32 (the char-0 verdict ladder) | **IDENTICAL** to banked: 6 / 46 / 1974 with per-stratum decompositions (630+1344 at n=32), closed-form column matching, ratios exact |
| ms_exact.py at n=64 | replayed in background; see the confirmation line appended below |
| the closed form STRAT_1 = (M+2)C(M/2-1, M/4-1) | arithmetic verified inside the identical replays (6/30/630/218790) |

Not replayed: the mod-q two-field runs (1988 at both fields — the
pilot's own two-field discipline plus the three-way char-0
confirmation, one leg of which IS my identical replay, covers the
verdict); the n=16 fullscan histogram reproduction (banked
byte-match by a different algorithm — internal cross-validation).

## Audit judgements

- **The parity theorem is the report's lasting contribution** — a
  clean Q-basis factorization argument in Z[omega] with an exact
  structural corollary (strata <= n/4), verified at four scales
  including two where it predicted exact zeros that measurement
  confirmed. Mint candidate alongside the closed form. The recursion
  note (E on a parity class is an e2 one level down) is the named
  route to both n=128 and the maximal-slack residual.
- **The pricing discipline worked as designed**: four routes priced
  before building, two rejected on the disjointness of their balance
  and signal windows — the kind of analysis that prevents renting
  compute to run the wrong algorithm.
- **The honest-residual ledger is exactly right**: the delta=1
  verdict is claimed; the maximal-slack curve is NOT claimed decided
  (the round-27 growing curve was that one); alpha=0-argmax at n=64
  is labelled assumed. No over-claim anywhere.
- **The self-caught compute-law near-violation** (an unguarded
  pipeline stopped via TaskStop before yielding output, re-run
  compliantly) is the correct handling; no number in the report
  came from an unguarded interpreter.
- **Misses first, and informative**: the background model was
  over-dispersed relative to Poisson (the separation argument was
  re-founded on measured numbers, not the model); the
  reachable-point registration was too pessimistic about the
  object that mattered.

## Corrections applied

- critical/nodes/rate_half_band_crossing_location/statement.md —
  round-28 maxscan addendum: the wall-break, the four-scale collapse
  verdict, the parity theorem + closed form, the two-field record,
  and the three honest residuals (maximal-slack undetermined;
  n=64 argmax assumed; the optional <$5 exhaustion). The "one
  undetermined number" line in Known Structure is superseded by
  this addendum. No status flip.
- MODAL_REQUEST.md noted as OPTIONAL and held (not filed): it does
  not gate the collapse verdict; filing decision deferred to the
  round bank summary.

## Follow-ups filed (not executed)

- Mint queue: the PARITY THEOREM + the STRAT_1 closed form.
- The parity recursion (route to n=128 and to the maximal-slack
  residual) — a natural round-29 brief if the supply side needs
  further closure after the endpoint pilots land.
- The optional Modal exhaustion (<$5) — file only if the argmax
  claim ever becomes load-bearing for a proof.

## n=64 replay confirmation (appended post-notification)

ms_exact.py at n=64: **IDENTICAL** to banked E_exact_64.json —
ANTIPODAL_exact = 1,946,902, per-stratum {1: 218790, 3: 1529088,
5: 199024}, ratio 0.0065. The full four-scale verdict ladder is
coordinator-replayed end to end.
