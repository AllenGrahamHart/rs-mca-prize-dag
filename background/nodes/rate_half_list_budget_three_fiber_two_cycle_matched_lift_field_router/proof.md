# Proof

The boundary-transfer dependency supplies the matched `c=0` generic floor
with `M=2^36`. The parameter-uniform even-factorization dependency therefore
applies with `N=8M=2^39`. Its two cells partition

```text
mu_N\{1,t^(-1)}
```

into sets of size `N/2-1`, and their inverse-root power sums agree for
`1<=j<=N/4`.

Label the inverse roots in the two cells by `+1` and `-1`, and the two
deleted roots by zero. This gives

```text
S(X)=sum_(j=0)^(N-1)s_jX^j in Z[X],
s_j in {+1,-1,0},       S(1)=0,       |{j:s_j=0}|=2.  (1)
```

For a primitive `N`th root `zeta` in the official field, flatness says

```text
S(zeta^m)=0,       1<=m<=N/4.                         (2)
```

Let `omega` be a complex primitive `N`th root and put

```text
R=Res(S,Phi_N)=product_(1<=m<N, m odd)S(omega^m).     (3)
```

This integer is nonzero. Indeed, `Phi_N=X^(N/2)+1`. If it divided `S`, then
`s_(j+N/2)=s_j`. The normalized zero at `j=0` would force the other zero to
be at `N/2`. Each half would contain the same odd number `N/2-1` of signs,
so `S(1)` would be twice a nonzero odd integer, contradicting `(1)`.

Parseval gives

```text
sum_(m=0)^(N-1)|S(omega^m)|^2=N(N-2).
```

Applying arithmetic-geometric mean to the `N/2` primitive factors yields

```text
0<|R|<(2N)^(N/4).                                    (4)
```

If `p=1 mod N`, the `N/8` odd exponents in `1,...,N/4` make the corresponding
factors in `(3)` vanish at one prime over `p`. Since the cyclotomic extension
is unramified there, `p^(N/8)` divides `R`; `(4)` gives `p<4N^2`. If
`p=-1 mod N`, Frobenius supplies the disjoint negative block as well, so
`p^(N/4)` divides `R` and `p<2N`. This proves `(CLF2)`.

The maximal-field dependency leaves `e=1` with `p=1 mod 2^41`, or `e=2`
with `p=+/-1 mod 2^40`. The first case is `p=1 mod N` and is impossible
because

```text
p=q_field>=3*2^128>4N^2.
```

The negative quadratic case is `p=-1 mod N` and is impossible because

```text
q_field=p^2<(2N)^2<3*2^128.
```

The remaining case is exactly `(CLF3)`.

We next audit descent without assuming `4N | p-1`. Since `2N | p-1`, every
root in `mu_N` lies in `F_p` and is a square there. The recurrence defining
the canonical truncation `B_0`, and uniqueness of the normalized secondary
square root defining `C_0`, put both polynomials in `F_p[w]`. Each of
`H_lambda,H_mu` is the constant-normalized product over a subset of
`mu_N`, so both also lie in `F_p[w]`. Comparing the coefficient of the first
shifted term in

```text
H_lambda-B_0^2=lambda w^(2M+1)C_0^2,
H_mu-B_0^2=mu w^(2M+1)C_0^2                         (5)
```

puts `lambda,mu` in `F_p`.

At a root `a` of `H_lambda`, coprimality implies `C_0(a)!=0`; otherwise `(5)`
would make `a` a root of both factors. Hence

```text
-lambda a^(2M+1)=(B_0(a)/C_0(a))^2.                 (6)
```

The factor `a^(2M+1)` is a square because `a in mu_N` and `2N | p-1`.
Thus `-lambda` is a square in `F_p`, and the same argument applies to
`-mu`. This proves `(CLF4)` and descent of all four outer roots.

Both factors in `(5)` have degree `4M-1=N/2-1`. If `c` is the leading
coefficient of `C_0`, the constant terms of their monic reversals are
`lambda c^2` and `mu c^2`. Each is, up to sign, a product of `N`th roots.
Their ratio therefore gives `(CLF5)`; distinct factors give `q_out!=1`.

The matched cycle condition identifies its completion roots with the four
square-root lifts of the two antipodal deleted pairs. Common source scaling
and relabeling give `(CLF6)`. Matching this source quadruple to the outer
quadruple with squared ratio `q_out` is characterized by cross ratio. The
three perfect matchings of four source points give exactly
`(CLF7)--(CLF9)` by direct substitution; this calculation is independent of
`M` and of the field of definition of `r`.

It remains to remove the possible top-lift extension. In the split class
`p=1 mod 4N`, every root of `X^(4N)-1` is in `F_p`. In the nonsplit class
`(CLF10)`, put `eta=r^(2N)`. Then `eta^2=1` and

```text
r^p=r^(1+2N)=eta r.                                  (7)
```

Suppose for contradiction that `eta=-1`. Since `q_out in F_p`, Frobenius
replaces `r` by `-r` in the same matching equation. Comparing `(CLF7)` with
its conjugate forces

```text
(r^2-r+1)^2=(r^2+r+1)^2,
```

and hence `r(r^2+1)=0`. The same comparison in `(CLF9)` gives the same
conclusion. Since `r!=0`, either equation would imply `r^2=-1`, but then
`r^(2N)=1` because `N` is even, contradicting `eta=-1`.

For `(CLF8)`, set

```text
A=(r-1)^4,       B=(r+1)^4,       C=(1+q_out)^2.
```

The equation and its conjugate are

```text
AC=4q_out B,       BC=4q_out A.                     (8)
```

Here `A,B` are nonzero because `r^4!=1`. Thus `A^2=B^2`. If `A=B`, expansion
again gives `r^2=-1`, already impossible. If `A=-B`, put `z=r^2`. Expansion
of `A+B=0`, followed by `(8)`, gives

```text
z^2+6z+1=0,       q_out^2+6q_out+1=0.               (9)
```

The two roots of this separable quadratic are reciprocal, so
`q_out in {z,z^(-1)}`. But `z^N=r^(2N)=-1`, whereas `(CLF5)` gives
`q_out^N=1`, a contradiction. The anti-invariant case is empty.

Consequently `r in F_p` in the nonsplit class as well. The normalized source
and outer quadruples are now both in `F_p`; the unique fractional-linear map
between any matched three distinct points lies in `PGL_2(F_p)`. This proves
all claims. QED.
