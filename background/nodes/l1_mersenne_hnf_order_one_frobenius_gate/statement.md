# L1 Mersenne HNF order-one Frobenius gate

- **status:** PROVED
- **dependency:** `l1_mersenne_next_to_maximal_hypergeometric_normal_form`
- **consumer:** `l1_mixed_petal_amplification`

Consider the `ord_0(T)=1` chamber of the dependency. Put

```text
rho=2A/[c(c-1)],
U_(rho,c)(t)=(1-t)^(c rho)(1-ct)^(-rho),
g_(rho,c)(y)=sum_(r=0)^h [t^r]U_(rho,c)(t)y^(h-r),
P_(rho,c)(W)=(c-1)^(-h)g_(rho,c)(1+(c-1)W).          (OFG1)
```

All generalized-binomial series are truncated through degree `h<p`. The
order-one and cyclotomic conditions are

```text
[t^h]U_(rho,c)=0,       [t^(h-1)]U_(rho,c)!=0,
P_(rho,c) | W^(m(p+1))-1,       (c-1)^(m(p+1))=1.    (OFG2)
```

Put `d=c-1`. Every survivor has one `zeta in mu_m` such that

```text
zeta=d^(p+1),       c^p=c_star:=1+zeta/d.            (OFG3)
```

Let `rho_star` stand for `rho^p`. Frobenius preserves the order-one curve:

```text
[t^h]U_(rho_star,c_star)=0.                           (OFG4)
```

Define

```text
Q_(rho,c)(Z)=Res_W(P_(rho,c)(W),Z-W^m),
C_(rho,c)=Q_(rho,c)(0).                              (OFG5)
```

Every survivor satisfies the reciprocal identity

```text
C_(rho,c)Q_(rho_star,c_star)(Z)
  =Z^h Q_(rho,c)(1/Z).                               (OFG6)
```

After substituting `c_star=1+zeta/(c-1)`, clearing the fixed denominators,
and adjoining `zeta^m-1`, equations (OFG2), (OFG4), and the coefficient
equations in (OFG6) form a bounded-degree algebraic system depending only on
`m,h`. Saturate by

```text
rho*c*(c-1)*[t^(h-1)]U_(rho,c)*C_(rho,c).            (OFG7)
```

A verified unit saturation closes the complete order-one chamber before any
degree-`n` remainder or inner lift. A retained component is only a necessary
candidate and must still satisfy

```text
rho_star=rho^p,       (c-1)^(p+1)=zeta,
P_(rho,c)|W^n-1,      and the inner equations.        (OFG8)
```

This gate does not assert that the bounded system is empty, treat order zero
or lower `h`, or promote L1.
