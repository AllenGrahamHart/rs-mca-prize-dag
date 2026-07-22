# Proof - unsafe spending-cell fiber-layout counterexample

## The admissible row

Put

```text
q=1705*2^120+1,
n=2^13,
k=n/4,
B*=floor(q/2^128).
```

The integer `1705` is odd and smaller than `2^120`.  The modular identity

```text
3^((q-1)/2)=-1 mod q
```

is checked by `verify.py`; Proth's theorem therefore proves that `q` is
prime.  Also `n|q-1`, `q<2^256`, `k<=2^40`, and direct division gives
`B*=6`.  This is an admissible prime-field row.

For rate `1/4`, the quotient-core counts at quotient orders four and eight
are

```text
binom(3,1)=3<=6,       binom(7,2)=21>6.
```

Thus `N*=8` is the first spending scale.  Write

```text
ell=n/N*=1024,
sigma=ell-1=1023,
J=(1-rho)N*=6.
```

The planted crossing has a core of size `k-1`, `J` petals of size `ell`,
and one background point because

```text
n-k+1=J*ell+1.
```

Its `J=6` distinct nonzero labels print six distinct planted polynomials,
so the W3 residual allowance is `B*-J=0`.

## Fiber construction

Let `omega` generate the order-`n` subgroup `H`.  Put `d=256`.  The map
`x -> x^d` has fibers of size `d` on `H`; write `F_z` for the fiber with
value `z`.  Select pairwise distinct fiber values

```text
z_c, z_0, z_1,...,z_J.
```

Choose the core `C` to contain the whole fiber

```text
D=F_(z_c)
```

and to avoid `F_(z_1),...,F_(z_J)`.  Choose the unique background point
inside `F_(z_0)` and outside `C`.  This is possible because `n/d=32`, while
only eight fiber classes are reserved.  Partition the remaining noncore
points into `J` petals of size `ell`, placing `F_(z_i)` inside petal `i`.

Give petal `i` the label

```text
a_i=(z_i-z_0)/(z_i-z_c).
```

These labels are nonzero and pairwise distinct because the displayed
fractional-linear map is injective away from `z_c` and sends only `z_0` to
zero.

The locator of `D` is `L_D(X)=X^d-z_c`.  Define

```text
g(X)=L_(C\D)(X)(X^d-z_0).
```

It has degree

```text
(k-1-d)+d=k-1<k.
```

It agrees with the planted receiver in three disjoint places:

1. on every point of `C\D`, where both values are zero;
2. on the background point in `F_(z_0)`, where `g` is zero; and
3. on all `d` points of every selected fiber `F_(z_i)`, because

```text
g(x)
 =L_(C\D)(x)(z_i-z_0)
 =a_i L_(C\D)(x)(z_i-z_c)
 =a_i L_C(x).
```

Therefore its agreement count is at least

```text
(k-1-d)+1+Jd
 = k+(J-1)d
 = 3328
 > k+sigma=3071.
```

Finally, `g` is not one of the planted polynomials.  Equality
`g=a_iL_C` would imply the polynomial identity

```text
X^d-z_0=a_i(X^d-z_c).
```

The leading coefficient would force `a_i=1`, and the constant coefficient
would then force `z_0=z_c`, a contradiction.  The list consequently contains
the six plants and the additional polynomial `g`, proving
`|List(U)|>=7>B*`.

## General mechanism

The construction only needs a power-of-two divisor `d|n` satisfying

```text
(J-1)d>=ell-1,       d<=min(ell,k-1),       n/d>=J+2.
```

Thus the failure of the all-cell extension is structural: arbitrary allowed
layouts can align the petals with fibers of a reduced rational pencil.
Increasing a numerical search cap or changing the former `K_cell` constant
cannot make that stronger extension true. The literal safe-side W3 claim is
outside this construction's scope.
