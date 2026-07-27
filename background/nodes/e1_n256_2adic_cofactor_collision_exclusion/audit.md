# Audit

Date: 2026-07-27.

The load-bearing ingredients are total ramification of two in the
power-of-two cyclotomic field, the integral Taylor expansion at one, and two
exact cofactor bounds. The proof carefully uses `p>2^250`, not merely a
floating approximation to the interval endpoint.

The local verifier checks the exact power inequality, the full two-singleton
multiplicity formula for every separation from 1 through 127, and both a
surviving and an excluded four-singleton example. These checks audit the
arithmetic interfaces; the field-theoretic proof is in `proof.md`.

No Modal run, factorization, resultant, or sampled norm computation is
load-bearing.
