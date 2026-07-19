# Proof

The four distinct centered parameters are the roots, up to sign, of

```text
T^4+e_2T^2+e_3T+e_4.
```

Under `(PQ2)`, distinctness forces `e_4!=0`. The product identity `(PQ1)`
therefore becomes

```text
A+B=Y^d-1,
A=D U^4,       B=e_4 D V^4.                            (1)
```

Pairwise coprimality of the `G_i` implies `gcd(U,V)=1`. Also `D` is monic,
squarefree, has degree four, and has nonzero constant term. Hence

```text
deg A=d,       deg B=4+4v<=d-4.                        (2)
```

Consider the second-derivative Wronskian

```text
W=A'B''-A''B'.                                         (3)
```

It is nonzero. Indeed, if `W=0`, then `A'` and `B'` are linearly dependent.
The characteristic is zero or greater than `d`, so integration gives
`A=kappa B+eta` for constants `kappa,eta`. Substitution in `(1)` either makes
`Y^d` constant or forces `deg B=d`, contradicting `(2)`.

We next give a lower degree bound for `W` over an algebraic closure. Let
`alpha!=0` be a root of `U` of multiplicity `m`. Since `U,V` are coprime,
`V(alpha)!=0`. If `D(alpha)!=0`, the two terms in `(3)` show

```text
ord_alpha W>=4m-2.
```

If `D(alpha)=0`, then `A` has order `4m+1` and `B` has order one, giving the
stronger bound `ord_alpha W>=4m-1`. Thus every nonzero root of `U` contributes
at least `4m-2`; the same argument applies to every nonzero root of `V`.

At zero, relation `(1)` supplies the missing contribution from the binomial.
For example, eliminating `B` from `(3)` gives

```text
W=d Y^(d-2) ((d-1)A'-Y A'').                           (4)
```

Therefore `ord_0 W>=d-2` when neither `U` nor `V` vanishes at zero. If `U`
has multiplicity `m` there, the leading term in the bracket in `(4)` has
coefficient

```text
4m(d-4m),
```

which is nonzero because `4m<=4r=d-4<d<char(F)`. Hence zero contributes
`d+4m-3`, at least the sum `(d-2)+(4m-2)`. If instead `V` vanishes at zero,
eliminating `A` gives the symmetric conclusion.

Let `R_U,R_V` be the numbers of distinct roots of `U,V`. Summing these local
orders gives

```text
deg W >= d-2+(4r-2R_U)+(4v-2R_V)
      >= d-2+2r+2v.                                    (5)
```

On the other hand, `(2),(3)` give

```text
deg W<=d+4v+1.                                         (6)
```

Comparison of `(5)` and `(6)` yields `2v>=2r-3`. Since both sides are
integers, `v>=r-1`. The defining degree drop already gives `v<=r-1`, proving
`(PQ3)`. Substituting `r=2^37-1` proves `(PQ4)`.

It remains to record the exact residual in `(PQ3')`. The local-order argument
above proves the polynomial divisibility

```text
Y^(d-2) U^2 V^2 | W.                                   (7)
```

After `(PQ3)`, `deg B=d-4`. If `beta` is the nonzero leading coefficient of
`B`, the coefficient of `Y^(2d-7)` in `(3)` is

```text
d beta (d-4)((d-5)-(d-1))=-4d beta(d-4),
```

which is nonzero under the characteristic hypothesis. Hence

```text
deg W=2d-7=8r+1.
```

The divisor in `(7)` has degree

```text
(d-2)+2r+2(r-1)=8r.
```

The quotient is therefore a nonzero polynomial of degree exactly one. This
proves `(PQ3')`.

We finally revisit the sharper first line of `(5)`. With `v=r-1` and
`deg W=8r+1`, it gives

```text
12r-2-2(R_U+R_V)<=8r+1.
```

Hence `R_U+R_V>=2r-1`. But always `R_U<=r` and `R_V<=r-1`, so equality holds
in both bounds. Thus `U` and `V` are squarefree.

For a simple nonzero root of `UV` outside `Z(D)`, the baseline local order
used above is two. A root shared with the squarefree `D` contributes at least
three. If zero is a root of `U` or `V`, equation `(4)` or its symmetric form
likewise contributes one more than the combined baseline. Therefore, if

```text
t=#(Z(UV) intersect (Z(D) union {0})),
```

then `deg W>=8r+t`. Since `deg W=8r+1`, this proves `t<=1`. At any such point
the quotient in `(7)` vanishes, so the point must be the unique root of the
linear polynomial `L`. This proves `(PQ3'')` and completes the proof.
