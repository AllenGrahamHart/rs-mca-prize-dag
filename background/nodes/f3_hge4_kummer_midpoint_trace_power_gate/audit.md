# Audit

1. The endpoint ratio is `x=v/u`, so swapping the ordered pair sends it to
   `x^(-1)`. The trace and `kappa` are symmetric under this swap.
2. The factor `8` in `(KTP1)` uses both `a=(v-u)/2` and
   `s=(u+v)/2`. Replacing it by `4` fails the endpoint identity.
3. The minus sign comes from the leading coefficient `uvw=-1` in
   `UVW=1-y^m`.
4. The exclusions `x=1,-1` are structural: the first makes the outside pair
   equal, while the second makes `deg S<h` and `kappa=0`.
5. Base-field splitting is used here in its stronger Kummer form: it supplies
   `alpha in F_p` with `alpha^m=kappa^(-1)`. Merely knowing that `S` splits as
   an arbitrary polynomial would not prove `(KTP2)`.
6. The power-test exponent is `(p-1)/m`, not `m` and not `(p-1)/2`.
7. The square-ratio corollary uses `p=1 (mod 8)`. It is automatic from the
   official `m|(p-1)` only because every retained dyadic level has `m>=8`.
8. The reduction to `mu_(m/2)` additionally requires `(p-1)/m` odd. For a
   proper exact level `m<n`, this quotient is even and the square gate is
   automatic on `mu_m`.
9. `(KTP3)` is a candidate test only. The trace does not determine a Belyi
   necklace or bound the number of primitive pencils above it.
10. No computation or empirical nonexistence claim enters the proof.
