# Audit - L1 m=4, h=3 Mason defect budget

1. The complement degree is `u=p+4`, not `p+3` or `p+5`.
2. Depression leaves a cubic `R^3+aR+b`; no quadratic term remains.
3. `D(0)!=0` because every domain point is nonzero.
4. Both summands in the reduced abc triple have exact valuation `3nu`.
5. The Frobenius-degenerate branch is excluded by the proved `h<m` arm; it
   is not silently discarded.
6. The Wronskian is nonzero: its vanishing would force the coprime reduced
   summands, and hence their monomial sum, into the excluded `p`th-power arm.
7. If `a=0`, distinct cubic roots imply `b!=0`; the Wronskian degree bound
   becomes negative, excluding this case. Direct Mason gives the independent
   impossible inequality `p-4+nu<=0`.
8. If `a!=0`, the second reduced summand has degree exactly
   `p+u-3nu`; lower terms cannot cancel its leader.
9. Comparing both forms of the Wronskian gives the nonzero eliminant
   `H=3XU'D+XUD'-LUD` with `deg H<=4-nu`.
10. `delta_A` uses `rad(UD)`, not the degree of `U^3D`; cubing creates no new
   radical roots.
11. The monomial's one radical root cancels the `-1` in Mason's bound.
12. The exact residual is `4-nu`, giving the same valuation ceiling and the
    defect budget.
13. Vanishing `delta_A` means that `U` is squarefree and coprime to the
    already-squarefree complement `D`.
14. The theorem is a compression, not an emptiness or counting result.
