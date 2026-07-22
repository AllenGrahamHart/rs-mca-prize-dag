# Audit

- Trade rank is preserved by the full-column-rank row compression.
- The Singleton argument deletes rows of the compressed `(t-2) x |V|`
  matrix, not rows of the original `t x |V|` matrix.
- `(RM3)` uses the proved lower bound `D`; a larger actual trade space can
  only improve the guaranteed rank.
- The official arity numbers use the sufficient `e=0` inequalities at
  `s=k-a`. They are not claims for every smaller `s`.
- Rank-at-most-two does not import the uniform-cell rank-two atlas when
  `u>0`.
- No Modal or large local computation is used.
