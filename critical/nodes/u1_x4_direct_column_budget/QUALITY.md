# QUALITY CERTIFICATE (red-quality program, charter r2, 2026-07-10)

## Red: u1_x4_direct_column_budget

STATUS: PRE-DECOMPOSITION (the one red that cannot yet carry a full
certificate — honestly documented per the charter). The 2026-07-10
coverage audit (KB #22) returned NOT-READY: the direct column's h-band is
itself unpinned (catch #38: prose h <= 8 vs refs (log2 n)^2), so "the
minimal predicate for the upstream amber" is UNDEFINED — the band pin IS
the minimality/sufficiency question. The band derivation is IN FLIGHT
(launched 2026-07-10, this program).

Q-SUFF (partial): consumer sufficiency of the floor FORM is proved (16n^3,
QA.22/QA.26; budget probe PASS at 1.5% with positive control); what is
missing is the h-coverage definition, not the budget arithmetic.

Q-SURV (interim): the floor campaign hardened the floor; the coverage
audit itself was a falsification-grade stress (23 verifier replays, weld
recount 5/5, the h=5 revoking witness independently replayed — catches
#36/#37 found and banked). h=2 proved; h=3 chain amber-grade with all
constants re-derived. QUEUED: after the band pin — per-h budget probes
under the F-3 ledger (h=3 alone = 50.002% of n^3 at s=13).

BAND RESOLUTION (2026-07-10, derivation audit): OUTER PIN PROVED —
the obligation is 2 <= h <= min(A(row), floor(n/2)), A = k+t
(star_pte_support_bound + star-PTE injectivity; h_window_derivation had
already adjudicated H_max := A). All three circulating candidates (8,
7..20, (log2 n)^2) STRUCK as non-inherited artifacts. INTERIOR OPEN —
named lemma minted: f3_active_core_width_cap (ev-wired); absent it the
uniform-in-h gate shape is FORCED (exact ledger: h=3 alone = 50.0002% of
n^3; one ACT(4096)-grade stratum fits; ~2^40 strata at prize rows).

CERTIFICATE STATUS: COMPLETE per charter — the node is honestly
documented pre-decomposition WITH its obligation band now well-defined
(proved outer pin + named interior lemma + exact budget ledger). The
minimality question has its answer: the minimal decomposition is
{conic gate, rankcap gate, uniform-h band gate covering (3, H_max]} —
poseable only after f3_active_core_width_cap or a general-h ACT compiler.
Executed stress record: the coverage audit (23 verifier replays, witness
replay, catches #36-#39) + this derivation (all figures exact,
notes/band_hband_arithmetic_20260710.py).
