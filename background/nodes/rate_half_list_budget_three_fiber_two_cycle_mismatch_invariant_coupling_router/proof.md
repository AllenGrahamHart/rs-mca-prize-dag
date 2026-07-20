# Proof

The cycle router supplies the exact root inventory. In the `c=2` stratum,
two roots `A,B` of `D_*` are the squares of two antipodal completion pairs;
the other two roots are residual exceptional-pair squares. Hence the source
set is `{a,-a,b,-b}` with `a^2=A`, `b^2=B`, and its binary quartic is `f_2`
in `(MIC5)`. Substitution of its coefficients

```text
(a,b,c,d,e)=(1,0,-A-B,0,AB)
```

in `(MIC3)` gives the displayed `I_2,J_2`. The source pair is an unordered
two-subset of four denominator roots, giving six candidates.

In the `c=1` stratum, one denominator root `A` is the square of the unique
antipodal completion pair, one root `C` comes from the residual exceptional
pair, and the remaining two roots `B,D` are squares of the two unpaired
completion roots. If those roots are `b,d`, put

```text
u=bd,       s=b+d,       u^2=BD,       s^2=B+D+2u.    (1)
```

The source set `{a,-a,b,d}` has binary quartic `f_1` in `(MIC7)`, with
coefficients

```text
(a,b,c,d,e)=(1,-s,u-A,As,-Au).                       (2)
```

Substitute `(1)--(2)` in `(MIC3)`. Direct expansion gives

```text
I=A^2+u^2+3A(B+D)-8Au,
J=2(A-u)(A^2+u^2+16Au-9A(B+D)).                      (3)
```

Using `u^2=BD` proves `(MIC7)`. The ordered choice `(A,C)` has `4*3`
possibilities and `u^2=BD` has two roots. The two values of `s` differ by
global negation of the source set, so the count is 24 rather than 48.

It remains to prove the scalar PGL criterion. Under a linear fractional
change of variables, `I` and `J` have weights four and six. Consequently
`[I^3:J^2]` is an invariant of an unordered four-point set. Completeness is
elementary. Over the algebraic closure, send three ordered points to
`infinity,0,1` and write the fourth as `lambda`, with
`lambda!=0,1`. The corresponding quartic is

```text
XZ(X-Z)(X-lambda Z),
```

and `(MIC3)` gives

```text
I=lambda^2-lambda+1,
J=(lambda-2)(lambda+1)(2lambda-1),
4I^3-J^2=27lambda^2(lambda-1)^2.                     (4)
```

For two parameters `lambda,mu`, equality of `[I^3:J^2]`, together with
`(4)`, is equivalent to equality of

```text
(lambda^2-lambda+1)^3/(lambda^2(1-lambda)^2).
```

After clearing the nonzero denominators, the difference factors as

```text
(lambda-mu)(lambda mu-1)(lambda+mu-1)
*(lambda mu-lambda+1)(lambda mu-lambda-mu)
*(lambda mu-mu+1).                                   (5)
```

The six factors are exactly the six anharmonic transforms of `lambda`.
Thus `(MIC8)` is also sufficient for an unordered PGL matching, including
the harmonic and equianharmonic special values. The official characteristic
exceeds three, and both quartics are separable, so no denominator or
inseparability exception occurs.

For an actual cycle survivor, all completion roots and outer roots lie in
the base field. Once `(MIC8)` selects an anharmonic matching, the unique
fractional-linear map between any three matched points has base-field
coefficients and sends the fourth point correctly. This proves the
reconstruction statement and all claims. QED.
