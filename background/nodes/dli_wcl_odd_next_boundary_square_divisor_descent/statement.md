# WCL odd next-boundary square-divisor descent

- **status:** PROVED
- **closure:** proof
- **consumers:** `dli_wcl_slot_1_5_emptiness`,
  `dli_wcl_slot_2_7_emptiness`
- **dependency:** `dli_wcl_newton_short_window_exclusion`

Take one row of the table

```text
ell   w=2ell+3   N     ord(omega)=2N   w^(-1) mod 2N
 1         5     256          512             205
 2         7     512         1024             439.       (OND1)
```

Let `K` be a field of characteristic zero or characteristic greater than
`w`, containing `omega` of exact order `2N`. For a reduced signed relation
put

```text
rho_i=s_i omega^e_i,       0<=e_i<N,
p_j=sum_i rho_i^j,         p_1=p_3=...=p_(2ell-1)=0.    (OND2)
```

Let `a_w=product_i rho_i` and let `nu` be the inverse in `(OND1)`. The
unique common dilation

```text
lambda=a_w^(-nu) in mu_(2N)                             (OND3)
```

makes the normalized root product one. There are then a unique monic
polynomial `A` of degree `ell+1` and a unique scalar `b` such that

```text
F(X)=product_i(X-lambda rho_i)
    =X A(X^2)-bX^2-1.                                  (OND4)
```

Define

```text
G(Y)=Y A(Y)^2-(bY+1)^2.                                (OND5)
```

Then

```text
G(Y)=product_i(Y-(lambda rho_i)^2),
G(Y) divides Y^N-1.                                    (OND6)
```

Conversely, every monic degree-`ell+1` polynomial `A` and scalar `b` over
`K` satisfying `(OND6)` reconstruct one normalized reduced relation by

```text
rho=(by+1)/A(y)                                        (OND7)
```

at every root `y` of `G`. Thus common-dilation orbits of the two WCL slots
are in exact bijection with the following fixed divisibility problems:

```text
(1,5): deg A=2,   Y A^2-(bY+1)^2 divides Y^256-1;
(2,7): deg A=3,   Y A^2-(bY+1)^2 divides Y^512-1.      (OND8)
```

For each row, divide `Y^N-1` by `G` and let `R_0,...,R_(w-1)` be the
remainder coefficients. They are integer polynomials in the `ell+1`
nonleading coefficients of `A` and in `b`. The ideals

```text
I_ell=(R_0,...,R_(w-1))                                (OND9)
```

have no characteristic-zero points. Hence there are nonzero integers
`Delta_ell` and integer polynomials `H_(ell,j)` with

```text
Delta_ell=sum_(j=0)^(w-1) H_(ell,j)R_j.                (OND10)
```

Every finite characteristic supporting the corresponding WCL relation
divides any certified `Delta_ell`. Computing, factoring, and applying the
official field constraints to these two integers can close both slots. This
theorem computes neither integer and does not promote either target.
