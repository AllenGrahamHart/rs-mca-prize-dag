# Proof - L1 m=4, h=3, nu=2 fixed-point certificate

Write `p=2^r-1`, so `n=2^(r+2)`. Direct reduction gives

```text
p^2=1+2^(r+1) mod n,       p^4=1 mod n,
ord_n(p)=4,                gcd(n,p-1)=2.              (1)
```

The normalized domain coset `C` is Frobenius-stable. The root set `X_c` of
the fixed split fiber `R_0-c` is also Frobenius-stable and has odd size `p`.
Every Frobenius orbit in `C` has length dividing four, so `X_c` has an odd
number of fixed points. On the other hand, a multiplicative coset contains
either zero or exactly `gcd(n,p-1)=2` prime-field points. Hence `X_c` has
exactly one prime-field root; call it `x`. The two prime-field points of `C`
are `x` and `-x`.

The polynomial `R_0-c` is monic of odd degree `p` and has constant term
`-c`, so the product of all roots in `X_c` is `c`. Since `C=xK`, write each
root as `xk_j` with `k_j in K`. Then

```text
c=product_(z in X_c) z=x^p product_j k_j
 =x product_j k_j.
```

Thus `c/x` lies in both `K` and `F_p^*`. Their intersection is `{1,-1}` by
(1), proving `x=epsilon c`. Since `-1 in K`, this also proves
`C=xK=cK` and `A=c^n`, which is `(FPC2)`.

The other point `-x` cannot lie in either conjugate split fiber, whose values
are not in `F_p`, and it cannot lie in `X_c` because `x` is its unique fixed
point. The exact factorization in `(FPC1)` therefore forces
`D_0(-x)=0`. This proves `(FPC3)` and also shows that exactly one sign works.

It remains to translate the fixed-root equation. Since `sum_i e_i=p` is odd,

```text
S_e(0)=product_i (-d_i^(-1))^(e_i)=-w^(-1),
c=4/(3w).                                             (2)
```

The equation `R_0(epsilon c)=c` is equivalent to

```text
S_e(epsilon c)/S_e(0)=-1/3.
```

Substitute (2) and divide each factor by its value at zero:

```text
product_i (1-4 epsilon d_i/(3w))^(e_i)=-1/3.          (3)
```

Multiplying by `(3w)^p=3w` in `F_p` turns (3) into `(FPC4)`. No converse is
used: the equation is only a necessary residue test for a multiplicity
triple already supplied by the Belyi theorem.

Finally substitute `Z=cW` into the normalized factorization. Since
`c^p=c`, the Belyi product becomes

```text
R_0(cW)/c
 =S_e(cW)/c-S_e(0)/c
 =product_i (W-(cd_i)^(-1))^(e_i)+3/4
 =F_e(W).                                              (4)
```

Equation (2) gives `(cd_i)^(-1)=3w/(4d_i)=q_i`. Also

```text
g_0(cF_e)=c^3(F_e^3-2F_e+1),
(cW)^n-c^n=c^n(W^n-1).
```

Dividing by `c^n` proves `(FPC6)` with the definition in `(FPC5)`. Its
leading coefficient is one because
`c^(3-n)D_0(cW)` has leading coefficient `c^(3-3p)=1` in `F_p`. Scaling
`(FPC3)` by `c` gives the two evaluations in `(FPC6)`.
