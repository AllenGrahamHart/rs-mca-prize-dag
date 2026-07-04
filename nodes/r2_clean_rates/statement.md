# r2_clean_rates

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

CURRENT FORM (the compiled target, superseding the X-1 emptiness framing — see the day's arc in notes): at each clean-rate decision candidate, for every pair (u,v), the post-strip residual slope count satisfies R_post(u,v; A) <= 16 n^3 (dihedral and extension columns INSIDE R_post). Sufficiency for the determination is PROVED exact integer arithmetic (the poly-forcing compiler: 16 n^3 <= s_lo at all six candidates, prize rows tight at 29 n^3). The supply side is the face-4 rung ladder under xr_clean_residual_any_gate. TOOL ASSIGNMENT stands: exclusion-type per-pair dichotomies here; the KLLM/globalness composition reserved for rate 1/2's E[X] >= 1 rows.

## Attack surface

the same conversion chain (strip -> tangent-cap globalness -> KLLM slice variant -> E_3 bridges -> pair ledger) evaluated at the clean-rate margins; the leak adjudication (10 candidates) still gates the hypothesis; hand the slack-composition arithmetic to the strongest available prover with #211's exponents and the wave-1 margins as given data

## Falsifier

the composition arithmetic failing even with 2^100 slack (would push the clean rates onto the SPI route, which inherits the F machinery)

## Ledger (migrated notes)

C-2 PIPELINE (#213, checker replayed green): corridor crossings located at all three clean rates with the ordering list_lo < quot < tau* < cap verified; per-row certificate skeletons emitted; minimum integrality margin ~8.0e11 bits. THE DETERMINED REGION: pinned-class rows are threshold-DECIDED for field sizes 128..168 bits (rate 1/4), 128..169 (1/8), 128..170 (1/16) by existing machinery; Row-C-class norm frontiers at even N' <= 100/120/112. Beyond ~170 bits the band/exclusion theory (xr_clean_residual_any_gate) gates. PRECISION (corrected 2026-07-03): the determined region covers the DEMONSTRATED ROW CLASSES (pinned-class, Row-C-class) at fields 2^128..~2^168-170; class-universality below 2^168 needs the pipeline sweep (mechanical, not yet run). The grand challenges at the clean rates are NOT resolved: fields 2^170..2^256 are gated by the per-pair exclusion (the band) — the honest claim is 'one named problem stands between the clean rates and full resolution', not 'basically resolved'. | STATEMENT ARC (one day): slack composition -> emptiness (X-1) -> integer budget (audit) -> compiled poly target (16 n^3). Each form superseded by computing the requirement more precisely. | The zero-residue form of the (A) closure makes the trade column rate-portable (see rate_half_coverage_gap note): when the clean-rate certificates land, running the rho = 1/2 rows through C2 is nearly free and should be done opportunistically — the 1/2 deferral then rests solely on the coverage band + margin point + B-side re-arithmetic. | PROMOTED red -> amber (Codex flip packet, my replay 8/8; flip_packets/r2_clean_rates.md): statement-level assembly over the wired kids.
