# Proof

The displayed polynomial is the determinant of the `4 x 4` Sylvester matrix
of `P` and `Q`; the verifier expands both expressions and also compares with
the symbolic quadratic resultant.

The homogeneous quadratics are

\[
 P^h(X,Y)=p_0Y^2+p_1XY+p_2X^2,\qquad
 Q^h(X,Y)=q_0Y^2+q_1XY+q_2X^2.
\]

The resultant vanishes precisely when these binary forms have a common point
of projective one-space over the algebraic closure. If that point has `Y !=
0`, scale it to `[u:1]`; this gives the finite equations `P(u)=Q(u)=0`. If
`Y=0`, the point is `[1:0]`, and the two equations are exactly `p2=q2=0`.
This includes zero polynomials and every degree-drop case, so no leading-term
genericity is assumed.

The outside compiler constructs `q4`, `q5`, and `q6` with this exact formula.
Distributing the two-chart union across the conjunction of three resultants
gives the eight distinct masks in `{finite,infinity}^3`. QED.
