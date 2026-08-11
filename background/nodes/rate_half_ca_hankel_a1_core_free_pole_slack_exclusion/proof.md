# Proof

Let `C:Q=0`, let `G` be the degree-`N` domain locator, and put

```text
H=product_(gamma in Z)(z-gamma),       J=(H:G) in O_C.
```

The fibrewise multiplication argument for `G` gives

```text
p=length(O_C/J)<=sum_gamma(rho-u_gamma)=O.            (1)
```

The surface space `H^0(O(alpha,b))` has dimension

```text
(alpha+1)(b+1)>p.                                     (2)
```

Therefore it contains a nonzero form `F` whose restriction lies in `J`, and

```text
s_G=FG/H in H^0(C,O_C(N+alpha,b-T))                  (3)
```

is regular.

Choose a component `C_i` on which the contact section `s_F` is nonzero, and
write its bidegree as `(r_i,e_i)`. The contact line bundle has nonnegative
degree there:

```text
(e+1)r_i-(rho+1)e_i>=0.                              (4)
```

The form `F` cannot contain `C_i`. For `alpha=2`, the range in `(A1P2)`
makes the right side of `(4)` negative whenever `r_i<=2`. For `alpha=1`,
`e<rho` makes it negative whenever `r_i<=1`. For `alpha=0`, a form with no
`X` degree cannot contain a mixed component. Neither `G` nor `H` contains
`C_i`. Hence `s_G` is nonzero on `C_i`, and `s_F^3s_G` is a nonzero global
section.

Using `N=4rho` and `T=4e-ell`, its line bundle is

```text
O_C(rho+alpha-3,b-e+ell+3).                           (5)
```

Under `(A1P3)` the second coordinate is negative. The restriction sequence
for the bidegree-`(rho,e)` curve is

```text
0 -> O(alpha-3,b-2e+ell+3)
  -> O(rho+alpha-3,b-e+ell+3)
  -> O_C(rho+alpha-3,b-e+ell+3) -> 0.                (6)
```

The middle surface has no sections. In the left term both coordinates are
negative, and the first is one of `-1,-2,-3`; Kunneth therefore gives zero
`H^1`. The curve line bundle in `(5)` has no section, contradicting the
nonzero product. This proves `(A1P3)`.

If `(A1P3)` fails, then

```text
floor(p/(alpha+1))>=e-ell-3,
```

which gives `(A1P4)`. At `e=m+1`, the slope ledger gives
`ell<=4e-rho-2=2`, `alpha=2`, and `Delta=3m-1`. Substitution yields
`(A1P5)`. QED.
