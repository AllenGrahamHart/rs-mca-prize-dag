# PRE-REGISTRATION — the t/q pin (mystery 2, DEDICATED): derive q = p^k and t from the rules freeze

Round 16, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. This is a DERIVATION task,
not a compute task — ramguard-tiny arithmetic checks only.

## 0. The catch being resolved (verbatim, FABLE_AUDIT of f2_sl1_powersums)

> **THE t CATCH (maintainer-level, SURFACED):** t has NO definition
> in the repo (a bare literal 7e10); the competing exact
> t* = 8,592,912,739 FLIPS LEMMA 3 at rung 16 from a 7.89x margin to
> a 0.9687x VIOLATION — a sign flip of a proved necessary condition
> for (O1) — and shortens the surjectivity band to rungs 1-10. Plus
> the m_16 = 2^38-vs-2^39 internal contradiction. RESOLUTION
> REQUIRED before mystery 2's "discharged at rungs 1-13" headline
> can stand: pin q = p^k and t from the rules freeze (a derivation
> task, not compute).

## 1. Source surfaces (read ALL before deriving; quote verbatim)

- `notes/pilots_20260802/f2_deployed_windows/REPORT.md:17` — the tower
  citations of record: official prime KoalaBear-shaped, p-1 = 2^24·127,
  e = v_2(p-1) = 24; n a 2-power ~2^40, ambient N = 2^41; rung j:
  n_j = 2^{24+j}, q_j = p^{2^j}, j = 1..16; ord_{2^40}(p) = 2^16
  exactly; "t ~ 7e10 conditions".
- `notes/pilots_20260802/f2_deployed_windows/selection.py:43` —
  `T_CONDITIONS = 70_000_000_000  # t ~ 7e10 (F2_NEWTON_EMPTY_EXTREMES)`
  — the bare literal.
- `notes/CONSOLIDATION_REPORT.md:19` — xr_radius_arithmetic: corridor
  edge t* solved from FM scale + gate at L = log2 q = 255.9;
  t* = 8592912739 / 7014660390 / 4722556392 / 2943177800 by rate;
  proved s* = t*-1 given the pinned ledger c(s,t) (open slot
  xr_ledger_qpower).
- `notes/kernel_basis/TARGET_3C_EXTRACTION.md:26` — the base-field vs
  extension reading of "t ~ 7e10" (log2 p ~ 31).
- `notes/pilots_20260804/f2_opening/PROOFS.md:234,:328` — LEMMA 3's
  7.89x margin at rung 16 under t ~ 7e10; the m_j = 2^{22+j} ladder
  and the rungs-1..13 band; rungs 14-16 status.
- `notes/pilots_20260804/f2_sl1_powersums/PROOFS.md` — the rung-16
  flip arithmetic under t*; the m_16 = 2^38-vs-2^39 contradiction.
- The rules freeze itself: grep the repo for the prize-spec /
  rules-freeze surfaces (F2_CAMPAIGN_LOG.md entries cited above;
  PRIZE spec files; anything defining the official row's q, p, n, and
  the condition count). The pin must trace to a RULES-LEVEL source,
  not to a downstream pilot's convenience constant.

## 2. Pre-registered deliverables

- **(P1)** A provenance chain for q: the official q = p^k with p and k
  pinned to a rules-level citation (file:line), and the resulting
  L = log2 q stated exactly (the 255.900-256 window vs the 255.9 gate
  used by xr_radius_arithmetic — reconcile or flag).
- **(P2)** A DERIVATION of t (the number of conditions) from the
  pinned q, n, and the F2 window mechanism — not an adoption of either
  literal. State exactly what t counts, at which rung, in which field
  reading (base vs extension), with the formula.
- **(P3)** The adjudication: t ~ 7e10 vs t* = 8,592,912,739 — which
  (if either) equals the derived value; where the wrong one came from.
- **(P4)** The m_16 contradiction resolved: m_j ladder restated with
  the pinned values; is m_16 = 2^38 or 2^39, and why.
- **(P5)** LEMMA 3's margin recomputed at EVERY rung 1..16 under the
  pinned (q, t): the resulting surjectivity band stated plainly.
  Recompute with `tools/ramguard tiny -- python3 ...` from repo root.
- **(P6, secondary)** The |K1| normalisation seam: settle WITH the
  PP5.0 freeze (sources: `notes/pilots_20260804/f2_opening/FABLE_AUDIT.md:16,:31`,
  `notes/pilots_20260804/f2_opening/PROOFS.md:257,:339-343` CATCH-3).
  If PP5.0 cannot be frozen from rules-level sources alone, say so and
  state exactly what choice remains open.

## 3. Pre-registered falsifiers / honesty clauses

- If the derived t matches NEITHER literal, report the third value and
  recompute (P5) under it; do not force a match.
- If the rules freeze genuinely does not pin t (i.e., t is a modelling
  choice, not a rules constant), that is itself the finding: state the
  minimal set of choices, and which choice each published margin
  assumed. The discharge caveat then becomes PERMANENT until a
  maintainer-level pin — say so explicitly.
- If the band under the pinned values is SHORTER than rungs 1-10,
  report it without softening.

## 4. Rules of engagement

- DRAFT ONLY: write only inside `notes/pilots_20260806/f2_tq_pin/`.
  Never touch dag.json, node shards, tools/, or push.
- COMPUTE LAW: never bare python3; `tools/ramguard tiny -- python3 ...`
  (256M/60s) or `tools/ramguard local -- python3 ...` (1G/5min);
  literal `--`; run from repo root
  `/home/u2470931/smooth-read-solomin/prize`.
- Verbatim quotes for every statement you rely on (file:line).
- Do NOT write REPORT.md — return the full report as your final
  message; the coordinator persists it verbatim.
