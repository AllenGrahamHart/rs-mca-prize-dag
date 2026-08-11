# Cycle 60: rate-half Schur interpolation defect (2026-08-10)

## Exact residual formula

Write the normalized highest-clone polynomial at `x` as

```text
H_x(Y)=Y^Delta_x (Y-mu_x) product_(gamma in A_x)(Y-gamma)
      =sum_j h_j(x)Y^j.
```

After pivoting on any `4m+1` points `P`, exact Lagrange elimination gives the
nonpivot Schur entry

```text
c_(1,x) (x^i h_j(x)-sum_(p in P) ell_p(x)p^i h_j(p)).
```

Lower deficiency clones retain their original entries because their top
coefficient is zero. Thus the residual matrix is not a generic rectangular
matrix: it is precisely the interpolation defect of elementary-symmetric
root data, with direct monomial columns at deficient points.

## Frontier

`rate_half_bivariate_schur_interpolation_defect_formula` is a proved leaf.
In the saturated branch, full rank of any one coefficient-defect block pays
the full residual rank. The formula itself asserts no such rank bound. The
next task is to characterize failure of a single coefficient block without
depending on the chosen pivots.
