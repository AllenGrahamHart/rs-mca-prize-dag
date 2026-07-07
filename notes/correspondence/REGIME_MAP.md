# Regime map: both programs on the balance coordinate (2026-07-07)

Pre-PR work item 2 (THREE_VS_SEVEN.md). Chart: `regime_map.svg`
(generator `gen_regime_map.py`); replay scripts `four_pairs_exact.py`
(this dir). Companion to MB_VS_F1_LEDGER.md.

## 0. The coordinate

Every object of both programs is placed by
Δ = log2(#configurations) − log2(#values in the TRUE value field),
at its row size n. Δ > 0 = above balance (pigeonhole forces collisions;
window populations live there); Δ < 0 = sub-balance (accident-free
regime, our F2 window's home). The "true value field" clause is
catch #11's content: for base-confined objects the value field is the
generated field, whatever the ambient row field is.

## 1. ALL FOUR upstream adjacent pairs replayed exactly (their conventions
##    pinned from V13 prop:capg-moved-frontier + cor:capg-adjacent-pairs)

Conventions (now verified, not conjectured):
- list row:  unsafe(m) ⟺ C(n,m) > p^(m−K)   · ⌊q·ε*⌋
- MCA row:   unsafe(m) ⟺ C(n,m) > p^(m−K−1) · ⌊q·ε*⌋
  (their own remark: "at equal m the MCA comparison is exactly one
  factor of p easier" — the identity witness runs at K = k+1, the
  pencil degree of freedom)
- KoalaBear rows: q = p^6, ε* = 2^−128 (official-shaped).
- M31 circle rows: q = p'^4, ε* = 2^−100, D ⊆ B = F_p' on the twin-coset
  x-domain (extra-official; "D ⊆ B is all that is used" — their words,
  our f1 case-(i) routing in their clothes).

Exact-integer replay (four_pairs_exact.py), n = 2^21, K = 2^20:

    row              a0        unsafe@a0   safe@a0+1   printed margin
    KoalaBear MCA    1116047   +8.978      −22.197     22.2  PAIR OK
    KoalaBear list   1116046   +9.164      −22.011     22.0  PAIR OK
    M31 MCA          1116023   +27.927     −3.259      3.3   PAIR OK
    M31 list         1116022   +28.113     −3.073      3.1   PAIR OK

Every location and every margin. The MCA−list margin offset at equal
pair index is log2(m/(n−m)) ≈ 0.186 bits (one binomial step vs one p),
their interleaving inequality a0_list ≤ a0_MCA ≤ a0_list + 1 realized
at the right edge on both rows. THE ENTIRE DEPLOYED FINITE FRONTIER OF
UPSTREAM'S PROGRAM IS ONE FORMULA FAMILY = OUR BASE TANGENT-COLUMN MEAN
vs THE ROW GATE, with the pencil shift for MCA. This completes work
item 2's cross-prediction half (the MCA gate convention, previously
unexplained, is now pinned to their printed identity-witness recipe).

Context they prove around these points: the deployed gaps sit within
7.2·10^−7 (KB) and 4.9·10^−7 (M31) of the entropy-subfield envelope
ceiling 1−ρ−g*; head-depth exactness is PROVED for w ≤ 21 (KB) / w ≤ 10
(M31) with million-bit margins — i.e. their theorems cover the deep
above-balance strata (Δ ≈ +2.09M bits) and their ONE red (Q) is the
claim that nothing beats the witness at the crossing depths.

## 2. The map (regime_map.svg)

- Their four crossings cluster at Δ = +21…+67 bits at n = 2^21 —
  ON the balance line at row resolution (tens of bits out of 2.09M,
  fractionally ~3·10^−5): margin-critical by construction.
- Their proved head-depth theorems: Δ ≈ +2.09M bits (deep above
  balance, the dense bulk — the regime where OUR F2 window never
  claims anything).
- Our F2 hardening censuses: Δ ∈ [−14.5, +5.6] bits at n = 32–128,
  straddling the line from below; extras = 0 at every sub-balance
  point; the above-balance witnesses (p = 97 giant blocks at +6.6,
  p = 21313 relatives at +0.4) populate exactly where pigeonhole says
  they must.
- Our F6 determination flips (σ = 1, q = 241…337): the measured
  unsafe→safe transitions sit at the balance-line crossing — the same
  phenomenon as their adjacent pairs, at toy scale.
- Official prize-max F2 window (generating rows): Δ = −0.02n =
  −4.4·10^10 bits — our floors live FAR below the line by design.
- Catch #11: the KoalaBear row appears twice — q-scale reading at
  Δ = −162 (window "admits") and true p-scale reading at Δ = +1.74M;
  the β-jump arrow between them is the finding.

## 3. Regime geometry conclusions for the F2↔Q bridge

1. NO OVERLAP of claim regimes: our F2 claims live at Δ ≤ 0 (true
   scale); their proved theorems live at Δ ≫ 0; their conjectured Q
   lives at the line. The bridge statement ("same object, uniform vs
   average form") is regime-consistent: no point of the map carries
   contradictory claims from the two programs.
2. BOTH determinations are balance-line phenomena: their four pairs
   and our F6 flips are the same crossing arithmetic at scales five
   orders apart (2^21 vs ≤ 2^7 points). This is F6 auxiliary evidence
   (pushed node-local to rate_half per the node-local rule).
3. The danger zone their calibration flags (Poisson boundary,
   max-to-mean growth) is the near-line region from above — exactly
   where our above-balance witnesses live and where neither program
   has theorems. The regime map makes the shared frontier visually
   one object: the line itself.
4. F7's envelope objects (challenger counts ~ K_cell/q^σ) are NOT
   placeable on this coordinate without forcing (they are per-cell
   count laws, not census-vs-value-space objects) — omitted from the
   chart deliberately; noted here so the omission is not read as
   coverage.

## 4. Node-local pushes done with this note (per the 2026-07-07 rule)

- rate_half (F6): external determination-fidelity datum — upstream's
  four pairs = first-moment crossing predictions confirmed exactly at
  n = 2^21 (vs our q ≤ 1153 ladders); statement addendum + node note.
- f1_case_tower: tower depth-1 fact at KoalaBear-shaped rows;
  statement addendum + node note.
- u2c_giant_tnull_dichotomy: catch #11 already in statement (M_B
  audit); node note added pointing here and to MB_VS_F1_LEDGER.md.
