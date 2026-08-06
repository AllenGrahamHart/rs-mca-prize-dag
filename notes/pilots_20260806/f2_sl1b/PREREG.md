# PRE-REGISTRATION — SL-1b (mystery 2): the base-3 first-moment dimension threshold

Round 16, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation.

## 0. The target (verbatim, FABLE_AUDIT of f2_sl1_powersums)

> ... the named SL-1b (dim L >= m log_p 3 — the base-3 first-moment
> threshold, exactly log2 3 from LEMMA 3's) ...

SL-1b is one of mystery 2's three remaining obligations (with the t/q
pin — running as a SIBLING pilot this round, do not duplicate it — and
the |K1| seam, assigned to that sibling).

## 1. Source surfaces (read ALL first; quote verbatim)

- `notes/pilots_20260804/f2_sl1_powersums/PROOFS.md` — SL-1's full
  proof (the diagonal-times-Vandermonde mechanism applied locally to
  minors; weight >= ceil(t/2)+1 characteristic-free; the true law
  min(2R+1, max(p, R+1)) sharp in both branches; the Z(L) mass bounds;
  the discharge criterion t >= 1.2263m; SL-1b's exact statement and
  why it was named). QUOTE SL-1b's statement verbatim from this file
  before any work — if the statement there differs from the audit's
  one-line gloss above, the PROOFS.md form governs and the discrepancy
  is your first reported item.
- `notes/pilots_20260804/f2_sl1_powersums/FABLE_AUDIT.md` — the
  banked context: what SL-1 subsumes (THEOREM A), the DLI/WCL stronger
  sibling (w >= 2R+1 under char > w, with 6 counterexamples showing
  char > w is NECESSARY), and the cross-lane scope facts.
- `notes/pilots_20260804/f2_opening/PROOFS.md` — LEMMA 3 (the
  necessary condition SL-1b's constant is calibrated against) and the
  rung ladder.

## 2. Pre-registered claims

- **(B1)** PROVE or REFUTE SL-1b as stated in PROOFS.md. First test:
  does SL-1's own mechanism (diagonal-times-Vandermonde on minors)
  extend to the dimension statement, and if not, name the exact
  obstruction.
- **(B2)** Sharpness: if proved, exhibit the extremal family attaining
  (or approaching) dim L = m log_p 3; if the truth is a different
  constant c != log_p 3, prove the true law and state which side the
  discharge criterion moves.
- **(B3)** Small-field search for counterexamples BEFORE investing in
  proof: exhaustive L over small p and m at ramguard-tiny scale, with
  the search space and its boundaries pre-registered in your appended
  section. A counterexample ends the pilot with a REFUTED verdict and
  the witness.
- **(B4)** The consequence, stated exactly: what does SL-1b (proved or
  refuted or re-constanted) do to mystery 2's discharge chain at each
  rung — independent of the t-pin question, which the sibling pilot
  owns. If your result INTERACTS with the t-pin (e.g., the criterion
  t >= 1.2263m moves), flag the interaction for the coordinator; do
  not resolve it yourself.

## 3. Pre-registered falsifiers / honesty clauses

- A single counterexample in (B3) refutes SL-1b as stated; report the
  witness and stop proving.
- If SL-1b's statement in PROOFS.md is ambiguous (e.g., which L, which
  m), the ambiguity is a reported defect, not a licence to pick the
  provable reading. State both readings and address the one LEMMA 3's
  calibration needs.
- No silent strengthening: if you prove a weaker threshold that still
  serves the discharge criterion, label it SL-1b-WEAK and say exactly
  what gap remains.

## 4. Rules of engagement

- DRAFT ONLY: write only inside `notes/pilots_20260806/f2_sl1b/`.
  Never touch dag.json, node shards, tools/, or push.
- COMPUTE LAW: never bare python3; `tools/ramguard tiny -- python3 ...`
  (256M/60s) or `tools/ramguard local -- python3 ...` (1G/5min);
  literal `--`; run from repo root
  `/home/u2470931/smooth-read-solomin/prize`.
- Verbatim quotes for every statement you rely on (file:line).
- Do NOT write REPORT.md — return the full report as your final
  message; the coordinator persists it verbatim.
