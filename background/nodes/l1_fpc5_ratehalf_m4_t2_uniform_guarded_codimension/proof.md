# Proof: rate-half FPC5 uniform guarded codimension

Let `P_s` be the `(s+1)`-dimensional space of polynomials of degree at most
`s`. The congruence map in (UC2) is

```text
T:P_s x P_s -> K[X]/(L_R),
T(A_1,A_2)=c_2L_1A_1-c_1L_2A_2 mod L_R.              (1)
```

The source background and petals are disjoint, so `L_1` is a unit modulo
`L_R`. Restricting (1) to the first cofactor block gives multiplication by a
unit after evaluation of `P_s` on the `r` distinct roots of `L_R`. That
evaluation map has rank `min(r,s+1)`: a nonzero degree-at-most-`s` polynomial
cannot vanish at more than `s` distinct points, and interpolation attains the
full smaller dimension. Hence

```text
rank T>=min(r,s+1),
dim ker T<=2s+2-min(r,s+1).                           (2)
```

The map from `(A_1,A_2)` to `F` in (UC3) is injective. If `F=0`, then
`L_1A_1=L_2A_2`. Coprimality gives `L_1|A_2`, but `deg A_2<ell`; hence
`A_2=0`, and similarly `A_1=0`. The guarded locator image has the same
dimension as `ker T`, proving (UC4).

The vector space of degree-at-most-`d` polynomials has dimension `d+1`.
Whenever the leading-coefficient functional on `V_F` is nonzero, passing to
its monic fiber subtracts one dimension from both the flat and ambient
spaces, so the affine codimension is still `(d+1)-dim V_F`. If the functional
is zero, the degree-`d` split cell is empty. Substituting `d=ell+s` in (2)
gives the first inequality in (UC5). Under (UC1), either `r=s`, when
`min(r,s+1)=s`, or `r>=s+1`, when it equals `s+1`. This proves the final
bound and (UC6). In the case `r=s`, the target of (1) has dimension `s`, so
the rank lower bound is equality and `dim V_F=s+2` exactly.

For the aggregate statement, the unguarded two-petal theorem already proves
that `F` determines a unique `W_F`. Every exact contributor has a unique
background agreement set

```text
R={x in B:W_F(x)=0}
```

and the list threshold gives `|R|>=s`. Its defect locator is monic, degree
`ell+s`, and split on `C`, proving the injection into (UC7). The remaining
conditions only filter that locus. Uniqueness of `R` makes the exact cells
disjoint, but does not bound how many different sets occur; no union bound is
asserted. QED.
