# Audit

## Forward audit

1. The swap router supplies exactly `(h-1)/2` odd power-sum congruences.
2. Antipodal freeness makes the lifted cyclotomic sum nonzero and gives odd
   Parseval energy exactly `h`, rather than the generic `4h`.
3. Complete splitting of `p` turns the congruences into distinct norm factors.
4. Strict `p>m^2` yields the strict necessary inequality `(SNH1)`.
5. The dyadic band uses only `h<=m/4` and exact exponent arithmetic.
6. The exact Haar condition implies `X^2<m`, which places it strictly inside
   the swap band; dependency composition proves full emptiness there.

## Consumer-backward audit

The full Haar overlap contributes zero to the exact-level ledger. This node
leaves only free-class orbits between the Haar cutoff and `(SNH4)`; the
downstream Vandermonde-defect theorem deletes an initial subrange of those as
well. No debit is claimed below the swap cutoff.

## Scope checks

- The result applies only to antipodal-swap pairs until the Haar dependency is
  invoked.
- Even swap widths were already empty; the new norm theorem matters on odd
  widths and completes the Haar overlap.
- Equality in `(SNH2)` is excluded because `p>m^2` is strict.
- No floating-point computation enters the proof.

## Independent replay

The main verifier checks every dyadic band endpoint through `2^41`, exact
small-level norm arithmetic, the Haar-band inclusion, and DAG wiring. The
audit verifier independently exhausts the first swap control and checks the
strict-prime and antipodal-freeness mutations.
