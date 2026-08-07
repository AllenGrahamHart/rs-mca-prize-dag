# WCL `(1,6)` unsigned sign-product router

- **status:** PROVED
- **closure:** proof and exact Burnside count
- **consumer:** `dli_wcl_slot_1_6_emptiness`

Let `y_1,...,y_6` be distinct elements of `mu_256`. Choose square roots
`r_i` in `mu_512` and define

```text
Psi_6(y_1,...,y_6)
  = product_(epsilon_2,...,epsilon_6 in {+1,-1})
      (r_1+epsilon_2 r_2+...+epsilon_6 r_6).             (USR1)
```

Then:

1. `Psi_6` is independent of the chosen square roots. It is a symmetric
   polynomial in `Z[y_1,...,y_6]`, homogeneous of degree 16.
2. Over every field of odd characteristic, `Psi_6=0` if and only if one of
   the 32 global-sign classes of square-root lifts is a reduced signed
   weight-six relation.
3. If `K=Q(zeta_512)` and `K_0=Q(zeta_256)`, then

   ```text
   product_[epsilon] Norm_(K/Q)(sum_i epsilon_i r_i)
      = Norm_(K_0/Q)(Psi_6)^2.                           (USR2)
   ```

   Thus the aggregate norm has exactly the union of the prime supports of
   all 32 signed norms.
4. Affine Galois acts on the squared exponents by
   `x -> ax+b` on `Z/256`, with `a` odd. Exact Burnside enumeration gives

   ```text
   product exponent even:   6,025,357 orbits
   product exponent odd:    5,624,703 orbits
   total:                  11,650,060 orbits.            (USR3)
   ```

   The two sectors are invariant. They normalize respectively to
   `product y_i=1` and `product y_i=zeta_256`.

This is an exact factor-`15.928589...` quotient of the `185,569,028` signed
affine-Galois classes. It is a structural router, not a slot closure or a
promise of faster factorization: each unsigned norm aggregates 32 sign lifts
and can be substantially larger.
