# Consumer-backward audit

- **verdict:** NO ISSUE
- **consumer:** `f3_h3_mobius_excess_half`
- **scope:** exact cutoff-18 weighted excess

The consumer needs `17X_18<=300n^2`. The reduction pays only terms with at
least one quotient representation; it does not incorrectly subtract one from
an empty quotient fiber. The pointwise identity
`R=1_(R>0)+(R-1)_+` handles `R=0,1`, and `R>=2` exactly.

The single layer uses only `Q_18<=P` and `sum_t P(t)=|A|^2`; no energy,
uniformity, or field-size hypothesis is hidden. The residual constant is the
exact subtraction `300n^2-17(n-1)^2`. The convenient `16n^2` form is stated
as stronger, not equivalent.

At the measured boundary rich fibers, `P=20,R=1`, so `X_18=2` per fiber but
`Y_18=0`. This illustrates the strict reduction but is not used in the proof.
The node makes no claim that the remaining double accidents are independent.
