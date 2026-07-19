# Claim contract

- **Claim:** the two-sided apolar generator of a deficient scalar Hankel
  pencil forces `(MI1)` and the supported-slope bound `(MI2)`; at the official
  rate-half row these bounds prove the first-transition CA assertion through
  budget `2^39-1`.
- **Quantifiers:** every field, every evaluation domain, and every syndrome
  Hankel pencil of generic rank `1<=rho<=r` in the split-pencil equivalence.
  Rank zero is separately vacuous for a column-far pair. The official
  corollary uses `N=2^41`, `R=2^40`, and a column-far received pair.
- **Dependencies:** `rate_half_ca_hankel_split_pencil_equivalence` identifies
  supported slopes with far-CA slopes;
  `rate_half_ca_hankel_fixed_kernel_branch` handles parameter degree zero;
  `rate_half_ca_hankel_fullrank_branch` handles generic rank `r+1`; and
  `rate_half_quadratic_exact_range` supplies the already-proved sparse-safe
  and adjacent-unsafe conversion from the CA bound to the exact agreement.
- **Characteristic:** unrestricted.  The proof uses divided-power apolarity,
  not ordinary differentiation.
- **Nonclaims:** no bound is claimed here for the remaining `A=3` or `A=1`
  branches, corresponding to budgets `2^39` and `2^39+1`.  The theorem does
  not assert that moving deficient kernels are impossible.
- **Falsifier:** a Hankel pencil violating `(MI1)` or `(MI2)`, or an official
  column-far pair at `r<=2^39-2` with more than `r+1` supported finite slopes.
