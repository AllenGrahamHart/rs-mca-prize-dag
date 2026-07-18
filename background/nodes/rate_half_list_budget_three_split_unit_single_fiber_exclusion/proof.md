# Proof

Let `Z_i` be the root set of `R_i`. Every `a in Z_i` is a root of
`X^d-tau_i`, so `a^d=tau_i`. Since the roots are simple, partial fractions
give

```text
1/R_i(X)=sum_(a in Z_i) 1/(R_i'(a)(X-a)).           (1)
```

Multiplying by `X^d-tau_i` and using `(SFE2)` yields

```text
A_i(X)=sum_(a in Z_i) V_a(X)/R_i'(a),
V_a(X)=(X^d-a^d)/(X-a)
      =X^(d-1)+aX^(d-2)+...+a^(d-1).               (2)
```

Put `Z=disjoint_union_(i in I) Z_i`, so `|Z|=C`. The vectors
`{V_a:a in Z}` are linearly independent when `C<=d`. Indeed, the first `C`
coefficients of a relation among them, from `X^(d-1)` down to `X^(d-C)`,
form the square Vandermonde system

```text
sum_(a in Z)mu_a a^j=0,       0<=j<C.
```

Its determinant is `product_(a<b)(b-a)`, nonzero because all removed points
are distinct. Hence every `mu_a` is zero.

Now suppose `sum_(i in I)lambda_i A_i=0`. Substitution of `(2)` gives the
coefficient `lambda_i/R_i'(a)` on `V_a` for `a in Z_i`. Independence makes
all these coefficients zero. Each derivative is nonzero and each `Z_i` is
nonempty, so every `lambda_i=0`. This proves the general claim.

The linear Grassmann atlas supplies the five displayed relation supports and
degree rows. Subtracting those degrees from `d` gives the printed deficits.
Every supported block has size at least `d-2`. If two such disjoint blocks
completed to the same `d`-point quotient fiber, their union would have size at
least `2d-4>d` for `d>=8`, a contradiction. Thus their completion fibers, and
hence their exceptional-root sets, are pairwise disjoint. Their deficit totals
are at most eight, so `(SFE3)` holds for every `d>=8`, including every official
instance. The atlas relations are nonzero, contradicting the independence
conclusion under `(SFE2)`. QED.
