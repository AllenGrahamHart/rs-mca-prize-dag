# Conditional proof: `M=4,t=2` rate split

Assume `l1_fpc5_ratehalf_m4_t2_payment`.

The official small-source sieve proves that strict `M=4,t=2` FPC5 cells occur
only at rates `1/2` and `1/4`. The proved rate-quarter payment bounds that
entire branch by first-layout domination and pair uniqueness. The assumed
rate-half child pays the other branch with the background, exactness, and
internal-owner guards retained.

The two branches are disjoint by the official rate. Their union is the whole
`M=4,t=2` residual, so the parent is paid. QED.
