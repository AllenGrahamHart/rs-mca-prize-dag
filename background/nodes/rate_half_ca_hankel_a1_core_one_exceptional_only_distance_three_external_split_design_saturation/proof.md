# Proof

The proved two-sided resultant identity on the exceptional-only face is

```text
product_(z:P(z)=0) Q(z;X)=c_t P_X(X)^e               (1)
```

for a nonzero scalar `c_t`. Every fiber is squarefree, so root
multiplicities may be compared directly.

The exceptional fiber contributes `A`. For the `e` internal slopes, let
`D_i` be the disjoint cancelled-pair polynomials. Their monic locators are

```text
B_T A/D_i.
```

Since the pairs partition `R_A`,

```text
product_i D_i=A.                                     (2)
```

The exceptional and internal locator product is therefore

```text
A product_i(B_T A/D_i)
 =A B_T^e A^e/product_iD_i
 =(A B_T)^e.                                         (3)
```

In particular every point of `S` occurs on the left side of `(1)` with
multiplicity exactly `e`. Hence every point of `S` is a root of `P_X`.

The residual domain has size `8e+7`, while the squarefree polynomial `P_X`
has `8e+6` residual-domain roots. It omits exactly one point. Since it
contains `S`, the omitted point `x_0` lies outside `S`, proving `(EDS2)`.

At a point outside `S`, only external locators contribute to the left side
of `(1)`. Comparison with the squarefree `e`th power on the right shows that
its external multiplicity is `e` when it is a root of `P_X`, and zero at the
unique omitted point. This proves `(EDS3)` and the biregular degrees in
`(EDS4)`.

Normalize every external locator to be monic. Equation `(EDS3)` says that
their product and `C^e` are monic polynomials with the same roots and the
same multiplicities, proving `(EDS5)`. Their degrees agree:

```text
3e(2e+1)=e(6e+3).
```

Finally `A`, `B_T`, and `C` are monic with disjoint root sets whose union is
the root set of `P_X`. Their total degree is

```text
2e+3+(6e+3)=8e+6=deg P_X.
```

This proves `(EDS6)` and completes the proof. QED.
