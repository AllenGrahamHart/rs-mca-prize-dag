# Proof

Let `omega` be a complex primitive `N`th root. The factorization dependency
partitions `mu_N\{1,t^(-1)}` into two cells of size `N/2-1`. Inverting the
cells changes the deleted roots to `1,t` and gives `(FRC1)`. The equal Fourier
moments `(DEF5)` are exactly `(FRC2)` after reduction at a prime above `p`.

First, the primitive cyclotomic resultant

```text
R=Res(S,Phi_N)=product_(1<=m<N, m odd) S(omega^m)      (1)
```

is a nonzero integer. Indeed, for dyadic `N`,
`Phi_N=X^(N/2)+1`. If `Phi_N` divided `S`, comparison of the two coefficient
halves would give

```text
s_(j+N/2)=s_j,       0<=j<N/2.                        (2)
```

The zero at `j=0` would force the other zero to occur at `N/2`. Each half
would then contain exactly `N/2-1` nonzero signs, an odd number. Equation
`(2)` would make `S(1)` twice a nonzero odd integer, contradicting `S(1)=0`.
Thus `(1)` is nonzero.

Parseval for the unnormalized discrete Fourier transform gives

```text
sum_(m=0)^(N-1)|S(omega^m)|^2
 =N sum_j |s_j|^2=N(N-2).                             (3)
```

There are `phi(N)=N/2` primitive roots. Applying arithmetic--geometric mean
to just their factors and bounding their square sum by `(3)` gives

```text
0<|R|<(2N)^(N/4).                                     (4)
```

Suppose first that `p=1 mod N`. Choose a prime ideal above `p` that sends
`omega` to the printed `zeta`. Among `1,...,N/4`, exactly `N/8` indices are
odd. By `(FRC2)`, all corresponding factors in `(1)` vanish at that prime
ideal. The extension is unramified, so

```text
p^(N/8) divides R.                                    (5)
```

Combining `(4)--(5)` yields `p<4N^2`, proving `(FRC3)`.

If `p=-1 mod N`, Frobenius also sends every zero at exponent `m` to a zero at
`-m`. The positive and negative odd blocks are disjoint and contain `N/4`
primitive exponents in total. Hence

```text
p^(N/4) divides R,                                    (6)
```

and `(4)` gives `p<2N`, proving `(FRC4)`.

The field-degree dependency leaves only `e=1` with
`p=q>=3*2^128`, or `e=2` with `p=+/-1 mod 2^40`. Since `N=2^38`, every one
of these residues is `+1` or `-1` modulo `N`. But

```text
3*2^128>4N^2,       3*2^128>(2N)^2.                  (7)
```

Thus `(FRC3)` excludes `e=1`, and `(FRC4)` excludes the `e=2`,
`p=-1 mod N` branch after squaring its bound and using `q=p^2>=3*2^128`.
Only `(FRC5)` remains.

In that branch the stronger official congruence is `p=1 mod 2^40=4N`.
Thus `mu_N`, the ratio `t`, and the order-`2^40` square-root lifts of the
deleted roots all lie in `F_p`. The coefficient recurrence for `B_0` and the
unique normalized secondary square root for `C_0` are defined over `F_p`, so
`B_0,C_0 in F_p[w]`. Each factor in `(DEF3)` is the constant-normalized
product of one subset of `mu_N`, hence also lies in `F_p[w]`. Comparing

```text
H_lambda-B_0^2=lambda w^hC_0^2,
H_mu-B_0^2=mu w^hC_0^2                              (8)
```

at their first shifted coefficient gives `lambda,mu in F_p`.

Every element of `mu_N` is a square in `F_p` because `4N` divides `p-1`.
At a root `a` of `H_lambda`, coprimality of the two factors implies
`C_0(a)!=0`; otherwise `(8)` would also give `B_0(a)=0` and make `a` a root
of both factors. Therefore

```text
-lambda a^h=(B_0(a)/C_0(a))^2.                       (9)
```

The factor `a^h` is a square, so `-lambda` is a square in `F_p`. The same
argument applies to `-mu`. Hence all roots of
`(W^2+lambda)(W^2+mu)` lie in `F_p`.

Finally, the four deleted-root square lifts and the four outer parameters are
distinct `F_p` points. A fractional-linear map over `F_{p^2}` carrying three
distinct `F_p` points to three distinct `F_p` points is the unique map between
those triples and therefore lies in `PGL_2(F_p)`. This proves `(FRC6)` and
the base-field Möbius claim. QED.
