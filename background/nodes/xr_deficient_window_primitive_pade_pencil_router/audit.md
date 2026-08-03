# Audit

## Logical checks

- The determinant is evaluated on the full joint error support, not on an
  arbitrary interpolation subset.
- The strict inequality `r'>2d-2` is checked at the worst official depth
  `d=h-2`; no asymptotic estimate is used.
- Polynomial gcd cancellation occurs only after an identity in `F[X]` has
  been proved. No finite-window recurrence is cancelled.
- The primitive relation outside `G_d` chooses a multiplier separately at
  each point; it does not require one multiplier avoiding all roots.
- The common polynomial `Pf+Qg` is unique because `n-g>=k+ell`, derived
  from `ell+g<=d-1`.
- The affine parameter bound uses both degree constraints and
  `ell=max(deg P,deg Q)`.

## Ownership audit

P0 annihilates both individual syndrome systems with one locator; this node
starts from two-word left syzygies, so P0 is not invoked. Upstream's
moving-root theorem counts split locators in one projective coefficient
pencil; `(PP4)` is instead an affine family of codeword pairs. There is no
transport theorem between those currencies.

## Residual risk

The remaining count may still require a new owner-aware list bound for the
parameter word `tau`, or a transport into the base-field-normalized
split-pencil census. This node proves the normal form only.
