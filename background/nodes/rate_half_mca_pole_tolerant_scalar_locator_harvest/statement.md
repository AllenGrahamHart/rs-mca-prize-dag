# Pole-tolerant scalar-locator localization

- **status:** PROVED
- **source:** upstream
  `experimental/notes/m2/pole_tolerant_scalar_locator_localization.md`
- **scope:** coherent scalar-locator certificates over an arbitrary finite
  field and evaluation domain

Let `G_Q` be the algebraic coincidence core of a scalar-locator certificate.
Without assuming that `Q` is root-free on the domain:

1. every coordinate outside `G_Q` occurs in at most one selected support;
2. if `g=|G_Q|<m`, then
   `|I| <= floor((n-g)/(m-g)) <= n-m+1`;
3. if `g>=m`, then
   `|I| <= n-g+B^MCA_{F,G_Q,k,Gamma}(m)`;
4. at `g=m`, the punctured numerator is at most one.

For exact monic support locators, delete the at most one slope where
`c_0+c_1 gamma=0`. Let `P` be the domain points at which `Q=A=B=0`, and let
`R` be their squarefree domain locator. Every remaining support contains
`P`; `R` divides `Q,A,B` and every support locator; and division by `R`
preserves the exact certificate, support-locator normalization, degree
profile, and coincidence core on `D\P`.

No claim is made that support-wise MCA nontriviality survives this
cancellation.
