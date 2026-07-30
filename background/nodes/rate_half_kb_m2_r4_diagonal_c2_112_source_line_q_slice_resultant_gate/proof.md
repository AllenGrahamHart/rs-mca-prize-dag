# Proof

Work over the geometric closure and write the two distinct roots of `q` as
`r_1,r_2`. For either root `r`, the forced-square cut gives

```text
U(r,w)=V(r,w)=0.                                  (1)
```

This also holds at `w=0` by the complete-source ramification repair. Hence
the polynomial `G(r,W)` is divisible by `(W-w)^2`.

At each `k_i in K_mix`, the source fiber is unramified. Indeed, its image
`tau(k_i) in Omega` is unramified by squarefreeness of the colored divisor,
and the source-line lift `s` is an automorphism carrying the fiber over
`k_i` to that image fiber. Its two reduced stars are mixed `J_0-J_1` edges.
If `r` occurs in `m_(r,i)` of those two stars, the product formula

```text
G(r,W)=H(r,X)H(r,-X),       W=X^2                 (2)
```

makes `G(r,W)` vanish to order at least `m_(r,i)` at `k_i`. The saturated
defect classifier says that each root of `q` occurs exactly twice among all
four mixed stars, while each mixed fiber contains exactly two `J_1`
incidences. Therefore

```text
sum_i m_(r,i)=2,
sum_r m_(r,i)=2.                                  (3)
```

The degree of `G(r,W)` is at most four. It is not the zero polynomial: if
`G(r,W)=0`, then the product in `(2)` is zero in the polynomial domain, so
one of `H(r,X),H(r,-X)` is identically zero and `T-r` divides the actual
source component. This contradicts its reduced irreducible degree-two
source model. Equations `(1)--(3)` already supply four finite zeros counted
with multiplicity, so they exhaust the degree and give

```text
G(r,W) ~ (W-w)^2
          (W-k_1)^m_(r,1) (W-k_2)^m_(r,2).        (4)
```

The product formula for the resultant, followed by `(3)--(4)`, now gives

```text
Res_T(q,G)
 ~ product_(q(r)=0) G(r,W)
 ~ (W-w)^4 (W-k_1)^2 (W-k_2)^2,
```

which is `(KBQS-1)`.

In the aligned branch the two mixed common-`K` labels are the images under
`tau` of the two labels in `J_1`, so their locator is `tau^*q`. In the
near-aligned branch the colored quotient compiler gives
`Omega={xi,ell}` and `K_mix=tau(Omega)`, so its locator is
`tau^*chi_Omega`. This proves `(KBQS-2)`. QED.
