# Audit

1. `P_delta` contains only actual support points outside `U`; padded heavy
   roots belong to `R_delta`, not to `P_delta`.
2. The size `|P_delta|=p+2` is independent of `r_delta` because the deficit
   is paid by the inside intersection.
3. On `X_delta`, the actual error vanishes, so the fixed-line residual is
   exactly the minimum word; this is where the circuit values enter.
4. The dual multiplier normalization is common over the domain and is
   absorbed only once into `kappa_delta`.
5. The derivative factorization `(12)` includes the contracted core factor
   `x-s_0`; omitting it gives the wrong source formula.
6. The padded factor appears in both sides of `(FBG5)` and cancels in
   `(FBG6)` because its roots are outside `U`.
7. The Hankel calculation alone gives an arbitrary numerator of degree at
   most `r_delta`; the minimum circuit is what identifies that numerator
   with `R_delta`.
8. Positive-deficit slopes are bounded by the sum of deficits, not assumed
   to have deficit one; the count `(FBG9)` remains valid in both arms.
