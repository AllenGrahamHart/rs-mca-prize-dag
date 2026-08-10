# FABLE_AUDIT — k_extremal (round 29)

Coordinator: Fable. Date: 2026-08-10. Pilot: Opus (task ae70406e7acfa145e,
~14 min, 71 tool uses, 3 interpreter invocations — a reading audit).
Quarantine marker: ledger line 4474, observed.

## Verdict

**BANKED. HOLE — the largest quantifier catch of the campaign: the
grand-challenge rate-half family is 41 row sizes (n = 2^s,
k = 2^(s-1), s = 1..41 per the PROVED descriptor node — k <= 2^40 is
a CAP, not a pin), and the entire rate-half crossing/floor lane is
posed at s = 41 alone. No extremality theorem, no reduction, no
monotonicity, no admissibility exclusion — verified by my own reads
of the descriptor text and the pilot's grep-gated sweep. The
uncovered set is mapped exactly (s = 8..40 fully; s = 1..7 above
per-s thresholds via the pilot's own elementary POSE 1, corridor
shutting permanently at s = 8); the blast radius is narrow (four
crossing/floor nodes + two absolute-width constants) but narrow for
the bad reason that small rows are simply unaddressed. A second
catch (FLAG E: two mutually exclusive maximal-row conventions,
agreeing only at rate 1/2) and one honest unresolved (the ABF26
"sufficiently large |F|" proviso, not vendored in-tree) ride along.**

## Coordinator verifications (mine)

| what | result |
|---|---|
| descriptor/proof.md:3-8 | verbatim — s free in the admissible tuple; k <= 2^40 is a check |
| the F_17^32 fixture | q = 17^32: 131 bits < 256, 512 divides q-1, v_2(q-1) = 9 — a fully admissible s = 9 rate-half row, used in-repo as the regression fixture |
| the bracket vacuity | [k+2^34, 1.5k] empty iff k < 2^35 — exact |
| Convention B quote | cp_statement.md:33-35 verbatim ("n = 2^41..2^44, k = 2^40") — FLAG E's collision is real |
| the band_closure node.json/statement.md quantifier disagreement | confirmed (the shard says "every admissible rate-1/2 row"; statement.md:66 pins) — resolved by FLAG B's both-texts reading note |

## Corrections applied (the flags — E7 pattern, flag-not-resolve)

1. **FLAG A** — mca_grand's shard statement: the row-size scope seam,
   with the descriptor family stated, the uncovered set named, and
   the owner pointer (the reduction poses + the ABF26 question).
2. **FLAG B** — rate_half_band_closure, BOTH texts (statement.md
   section + shard statement): posed AT n=2^41, k=2^40 ONLY; the
   "every admissible rate-1/2 row" phrase read as row-pinned; the
   band arithmetic carries no information at s < 41.
3. **FLAG C** — rate_half_list_adjacent_crossing via the full
   three-write sectioned discipline (addendum file 16 + the index
   bullet in statement.md AND the registry index string + the
   registry addenda tuple + document.json regenerated): the
   claim/machinery quantifier seam, with the vacuity thresholds.
4. **FLAG D** — BAND_LANE_DEFINITIONS.md item 13: "official row" is
   ambiguous and banned bare; admissible-vs-maximal vocabulary
   fixed; the dli_wcl_* parenthetical read as an s = 41 pin.
5. **FLAG E** recorded in item 13 + the ledger as ADJUDICATION
   PENDING (the two conventions decide which rows the clean-rate
   lane is about — a coordinator/user adjudication, not applied).

Verify chain fully green after the flags (one mechanical lesson
banked: a sectioned-registry addendum needs document.json
regenerated; the --write repacket path refuses on legitimately-grown
sources, so the per-node manifest regeneration is the right tool).

## Audit judgements

- **This is the round-28 lesson executed at range**: the pilot
  traced mca_grand to the DAG root, read the rescue candidates one
  level up (the ww router/envelope/descriptor), and they CONFIRMED
  the hole rather than closing it — citation, not inference.
- **The E7 idiom held throughout**: five flags drafted as exact
  edits, three poses posed-not-proved with falsifiers, POSE 2
  argued AGAINST by its own author (the absolute-width floors
  cannot be the image of a monotone transport — the sharpest reason
  on the table).
- **The honest unresolved is the pivot**: if ABF26's "sufficiently
  large |F|" proviso excludes small rows, HOLE flips to PINNED and
  bands I-III retire. That is a rules-citation question the repo
  cannot answer (the PDF is not vendored) — a candidate Przemek
  question, surfaced to the user.
- **Blast-radius honesty**: the k-uniform table (descriptor, the
  interleaved census, census_bounded_scales WITH its silently-
  flooring caveat caught by the pilot, staircase, petal_g1) vs the
  four k-specific nodes — and the one softener (the 719 constant
  bends conservatively, verified).
- **Compliance clean**: blind priors before any read beyond the two
  anchors; quarantine total; 3/3 ramguard.

## Follow-ups filed (not executed)

- USER DECISIONS surfaced: (1) POSE 3 — the per-s four-band family
  re-pose of the rate-half lane (the recommended shape); (2) the
  ABF26 proviso as a Przemek/rules-citation question (outward);
  (3) FLAG E adjudication (Convention A vs B for the maximal rows).
- POSE 1 (the elementary list-side triviality corridor) is a cheap
  mint candidate once refereed — it retires band I above its
  thresholds.
- The MCA analogue of POSE 1 is a separate unposed obligation
  (B_mca is a slope count; the binomial argument does not
  transfer — the pilot's own scoping correction).
