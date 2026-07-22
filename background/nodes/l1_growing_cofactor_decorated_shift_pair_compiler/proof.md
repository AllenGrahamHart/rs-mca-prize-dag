# Proof - L1 growing-cofactor decorated shift-pair compiler

## 1. Domain partition and low residual

Distinct shell codewords cannot have the same exact agreement set: two
degree-below-`k` polynomials agreeing on more than `k` points are equal.
Therefore `S_1` and `S_2` are distinct but have the same size `a`, so the two
set differences have the same positive size `d`.

The four sets in `(DS1)` partition `H`, proving `Omega=GABN`. From
`(DS2)`, subtraction gives `(DS5)` with `R=AQ_1-BQ_2`. The polynomial
`P_2-P_1` is nonzero and has degree at most `k-1`. Since it is divisible by
the degree-`g` locator `G`,

```text
g<=k-1,       R!=0,       deg R<=k-g-1.
```

But `d=a-g` and `w=a-k`, so `k-g=d-w`. This proves `(DS3)`.

The complement of `S_1` has locator `BN`. Exactness of its factorization in
`(DS2)` says `Q_1` is nonzero on every such root, equivalently
`gcd(Q_1,BN)=1`. The same argument for `S_2` proves `(DS4)`.

Conversely, define `P_1=U-GAQ_1`. The anchor condition makes it a codeword.
Equation `(DS5)` defines `P_2=P_1+GR=U-GBQ_2`, which also has degree below
`k`. The coprimality conditions exclude every complement agreement, so the
two agreement sets are exactly `S_1,S_2`. All locators and cofactors are
recovered uniquely from the ordered pair, proving `(DS6)`.

## 2. Scalar cofactor

When `e=0`, monicity of the agreement locators forces both cofactors to equal
the leading coefficient of `U`. Therefore `R` is that scalar times `A-B`,
and `(DS3)` is exactly `(DS7)`. Equality of the top `w` locator coefficients
is equivalent to the printed difference-degree bound, giving the standard
shift-pair record.

## 3. Primitive uniqueness

Suppose `(Q_1,Q_2,R)` and `(Q'_1,Q'_2,R')` are two cofactor-primitive
solutions for the same ordered `(A,B)`. Multiply their defining equations by
`Q'_2` and `Q_2` respectively and subtract. This gives `(DS9)`.

Since `deg R,deg R'<=d-w-1` and all cofactors have degree `e`, the right side
has degree at most `d-w-1+e`. If `e<=w`, this is at most `d-1`. It is divisible
by the monic degree-`d` polynomial `A`, so it is zero. Hence

```text
Q_1Q'_2=Q'_1Q_2.
```

Because `gcd(Q_1,Q_2)=1`, one has `Q_1|Q'_1` and `Q_2|Q'_2`. Equal degrees
make each quotient a scalar, and the common prescribed leading coefficient
makes that scalar one. The two pairs and then their residuals are equal.

Finally, for `D=gcd(Q_1,Q_2)`, both terms defining `R` are divisible by `D`,
so `D|R`. Every factor of `D` is a factor of both cofactors. Equation `(DS4)`
then makes it coprime to `A`, `B`, and `N`, proving `(DS10)`.
