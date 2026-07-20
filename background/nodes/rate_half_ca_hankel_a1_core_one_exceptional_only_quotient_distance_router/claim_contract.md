# Claim contract

- **scope:** official `A=1`, core-one, exceptional-only sharp-cap profile
- **input:** the three scalar moment gate
  `(Theta_0,Theta_1,Theta_2)=(0,0,nonzero)`
- **currency:** support size of the first-order syndrome modulo the
  exceptional locator columns
- **output:** quotient distance at least three; at distance three, one unique
  support triple with explicit barycentric coefficients
- **consumer:** `rate_half_band_closure`
- **load-bearing hypotheses:** squarefree split `A`, distinct residual-domain
  points, moments available through degree `2r`, and `Theta_2!=0`
- **nonclaim:** neither the distance-three nor distance-at-least-four branch
  is excluded; lower Hankel, reciprocal, and splitting gates remain due
- **failure certificate:** a representation modulo `W_A` on at most two
  columns, or two distinct supporting triples, replayed against the three
  moment functionals
