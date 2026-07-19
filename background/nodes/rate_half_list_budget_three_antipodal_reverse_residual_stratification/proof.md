# Proof

Centering the four pencil parameters gives

```text
product_i(U+c_iV)=U^4+e_2U^2V^2+e_3UV^3+e_4V^4.       (1)
```

The `c_i` are distinct, so they cannot all be zero. Their centered monic
quartic is `X^4+e_2X^2-e_3X+e_4`; consequently at least one of
`e_2,e_3,e_4` is nonzero and `q` is defined.

Use the reverse polynomials from the degree-floor theorem:

```text
B(z)=z^rU(z^-1),       C(z)=z^vV(z^-1),
E(z)=z^4D(z^-1).                                      (2)
```

Here `E(0)=B(0)=1` and `C(0)!=0`. Reversing the product identity gives

```text
E(B^4+e_2z^(2h)B^2C^2+e_3z^(3h)BC^3+e_4z^(4h)C^4)
 =1-z^d.                                             (3)
```

Put `H=EB^4-1`. By the definition of `q`, equation `(3)` shows that `H` has
exact order `qh` at zero: its leading coefficient there is
`-e_q C(0)^q`, which is nonzero. Also `qh<=4r=d-4<d`, so the binomial term
cannot interfere. Since the characteristic is zero or greater than `d`,
differentiation lowers this order exactly by one.

Direct differentiation gives

```text
H'=B^3K,       K=E'B+4EB'.                            (4)
```

As `B(0)=1`,

```text
ord_0 K=qh-1.                                         (5)
```

We now identify `K` in original coordinates. With `Y=z^-1`, differentiation
of `(2)` gives

```text
E'=4z^3D-z^2D',       B'=rz^(r-1)U-z^(r-2)U'.        (6)
```

Substituting `(6)` into `(4)` and using `d=4r+4` yields

```text
K(z)=z^(r+3) T(z^-1),                                (7)
```

with `T` exactly as in `(RRS3)`. The coefficient of `Y^(r+4)` cancels in
`T`, so `deg T<=r+3` and `(7)` is a polynomial identity. Equations `(5),(7)`
give

```text
deg T=r+3-(qh-1)=r+4-qh.
```

In particular `T` is nonzero and its degree is nonnegative. This proves
`(RRS4)` and the degree-floor consequence.

Let `alpha` be a root of `U`. Evaluation of `(RRS3)` gives

```text
T(alpha)=-4 alpha D(alpha)U'(alpha).                 (8)
```

Thus `(8)` vanishes whenever `alpha=0`, `D(alpha)=0`, or `U'(alpha)=0`.
The number of distinct such roots is at most `deg T`, proving `(RRS5)`.

Finally take `r=2^37-1`. On the generic minimum-degree boundary
`v=2^36-2`, one has `h=2^36+1` and

```text
r+4-2h=1.
```

On the intermediate minimum-degree boundary
`v=(2^38-4)/3`, one has `3h=2^37+1` and

```text
r+4-3h=2.
```

Equations `(RRS6),(RRS7)` now follow from `(RRS4),(RRS5)`. QED.
