# Proof

Put `V=z^H C` and `F=-B/V`.  The canonical-cell dependency gives
`gcd(B,V)=1`, exact rational degree

```text
deg F=r=2H-3,                                        (1)
```

and identifies `F(x^(-1))` with the outer label of the cell containing
`x`.

Assume first that the four barycentric weights are distinct.  At every
ordinary mismatch zero `x notin {+1,-1}`, neither `x` nor `-x` can be one of
the unmatched deleted points: one side would have coloring value zero and
the other a nonzero `lambda_i`.  Thus both points have cell labels.  Equality
`u(x)=0` and distinctness of the weights force those labels to agree, so
`z=x^(-1)` is a root of

```text
D(z)=B(z)V(-z)-B(-z)V(z).                            (2)
```

The leading terms in `(2)` cancel and

```text
deg D<=2r-1=4H-7.                                    (3)
```

The polynomial `D` is nonzero.  Otherwise `F(-z)=F(z)`, so `F` would lie in
the fixed field `F_q(z^2)` and have even degree, contradicting the odd exact
degree `(1)`.

Let `Z` be the number of ordinary mismatch zeros.  Equation `(2)` gives
`Z<=4H-7`.  The zero set is stable under `x -> -x` and has no fixed point in
odd characteristic, so `Z` is even and in fact

```text
Z<=4H-8.                                             (4)
```

The support compiler says that `+1,-1` are the remaining automatic zeros.
Using `N=8H-8`, equation `(4)` yields

```text
|supp u|=N-2-Z>=8H-10-(4H-8)=4H-2,                  (5)
```

which proves the first branch.

Suppose now that the weights are not all distinct.  The barycentric moment
identities are

```text
sum_i lambda_i w_i^j=0,       0<=j<=2.               (6)
```

The normalized gap compiler gives `alpha!=0`.  The same elementary
classification as in the minimum-support collision proof uses only `(6)`
and this nonvanishing: a triple equality forces the fourth root to zero and
then `alpha=0`; two equal pairs force both root pairs to be antipodal and
make the reciprocal derivative weights opposite rather than equal; four
equal weights contradict the `j=0` equation.  Therefore exactly one pair is
equal.

For its roots `w_i,w_j`, put `s=w_i+w_j`.  The equality
`Phi'(w_i)=Phi'(w_j)` gives their product `s^2+alpha/2`.  The complementary
pair has sum `-s` and product `alpha/2`.  Expanding the two quadratics proves
`(CHR3)--(CHR4)` and `s!=0` follows from separability.

Substitution in the binary-quartic invariants gives

```text
I=2alpha^2(3y+2),
J=-alpha^3(3y-4)(3y+2)^2.                            (7)
```

The completion coupling therefore becomes

```text
32z(z-36)^2=(3y-4)^2(3y+2)(z+12)^3.                 (8)
```

Direct expansion factors the difference of the two sides as

```text
-27[y(z+12)-2z+8]([y(z+12)-16]^2-64z).              (9)
```

At `z=-12` the two factors are nonzero.  Their common zeros are exactly
`(0,4)` and `(4/3,36)`, proving the disjoint convention in `(CHR5)`.

The torsion-field dependency lets us write `z=x^2` over the base field.  The
two discriminants of `(CHR4)` are

```text
Delta_1=-alpha(3y+2),       Delta_2=alpha(y-2).      (10)
```

On `L`, they are `4kappa x^2,16kappa`; on either square-root sign of `Q`,
they are `kappa(x+6epsilon)^2,kappa(x-2epsilon)^2`.  Separability makes the
displayed square factors nonzero.  Since both quadratics split, `(10)` is
equivalent to `kappa` being a nonzero square, proving `(CHR6)`.

If the selected pair is antipodal, then `z=0`.  The `L` value `y=-2/3`
violates separability, while `Q` gives `y=4/3`.  Equations `(CHR3)` and `(7)`
give `(CHR7)`, and the quotient of the squares `alpha/3=(s/2)^2` and
`-alpha/6` proves that `-2` is square.  None of these arguments used the size
of `supp u` after entering the collision branch.  This completes the
dichotomy. QED.
