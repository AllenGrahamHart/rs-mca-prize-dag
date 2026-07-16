# Proof

Write `D=gamma H`, where `H` is the order-`n` subgroup of `F^*`, and put

```text
Q=D^c,                 delta=gamma^n.
```

The set `Q` has order `N=n/c`, every element of `Q` indexes one `c`-point
fiber of `x -> x^c` on `D`, and every `y in Q` satisfies

```text
y^N=delta.                                                  (1)
```

Let `b_0` index the distinguished fiber containing `T_0`, and set

```text
L_0(X)=product_(t in T_0)(X-t).
```

For every `m`-subset `A` of `Q\{b_0}`, write

```text
P_A(Y)=product_(b in A)(Y-b)=sum_(j=0)^m a_j(A)Y^j,
a_m(A)=1.
```

Rotate this coefficient arc cyclically through the quotient-domain equation:

```text
R_A(Y) = rem_(Y^N-delta)(Y^(N-d)P_A(Y)).                    (2)
```

Since `m=N/2+d<=N-1`, only one wrap occurs. Expanding `(2)` gives

```text
R_A(Y)
 = sum_(j=0)^(d-1) a_j(A)Y^(N-d+j)
   + delta sum_(j=d)^m a_j(A)Y^(j-d).                       (3)
```

Now define the locator

```text
L_A(X)=L_0(X)R_A(X^c).                                     (4)
```

Because `s<c`, multiplication by `L_0` leaves disjoint degree blocks
`[ic,ic+s]` for the quotient indices `i` appearing in `(3)`. The code
dimension is

```text
k=n/2=(N/2)c.
```

The indices in `(3)` that contribute to degrees at least `k` are exactly

```text
N-d,...,N-1                 from j=0,...,d-1,
N/2                         from j=m.
```

The coefficient at the last index is the fixed value `delta*a_m=delta`.
Consequently the complete polynomial part of `L_A` in degrees at least `k`
depends only on

```text
(a_0(A),a_1(A),...,a_(d-1)(A)).                            (5)
```

There are only `N q^(d-1)` possible vectors in `(5)`. Indeed,

```text
a_0(A)=(-1)^m product_(b in A)b.
```

The quotient set `Q` is a multiplicative coset of its order-`N` subgroup, so
all such products lie in one multiplicative coset of size `N`; the remaining
`d-1` entries have at most `q^(d-1)` values. Pigeonholing the
`C(N-1,m)` choices of `A` therefore gives a class `S` of size at least `(CR1)`
whose locators share every coefficient of degree at least `k`.

Let `U` be this common high-degree part, and put

```text
E_A=L_A-U.
```

Then `deg(E_A)<k`, so `-E_A` is a codeword and

```text
U-(-E_A)=L_A.                                               (6)
```

For `x in D`, equations `(1)` and `(2)` give

```text
R_A(x^c)=x^(c(N-d))P_A(x^c).
```

The prefactor is nonzero. Thus `(4)` vanishes on exactly the fixed `s` points
of `T_0` and the `m` full fibers indexed by `A`. These sets are disjoint
because `b_0` was excluded, so `(6)` has exactly

```text
s+mc=s+(N/2+d)c=n/2+dc+s
```

agreement positions. Distinct `A` give distinct root sets, hence distinct
locators and distinct degree-below-`k` codewords. This proves `(CR1)` and
`(CR2)`.

For an `r`-fold common-support interleaving, use received word
`(U,...,U)` and codeword tuples `(-E_A,...,-E_A)`. Their common agreement
support is unchanged, proving the interleaving assertion.

At the printed cap-row parameters, `(CR1)` is strictly greater than the prize
threshold `q/2^128` whenever

```text
C(N-1,m)/(N q^(d-1)) > q/2^128,
```

which is exactly `(CR3)`. The exact integer verifier proves `(CR3)` at
`q=2^256`; its two sides are integers, so no decimal approximation is used.
The condition only becomes stronger as `q` decreases. Finally, list balls are
monotone as the required agreement decreases, which propagates failure at
`sigma*` through the whole residual band.
