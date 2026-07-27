# Proof

Write the positive-half negacyclic autocorrelation coefficients as
`A_1,...,A_63`. There are only 21 unordered support pairs, so at
most 21 of these integer coefficients are nonzero. Put

```text
E=sum_d A_d^2=V/2,       L=sum_d |A_d|.
```

For every positive integer `a`,

```text
a^2>=3a-2.
```

Summing over the at most 21 nonzero coefficients gives

```text
E>=3L-42,       L<=floor((E+42)/3).                    (1)
```

If `y_u=|F(zeta^u)|^2` for odd `u`, then the mean of the
`y_u` is 16. Autocorrelation antisymmetry gives

```text
|y_u-16|<=2L.                                          (2)
```

Apply (1) to the five upper variance blocks:

```text
V range    E upper    L upper    y upper B    denominator C
112          56         32          80             1714
114--118     59         33          82             1749
120--124     62         34          84             1785
126--130     65         35          86             1820
132--134     67         36          88             1855
```

For each row define, on `0<x<=B`,

```text
g(x)=log 16+(x-16)/16-(x-16)^2/C-log x.
```

Its derivative factors exactly:

```text
g'(x)=(x-16)(C-32x)/(16 C x).
```

In every row `16<C/32<B`. Thus the only minima are `x=16`
and the endpoint `x=B`. We have `g(16)=0`. Put

```text
r=(B-16)/16-(B-16)^2/C.
```

For each table row, the degree-12 positive Taylor truncation verifies by exact
rational arithmetic that

```text
sum_(j=0)^12 r^j/j! > B/16.
```

Hence `exp(r)>B/16`, so `g(B)>0` and the pointwise
majorant is valid.

Average it over the 128 odd conjugates. The linear deviations have mean zero
and their mean square is `V`, giving

```text
log G<=log 16-V/C,
|Norm(F(zeta))|=G^64<=2^256 exp(-64V/C).               (3)
```

For each row use its minimum `V` and put `q=32V/(3C)`.
The degree-nine positive Taylor truncation verifies exactly that

```text
sum_(j=0)^9 q^j/j! > 2.
```

Therefore `q>log 2`, so `64V/C>6 log 2`. Equation (3)
is strictly below `2^250`. The collision-norm criterion excludes
every listed variance. Since `V` is even, only
`0<V<=110` remains.
