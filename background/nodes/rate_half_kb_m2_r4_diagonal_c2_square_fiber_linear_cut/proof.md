# Proof

Let the two source points over `w` be `x` and `-x`. The two quadratic stars
are

```text
H(T,x)=U(T,w)+xV(T,w),
H(T,-x)=U(T,w)-xV(T,w).                             (1)
```

The square-fiber theorem says that both reduced stars have the same two
roots `J_1`, so both are nonzero scalar multiples of `q=P_(J_1)`.

## 1. Unramified rank

In the unramified case `x!=0`. Adding and subtracting the two identities in
`(1)` proves `(KBC2-2)`, since the characteristic is odd. The wedge equations
`(KBC2-3)` are exactly the condition that each three-vector of coefficients
lies in the line spanned by the nonzero vector `(q_0,q_1,q_2)`.

Write the reciprocal forms as

```text
u_0=a+bW+cW^2,
u_1=d+eW+epsilon*dW^2,
u_2=epsilon*(c+bW+aW^2),

v_0=f+gW,
v_1=h*(1+epsilon*W),
v_2=epsilon*(g+fW),                                (2)
```

where `e` is free for `epsilon=+1` and is zero for `epsilon=-1`. For
`w!=0,+1,-1`, evaluation of `(u_0,u_1,u_2)` at `w` has rank three. Indeed,
the first and third rows in the variables `(a,b,c)` are independent unless
`w^2=1`, while the middle row has a nonzero coefficient in `(d,e)`.
Evaluation of `(v_0,v_1,v_2)` has determinant

```text
epsilon*(1-w^2)*(1+epsilon*w),                     (3)
```

and is therefore also an isomorphism. Requiring a surjective three-vector
to lie in the fixed line `<q>` has codimension two. The `U` and `V`
variables are disjoint, so the total rank is four. Subtracting four from
the ambient dimensions eight and seven proves `(KBC2-4)`.

## 2. Minor factorization

The reciprocal identities imply

```text
W^3 m_12(1/W)=-m_01(W),
W^3 m_02(1/W)=-m_02(W).                            (4)
```

All three minors vanish at `w` by `(KBC2-2)`. Equations `(4)` make them
vanish at `w^(-1)` as well, so each is divisible by the reciprocal quadratic
`chi_w`. Since every minor has degree at most three, the quotients are
linear. Write `m_12=chi_w(AW+B)`. The first identity in `(4)` gives
`m_01=-chi_w(BW+A)`. If `m_02=chi_w(CW+D)`, the second identity gives
`D=-C`. This is `(KBC2-5)`.

## 3. Ramification

The ramified fibers of `W=X^2` are `0` and infinity, exchanged by
`W->1/W`. At `X=0`, both points in the degree-two fiber are the same and

```text
H(T,0)=U(T,0),       G(T,0)=U(T,0)^2.              (5)
```

Thus the printed square root forces only `(KBC2-6)`. Evaluation
`U -> U(T,0)` is surjective in both signs by `(2)`, so membership in `<q>`
has rank two. The `V` variables remain free, leaving dimensions
`(5-2)+3=6` and `(4-2)+3=5`. The argument at infinity is the reciprocal
one and uses the `W^2` coefficient of `U`. Since `V` is unconstrained,
neither proportionality of `U,V` nor the minor factorization can be asserted.
QED.
