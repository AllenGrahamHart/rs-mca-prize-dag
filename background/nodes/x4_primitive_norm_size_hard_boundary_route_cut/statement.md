# X4 primitive norm-size hard-boundary route cut

- **status:** PROVED
- **closure:** route cut

At the official rate-half scale put

```text
N=2^41,       e=N/8,       T=t_XR,       d=e-T-1.
```

The exact corridor gives `T<=N/128-2`, so this is a valid cell in the
Johnson-nonpositive residual wedge.  Let `J` be all prefix-supplied dyadic
levels, and partition any coefficient-primitive fold pattern as
`J=S disjoint-union Z`, with `0 in S`.

For every official finite field `F_q`, `log2(q)<256`, the complete generic
norm-size lower factor from
`x4_primitive_shiftpair_zero_fold_norm_divisibility` satisfies

```text
log2(2^(|S|+T_2(S,Z)) p^R_S) <3N+5160,              (RC-1)
```

whereas its shared Haar ceiling satisfies

```text
log2((eN/A_S)^A_S)>=10N.                            (RC-2)
```

Hence the strengthened active/zero pattern inequality holds for every
possible pattern at this cell.  No pattern is excluded by the generic
residue-degree, structural-zero, and Haar-energy size comparison.

This is not an actual shift-pair construction and does not falsify X4.  It
proves that this norm-size route alone cannot close the residual wedge.  Any
continuation at the hard boundary must use exact norm factors/common ideals,
locator incidence, or operational first-owner structure.
