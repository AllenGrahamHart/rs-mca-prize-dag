# Audit - L1 Pade split-section/support-moment inversion

## Checked axes

1. `Uhat` is the degree-below-`n` interpolant of an arbitrary received word.
2. Support size satisfies `m>=k`, ensuring a unique explaining codeword.
3. The Pade section is unguarded in `S_m`.
4. The complement gcd guard selects complete agreement sets.
5. One codeword with `a` agreements contributes `binom(a,m)` supports.
6. Binomial inversion runs upward from `a` to `n` with alternating signs.
7. The direct upper bound uses nonnegativity, not cancellation.
8. Smoothness is unnecessary for the identity.
9. Primitive/quotient labels are not claimed to survive inversion.
10. Upstream finite numerator conventions remain an explicit obligation.

## Route effect

The Pade split count and upstream lattice/split-pencil support census are no
longer merely analogous.  They are the same unguarded object, with exact L1
shells as its binomial atoms.
