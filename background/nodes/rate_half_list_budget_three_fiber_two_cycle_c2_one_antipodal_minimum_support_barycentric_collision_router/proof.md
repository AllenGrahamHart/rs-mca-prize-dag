# Proof

Write `V=z^H C` and

```text
F(z)=-B(z)/V(z).
```

At a root `z=a^(-1)` of the cell factor `G_i=B+w_iV`, pairwise coprimality
of the four `G_i` makes `V(z)` nonzero, and hence `F(z)=w_i`.  Moreover
`gcd(B,V)=1`, every `G_i` has exact degree `r=2H-3`, and therefore the exact
degree of the rational map `F` is `r`.

Assume minimum support.  By `(BSP5)`, the compiler polynomial has exactly
`5H-11` distinct roots in `mu_N`, none equal to `+1` or `-1`.  At their
inverse points the barycentric mismatch vanishes.  Besides `+1` and `-1`,
the four points `c,d,-c,-d` cannot be mismatch zeros: exactly one deleted
pair is antipodal, while every `lambda_i` is nonzero.  Thus at every one of
these `5H-11` ordinary points the cell labels at `a` and `-a` have equal
barycentric weights.

Suppose first that the four `lambda_i` are distinct.  Equality of weights
then means equality of cell labels, so all `5H-11` roots annihilate

```text
D(z)=B(z)V(-z)-B(-z)V(z).                            (1)
```

The degree of `D` is at most `2r-1`: if both inputs have degree `r`, their
top terms cancel, and otherwise the bound is immediate.  But

```text
5H-11 > 2r-1=4H-7
```

because the official `H` is greater than four.  Hence `D=0` and
`F(-z)=F(z)`.  In odd characteristic the fixed field of `z -> -z` is
`F(z^2)`, so every nonconstant invariant rational map has even degree.  This
contradicts the odd exact degree `r=2H-3`.  A minimum-support survivor must
therefore have a repeated barycentric weight.

It remains to compile that repetition into outer coefficients.  Suppose
`lambda_i=lambda_j`, and put

```text
s=w_i+w_j,       p=w_iw_j.
```

Since the roots are distinct and `Phi` is separable, equality of the
reciprocal derivative weights is equivalent to
`Phi'(w_i)=Phi'(w_j)`.  From `(BCR1)`,

```text
0=(Phi'(w_i)-Phi'(w_j))/(w_i-w_j)
 =4(w_i^2+w_iw_j+w_j^2)+2alpha.
```

Consequently `p=s^2+alpha/2`.  The complementary pair has sum `-s` and,
because the total quadratic coefficient is `alpha`, product `alpha/2`.
Comparing its cubic and constant coefficients gives

```text
beta=-s^3,
gamma=(s^2+alpha/2)(alpha/2).
```

These are `(BCR2)`, give the two factorizations in `(BCR4)`, and, after
cubing the second relation and using `s^6=beta^2`, prove `(BCR3)`.  The
normalized primary gap supplies `alpha=4c!=0`.  Also `s!=0`, since `s=0`
would make the two quadratic factors in `Phi` equal and contradict
separability.

We next exclude every larger collision class.  Suppose first that
`lambda_1=lambda_2=lambda_3=a` and `lambda_4=b`.  The barycentric identities
through degree two give

```text
sum_i lambda_i w_i^m=0,       m=0,1,2.               (2)
```

The case `m=0` says `b=-3a`.  Since `sum_i w_i=0`, the case `m=1` becomes
`-4aw_4=0`, so `w_4=0`.  The case `m=2` then says that the three remaining
roots have both sum and second elementary symmetric function zero.  They
are the distinct nonzero roots of `T^3-q`.  Thus `alpha=gamma=0`, which
contradicts the normalized primary-gap identity `alpha=4c!=0`.

If instead the weights form two equal pairs `a,a,b,b`, their sum gives
`b=-a`.  If `s` is the sum of the roots in the first pair, the complementary
sum is `-s`, and the first weighted identity is `2as=0`.  Hence `s=0`, both
root pairs are antipodal, and `Phi` is even.  Its derivative is odd, so the
weights at opposite roots are negatives rather than equal, a contradiction.
Four equal nonzero weights contradict `sum_i lambda_i=0` directly.  The
collision is therefore exactly one pair.

Finally put `y=s^2/alpha`.  Substitution of `(BCR2)` into the normalized
binary-quartic invariants gives

```text
I=2alpha^2(3y+2),
J=-alpha^3(3y-4)(3y+2)^2.                            (3)
```

The outer quartic is separable, so `I` and `J` cannot both vanish; by `(3)`,
`3y+2!=0`.  Substitute `(3)` into the completion-root coupling

```text
4I^3 z_t(z_t-36)^2-J^2(z_t+12)^3=0
```

and divide by the nonzero factor `alpha^6(3y+2)^3`.  The result is exactly
the normalized curve `(BCR5)`. QED.
