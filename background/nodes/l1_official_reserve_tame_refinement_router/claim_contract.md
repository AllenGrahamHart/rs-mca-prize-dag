# Claim contract - L1 official-reserve tame-refinement router

## Inputs

- the generated field `F_(p^f)`, not an unrelated ambient field;
- `n=2^m>=2^13`, `n|p^f-1`, `p^f<2^256`, and `k<=n/2`;
- one reserve-qualified `sigma` and the canonical weaker cutoff using
  `eta=min(epsilon,1/4)`;
- a fixed-source whole-petal refinement at `ell_0=sigma_0+1`.

## Output

The canonical cutoff satisfies `ell_0<p`. Every divisor `ell_0/s` is tame,
so all fixed-petal refinement maps in one source number at most `n`.
Threshold monotonicity transports any larger reserve-qualified agreement to
this cutoff.

## Falsifier

An input satisfying every official hypothesis with `ell_0>=p`; or a
whole-petal refinement at the canonical cutoff with
`p|ell_0/s`.

## Nonclaims

No role-vector payment, partial-fiber payment, unanchored-map count,
arbitrary-locator count, quotient-list theorem, or row-sharp Q theorem.
