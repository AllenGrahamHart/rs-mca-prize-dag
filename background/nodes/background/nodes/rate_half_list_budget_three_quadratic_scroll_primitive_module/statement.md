# Budget-three quadratic scroll primitive module

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Retain the full-rank balanced basis

```text
A=alpha U+beta V,
U=U_0+XU_1,       V=V_0+XV_1,
C=(U_0,U_1,V_0,V_1) in GL_4(F).                    (QPM1)
```

For every quadratic B*=3 chamber with `d>=4`, the two generators are
coprime and have exact degrees

```text
                         deg alpha   deg beta
pendant                     d-2         d-1
quadratic K_4-e             d-2         d-2.        (QPM2)
```

Moreover

```text
<alpha,Xalpha> intersect <beta,Xbeta>={0},          (QPM3)
```

so the four entries of `C^(-1)A` are linearly independent over the base
field. In particular, the four block locators have no constant relation and
the full-rank scroll cannot secretly return to the split-unit class.

Writing the coordinates of `U,V` as affine-linear polynomials `u_i,v_i`
gives the exact primitive factorization

```text
A_i=u_i alpha+v_i beta,
Lambda_D=E product_(i=0)^3 (u_i alpha+v_i beta),     (QPM4)
```

where `deg u_i,deg v_i<=1`, their `4 x 4` coefficient matrix is invertible,
and `deg E=4` for pendant or `6` for quadratic `K_4-e`.

Thus each quadratic chamber is a coprime two-generator, four-moving-target
factorization of the official subgroup polynomial with exact generator
degrees. This theorem does not exclude such a factorization.
