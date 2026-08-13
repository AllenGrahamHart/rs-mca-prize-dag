# Proof

## Rational points on non-base-field components

Work over an algebraic closure of `K=F(X)` and factor the radical of `P`
as

```text
rad(P)=product_i R_i,       delta_i=deg_(Y,Z)(R_i),
sum_i delta_i<=d.
```

The deployed Mersenne field has characteristic `p=2147483647>d`.  Hence
no component field of definition can carry a nontrivial purely inseparable
degree: such a degree would be a positive power of `p` and would force at
least that much geometric degree in the `K`-polynomial containing the
component.

Suppose `R_i` is not individually defined over `K`.  Its field of
definition is therefore separable over `K`, so some `K`-automorphism
`sigma` has `sigma(R_i)!=R_i`.  Every `K`-rational point `z` on
`R_i` also lies on `sigma(R_i)`: apply `sigma` to `R_i(z)=0`.
The two distinct irreducible plane curves have the same degree
`delta_i`, so Bezout gives at most `delta_i^2` such points.

Assign every selected pair outside the union of the `K`-defined components
to one non-`K` component containing it.  The number assigned is at most

```text
sum_(R_i not over K) delta_i^2
 <= (sum_i delta_i)^2
 <= d^2.                                           (FD1)
```

## Uniform retained mass

The factor-mass theorem gives `t_d=7583-(52-d)^2` selected pairs on
`P`.  By (FD1), at least

```text
t_d-d^2=4879+104d-2d^2                            (FD2)
```

lie on components individually defined over `K`.  The right side is
concave in `d`, so its minimum on `2<=d<=43` is at an endpoint:

```text
d=2:  5079,             d=43: 5653.
```

This proves the uniform lower bound `5079`.  There are at most `d`
geometric components, so one `K`-defined absolutely irreducible component
contains at least

```text
ceil((t_d-d^2)/d)>=132,                            (FD3)
```

where exact enumeration of `2<=d<=43` puts the minimum at `d=43`.

## Received-point concentration

Let `P_K` be the product of the `K`-defined components, represented
primitively after clearing denominators.  Every one of the at least `5079`
retained polynomial pairs lies identically on `P_K`.  Their inside cores
have size at least `807` and pairwise intersections at most five.  The
same incidence inequality as before gives

```text
ceil(5079*807^2/(807+5*(5079-1)))=126263.          (FD4)
```

Therefore at most `130237-126263=3974` inside coordinates are exceptional
to the base-field component union.
