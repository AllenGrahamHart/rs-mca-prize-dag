# WCL fixed-divisor straight-line certificate lift

- **status:** PROVED
- **closure:** proof
- **consumers:** `dli_wcl_slot_1_5_emptiness`,
  `dli_wcl_slot_1_6_emptiness`, `dli_wcl_slot_2_7_emptiness`,
  `dli_wcl_slot_4_9_emptiness`
- **dependencies:** the three proved WCL fixed-divisor descents

Let

```text
G(Y)=Y^w+g_(w-1)Y^(w-1)+...+g_0 in Z[z_1,...,z_b][Y]       (SL1)
```

be one of the four monic divisor polynomials in the table below. In every
row each `g_j` has total degree at most two in the base variables `z_i`.

```text
slot    N=2^m   w   b   G
(1,5)     256   5   3   Y A(Y)^2-(bY+1)^2, deg A=2
(1,6)     256   6   5   E(Y)^2-YB(Y)^2, deg E=3, deg B<=1
(2,7)     512   7   4   Y A(Y)^2-(bY+1)^2, deg A=3
(4,9)    1024   9   4   Y A(Y)^2-1, deg A=4.                 (SL2)
```

Put `V_0(Y)=Y`. Introduce polynomials

```text
V_t(Y)=sum_(j=0)^(w-1) v_(t,j)Y^j,       1<=t<=m,
Q_t(Y)=sum_(j=0)^(w-2) q_(t,j)Y^j,       0<=t<m,             (SL3)
```

and impose, coefficient by coefficient,

```text
V_t(Y)^2=V_(t+1)(Y)+G(Y)Q_t(Y),           0<=t<m,
V_m(Y)=1.                                                        (SL4)
```

For every commutative base ring, the recurrence equations before `V_m=1`
have a unique solution in the variables `(V_t,Q_t)`: they are the successive
monic quotients and remainders

```text
V_t=Y^(2^t) mod G.                                      (SL5)
```

Consequently the full straight-line scheme `(SL4)` is isomorphic over
`Z` to the original base divisor scheme

```text
G divides Y^N-1.                                       (SL6)
```

No solutions or scheme components are introduced or discarded.

There are `b+m(2w-1)` variables and `m(2w-1)+w` coefficient equations.
Every equation has total degree at most three. The exact sizes are

```text
slot    variables   equations   maximum total degree
(1,5)       75          77               3
(1,6)       93          94               3
(2,7)      121         124               3
(4,9)      174         179               3.             (SL7)
```

There is an exact smaller presentation for computation. Put

```text
s=floor(log_2(w-1)),       k=m-s.                       (SL8)
```

The remainders through `V_s=Y^(2^s)` occur below degree `w`, so they and
their zero quotients are fixed. Start `(SL4)` at `t=s`, and substitute the
terminal value `V_m=1` directly in the last recurrence. The resulting scheme
is still isomorphic to `(SL6)`, now with

```text
b+k(2w-1)-w variables,       k(2w-1) equations.         (SL9)
```

Its exact sizes are

```text
slot    s   k   variables   equations   maximum total degree
(1,5)   2   6       52          54               3
(1,6)   2   6       65          66               3
(2,7)   2   7       88          91               3
(4,9)   3   7      114         119               3.     (SL10)
```

Each of the four base divisor ideals is already proved to have no
characteristic-zero point. Therefore its straight-line ideal is also the
unit ideal over `Q`. For every row there are a nonzero integer `Delta` and
integer polynomials `H_a` such that

```text
Delta=sum_a H_a E_a,                                   (SL11)
```

where the `E_a` are precisely the sparse equations in `(SL4)`. Such an
identity is an exact alternative to expanding `(Y^N-1) mod G` first.
Computing and factoring a checked `Delta`, and excluding its compatible
characteristics, remains open. This theorem does not close any WCL slot and
does not assert that Groebner elimination on the lifted system is cheap.
