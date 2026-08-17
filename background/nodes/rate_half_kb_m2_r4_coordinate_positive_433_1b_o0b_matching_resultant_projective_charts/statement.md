# Statement

Write

\[
 P(z)=p_0+p_1z+p_2z^2,\qquad Q(z)=q_0+q_1z+q_2z^2.
\]

Each of the O0b matching equations `q4`, `q5`, and `q6` is exactly

\[
 \operatorname{Res}_z(P,Q)
 =(p_2q_0-p_0q_2)^2
 -(p_2q_1-p_1q_2)(p_1q_0-p_0q_1).
\]

Over the algebraic closure of `F_2130706433`, this vanishes exactly when one
of the following charts holds:

1. **finite:** there is a `u` with `P(u)=Q(u)=0`;
2. **infinity:** `p2=q2=0`, so the homogenizations share `[1:0]`.

Therefore the conjunction of the three matching equations is exactly the
union of the eight choices in `{finite,infinity}^3`.
