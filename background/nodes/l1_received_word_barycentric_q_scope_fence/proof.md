# Proof - L1 received-word barycentric Q scope fence

## 1. Dual Reed-Solomon moments

For values `y_x` on `A`, Lagrange interpolation gives

```text
I_A(y)(Z)=sum_(x in A) y_x L_A(Z)/((Z-x)L_A'(x)).      (1)
```

The coefficient of `Z^(a-1)` in the interpolant of the values `x^j y_x` is
therefore

```text
sum_(x in A) x^j y_x/L_A'(x).                         (2)
```

Write `I_A(y)=sum_(r=0)^(a-1)c_r Z^r`. For `j=0`, expression `(2)` is
`c_(a-1)`. After `c_(a-1),...,c_(a-j)` have vanished, multiplying the
interpolant by `Z^j` shows that `(2)` is `c_(a-1-j)`. Induction therefore
gives

```text
B_0=...=B_(w-1)=0
iff c_(a-1)=...=c_(a-w)=0
iff deg I_A(U)<a-w=k.
```

Before specializing to the zero target, each `B_j` equals
`c_(a-1-j)` plus a linear combination of the higher coefficients. The
coefficient change is thus triangular with diagonal one.

## 2. Depth-one formula

For `U(Z)=Z^4` and a triple `A`, write

```text
L_A(Z)=Z^3-e_1(A)Z^2+e_2(A)Z-e_3(A).
```

Polynomial division by `L_A` gives

```text
[Z^2](Z^4 mod L_A)=e_1(A)^2-e_2(A),
```

which proves `(BQ3)`. In `F_7`, the triples `012` and `136` both have root
sum `3`, so their first locator coefficient is `-3`. Their second elementary
sums are `2` and `6`; `(BQ3)` gives received-word prefix values `0` and `3`.
Thus the first locator prefix does not determine the first interpolation
prefix.

For a triple `{0,r,s}`, formula `(BQ3)` becomes

```text
f(0rs)=r^2+rs+s^2.
```

At `(r,s)=(1,2),(3,5),(1,3),(2,5)` the four values are `0,0,6,4`, giving
the nonzero exchange defect `4 mod 7` in `(BQ4)`.

If `f(A)=c+sum_(x in A)g(x)`, both sides of the exchange contain the base
point zero twice and each of `1,2,3,5` once. Their difference must be zero,
contradicting `(BQ4)`. This proves the fixed-column obstruction.

Finally, the interpolant on `012` is `P(Z)=Z`. The roots of
`Z^4-Z=Z(Z^3-1)` in `F_7` are `0,1,2,4`; since `4` is not in `H`, its exact
agreement set on `H` is `012`. This verifies the exact-shell assertion.

## 3. Route conclusion

Upstream primitive Q assumes a proved linear syndrome map from fixed Boolean
columns, and its row atom is the locator-prefix fiber. Sections 1 and 2 show
that the arbitrary-received-word exact shell naturally has moving
barycentric columns and is not even determined by the same-depth locator
prefix. Therefore direct theorem consumption is not typed. The conclusion
does not exclude a separately proved nonlinear or chart-specific transport.
