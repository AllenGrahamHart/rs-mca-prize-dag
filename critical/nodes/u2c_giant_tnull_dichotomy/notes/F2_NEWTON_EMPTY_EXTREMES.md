# F2 campaign: the NEWTON EMPTY-EXTREMES LEMMA
# (resolves catch #4 at the TRUE official shape; supersedes the
#  Weil-Newton band payment for F2's official rows)

Status: PROVED (three lines, inline) + verified (local, very small:
6 rows exhaustive, digest F2_NEWTON_EMPTY_EXTREMES_PASS). The official
(q,n,t) shape is pinned from the banked consumer survey
(notes/floor_campaign/SURVEY_X4_CLUSTER.md): prize-max has
t*log2(q) ~ 2.15e12 > n ~ 1.1e12 (q generated-field per catch #11),
i.e. t ~ 7e10 — LARGE t, window empty at every b.

## Lemma (CORRECTED same night — catch #6: char-limited width)

For 1 <= b <= min(t, q-1): there is NO t-null block of size b,
and (by the PROVED complementation lemma, valid since the full-domain
power sums sum_{x in mu_n} x^j vanish for 1 <= j < n) none of size
b >= n - t either.

Proof. p_1(S) = ... = p_t(S) = 0 with b = |S| <= min(t, q-1) gives,
by Newton's identities (inversion valid since 1..b are invertible in
F_q, i.e. b < char q), e_1(S) = ... = e_b(S) = 0. But
e_b(S) = +- prod_{x in S} x != 0 since 0 not in mu_n. Contradiction.
The complement case is the complementation lemma applied to D \ S. QED

## Consequences at the official shape

1. The extreme bands are EMPTY (not merely under budget) out to width
   min(t, q-1) ~ q ~ 2^31 on each side [catch #6: the first version
   claimed width t ~ 2^36, but char q ~ 2^31 < t at official rows —
   Newton inversion is char-limited; the toy rows (q > n) could not
   expose this] — vastly superseding the Weil-Newton
   b* = 5 payment, WHICH HAS ZERO REACH at F2's true shape (there
   t*sqrt(q) > n makes the subgroup Weil bound vacuous; the
   Weil-Newton lemma remains banked for small-t shapes and other
   floors). Catch #4 RESOLVED with this replacement.
2. The remaining obligation is the mid-band t < b < n - t with the
   flat-model mean C(n,b)/q^t < 2^{-1e12}-scale at EVERY b (window
   empty), while the budget is n^3: the required anti-concentration
   is a max/mean ratio bound of up to ~2^{1.05e12} — EXPONENTIALLY
   WEAK. M1's target is reframed: not sharp flatness, ANY nontrivial
   fiber-to-mean bound with sub-double-exponential loss suffices.
3. beta-discipline: q throughout is the GENERATED field (catch #11);
   the survey quote is already beta-normalized.

## Replay

python3 - (inline in the campaign log entry #9; exhaustive at
(97,32,t=2..4), (193,32,3), (97,16,4), (257,16,5): zero t-null blocks
at every b <= t; full-domain vanishing checked so the complement
mirror applies).

## Catch #6 addendum (same night)

The char bound also imposes Frobenius redundancy on the condition
system in char q: p_{qj}(S) = (p_j(S))^q, so conditions at indices
divisible by q are free given their q-free parts, and any p -> e
dictionary at indices >= q is invalid as stated. All mid-band
structure arguments (e.g. gap-divisor framings of t-null locators)
must be posed on the q-free index set with Frobenius handled
explicitly. The mid-band tolerance (~2^{1.05e12}) and per-condition
target (~2^15) are unchanged — they never used the band width.
