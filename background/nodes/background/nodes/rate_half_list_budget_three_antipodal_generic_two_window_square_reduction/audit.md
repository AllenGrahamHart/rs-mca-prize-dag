# Audit

The modulus `z^h` is load-bearing. It discards every term containing two
copies of `A-B`, but the exact full residual has higher tail terms and is not
claimed to equal `4B^3T_hat` as a polynomial.

The square normalization uses `c=a_(2h)!=0`, which is the exact-contact part
of the primary generic boundary. A double zero followed by another zero is a
different stratum and is not covered.

The exact characteristic-193 packet with order `64` and deleted exponents
`{0,1,3,62}` passes the primary gap but has terminal square-root coefficients
`102,24`; `verify_audit.py` checks that the original residual construction and
the two-window formula agree coefficientwise.

The characteristic-zero fixture `E=1+z^4`, `d=24`, `h=4` passes both the
primary and secondary gaps, although the existing canonical-span strictness
fixture rejects it later. This non-dyadic example prevents interpreting
`(TWS5)` as a formal-series contradiction independent of subgroup arithmetic.

A complete order-128 pilot finds primary-gap packets only over `F_257` and
`F_641`, `192` in each field, and rejects all of them at `(TWS5)`. Orbit
classification exposes one ordinary scaling orbit and one orbit consisting
of two deleted antipodal pairs in each field. This is evidence selecting a
parity-reduced sublane, not transport to official order.
