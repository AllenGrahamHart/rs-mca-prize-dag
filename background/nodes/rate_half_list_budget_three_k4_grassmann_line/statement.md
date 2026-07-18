# Budget-three K4 Grassmann-line compression

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Assume the canonical `K_4` incidence type with `d>=3` over a field of odd
characteristic. All six edge factors have exact degree one and distinct edge
roots. In the four-dimensional base-field vector space with basis
`e_0,...,e_3`, put

```text
B(X)=sum_(i<j) b_ij(X) e_i wedge e_j.                 (KGL1)
```

The Plucker identity is equivalent to `B(X) wedge B(X)=0`. There are three
linearly independent constant vectors `w,u,v in F^4` such that

```text
B(X)=w wedge (u+Xv).                                  (KGL2)
```

Thus the all-linear Plucker sextuple is a projective line on `Gr(2,4)`, not
an arbitrary six-tuple of edge locators.

Let `A=(A_0,A_1,A_2,A_3)` be the four block locators. The rank-two
parameterization from the Plucker gate becomes

```text
A(X)=alpha(X)w+beta(X)(u+Xv),
alpha,beta in F(X).                                   (KGL3)
```

If `lambda in F^4\{0}` annihilates the fixed three-space
`<w,u,v>`, then every coordinate of `lambda` is nonzero and

```text
lambda_0 A_0+lambda_1 A_1+lambda_2 A_2+lambda_3 A_3=0. (KGL4)
```

This relation has no vanishing proper subsum. Each `A_i` is monic,
pairwise coprime, fully split over its disjoint block `T_i`, and has degree
`d-2`. If

```text
E=J product_(i<j)e_ij,
```

then `deg E=2+6=8` and

```text
Lambda_D=E A_0A_1A_2A_3.                             (KGL5)
```

Consequently the official `K_4` branch is reduced to a nondegenerate
four-term base-field split-unit equation among four equal-degree, disjoint
divisors of the subgroup polynomial, with exactly eight exceptional roots.
This theorem does not prove that such a split-unit equation is absent.
