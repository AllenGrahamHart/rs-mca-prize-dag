# Proof

Work in the rational function field in `b,c,d,w` on the named chart `b!=0`.
The exact audit reverses numerator and denominator polynomials in `b`, so no
fractional substitution or interpolation is used.

For each of `F04 -> F05` and `F06 -> F07`, direct reconstruction proves that
`U`, `V`, and `z` pull back exactly. The `J`, `I`, `K`, and `R` label lists
pull back as multisets. Apart from the monomial `b`, whose inverse is again a
unit on this chart, reversal maps the 29 other primitive named factors
bijectively to their target factors.

The same substitution sends `G=U^2-WV^2` exactly to the target `G`. It maps
the six `J` evaluations and six `I` evaluations as multisets, and maps the
`q`, `K`, and `R` locators exactly. Hence both full quotient identities are
preserved, not merely their q-slice consequences.

Finally, for each of `R02,R11,R20`, all four raw q-slice rational equations
are replayed. Their cleared numerators agree up to sign and the transport
ratio has numerator and denominator supported only on target named units.
Thus their named-open zero loci agree. Inversion is involutive on `b!=0`, so
the maps are isomorphisms and preserve emptiness in both directions. QED.
