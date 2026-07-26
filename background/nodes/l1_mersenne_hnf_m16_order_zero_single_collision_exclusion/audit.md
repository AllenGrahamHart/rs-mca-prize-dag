# Audit

## Pattern completeness

After division by the duplicated color, the omitted colors are two distinct
members of `mu_16\{1}`. The 105 exponent pairs in the verifier are therefore
exhaustive. A different primitive sixteenth root only permutes those pairs.

## Moment scope

Only the first three centered moments are used, consuming locator power sums
through degree six. This lies well inside the proved range through degree 15.
The scripts test every color second moment before division.

## Common-root scope

The parameter `s` is not assumed to lie in `F_(p^2)`. Coprimality is computed
over the coefficient field `F_p(mu_16)` and excludes common roots in its
algebraic closure. The constant-coefficient equation is a necessary
consequence of all locator roots being `n`th roots; no sufficiency claim is
needed.

## Independent replay

The primary implementation uses the relation `z^2-128z+1`; the audit uses
`u^2+2`. Their primitive roots, multiplication laws, and common-root tests
are different. The audit pins a digest over the 105 quadratic coefficients,
resultants, and base-field norms.

## Nonclaims

The even multi-repeat chamber remains live. No `m=8` arithmetic is
extrapolated to this row, and no result is claimed for degree at least three.
