# Proof

Write `h=256`. Since `deg F<h=deg Phi_512`, every four-term `F` in the
statement is nonzero at every conjugate of `zeta`. Thus

```text
y_u=F(zeta^u)F(zeta^(-u))>0                    (u odd).
```

Odd-character orthogonality gives

```text
(1/h) sum_(u odd) y_u = 4.
```

## 1. The exact variance

Work in `Z[X]/(X^h+1)` and put

```text
A(X)=F(X)F(X^-1)-4=sum_(d=0)^(h-1) A_d X^d.
```

The constant coefficient is zero. The involution `X -> X^-1` fixes `A` and
gives

```text
A_(h-d)=-A_d       (1<=d<h),       A_(h/2)=0.
```

Parseval over the odd roots now yields

```text
V := (1/h) sum_(u odd) (y_u-4)^2 = sum_d A_d^2.
```

The nonzero coefficients occur in opposite pairs with equal squares. Hence
`V` is an even nonnegative integer. If

```text
G=exp((1/h) sum_(u odd) log y_u),
```

then conjugate pairing gives

```text
|Norm(F(zeta))|=G^(h/2)=G^128.                 (1)
```

## 2. The zero-variance case

If `V=0`, all `y_u=4`. Equation (1) gives

```text
|Norm(F(zeta))|=4^128=2^256.
```

No odd row prime divides this norm.

## 3. The range V>=4

For `0<x<=16`, define

```text
g(x)=log 4+(x-4)/4-(x-4)^2/90-log x.
```

Direct differentiation gives

```text
g'(x)=-(x-4)(4x-45)/(180x).
```

Thus the only possible minima on `(0,16]` are at `x=4` and the endpoint
`x=16`. Here `g(4)=0` and

```text
g(16)=7/5-log 4>0.
```

The last inequality is exact: the degree-five positive Taylor truncation for
`exp(7/5)` is `189479/46875>4`. Therefore

```text
log x <= log 4+(x-4)/4-(x-4)^2/90              (2)
```

throughout the required interval. Since `F` has four unit terms,
`0<y_u<=16`. Average (2), use `mean(y_u-4)=0`, and obtain

```text
log G <= log 4-V/90.
```

For `V>=4`, the elementary inequality `exp(t)>1+t` at `t=2/45` gives

```text
G <= 4 exp(-2/45) < 180/47.
```

Exact integer arithmetic gives

```text
(180/47)^128 < 2^250.                           (3)
```

Equations (1) and (3) exclude divisibility by every row prime
`p>=2^250`.

## 4. The exceptional variance V=2

The antisymmetry and `sum A_d^2=2` force exactly one coefficient pair:

```text
A(X)=epsilon (X^d-X^(h-d)),       epsilon in {+1,-1},
1<=d<h,                           d!=h/2.
```

At an odd root this is

```text
y_u=4+epsilon(w+w^-1),            w=zeta^(ud).
```

Let `M` be the order of `zeta^d` and `r=M/2`. The excluded values `d=0,h/2`
show that the power of two `M` is at least eight, so `r>=4`. As `u` runs over
the odd residues modulo 512, `w` runs over every primitive `M`-th root with
multiplicity `h/r`.

Put `lambda=2+sqrt(3)`, so `lambda+lambda^-1=4`. The primitive `M`-th roots
are exactly the roots of `X^r+1`. Factoring the two linear terms, for either
sign of `epsilon`, gives the exact product

```text
product_(w primitive M) (4+epsilon(w+w^-1))
  = lambda^r+lambda^(-r)+2
  = lambda^r(1+lambda^(-r))^2.
```

Multiplicity therefore cancels from the geometric mean:

```text
G=lambda(1+lambda^(-r))^(2/r).
```

Now `lambda<15/4`, `lambda>3`, and `r>=4`. Hence

```text
G < (15/4) sqrt(1+1/81)
  < (15/4)(76/75)
  = 19/5,
```

where the second strict inequality is the integer comparison
`82*75^2<81*76^2`. Finally,

```text
(19/5)^128<2^250.                               (4)
```

Equations (1) and (4) exclude the `V=2` case. All even possibilities for `V`
have now been covered. The collision-norm criterion proves the claim.
