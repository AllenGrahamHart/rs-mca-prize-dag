# F1 β-check: the evaluation-field clause at base-domain extension rows
# (node-local, 2026-07-07)

Part of the correspondence β-round (MB_VS_F1_LEDGER.md §7 follow-ups).
Definitional audit — no computation needed for the verdict; the sibling
F7 census (worst_word_challenger_pricing/notes/f7_beta_check.md)
verifies the same mechanism end-to-end.

## The exposure (model-clause level)

The consumer's flatness target (x4 REDUCTION_PACKET,
pcf_evaluation_flatness) prices

    B_j(M) = #{d ∈ D_j(M) : Q_d(ζ^{2l−1}) = 0 in F_q, 1 ≤ l ≤ L_j}

as "L_j genuinely independent F_q-conditions" (model q^{−L_j}), and the
floor's budget q^{−t+H}·W_cen ≤ 2^122 carries that q-normalization.

At a base-domain extension row this premise FAILS by field confinement
(proved, one line each):
- the objects d are domain-combinatorial (t-null multiset blocks and
  their profiles) — D ⊆ F_p makes Q_d ∈ F_p[x];
- the evaluation points ζ^{2l−1} lie in F_p(ζ), with [F_p(ζ):F_p] ≤ 2
  (ζ a 2n-th root of unity; at the KoalaBear-shaped row 2n = 2^22
  divides p−1 = 2^24·127, so ζ ∈ F_p exactly);
- hence each condition "Q_d(ζ^{2l−1}) = 0 in F_q" is an F_p(ζ)-condition:
  per-condition density 1/|F_p(ζ)|, not 1/q. Mis-pricing factor
  (q/p)^{L_j} = 2^{154.9·L_j} at the KoalaBear-shaped row; aggregated
  over t conditions at the x4 lane's t-scale, the same 2^(~1.7M)-bit
  class as F2's catch #11.

Unlike a word-averaged statement, W_cen has no measure dilution to hide
behind: "U-weighted" refers to the U_j(M) universe counts and profile
weights (packet line B_j(M) ≤ q^{−L_j+η_j}·U_j(M)), not to an
expectation over received words.

## Honest grading (catch #13)

- PROVED: the "genuinely independent F_q-conditions" clause is false at
  base-domain official extension rows (field confinement above).
- NOT constructed here: an explicit B_j(M) count exceeding the budget at
  such a row (would require porting the b2b skew machinery to F_{p²} —
  deliberately not launched; the wording fix does not need it, per the
  no-big-runs-without-confidence rule). The F7 census confirms the
  identical mechanism (base-confined conditions ⇒ p-law counts) in the
  sibling lane.
- FIX: the floor and the flatness target read the evaluation field as
  the GENERATED field F_p(D, ζ): conditions are |F_p(D,ζ)|-conditions;
  the budget's normalizer follows. At generating rows (all nine
  adversarial rounds, all toy towers: F_17/97/193 etc.) the readings
  coincide — the entire evidence ledger is untouched. Non-generating
  official rows route through the f1/ext descent, where the base-row
  reading is the correct one natively (same consumer rule as F2's
  catch #11).
