# WCL `(4,9)` quartic-divisor descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `dli_wcl_slot_4_9_emptiness`
- **dependency:** `dli_wcl_newton_short_window_exclusion`

Let `K` be a field of characteristic zero or characteristic greater than
`9`, containing `omega` of exact order `2048`. For a reduced signed
weight-nine relation put

```text
rho_i=s_i omega^e_i,       0<=e_i<1024,
p_j=sum_i rho_i^j.                                      (QDD1)
```

Assume

```text
p_1=p_3=p_5=p_7=0.                                    (QDD2)
```

Let `a_9=product_i rho_i`. Since `9^(-1)=1593 mod 2048`, there is a unique
common dilation

```text
lambda=a_9^(-1593) in mu_2048                         (QDD3)
```

for which the normalized roots `lambda rho_i` have product one. Dilation
preserves reducedness and `(QDD2)`.

There is then a unique monic quartic

```text
A(Y)=Y^4+c_3Y^3+c_2Y^2+c_1Y+c_0                       (QDD4)
```

such that the normalized root locator is

```text
F(X)=product_i(X-lambda rho_i)=X A(X^2)-1.             (QDD5)
```

Put

```text
G(Y)=Y A(Y)^2-1.                                      (QDD6)
```

Then

```text
G(Y)=product_i(Y-(lambda rho_i)^2),
G(Y) divides Y^1024-1.                                (QDD7)
```

Conversely, every monic quartic `A` over `K` satisfying the divisibility in
`(QDD7)` reconstructs one normalized reduced relation satisfying `(QDD2)`:
for every root `y` of `G`, put

```text
rho=A(y)^(-1).                                        (QDD8)
```

Then `rho^2=y`, the nine reconstructed roots are distinct and nonantipodal,
their product is one, and their first four odd power sums vanish. Thus
common-dilation orbits of `(4,9)` relations are in bijection with the monic
quartics in `(QDD7)`.

This gives a fixed characteristic-only elimination endpoint. Divide
`Y^1024-1` by the monic degree-nine polynomial `G` and write

```text
(Y^1024-1) mod G=sum_(j=0)^8 R_j(c_0,c_1,c_2,c_3)Y^j. (QDD9)
```

The `R_j` lie in `Z[c_0,c_1,c_2,c_3]`. The ideal

```text
I=(R_0,...,R_8)                                       (QDD10)
```

has no characteristic-zero point. Consequently there is a nonzero integer
`Delta` and polynomials `H_j` over `Z` such that

```text
Delta=sum_(j=0)^8 H_j R_j.                            (QDD11)
```

Every finite characteristic supporting a `(4,9)` relation divides any such
certified `Delta`. Computing and factoring one certificate, then checking
its characteristics against the official field constraints, is sufficient
to close the slot. This theorem does not compute `Delta` or prove the slot
empty.
