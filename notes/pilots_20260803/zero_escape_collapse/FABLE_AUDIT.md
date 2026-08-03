# Coordinator audit — zero-escape collapse pilot

**Auditor:** Fable, 2026-08-03. **Verdict: BANKED — REFUTATION accepted;
this is the round's most consequential result.**

## Replay

`tools/ramguard tiny -- python3 notes/pilots_20260803/zero_escape_collapse/verify.py`
-> 26 checks, 0 FAIL, `ZERO_ESCAPE_COLLAPSE_ALL_PASS` (coordinator
replay). PREREG.md read and confirmed: the counterexample X1 — its
construction AND its exact rank `2m-1 = 9` — was predicted from the
duality theory and pre-registered with falsifiers P1-P7 BEFORE any
computation. All seven falsifiers came out as pre-registered. Textbook
falsification discipline.

## Hand-verification (line-audited)

- **Theorem 1 (duality)**: the shortened-dual identity
  `C_{S_a}|_{S_a} = (RS_k|_{S_a})^perp` and the quotient by
  `(RS_k|_U)^2` are exact; `rank = 2m - dim Ann` follows. Correct.
- **X1 fixture arithmetic** (hand-recomputed): fibres of `x^2` over
  `F_17` at `c = 1,2,4,8` are `{1,16},{6,11},{2,15},{5,12}`; `|U|=8`,
  `m=5`; pairwise `|I_ab| = 4 = k+1`; triples `= 2 = k-1` (gate (T)
  HOLDS); every point in exactly 3 supports (zero escape). The
  annihilator members `X^2-8, X^2-4, X^2-1, X^2-2` vanish on the right
  fibres. Correct.
- **Theorem 3**: normalising two rays to zero and killing each `p_j` on
  `>= k` points of `I_ab` is exact; the `(T)`-failure boundary ("fires
  iff some triple has `>= k` points") is honest and is the sting.
- **Proposition 6 arithmetic**: `t_0+2t >= k+1` and `t_0+t <= k-1`
  give `t >= 2`; both branches of
  `rank >= 2m - (k-t_0-t)^+ >= min(3t+3, 4t+2) >= 9 > 8` verified by
  hand and machine-swept over 1,575 admissible triples. Correct.
- **Reconciliation with the record**: NOT a contradiction of the
  banked measurement — the 12,731-tuple sweep varied slopes at fixed
  supports; the obstruction lives in the supports (four fibres of one
  pencil) plus a codimension-1 slope condition (the cross-ratio locus,
  the exact dual of banked S4-4). The control fixture (same shape,
  non-fibre blocks, exhaustive slopes, collapse holds) seals the
  explanation.

## Flag adjudication (9 flags)

F1 (claim 7 restated) — APPLIED as a dated addendum to
`background/nodes/xr_support4_structure/statement.md`: the general
collapse conjecture is REFUTED; the node's fixture measurements are
UPGRADED to theorems (Theorem 2/3 + Cor 3b/3c cover every cited
fixture); PROVED claims 1-6, 8 untouched (nothing consumed claim 7 —
the node's own honest MEASURED label did its job). F2 (RowC toy-row
kill unsupported) — APPLIED to the same addendum; the `k > 2h^2`
secondary criterion's load-bearing use at RowC rows is now OPEN
(Theorem 3 misses by 3 there). F3 (V <= m/2 struck) — APPLIED;
replaced by Prop 6 and the V >= 5 question. F4 (band-gate
realisability of X1-X3 unchecked; toy fields) — correctly flagged;
recorded as the COMPUTE REQUEST it is. F5/F6 (V=4 scope; no deficit
bound) — honest. F7 (read-only reuse of the node verifier; 57/60
matches the node's own degenerate filter) — verified. F8 (compute law
kept) — clean. F9 (the coordinator's `git add -A` swept its
in-progress files) — coordinator's fault, benign; final state banked
in this commit; explicit-path commits while pilots run from now on.

## What this changes

- **Both named open sub-items of the band heart are DEAD as posed**:
  the zero-escape collapse is false (gate-clean counterexamples,
  deficit up to 2); `V <= m/2` is false. The heart itself SURVIVES:
  Prop 6 proves per-ray charge >= 2 through the escape-0 channel at
  V=4 — settling that channel positively at V=4 and answering the
  sibling pilot's flag-5 structure at escape 0.
- The remaining open channels for the occupancy heart are now EXACTLY:
  (i) V >= 5 zero-escape systems below the Cor-3b threshold
  (`(V-3)t + |A_0| <= k-1`), and (ii) the escape-1 channel
  (gate-clean realizability still open).
- New proved tools of record: the duality criterion (Ann = 0), the
  MDS-chain and triple-cover collapse criteria, the V=4 cross-ratio
  classification (dual of S4-4), and PROP 5's improved unconditional
  floor `rank >= m + dim Sum C_{I_ab}`.
- The band-mint fixture's collapse is now a THEOREM (Cor 3c), removing
  one MEASURED label's load.

## Surfaced decisions (for the user)

- Next pilot anchor: the V >= 5 occupancy question
  (`V >= 5` zero-escape + pairwise + k-packing => `rank >= 2V`?) with
  the pilot's pre-registered falsifier — this and escape-1 are now the
  ONLY routes to the heart. Recommended: YES, both, one pilot each.
- The RowC 1/4 toy-row kill needs re-derivation from V >= 5 support
  conditions (or an honest OPEN marker in the re-pricing trail) —
  applied as OPEN in the addendum; a re-derivation task is queued.
