# Budget-three deleted-pair even-Jacobi norm router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_trace_gcd_router`

Retain `(TGR1)--(TGR7)` with `L=2M`. Write `J_n^(a,b)` for the Jacobi
polynomial and set

```text
w=2x^2-1,       z=(w+1)/2=x^2,
J(w)=J_M^(-1/4,-1/2)(w).                              (EJN1)
```

The quadratic transformations are

```text
C_(2M)^(1/4)(x)=((1/4)_M/(1/2)_M) J(w),
P_(2L-1)(x)=x J_(L-1)^(0,1/2)(w),
T_(2L)(x)=T_L(w),
U_(2L-1)(x)=2x U_(L-1)(w).                            (EJN2)
```

All displayed constants are nonzero in the official characteristic. Let

```text
Q(w)=J_(L-1)^(0,1/2)(w) mod J(w),       deg Q<M.      (EJN3)
```

Then the Legendre remainder in `(TGR4)` is exactly `R(x)=xQ(w)` on `J=0`.
For one fixed sign `s`, with `s^2=-epsilon`, define

```text
A_0=zQ^2-s^2,                    B_0=2s(Q-s),
A_1=zQ^2+2szQ+s^2,              B_1=6sQ-zQ^2-s^2,
A_2=zQ^2-2szQ-7s^2,             B_2=zQ^2-2sQ+s^2,
F_(j,s)=A_j^2-zB_j^2.                                (EJN4)
```

The signed branch `(j,s)` in `(TGR5)` is nonempty over the algebraic closure
if and only if

```text
J(w)=K_epsilon(w)=F_(j,s)(w)=0,                       (EJN5)
```

where

```text
K_-(w)=T_L(w),       K_+(w)=U_(L-1)(w).               (EJN6)
```

Equivalently, reduce `K_epsilon` and `F_(j,s)` modulo `J`. The branch is empty
exactly when

```text
gcd(J, K_epsilon mod J, F_(j,s) mod J)=1.             (EJN7)
```

This is still six signed tests, but every representative now has degree at
most

```text
M=L/2=2^35                                           (EJN8)
```

on the official deleted-pair row, instead of `L=2^36`. The norm polynomial
in `(EJN4)` should be reduced modulo `J` during its construction; no degree-
`4M` intermediate is required.

This theorem does not prove any gcd in `(EJN7)` to be one. It is an exact
degree-halving endpoint for a symbolic cyclotomic/subresultant proof or a
coverage-proved contributor implementation.
