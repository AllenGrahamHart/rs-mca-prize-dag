# DLI weight-five squared-root hypersurface router

- **status:** PROVED
- **closure:** proof
- **dependency:** `dli_wcl_odd_next_boundary_square_divisor_descent`
- **consumer:** `dli_wcl_slot_1_5_emptiness`

Let `K` be a field of odd characteristic containing an element `omega` of
exact order `512`, and put `U=<omega^2>=mu_256`. For a five-subset
`S={y_1,...,y_5}` of `U` with product one, write `e_j=e_j(S)` for its
elementary symmetric functions and put

```text
d=4e_2-e_1^2,
Psi(S)=(d^2-64e_4)^2-16384e_3+2048e_1d.              (SH1)
```

Then the following conditions are equivalent:

1. `S` is the set of squares of a normalized reduced weight-five relation
   `{rho_i}` in `mu_512`, with `product rho_i=1` and `sum rho_i=0`.
2. `Psi(S)=0`.
3. There are unique `c_1,c_0,b in K` such that, for
   `A(Y)=Y^2+c_1Y+c_0`,

```text
product_(y in S)(Y-y)=Y A(Y)^2-(bY+1)^2.             (SH2)
```

If square roots `x_i in mu_512` are chosen with `product x_i=1`, then the
same equation has the exact integral factorization

```text
Psi(x_1^2,...,x_5^2)
 = product_(s_i in {+1,-1}, product s_i=1)
     (s_1x_1+...+s_5x_5),                             (SH3)
```

on the torus `x_1...x_5=1`. Thus one squared-root row groups all 16
product-one sign lifts without losing or adding a relation.

For `U=mu_256`, multiplication by odd residues on exponent five-subsets of
sum zero has exactly

```text
34,412,301 normalized subsets,
   289,043 odd-dilation orbits.                        (SH4)
```

This is an exact reduction from the `2,296,920` signed affine-Galois classes
in the direct norm route. It does not prove emptiness: the norm of `(SH3)`
aggregates the sign-lift norms, so factoring one such aggregate is not a
certified shortcut through the remaining characteristic obstruction.
