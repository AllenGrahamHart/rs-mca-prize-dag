# Audit

The trace coordinate is named `chi` because `x` already denotes the
polynomial variable in `D_0,U_0,S,T`. Mixing those coordinates would make the
cleared identities ambiguous.

The fourth-power test is sufficient only together with the selected scalar
identity and exact torsion trace. A fourth-power remainder by itself still
does not identify the Mobius branch or the correct quotient direction.

No square root of `q_out` must be computed by an implementation. The element
`eta` appears only in the proof that the old root-dependent square class and
the new fourth-power test are equivalent.

Every denominator is protected by the existing nondegeneracy and harmonic
exclusion. In particular `chi-1=0` or `chi-4=0` would force the corresponding
`b_j` to vanish and hence force `q_out=-1`; `chi+2=0`, `chi-2=0`, or `chi=0`
would give `r^4=1` in the branches where they occur.

The official exclusion problem still requires compressed access to `S,T`.
Materializing `x^N-1`, or treating the fourth-power test on a prefix as exact,
is outside the theorem.
