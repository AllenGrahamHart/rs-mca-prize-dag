# Audit

- The chamber count is exact: `4+1+1+2+1=9` linear chambers and
  `3+1=4` quadratic chambers.
- Constant edges do not invalidate the Grassmann-line proof. They instead
  make independence of `B_0,B_1` immediate.
- A zero annihilator coefficient would force one complementary triangle to
  have three constants or three linear factors with a shared root. The table
  allows the constant case only for the path `013` triangle. In an all-linear
  cycle triangle, two tight selected-edge roots are already distinct; no
  distinctness assumption is made about a slack quotient root.
- The no-proper-subsum assertion is scoped to `d>=3`, so every consumed block
  locator is nonconstant.
- Exceptional degrees count selected coordinates, not quotient-factor roots:
  cycle `4`, `K_4-e` `6`, `K_4` `8`, path `3`, triangle-singleton `5`.
- The four quadratic chambers are not declared impossible. They are the exact
  remaining bounded-edge classification problem.
