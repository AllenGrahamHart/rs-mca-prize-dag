# WCL `(1,6)` even-norm divisor descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `dli_wcl_slot_1_6_emptiness`
- **dependency:** `dli_wcl_newton_short_window_exclusion`

Let `K` be a field of characteristic zero or characteristic greater than
`6`, containing `omega` of exact order `512`. For a reduced signed relation
put

```text
rho_i=s_i omega^e_i,       0<=e_i<256,
sum_(i=1)^6 rho_i=0.                                     (END1)
```

There are unique polynomials

```text
E(Y)=Y^3+e_2Y^2+e_1Y+e_0,
B(Y)=b_1Y+b_0                                             (END2)
```

such that the root locator is

```text
F(X)=product_i(X-rho_i)=E(X^2)-X B(X^2).                 (END3)
```

Put

```text
G(Y)=E(Y)^2-YB(Y)^2.                                     (END4)
```

Then

```text
G(Y)=product_i(Y-rho_i^2),
G(Y) divides Y^256-1.                                    (END5)
```

Conversely, every monic cubic `E` and polynomial `B` of degree at most one
over `K` satisfying `(END5)` reconstruct one reduced weight-six relation:
for every root `y` of `G`, put

```text
rho=E(y)/B(y).                                           (END6)
```

The denominator is automatically nonzero, `rho^2=y`, and the reconstructed
locator is `(END3)`. Thus `(1,6)` relations are in exact bijection with the
five-variable divisor problem `(END4)--(END5)`.

Divide `Y^256-1` by `G` and write its six remainder coefficients as

```text
R_j(e_0,e_1,e_2,b_0,b_1),       0<=j<=5.                (END7)
```

The integer ideal `I=(R_0,...,R_5)` has no characteristic-zero point.
Consequently there are a nonzero integer `Delta_6` and integer polynomials
`H_j` such that

```text
Delta_6=sum_(j=0)^5 H_jR_j.                              (END8)
```

Every finite characteristic supporting a slot `(1,6)` relation divides any
certified `Delta_6`. Computing and factoring such a certificate, followed by
the official field checks, is sufficient to close the slot. This theorem
does not compute `Delta_6` or promote the target.
