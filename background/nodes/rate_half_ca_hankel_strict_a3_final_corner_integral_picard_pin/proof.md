# Proof

The pole-ideal calculation gives

```text
d=length(O_C/(H:G))<=O<=1.                            (1)
```

The surface space `H^0(O(d,0))` has dimension `d+1>d`. Hence it contains a
nonzero biform `F` whose restriction belongs to `(H:G)`, and

```text
s_G=FG/H in H^0(C,O_C(N+d,-T))                       (2)
```

is regular.

The contact theorem gives a nonzero section `s_F` of `L_F`. Choose a
component `C_i` on which it is nonzero, and write its bidegree as `(r_i,e_i)`.
Then

```text
deg L_F|_(C_i)=(e+1)r_i-(rho+3)e_i>=0.               (3)
```

In particular `r_i!=1`, because the right side would be at most
`e+1-(rho+3)<0`. Thus the domain-degree-`d<=1` form `F` does not contain
`C_i`; neither do `G` or `H`. The product `s_F^3s_G` is therefore nonzero.

Using `N=4rho+4`, `T=3e+3`, and `rho=3e+1`, its line bundle is

```text
L_F^3 tensor O_C(N+d,-T)=O_C(rho-5+d,0).             (4)
```

Restriction from the surface gives

```text
0 -> O(-5+d,-e)
  -> O(rho-5+d,0)
  -> O_C(rho-5+d,0) -> 0.                            (5)
```

Both coordinates of the left term are negative. Its `H^0` and `H^1`
vanish by Kunneth, so every section in `(4)` is the restriction of a unique
univariate section `A_d(X)`. This proves `(FCP5)`.

The nonzero polynomial `A_d(X)` restricts nontrivially to every component of
`C`, because every component has positive parameter degree and therefore
cannot divide an `X`-only polynomial. Equation `(FCP5)` consequently makes
`s_F` nonzero on every component.

For each component put

```text
a_i=4e_i-r_i.
```

Since `sum e_i=e` and `sum r_i=rho=3e+1`,

```text
sum_i a_i=e-1.                                        (6)
```

The degree of `L_F` on `C_i` is now

```text
l_i=e e_i-(e+1)a_i.                                  (7)
```

Every `l_i` is nonnegative because `s_F|_(C_i)` is nonzero, and their sum is
the total degree `delta=1`. If `l_i=0`, coprimality of `e` and `e+1` would
make `e+1` divide `e_i`, impossible for `1<=e_i<=e`. Thus every component
has `l_i>=1`. Their sum can equal one only if there is a single component.
The curve is therefore absolutely irreducible.

For that component `(7)` equals one. Reducing modulo `e+1` gives
`e_i=e`, then `(7)` gives `a_i=e-1` and `r_i=3e+1=rho`, consistently.
Finally a nonzero section of the degree-one line bundle `L_F` on the
integral projective curve has an effective Cartier divisor of degree one.
Over the algebraic closure it is one point `P_*`, proving `(FCP3)`. QED.
