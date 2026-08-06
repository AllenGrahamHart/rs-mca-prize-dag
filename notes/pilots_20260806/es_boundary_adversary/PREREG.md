# PRE-REGISTRATION — (ES) boundary adversary: hunt the accident below balance

Round 16, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. Role: the ADVERSARIAL lens on
(ES) — the sibling pilot (es_axkatz_transfer) tries to prove a
transfer; this pilot tries to BREAK the conjecture at the boundary.
Neither reads the other's drafts.

## 0. The conjecture under attack (sources of record)

(ES) ENTROPIC SUPPRESSION, the unified terminal of FOUR lanes (band
fullrank, crossing, syzygy via BC routing, u2c/dli RES): sub-balance
codimension implies only periodic divisors on the prescribed windows —
concretely at the crossing instance, the 0/1 codewords of weight r' in
the [2^41, 2^41-w+1, w] RS/cyclic codes are the periodic ones only.

Banked empirics to beat (verbatim, FABLE_AUDIT of mun_anticoncentration):

> ... suppression measured 1-2 orders EARLY (for (ES)); above-balance
> accident witness pins the boundary.

## 1. Source surfaces (read ALL first; quote verbatim)

- `notes/pilots_20260804/mun_anticoncentration/PREREG.md` section 0 —
  the objects of record (crossing + band instances, the
  characteristic arithmetic delta in {1,2,4}).
- `notes/pilots_20260804/mun_anticoncentration/FABLE_AUDIT.md` — the
  four proved structural constraints on any accidental solution, the
  suppression measurements, and the above-balance witness. The
  constraints are your search-space pruners; the witness is your
  starting template.
- The five verifiers in that dir — the banked exact-count machinery;
  extend, do not rewrite.

## 2. Pre-registered claims

- **(C1)** THE HUNT: a systematic search for an ACCIDENTAL
  (non-periodic) 0/1 codeword strictly BELOW the balance boundary, at
  scaled-down parameter families chosen to respect the row arithmetic
  (delta in {1,2,4}; n | p^delta - 1; the same window shape). Search
  strategies to include at least: (a) deforming the above-balance
  witness downward parameter-by-parameter; (b) structure-guided
  construction through the four constraints (treat each as an
  equality-case analysis: what attains it?); (c) random + algebraic
  hybrid search at the largest ramguard-local-feasible rows. REGISTER
  the parameter grid and search budget in your appended section
  BEFORE running.
- **(C2)** THE CURVE: extend the suppression measurement toward the
  boundary from below — quantify "1-2 orders EARLY" as a fitted decay
  law with the boundary location as a fitted parameter, and state
  whether the fit predicts zero accidents at prize rows with margin.
- **(C3)** THE BOUNDARY: sharpen the above-balance witness — the
  MINIMAL above-balance accident over the searched families (is the
  known witness extremal?), and the exact codimension at which
  accidents switch on.
- **(C4)** Constraint feedback: any structural regularity of the
  near-boundary accidents (support structure, orbit structure under
  the p-Frobenius, divisor pattern) stated as candidate lemma(s) for
  the transfer pilot and mint-4.

## 3. Pre-registered falsifiers / honesty clauses

- A single sub-balance accident REFUTES (ES) as posed — that is a
  campaign-critical catch, not a failure: report the witness with a
  self-contained ramguard-tiny reproduction script and STOP the hunt.
  The four lanes then need the coordinator's re-pose, not yours.
- If the search space at feasible scale cannot reach the sub-balance
  regime for ANY admissible family (scope gap), report the gap
  exactly — a null result from an unreachable regime is NOT evidence
  for (ES) and must not be phrased as such.
- Fitted-curve extrapolation is EVIDENCE, never proof; label it.

## 4. Rules of engagement

- DRAFT ONLY: write only inside
  `notes/pilots_20260806/es_boundary_adversary/`. Never touch
  dag.json, node shards, tools/, or push.
- COMPUTE LAW: never bare python3; `tools/ramguard tiny -- python3 ...`
  (256M/60s) or `tools/ramguard local -- python3 ...` (1G/5min);
  literal `--`; run from repo root
  `/home/u2470931/smooth-read-solomin/prize`.
- Verbatim quotes for every statement you rely on (file:line).
- Do NOT write REPORT.md — return the full report as your final
  message; the coordinator persists it verbatim.
