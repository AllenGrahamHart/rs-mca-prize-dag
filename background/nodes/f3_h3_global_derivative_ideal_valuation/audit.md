# Audit

Date: 2026-07-18.

Verdict: **NO ISSUE** after an independent construction and
consumer-backward read of the earlier quarantined packet.

## Construction read

- `Pcal` uses the ordered product multiset. The shifted-product Sidon theorem
  makes its characteristic-zero root multiplicities exactly one or two, so
  the derivative ideal is nonzero.
- Hasse derivatives, rather than ordinary derivatives, give the coefficient
  identity and the valuation estimate without factorial conventions.
- The denominator clearing factor is `c_u^N`; its norm is a power of two at
  dyadic order, so removing the two-primary part is legitimate.
- Galois invariance is factorwise: odd dilation permutes all ordered pairs
  `(u,v)`. At odd primes the cyclotomic extension is unramified, which makes
  the odd norm a `d`th power. No splitting assumption is used here.
- The row prime does split completely because `p=1 mod n`. Each ordered
  quotient representation occurs once among the reductions of `gamma_uv`,
  giving the required quotient weight `R(t)` rather than a marginal product
  count.

The focused verifier independently constructs the integral derivative ideals
in `Z[zeta_8]`, computes their lattice norms by Smith normal form, checks the
perfect-power property, and tests the generalized cutoff-two valuation on
finite rows where the weighted excess is nonzero.

## Consumer-backward read

The critical consumer requires `17X_18<=300n^2`. From `p^X_18|e_n`, either
the printed size bound or the stronger condition `p` not dividing `e_n`
supplies that exact target. No estimate for `e_n` is proved, so this node is
wired only as evidence and the critical status remains `TARGET`.

## Nonclaims

- No efficient official-order construction or factorization of `e_n` is
  claimed.
- The theorem does not show that the exceptional set is empty.
- Small-order `e_n` computations are verifier fixtures, not evidence for the
  official orders.
- No Modal resource is used.
