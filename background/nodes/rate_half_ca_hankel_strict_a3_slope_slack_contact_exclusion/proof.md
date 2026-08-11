# Proof

Let `C:Q=0`, `G=X^N-1`, and
`H=product_(gamma in Z)(z-gamma)`. Exactly as in the first-endpoint pole
calculation, the ideal

```text
J=(H:G) subset O_C                                    (1)
```

has finite quotient of length at most

```text
sum_gamma(rho-u_gamma)=O<=delta.                      (2)
```

Indeed, over a supported fibre with local equation `h`, multiplication by
`g=G|_C` on `O_C/(h)` shows

```text
length(O_C/(h:g))
 =length(O_C/(h))-length(O_C/(h,g))
 <=rho-u_gamma.                                       (3)
```

The surface space `H^0(O(1,ell))` has dimension

```text
2(ell+1)>delta.                                       (4)
```

It therefore contains a nonzero biform `F` whose restriction lies in `J`.
The quotient

```text
s_G=FG/H in H^0(C,O_C(N+1,ell-T))                    (5)
```

is regular.

Let `s_F` be the universal contact section of
`L_F=O_C(-rho-3,e+1)`. Choose an irreducible component on which `s_F` is
nonzero. The degree of `L_F` on that component is nonnegative. Such a
component cannot have domain degree one: if its bidegree were `(1,e_i)`,
then

```text
deg L_F|_(C_i)=(e+1)-(rho+3)e_i<0.                    (6)
```

Hence the domain-degree-one form `F` does not contain this component, and
neither do `G` or `H`. Thus `s_G` is nonzero there and `s_F^3s_G` is a
nonzero global section.

Its line bundle is

```text
L_F^3 tensor O_C(N+1,ell-T)
 =O_C(rho-4,-e+ell+h+2),                              (7)
```

using `N=4rho+4` and `T=4e+1-h`. Under `(SSC3)`, the second coordinate in
`(7)` is negative. Restriction from the surface gives

```text
0 -> O(-4,-2e+ell+h+2)
  -> O(rho-4,-e+ell+h+2)
  -> O_C(rho-4,-e+ell+h+2) -> 0.                     (8)
```

The middle surface has no `H^0`. Both coordinates of the left term are
negative, so its `H^1` vanishes by Kunneth. The long exact sequence says the
curve line bundle in `(7)` has no section, a contradiction.

It remains to specialize the arithmetic. Since `m=2^37` is congruent to two
modulo three, write

```text
m=3q+2,       e=m+s,       0<=s<=q.                  (9)
```

Put `r=q-s`. Then

```text
e=4q+2-r,       delta=3r+1,       h<=4(q-r).         (10)
```

If `r>=1`,

```text
floor((3r+1)/2)<3r,
```

which makes `(SSC3)` hold even at the maximum allowed `h`. If `r=0`, then
`delta=1`, `ell=0`, and `(SSC3)` holds for every `h<=e-3`; the sole failure
is `h=e-2=4q`. At that point `rho=3e+1` and

```text
T=4e+1-(e-2)=3e+3=rho+2.
```

This is exactly `(SSC4)`. QED.
