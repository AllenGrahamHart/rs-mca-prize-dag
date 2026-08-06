# PRE-REGISTRATION — F2-ADM: re-derive mystery 2 on a prize-admissible row

Round 17, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. This is the named successor
task from round-16's f2_tq_pin (its honest residual 5: "I did not
re-derive the F2 tower on an admissible row... this is the natural
successor task").

## 0. The scope correction being executed (sources of record)

Round-16 f2_tq_pin CATCH-1 (banked, maintainer-level): the 16-rung
KoalaBear tower is NOT prize-admissible — the field cap |F| < 2^256 is
broken from rung 4; the complete admissible region at the maximal
rate-1/2 row (n = 2^41) is

> `v_2(e) <= 2`, `e <= 6`, `log2 p >= 39`, tower depth <= 2 rungs

with the explicit admissible prize-max witness
`p = 18446735827372343297` (v_2(p-1) = 39), `q = p^4`,
`log2 q = 255.99997`, `v_2(q-1) = 41`, `ord_{2^41}(p) = 4`.
Also banked: t pinned to the interval `(2^33, 5.364e10]` (t = n/L);
the F2 discharge headline WITHDRAWN to rungs 1-10 (1-9 stricter) ON
THE TOWER-AS-WRITTEN; round-16 f2_sl1b CATCH-B: f2_opening's stated
setting (n | p^2-1) is rung-1-only even on that tower.

## 1. Source surfaces (read ALL first; quote verbatim)

- `notes/pilots_20260806/f2_tq_pin/REPORT.md` + `PROOFS.md` — the
  admissible region derivation, the explicit row, the t interval,
  CATCH-2 (the L = 255.9 vs 255.911275 seam), CATCH-3 (stricter
  window), the |K1|/PP5.0 pricing.
- `notes/pilots_20260804/f2_opening/PROOFS.md` — the (O1) obligation,
  LEMMA 3, the rung ladder and window mechanism, THEOREM A/B.
- `notes/pilots_20260804/f2_sl1_powersums/PROOFS.md` — SL-1
  (characteristic-free), the Z(L) terminal (SL-1b').
- `notes/pilots_20260806/f2_sl1b/PROOFS.md` — LEMMA SL-1b-DIM
  (k-free), the (R-A)/(R-B) split, the 61-witness refutation.
- `notes/pilots_20260806/f2_tq_pin/REPORT.md` HONEST RESIDUALS —
  the t-naming collision is the SIBLING pilot's (t_naming); flag
  interactions, do not resolve.

## 2. Pre-registered deliverables

- **(D1) The admissible F2 object.** On an admissible row (use the
  explicit witness as the concrete instance, and state which parts
  hold for ALL admissible rows vs the instance), reconstruct the F2
  mechanism: what replaces the 16-rung tower when at most 2 rungs
  exist (ord_{2^41}(p) <= 4)? State the new rung/window ladder
  (m_j, n_j, q_j) exactly, under BOTH the new-part and nested window
  readings (the stricter governs headline margins per CATCH-3).
- **(D2) Theorem survival table.** For each banked F2-lane theorem —
  THEOREM A/B, LEMMA 3, SL-1, LEMMA SL-1b-DIM, the Z(L) reduction,
  the antipodal-fibre/parity results f2_opening relies on — state:
  survives VERBATIM (k-free / characteristic-free), survives WITH
  RESTATED CONSTANTS (give them), or NEEDS RE-DERIVATION (name the
  gap). No theorem may be carried over silently.
- **(D3) The margins on the admissible row.** Recompute the LEMMA 3
  necessary condition and the discharge margins at every rung of the
  ADMISSIBLE ladder, over the full pinned t-interval (2^33,
  5.364e10], both window readings, worst case first. State plainly:
  what is (O1)'s discharge status on admissible rows?
- **(D4) The re-based obligation list.** Mystery 2's obligations
  restated for the admissible object: does SL-1b' (the Z(L) bound)
  survive as THE terminal, and at which (m, p) does it now sit? Does
  the 2-rung structure make anything EASIER (e.g. fewer rungs = fewer
  obligations) or HARDER (e.g. the descent argument needed 16 steps)?
  This is the deliverable the board update will be written from.
- **(D5) The PP5.0 seam on the admissible row.** Recompute the
  |K1| pricing (avg-vs-sum = 2^{n/2} was proved via (t*/2)L = n/2 —
  does the identity survive when t is an interval and L is the
  admissible row's?). Do not choose the reading (user decision,
  pending); price both.

## 3. Pre-registered falsifiers / honesty clauses

- If the F2 mechanism CANNOT be reconstructed on a <= 2-rung tower
  (i.e. the descent genuinely needed the inadmissible depth), that is
  the finding: mystery 2's F2 lane would be VACUOUS as posed (its
  object excluded by the rules) — state what the lane's question
  becomes, do not force a reconstruction.
- If any banked theorem's survival is ambiguous, it goes in NEEDS
  RE-DERIVATION, never in survives-verbatim.
- All margins worst-case over the t-interval; no point-value t.

## 4. Rules of engagement

- DRAFT ONLY: write only inside `notes/pilots_20260806/f2_adm/`.
  Never touch dag.json, node shards, tools/, or push. Do NOT read
  `notes/pilots_20260806/t_naming/` (sibling this round).
- COMPUTE LAW: never bare python3; `tools/ramguard tiny -- python3 ...`
  (256M/60s) or `tools/ramguard local -- python3 ...` (1G/5min);
  literal `--`; run from repo root
  `/home/u2470931/smooth-read-solomin/prize`.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — return the full report as your final
  message; the coordinator persists it verbatim.
