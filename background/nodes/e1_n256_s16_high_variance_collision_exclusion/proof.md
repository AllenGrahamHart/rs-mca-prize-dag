# Proof

Put `h=128`. Odd-character orthogonality gives

```text
(1/h) sum_(u odd) y_u = sum_i c_i^2 = 16.
```

The coefficient `L1` norm is ten, so `0<y_u<=100`. Nonvanishing follows from
`deg F<h=deg Phi_256`.

As in the folded-L2 theorem, write

```text
F(X)F(X^-1)-16=sum_(d=0)^(h-1) A_d X^d mod (X^h+1).
```

Parseval gives `V=sum_d A_d^2`. The coefficients satisfy
`A_(h-d)=-A_d`, with `A_0=A_(h/2)=0`, so `V` is an even nonnegative integer.
Conjugate pairing also gives

```text
|Norm(F(zeta))|=G^64,
G=exp((1/h) sum_(u odd) log y_u).                (1)
```

If `V=0`, all `y_u=16`, so (1) is `16^64=2^256`. No odd row prime divides
it.

For the remaining range define, on `0<x<=100`,

```text
g(x)=log 16+(x-16)/16-(x-16)^2/2070-log x.
```

Its derivative factors exactly as

```text
g'(x)=-(x-16)(32x-2070)/(33120x).
```

Thus the only possible minima are `x=16` and the endpoint `x=100`. We have
`g(16)=0`, while

```text
g(100)=847/460-log(25/4)>0.
```

For the strict endpoint inequality, the degree-six positive Taylor
truncation gives

```text
exp(847/460)
 > 42882796663116856249 / 6821493765120000000
 > 25/4.
```

Hence `g(x)>=0` throughout the interval. Average the resulting logarithmic
majorant and use `mean(y_u-16)=0`:

```text
log G <= log 16-V/2070.
```

For `V>=136`, equation (1) gives

```text
|Norm(F(zeta))|
 <= 2^256 exp(-64*136/2070)
 = 2^256 exp(-4352/1035).
```

Now `4352/1035>21/5`. Also the degree-three positive Taylor truncation gives

```text
exp(7/10)>1+7/10+49/200+343/6000=12013/6000>2.
```

Therefore `exp(4352/1035)>exp(21/5)>2^6`, and the norm is strictly below
`2^250`. The collision-norm criterion excludes divisibility by every live row
prime. Since `V` is even, only `0<V<=134` remains.
