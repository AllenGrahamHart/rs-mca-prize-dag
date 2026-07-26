# subfield_trace_paid_gate

- **status:** PROVED
- **closure:** proof
- **title:** Subfield/trace-flat paid gate (SHARED: dli + sov)
- **proof:** `proof.md` (Pro T1, all core claims verified); thread record in `PRO_T1.md`

*Transcription note (2026-07-26): this node predates the statement-artifact
convention and had no `statement.md`, which the DAG validator flagged. The
Statement / Attack surface / Falsifier sections below are the `dag.json` fields
**verbatim** — the DAG statement text is the spec, so this file is a faithful
transcription with no paraphrase. Nothing here is new content; the mathematics
lives in `proof.md` and `PRO_T1.md`.*

## Statement

Over extension rows `F_q=F_{p^k}` (`k>=2`), the TRACE-FLAT/subfield-degenerate
locus is a PAID class OR reduces to the base `F_p` by Weil restriction:
(frequency form, dli) `lambda` with `Tr_{F_q/F_p}(lambda*phi(x)) == 0` on a
positive-density section-image; (cell form, sov) cells where `x->Tr(ax)` is
constant on a positive-density free-root set. VERIFIED these are non-negligible:
`F_{p^2}` trace-zero `lambda` gives `S=Omega(L_j)` (P2); `F_{17^32}` canonical
trace char is flat on 496/512 grid points, cell density 0.506 at `h=21` (P3).
Prime rows (`k=1`): VACUOUS (`Tr=id`, no proper subfield). SUPPORTED by the proved
interleaved/Weil-restriction machinery that closed f1 (base reduction).

## Attack surface

Weil-restrict extension rows to base `F_p` (proved f1/interleaved machinery); or
price the trace-flat/subfield-norm class in the paid ledger.

## Falsifier

An extension row whose trace-flat/subfield-degenerate locus is neither paid nor
base-reducible.

## Resolution (as recorded in `dag.json` notes)

PROVED (Pro T1, all core claims verified): exact Weil descent + trace-flat
classification `|Ann(A)|=p^{e-dimW}` + SOV Euler product; both counterexamples
absorbed as paid trace-kernel collapses. TRACE_FLAT ledger column installed;
affordability (`2^122.5 << |F|=2^131`) routed to the `mca_safe` budget audit.
SHARED SPINE CLOSED — dli & sov now need only their residual.
