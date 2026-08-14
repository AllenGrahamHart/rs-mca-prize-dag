# Cycle 314: MCA rank-11 absorbing clone collapse (2026-08-14)

The new PROVED node
`rate_half_mca_rank11_relative_absorbing_clone_affine_collapse` classifies
the full-evaluation-rank half of Cycle 313's component residual.

Let `B` be an evaluation basis of the absorbing correction space `W`. The
polynomial clone curve has coefficients `P_(B,j) in W`. On `B`, the degree
`j>=2` coefficient equation is

```text
H_j+P_(B,j)=0.
```

Both terms lie in `W`, and evaluation on `B` is injective. Therefore

```text
P_(B,j)=-H_j
```

as codewords, for every `j>=2`. All high coefficients cancel globally and
the clone curve is one affine codeword owner line `A+ZB`. Residual
support-wise badness then gives

```text
one component <= n'-m'+1=R-d+1=981105 slopes.
```

This deletes genuinely nonlinear absorbing clone components. It does not
sum multiple affine owners: the live residual is evaluation rank-flats plus
owner chronology/compatibility.

Focused verification:

```text
RATE_HALF_MCA_RANK11_RELATIVE_ABSORBING_CLONE_AFFINE_COLLAPSE_PASS
  owner_cap=981105 routes=2 controls=5/5
RATE_HALF_MCA_RANK11_RELATIVE_ABSORBING_CLONE_AFFINE_COLLAPSE_AUDIT_PASS
  owner_cap=981105 routes=2 controls=4/4
```

No numerical experiment or Modal computation was used.

```text
start:                   c64327c16
DAG delta:               +1 PROVED clone-to-affine collapse,
                         +1 requirement edge, +1 evidence edge
critical status delta:   none
upstream terminal delta: nonlinear H_C clones deleted
delta-star movement:     none
compute:                 exact coefficientwise linear algebra only
next route action:       attack evaluation rank-flats and compatibility
                         across the resulting affine owners
```
