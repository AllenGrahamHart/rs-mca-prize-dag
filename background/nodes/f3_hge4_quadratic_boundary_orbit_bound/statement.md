# HGE4 quadratic-boundary orbit bound

- **status:** PROVED
- **consumer:** `f3_hge4_norm_gate_count`
- **dependency:** `f3_hge4_boundary_defect_trace_pin`

Let `m=3h+2` be dyadic with `h>2`, and let the field contain `mu_m` and have
characteristic zero or characteristic greater than `4h+1`. Fix a generator
`omega` of `mu_m`. Every ordered scaling orbit at the `e=2` exact-ratio
boundary has a representative with

```text
P(0)=epsilon in {1,omega},
x=Q(0)/P(0) in mu_m\{1},
d=epsilon(x-1),
c_2=b-2a^2=(1+x)/(epsilon^3 x(x-1)^2).              (QBO1)
```

Put

```text
F_(a,c_2)(y)=(1-3ay-3c_2y^2)^(-1/3)
             =sum_(j>=0) f_j(a,c_2)y^j.             (QBO2)
```

Then the normalized reciprocal locator is forced below its constant term:

```text
y^hP(1/y)=F_(a,c_2)(y) mod y^h,                     (QBO3)
```

and the two endpoint equations are

```text
f_h(a,c_2)=epsilon(1+x)/2,
f_(h+1)(a,c_2)=0.                                   (QBO4)
```

For fixed `(epsilon,x)`, the second polynomial in `(QBO4)` has degree exactly
`h+1` in `a`. Consequently

```text
E_h^prim(m,p)<=2(m-1)(h+1)
               =2(m^2-1)/3 <(2/3)m^2.              (QBO5)
```

Thus the entire `e=2` exact-level width is analytically paid. The equations
are necessary, not sufficient, and no claim is made for `e>=4`.
