# TARGET 1B — THE PARITY SUMMIT, corrected centering. Prove or falsify.

Supersedes SOL_TARGET_1 (refuted as written at j >= 4 — mis-centered;
see its appendix). Setup identical to SOL_TARGET_1 (q odd prime, n a
2-power, mu_n <= F_q^x, s_x(c), S_c, K_c, U_c, eps_c).

## The corrected conjecture

For every fixed j >= 2, with M_j = 2^{ceil(log2(j+1))} (the least
2-power exceeding j) and Struct_j = 2^{n/M_j} (the exact char-0
structural census: unions of mu_{M_j}-cosets — banked theorem, M > j),
there is delta(n) -> 0 such that for all (q, n) with n -> infinity:

  ( sum_{c != 0} eps_c e^{S_c}  -  Struct_j (q^j - 1) )^2
      <=  4^{delta(n) n} * ( sum_{c != 0} e^{2 S_c} ).

(The right-hand sum is an exact integer via the in-repo ladder
identity; squaring avoids the non-integral square root.)

## PROVE OR FALSIFY.

Scope notes (honest, load-bearing):
- j in {2, 3} is the case with the complete in-repo instrument chart
  (satellites 16-30) and all numerical ground truth (orbit-normalized
  ratios 0.04-1.6 across 9.4k..9.4e9 states). j >= 4 has the corrected
  centering above and no dedicated measurements yet.
- A proof at fixed j does NOT by itself flip a prize floor: the
  banked consumer needs all q-free levels up to growing t. It would
  be the first theorem-level cancellation result for this object
  class and the direct input to the level-induction the consumer
  needs.
- A falsification means the orbit-normalized ratio growing like
  2^{cn} along a family at 3+ growing scales WITH the corrected
  centering (deep-prime families are now correctly centered by
  construction; the deep-regime exactness theorem makes them
  ratio -> 0, so a falsifier must live at moderate q — the
  fluctuation band — or at structured families no test found).
- Everything in SOL_TARGET_1's "facts you may take as given" list
  remains valid verbatim EXCEPT the centering and the floor-flip
  claim.
