# H3 global product/quotient resultant compression

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half` (evidence/router)
- **dependency:** `f3_h3_global_derivative_ideal_valuation`

Let `n=2^s`, `s>=2`, let `zeta=zeta_n`, and put

```text
c_a=1-zeta^a,       1<=a<n,
d=n-1,              N=d^2,
F_n(X)=product_(a=1)^(n-1)(X-c_a).
```

Then the complete shifted-root polynomial is the explicit binomial
polynomial

```text
F_n(X)=((1-X)^n-1)/X in Z[X].                    (GRC1)
```

The ordered shifted-product polynomial used by the global derivative ideal
has the exact resultant representation

```text
Pcal_n(T)=product_(a,b)(T-c_a c_b)
         =Res_X(F_n(X),X^d F_n(T/X)).             (GRC2)
```

The cleared nonidentity quotient polynomial from the double-accident
derivative ideal similarly satisfies

```text
Q_n(T)=product_(a!=b)(c_a T-c_b)
      =Res_X(F_n(X),F_n(TX))/(n(T-1)^d).          (GRC3)
```

Finally fix ordered nonidentity quotient exponents `(u,v)`, and write
`C=c_u`, `D=c_v`. The integral derivative packet

```text
G_uv(U)=C^N Pcal_n(D/C+U)
       =product_(a,b)(D+CU-C c_a c_b)
```

is one bivariate resultant:

```text
G_uv(U)=Res_X(F_n(X),H_(C,D)(X,U)),               (GRC4)
H_(C,D)(X,U)=(CX)^d F_n((D+CU)/(CX)).
```

The expression defining `H_(C,D)` is a polynomial in `O[X,U]`. Therefore
the first nineteen coefficients defining the ideal `J_uv` can be recovered
by computing `(GRC4)` modulo `U^19`; neither the `d^2` ordered product-root
list nor a dense `Pcal_n` is a mathematical input to that packet.

These are exact representation identities. They do not bound the derivative
integer `e_n` or the refined double-accident integer `f_n`, provide an
official-scale resultant algorithm, or make a large factorization campaign
responsible by themselves. In particular, the ideals remain indexed by the
individual quotient lifts `(u,v)`; eliminating or aggregating that index is a
separate theorem.
