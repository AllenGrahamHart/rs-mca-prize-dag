# Proof

## Local valuation and cofactors

Reduce `F` coefficientwise modulo two. Only the six singleton coefficients
remain. If their exponents form `E`, put

```text
P(X)=sum_(e in E) X^e in F_2[X].
```

The integral expansion at `zeta=1+pi`, exactly as in the local-norm cofactor
proof, gives

```text
mu=v_pi(F(zeta))=ord_(X=1)(P)=v_2(R).                (2)
```

The prize field floor and `R<=18^64` give

```text
m=R/p<=floor(18^64/(B_P 2^128))=2013.               (3)
```

Hence `2^mu<=m<=2013`, so `mu<=10`.

It remains to classify the small multiplicities of a six-term binary
polynomial. Modulo `(X+1)^16`, one has `X^16=1`. After exponents are reduced
modulo 16 and equal residues cancel in pairs, the parity support therefore
has size 0, 2, 4, or 6. The zero support has multiplicity at least 16. For
every subset `J` of `{0,...,15}` of size 2, 4, or 6, the Hasse-derivative
criterion is

```text
ord_(X=1)(sum_(r in J) X^r)
 = min{j: sum_(r in J) binom(r,j)=1 mod 2}.          (4)
```

Enumerating the `120+1820+8008` subsets in (4) gives, below 16,

```text
{1,2,3,4,5,6,8,9,10,12}.
```

Intersecting with `mu<=10` removes 12 and proves the valuation set in the
statement. The committed verifier reproduces (4), its complete count by
support size, and a witness for every retained value.

Local reciprocity gives `R/2^mu=1 mod 256`, while pair feasibility gives
`p=1 mod 256`. Consequently

```text
m=2^mu(1+256t),          t>=0.                       (5)
```

Intersecting (5), the valuation set, and (3) gives thirteen values before
the global residue-degree sieve. The extra value is
`1026=2*3^3*19`; both 3 and 19 have order 64 modulo 256, but their exponents
in a cyclotomic norm would have to be multiples of 64. Removing 1026 gives
exactly (1).

## The first two variance levels

In `Z[X]/(X^128+1)`, write

```text
F(X)F(X^-1)-18=sum_(d=0)^127 A_d X^d.
```

Odd-character Parseval and `A_(128-d)=-A_d`, `A_0=A_64=0`, give

```text
V=2 sum_(d=1)^63 A_d^2.                              (6)
```

Thus `V` is even. If `V=0`, every conjugate square has value 18 and
`R=18^64`, whose 2-adic valuation is 64. This contradicts `mu<=10`.

If `V=2`, exactly one positive-half autocorrelation is `+1` or `-1`, at a
lag `delta`. Modulo two, (6) gives in the Laurent group ring

```text
P(X)P(X^-1)=X^delta+X^(-delta).
```

The left side has multiplicity `2mu` at one. The right side has multiplicity
`2^(1+v_2(delta))`, so

```text
mu=2^v_2(delta) in {1,2,4,8}.                        (7)
```

Moreover every conjugate square is

```text
18+epsilon(zeta^(u delta)+zeta^(-u delta)).
```

The exact Lucas-resultant calculation already used for the profile-(4,2)
window depends only on this display and (7). For pure cofactors
`2,4,16,256` its resultant is above `m p_max`; for the other values allowed
at the corresponding valuations it is nonzero modulo `514`, `1538`, and
`1028`. Hence no candidate cofactor permits `V=2`.

## Logarithmic deficit

Here `0<y_u=|F(zeta^u)|^2<=12^2=144`. For `0<x<=144`,

```text
log x <= log 18+(x-18)/18-(x-18)^2/3240.             (8)
```

Indeed, the derivative of the right side minus `log x` is

```text
(x-18)(3240-36x)/(18*x*3240).
```

The only minima are therefore at `x=18` and an endpoint. The value at 18 is
zero; the value at 144 is `21/10-log 8>0`, certified by
`T_6(21/10)>8`.

Averaging (8), using mean `18`, and applying (6) yields

```text
R<=18^64 exp(-64V/3240)=18^64 exp(-8V/405).          (9)
```

For each cofactor in (1), exact rational Taylor lower bounds prove that (9)
is below `m B_P 2^128` at the onset printed in the statement. Exact Taylor
upper bounds show that the preceding even variance is not removed by this
particular majorant. The verifier records both certificate degrees. Since
`V=0,2` are already impossible, the residual windows follow.
