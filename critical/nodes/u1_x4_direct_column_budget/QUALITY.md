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

NEXT: band pin lands -> either predicates {conic gate, rankcap gate,
f3_hband_act_gate} become poseable (then the standard certificate) or
BAND-OPEN is documented as the named lemma.
