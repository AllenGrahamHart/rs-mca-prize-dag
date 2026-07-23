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

which proves (OFG5)--(OFG6).

The coefficient constructions use only the fixed degrees `h,m`. Clearing
powers of `c`, `c-1`, and factorials at most `h` therefore gives a
bounded-degree system independent of the official exponent. The factors in
(OFG7) are nonzero on a survivor: `A`, `c`, and `c-1` are nonzero; the
order-one condition gives the penultimate coefficient; and all roots of `P`
are nonzero, so its `m`th-power resultant has nonzero constant term. A unit
saturation consequently excludes every possible survivor.

The reverse implication is not claimed. The bounded equations remember only
setwise Frobenius inversion and the necessary curve/torsion data. Thus every
retained component must pass the actual Frobenius equations, full cyclotomic
remainder, and inner lift listed in (OFG8).
