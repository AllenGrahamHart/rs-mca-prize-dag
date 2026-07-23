# Proof - L1 Mersenne HNF order-one Frobenius gate

The dependency proves the coefficient generating formula in (OFG1), the
order-one coefficient conditions, the divisibility of `P_(rho,c)` by
`W^n-1`, and `(c-1)^n=1`. This gives (OFG1)--(OFG2).

Put `d=c-1` and define `zeta=d^(p+1)`. Since `n=m(p+1)`,

```text
zeta^m=d^n=1.
```

In characteristic `p`, Frobenius gives

```text
c^p=(1+d)^p=1+d^p=1+zeta/d,                          (1)
```

proving (OFG3). Every coefficient of the truncated series `U_(rho,c)` is a
rational expression defined over the prime field, with denominators
invertible on the displayed chamber. Raising its vanishing top coefficient
to the `p`th power therefore gives (OFG4).

Let `x_1,...,x_h` be the distinct nonzero roots of `P_(rho,c)`, and put
`y_i=x_i^m`. The root formula for the resultant gives

```text
Q_(rho,c)(Z)=product_i(Z-y_i).                        (2)
```

Cyclotomic divisibility gives `y_i^(p+1)=1`, hence `y_i^p=y_i^(-1)`.
Frobenius on the coefficients of (2), using (OFG3), gives

```text
Q_(rho_star,c_star)(Z)=product_i(Z-y_i^(-1)).         (3)
```

As in the order-zero reciprocal gate,

```text
Z^hQ_(rho,c)(1/Z)
 =((-1)^h product_i y_i)product_i(Z-y_i^(-1))
 =C_(rho,c)Q_(rho_star,c_star)(Z),                    (4)
```

which proves the full degree-`h` reciprocal identity associated with (OFG5).

More precisely, the dependency identifies the zero split value with
`x_0=-1/d`. Since `m` is even, its `m`th power is `y_0=d^(-m)`. Equation
(1) gives

```text
y_0^p=(d^p)^(-m)=(zeta/d)^(-m)=d^m=y_0^(-1),
```

because `zeta^m=1`. Factor

```text
Q=(Z-y_0)Qtilde,       C=-y_0 Ctilde.
```

The full degree-`h` identity (4) has the factor `Z-y_0^(-1)` on both sides.
Cancelling it and then cancelling `-y_0` yields

```text
Ctilde Qtilde_star=Z^(h-1)Qtilde(1/Z),
```

which is the reduced identity printed in (OFG6). Thus the bounded system
need not carry the automatic zero-value factor.

The coefficient constructions use only the fixed degrees `h,m`. Clearing
powers of `c`, `c-1`, and factorials at most `h` therefore gives a
bounded-degree system independent of the official exponent. The factors in
(OFG7) are nonzero on a survivor: `rho`, `c`, and `c-1` are nonzero; the
order-one condition gives the penultimate coefficient; and all roots of
`L` are nonzero, so its `m`th-power resultant has nonzero constant term
`Ctilde`. A unit saturation consequently excludes every possible survivor.

The reverse implication is not claimed. The bounded equations remember only
setwise Frobenius inversion and the necessary curve/torsion data. Thus every
retained component must pass the actual Frobenius equations, full cyclotomic
remainder, and inner lift listed in (OFG8).
