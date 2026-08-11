# FABLE_AUDIT — r37_urand (round 37, bank 1/4)

Auditor: coordinator (Fable). Date: 2026-08-11.
Verdict: **BANKED — STATEMENT U REFUTED (the day-old round-36 pin
withdrawn and re-priced to r+1 + Theta(n/rho)); the coset-leader
frame adopted as the far-CA instrument of record; U-sym closed
with the parity derivation corrected; the C(128,63) check closed
(cap no, dedup yes). Four forced corrections applied — the
fastest banked-pin turnover in the campaign (posed round 36,
refuted round 37, same day).** Node work: REFUTED/CHECK-DONE
markers on the round-36 R-HRLOW addendum + the round-37 U-rand
addendum. No status flips; census unchanged.

## Verification (hand-checks, all pass)

1. **The MDS code:** ker syn = {g|_D : deg g <= k-1} via the
   power-sum vanishing; [n,k] GRS, d_min = R+1 — CHECK (textbook,
   correctly re-derived).
2. **FENCE-1:** supp(c) in S u W and wt(c) >= R+1 force
   |S u W| >= R+1; contrapositive exact — CHECK (two lines). The
   pilot's own subtraction (#4: the inequality is the banked
   minimum-distance spend in the FR lane) is right, and its
   additive part (the razor instantiation at forced |W| = r+1,
   the fence reading, 297/297) is genuinely new.
3. **The rho-1 law:** (f+t) - (|W|+t-R) - 1 with |W| = r+f gives
   R-r-1 = rho-1, t- and f-free — CHECK; the three derivations
   are genuinely independent (degree bookkeeping / affine system
   / the V_S codimension jump 1 -> rho).
4. **The razor cap:** 2(r+1) = 2,164,663,517,186; minus 126*2^34
   = 2 — kernel dimension EXACTLY 2 at j = 126, negative at 127;
   r+1+126 = 1,082,331,758,719 — CHECK to the digit.
5. **The construction + census:** T = (r+1)+j exactly at every
   census row including the FULL C(26,10) sweep — the right
   verification level (exhaustive, not sampled), on mu_n domains
   (the razor's type), three fields at mu_20.
6. **ceil vs floor:** rows 2s and 2s+1 fuse on the carrier
   (sigma^o = p, sigma^e = -x_0 p) — the round-36 derivation
   double-counted the parity blocks; measured excess 0 at rho =
   3,4 with BOTH inclusions — decisive. My round-36 bank-3
   addendum text carried the floor version; corrected.
7. **C(128,63):** ratio 128/65 exact (integer identity verified);
   the two objects are genuinely different quantifiers on
   different objects; the dedup-transports/cap-does-not verdict
   is sound. The pilot's blind 0.977488 vs true 0.977632 —
   self-caught, and its pre-registered warning (two different
   0.977s) was the load-bearing part and was right.

## The repricing (coordinator judgment)

The refutation is accepted at full strength: the construction is
linear algebra, the censuses are exhaustive, the domains are the
razor's type, and the mechanism needs no symmetry. The +126 floor
is banked as CONSTRUCTIVE-MODULO-GENERICITY exactly as the pilot
graded it (ZP-7 — the honest gap named R-GENERICITY). Strategic
note: in BITS nothing moves (2^39.9773 both ways), so the prize
question is untouched; what changes is the shape of the residual
(R-URATE: one finite rank question; R-GENERICITY: one lemma) —
arguably a SIMPLIFICATION of the far-CA endgame, not a setback.
MINT-WAVE INTERACTION: the r37_mint_drafts pilot is drafting
statement_u as package #1 against the now-refuted pin — its
draft will be re-statused at that bank (U as definition; REFUTED
as theorem; the new pricing). Recorded here for reconciliation.

## Honesty audit

Excellent: the wrong blind constant reported as miss 1; the
j-ladder gap that made its own headline a 2x understatement
(miss 2) caught by re-reading its own design; the A-5 falsified
half and the R2j self-refutation reported; the integer-collinear
family explicitly de-powered (ZP-13) after nearly being the
headline; no widening needed because the field range was
registered honestly up front.

## Compliance

Compute law CLEAN 5/5 (the streak rebuilds: 1). BOTH new
round-37 rules held on first outing (append-mode results files —
which would have saved round 36's two losses; no head pipes).
Anti-import pattern used (helpers duplicated per file).
Quarantine exemplary. Registrations honest with three
self-refutations reported.

## Mint queue additions

1. The coset-leader frame node (u = h + c; FENCE-1; minimal-spend
   rigidity; chi_Y; the rho-1 law) — PROVED components.
2. The U-refutation + re-priced count record (constructive floor
   modulo R-GENERICITY; the cap heuristic; the bits-invariance).
3. R-URATE + R-GENERICITY as the far-CA targets of record.
4. The ceil(rho/2) symmetric-T closure (+ the T = 336
   decomposition; carrier-exhaustiveness residue).
5. The C(128,63) check record (cap no, dedup yes — the dedup is
   a usable lemma for any T_sym campaign).

## Round-38 anchors fed by this bank

R-URATE (the rank question — finite and self-contained);
R-GENERICITY (converts +126 to unconditional); the
carrier-exhaustiveness residue; the statement_u mint re-status.
