# Budget-three fiber-two cycle quartic-pencil router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_multifiber_vandermonde_exclusion`,
  `rate_half_list_budget_three_antipodal_mobius_weld`,
  `rate_half_list_budget_three_antipodal_primitive_quotient_gate`,
  `rate_half_list_budget_three_antipodal_pencil_degree_floor`,
  `rate_half_list_budget_three_maximal_field_degree_collapse`

Work in a direct equal-complete-fiber four-cycle chamber over an odd field.
Write the block degree as `d=2s`, the domain size as `n=4d`, normalize the
domain polynomial to `X^(4d)-1`, and suppose the common fiber map is `X^2`.
Let `A_i` be the four pairwise-coprime degree-`d-1` block locators, let `E`
be the squarefree degree-four exceptional locator, and write

```text
E product_i A_i=X^(4d)-1.                             (F2C1)
```

For deleted roots `rho_i`, let `H_i(Y)` be monic of degree `s` and assume

```text
H_i(X^2)=(X-rho_i)A_i(X),
sum_i lambda_i A_i=0,       product_i lambda_i!=0.    (F2C2)
```

Then there are monic degree-`s-1` polynomials `G_i(Y)` such that

```text
H_i(Y)=(Y-rho_i^2)G_i(Y),
A_i(X)=(X+rho_i)G_i(X^2),                             (F2C3)

sum_i lambda_iG_i=0,
sum_i lambda_i rho_iG_i=0.                            (F2C4)
```

The four `rho_i` are automatically distinct. Let `c` be the number of
antipodal pairs among them; thus
`c in {0,1,2}`. There is a monic squarefree quartic `D_*(Y)`, all of whose
roots lie in the order-`2d` quotient subgroup, such that

```text
D_* product_i G_i=Y^(2d)-1.                           (F2C5)
```

More precisely, `D_*` has one root `rho_i^2` for every unpaired index, one
root for every antipodal index pair, and one root for every residual
antipodal pair in `Z(E)`. Hence

```text
c=0  ==>  D_*=product_i(Y-rho_i^2),                   (F2C6)
```

while `c=1,2` replace respectively one or two repeated coefficient-square
roots by exceptional-pair squares.

The `G_i` are pairwise coprime and, for `s>=2`, span a two-dimensional
base-field pencil. There are independent `R,S` of degree at most `s-1`,
nonzero scalars `mu_i`, and `kappa!=0` such that

```text
G_i=mu_i(R+rho_iS),
D_* product_i(R+rho_iS)=kappa(Y^(2d)-1).              (F2C7)
```

The reduced rational map `-R/S` has degree exactly `s-1` and is neither a
nontrivial dyadic cyclic nor dihedral pullback. If the characteristic exceeds
`2d`, the degree-drop direction `V` in a monic pencil basis satisfies

```text
deg V>=ceil((s-5)/2).                                 (F2C8)
```

In the `c=0` stratum, `(F2C6)--(F2C7)` are exactly the existing antipodal
quotient-pencil norm equation under

```text
d_ant=2d=4s,       a_i=rho_i,       b_i=rho_i^2.      (F2C9)
```

Its direct four-coset partition is therefore excluded as well. The
`c=1,2` strata are explicit **denominator-mismatch** quartic pencils and are
not covered by that matched norm equation.

At the prize maximum,

```text
d=2^39,       2d=2^40,       s=2^38,
deg(-R/S)=2^38-1,       deg V>=2^37-2.               (F2C10)
```

Thus every direct common-`X^2` four-cycle case has a primitive quartic-pencil
normal form at the next dyadic order. The matched `c=0` branch embeds in the
existing antipodal census; the `c=1,2` mismatch branches remain separate.
The theorem proves none of these censuses empty and does not cover mixed maps,
partial fibers, or primitive locators outside the direct completion model.
