# Audit - L1 official first-checkpoint split-pencil reduction

1. The classification assumes exactly `t=p` and `p<=d<=2p-2`.
2. For nonconstant `R` of degree below `p`, `R'` has degree exactly one less;
   this is where the minimum-width degree matters.
3. The term `F_XR'` is one degree above `F_X'R`, so its leader cannot cancel.
4. The converse uses the Wronskian degree to recover moment equality; it does
   not assert full elementary-prefix equality.
5. At terminal depth, squarefreeness forces the linear coefficient nonzero.
6. A smooth domain may be a multiplicative coset; ratios land in its
   underlying subgroup.
7. If the scaled affine-line offset were in `F_p`, the line would contain
   zero and could not lie in the domain.
8. Off-diagonal ratio injectivity uses only linear independence of `1,c`.
9. The terminal exclusion uses both `p>=3583` and `11n<=256p`.
10. No computation or probabilistic estimate is load-bearing.
11. The deep-band ratio argument chooses the nonzero one of the two distinct
    fiber values; otherwise the scaling polynomial could vanish identically.
12. For nonidentity `lambda`, `lambda^p!=1` because the smooth subgroup has
    power-of-two order and `p` is odd.
13. The ratio count separates the `p` diagonal pairs before applying the
    degree-`r_d` multiplicity bound.
14. The row endpoint is the strict integer cutoff
    `floor((p(p-1)-1)/(n-1))`; omitting either minus one can admit the equality
    case `|X/X|=n`.
15. `floor(11(p-1)/256)` is only the uniform corollary; contributor pruning
    must use the stronger row-dependent endpoint.
