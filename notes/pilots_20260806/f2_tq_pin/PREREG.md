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

---

# APPENDIX — PILOT'S OWN PRE-REGISTRATIONS (Opus 5, appended 2026-08-06
# BEFORE any computation; nothing below was run at the time of writing)

Read-only source sweep completed first (no arithmetic). The following
claims are registered with falsifiers; each is tested in `verify.py`.

## (Q1) THE ADMISSIBILITY TEST — the load-bearing new claim

**Claim.** The 16-rung KoalaBear tower is **not a prize-admissible row**.
Concretely, with `p = 2^31 - 2^24 + 1` and `q_j = p^{2^j}`:
`log2 q_j = 2^j * log2 p` exceeds the rules cap `|F| < 2^256`
(`critical/nodes/rules_freeze/statement.md:9`) for every `j >= 4`, and at
`j = 16` exceeds it by a factor `> 7000x IN BITS`.

**Falsifier.** If `q_j < 2^256` for `j` up to 16, this collapses and the
whole (P1)-(P5) chain below must be withdrawn.

## (Q2) THE DIVISOR-OF-RECORD CLAIM

**Claim.** The banked window-bits product `t * log2 q ~ 2.15e12`
(`archive/compressed_dli_lane_20260705/b2_modp_giant_extras/statement.md:9`)
must be divided by `L = log2 q`, not by `log2 p`, and the rules force
`L > log2 n` because the smooth domain is a multiplicative subgroup of
`F^*` of size `n`, hence `n | q - 1`, hence `q > n`. Therefore at the
maximal rate-1/2 row (`n = 2^41`)

```
    2^41 / 256  <  t  <=  2^41 / 41 ,     i.e.   8.59e9 < t <= 5.37e10 ,
```

and `t = 7e10` lies OUTSIDE this interval for every admissible field.

**Falsifier F-Q2a.** If the rules do not force `n | q - 1` (i.e. the smooth
domain need not be a subgroup of `F_q^*`), the lower bound `L > log2 n`
dies and `t = 7e10` is readmitted.
**Falsifier F-Q2b.** If a base-field reading is nonetheless defensible,
the same bound must be run with `log2 p`; I pre-register that I will
report BOTH and will NOT suppress the base-field column.

## (Q3) THE CHARACTERISTIC BOUND

**Claim.** At any prize-admissible rate-1/2 maximal row (`n = 2^41`,
`q < 2^256`, `n | q-1`), writing `q = p^e` and `s = v_2(e)`:
`s <= 2`, `e <= 6`, and `log2 p >= 39`. In particular the KoalaBear
`log2 p ~ 31` base field is inadmissible, and the tower depth
`log2 ord_n(p) <= 2` — at most TWO rungs exist, not sixteen.

**Falsifier.** An explicit admissible `(p, e)` with `log2 p < 39` or
`v_2(e) >= 3` satisfying `2^41 | p^e - 1` and `p^e < 2^256`.
Registered as an exhaustive search over `s = 0..8`, `u` odd.

## (Q4) THE m_16 PREDICTION (made before computing)

**Claim.** The `2^38`-vs-`2^39` split is exactly the nested-vs-new-part
window ambiguity of `f2_deployed_windows/REPORT.md:69`:
new-part `m_j = (n_j - n_{j-1})/2 = 2^{22+j}` (so `m_16 = 2^38`) versus
nested `m_j = n_j/2 = 2^{23+j}` (so `m_16 = 2^39`). Both are correct
counts of different windows; neither is an arithmetic error.

**Falsifier.** If `2^39` is not `n_16/2` under the banked ladder, or if
some third window count is what `PREREG.json:58` meant.

## (Q5) THE SLIVER PREDICTION

**Claim.** The `[255.9113, 256)` sliver of
`notes/kernel_basis/TARGET_3C_EXTRACTION.md:29-30` is exactly
`{L : t*(L) <= 2^33}` at `n = 2^41`, rate 1/2, under formula (T*) of
`background/nodes/xr_radius_arithmetic/proof.md:41-43`.

**Falsifier.** A computed left endpoint differing from 255.9113 by more
than 0.001 bits.

## (Q6) THE RECOMPUTE PROTOCOL (fixed before seeing results)

LEMMA 3's official-row reading `t >= m_j / log2 p`
(`notes/pilots_20260804/f2_opening/PROOFS.md:232-233`) and LEMMA 2's
`Lambda ⊇ {1,3,...,2m-1}` cutoff `t >= 2 m_j - 1`
(`:327-328`) are recomputed at EVERY rung `j = 1..16` under the full
cross product {new-part, nested} x {every t on the pinned interval and
every literal in circulation}. The band is reported as the intersection
over the admissible t-interval, i.e. the WORST case, never the best.

## (Q7) HONESTY CLAUSES (binding)

- If the derived `t` is an INTERVAL rather than a value, that is the
  finding; I will not collapse it to a point to force a verdict.
- If the band is shorter than rungs 1-10 I report it unsoftened.
- If PP5.0 / `|K1|` cannot be frozen from rules-level sources, I say so
  and state exactly which choice remains open, rather than adopting the
  convenient normalisation.
- Any claim of mine that turns on the KoalaBear prime being the official
  row is to be read as CONDITIONAL and labelled as such, since (Q1)/(Q3)
  predict it is not admissible.
