# Proof

Write the quotient set `Q=D^c`. Its `N` elements index the `c`-point fibers
of `x -> x^c` on `D`. Let `b_0` index the distinguished fiber `C_0`, and
write

```text
L_0(X)=product_(t in T_0)(X-t).
```

For every `m`-subset `A` of `Q\{b_0}`, put

```text
P_A(X)=product_(b in A)(X^c-b)
      =X^(mc)+alpha_1(A)X^((m-1)c)+...+alpha_m(A),
L_A(X)=L_0(X)P_A(X).
```

There are `C(N-1,m)` such locators. Pigeonhole the vectors

```text
(alpha_1(A),...,alpha_d(A)) in F^d.
```

Some class `S` has size at least `ceil(C(N-1,m)/q^d)`. For two members of
this class, the difference of their locators contains only quotient terms
with index at least `d+1`. Its degree is therefore at most

```text
s+(m-d-1)c = s+(k/c-1)c = k-c+s < k.                      (1)
```

Thus all locators in `S` have the same polynomial part in degrees at least
`k`; call that common part `U`. For each `A in S`, the remainder

```text
R_A=L_A-U
```

has degree below `k` by `(1)`. Hence `-R_A` is a codeword and

```text
U-(-R_A)=L_A.
```

It agrees with `U` exactly on the roots of `L_A`: the fixed `s` points of
`T_0` and the `m` disjoint full fibers indexed by `A`. Their number is

```text
s+mc=s+(k/c+d)c=k+dc+s.
```

Distinct `A` give distinct root sets and therefore distinct locators. Since
their common high part is `U`, they also give distinct degree-below-`k`
remainders. This proves `(FT1)` and `(FT2)`.

At the printed cap-row parameters, `(FT2)` is `k+sigma*` and `(FT1)` is

```text
ceil(C(524287,264192)/q^2048).
```

Condition `(FT3)` implies that this count is strictly greater than
`q/2^128`, the ordinary-list prize threshold. List balls are monotone as the
agreement requirement decreases, so failure at `sigma*` certifies every
smaller agreement excess in the residual band. The decimal in `(FT4)` is the
display of the exact boundary

```text
(128+log2 C(524287,264192))/2049.
```

No decimal approximation is used in `(FT3)`.
