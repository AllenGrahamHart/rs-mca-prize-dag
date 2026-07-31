# Audit

1. The scalar is derived by applying the homogeneous transformation twice;
   no leading coefficient or Mobius denominator is divided out.
2. The negative eigenvalue is excluded only after using fixed-point freedom.
3. Fixed points are considered over an algebraic closure, so nonsplit
   involutions are covered.
4. The rank-three count uses odd characteristic and `Delta!=0` explicitly.
5. The primary checker expands the general coefficient action; the audit
   checker independently diagonalizes the action and checks both eigenspaces.
