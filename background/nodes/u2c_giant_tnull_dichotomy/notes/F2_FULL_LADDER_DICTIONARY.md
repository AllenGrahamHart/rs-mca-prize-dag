# F2 campaign: the FULL-LADDER DICTIONARY (log-derivative form)
# — dissolves catch #6's char restriction at the dictionary level

Status: PROVED (five lines, below) + exhaustively machine-verified
(750k+ subsets across 10 cells, both truth branches exercised, five
cells with t > q; digests F2_FULL_LADDER_DICTIONARY_PASS +
F2_FULL_LADDER_DICTIONARY_TRUEBRANCH_PASS).

## Theorem

For any t, any characteristic q, S a b-subset of mu_n with reversed
locator ell*_S(X) = prod_{x in S}(1 - xX) = 1 + c_1 X + ... + c_b X^b:

  S is t-null  <=>  c_i = 0 for every 1 <= i <= min(t, b) with q !| i.

Indices divisible by q are exactly FREE (the Frobenius redundancy,
now a theorem rather than a caveat); indices i > b impose nothing
(deg (ell*)' = b - 1).

## Proof

(ell*)'/ell* = sum_{x in S} -x/(1 - xX) = -sum_{j >= 0} p_{j+1} X^j.
Since ell*(0) = 1 is a unit, p_1 = ... = p_t = 0 iff (ell*)' == 0
mod X^t, i.e. i*c_i = 0 for 1 <= i <= t, i.e. c_i = 0 exactly at the
q-free indices. QED

## Consequences

1. The zero-prefix Q identification (f2_zero_prefix_q_equivalence)
   now covers the ENTIRE official ladder, not just j < char q: the
   official F2 object IS the census of degree-b divisors of X^n - 1
   with coefficients vanishing on the q-free indices <= t. Catch #6's
   restriction is dissolved at the dictionary level (it survives only
   as the width bound in the empty-extremes lemma).
2. Both crux faces upgrade: FACE B is now exact at the official
   shape; FACE A's W_j can be replaced by the coefficient-vanishing
   scheme at any ladder height.
3. Effective condition count = #q-free indices <= min(t,b) — the
   exact figure for the L5 tolerance arithmetic.

## Replay

Inline in campaign log #18 (local, very small): exhaustive two-branch
agreement at (17,16), (31,30), (13,12), (97,32), (113,16) cells
including t = 20..40 > q rows and live-null small-t cells.
