# Audit

1. The congruence is modulo `y^c`, not `y^(c+1)`. The undetermined endpoint
   is exactly the scalar `lambda` in `(KMP1)`.
2. The inequality `c<2h` is equivalent to `e<h` and is load-bearing when
   replacing `D^(-1)` by `S^(-2)`.
3. The exponent in the modulo-`S` product is `2h+c=m`; changing `c` to the
   dual-gap endpoint gives the wrong twisted binomial.
4. The scalar is `kappa=1-a^2lambda`, with a minus sign. The root equation
   itself proves `kappa!=0`.
5. Uniform Kummer factor degree uses `mu_m subset F_q`. Without that
   hypothesis Frobenius can also act nontrivially on the root-of-unity factor.
6. The factor-degree ledger alone permits a nontrivial extension when `h` is
   even. The final `d=1` conclusion additionally consumes primitivity: the
   Frobenius multiplier would stabilize both outside members because `d|h`.
   Omitting either root-set stability or `eta^h=1` invalidates this step.
7. Base-field splitting does not mean that the midpoint roots lie in the
   original subgroup `mu_m`; they lie in one base-field Kummer torsor.
8. The result filters the retained Belyi necklaces but supplies no numerical
   orbit debit. It is an evidence edge into HGE4, not a status-changing
   requirement.
