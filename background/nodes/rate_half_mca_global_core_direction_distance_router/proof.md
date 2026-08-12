# Proof

After global-core cancellation, choose for every selected slope `gamma` a
shortened explanation `c_gamma` and an exact pair-noncontained agreement
support of size `m=d+s`.  The error

```text
e_gamma=r_0+gamma r_1-c_gamma
```

has weight at most `t=R-d` and syndrome `y_0+gamma y_1`.  If `y_1=0`, then
`r_1` is a codeword.  Subtracting `gamma r_1` from any slope explanation
would explain `r_0` on the same support, contradicting pair noncontainment.
Thus `y_1` is nonzero.

The direction-distance ray theorem applies to the entire shortened domain
`U`, whose size is `N=R+s`.  Since any `R` parity-check columns span syndrome
space, `d_U(y_1)<=R`, so `j=R-d_U(y_1)>=0`.  Its denominator is

```text
(N-t)^2-N(N-d_U(y_1))
 = (d+s)^2-(R+s)(s+j)
 = d^2-(R-2d)s-(R+s)j
 = D_s(j),
```

and its numerator is

```text
N(d_U(y_1)-t)=(R+s)(d-j).
```

This proves the displayed bound whenever `D_s(j)>0`.

For integer `B`, positivity is equivalent to

```text
j <= floor((D_s(0)-1)/(R+s)),
```

and the floor of the rational bound is at most `B` exactly when

```text
(R+s)(d-j) < (B+1)(D_s(0)-(R+s)j).
```

Solving this strict integer inequality and also imposing `j<=d-1` gives the
contract's formula for `J_B(s)`.  The affine-span compiler pays all smaller
dimensions independently of `j`.

The verifier evaluates these integer formulae at every official dimension in
the two stated ranges.  It also checks the first nonpositive dimension, both
global maxima, and the thirteen Mersenne dimensions at which the budget cuts
one last positive-denominator defect.  No asymptotic or floating-point
comparison is used.
