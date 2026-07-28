# Proof

Put `h=128`. Odd-character orthogonality gives

```text
(1/h) sum_(u odd) y_u = sum_i c_i^2 = 18.
```

The coefficient `L1` norm is ten, so `0<y_u<=100`; nonvanishing follows from
`deg F<h=deg Phi_256`. Write in `Z[X]/(X^128+1)`

```text
F(X)F(X^-1)-18=sum_(d=0)^127 A_d X^d.
```

Parseval gives `V=sum_d A_d^2`. Moreover `A_(128-d)=-A_d` and
`A_0=A_64=0`, so

```text
V=2E,             E=sum_(d=1)^63 A_d^2.              (1)
```

Every coefficient product involving one of the four magnitude-two entries is
even. The unique pair of singleton entries contributes an odd summand to one
positive-half autocorrelation coefficient. The local-norm theorem restricts
the live cofactors to 2-adic valuations `1,2,4,8`; equivalently, the singleton
separation has 2-adic order `0,1,2,3`, so it is not the antipodal lag 64.
Consequently exactly one `A_d` is odd. Squares modulo four in (1) give

```text
E=1 mod 4,             V=2 mod 8.                    (2)
```

## Logarithmic deficit

For `0<x<=100`, define

```text
g(x)=log 18+(x-18)/18-(x-18)^2/2367-log x.
```

Its derivative factors exactly as

```text
g'(x)=(x-18)(2367-36x)/(18*x*2367).
```

Thus the only possible minima are `x=18` and the endpoint `x=100`. We have
`g(18)=0` and

```text
g(100)=451/263-log(50/9)>0.
```

Indeed, for `T_k(x)=sum_(j=0)^k x^j/j!`, exact rational arithmetic gives

```text
T_9(451/263)-50/9
 =106695074635404932039009/1092281991851445329987277120 > 0.
```

Hence the displayed majorant holds. Averaging it and using the zero mean of
`y_u-18` yields

```text
R <= 18^64 exp(-64V/2367).                            (3)
```

Put

```text
p_min=B_P 2^128,
B_P=317494674775468773183020924238786383963.
```

If `R=pm`, then (3) contradicts `p>=p_min` as soon as

```text
exp(64V/2367) > 18^64/(m p_min).                      (4)
```

For the seven live cofactors, positive Taylor truncations certify (4) at the
following admissible onsets. Every entry is an exact rational comparison.

| `m` | onset `V` | truncation degree `k` in `T_k(64V/2367)` |
|---:|---:|---:|
| 2 | 258 | 11 |
| 514 | 58 | 3 |
| 1538 | 10 | 3 |
| 4 | 234 | 10 |
| 1028 | 26 | 3 |
| 16 | 186 | 7 |
| 256 | 82 | 4 |

Together with (2), this gives the upper ends in `statement.md`.

## Exact exclusion of `V=2`

If `V=2`, equation (1) forces one positive-half autocorrelation coefficient
to equal `epsilon in {+1,-1}` and every other one to vanish. If the singleton
separation has 2-adic order `t`, then for every odd `u`

```text
y_u=18+epsilon(zeta^(u delta)+zeta^(-u delta)),
t in {0,1,2,3}.
```

Define the integer Lucas sequence

```text
L_0=2,   L_1=18,   L_n=18L_(n-1)-L_(n-2).
```

Multiplication by the odd part of `delta` permutes the relevant primitive
roots. Taking the resultant against the appropriate power-of-two cyclotomic
polynomial and then accounting for multiplicity gives

```text
R=L_(64/2^t)^(2^t).                                  (5)
```

The sign `epsilon` does not change (5), since all four Lucas indices are even.
The exact recurrence values are

| `t` | `L_(64/2^t)` |
|---:|---:|
| 0 | 178342091698891843163466683840822101223162205277179656650156983624835803932590082 |
| 1 | 13354478338703157414450712387359637585922 |
| 2 | 115561578124838522882 |
| 3 | 10749957122 |

For all four rows, (5) is strictly greater than `256 p_max`, where

```text
p_max=(B_P+1)2^128-1.
```

Thus the pure-power cofactor attached to that row (`2,4,16,256`) would give
`p=R/m>p_max`. The remaining candidates fail exact divisibility:

```text
t=0: R mod 514=450,    R mod 1538=2;
t=1: R mod 1028=452.
```

Therefore `V=2` is impossible for every prize cofactor. The `m=1538` window
is empty, and deleting `V=2` from the other six windows proves the claim.
