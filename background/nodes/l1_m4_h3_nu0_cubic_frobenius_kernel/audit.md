# Audit - L1 m=4, h=3, nu=0 cubic Frobenius kernel

1. The multiplier is `X^(p-4)` and is nonnegative for every official prime.
2. The domain degree becomes exactly `5p`, so its derivative vanishes.
3. The only forbidden integration slots are `p-1` and `2p-1`; Cartier pays
   both through source degrees `4` and `p+4`.
4. Canonical integration removes every degree divisible by `p` from `J`.
5. The perfect-field Frobenius kernel has degree five and zero constant term.
6. The companion term has degree exactly `3p`, while `deg J<3p`; hence the
   residual kernel is cubic with nonzero leader.
7. `Q=X^5-A` automatically has no quartic term because `A` is monic.
8. `q_3^p=a` uses the leading coefficient of `B_0`, not an unproved choice
   of a `p`th root.
9. `ord_0(J)=p-4` uses `H(0)!=0`; without the Euler node it would not follow.
10. The degree-`p-4` comparison is below every positive degree in `A^p` and
    correctly uses `(p-4)^(-1)=-1/4` in `F_p`.
11. A three-scalar kernel is structural compression, not a finite solution
    count because `J` still depends on `R^2H`.
